#!/usr/bin/env python3
"""Stop hook — retain the conversation transcript to Hindsight (async).

Reads the session transcript, strips injected ``<hindsight_memories>`` blocks
(the feedback-loop guard), formats it, and stores it under a deterministic
per-session document id so re-runs replace rather than duplicate. Fails open on
every error path (exit 0). Wired as ``async`` so it never delays the response.
"""

from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import cli
from lib.transcript import build_retain_chunks, read_transcript


def main() -> None:
    config = cli.load_config()
    if not config["autoRetain"]:
        cli.debug_log(config, "auto-retain disabled")
        return

    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        cli.debug_log(config, "failed to read hook input")
        return

    session_id = hook_input.get("session_id", "unknown")
    transcript_path = hook_input.get("transcript_path", "")

    messages = read_transcript(transcript_path)
    if not messages:
        cli.debug_log(config, "empty transcript, skipping retain")
        return

    chunks = build_retain_chunks(messages, include_tool_calls=config["includeToolCalls"])
    if not chunks:
        cli.debug_log(config, "nothing to retain after stripping")
        return

    base = cli.make_doc_id(session_id)
    bank_id = config["bankId"]
    cli.debug_log(
        config, f"retaining session {session_id} in {len(chunks)} chunk(s) -> base doc {base}"
    )
    # Per-chunk document id so a long, multi-chunk session loses nothing; chunk 0
    # keeps the plain base id for idempotent replacement of single-chunk sessions.
    stored = 0
    for i, chunk in enumerate(chunks):
        doc_id = base if i == 0 else f"{base}-c{i}"
        if cli.retain(config, bank_id, chunk, doc_id, timeout=15):
            stored += 1
    cli.debug_log(config, f"retained {stored}/{len(chunks)} chunk(s) to bank {bank_id}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # fail open
        print(f"[Hindsight] retain error: {e}", file=sys.stderr)
        try:
            sys.exit(2 if cli.load_config()["debug"] else 0)
        except Exception:
            sys.exit(0)
