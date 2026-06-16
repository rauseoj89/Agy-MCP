# Postgres-MCP Blueprint 🗄️

`postgres-mcp` is a secure PostgreSQL database connector, providing standard schema inspection, query execution, and database maintenance capabilities to AI assistants.

## 📁 Structure

* **`BLUEPRINT.md`**: This manual.
* **`schemas/`**: JSON tool definition files.
* **`templates/`**: Connection parameters.

## 🚀 Capabilities

1. **Database Explorer (`list_databases`, `list_tables`, `describe_table`)**: Scans databases, catalogs, primary keys, and table columns.
2. **Safe Engine (`execute_query`)**: Executes direct SQL statements within defined scopes.

---

## 🔒 Security & Deployment Configuration

### `.env` Structure
Use the following local `.env` setup, ensuring to load secrets from Project Fortress Vault dynamically instead of raw values in code:
```bash
# 🗄️ DATABASE CONNECTION
DB_HOST=${DB_HOST}
DB_PORT=5432
DB_USER=${DB_USER}
DB_DATABASE=${DB_DATABASE}
DB_PASSWORD=${VAULT_SECRET_DB_PASSWORD}
```
