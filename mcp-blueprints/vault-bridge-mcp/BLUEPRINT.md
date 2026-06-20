# Agy-MCP Blueprint: Vault Bridge MCP 🔐

This MCP server acts as a secure bridge to HashiCorp Vault, providing secret retrieval, creation, namespace administration, and secret access audits.

## 1. Architectural Overview

The Vault Bridge MCP connects local sessions to HashiCorp Vault API endpoints, strictly separating namespaces.

```mermaid
graph TD
    Agent([Agent / Client]) -->|JSON RPC| MCP[Vault Bridge MCP]
    MCP -->|AppRole / TLS Auth| Vault[(HashiCorp Vault)]
```

## 2. Setup Requirements

- **Runtime:** Node.js >= 18 or Python >= 3.10
- **Vault:** HashiCorp Vault reachable on the network.

## 3. Environment Configuration (`.env.example`)

Inject AppRole credentials or tokens using project environment bindings:
```env
# 🔐 VAULT INTEGRATION
VAULT_ADDR=https://vault.internal.network:8200
VAULT_ROLE_ID=${VAULT_ROLE_ID}
VAULT_SECRET_ID=${VAULT_SECRET_ID}
```

## 4. Least Privilege Design

- **Namespace Scope:** AppRole access is restricted to specific namespaces (`dev`, `staging`, `production`).
- **Input Validation:** Key paths enforce strict alphanumeric and slash/hyphen pattern checks.

## 5. Atomic Write Strategy

- Secret updates (`put_secret`) are handled atomically by Vault's backend.

## 6. Deployment / Verification Plan

Deploy using node:
```json
{
  "mcpServers": {
    "vault-bridge": {
      "command": "node",
      "args": ["dist/vault_bridge_mcp.js"]
    }
  }
}
```
Verify by calling `list_secrets` on a non-production path.
