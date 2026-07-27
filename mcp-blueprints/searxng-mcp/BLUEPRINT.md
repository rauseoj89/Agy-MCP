# Agy-MCP Blueprint: SearXNG Web Search MCP 🔍

This MCP server connects AI agents to a locally hosted SearXNG instance for privacy-respecting, customizable web search operations.

## 1. Architectural Overview

```mermaid
graph TD
    Agent([Agent / Client]) -->|JSON-RPC via Stdio| MCP[SearXNG MCP Server]
    MCP -->|HTTP GET /search| SearXNG[(SearXNG Engine - http://localhost:8080)]
```

## 2. Setup & Installation

- **Location:** `P:\Infrastructure\MCP\searxng`
- **Runtime:** Node.js >= 18 (ES Modules)
- **Dependencies:** `@modelcontextprotocol/sdk`, `axios`, `zod`

```powershell
cd P:\Infrastructure\MCP\searxng
npm install
```

## 3. Environment Configuration (`.env`)

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
        "P:/Infrastructure/MCP/searxng/index.js"
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
