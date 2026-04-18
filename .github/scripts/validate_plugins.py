#!/usr/bin/env python3
"""
SkillStack plugin validation.

Validates every skill plugin in the repository against the contract the
catalog implicitly assumes. Catches real bugs that the old CI missed:
missing plugin.json, orphan catalog entries, version drift between
plugin.json and registry.json, SKILL.md cross-references to missing
reference files, frontmatter omissions, plugin-count mismatches in
README headers.

Exit codes:
    0 - all checks pass
    1 - validation errors found
    2 - the validator itself crashed (bug in this script)
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / ".claude-plugin" / "registry.json"
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"
ROOT_README = REPO_ROOT / "README.md"

# Directories at repo root that are NOT plugins and should be ignored.
NON_PLUGIN_ROOT_DIRS = {
    ".claude",
    ".claude-plugin",
    ".git",
    ".github",
    ".omc",
    "node_modules",
}


@dataclass
class Issue:
    level: str  # "error" or "warning"
    plugin: str  # plugin name or "-"
    message: str


@dataclass
class Report:
    errors: list[Issue] = field(default_factory=list)
    warnings: list[Issue] = field(default_factory=list)

    def err(self, plugin: str, msg: str) -> None:
        self.errors.append(Issue("error", plugin, msg))

    def warn(self, plugin: str, msg: str) -> None:
        self.warnings.append(Issue("warning", plugin, msg))

    def render(self) -> str:
        lines: list[str] = []
        if self.errors:
            lines.append(f"ERRORS ({len(self.errors)})")
            lines.append("-" * 72)
            for i in self.errors:
                lines.append(f"  [{i.plugin}] {i.message}")
        if self.warnings:
            if lines:
                lines.append("")
            lines.append(f"WARNINGS ({len(self.warnings)})")
            lines.append("-" * 72)
            for i in self.warnings:
                lines.append(f"  [{i.plugin}] {i.message}")
        if not self.errors and not self.warnings:
            lines.append("All plugin validation checks passed.")
        return "\n".join(lines)


def load_json(path: Path, report: Report, scope: str) -> dict | list | None:
    """Load a JSON file, recording parse errors in the report."""
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        report.err(scope, f"required file does not exist: {path.relative_to(REPO_ROOT)}")
        return None
    except json.JSONDecodeError as e:
        report.err(scope, f"invalid JSON in {path.relative_to(REPO_ROOT)}: {e}")
        return None


def parse_frontmatter(skill_md_path: Path) -> tuple[dict | None, str]:
    """Extract YAML frontmatter and body from a SKILL.md file.

    Returns a permissive key-value map parsed from lines of the form
    ``key: value`` inside the ``---`` fence. We intentionally do not pull
    PyYAML as a dependency — the frontmatter in this repo uses simple
    single-line scalars plus multi-line continuations, which we handle
    explicitly.
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
    body = text[end_marker + 4 :]

    fm: dict[str, str] = {}
    current_key: str | None = None
    buf: list[str] = []
    # Match ``key:`` (possibly with a value on the same line).
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
            # Continuation line for a multi-line value.
            if current_key is not None:
                buf.append(line.strip())
    flush()

    return fm, body


