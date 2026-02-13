#!/usr/bin/env bash
#
# state-write.sh - Atomically write FABER workflow state
#
# Usage:
#   state-write.sh --run-id <run-id> < state.json
#   state-write.sh [<state-file>] < state.json  # Legacy mode
#   echo '{"status":"completed"}' | state-write.sh
#
# Features:
#   - File locking (flock) for concurrent access safety
#   - Atomic write (temp file + mv)
#   - Automatic backup before write
#   - Timestamp update
#   - JSON validation

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCK_TIMEOUT=30  # seconds to wait for lock

# Parse arguments
if [[ "${1:-}" == "--run-id" ]]; then
    RUN_ID="${2:?Run ID required with --run-id flag}"
    STATE_FILE=".fractary/plugins/faber/runs/$RUN_ID/state.json"
else
    STATE_FILE="${1:-.fractary/plugins/faber/state.json}"
fi

LOCK_FILE="${STATE_FILE}.lock"

# Create state directory if needed
STATE_DIR=$(dirname "$STATE_FILE")
mkdir -p "$STATE_DIR"

# Read new state from stdin (before acquiring lock to minimize lock duration)
NEW_STATE=$(cat)

# Validate JSON (before acquiring lock)
if ! echo "$NEW_STATE" | jq empty 2>/dev/null; then
    echo "Error: Invalid JSON provided" >&2
    exit 1
fi

# Update timestamp (before acquiring lock)
NEW_STATE=$(echo "$NEW_STATE" | jq --arg ts "$(date -u +%Y-%m-%dT%H:%M:%SZ)" '.updated_at = $ts')

# Temp file for atomic write
TEMP_FILE="${STATE_FILE}.tmp.$$"

# Cleanup function
cleanup() {
    rm -f "$TEMP_FILE" 2>/dev/null || true
}
trap cleanup EXIT

# Acquire exclusive lock and perform write
# Using flock with file descriptor 200
exec 200>"$LOCK_FILE"
if ! flock -w "$LOCK_TIMEOUT" 200; then
    echo "Error: Could not acquire lock on $STATE_FILE after ${LOCK_TIMEOUT}s" >&2
    exit 1
fi

# Critical section (under lock)
{
    # Backup existing state if it exists
    if [ -f "$STATE_FILE" ]; then
        "$SCRIPT_DIR/state-backup.sh" "$STATE_FILE" 2>/dev/null || true
    fi

    # Atomic write: temp file + mv
    echo "$NEW_STATE" > "$TEMP_FILE"
    mv "$TEMP_FILE" "$STATE_FILE"
}
# Lock automatically released when fd 200 closes (script exit)

exit 0
