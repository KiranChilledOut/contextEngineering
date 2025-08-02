# MINIMAL COST VERSION - Only essential resources
terraform {
  required_version = ">= 1.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Get current client configuration
data "azurerm_client_config" "current" {}

# Random suffix for unique resource names
resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}

# Resource Group - FREE
resource "azurerm_resource_group" "main" {
  name     = "${var.resource_group_name}-${var.environment}"
  location = var.location
  tags     = var.tags
}

# Storage Account for Function App - ~$0.02/month
resource "azurerm_storage_account" "function_storage" {
  name                     = "${var.storage_account_name}${var.environment}01"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"

  tags = var.tags
}

# Consumption Plan (Y1) - FREE up to 1M executions
resource "azurerm_service_plan" "main" {
  name                = "asp-${var.project_name}-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "Y1" # Consumption plan - FREE tier
  tags                = var.tags
}

# Function App - FREE (runs on consumption plan)
resource "azurerm_linux_function_app" "main" {
  name                = "${var.function_app_name}-${var.environment}-${random_string.suffix.result}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  storage_account_name       = azurerm_storage_account.function_storage.name
  storage_account_access_key = azurerm_storage_account.function_storage.primary_access_key

  functions_extension_version = "~4"
  https_only                 = true

  # Managed Identity - FREE
  identity {
    type = "SystemAssigned"
  }

  site_config {
    application_stack {
      python_version = "3.11"
    }
    
    # Minimal settings for cost optimization
    always_on = false # Required for consumption plan
  }

  # Store secrets directly in app settings (less secure but FREE)
  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME" = "python"
    "PYTHON_ISOLATE_WORKER_DEPENDENCIES" = "1"
    
    # Environment variables (will be set later)
    "PERPLEXITY_API_KEY"          = ""
    "TELEGRAM_BOT_TOKEN"          = ""
    "TELEGRAM_CHAT_ID"            = ""
    "GIT_ACCESS_TOKEN"            = ""
    "GIT_REPO_URL"                = ""
    "GIT_BRANCH"                  = "main"
    "FUNCTION_TIMEOUT"            = "600"
    "DAILY_TRIGGER_SCHEDULE"      = "0 0 9 * * *"
    "ENVIRONMENT"                 = var.environment
    "LOGGING_LEVEL"               = "INFO"
  }

  tags = var.tags
}

# Outputs
output "resource_group_name" {
  description = "Name of the created resource group"
  value       = azurerm_resource_group.main.name
}

output "function_app_name" {
  description = "Name of the Function App"
  value       = azurerm_linux_function_app.main.name
}

output "function_app_url" {
  description = "URL of the Function App"
  value       = "https://${azurerm_linux_function_app.main.default_hostname}"
}