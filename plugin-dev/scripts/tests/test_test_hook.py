"""
Tests for test_hook.sh — the mock-stdin hook tester.

Invokes the bash script via subprocess with synthetic hook scripts.
On macOS without coreutils, timeout-dependent tests fail loudly
(never skip silently — see plan critic finding #9).
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

THIS_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = THIS_DIR.parent
TEST_HOOK_SH = SCRIPTS_DIR / "test_hook.sh"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def write_hook(path: Path, content: str) -> Path:
    path.write_text(content)
    path.chmod(0o755)
    return path


def run_test_hook(script: Path, event_json: str, *extra_args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["bash", str(TEST_HOOK_SH), str(script), event_json, *extra_args],
        capture_output=True, text=True,
    )


# ---------------------------------------------------------------------------
# Basic assertions
# ---------------------------------------------------------------------------


class TestTestHookBasic:
    def test_trivial_hook_exits_0_passes(self, tmp_path: Path) -> None:
        hook = write_hook(tmp_path / "ok.sh", "#!/bin/bash\nprintf '{\"ok\":true}'\nexit 0\n")
        result = run_test_hook(hook, "{}", "--expect-exit", "0")
        assert result.returncode == 0, f"Expected 0, got: {result.stderr}"
        assert "OK:" in result.stdout

    def test_exit_code_mismatch_fails(self, tmp_path: Path) -> None:
        hook = write_hook(tmp_path / "ok.sh", "#!/bin/bash\nexit 0\n")
        result = run_test_hook(hook, "{}", "--expect-exit", "1")
        assert result.returncode == 1
        assert "expected exit 1" in result.stderr

    def test_missing_hook_exits_2(self, tmp_path: Path) -> None:
        result = run_test_hook(tmp_path / "nonexistent.sh", "{}")
        assert result.returncode == 2
        assert "not found" in result.stderr

    def test_non_executable_hook_exits_2(self, tmp_path: Path) -> None:
        hook = tmp_path / "not-executable.sh"
        hook.write_text("#!/bin/bash\nexit 0\n")
        hook.chmod(0o644)  # not executable
        result = run_test_hook(hook, "{}")
        assert result.returncode == 2
        assert "not executable" in result.stderr


class TestTestHookStderr:
    def test_stderr_assertion_passes_when_present(self, tmp_path: Path) -> None:
        hook = write_hook(
            tmp_path / "err.sh",
            "#!/bin/bash\necho 'blocked dangerous command' >&2\nexit 2\n",
        )
        result = run_test_hook(
            hook, "{}", "--expect-exit", "2", "--expect-stderr", "blocked"
        )
        assert result.returncode == 0

    def test_stderr_assertion_fails_when_missing(self, tmp_path: Path) -> None:
        hook = write_hook(tmp_path / "quiet.sh", "#!/bin/bash\nexit 2\n")
        result = run_test_hook(
            hook, "{}", "--expect-exit", "2", "--expect-stderr", "blocked"
        )
        assert result.returncode == 1
        assert "blocked" in result.stderr


class TestTestHookTimeout:
    """Timeout tests. Fail loudly if timeout command is unavailable — never skip."""

    @classmethod
    def _check_timeout_available(cls) -> None:
        if not shutil.which("timeout") and not shutil.which("gtimeout"):
            pytest.fail(
                "Neither 'timeout' nor 'gtimeout' found.\n"
                "On macOS: brew install coreutils\n"
                "On Linux: should be available by default (GNU coreutils).\n"
                "This test cannot be skipped — it verifies a core safety feature."
            )

    def test_slow_hook_triggers_timeout(self, tmp_path: Path) -> None:
        self._check_timeout_available()
        hook = write_hook(tmp_path / "slow.sh", "#!/bin/bash\nsleep 60\nexit 0\n")
        result = run_test_hook(hook, "{}", "--timeout", "1")
        assert result.returncode == 3, f"Expected timeout exit 3, got: {result.returncode}"
        assert "timed out" in result.stdout or "timed out" in result.stderr

    def test_fast_hook_does_not_timeout(self, tmp_path: Path) -> None:
        self._check_timeout_available()
        hook = write_hook(tmp_path / "fast.sh", "#!/bin/bash\nexit 0\n")
        result = run_test_hook(hook, "{}", "--timeout", "5")
        assert result.returncode == 0