def discover_plugin_directories() -> list[Path]:
    """Return all directories at repo root that contain a plugin.json."""
    result: list[Path] = []
    for entry in sorted(REPO_ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name in NON_PLUGIN_ROOT_DIRS:
            continue
        if entry.name.startswith("."):
            continue
        if (entry / ".claude-plugin" / "plugin.json").is_file():
            result.append(entry)
    return result


def validate_skill(skill_dir: Path, plugin_name: str, report: Report) -> None:
    """Validate one skill inside a plugin.

    Single-skill plugins have ``skills/{plugin-name}/SKILL.md`` with
    frontmatter ``name: {plugin-name}``. Multi-skill plugins have
    multiple ``skills/*/SKILL.md`` files; in that case each skill's
    frontmatter ``name`` must match its own directory, not the plugin
    directory.
    """
    skill_name = skill_dir.name
    scope = f"{plugin_name}/{skill_name}" if skill_name != plugin_name else plugin_name

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        report.err(scope, f"missing SKILL.md at {skill_md.relative_to(REPO_ROOT)}")
        return

    fm, body = parse_frontmatter(skill_md)
    if fm is None:
        report.err(scope, "SKILL.md has no YAML frontmatter (missing `---` fence)")
        return

    if "name" not in fm or not fm["name"]:
        report.err(scope, "SKILL.md frontmatter missing required field: name")
    elif fm["name"] != skill_name:
        report.err(
            scope,
            f"SKILL.md frontmatter name '{fm['name']}' does not match skill directory '{skill_name}'",
        )

    if "description" not in fm or not fm["description"]:
        report.err(scope, "SKILL.md frontmatter missing required field: description")

    # Cross-reference check: every `references/foo.md` mentioned in
    # SKILL.md should exist on disk.
    ref_dir = skill_dir / "references"
    if ref_dir.exists():
        # Match markdown links/references like [text](references/foo.md) or `references/foo.md`
        # but skip examples inside inline code that use placeholder names.
        # Strip inline code spans first to avoid false positives from examples.
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
    """Validate a single plugin. Returns the parsed plugin.json, or None.

    Supports both single-skill plugins (``skills/{plugin-name}/SKILL.md``)
    and multi-skill plugins (multiple ``skills/*/SKILL.md`` files under
    one plugin root).
    """
    plugin_name = plugin_dir.name
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"

    manifest = load_json(manifest_path, report, plugin_name)
    if manifest is None:
        return None
    if not isinstance(manifest, dict):
        report.err(plugin_name, "plugin.json must be a JSON object")
        return None

    # Required top-level fields.
    for field_name in ("name", "version", "description"):
        if field_name not in manifest or not manifest[field_name]:
            report.err(plugin_name, f"plugin.json missing required field: {field_name}")

    # Author field accepts two shapes across the repo (`author` or `authors`).
    if "author" not in manifest and "authors" not in manifest:
        report.err(plugin_name, "plugin.json missing author (or authors)")

    # Name consistency.
    if manifest.get("name") and manifest["name"] != plugin_name:
        report.err(
            plugin_name,
            f"plugin.json name '{manifest['name']}' does not match directory name '{plugin_name}'",
        )

    # README.md should exist for human documentation.
    readme = plugin_dir / "README.md"
    if not readme.is_file():
        report.err(plugin_name, "plugin README.md does not exist")

    # Discover all skills inside this plugin.
    skills_root = plugin_dir / "skills"
    if not skills_root.is_dir():
        report.err(plugin_name, f"missing skills/ directory at {skills_root.relative_to(REPO_ROOT)}")
        return manifest

    skill_dirs = sorted(
        d for d in skills_root.iterdir() if d.is_dir() and not d.name.startswith(".")
    )
    if not skill_dirs:
        report.err(plugin_name, f"skills/ directory is empty at {skills_root.relative_to(REPO_ROOT)}")
        return manifest

    for skill_dir in skill_dirs:
        validate_skill(skill_dir, plugin_name, report)

    return manifest


def validate_catalog(
    plugin_manifests: dict[str, dict],
    report: Report,
) -> None:
    """Check registry.json and marketplace.json against the filesystem."""
    registry = load_json(REGISTRY_PATH, report, "registry.json")
    marketplace = load_json(MARKETPLACE_PATH, report, "marketplace.json")
    if registry is None or marketplace is None:
        return
    if not isinstance(registry, dict) or not isinstance(marketplace, dict):
        report.err("catalog", "registry.json / marketplace.json must be JSON objects")
        return

    reg_plugins = {p["id"]: p for p in registry.get("plugins", []) if isinstance(p, dict) and "id" in p}
    mkt_plugins = {p["name"]: p for p in marketplace.get("plugins", []) if isinstance(p, dict) and "name" in p}

    # Every discovered plugin must be in both catalogs.
    for name, manifest in plugin_manifests.items():
        version = manifest.get("version", "")

        # registry.json presence + consistency
        if name not in reg_plugins:
            report.err(name, "missing entry in .claude-plugin/registry.json")
        else:
            entry = reg_plugins[name]
            reg_version = entry.get("version", "")
            if reg_version != version:
                report.err(
                    name,
                    f"version drift: plugin.json={version} vs registry.json={reg_version}",
                )
            path_in_repo = entry.get("path_in_repo", "")
            if path_in_repo:
                target = REPO_ROOT / path_in_repo
                if not target.is_dir():
                    report.err(
                        name,
                        f"registry.json path_in_repo='{path_in_repo}' does not exist",
                    )

        # marketplace.json presence + consistency
        if name not in mkt_plugins:
            report.err(name, "missing entry in .claude-plugin/marketplace.json")
        else:
            entry = mkt_plugins[name]
            mkt_version = entry.get("version", "")
            if mkt_version != version:
                report.err(
                    name,
                    f"version drift: plugin.json={version} vs marketplace.json={mkt_version}",
                )
            source = entry.get("source", "")
            if source:
                target = REPO_ROOT / source.lstrip("./")
                if not target.is_dir():
                    report.err(
                        name,
                        f"marketplace.json source='{source}' does not exist",
                    )

    # Orphans — catalog entries without matching plugin directories.
    for reg_id in reg_plugins:
        if reg_id not in plugin_manifests:
            report.err(
                "registry.json",
                f"orphan entry '{reg_id}' has no matching plugin directory",
            )
    for mkt_name in mkt_plugins:
        if mkt_name not in plugin_manifests:
            report.err(
                "marketplace.json",
                f"orphan entry '{mkt_name}' has no matching plugin directory",
            )


def validate_root_readme(plugin_count: int, report: Report) -> None:
    """Check that the root README's plugin count claims match reality."""
    if not ROOT_README.is_file():
        report.err("README.md", "root README.md does not exist")
        return

    text = ROOT_README.read_text(encoding="utf-8")

    expected = str(plugin_count)
    # Patterns that should match the total plugin count. The SkillStack
    # summary pattern is restricted to the full-collection <summary> tag
    # so it does not match category sub-collections (Development, DevOps,
    # Quality, etc.) which correctly have smaller counts.
    count_patterns = [
        (re.compile(r"(\d+)\s+expert\s+plugins"), "expert plugins"),
        (re.compile(r"\*\*(\d+)\*\*\s+plugins\s*·"), "header plugin count"),
        (
            re.compile(r"<summary><strong>SkillStack</strong>\s*—\s*(\d+)\s+plugins"),
            "SkillStack collection summary",
        ),
    ]
    for pattern, label in count_patterns:
        for match in pattern.finditer(text):
            found = match.group(1)
            if found != expected:
                report.err(
                    "README.md",
                    f"{label}: README says '{found}' but actual count is {expected}",
                )


def main() -> int:
    report = Report()

    plugin_dirs = discover_plugin_directories()
    plugin_manifests: dict[str, dict] = {}

    for plugin_dir in plugin_dirs:
        manifest = validate_plugin(plugin_dir, report)
        if manifest is not None:
            plugin_manifests[plugin_dir.name] = manifest

    validate_catalog(plugin_manifests, report)
    validate_root_readme(len(plugin_manifests), report)

    print(f"Discovered {len(plugin_dirs)} plugin directories.")
    print(report.render())

    return 1 if report.errors else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # noqa: BLE001 - surfacing is the point
        print(f"validator crashed: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
