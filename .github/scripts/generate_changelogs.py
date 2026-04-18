#!/usr/bin/env python3
"""Generate per-plugin CHANGELOG.md files from git history.

Scans all plugins (directories with .claude-plugin/plugin.json), extracts
conventional-commit messages scoped to each plugin, and writes a CHANGELOG.md
in each plugin directory grouped by version and date.

Commit message format expected:
  type(scope): description          -> type: description
  improve(scope): description       -> Changed: description
  fix(scope): description           -> Fixed: description
  feat(scope): description          -> Added: description
  refactor(scope): description      -> Changed: description
  docs(scope): description          -> Changed: description

Falls back to including any commit that touches files under the plugin dir
even without a conventional-commit prefix.
"""

import json
import os
import re
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Conventional commit type -> changelog section
TYPE_MAP = {
    "feat": "Added",
    "add": "Added",
    "improve": "Changed",
    "change": "Changed",
    "refactor": "Changed",
    "docs": "Changed",
    "fix": "Fixed",
    "fixup": "Fixed",
    "perf": "Changed",
    "revert": "Removed",
    "remove": "Removed",
    "delete": "Removed",
    "security": "Fixed",
}

# Pattern: type(scope): message  or  type(scope): message
CC_RE = re.compile(
    r"^(?P<type>[a-z]+)" r"(?:\((?P<scope>[^)]+)\))?" r":\s*(?P<msg>.+)$",
    re.IGNORECASE,
)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], capture_output=True, text=True, cwd=REPO_ROOT
    )
    return result.stdout.strip()


def get_plugins() -> list[Path]:
    """Return sorted list of plugin directories."""
    plugins = []
    for child in sorted(REPO_ROOT.iterdir()):
        plugin_json = child / ".claude-plugin" / "plugin.json"
        if plugin_json.is_file():
            plugins.append(child)
    return plugins


def get_plugin_version(plugin_dir: Path) -> str:
    plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
    try:
        with open(plugin_json) as f:
            return json.load(f).get("version", "0.0.0")
    except (json.JSONDecodeError, FileNotFoundError):
        return "0.0.0"


def get_plugin_name(plugin_dir: Path) -> str:
    plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
    try:
        with open(plugin_json) as f:
            return json.load(f).get("name", plugin_dir.name)
    except (json.JSONDecodeError, FileNotFoundError):
        return plugin_dir.name


def parse_commits_for_plugin(plugin_dir: Path) -> dict[str, list[dict]]:
    """Return {version_tag: [entries]} from git log touching this plugin.

    Walks git log. For each commit:
    - If the commit message matches conventional-commit with this plugin's
      dir name as scope, use the type mapping.
    - If the commit touches files under this plugin dir but has no matching
      scope, categorize as "Changed".
    - Track version by reading plugin.json at each commit (approximated by
      using the version in the commit tree).
    """
    plugin_rel = plugin_dir.name
    # Get all commits touching this plugin directory
    log_format = "%H%x00%ai%x00%s"
    raw = git(
        "log", f"--format={log_format}", "--", f"{plugin_rel}/"
    )

    if not raw:
        return {}

    # Build version timeline: for each commit, try to read plugin.json version
    # This is expensive per-commit, so we batch: get all hashes, then resolve
    version_at: dict[str, str] = {}
    hashes = []
    for line in raw.split("\n"):
        if not line.strip():
            continue
        parts = line.split("\x00", 2)
        if len(parts) < 3:
            continue
        h, _date, _subject = parts
        hashes.append(h)

    # Read plugin.json version at each commit
    for h in hashes:
        try:
            content = git("show", f"{h}:{plugin_rel}/.claude-plugin/plugin.json")
            data = json.loads(content)
            version_at[h] = data.get("version", "0.0.0")
        except Exception:
            # File didn't exist or was invalid at this commit
            version_at[h] = "0.0.0"

    # Parse entries grouped by version
    entries_by_version: dict[str, list[dict]] = defaultdict(list)
    seen_keys = set()

    for line in raw.split("\n"):
        if not line.strip():
            continue
        parts = line.split("\x00", 2)
        if len(parts) < 3:
            continue
        h, date_str, subject = parts
        version = version_at.get(h, "0.0.0")
        date = date_str[:10]  # YYYY-MM-DD

        # Try conventional commit parse
        m = CC_RE.match(subject)
        if m:
            cc_type = m.group("type").lower()
            scope = m.group("scope") or ""
            msg = m.group("msg").strip()

            # Only include if scope matches plugin dir name
            if scope == plugin_rel or not scope:
                section = TYPE_MAP.get(cc_type, "Changed")
            else:
                # Scope doesn't match this plugin — skip
                continue
        else:
            # Non-conventional commit that touches this plugin
            section = "Changed"
            msg = subject.strip()

        # Deduplicate (same version + section + message)
        key = (version, section, msg)
        if key in seen_keys:
            continue
        seen_keys.add(key)

        entries_by_version[version].append(
            {"section": section, "message": msg, "date": date}
        )

    return dict(entries_by_version)


def render_changelog(plugin_name: str, entries_by_version: dict[str, list[dict]]) -> str:
    """Render changelog in Keep-a-Changelog format."""
    lines = [
        f"# Changelog — {plugin_name}",
        "",
        "All notable changes to this plugin will be documented in this file.",
        "",
        "The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).",
        "",
    ]

    # Sort versions: try semver, fall back to string
    def version_sort_key(v: str) -> tuple:
        try:
            parts = v.split("-")[0].split(".")
            return tuple(int(p) for p in parts)
        except (ValueError, AttributeError):
            return (0, 0, 0)

    sorted_versions = sorted(entries_by_version.keys(), key=version_sort_key, reverse=True)

    for version in sorted_versions:
        entries = entries_by_version[version]
        # Get date from first entry (most recent commit in this version)
        date = entries[0]["date"] if entries else "UNKNOWN"

        lines.append(f"## [{version}] - {date}")
        lines.append("")

        # Group by section
        section_order = ["Added", "Changed", "Fixed", "Removed"]
        by_section: dict[str, list[str]] = defaultdict(list)
        for e in entries:
            by_section[e["section"]].append(e["message"])

        for section in section_order:
            if section in by_section:
                lines.append(f"### {section}")
                lines.append("")
                for msg in by_section[section]:
                    lines.append(f"- {msg}")
                lines.append("")

    return "\n".join(lines)


def main():
    plugins = get_plugins()
    changed = []

    for plugin_dir in plugins:
        plugin_name = get_plugin_name(plugin_dir)
        current_version = get_plugin_version(plugin_dir)

        entries = parse_commits_for_plugin(plugin_dir)

        # If no git history, generate a stub
        if not entries:
            entries = {
                current_version: [
                    {
                        "section": "Added",
                        "message": "Initial release",
                        "date": datetime.now().strftime("%Y-%m-%d"),
                    }
                ]
            }

        content = render_changelog(plugin_name, entries)
        changelog_path = plugin_dir / "CHANGELOG.md"

        # Check if content changed
        existing = ""
        if changelog_path.exists():
            existing = changelog_path.read_text()

        if content != existing:
            changelog_path.write_text(content)
            n_versions = len(entries)
            print(f"  UPDATED {plugin_name} ({n_versions} versions, current v{current_version})")
            changed.append(plugin_dir.name)
        else:
            print(f"  OK       {plugin_name} (no changes)")

    print(f"\n{len(changed)} changelogs updated: {', '.join(changed) if changed else 'none'}")


if __name__ == "__main__":
    main()
