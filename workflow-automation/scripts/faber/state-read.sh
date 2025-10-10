#!/usr/bin/env bash
#
# state-read.sh - Safely read FABER workflow state
#
# Usage:
#   state-read.sh --run-id <run-id> [<jq-query>]
#   state-read.sh [<state-file>] [<jq-query>]  # Legacy mode
#
# Examples:
#   state-read.sh --run-id "org/project/uuid"            # Read entire state
#   state-read.sh --run-id "org/project/uuid" '.status'  # Query specific field
#   state-read.sh '.current_phase'                        # Legacy: query with default file
#   state-read.sh state.json '.status'                    # Legacy: custom file + query
#
# Features:
#   - Shared locking (flock -s) for read consistency during writes

set -euo pipefail

LOCK_TIMEOUT=10  # seconds to wait for shared lock

# Parse arguments
RUN_ID=""
if [[ "${1:-}" == "--run-id" ]]; then
    RUN_ID="${2:?Run ID required with --run-id flag}"
    shift 2
    STATE_FILE=".fractary/plugins/faber/runs/$RUN_ID/state.json"
    JQ_QUERY="${1:-.}"
else
    STATE_FILE="${1:-.fractary/plugins/faber/state.json}"
    JQ_QUERY="${2:-.}"

    # Legacy: Shift if first arg is a jq query (starts with .)
    if [[ "$STATE_FILE" != .* ]] && [[ "$STATE_FILE" != /* ]] && [[ "$STATE_FILE" == *.json ]]; then
        JQ_QUERY="${2:-.}"
    elif [[ "$STATE_FILE" == .* ]]; then
        # First arg is a query, use default file
        JQ_QUERY="$STATE_FILE"
        STATE_FILE=".fractary/plugins/faber/state.json"
    fi
fi

if [ ! -f "$STATE_FILE" ]; then
    echo "Error: State file not found: $STATE_FILE" >&2
    exit 1
fi

LOCK_FILE="${STATE_FILE}.lock"

# Acquire shared lock for consistent read
# Multiple readers can hold shared lock; exclusive lock blocks until all readers finish
exec 200>"$LOCK_FILE"
if ! flock -s -w "$LOCK_TIMEOUT" 200; then
    echo "Error: Could not acquire read lock on $STATE_FILE after ${LOCK_TIMEOUT}s" >&2
    exit 1
fi

# Read and query state with jq (under shared lock)
jq -r "$JQ_QUERY" "$STATE_FILE" 2>/dev/null || {
    echo "Error: Failed to read state file or invalid jq query" >&2
    exit 1
}
# Lock automatically released when fd 200 closes (script exit)
