"""
Drift contract test for validate_plugin.py vs .github/scripts/validate_plugins.py.

Both validators are run against well-known plugins (skillstack-workflows, skill-creator)
and their outputs are compared to detect drift between the two implementations.

The contract: for plugins that are VALID, both validators should agree on "no errors".
For plugins that have SPECIFIC known errors (frontmatter name mismatch, missing references),
both validators should detect the same category of error (though exact messages may differ).

If this test fails in a future commit, it means the two validators have drifted in their
behavior for overlapping checks. See the header comment in validate_plugin.py for the
drift-documentation convention.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

THIS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = THIS_DIR.parent
REPO_ROOT = SCRIPTS_DIR.parents[1]  # plugin-dev/scripts -> plugin-dev -> skillstack

sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(REPO_ROOT / ".github" / "scripts"))

import validate_plugin as local_vp  # noqa: E402
import validate_plugins as repo_vp  # noqa: E402


def local_errors(plugin_dir: Path) -> list[str]:
    report = local_vp.Report()
    local_vp.validate_plugin(plugin_dir, report)
    return [e.message for e in report.errors]


def repo_errors(plugin_dir: Path) -> list[str]:
    """Run only the skill-level validation (not catalog checks) from the repo validator."""
    report = repo_vp.Report()
    plugin_name = plugin_dir.name
    # Run only validate_plugin (skill-level), not validate_catalog or validate_root_readme
    repo_vp.validate_plugin(plugin_dir, report)
    return [e.message for e in report.errors]


class TestValidatorDrift:
    def test_skillstack_workflows_clean_in_both(self) -> None:
        """skillstack-workflows (multi-skill plugin) should pass both validators."""
        plugin_dir = REPO_ROOT / "skillstack-workflows"
        if not plugin_dir.is_dir():
            pytest.skip("skillstack-workflows not found in repo")

        local = local_errors(plugin_dir)
        repo = repo_errors(plugin_dir)

        assert local == [], f"local validator found errors: {local}"
        assert repo == [], f"repo validator found errors: {repo}"

    def test_skill_creator_clean_in_both(self) -> None:
        """skill-creator (single-skill plugin) should pass both validators."""
        plugin_dir = REPO_ROOT / "skill-creator"
        if not plugin_dir.is_dir():
            pytest.skip("skill-creator not found in repo")

        local = local_errors(plugin_dir)
        repo = repo_errors(plugin_dir)

        assert local == [], f"local validator found errors: {local}"
        assert repo == [], f"repo validator found errors: {repo}"

    def test_plugin_dev_clean_in_both(self) -> None:
        """plugin-dev itself should pass both validators."""
        plugin_dir = REPO_ROOT / "plugin-dev"
        if not plugin_dir.is_dir():
            pytest.skip("plugin-dev not found")

        local = local_errors(plugin_dir)
        repo = repo_errors(plugin_dir)

        assert local == [], f"local validator found errors: {local}"
        assert repo == [], f"repo validator found errors: {repo}"

    def test_frontmatter_name_mismatch_detected_by_both(self, tmp_path: Path) -> None:
        """Both validators should detect a frontmatter name mismatch."""
        plugin_dir = tmp_path / "test-plugin"
        plugin_dir.mkdir()
        (plugin_dir / ".claude-plugin").mkdir()
        (plugin_dir / ".claude-plugin" / "plugin.json").write_text(
            json.dumps({"name": "test-plugin", "version": "1.0.0",
                        "description": "x", "author": {"name": "t", "url": "http://x.com"}})
        )
        (plugin_dir / "README.md").write_text("# x\n")
        skill_dir = plugin_dir / "skills" / "test-plugin"
        skill_dir.mkdir(parents=True)
        # WRONG name in frontmatter
        (skill_dir / "SKILL.md").write_text(
            "---\nname: wrong-name\ndescription: test\n---\n# body\n"
        )

        local = local_errors(plugin_dir)
        repo = repo_errors(plugin_dir)

        assert any("wrong-name" in e or "does not match" in e for e in local), \
            f"local validator did not catch name mismatch: {local}"
        assert any("wrong-name" in e or "does not match" in e for e in repo), \
            f"repo validator did not catch name mismatch: {repo}"
