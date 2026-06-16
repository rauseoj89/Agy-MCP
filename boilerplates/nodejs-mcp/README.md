# Node.js MCP Server Boilerplate

This directory contains a clean, production-ready template for building custom Model Context Protocol (MCP) servers using Node.js. It follows standard security-first development practices, isolating command execution parameters and ensuring zero raw credentials or IP leaks.

## 🚀 Getting Started

### 1. Install Dependencies
Run npm install in this folder to install the required MCP SDK:
```bash
npm install
```

### 2. Implement Your Tools
Open `index.js` and edit the `TOOLS` catalog and the request handlers.
- **ListToolsRequestSchema**: Registers the schemas, descriptions, and expected parameters.
- **CallToolRequestSchema**: Contains the execution logic for each registered tool.

### 3. Connect to Your Assistant
Configure your environment using the local `mcp_config.json` schema, specifying the path to this folder dynamically:

```json
{
  "mcpServers": {
    "my-custom-mcp": {
      "command": "node",
      "args": [
        "${CUSTOM_MCP_DIR}/index.js"
      ],
      "env": {
        "CUSTOM_SECRET": "${VAULT_SECRET_CUSTOM_KEY}"
      }
    }
  }
}
```

## 🔒 Security Requirements
All custom tools built from this template must adhere to the central security guidelines:
1. **Parameterized Queries**: If interacting with databases, always parameterize inputs.
2. **Array-based Execution**: If running external commands, never use `exec` with concatenated strings; always use `spawn` with array-based arguments.
3. **Redact Logs**: Ensure that error exceptions catch raw stack traces, log them locally, and return generic references to the client.
