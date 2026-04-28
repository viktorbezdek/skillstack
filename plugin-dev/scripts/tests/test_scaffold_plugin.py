"""
Tests for scaffold_plugin.py — the plugin skeleton generator.

Verifies correct generation, determinism, flag handling, and that generated
output passes validate_plugin.py.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest

THIS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = THIS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import scaffold_plugin as sp  # noqa: E402
import validate_plugin as vp  # noqa: E402


def scaffold_to_tmp(name: str, tmp_path: Path, **kwargs) -> Path:
    sp.scaffold(
        name=name,
        skills=kwargs.get("skills", [name]),
        hooks=kwargs.get("hooks", []),
        mcp=kwargs.get("mcp", False),
        author_name=kwargs.get("author_name", "Test Author"),
        author_url=kwargs.get("author_url", "https://example.com"),
        output_dir=tmp_path,
        force=kwargs.get("force", False),
    )
    return tmp_path / name


def passes_validator(plugin_dir: Path) -> bool:
    report = vp.Report()
    vp.validate_plugin(plugin_dir, report)
    return len(report.errors) == 0


class TestScaffoldGeneration:
    def test_minimal_generation_passes_validator(self, tmp_path: Path) -> None:
        plugin_dir = scaffold_to_tmp("test-plugin", tmp_path)
        assert passes_validator(plugin_dir), "Generated plugin failed validation"

    def test_plugin_json_has_required_fields(self, tmp_path: Path) -> None:
        plugin_dir = scaffold_to_tmp("test-plugin", tmp_path)
        manifest = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text())
        for field in ("name", "version", "description", "author"):
            assert field in manifest, f"Missing field: {field}"
        assert manifest["name"] == "test-plugin"

    def test_skills_flag_creates_skill_dirs(self, tmp_path: Path) -> None:
        plugin_dir = scaffold_to_tmp("multi-skill", tmp_path, skills=["alpha", "beta", "gamma"])
        for skill in ("alpha", "beta", "gamma"):
            assert (plugin_dir / "skills" / skill / "SKILL.md").is_file()

    def test_hooks_flag_creates_hooks_json(self, tmp_path: Path) -> None:
        plugin_dir = scaffold_to_tmp("hooked", tmp_path, hooks=["PreToolUse", "PostToolUse"])
        hooks_json = plugin_dir / "hooks" / "hooks.json"
        assert hooks_json.is_file()
        data = json.loads(hooks_json.read_text())
        assert "PreToolUse" in data.get("hooks", {})
        assert "PostToolUse" in data.get("hooks", {})

    def test_no_hooks_flag_no_hooks_dir(self, tmp_path: Path) -> None:
        plugin_dir = scaffold_to_tmp("clean", tmp_path)
        assert not (plugin_dir / "hooks").exists()

    def test_mcp_flag_creates_mcp_json(self, tmp_path: Path) -> None:
        plugin_dir = scaffold_to_tmp("with-mcp", tmp_path, mcp=True)
        assert (plugin_dir / ".mcp.json").is_file()
        data = json.loads((plugin_dir / ".mcp.json").read_text())
        assert "mcpServers" in data

    def test_no_mcp_flag_no_mcp_json(self, tmp_path: Path) -> None:
        plugin_dir = scaffold_to_tmp("no-mcp", tmp_path)
        assert not (plugin_dir / ".mcp.json").exists()

    def test_readme_created(self, tmp_path: Path) -> None:
        plugin_dir = scaffold_to_tmp("test-plugin", tmp_path)
        assert (plugin_dir / "README.md").is_file()
        content = (plugin_dir / "README.md").read_text()
        assert "Test-Plugin" in content or "test-plugin" in content.lower()

    def test_eval_runner_bundled(self, tmp_path: Path) -> None:
        """run_eval.py must ship with every scaffolded plugin so authors can run evals immediately."""
        plugin_dir = scaffold_to_tmp("with-evals", tmp_path)
        scaffolded_runner = plugin_dir / "scripts" / "run_eval.py"
        assert scaffolded_runner.is_file(), "Scaffolded plugin missing scripts/run_eval.py"

        # Bytes must match the source runner exactly.
        source_runner = SCRIPTS_DIR / "run_eval.py"
        assert scaffolded_runner.read_bytes() == source_runner.read_bytes()

    def test_eval_runner_executes_smoke(self, tmp_path: Path) -> None:
        """The bundled run_eval.py must be invokable against the scaffolded plugin (offline smoke)."""
        plugin_dir = scaffold_to_tmp("evalable", tmp_path, skills=["primary"])
        # Provide eval files that meet the smoke runner's minimum thresholds
        # (≥8 positive triggers, ≥5 negative triggers, ≥3 output cases).
        evals_dir = plugin_dir / "skills" / "primary" / "evals"
        evals_dir.mkdir(parents=True, exist_ok=True)
        triggers = [
            {"query": f"positive query {i}", "should_trigger": True} for i in range(8)
        ] + [
            {"query": f"negative query {i}", "should_trigger": False} for i in range(5)
        ]
        (evals_dir / "trigger-evals.json").write_text(
            json.dumps(triggers) + "\n", encoding="utf-8"
        )
        outputs = [
            {"query": f"scenario {i}", "files": [], "expected_behavior": [f"behavior {i}"]}
            for i in range(3)
        ]
        (evals_dir / "evals.json").write_text(
            json.dumps(outputs) + "\n", encoding="utf-8"
        )

        result = subprocess.run(
            [
                sys.executable,
                str(plugin_dir / "scripts" / "run_eval.py"),
                "--plugin-dir",
                str(plugin_dir),
                "--skill",
                "primary",
                "--offline",
                "--workspace",
                str(tmp_path / "eval-workspace"),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, (
            f"Bundled runner failed:\nSTDOUT:{result.stdout}\nSTDERR:{result.stderr}"
        )
        # Smoke report should land in the workspace.
        assert (tmp_path / "eval-workspace" / "skill-primary" / "benchmark.md").is_file()

    def test_refuses_to_overwrite_without_force(self, tmp_path: Path) -> None:
        scaffold_to_tmp("test-plugin", tmp_path)
        with pytest.raises(SystemExit) as exc_info:
            scaffold_to_tmp("test-plugin", tmp_path, force=False)
        assert exc_info.value.code == 1

    def test_force_overwrites_successfully(self, tmp_path: Path) -> None:
        scaffold_to_tmp("test-plugin", tmp_path)
        plugin_dir = scaffold_to_tmp("test-plugin", tmp_path, force=True)
        assert passes_validator(plugin_dir)


class TestScaffoldDeterminism:
    def test_scaffold_is_deterministic(self, tmp_path: Path) -> None:
        """Same args must produce byte-equal files every time (no datetime/uuid/random)."""
        run1_dir = tmp_path / "run1"
        run1_dir.mkdir()
        sp.scaffold(
            name="det-plugin", skills=["det-skill"], hooks=["PreToolUse"],
            mcp=True, author_name="Tester", author_url="https://t.com",
            output_dir=run1_dir, force=False,
        )

        run2_dir = tmp_path / "run2"
        run2_dir.mkdir()
        sp.scaffold(
            name="det-plugin", skills=["det-skill"], hooks=["PreToolUse"],
            mcp=True, author_name="Tester", author_url="https://t.com",
            output_dir=run2_dir, force=False,
        )

        def file_hashes(base: Path) -> dict[str, str]:
            return {
                str(f.relative_to(base)): hashlib.md5(f.read_bytes()).hexdigest()
                for f in sorted(base.rglob("*")) if f.is_file()
            }

        h1 = file_hashes(run1_dir)
        h2 = file_hashes(run2_dir)
        diffs = {k: (h1.get(k), h2.get(k)) for k in set(h1) | set(h2) if h1.get(k) != h2.get(k)}
        assert not diffs, f"Non-deterministic output — files differ: {diffs}"


class TestScaffoldCLI:
    def test_cli_produces_valid_plugin(self, tmp_path: Path) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "scaffold_plugin.py"),
             "--name", "cli-test", "--output-dir", str(tmp_path)],
            capture_output=True, text=True,
        )
        assert result.returncode == 0, f"Scaffold CLI failed: {result.stderr}"
        plugin_dir = tmp_path / "cli-test"
        assert passes_validator(plugin_dir)
