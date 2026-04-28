#!/usr/bin/env python3
"""
scaffold_plugin.py — interactive plugin skeleton generator.

Generates a minimum-viable Claude Code plugin skeleton that passes
validate_plugin.py on first run. Deterministic output: same arguments
always produce the same files (no datetime.now(), uuid.uuid4(), or
os.urandom() calls anywhere).

Usage:
    python3 scaffold_plugin.py --name NAME [OPTIONS]

Examples:
    python3 scaffold_plugin.py --name my-plugin
    python3 scaffold_plugin.py --name finance-tool --skills budget,forecast --hooks PreToolUse,PostToolUse
    python3 scaffold_plugin.py --name data-tools --mcp --author "Jane Smith" --output-dir /tmp/plugins
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

EVAL_RUNNER_NAME = "run_eval.py"


# ---------------------------------------------------------------------------
# Template helpers
# ---------------------------------------------------------------------------

def _plugin_json(name: str, author_name: str, author_url: str) -> dict:
    return {
        "name": name,
        "version": "0.1.0",
        "description": f"Claude Code plugin: {name}. Describe what this plugin does and when to use it.",
        "author": {
            "name": author_name,
            "url": author_url,
        },
        "license": "MIT",
        "repository": f"https://github.com/your-org/{name}",
        "keywords": [
            "claude-code",
            "skill",
            name,
        ],
    }


def _skill_md(skill_name: str) -> str:
    return f"""---
name: {skill_name}
description: Describe what the {skill_name} skill does and when to use it. Include specific trigger phrases users would say. NOT for unrelated queries (use a more specific skill instead).
---

# {skill_name.replace("-", " ").title()}

> One sentence describing the core principle of this skill.

---

## When to use this skill

- "Describe a concrete scenario where a user would invoke this skill"
- "Another trigger scenario"

## When NOT to use this skill

- **For X** — use the `other-skill` skill instead

---

## Core principle

