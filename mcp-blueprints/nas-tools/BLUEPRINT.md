# NAS-Tools Blueprint 🛠️

`nas-tools` is an MCP server designed for system diagnostics, Docker orchestration, and ZFS pool management on a custom home storage server.

## 📁 Structure

* **`BLUEPRINT.md`**: This architectural manual.
* **`schemas/`**: JSON tool files for registration.
* **`templates/`**: Setup variables and secure config examples.

## 🚀 Capabilities

1. **System Statistics (`get_system_stats`)**: Retrieves real-time CPU, RAM, disk, and ZFS temperature stats.
2. **Docker Orchestration (`docker_ps`, `docker_logs`, `docker_inspect`, `docker_control`)**: Lists, stops, starts, or inspects Docker containers.
3. **ZFS Storage (`zfs_get_pools`)**: Views health and configurations of ZFS storage pools.
4. **Shell Control (`execute_shell_command`, `check_permissions`)**: Run managed commands securely on targeted hubs.

---

## 🔒 Security & Deployment Configuration

### `.env` Structure
Store the environment settings in a local, uncommitted `.env` file pointing to your TrueNAS SSH credentials:
```bash
# 🛡️ SYSTEM SECURITY (SSH-Powered)
REMOTE_HOST=dev_jimmy@<your-server-ip>
SSH_KEY_PATH=C:/Users/JimmyR/.ssh/id_rsa

# 🛠️ CORE CONFIGURATION
NAS_ROOT_PATH=/mnt/data_raid/mcp_projects
MANAGED_HUBS=Infrastructure,Workspaces,Shared
```
