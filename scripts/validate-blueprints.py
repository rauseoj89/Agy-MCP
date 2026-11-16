#!/usr/bin/env python3
"""Blueprint & Schema Validator for Agy-MCP."""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


def check_package_exists(ecosystem: str, pkg: str) -> str | None:
    """Return error string if package is missing/security-holder, else None."""
    if ecosystem == "npm":
        url = f"https://registry.npmjs.org/{pkg}"
    elif ecosystem == "pypi":
        url = f"https://pypi.org/pypi/{pkg}/json"
    else:
        return None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "agy-mcp-validator/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if ecosystem == "npm":
                latest = data.get("dist-tags", {}).get("latest", "")
                if latest == "0.0.1-security":
                    return f"npm package '{pkg}' is a 0.0.1-security placeholder"
                if data.get("versions", {}).get(latest, {}).get("deprecated"):
                    return f"npm package '{pkg}'@{latest} is deprecated"
            return None
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return f"{ecosystem} package '{pkg}' not found (404)"
        return None
    except Exception:
        return None


def validate_tools_json(path: Path) -> tuple[int, list[str]]:
    issues: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return 0, [f"Invalid JSON: {exc}"]

    tools = data.get("tools", data if isinstance(data, list) else [])
    if not isinstance(tools, list) or not tools:
        return 0, ["Missing or empty 'tools' list"]

    for idx, tool in enumerate(tools):
        name = tool.get("name", f"tool[{idx}]")
        desc = tool.get("description", "")
        if not isinstance(desc, str) or len(desc.strip()) < 20:
            issues.append(f"Tool '{name}' description must be >= 20 characters (got {len(str(desc).strip())})")

        schema = tool.get("inputSchema") or tool.get("parameters")
        if not isinstance(schema, dict):
            issues.append(f"Tool '{name}' missing inputSchema/parameters object")
            continue
        if schema.get("additionalProperties") is not False:
            issues.append(f"Tool '{name}' missing 'additionalProperties: false'")

        props = schema.get("properties", {})
        if isinstance(props, dict):
            for pname, pdef in props.items():
                if isinstance(pdef, dict) and pdef.get("type") == "string":
                    if "maxLength" not in pdef and "enum" not in pdef:
                        issues.append(f"Tool '{name}.{pname}' string property missing 'maxLength'")

    return len(tools), issues


def parse_readme_catalog(readme_path: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    text = readme_path.read_text(encoding="utf-8")
    row_re = re.compile(r"^\|\s*\*\*`([^`]+)`\*\*\s*\|\s*`[^`]+`\s*\|\s*[^|]+\|\s*(\d+)\s*\|", re.M)
    for m in row_re.finditer(text):
        counts[m.group(1)] = int(m.group(2))
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Agy-MCP blueprints and schemas.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root directory")
    parser.add_argument("--check-packages", action="store_true", help="Verify npm/PyPI packages online")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    readme = root / "README.md"
    blueprints_dir = root / "mcp-blueprints"

    all_issues: list[str] = []
    readme_counts = parse_readme_catalog(readme) if readme.exists() else {}

    for mcp_name, expected_count in sorted(readme_counts.items()):
        bp_dir = blueprints_dir / mcp_name
        if not bp_dir.is_dir():
            all_issues.append(f"README lists '{mcp_name}' but directory {bp_dir} does not exist")
            continue
        tools_path = bp_dir / "schemas" / "tools.json"
        if tools_path.exists():
            actual_count, issues = validate_tools_json(tools_path)
            for issue in issues:
                all_issues.append(f"[{mcp_name}] {issue}")
            if actual_count != expected_count:
                all_issues.append(
                    f"[{mcp_name}] README Tools Count ({expected_count}) != tools.json count ({actual_count})"
                )
        elif expected_count != 0:
            all_issues.append(f"[{mcp_name}] Expected {expected_count} tools but schemas/tools.json is missing")

    if args.check_packages:
        pkg_json = root / "boilerplates" / "nodejs-mcp" / "package.json"
        if pkg_json.exists():
            deps = json.loads(pkg_json.read_text(encoding="utf-8")).get("dependencies", {})
            for pkg in deps:
                err = check_package_exists("npm", pkg)
                if err:
                    all_issues.append(f"[boilerplates/nodejs-mcp] {err}")

    if all_issues:
        for issue in all_issues:
            print(f"[FAIL] {issue}")
        return 1

    print(f"[OK] Validated {len(readme_counts)} blueprints in {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
