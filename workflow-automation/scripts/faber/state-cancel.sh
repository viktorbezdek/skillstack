#!/usr/bin/env bash
#
# state-cancel.sh - Cancel FABER workflow
#
# Usage:
#   state-cancel.sh --run-id <run-id> [reason]
#   state-cancel.sh [reason]  # Legacy mode
#
# Arguments:
#   --run-id  - Optional run identifier (format: org/project/uuid)
#   reason    - Optional cancellation reason (default: "User cancelled")
#
# Examples:
#   state-cancel.sh --run-id "org/project/uuid" "User requested cancellation"
#   state-cancel.sh "User requested cancellation"  # Legacy
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse arguments
RUN_ID=""
if [[ "${1:-}" == "--run-id" ]]; then
    RUN_ID="${2:?Run ID required with --run-id flag}"
    shift 2
fi

REASON="${1:-User cancelled}"

# Compute state file path
if [ -n "$RUN_ID" ]; then
    STATE_FILE=".fractary/plugins/faber/runs/$RUN_ID/state.json"
else
    STATE_FILE=".fractary/plugins/faber/state.json"
fi

# Check if state file exists
if [ ! -f "$STATE_FILE" ]; then
    echo "Error: State file not found: $STATE_FILE" >&2
    echo "No active workflow to cancel" >&2
    exit 1
fi

# Read current state
CURRENT_STATE=$("$SCRIPT_DIR/state-read.sh" "$STATE_FILE")

# Current timestamp
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Update state to cancelled
echo "$CURRENT_STATE" | jq \
    --arg status "cancelled" \
    --arg reason "$REASON" \
    --arg timestamp "$TIMESTAMP" \
    '.status = $status |
     .cancelled_at = $timestamp |
     if .errors then . else .errors = [] end |
     .errors += [{
       "type": "cancellation",
       "timestamp": $timestamp,
       "reason": $reason
     }]' | \
    "$SCRIPT_DIR/state-write.sh" "$STATE_FILE"

echo "Workflow cancelled: $REASON"
exit 0
