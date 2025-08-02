# Key Vault for storing secrets
resource "azurerm_key_vault" "main" {
  name                       = "${var.key_vault_name}-${var.environment}-${random_string.suffix.result}"
  location                   = azurerm_resource_group.main.location
  resource_group_name        = azurerm_resource_group.main.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  soft_delete_retention_days = 7
  purge_protection_enabled   = false

  # Network ACLs
  network_acls {
    default_action = "Allow" # Change to "Deny" in production
    bypass         = "AzureServices"
    ip_rules       = var.allowed_ip_ranges
  }

  tags = var.tags
}

# Key Vault Access Policy for current user (for initial setup)
resource "azurerm_key_vault_access_policy" "current_user" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id

  secret_permissions = [
    "Get",
    "List",
    "Set",
    "Delete",
    "Recover",
    "Purge"
  ]
}

# Key Vault Access Policy for Function App (will be created after function app)
resource "azurerm_key_vault_access_policy" "function_app" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = azurerm_linux_function_app.main.identity[0].tenant_id
  object_id    = azurerm_linux_function_app.main.identity[0].principal_id

  secret_permissions = [
    "Get",
    "List"
  ]

  depends_on = [azurerm_linux_function_app.main]
}

# Placeholder secrets (these should be set manually or via pipeline)
resource "azurerm_key_vault_secret" "perplexity_api_key" {
  name         = "perplexity-api-key"
  value        = "placeholder-value" # Set this manually after deployment
  key_vault_id = azurerm_key_vault.main.id

  depends_on = [azurerm_key_vault_access_policy.current_user]

  lifecycle {
    ignore_changes = [value]
  }
}

resource "azurerm_key_vault_secret" "telegram_bot_token" {
  name         = "telegram-bot-token"
  value        = "placeholder-value" # Set this manually after deployment
  key_vault_id = azurerm_key_vault.main.id

  depends_on = [azurerm_key_vault_access_policy.current_user]

  lifecycle {
    ignore_changes = [value]
  }
}

resource "azurerm_key_vault_secret" "telegram_chat_id" {
  name         = "telegram-chat-id"
  value        = "placeholder-value" # Set this manually after deployment
  key_vault_id = azurerm_key_vault.main.id

  depends_on = [azurerm_key_vault_access_policy.current_user]

  lifecycle {
    ignore_changes = [value]
  }
}

resource "azurerm_key_vault_secret" "git_access_token" {
  name         = "git-access-token"
  value        = "placeholder-value" # Set this manually after deployment
  key_vault_id = azurerm_key_vault.main.id

  depends_on = [azurerm_key_vault_access_policy.current_user]

  lifecycle {
    ignore_changes = [value]
  }
}

# Output Key Vault URL
output "key_vault_uri" {
  description = "URI of the Key Vault"
  value       = azurerm_key_vault.main.vault_uri
}