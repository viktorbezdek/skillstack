"""Thin wrapper around the installed ``hindsight`` CLI.

The CLI is the transport: it already resolves the API URL / token from its own
configuration (``HINDSIGHT_API_URL`` / ``HINDSIGHT_API_KEY`` env vars, or a
named profile). This module only shells out to it and parses JSON, failing open
(never raising into a hook) so a slow or unreachable server can never block a
turn.

Configuration is env-var driven (no settings file required). All knobs are
namespaced ``HINDSIGHT_CC_*`` to avoid clashing with the CLI's own env vars.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from typing import Any


def _env_bool(name: str, default: bool) -> bool:
    val = os.environ.get(name)
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "on")


def _env_int(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, "").strip())
    except (ValueError, AttributeError):
        return default


def load_config() -> dict[str, Any]:
    """Load integration config from environment with documented defaults."""
    return {
        "bankId": os.environ.get("HINDSIGHT_CC_BANK_ID", "claude_code").strip() or "claude_code",
        "autoRecall": _env_bool("HINDSIGHT_CC_AUTO_RECALL", True),
        "autoRetain": _env_bool("HINDSIGHT_CC_AUTO_RETAIN", True),
        "recallBudget": os.environ.get("HINDSIGHT_CC_RECALL_BUDGET", "mid").strip() or "mid",
        "recallMaxTokens": _env_int("HINDSIGHT_CC_RECALL_MAX_TOKENS", 1024),
        "recallTypes": [
            t.strip()
            for t in os.environ.get("HINDSIGHT_CC_RECALL_TYPES", "world,experience").split(",")
            if t.strip()
        ],
        "maxQueryChars": _env_int("HINDSIGHT_CC_MAX_QUERY_CHARS", 800),
        "retainContext": os.environ.get("HINDSIGHT_CC_RETAIN_CONTEXT", "claude-code").strip()
        or "claude-code",
        "includeToolCalls": _env_bool("HINDSIGHT_CC_RETAIN_TOOL_CALLS", True),
        "profile": os.environ.get("HINDSIGHT_CC_PROFILE", "").strip(),
        "cliBin": os.environ.get("HINDSIGHT_CC_CLI_BIN", "").strip(),
        "debug": _env_bool("HINDSIGHT_CC_DEBUG", False),
    }


def debug_log(config: dict[str, Any], *parts: object) -> None:
    if config.get("debug"):
        print("[Hindsight]", *parts, file=sys.stderr)


def find_cli(config: dict[str, Any]) -> str | None:
    """Resolve the hindsight binary: explicit override, then PATH."""
    explicit = config.get("cliBin")
    if explicit:
        return explicit if os.path.isfile(explicit) else None
    return shutil.which("hindsight")


def make_doc_id(session_id: str) -> str:
    """Deterministic, idempotent document id for a session.

    Stable per session so re-running retain replaces the document instead of
    creating duplicates (the idempotency pattern from the user's pipeline-memory
    package). Compaction note: if the transcript shrinks after compaction, the
    shorter document overwrites the longer one for that session — an accepted
    trade-off for staying state-file-free.
    """
    digest = hashlib.sha256(f"claude-code:{session_id}".encode()).hexdigest()
    return f"cc-{digest[:16]}"


def _base_args(config: dict[str, Any], output_json: bool) -> list[str]:
    binary = find_cli(config)
    if not binary:
        return []
    args = [binary]
    if config.get("profile"):
        args += ["-p", config["profile"]]
    if output_json:
        args += ["-o", "json"]
    return args


def recall(config: dict[str, Any], bank_id: str, query: str, timeout: int = 10) -> list[dict[str, Any]]:
    """Call ``hindsight memory recall`` and return the results list. Fails open to []."""
    base = _base_args(config, output_json=True)
    if not base:
        debug_log(config, "hindsight CLI not found on PATH")
        return []
    cmd = base + ["memory", "recall", bank_id, query]
    cmd += ["--budget", config["recallBudget"]]
    cmd += ["--max-tokens", str(config["recallMaxTokens"])]
    for t in config.get("recallTypes") or []:
        cmd += ["-t", t]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        debug_log(config, f"recall timed out after {timeout}s")
        return []
    except OSError as e:
        debug_log(config, f"recall exec error: {e}")
        return []
    if proc.returncode != 0:
        debug_log(config, f"recall exit {proc.returncode}: {proc.stderr.strip()[:200]}")
        return []
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        debug_log(config, "recall returned non-JSON output")
        return []
    results = data.get("results", []) if isinstance(data, dict) else []
    return results if isinstance(results, list) else []


def retain(config: dict[str, Any], bank_id: str, content: str, doc_id: str, timeout: int = 15) -> bool:
    """Call ``hindsight memory retain --async``. Returns success; fails open to False."""
    base = _base_args(config, output_json=True)
    if not base:
        debug_log(config, "hindsight CLI not found on PATH")
        return False
    cmd = base + [
        "memory",
        "retain",
        bank_id,
        content,
        "-d",
        doc_id,
        "-c",
        config["retainContext"],
        "--async",
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        debug_log(config, f"retain timed out after {timeout}s")
        return False
    except OSError as e:
        debug_log(config, f"retain exec error: {e}")
        return False
    if proc.returncode != 0:
        debug_log(config, f"retain exit {proc.returncode}: {proc.stderr.strip()[:200]}")
        return False
    debug_log(config, f"retained doc {doc_id} to bank {bank_id}")
    return True


def health_ok(config: dict[str, Any], timeout: int = 4) -> bool:
    """Check ``hindsight health``. Fails open to False (never blocks the session)."""
    base = _base_args(config, output_json=True)
    if not base:
        return False
    try:
        proc = subprocess.run(base + ["health"], capture_output=True, text=True, timeout=timeout)
    except (subprocess.TimeoutExpired, OSError):
        return False
    return proc.returncode == 0
