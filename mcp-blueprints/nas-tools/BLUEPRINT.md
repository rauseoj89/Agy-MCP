# NAS-Tools Blueprint 🛠️ [RETIRED]

> [!CAUTION]
> **BLUEPRINT RETIRED (2026-09-28)**  
> The `nas-tools` custom MCP server has been formally **RETIRED**. There is no dedicated NAS appliance in this development environment. All system operations, container monitoring, and Docker orchestration previously handled by `nas-tools` must now be executed using **native Docker CLI** commands (`docker ps`, `docker inspect`, `docker stats`, `docker compose`) or **Windows PowerShell cmdlets** (`Get-PSDrive`, `Get-Process`). All skills have been refactored away from `nas-tools`.

## 📁 Structure

* **`BLUEPRINT.md`**: Architectural archive.
* **`schemas/`**: *Pending / Deprecated*
* **`templates/`**: *Pending / Deprecated*

## 📜 Historical Capabilities (Now Migrated to Native Tooling)

| Historical Tool | Native Replacement Tooling |
| :--- | :--- |
| `get_system_stats` | Native PowerShell: `Get-PSDrive`, `Get-Counter`, or POSIX: `df -h`, `top` |
| `docker_ps` | Native CLI: `docker ps --format json` |
| `docker_logs` | Native CLI: `docker logs --tail 100 <container>` |
| `docker_inspect` | Native CLI: `docker inspect <container>` |
| `docker_control` | Native CLI: `docker start|stop|restart <container>` |
| `docker_compose` | Native CLI: `docker compose -f compose.yaml up -d` |
| `zfs_get_pools` | ZFS CLI (if available): `zpool status -x` |
| `check_permissions` | PowerShell: `Get-Acl <path>` / POSIX: `ls -ld <path>` |

---
**Author:** JimmyR  
**Powered by:** AntigravityAI
