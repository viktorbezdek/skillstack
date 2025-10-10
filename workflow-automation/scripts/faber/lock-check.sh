#!/usr/bin/env bash
# lock-check.sh - Check if workflow is locked
set -euo pipefail
LOCK_FILE=".fractary/plugins/faber/state.json.lock"

if [ -f "$LOCK_FILE" ]; then
    PID=$(cat "$LOCK_FILE" 2>/dev/null || echo "unknown")
    echo "Workflow is locked (PID: $PID)"
    exit 1
else
    echo "Workflow is not locked"
    exit 0
fi
