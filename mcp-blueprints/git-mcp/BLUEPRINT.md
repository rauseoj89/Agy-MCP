# Git-MCP Blueprint 🌿

`git-mcp` is an integration that connects AI agents to local Git repositories, enabling structured staging, status queries, diff audits, commits, and pushes through safe argument-based commands.

## 📁 Structure

* **`BLUEPRINT.md`**: This manual.
* **`schemas/`**: JSON tool definition files.
* **`templates/`**: Git hook setups and credentials.

## 🚀 Capabilities

1. **Git Status (`git_status`)**: Queries current modifications, untracked files, and branch states.
2. **Git Diff (`git_diff`)**: Compares active changes against HEAD or parent commits for security vetting.
3. **Git Stage (`git_add`)**: Stages files, ensuring directories containing credentials (like `CHG-Review/`) are excluded.
4. **Git Commit (`git_commit`)**: Creates new commits enforcing conventional commit messages.
5. **Git Push (`git_push`)**: Syncs local commits to remote central origins (e.g. GitHub/GitLab).

---

## 🔒 Security & Deployment Configuration

### `mcp_config.json` Snippet
Integrate your environment using this configuration pattern:
```json
{
  "mcpServers": {
    "git-mcp": {
      "command": "node",
      "args": [
        "${GIT_MCP_DIR}/build/index.js"
      ],
      "env": {
        "GIT_AUTHOR_NAME": "${GIT_USER_NAME}",
        "GIT_AUTHOR_EMAIL": "${GIT_USER_EMAIL}",
        "GIT_COMMITTER_NAME": "${GIT_USER_NAME}",
        "GIT_COMMITTER_EMAIL": "${GIT_USER_EMAIL}"
      }
    }
  }
}
```
