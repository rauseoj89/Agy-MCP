# Agy-MCP Blueprint: SearXNG Web Search MCP 🔍

This MCP server connects AI agents to a locally hosted or network SearXNG instance for privacy-respecting, customizable web search operations.

## 1. Architectural Overview

```mermaid
graph TD
    Agent([Agent / Client]) -->|JSON-RPC via Stdio| MCP[SearXNG MCP Server]
    MCP -->|HTTP GET /search| SearXNG[(SearXNG Engine - ${SEARXNG_URL})]
```

## 2. Setup & Installation

- **Runtime:** Node.js >= 18 (ES Modules)
- **Dependencies:** `@modelcontextprotocol/sdk`, `axios`, `zod`

```bash
cd /path/to/searxng-mcp
npm install
```

## 3. Server Requirement & Environment Configuration (`.env`)

SearXNG must have JSON format enabled in its `/etc/searxng/settings.yml`:
```yaml
search:
  formats:
    - html
    - json
```

Environment file (`.env`):
```env
# URL pointing to local or network SearXNG instance
SEARXNG_URL=http://localhost:8080
```

## 4. Client Manifest Example

```json
{
  "mcpServers": {
    "searxng": {
      "command": "node",
      "args": [
        "/path/to/searxng-mcp/index.js"
      ],
      "env": {
        "SEARXNG_URL": "http://localhost:8080"
      }
    }
  }
}
```

## 5. Tool Inventory

- **`web_search`**: Accepts a search `query`, optional `categories` (general, IT, science, news), and `pageno` for pagination.

---
**Author:** JimmyR  
**Powered by:** AntigravityAI

