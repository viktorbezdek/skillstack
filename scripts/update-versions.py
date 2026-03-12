#!/usr/bin/env python3
"""Update plugin.json versions from the computed version map."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    version_map_path = ROOT / "scripts" / "version-map.json"
    with open(version_map_path) as f:
        version_map = json.load(f)

    updated = 0
    for plugin_name, data in sorted(version_map.items()):
        plugin_json_path = ROOT / plugin_name / ".claude-plugin" / "plugin.json"
        if not plugin_json_path.exists():
            print(f"  SKIP {plugin_name}: plugin.json not found")
            continue

        with open(plugin_json_path) as f:
            plugin = json.load(f)

        old_version = plugin.get("version", "1.0.0")
        new_version = data["version"]

        if old_version != new_version:
            plugin["version"] = new_version
            with open(plugin_json_path, "w") as f:
                json.dump(plugin, f, indent=2)
                f.write("\n")
            print(f"  {plugin_name}: {old_version} -> {new_version}")
            updated += 1
        else:
            print(f"  {plugin_name}: {old_version} (unchanged)")

    print(f"\nUpdated {updated} plugin.json files")


if __name__ == "__main__":
    main()
