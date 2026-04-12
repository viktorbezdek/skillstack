"""
Tests for validate_plugin.py — the standalone structural plugin validator.

Each test builds a synthetic plugin in a tmp_path fixture and asserts the
correct errors/warnings appear. Pattern mirrors .github/scripts/tests/test_validate_plugins.py.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

THIS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = THIS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import validate_plugin as vp  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def create_plugin(
    root: Path,
    name: str,
    *,
    manifest_name: str | None = None,
    skill_name: str | None = None,
    description: str = "Test skill description. Use when running tests.",
    include_skill: bool = True,
    include_readme: bool = True,
    references_cited: list[str] | None = None,
    references_on_disk: list[str] | None = None,
    version: str = "1.0.0",
) -> Path:
    """Create a minimal plugin directory at root/name."""
    plugin_dir = root / name
    plugin_dir.mkdir()
    (plugin_dir / ".claude-plugin").mkdir()
    manifest = {
        "name": manifest_name or name,
        "version": version,
        "description": "test plugin",
        "author": {"name": "test", "url": "https://example.com"},
    }
    (plugin_dir / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest))

    if include_readme:
        (plugin_dir / "README.md").write_text(f"# {name}\n")

    if include_skill:
        fm_name = skill_name or name
        body = "# Body\n"
        if references_cited:
            for ref in references_cited:
                body += f"\nSee references/{ref} for more.\n"
        skill_dir = plugin_dir / "skills" / name
        skill_dir.mkdir(parents=True)
        skill_md = f"---\nname: {fm_name}\ndescription: {description}\n---\n{body}"
        (skill_dir / "SKILL.md").write_text(skill_md)

        if references_on_disk is not None:
            refs_dir = skill_dir / "references"
            refs_dir.mkdir()
            for ref in references_on_disk:
                (refs_dir / ref).write_text("# ref\n")

    return plugin_dir


def run(plugin_dir: Path) -> vp.Report:
    report = vp.Report()
    vp.validate_plugin(plugin_dir, report)
    return report


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------


class TestValidPlugin:
    def test_minimal_valid_plugin_passes(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha")
        report = run(plugin_dir)
        assert report.errors == []

    def test_plugin_with_references_passes(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(
            tmp_path,
            "alpha",
            references_cited=["foo.md", "bar.md"],
            references_on_disk=["foo.md", "bar.md"],
        )
        report = run(plugin_dir)
        assert report.errors == []

    def test_multi_skill_plugin_passes(self, tmp_path: Path) -> None:
        plugin_dir = tmp_path / "bundle"
        plugin_dir.mkdir()
        (plugin_dir / ".claude-plugin").mkdir()
        (plugin_dir / ".claude-plugin" / "plugin.json").write_text(
            json.dumps({"name": "bundle", "version": "1.0.0", "description": "x",
                        "author": {"name": "t", "url": "http://x.com"}})
        )
        (plugin_dir / "README.md").write_text("# bundle\n")
        for skill_name in ("skill-a", "skill-b"):
            sd = plugin_dir / "skills" / skill_name
            sd.mkdir(parents=True)
            (sd / "SKILL.md").write_text(
                f"---\nname: {skill_name}\ndescription: test skill. Use when testing.\n---\n# body\n"
            )
        report = run(plugin_dir)
        assert report.errors == []


# ---------------------------------------------------------------------------
# Structure errors
# ---------------------------------------------------------------------------


class TestPluginStructure:
    def test_missing_readme_reports_error(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha", include_readme=False)
        report = run(plugin_dir)
        assert any("README.md does not exist" in e.message for e in report.errors)

    def test_missing_skills_dir_reports_error(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha", include_skill=False, include_readme=True)
        report = run(plugin_dir)
        assert any("missing skills/" in e.message for e in report.errors)

    def test_empty_skills_dir_reports_error(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha", include_skill=False)
        (plugin_dir / "skills").mkdir()
        report = run(plugin_dir)
        assert any("skills/ directory is empty" in e.message for e in report.errors)

    def test_missing_skill_md_reports_error(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha", include_skill=False)
        (plugin_dir / "skills" / "alpha").mkdir(parents=True)
        report = run(plugin_dir)
        assert any("missing SKILL.md" in e.message for e in report.errors)

    def test_frontmatter_name_mismatch_reports_error(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha", skill_name="wrong-name")
        report = run(plugin_dir)
        assert any("does not match skill directory 'alpha'" in e.message for e in report.errors)

    def test_manifest_name_mismatch_reports_error(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha", manifest_name="beta")
        report = run(plugin_dir)
        assert any("plugin.json name 'beta'" in e.message for e in report.errors)

    def test_missing_reference_reports_error(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(
            tmp_path,
            "alpha",
            references_cited=["missing-ref.md"],
            references_on_disk=[],
        )
        report = run(plugin_dir)
        assert any("missing-ref.md which does not exist" in e.message for e in report.errors)

    def test_multi_skill_bad_skill_scoped_error(self, tmp_path: Path) -> None:
        plugin_dir = tmp_path / "bundle"
        plugin_dir.mkdir()
        (plugin_dir / ".claude-plugin").mkdir()
        (plugin_dir / ".claude-plugin" / "plugin.json").write_text(
            json.dumps({"name": "bundle", "version": "1.0.0", "description": "x",
                        "author": {"name": "t", "url": "http://x.com"}})
        )
        (plugin_dir / "README.md").write_text("# bundle\n")
        # skill-a valid
        sa = plugin_dir / "skills" / "skill-a"
        sa.mkdir(parents=True)
        (sa / "SKILL.md").write_text("---\nname: skill-a\ndescription: test\n---\nbody\n")
        # skill-b has wrong name
        sb = plugin_dir / "skills" / "skill-b"
        sb.mkdir(parents=True)
        (sb / "SKILL.md").write_text("---\nname: wrong\ndescription: test\n---\nbody\n")

        report = run(plugin_dir)
        scoped = [e for e in report.errors if "bundle/skill-b" in e.scope]
        assert scoped, f"expected bundle/skill-b scoped error, got: {[(e.scope, e.message) for e in report.errors]}"


# ---------------------------------------------------------------------------
# CLI tests
# ---------------------------------------------------------------------------


class TestCLI:
    def test_json_output_valid(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "validate_plugin.py"),
             "--plugin-dir", str(plugin_dir), "--json"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert "errors" in data
        assert "warnings" in data

    def test_exits_1_on_errors(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha", include_readme=False)
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "validate_plugin.py"),
             "--plugin-dir", str(plugin_dir)],
            capture_output=True, text=True,
        )
        assert result.returncode == 1

    def test_exits_0_on_clean_plugin(self, tmp_path: Path) -> None:
        plugin_dir = create_plugin(tmp_path, "alpha")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "validate_plugin.py"),
             "--plugin-dir", str(plugin_dir)],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
