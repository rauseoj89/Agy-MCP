# Agy-MCP Blueprint: SearXNG Web Search MCP 🔍

This MCP server connects AI agents to a locally hosted or network SearXNG instance for privacy-respecting, customizable web search operations.

## 1. Architectural Overview

```mermaid
graph TD
    Agent([Agent / Client]) -->|JSON-RPC via Stdio| MCP[SearXNG MCP Server]
    MCP -->|HTTP GET /search| SearXNG[(SearXNG Engine - ${SEARXNG_URL})]
```

## 2. Setup Requirements

- **Runtime:** Node.js >= 18 (ES Modules)
- **Dependencies:** `@modelcontextprotocol/sdk`, `axios`, `zod`
- SearXNG must have JSON format enabled in its `/etc/searxng/settings.yml`:
  ```yaml
  search:
    formats:
      - html
      - json
  ```

## 3. Environment Configuration (`.env.example`)

```env
# URL pointing to local or network SearXNG instance
SEARXNG_URL=http://localhost:8080
```

## 4. Least Privilege Design

- **Read-Only Protocol:** Only exposes read-only search operations (`HTTP GET /search`).
- **Internal Network Scoping:** SearXNG instance should be bound to `localhost` or private internal network interfaces.
- **Input Bounds:** Search queries are limited to 500 characters; pagination is strictly validated.

## 5. Atomic Write Strategy

- Search results are streamed directly as structured JSON to the agent session; no disk persistence is performed.

## 6. Multi-Agent Deployment & Verification Plan

### ▶️ If you are on Antigravity / Hermes Agent:
Configure in `mcp_config.json`:
```json
{
  "mcpServers": {
    "searxng": {
      "command": "node",
      "args": ["./mcps/searxng/index.js"],
      "env": {
        "SEARXNG_URL": "http://localhost:8080"
      }
    }
  }
}
```

### ▶️ If you are on Cline / Roo Code / OpenCode:
```json
{
  "mcpServers": {
    "searxng": {
      "command": "node",
      "args": ["./mcps/searxng/index.js"],
      "env": {
        "SEARXNG_URL": "http://localhost:8080"
      }
    }
  }
}
```

### ⚠️ If you do NOT have MCP support (Fallback):
- Query SearXNG directly via browser or `curl -s "${SEARXNG_URL}/search?q=<query>&format=json"`.

Verify installation by calling `web_search` with query `"test"`.

---
**Author:** JimmyR  
**Powered by:** AntigravityAI