[Replace with the non-negotiable rule that governs this skill's behavior.]

---

## How to use this skill

[Provide the main guidance here. Keep SKILL.md under 500 lines.
Move detailed content to references/ files and link to them.]
"""


def _hooks_json(events: list[str]) -> dict:
    hooks: dict = {}
    for event in events:
        hooks[event] = [
            {
                "hooks": [
                    {
                        "type": "command",
                        "command": "${CLAUDE_PLUGIN_ROOT}/scripts/your-hook.sh",
                    }
                ],
                "matcher": "*",
            }
        ]
    return {"description": "Hook configuration for this plugin.", "hooks": hooks}


def _mcp_json(plugin_name: str) -> dict:
    return {
        "mcpServers": {
            f"{plugin_name}-server": {
                "command": "${CLAUDE_PLUGIN_ROOT}/scripts/mcp-server.py",
                "args": [],
                "env": {},
            }
        }
    }


def _copy_eval_runner(plugin_dir: Path) -> Path:
    """Copy run_eval.py from this scripts dir into the scaffolded plugin's scripts dir."""
    source = Path(__file__).parent / EVAL_RUNNER_NAME
    target = plugin_dir / "scripts" / EVAL_RUNNER_NAME
    if not source.exists():
        raise FileNotFoundError(
            f"Eval runner source not found at {source}. "
            "scaffold_plugin.py expects to be co-located with run_eval.py."
        )
    shutil.copy2(source, target)
    return target


def _readme(plugin_name: str, skills: list[str]) -> str:
    skills_list = "\n".join(f"- `{s}` — [describe what this skill does]" for s in skills)
    return f"""# {plugin_name.replace("-", " ").title()}

> **v0.1.0** | [Category] | 0 iterations

[One-sentence description of what this plugin does and the problem it solves.]

## What Problem Does This Solve

[2-3 sentences describing the specific pain points this plugin addresses.]

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Describe a concrete user query" | Specific capability the skill delivers |
| "Another trigger scenario" | Another concrete capability |

## When NOT to Use This Skill

- **For X** — use a different plugin instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add your-org/{plugin_name}
/plugin install {plugin_name}@your-marketplace
```

## How to Use

**Direct invocation:**

```
Use the {skills[0] if skills else plugin_name} skill to ...
```

## Running Evals

This plugin ships with `scripts/run_eval.py` so you can validate your skills
without depending on an external harness. Offline mode (default) does
structural checks only and needs no API key:

```bash
uv run --with anthropic python scripts/run_eval.py \\
    --plugin-dir . --skill {skills[0] if skills else plugin_name} --offline
```

For online activation/output evals, set `ANTHROPIC_API_KEY` and drop
`--offline`.

## What's Inside

{skills_list}

## Version History

- `0.1.0` Initial release

---

Part of your plugin collection.
"""


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def scaffold(
    name: str,
    skills: list[str],
    hooks: list[str],
    mcp: bool,
    author_name: str,
    author_url: str,
    output_dir: Path,
    force: bool,
) -> Path:
    """Generate the plugin skeleton. Returns the plugin root directory."""
    plugin_dir = output_dir / name

    if plugin_dir.exists() and not force:
        print(
            f"Error: directory '{plugin_dir}' already exists.\n"
            "Use --force to overwrite or choose a different --name.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Create directory structure.
    (plugin_dir / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (plugin_dir / "scripts").mkdir(exist_ok=True)
    (plugin_dir / "assets").mkdir(exist_ok=True)

    # Bundle the eval runner so the new plugin can run its own evals out of the box.
    _copy_eval_runner(plugin_dir)

    # plugin.json
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    manifest_path.write_text(
        json.dumps(_plugin_json(name, author_name, author_url), indent=2) + "\n",
        encoding="utf-8",
    )

    # Skill directories.
    for skill_name in skills:
        skill_dir = plugin_dir / "skills" / skill_name
        (skill_dir / "references").mkdir(parents=True, exist_ok=True)
        (skill_dir / "SKILL.md").write_text(_skill_md(skill_name), encoding="utf-8")

    # hooks/hooks.json (only if --hooks given).
    if hooks:
        (plugin_dir / "hooks").mkdir(exist_ok=True)
        hooks_path = plugin_dir / "hooks" / "hooks.json"
        hooks_path.write_text(
            json.dumps(_hooks_json(hooks), indent=2) + "\n",
            encoding="utf-8",
        )

    # .mcp.json (only if --mcp given).
    if mcp:
        mcp_path = plugin_dir / ".mcp.json"
        mcp_path.write_text(
            json.dumps(_mcp_json(name), indent=2) + "\n",
            encoding="utf-8",
        )

    # README.md
    (plugin_dir / "README.md").write_text(_readme(name, skills), encoding="utf-8")

    return plugin_dir


def run_validator(plugin_dir: Path) -> bool:
    """Run validate_plugin.py against the generated plugin. Returns True if clean."""
    validator = Path(__file__).parent / "validate_plugin.py"
    if not validator.exists():
        print("Warning: validate_plugin.py not found — skipping post-generation validation")
        return True

    result = subprocess.run(
        [sys.executable, str(validator), "--plugin-dir", str(plugin_dir)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Post-generation validation FAILED:\n{result.stdout}{result.stderr}", file=sys.stderr)
        return False
    print(f"Post-generation validation passed: {result.stdout.strip()}")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate a minimum-viable Claude Code plugin skeleton.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scaffold_plugin.py --name my-plugin
  python3 scaffold_plugin.py --name finance-tool --skills budget,forecast --hooks PreToolUse
  python3 scaffold_plugin.py --name data-tools --mcp --output-dir /tmp/plugins
""",
    )
    parser.add_argument("--name", required=True, help="Plugin name (kebab-case)")
    parser.add_argument(
        "--skills",
        default="",
        help="Comma-separated skill names (default: same as plugin name)",
    )
    parser.add_argument(
        "--hooks",
        default="",
        help="Comma-separated hook events (e.g. PreToolUse,PostToolUse)",
    )
    parser.add_argument(
        "--mcp",
        action="store_true",
        help="Include .mcp.json stub",
    )
    parser.add_argument(
        "--author",
        default="Your Name",
        help="Author name for plugin.json",
    )
    parser.add_argument(
        "--author-url",
        default="https://github.com/your-org",
        help="Author URL for plugin.json",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory to create the plugin in (default: current directory)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing plugin directory",
    )
    args = parser.parse_args(argv)

    # Parse skills list (default to plugin name).
    skills = [s.strip() for s in args.skills.split(",") if s.strip()] or [args.name]

    # Parse hooks list.
    hooks = [h.strip() for h in args.hooks.split(",") if h.strip()]

    output_dir = Path(args.output_dir).resolve()
    if not output_dir.exists():
        print(f"Error: output directory '{output_dir}' does not exist", file=sys.stderr)
        return 1

    plugin_dir = scaffold(
        name=args.name,
        skills=skills,
        hooks=hooks,
        mcp=args.mcp,
        author_name=args.author,
        author_url=args.author_url,
        output_dir=output_dir,
        force=args.force,
    )

    print(f"\nPlugin skeleton created at: {plugin_dir}")
    print(f"  Skills:  {', '.join(skills)}")
    if hooks:
        print(f"  Hooks:   {', '.join(hooks)}")
    if args.mcp:
        print("  MCP:     .mcp.json stub created")
    print(f"  Evals:   scripts/{EVAL_RUNNER_NAME} bundled (offline mode runs without API key)")

    if not run_validator(plugin_dir):
        return 1

    print("\nNext steps:")
    print(f"  1. Edit {plugin_dir}/.claude-plugin/plugin.json — fill in description")
    print(f"  2. Edit each SKILL.md in {plugin_dir}/skills/ — replace placeholder content")
    print("  3. Add references/ files for progressive disclosure")
    next_step = 4
    if hooks:
        print(f"  {next_step}. Implement hook scripts referenced in {plugin_dir}/hooks/hooks.json")
        next_step += 1
    print(
        f"  {next_step}. Author trigger-evals.json + evals.json under skills/<skill>/evals/ "
        f"and run scripts/{EVAL_RUNNER_NAME} (offline by default, no API key required)"
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"scaffolder crashed: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
