# 🛡️ Agy-MCP: Hardened Blueprints for Local MCP Workflows

![Agy-MCP Banner](agy_mcp_cover.png)

Agy-MCP is a centralized, self-documenting library of **Model Context Protocol (MCP)** blueprints, schemas, and configurations. It is designed to house complete architectural specifications, operational runbooks, and strict JSON Schemas for all tools and integrations used by AI coding assistants to manage workflows and server infrastructure safely.

---

## 📁 Repository Structure

All MCP server blueprints are located under `mcp-blueprints/`, categorized by server name.

```
Agy-MCP/
├── mcp-blueprints/
│   ├── browser-tools-mcp/     # Browser automation, visual validation & Lighthouse audits
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── data-analyst-mcp/      # 11-tool Universal Data & Document Processing Suite
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── filesystem-mcp/        # Sandboxed local filesystem read, write, list and search
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── git-mcp/               # Workspace git operations with conventional-commit gates
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── markitdown-mcp/        # PDF/Word/Excel/Audio conversion to Markdown
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── nas-tools/             # Blueprint for NAS systems, ZFS, and container automation
│   │   ├── BLUEPRINT.md
│   │   └── templates/
│   │
│   ├── office-mcp/            # 5-tool Office Authoring (Word, Excel, PowerPoint, PDF)
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── postgres-mcp/          # Secure PostgreSQL DB query & schema explorer
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── searxng-mcp/           # Privacy-respecting web search via local SearXNG engine
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── terminal-mcp/          # Validated subprocess shell command executor
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   ├── vault-bridge-mcp/      # Secrets bridge to HashiCorp Vault
│   │   ├── BLUEPRINT.md
│   │   └── schemas/tools.json
│   │
│   └── web-search-mcp/        # Web search querying and content citation extraction
│       ├── BLUEPRINT.md
│       └── schemas/tools.json
│
├── boilerplates/              # Quickstart code bases for new MCP developments
└── README.md                  # This main directory index
```

---

## 🧩 Blueprint Catalog & Capabilities

| Blueprint Server | Runtime | Tools Count | Primary Scope & Capabilities |
| :--- | :--- | :---: | :--- |
| **`browser-tools-mcp`** | Node.js | 4 | Browser automation, visual regressions, DOM inspection, and Lighthouse audits |
| **`data-analyst-mcp`** | Node.js | 11 | Multi-format ingestion (CSV, Excel, PDF, Word, PPTX, HTML, Logs), data hygiene, stats metrics, and image OCR |
| **`filesystem-mcp`** | Node.js / npx | 6 | Sandboxed local filesystem operations (read, write, list, search, move) |
| **`git-mcp`** | Node.js / npx | 7 | Conventional-commit gated git status, branch, log, diff, commit, and push |
| **`markitdown-mcp`** | Python 3.12 | 1 | Multi-format document to Markdown conversion (PDF, Office, HTML, Audio) |
| **`nas-tools`** | Node.js | 8 | Hardware statistics, ZFS pool monitoring, Docker container controls, and shell checks |
| **`office-mcp`** | Node.js | 5 | Styled Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF (.pdf) generation & OOXML inspection |
| **`postgres-mcp`** | Node.js | 4 | Secure PostgreSQL schema exploration, table inspection, and parameterized queries |
| **`searxng-mcp`** | Node.js | 1 | Privacy-respecting web search via local or network SearXNG instance |
| **`terminal-mcp`** | Node.js | 2 | Sandboxed subprocess command execution with timeout and output guards |
| **`vault-bridge-mcp`** | Node.js | 5 | HashiCorp Vault KV v2 credential storage, retrieval, rotation, and audit logs |
| **`web-search-mcp`** | Node.js | 2 | Web search querying and structured citation extraction |

---

## 🔒 Security Principles (Hardened Vanilla)

1. **Zero Raw Secrets:** Never commit real tokens, keys, passwords, or raw environment config files. Always use placeholders (`${VAULT_SECRET_<NAME>}`) and point to a secure secrets manager.
2. **Input Validation Schemas:** Every blueprint must contain a `schemas/tools.json` file defining strict parameters, types, `maxLength`, pattern regex, `minimum`/`maximum`, and array bounds (`maxItems`) to reject malformed inputs at the protocol layer.
3. **Least Privilege Design:** Any blueprint utilizing system credentials should restrict access to designated namespaces (e.g. `dev`, `staging`, `production`) and limit actions (e.g., read-only by default for SQL databases, no force pushes for git).
4. **Atomic Write Strategy:** Write operations that mutate files must first write to a `.tmp` buffer file and atomically rename it to the target path.

---
**Author:** JimmyR  
**Powered by:** AntigravityAI
