#!/usr/bin/env bash
# lock-release.sh - Release workflow lock
set -euo pipefail
LOCK_FILE=".fractary/plugins/faber/state.json.lock"

if [ -f "$LOCK_FILE" ]; then
    rm -f "$LOCK_FILE"
    echo "✓ Lock released" >&2
fi
exit 0
