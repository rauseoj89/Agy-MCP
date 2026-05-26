#🛡️ Agy-MCP : Hardened Blueprints for Local MCP Workflows

![Agy-MCP Banner](agy_mcp_cover.png)

Agy-MCP is a centralized, self-documenting library of **Model Context Protocol (MCP)** blueprints, schemas, and configurations. It is designed similarly to `Agy-Skills`, housing complete descriptions and instructions for all custom tools and integrations used by AI coding assistants (like Antigravity) to manage and interact with home server infrastructure securely.


---

## 📁 Repository Structure

All MCP server blueprints are located under `mcp-blueprints/`, categorized by server name.

```
Agy-MCP/
├── mcp-blueprints/
│   ├── nas-tools/             # Blueprint for NAS systems and shell automation
│   │   ├── BLUEPRINT.md       # Architectural guides and instructions
│   │   ├── schemas/           # Reusable JSON schema templates
│   │   └── templates/         # Configuration snippets (.env.example, etc.)
│   │
│   └── postgres-mcp/          # Blueprint for secure Postgres DB operations
│       ├── BLUEPRINT.md
│       ├── schemas/
│       └── templates/
│
├── boilerplates/              # Quickstart code bases for new MCP developments
└── README.md                  # This main directory index
```

---

## 🔒 Security Principles

1. **Zero Raw Secrets:** Never commit real tokens, keys, passwords, or raw environment config files. Always use placeholders (`__SECRET__` or `VAULT_SECRET`) and point to a secure secrets manager (like Project Fortress Vault).
2. **Standardized Schemas:** Tools schemas must be pure JSON and easily reusable across development environments.
3. **AppRole Least Privilege:** Any blueprint utilizing system credentials should outline exact HCL security policies rather than root keys.
