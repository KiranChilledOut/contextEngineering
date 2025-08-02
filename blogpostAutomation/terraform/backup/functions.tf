# App Service Plan for Function App
resource "azurerm_service_plan" "main" {
  name                = "asp-${var.project_name}-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = var.app_service_plan_sku

  tags = var.tags
}

# Linux Function App
resource "azurerm_linux_function_app" "main" {
  name                = "${var.function_app_name}-${var.environment}-${random_string.suffix.result}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  storage_account_name       = azurerm_storage_account.function_storage.name
  storage_account_access_key = azurerm_storage_account.function_storage.primary_access_key

  functions_extension_version = "~4"
  https_only                 = true

  # Managed Identity
  identity {
    type = "SystemAssigned"
  }

  site_config {
    application_stack {
      python_version = "3.11"
    }

    # CORS configuration
    cors {
      allowed_origins = ["*"] # Restrict this in production
    }

    # Function App settings
    application_insights_connection_string = azurerm_application_insights.main.connection_string
    application_insights_key               = azurerm_application_insights.main.instrumentation_key

    # Security settings
    ftps_state                             = "FtpsOnly"
    minimum_tls_version                    = "1.2"
    scm_minimum_tls_version               = "1.2"
    use_32_bit_worker                     = false
    
    # Performance settings
    always_on                             = false # Not available for Consumption plan
    pre_warmed_instance_count            = 0
  }

  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME"     = "python"
    "PYTHON_ISOLATE_WORKER_DEPENDENCIES" = "1"
    
    # Key Vault references
    "PERPLEXITY_API_KEY"          = "@Microsoft.KeyVault(VaultName=${azurerm_key_vault.main.name};SecretName=perplexity-api-key)"
    "TELEGRAM_BOT_TOKEN"          = "@Microsoft.KeyVault(VaultName=${azurerm_key_vault.main.name};SecretName=telegram-bot-token)"
    "TELEGRAM_CHAT_ID"            = "@Microsoft.KeyVault(VaultName=${azurerm_key_vault.main.name};SecretName=telegram-chat-id)"
    "GIT_ACCESS_TOKEN"            = "@Microsoft.KeyVault(VaultName=${azurerm_key_vault.main.name};SecretName=git-access-token)"
    
    # Application settings
    "AZURE_KEYVAULT_URL"          = azurerm_key_vault.main.vault_uri
    "FUNCTION_TIMEOUT"            = var.function_timeout
    "DAILY_TRIGGER_SCHEDULE"      = var.daily_trigger_schedule
    "ENVIRONMENT"                 = var.environment
    
    # Git repository settings (these can be set as app settings or in Key Vault)
    "GIT_REPO_URL"                = "https://github.com/yourusername/blog-content.git"
    "GIT_BRANCH"                  = "main"
    
    # Logging
    "LOGGING_LEVEL"               = var.environment == "prod" ? "INFO" : "DEBUG"
    
    # Application Insights
    "APPINSIGHTS_INSTRUMENTATIONKEY" = azurerm_application_insights.main.instrumentation_key
    "APPLICATIONINSIGHTS_CONNECTION_STRING" = azurerm_application_insights.main.connection_string
  }

  # Network restrictions (optional)
  site_config {
    ip_restriction {
      ip_address = "0.0.0.0/0" # Restrict this in production
      action     = "Allow"
      priority   = 100
      name       = "AllowAll"
    }
  }

  tags = var.tags

  lifecycle {
    ignore_changes = [
      app_settings["WEBSITE_RUN_FROM_PACKAGE"]
    ]
  }
}

# Function App Slot for staging (optional)
resource "azurerm_linux_function_app_slot" "staging" {
  count           = var.environment == "prod" ? 1 : 0
  name            = "staging"
  function_app_id = azurerm_linux_function_app.main.id

  storage_account_name       = azurerm_storage_account.function_storage.name
  storage_account_access_key = azurerm_storage_account.function_storage.primary_access_key

  site_config {
    application_stack {
      python_version = "3.11"
    }
    application_insights_connection_string = azurerm_application_insights.main.connection_string
    application_insights_key               = azurerm_application_insights.main.instrumentation_key
  }

  app_settings = azurerm_linux_function_app.main.app_settings

  tags = var.tags
}

# Outputs
output "function_app_name" {
  description = "Name of the Function App"
  value       = azurerm_linux_function_app.main.name
}

output "function_app_url" {
  description = "URL of the Function App"
  value       = "https://${azurerm_linux_function_app.main.default_hostname}"
}

output "function_app_identity_principal_id" {
  description = "Principal ID of the Function App managed identity"
  value       = azurerm_linux_function_app.main.identity[0].principal_id
}