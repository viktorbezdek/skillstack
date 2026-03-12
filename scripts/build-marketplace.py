#!/usr/bin/env python3
"""Generate .claude-plugin/marketplace.json from registry.json.

Produces a Claude Code-compatible marketplace manifest.
"""

import json
import sys
from pathlib import Path

REPO = "viktorbezdek/skillstack"


def main():
    root = Path(__file__).resolve().parent.parent
    registry_path = root / ".claude-plugin" / "registry.json"
    marketplace_path = root / ".claude-plugin" / "marketplace.json"

    if not registry_path.exists():
        print("Error: .claude-plugin/registry.json not found", file=sys.stderr)
        sys.exit(1)

    with open(registry_path) as f:
        registry = json.load(f)

    repos_by_id = {
        r["id"]: r
        for r in registry.get("repositories", [])
        if r.get("integration_status") == "active"
    }

    marketplace_plugins = []
    for plugin in registry.get("plugins", []):
        if plugin.get("status") != "active":
            continue

        repo = repos_by_id.get(plugin.get("repo_id"))
        if not repo:
            continue

        sha = repo.get("last_synced_sha", "")

        marketplace_plugins.append({
            "name": plugin["id"],
            "source": f"./{plugin['id']}",
            "description": plugin.get("description", ""),
            "version": plugin.get("version", "1.0.0"),
            "category": plugin.get("category", ""),
            "tags": plugin.get("tags", [])
        })

    marketplace = {
        "name": "skillstack",
        "owner": {
            "name": registry["owner"]["name"],
            "url": registry["owner"]["url"]
        },
        "metadata": {
            "description": registry.get("description", ""),
            "version": registry["metadata"]["version"]
        },
        "plugins": marketplace_plugins
    }

    with open(marketplace_path, "w") as f:
        json.dump(marketplace, f, indent=2)
        f.write("\n")

    print(f"Generated marketplace.json with {len(marketplace_plugins)} plugins")


if __name__ == "__main__":
    main()
