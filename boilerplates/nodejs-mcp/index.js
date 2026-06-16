#!/usr/bin/env node

/**
 * Node.js Model Context Protocol (MCP) Server Boilerplate
 * Enforces security-first practices: parameterized commands, no hardcoded secrets, and no raw shell execution.
 */

const { Server } = require("@modelcontextprotocol/sdk/server/index.js");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio.js");
const { 
  CallToolRequestSchema, 
  ListToolsRequestSchema 
} = require("@modelcontextprotocol/sdk/types.js");

// Initialize server metadata
const server = new Server(
  {
    name: "nodejs-mcp-boilerplate",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Define available tools
const TOOLS = [
  {
    name: "secure_calculate",
    description: "Performs mathematical calculations securely on input parameters.",
    inputSchema: {
      type: "object",
      properties: {
        operation: {
          type: "string",
          enum: ["add", "subtract", "multiply", "divide"],
          description: "Math operation to perform"
        },
        a: {
          type: "number",
          description: "First operand"
        },
        b: {
          type: "number",
          description: "Second operand"
        }
      },
      required: ["operation", "a", "b"]
    }
  }
];

// Register tools list request handler
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: TOOLS
  };
});

// Register tool invocation handler
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "secure_calculate") {
    const { operation, a, b } = args;
    
    switch (operation) {
      case "add":
        return { content: [{ type: "text", text: String(a + b) }] };
      case "subtract":
        return { content: [{ type: "text", text: String(a - b) }] };
      case "multiply":
        return { content: [{ type: "text", text: String(a * b) }] };
      case "divide":
        if (b === 0) {
          return {
            isError: true,
            content: [{ type: "text", text: "Error: Division by zero" }]
          };
        }
        return { content: [{ type: "text", text: String(a / b) }] };
      default:
        throw new Error(`Unsupported operation: ${operation}`);
    }
  }

  throw new Error(`Tool not found: ${name}`);
});

// Connect to stdio transport and start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Node.js MCP Boilerplate Server running on stdio transport");
}

main().catch((error) => {
  console.error("Fatal error starting server:", error);
  process.exit(1);
});
