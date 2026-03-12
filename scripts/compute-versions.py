#!/usr/bin/env python3
"""Compute semantic versions for each plugin based on git history.

For each plugin directory, analyzes every commit that touched it and classifies
the change as major/minor/patch using conventional commit prefixes:
  - feat:     → minor (new functionality)
  - fix:      → patch
  - docs:     → patch
  - style:    → patch
  - refactor: → patch
  - test:     → patch
  - ci:       → patch
  - chore:    → patch
  - revert:   → patch
  - BREAKING or major restructure → major

First commit for each plugin is always 1.0.0.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Conventional commit pattern: type(scope): message
CC_RE = re.compile(r"^(\w+)(?:\(([^)]*)\))?[!]?:\s*(.*)")


def get_plugin_dirs():
    """Find all plugin directories (those containing .claude-plugin/plugin.json)."""
    dirs = []
    for pj in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        dirs.append(pj.parent.parent)
    return dirs


def get_commits_for_dir(plugin_dir):
    """Get chronological list of (hash, message) tuples for commits touching this dir."""
    result = subprocess.run(
        ["git", "log", "--oneline", "--reverse", "--", str(plugin_dir.relative_to(ROOT)) + "/"],
        capture_output=True, text=True, cwd=ROOT
    )
    commits = []
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        parts = line.split(" ", 1)
        if len(parts) == 2:
            commits.append((parts[0], parts[1]))
    return commits


def classify_commit(message):
    """Classify a commit message as 'major', 'minor', or 'patch'."""
    # Check for breaking change indicator
    if "!" in message.split(":")[0] if ":" in message else False:
        return "major"
    if "BREAKING" in message.upper():
        return "major"

    m = CC_RE.match(message)
    if m:
        ctype = m.group(1).lower()
        if ctype == "feat":
            return "minor"
        elif ctype in ("fix", "docs", "style", "refactor", "test", "ci", "chore", "revert", "perf"):
            return "patch"

    # Non-conventional commits default to patch
    return "patch"


def compute_version(commits):
    """Given a list of (hash, message) commits, compute the semver version.

    First commit = 1.0.0, subsequent commits bump based on classification.
    """
    if not commits:
        return "1.0.0", []

    major, minor, patch = 1, 0, 0
    history = []

    # First commit is always the initial release
    history.append({
        "hash": commits[0][0],
        "message": commits[0][1],
        "bump": "initial",
        "version": "1.0.0"
    })

    for sha, msg in commits[1:]:
        bump = classify_commit(msg)
        if bump == "major":
            major += 1
            minor = 0
            patch = 0
        elif bump == "minor":
            minor += 1
            patch = 0
        else:
            patch += 1

        history.append({
            "hash": sha,
            "message": msg,
            "bump": bump,
            "version": f"{major}.{minor}.{patch}"
        })

    return f"{major}.{minor}.{patch}", history


def main():
    plugin_dirs = get_plugin_dirs()
    results = {}

    for pdir in plugin_dirs:
        name = pdir.name
        commits = get_commits_for_dir(pdir)
        version, history = compute_version(commits)
        results[name] = {
            "version": version,
            "commit_count": len(commits),
            "history": history
        }

    # Output summary
    print(f"{'Plugin':<35} {'Commits':>8} {'Version':>10}")
    print("-" * 55)
    for name in sorted(results.keys()):
        r = results[name]
        print(f"{name:<35} {r['commit_count']:>8} {r['version']:>10}")

    # Write full results to JSON
    output_path = ROOT / "scripts" / "version-map.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nFull version map written to {output_path}")

    return results


if __name__ == "__main__":
    main()
