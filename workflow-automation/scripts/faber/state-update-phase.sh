#!/usr/bin/env bash
#
# state-update-phase.sh - Update a specific phase in FABER workflow state
#
# Usage:
#   state-update-phase.sh --run-id <run-id> <phase> <status> [data_json]
#   state-update-phase.sh <phase> <status> [data_json]  # Legacy mode
#
# Arguments:
#   --run-id    - Optional run identifier (format: org/project/uuid)
#   phase       - Phase name (frame, architect, build, evaluate, release)
#   status      - Phase status (pending, in_progress, completed, failed)
#   data_json   - Optional JSON data to store with phase (default: {})
#
# Examples:
#   state-update-phase.sh --run-id "org/project/uuid" frame in_progress
#   state-update-phase.sh --run-id "org/project/uuid" frame completed '{"branch": "feat/123"}'
#   state-update-phase.sh frame started  # Legacy
#   state-update-phase.sh build failed '{"error": "Tests failed"}'  # Legacy
#
# Features:
#   - Updates phase status and timestamps automatically
#   - Handles phase transitions (pending → in_progress → completed)
#   - Updates current_phase if status is in_progress
#   - Preserves existing phase data
#   - Atomic write via state-write.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse arguments
RUN_ID=""
if [[ "${1:-}" == "--run-id" ]]; then
    RUN_ID="${2:?Run ID required with --run-id flag}"
    shift 2
fi

PHASE="${1:?Phase name required (frame, architect, build, evaluate, release)}"
STATUS="${2:?Status required (pending, in_progress, completed, failed)}"
DATA_JSON="${3:-{}}"

# Compute state file path
if [ -n "$RUN_ID" ]; then
    STATE_FILE=".fractary/plugins/faber/runs/$RUN_ID/state.json"
else
    STATE_FILE=".fractary/plugins/faber/state.json"
fi

# Validate phase
case "$PHASE" in
    frame|architect|build|evaluate|release) ;;
    *)
        echo "Error: Invalid phase: $PHASE" >&2
        echo "Valid phases: frame, architect, build, evaluate, release" >&2
        echo "Usage: state-update-phase.sh <phase> <status> [data_json]" >&2
        exit 1
        ;;
esac

# Validate status
case "$STATUS" in
    pending|in_progress|completed|failed) ;;
    *)
        echo "Error: Invalid status: $STATUS" >&2
        echo "Valid statuses: pending, in_progress, completed, failed" >&2
        echo "Usage: state-update-phase.sh <phase> <status> [data_json]" >&2
        exit 1
        ;;
esac

# Validate data JSON
if ! echo "$DATA_JSON" | jq empty 2>/dev/null; then
    echo "Error: Invalid JSON in data parameter" >&2
    exit 1
fi

# Initialize state if it doesn't exist
if [ ! -f "$STATE_FILE" ]; then
    echo "Error: State file not found: $STATE_FILE" >&2
    echo "Initialize state first using state-init.sh" >&2
    exit 1
fi

# Read current state
CURRENT_STATE=$("$SCRIPT_DIR/state-read.sh" "$STATE_FILE")

# Current timestamp
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Build jq update expression based on status
case "$STATUS" in
    in_progress)
        # Set phase to in_progress, record started_at, update current_phase
        UPDATE_EXPR=$(cat <<'EOF'
.phases[$phase].status = $status |
.phases[$phase].started_at = $timestamp |
if .phases[$phase].data then . else .phases[$phase].data = {} end |
.phases[$phase].data += $data |
.current_phase = $phase
EOF
)
        ;;
    completed)
        # Set phase to completed, record completed_at
        UPDATE_EXPR=$(cat <<'EOF'
.phases[$phase].status = $status |
.phases[$phase].completed_at = $timestamp |
if .phases[$phase].data then . else .phases[$phase].data = {} end |
.phases[$phase].data += $data
EOF
)
        ;;
    failed)
        # Set phase to failed, record error
        UPDATE_EXPR=$(cat <<'EOF'
.phases[$phase].status = $status |
.phases[$phase].failed_at = $timestamp |
if .phases[$phase].data then . else .phases[$phase].data = {} end |
.phases[$phase].data += $data |
if .errors then . else .errors = [] end |
.errors += [{
  "phase": $phase,
  "timestamp": $timestamp,
  "data": $data
}]
EOF
)
        ;;
    pending)
        # Reset phase to pending
        UPDATE_EXPR=$(cat <<'EOF'
.phases[$phase].status = $status |
.phases[$phase] |= del(.started_at, .completed_at, .failed_at, .data)
EOF
)
        ;;
esac

# Update state
echo "$CURRENT_STATE" | jq \
    --arg phase "$PHASE" \
    --arg status "$STATUS" \
    --arg timestamp "$TIMESTAMP" \
    --argjson data "$DATA_JSON" \
    "$UPDATE_EXPR" | \
    "$SCRIPT_DIR/state-write.sh" "$STATE_FILE"

exit 0
