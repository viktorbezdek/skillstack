#!/usr/bin/env python3
"""
validate_plugin.py — standalone structural validator for Claude Code plugins.

Adapted from .github/scripts/validate_plugins.py at commit 9c762cd.
Independent contract: does not walk the whole repo, takes --plugin-dir argument,
no catalog (registry.json / marketplace.json) checks, no root README count check.
Drift from the repo validator is monitored by a contract test at
plugin-dev/scripts/tests/test_validator_drift.py.

Usage:
    python3 validate_plugin.py --plugin-dir PATH [--strict] [--json]

Exit codes:
    0 - all checks pass
    1 - validation errors found
    2 - the validator itself crashed (bug in this script)
    3 - --strict mode: warnings present (errors would exit 1 instead)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Issue:
    level: str  # "error" or "warning"
    scope: str  # skill name or plugin name
    message: str


@dataclass
class Report:
    errors: list[Issue] = field(default_factory=list)
    warnings: list[Issue] = field(default_factory=list)

    def err(self, scope: str, msg: str) -> None:
        self.errors.append(Issue("error", scope, msg))

    def warn(self, scope: str, msg: str) -> None:
        self.warnings.append(Issue("warning", scope, msg))

    def render(self) -> str:
        lines: list[str] = []
        if self.errors:
            lines.append(f"ERRORS ({len(self.errors)})")
            lines.append("-" * 72)
            for i in self.errors:
                lines.append(f"  [{i.scope}] {i.message}")
        if self.warnings:
            if lines:
                lines.append("")
            lines.append(f"WARNINGS ({len(self.warnings)})")
            lines.append("-" * 72)
            for i in self.warnings:
                lines.append(f"  [{i.scope}] {i.message}")
        if not self.errors and not self.warnings:
            lines.append("All plugin validation checks passed.")
        return "\n".join(lines)

    def as_dict(self) -> dict:
        return {
            "errors": [{"scope": i.scope, "message": i.message} for i in self.errors],
            "warnings": [{"scope": i.scope, "message": i.message} for i in self.warnings],
        }


def load_json(path: Path, report: Report, scope: str) -> dict | list | None:
    """Load a JSON file, recording parse errors in the report."""
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        report.err(scope, f"required file does not exist: {path}")
        return None
    except json.JSONDecodeError as e:
        report.err(scope, f"invalid JSON in {path}: {e}")
        return None


def parse_frontmatter(skill_md_path: Path) -> tuple[dict | None, str]:
    """Extract YAML frontmatter and body from a SKILL.md file.

    Returns a permissive key-value map parsed from lines of the form
    ``key: value`` inside the ``---`` fence. No PyYAML dependency.
    """
    try:
        text = skill_md_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, ""

    if not text.startswith("---"):
        return None, text

    end_marker = text.find("\n---", 3)
    if end_marker == -1:
        return None, text

    fm_block = text[3:end_marker].strip("\n")
    body = text[end_marker + 4:]

    fm: dict[str, str] = {}
    current_key: str | None = None
    buf: list[str] = []
    key_re = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")

    def flush() -> None:
        nonlocal current_key, buf
        if current_key is not None:
            fm[current_key] = " ".join(s.strip() for s in buf).strip()
        current_key = None
        buf = []

    for line in fm_block.splitlines():
        if not line.strip():
            continue
        m = key_re.match(line)
        if m and not line.startswith(" "):
            flush()
            current_key = m.group(1)
            rest = m.group(2).strip()
            if rest and rest != ">":
                buf.append(rest)
        else:
            if current_key is not None:
                buf.append(line.strip())
    flush()

    return fm, body


def validate_skill(skill_dir: Path, plugin_name: str, report: Report) -> None:
    """Validate one skill within a plugin.

    For single-skill plugins, skill_name == plugin_name.
    For multi-skill plugins, scope is 'plugin_name/skill_name'.
    """
    skill_name = skill_dir.name
    scope = f"{plugin_name}/{skill_name}" if skill_name != plugin_name else plugin_name

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        report.err(scope, f"missing SKILL.md at {skill_md}")
        return

    fm, body = parse_frontmatter(skill_md)
    if fm is None:
        report.err(scope, "SKILL.md has no YAML frontmatter (missing --- fence)")
        return

    if "name" not in fm or not fm["name"]:
        report.err(scope, "SKILL.md frontmatter missing required field: name")
    elif fm["name"] != skill_name:
        report.err(
            scope,
            f"SKILL.md frontmatter name '{fm['name']}' does not match "
            f"skill directory '{skill_name}'",
        )

    if "description" not in fm or not fm["description"]:
        report.err(scope, "SKILL.md frontmatter missing required field: description")

    # Cross-reference check: every references/X.md cited in SKILL.md body must exist.
    # Strip inline code spans to avoid false positives from placeholder examples.
    ref_dir = skill_dir / "references"
    if ref_dir.exists():
        body_no_code = re.sub(r"`[^`]+`", "", body)
        cited = set(re.findall(r"references/([A-Za-z0-9_\-]+\.md)", body_no_code))
        # Filter out obvious placeholder names used in examples
        placeholders = {"foo.md", "bar.md", "baz.md", "example.md", "template.md"}
        cited -= placeholders
        for ref in sorted(cited):
            target = ref_dir / ref
            if not target.is_file():
                report.err(
                    scope,
                    f"SKILL.md cites references/{ref} which does not exist",
                )


def validate_plugin(plugin_dir: Path, report: Report) -> dict | None:
    """Validate a single plugin directory. Returns parsed plugin.json or None.

    Supports both single-skill plugins (skills/{plugin-name}/SKILL.md) and
    multi-skill plugins (multiple skills/*/ directories under one plugin root).
    Does NOT check catalog entries (registry.json, marketplace.json) — those
    are skillstack-specific and out of scope for this standalone validator.
    """
    plugin_name = plugin_dir.name
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"

    manifest = load_json(manifest_path, report, plugin_name)
    if manifest is None:
        return None
    if not isinstance(manifest, dict):
        report.err(plugin_name, "plugin.json must be a JSON object")
        return None

    # Required fields.
    for fname in ("name", "version", "description"):
        if fname not in manifest or not manifest[fname]:
            report.err(plugin_name, f"plugin.json missing required field: {fname}")

    # Author field: either 'author' or 'authors'.
    if "author" not in manifest and "authors" not in manifest:
        report.err(plugin_name, "plugin.json missing author (or authors)")

    # plugin.json name must match directory.
    if manifest.get("name") and manifest["name"] != plugin_name:
        report.err(
            plugin_name,
            f"plugin.json name '{manifest['name']}' does not match "
            f"directory name '{plugin_name}'",
        )

    # README.md should exist.
    readme = plugin_dir / "README.md"
    if not readme.is_file():
        report.err(plugin_name, "plugin README.md does not exist")

    # Discover skills.
    skills_root = plugin_dir / "skills"
    if not skills_root.is_dir():
        report.err(
            plugin_name,
            f"missing skills/ directory at {skills_root}",
        )
        return manifest

    skill_dirs = sorted(
        d for d in skills_root.iterdir() if d.is_dir() and not d.name.startswith(".")
    )
    if not skill_dirs:
        report.err(plugin_name, f"skills/ directory is empty at {skills_root}")
        return manifest

    for skill_dir in skill_dirs:
        validate_skill(skill_dir, plugin_name, report)

    return manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the structural correctness of a Claude Code plugin.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exit codes:
  0  All checks pass
  1  Validation errors found
  2  Validator crashed (bug in this script)
  3  --strict mode: warnings present
""",
    )
    parser.add_argument(
        "--plugin-dir",
        required=True,
        metavar="PATH",
        help="Path to the plugin directory to validate",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 3 if warnings are present (in addition to the normal error check)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON instead of human-readable text",
    )
    args = parser.parse_args(argv)

    plugin_dir = Path(args.plugin_dir).resolve()
    if not plugin_dir.is_dir():
        print(f"Error: {plugin_dir} is not a directory", file=sys.stderr)
        return 1

    report = Report()
    validate_plugin(plugin_dir, report)

    if args.json:
        print(json.dumps(report.as_dict(), indent=2))
    else:
        print(report.render())

    if report.errors:
        return 1
    if args.strict and report.warnings:
        return 3
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"validator crashed: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
