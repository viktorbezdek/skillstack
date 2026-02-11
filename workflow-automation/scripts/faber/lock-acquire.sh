#!/usr/bin/env bash
#
# lock-acquire.sh - Acquire workflow lock using flock
#
# Usage:
#   lock-acquire.sh [timeout-seconds]
#
# Exit codes:
#   0 - Lock acquired
#   1 - Lock acquisition failed (timeout or error)
#   2 - Another workflow is running

set -euo pipefail

TIMEOUT="${1:-30}"
LOCK_FILE=".fractary/plugins/faber/state.json.lock"
LOCK_DIR=$(dirname "$LOCK_FILE")

# Create lock directory
mkdir -p "$LOCK_DIR"

# Clean up stale locks (>5 minutes old)
if [ -f "$LOCK_FILE" ]; then
    LOCK_AGE=$(($(date +%s) - $(stat -c %Y "$LOCK_FILE" 2>/dev/null || stat -f %m "$LOCK_FILE" 2>/dev/null || echo 0)))
    if [ $LOCK_AGE -gt 300 ]; then
        echo "⚠ Cleaning up stale lock (${LOCK_AGE}s old)" >&2
        rm -f "$LOCK_FILE"
    fi
fi

# Try to acquire lock with timeout
exec 200>"$LOCK_FILE"
if flock -w "$TIMEOUT" 200 2>/dev/null; then
    echo $$ > "$LOCK_FILE"
    echo "✓ Lock acquired (PID: $$)" >&2
    exit 0
else
    echo "Error: Failed to acquire lock within ${TIMEOUT}s" >&2
    echo "Another FABER workflow may be running" >&2
    exit 2
fi
