"""Smoke tests for the plugin validation script.

These tests build up tiny synthetic plugin directories and feed them
to the validator, then assert the expected errors surface. They do
not touch the real repository contents.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

THIS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = THIS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import validate_plugins as vp  # noqa: E402 - sys.path manipulation required


@pytest.fixture
def fake_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Construct a minimal fake repository and point the validator at it."""
    (tmp_path / ".claude-plugin").mkdir()
    (tmp_path / ".claude-plugin" / "registry.json").write_text(
        json.dumps({"plugins": []})
    )
    (tmp_path / ".claude-plugin" / "marketplace.json").write_text(
        json.dumps({"plugins": []})
    )
    (tmp_path / "README.md").write_text("# fake\n")

    monkeypatch.setattr(vp, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(vp, "REGISTRY_PATH", tmp_path / ".claude-plugin" / "registry.json")
    monkeypatch.setattr(
        vp, "MARKETPLACE_PATH", tmp_path / ".claude-plugin" / "marketplace.json"
    )
    monkeypatch.setattr(vp, "ROOT_README", tmp_path / "README.md")
    return tmp_path


def create_plugin(
    root: Path,
    name: str,
    *,
    manifest_name: str | None = None,
    skill_name: str | None = None,
    include_skill: bool = True,
    include_readme: bool = True,
    references_cited: list[str] | None = None,
    references_on_disk: list[str] | None = None,
    version: str = "1.0.0",
) -> Path:
    """Create a minimal plugin directory at `root/name`."""
    plugin_dir = root / name
    plugin_dir.mkdir()
    (plugin_dir / ".claude-plugin").mkdir()
    manifest = {
        "name": manifest_name if manifest_name is not None else name,
        "version": version,
        "description": "test plugin",
        "author": {"name": "test", "url": "https://example.com"},
    }
    (plugin_dir / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest))

    if include_readme:
        (plugin_dir / "README.md").write_text(f"# {name}\n")

    if include_skill:
        skill_dir = plugin_dir / "skills" / name
        skill_dir.mkdir(parents=True)
        fm_name = skill_name if skill_name is not None else name
        body = "# Body\n"
        for ref in references_cited or []:
            body += f"\nSee references/{ref} for more.\n"
        skill_md = f"---\nname: {fm_name}\ndescription: test desc\n---\n{body}"
        (skill_dir / "SKILL.md").write_text(skill_md)

        if references_on_disk is not None:
            refs_dir = skill_dir / "references"
            refs_dir.mkdir()
            for ref in references_on_disk:
                (refs_dir / ref).write_text("# ref\n")

    return plugin_dir


def register_in_catalog(
    root: Path,
    name: str,
    *,
    version: str = "1.0.0",
    path_in_repo: str | None = None,
    source: str | None = None,
) -> None:
    registry = json.loads((root / ".claude-plugin" / "registry.json").read_text())
    marketplace = json.loads((root / ".claude-plugin" / "marketplace.json").read_text())
    registry["plugins"].append(
        {
            "id": name,
            "name": name,
            "version": version,
            "path_in_repo": path_in_repo or f"{name}/skills/{name}",
        }
    )
    marketplace["plugins"].append(
        {"name": name, "version": version, "source": source or f"./{name}"}
    )
    (root / ".claude-plugin" / "registry.json").write_text(json.dumps(registry))
    (root / ".claude-plugin" / "marketplace.json").write_text(json.dumps(marketplace))


def run(report_class=None) -> vp.Report:
    report = vp.Report()
    plugin_dirs = vp.discover_plugin_directories()
    manifests: dict[str, dict] = {}
    for plugin_dir in plugin_dirs:
        manifest = vp.validate_plugin(plugin_dir, report)
        if manifest is not None:
            manifests[plugin_dir.name] = manifest
    vp.validate_catalog(manifests, report)
    vp.validate_root_readme(len(manifests), report)
    return report


class TestValidPlugin:
    def test_minimal_valid_plugin_passes(self, fake_repo):
        create_plugin(fake_repo, "alpha")
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert report.errors == []

    def test_plugin_with_references_passes(self, fake_repo):
        create_plugin(
            fake_repo,
            "alpha",
            references_cited=["foo.md", "bar.md"],
            references_on_disk=["foo.md", "bar.md"],
        )
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert report.errors == []


class TestPluginStructure:
    def test_missing_skill_md_reports_error(self, fake_repo):
        create_plugin(fake_repo, "alpha", include_skill=False)
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert any("missing SKILL.md" in e.message for e in report.errors)

    def test_missing_readme_reports_error(self, fake_repo):
        create_plugin(fake_repo, "alpha", include_readme=False)
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert any("README.md does not exist" in e.message for e in report.errors)

    def test_frontmatter_name_mismatch_reports_error(self, fake_repo):
        create_plugin(fake_repo, "alpha", skill_name="wrong")
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert any("frontmatter name 'wrong'" in e.message for e in report.errors)

    def test_manifest_name_mismatch_reports_error(self, fake_repo):
        create_plugin(fake_repo, "alpha", manifest_name="wrong")
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert any("plugin.json name 'wrong'" in e.message for e in report.errors)

    def test_missing_reference_reports_error(self, fake_repo):
        create_plugin(
            fake_repo,
            "alpha",
            references_cited=["foo.md"],
            references_on_disk=[],  # cited but not on disk
        )
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert any("foo.md which does not exist" in e.message for e in report.errors)


class TestCatalogConsistency:
    def test_unregistered_plugin_reports_error(self, fake_repo):
        create_plugin(fake_repo, "alpha")
        # Do NOT register in catalog.
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert any("missing entry in .claude-plugin/registry.json" in e.message for e in report.errors)
        assert any("missing entry in .claude-plugin/marketplace.json" in e.message for e in report.errors)

    def test_version_drift_reports_error(self, fake_repo):
        create_plugin(fake_repo, "alpha", version="1.0.0")
        # Register with a different version.
        register_in_catalog(fake_repo, "alpha", version="2.0.0")
        (fake_repo / "README.md").write_text("**1** plugins · categories\n")
        report = run()
        assert any("version drift" in e.message for e in report.errors)

    def test_orphan_registry_entry_reports_error(self, fake_repo):
        # Register a plugin that does not exist on disk.
        register_in_catalog(fake_repo, "ghost")
        (fake_repo / "README.md").write_text("**0** plugins · categories\n")
        report = run()
        assert any(
            "orphan entry 'ghost'" in e.message
            for e in report.errors
        )


class TestRootReadmeCount:
    def test_wrong_count_in_header_reports_error(self, fake_repo):
        create_plugin(fake_repo, "alpha")
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text("**42** plugins · categories\n")
        report = run()
        assert any("header plugin count" in e.message for e in report.errors)

    def test_wrong_expert_count_reports_error(self, fake_repo):
        create_plugin(fake_repo, "alpha")
        register_in_catalog(fake_repo, "alpha")
        (fake_repo / "README.md").write_text(
            "**1** plugins · categories\n\n99 expert plugins covering things.\n"
        )
        report = run()
        assert any("expert plugins" in e.message for e in report.errors)
