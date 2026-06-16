# Terminal-MCP Blueprint 💻

`terminal-mcp` provides a secure shell interface for AI assistants to run system diagnostics, check active configurations, and compile projects, enforcing strict shell parameter sanitization.

## 📁 Structure

* **`BLUEPRINT.md`**: This manual.
* **`schemas/`**: JSON tool definition files.

## 🚀 Capabilities

1. **Run Command (`run_command`)**: Runs workstation-level commands using array-based argument spawns (no raw string evaluations).
2. **Read Environment (`get_env_variables`)**: Queries active system environment variables without printing secrets.
3. **OS Diagnostics (`get_os_info`)**: Inspects shell architectures, paths, and platform versions.

---

## 🔒 Security & Deployment Configuration

### 🛡️ Shell Parameter Hardening
All commands executed through this connector must bypass raw command processors (e.g. `cmd /c` or `bash -c`) where user-supplied inputs could lead to command injections. 

- **Incorrect Integration**:
  ```javascript
  exec(`npm install ${package_name}`);
  ```
- **Correct Integration**:
  ```javascript
  spawn('npm', ['install', package_name]);
  ```

### `mcp_config.json` Snippet
```json
{
  "mcpServers": {
    "terminal-mcp": {
      "command": "node",
      "args": [
        "${TERMINAL_MCP_DIR}/build/index.js"
      ],
      "env": {
        "PAGER": "cat",
        "ALLOWED_COMMAND_PREFIXES": "git,npm,pytest,phpunit,docker"
      }
    }
  }
}
```
