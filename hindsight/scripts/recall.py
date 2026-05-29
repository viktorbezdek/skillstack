#!/usr/bin/env python3
"""UserPromptSubmit hook — recall relevant memories and inject them.

Queries the Hindsight bank for memories relevant to the current prompt and
injects them as invisible ``additionalContext``. Fails open on every error
path (exit 0, no output) so a slow or unreachable server never blocks the turn.
"""

from __future__ import annotations

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import cli
from lib.transcript import format_memories

PREAMBLE = (
    "Relevant memories from past sessions (prefer recent when conflicting). "
    "Use only what helps the current task; ignore the rest."
)


def main() -> None:
    config = cli.load_config()
    if not config["autoRecall"]:
        cli.debug_log(config, "auto-recall disabled")
        return

    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        cli.debug_log(config, "failed to read hook input")
        return

    prompt = (hook_input.get("prompt") or hook_input.get("user_prompt") or "").strip()
    if len(prompt) < 5:
        cli.debug_log(config, "prompt too short, skipping recall")
        return

    query = prompt[: config["maxQueryChars"]]
    bank_id = config["bankId"]
    results = cli.recall(config, bank_id, query, timeout=10)
    if not results:
        cli.debug_log(config, "no memories found")
        return

    cli.debug_log(config, f"injecting {len(results)} memories from bank '{bank_id}'")
    current_time = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
    context = (
        f"<hindsight_memories>\n"
        f"{PREAMBLE}\n"
        f"Current time - {current_time}\n\n"
        f"{format_memories(results)}\n"
        f"</hindsight_memories>"
    )
    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }
    json.dump(output, sys.stdout)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # fail open — never block a turn
        print(f"[Hindsight] recall error: {e}", file=sys.stderr)
        try:
            sys.exit(2 if cli.load_config()["debug"] else 0)
        except Exception:
            sys.exit(0)
