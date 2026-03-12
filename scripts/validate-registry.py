#!/usr/bin/env python3
"""Validate .claude-plugin/registry.json schema and cross-references."""

import json
import sys
from pathlib import Path

REQUIRED_REPO_FIELDS = {"id", "url", "added_by", "added_date", "integration_status"}
REQUIRED_PLUGIN_FIELDS = {"id", "name", "type", "category", "description", "repo_id", "status"}
REQUIRED_COLLECTION_FIELDS = {"id", "name", "plugin_ids"}
VALID_PLUGIN_TYPES = {"skill", "agent", "mcp", "command"}
VALID_CATEGORIES = {"development", "devops", "quality", "context-engineering",
                    "agent-architecture", "thinking", "design", "documentation"}
VALID_STATUSES = {"active", "deprecated", "removed"}
VALID_INTEGRATION_STATUSES = {"active", "paused", "removed"}


def main():
    root = Path(__file__).resolve().parent.parent
    registry_path = root / ".claude-plugin" / "registry.json"

    if not registry_path.exists():
        print("FAIL: .claude-plugin/registry.json not found", file=sys.stderr)
        sys.exit(1)

    try:
        with open(registry_path) as f:
            registry = json.load(f)
    except json.JSONDecodeError as e:
        print(f"FAIL: Invalid JSON - {e}", file=sys.stderr)
        sys.exit(1)

    errors = []
    warnings = []

    for key in ("name", "metadata", "repositories", "plugins", "collections"):
        if key not in registry:
            errors.append(f"Missing top-level key: {key}")

    if not isinstance(registry.get("repositories"), list):
        errors.append("'repositories' must be an array")
    if not isinstance(registry.get("plugins"), list):
        errors.append("'plugins' must be an array")
    if not isinstance(registry.get("collections"), list):
        errors.append("'collections' must be an array")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    repos = registry["repositories"]
    plugins = registry["plugins"]
    collections = registry["collections"]

    repo_ids = set()
    plugin_ids = set()

    # Validate repositories
    for i, repo in enumerate(repos):
        prefix = f"repositories[{i}]"
        missing = REQUIRED_REPO_FIELDS - set(repo.keys())
        if missing:
            errors.append(f"{prefix}: missing fields: {missing}")
            continue

        rid = repo["id"]
        if rid in repo_ids:
            errors.append(f"{prefix}: duplicate repo id '{rid}'")
        repo_ids.add(rid)

        if not repo["url"].startswith("https://github.com/"):
            errors.append(f"{prefix}: url must start with https://github.com/")

        if repo.get("integration_status") not in VALID_INTEGRATION_STATUSES:
            warnings.append(f"{prefix}: unknown integration_status '{repo.get('integration_status')}'")

    # Validate plugins
    for i, plugin in enumerate(plugins):
        prefix = f"plugins[{i}]"
        missing = REQUIRED_PLUGIN_FIELDS - set(plugin.keys())
        if missing:
            errors.append(f"{prefix}: missing fields: {missing}")
            continue

        pid = plugin["id"]
        if pid in plugin_ids:
            errors.append(f"{prefix}: duplicate plugin id '{pid}'")
        plugin_ids.add(pid)

        if plugin["repo_id"] not in repo_ids:
            errors.append(f"{prefix}: repo_id '{plugin['repo_id']}' not found in repositories")

        if plugin["type"] not in VALID_PLUGIN_TYPES:
            errors.append(f"{prefix}: invalid type '{plugin['type']}'")

        if plugin["category"] not in VALID_CATEGORIES:
            warnings.append(f"{prefix}: unknown category '{plugin['category']}'")

        if plugin.get("status") not in VALID_STATUSES:
            warnings.append(f"{prefix}: unknown status '{plugin.get('status')}'")

        # Check documentation path exists
        doc_path = plugin.get("documentation_path")
        if doc_path:
            full_path = root / doc_path.lstrip("./")
            if not full_path.exists():
                warnings.append(f"{prefix}: documentation_path '{doc_path}' does not exist")

    # Validate collections
    for i, col in enumerate(collections):
        prefix = f"collections[{i}]"
        missing = REQUIRED_COLLECTION_FIELDS - set(col.keys())
        if missing:
            errors.append(f"{prefix}: missing fields: {missing}")
            continue

        for pid in col.get("plugin_ids", []):
            if pid not in plugin_ids:
                errors.append(f"{prefix}: plugin_id '{pid}' not found in plugins")

        if col.get("auto_inferred_from_repo") and col["auto_inferred_from_repo"] not in repo_ids:
            errors.append(f"{prefix}: auto_inferred_from_repo '{col['auto_inferred_from_repo']}' not found")

    # Check plugin directories exist
    for plugin in plugins:
        if plugin.get("status") != "active":
            continue
        plugin_dir = root / plugin["id"]
        if not plugin_dir.exists():
            warnings.append(f"Plugin directory missing: {plugin['id']}/")
        elif not (plugin_dir / ".claude-plugin" / "plugin.json").exists():
            warnings.append(f"Plugin manifest missing: {plugin['id']}/.claude-plugin/plugin.json")

    # Report
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)

    total = len(repos) + len(plugins) + len(collections)
    if errors:
        print(f"\nFAILED: {len(errors)} errors, {len(warnings)} warnings ({total} entries checked)")
        sys.exit(1)
    else:
        print(f"PASSED: {len(repos)} repos, {len(plugins)} plugins, {len(collections)} collections "
              f"({len(warnings)} warnings)")
        sys.exit(0)


if __name__ == "__main__":
    main()
