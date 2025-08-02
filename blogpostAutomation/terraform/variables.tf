variable "resource_group_name" {
  description = "Name of the Azure resource group"
  type        = string
  default     = "rg-blogpost-automation"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "North Europe"
}

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "blogpost-automation"
}

variable "function_app_name" {
  description = "Name of the Azure Function App"
  type        = string
  default     = "func-blogpost-automation"
}

variable "storage_account_name" {
  description = "Name of the storage account"
  type        = string
  default     = "stblog"
}

variable "key_vault_name" {
  description = "Name of the Azure Key Vault"
  type        = string
  default     = "kv-blogpost-automation"
}

variable "app_service_plan_sku" {
  description = "SKU for the App Service Plan"
  type        = string
  default     = "Y1"
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default = {
    Environment = "dev"
    Project     = "BlogPostAutomation"
    ManagedBy   = "Terraform"
  }
}

variable "allowed_ip_ranges" {
  description = "IP ranges allowed to access the Function App"
  type        = list(string)
  default     = ["0.0.0.0/0"] # Restrict this in production
}

variable "function_timeout" {
  description = "Function execution timeout in seconds"
  type        = number
  default     = 600
}

variable "daily_trigger_schedule" {
  description = "CRON expression for daily trigger"
  type        = string
  default     = "0 0 9 * * *" # 9 AM UTC daily
}