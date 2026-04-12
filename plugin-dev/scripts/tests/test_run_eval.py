"""
Tests for run_eval.py — the eval harness.

Tests use the fixture eval files at tests/fixtures/example-evals/ and
synthetic plugins in tmp_path. All API calls are offline-only (no SDK needed).
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

THIS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = THIS_DIR.parent
FIXTURES = THIS_DIR / "fixtures" / "example-evals"
sys.path.insert(0, str(SCRIPTS_DIR))

import run_eval as re_  # noqa: E402, N813


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def make_plugin_with_evals(
    tmp_path: Path,
    skill_name: str,
    trigger_cases: list[dict] | None = None,
    output_cases: list[dict] | None = None,
    description: str = "Test skill. Use when running tests for the plugin-dev skill.",
) -> Path:
    plugin_dir = tmp_path / "test-plugin"
    plugin_dir.mkdir()
    (plugin_dir / ".claude-plugin").mkdir()
    (plugin_dir / ".claude-plugin" / "plugin.json").write_text(
        json.dumps({"name": "test-plugin", "version": "1.0.0",
                    "description": "test", "author": {"name": "t", "url": "http://x.com"}})
    )
    (plugin_dir / "README.md").write_text("# test\n")
    skill_dir = plugin_dir / "skills" / skill_name
    evals_dir = skill_dir / "evals"
    evals_dir.mkdir(parents=True)

    (skill_dir / "SKILL.md").write_text(
        f"---\nname: {skill_name}\ndescription: {description}\n---\n# body\n"
    )

    if trigger_cases is not None:
        (evals_dir / "trigger-evals.json").write_text(json.dumps(trigger_cases))
    else:
        # Copy from fixture
        (evals_dir / "trigger-evals.json").write_bytes((FIXTURES / "trigger-evals.json").read_bytes())

    if output_cases is not None:
        (evals_dir / "evals.json").write_text(json.dumps(output_cases))
    else:
        (evals_dir / "evals.json").write_bytes((FIXTURES / "evals.json").read_bytes())

    return plugin_dir


# ---------------------------------------------------------------------------
# Smoke mode (no API required)
# ---------------------------------------------------------------------------


class TestSmokeMode:
    def test_offline_smoke_mode_passes_clean_eval(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(tmp_path, "my-skill")
        result = re_.run_smoke(plugin_dir, "my-skill", tmp_path / "workspace")
        assert result.mode == "offline"
        assert "synthetic" in result.warning.lower()
        assert result.trigger_file_valid
        assert result.output_file_valid

    def test_smoke_uses_fixture_schemas(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(tmp_path, "my-skill")
        result = re_.run_smoke(plugin_dir, "my-skill", tmp_path / "workspace")
        # Fixture has 8 positive + 5 negative = 13 total
        assert result.trigger_cases == 13
        assert result.should_trigger_count == 8
        assert result.should_not_trigger_count == 5
        assert result.output_cases == 3

    def test_smoke_detects_missing_trigger_file(self, tmp_path: Path) -> None:
        plugin_dir = tmp_path / "test-plugin"
        plugin_dir.mkdir()
        (plugin_dir / ".claude-plugin").mkdir()
        (plugin_dir / ".claude-plugin" / "plugin.json").write_text(
            json.dumps({"name": "test-plugin", "version": "1.0.0",
                        "description": "x", "author": {"name": "t", "url": "http://x.com"}})
        )
        (plugin_dir / "README.md").write_text("# x\n")
        skill_dir = plugin_dir / "skills" / "my-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: my-skill\ndescription: test use when testing\n---\nbody\n"
        )
        # No evals directory
        result = re_.run_smoke(plugin_dir, "my-skill", tmp_path / "workspace")
        assert any("trigger-evals.json not found" in e for e in result.errors)

    def test_smoke_detects_malformed_trigger_file(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(
            tmp_path, "my-skill",
            trigger_cases=[{"query": "no should_trigger field here"}],
        )
        result = re_.run_smoke(plugin_dir, "my-skill", tmp_path / "workspace")
        assert not result.trigger_file_valid or any("should_trigger" in e for e in result.errors)

    def test_smoke_report_has_mode_and_warning(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(tmp_path, "my-skill")
        result = re_.run_smoke(plugin_dir, "my-skill", tmp_path / "workspace")
        d = result.as_dict()
        assert d["mode"] == "offline"
        assert "synthetic" in d["warning"].lower()


class TestSmokeReportFiles:
    def test_smoke_creates_benchmark_json(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(tmp_path, "my-skill")
        workspace = tmp_path / "ws"
        result = re_.run_smoke(plugin_dir, "my-skill", workspace)
        re_._write_smoke_report(result, workspace, "my-skill")
        assert (workspace / "benchmark.json").is_file()
        data = json.loads((workspace / "benchmark.json").read_text())
        assert data["mode"] == "offline"

    def test_smoke_benchmark_md_has_synthetic_banner(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(tmp_path, "my-skill")
        workspace = tmp_path / "ws"
        result = re_.run_smoke(plugin_dir, "my-skill", workspace)
        re_._write_smoke_report(result, workspace, "my-skill")
        content = (workspace / "benchmark.md").read_text()
        assert "OFFLINE MODE" in content
        assert "SMOKE" in content or "structural" in content.lower()


class TestCLIOfflineMode:
    def test_offline_flag_mode_smoke(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(tmp_path, "my-skill")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "run_eval.py"),
             "--plugin-dir", str(plugin_dir), "--skill", "my-skill", "--offline"],
            capture_output=True, text=True,
        )
        # Passes if eval files are clean
        assert result.returncode in (0, 1)  # 0=clean, 1=eval issues
        assert "OFFLINE MODE" in result.stdout or "OFFLINE MODE" in result.stderr

    def test_trigger_mode_offline_exits_3(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(tmp_path, "my-skill")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "run_eval.py"),
             "--plugin-dir", str(plugin_dir), "--skill", "my-skill",
             "--mode", "trigger", "--offline"],
            capture_output=True, text=True,
        )
        assert result.returncode == 3

    def test_missing_skill_exits_2(self, tmp_path: Path) -> None:
        plugin_dir = make_plugin_with_evals(tmp_path, "my-skill")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "run_eval.py"),
             "--plugin-dir", str(plugin_dir), "--skill", "nonexistent", "--offline"],
            capture_output=True, text=True,
        )
        assert result.returncode == 2
