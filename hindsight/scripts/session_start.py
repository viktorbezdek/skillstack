#!/usr/bin/env python3
"""SessionStart hook — verify Hindsight is reachable.

A lightweight health check. On success it stays silent; on failure it logs to
stderr (only visible with debug enabled) and exits 0. It never blocks a session
and never injects context — per-prompt recall handles context retrieval.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import cli


def main() -> None:
    config = cli.load_config()
    if not (config["autoRecall"] or config["autoRetain"]):
        return
    if cli.find_cli(config) is None:
        cli.debug_log(config, "hindsight CLI not found on PATH — memory disabled")
        return
    if cli.health_ok(config):
        cli.debug_log(config, f"healthy — bank '{config['bankId']}' active")
    else:
        cli.debug_log(config, "health check failed — memory will retry per-prompt")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # fail open
        print(f"[Hindsight] session_start error: {e}", file=sys.stderr)
        sys.exit(0)
