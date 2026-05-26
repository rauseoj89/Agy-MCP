# Vault-Bridge-MCP Blueprint 🛡️

`vault-bridge-mcp` acts as a secure connector between AI coding assistants and a HashiCorp Vault secrets management backend (Project Fortress). It manages access, creation, and rotation of project secrets using scoped AppRole permissions instead of raw root tokens.

## 📁 Structure

* **`BLUEPRINT.md`**: This manual.
* **`schemas/`**: JSON tool files for registration.
* **`templates/`**: Setup config snippets.

## 🚀 Capabilities

1. **Get Secret (`get_secret`)**: Safely retrieves a decrypted value from a project path in Vault.
2. **Put Secret (`put_secret`)**: Safely stores or updates a secret key-value pair under a specific project's path.
3. **List Secrets (`list_secrets`)**: Enumerates secret paths assigned to the authenticated namespace.
4. **Rotate Secret (`rotate_secret`)**: Integrates with target systems to update credentials and push the new values back to Vault dynamically.

---

## 🔒 Security & Deployment Configuration

### `mcp_config.json` Snippet
Connect your AI environment using this template, injecting your AppRole credentials securely:
```json
{
  "mcpServers": {
    "vault-bridge-mcp": {
      "command": "node",
      "args": [
        "P:/Infrastructure/Fortress/vault-bridge-mcp/build/index.js"
      ],
      "env": {
        "VAULT_ADDR": "http://192.168.1.10:8200",
        "VAULT_ROLE_ID": "__VAULT_ROLE_ID__",
        "VAULT_SECRET_ID": "__VAULT_SECRET_ID__",
        "VAULT_SECRET_MOUNT": "secret"
      }
    }
  }
}
```
