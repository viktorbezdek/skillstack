#!/usr/bin/env bash
#
# state-init.sh - Initialize FABER workflow state
#
# Usage:
#   state-init.sh --run-id <run-id> <work-id> [workflow-id]
#   state-init.sh <work-id> [workflow-id] [<state-file>]  # Legacy mode
#
# Examples:
#   state-init.sh --run-id "org/project/uuid" "123" "default"
#   state-init.sh "123" "default"  # Legacy

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Parse arguments
RUN_ID=""
if [[ "${1:-}" == "--run-id" ]]; then
    RUN_ID="${2:?Run ID required with --run-id flag}"
    shift 2
fi

WORK_ID="${1:?Work ID required}"
WORKFLOW_ID="${2:-default}"

# Compute state file path
if [ -n "$RUN_ID" ]; then
    STATE_FILE=".fractary/plugins/faber/runs/$RUN_ID/state.json"
else
    STATE_FILE="${3:-.fractary/plugins/faber/state.json}"
fi

# Create state directory if needed
STATE_DIR=$(dirname "$STATE_FILE")
mkdir -p "$STATE_DIR"

# Build initial state with run_id if provided
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)

if [ -n "$RUN_ID" ]; then
    INITIAL_STATE=$(cat <<EOF
{
  "run_id": "$RUN_ID",
  "work_id": "$WORK_ID",
  "workflow_id": "$WORKFLOW_ID",
  "workflow_version": "2.1",
  "status": "in_progress",
  "current_phase": "frame",
  "last_event_id": 0,
  "started_at": "$TIMESTAMP",
  "updated_at": "$TIMESTAMP",
  "completed_at": null,
  "phases": {
    "frame": {"status": "pending", "steps": [], "retry_count": 0},
    "architect": {"status": "pending", "steps": [], "retry_count": 0},
    "build": {"status": "pending", "steps": [], "retry_count": 0},
    "evaluate": {"status": "pending", "steps": [], "retry_count": 0},
    "release": {"status": "pending", "steps": [], "retry_count": 0}
  },
  "artifacts": {},
  "errors": []
}
EOF
)
else
    # Legacy format without run_id
    INITIAL_STATE=$(cat <<EOF
{
  "work_id": "$WORK_ID",
  "workflow_id": "$WORKFLOW_ID",
  "workflow_version": "2.0",
  "status": "in_progress",
  "current_phase": "frame",
  "started_at": "$TIMESTAMP",
  "updated_at": "$TIMESTAMP",
  "phases": {
    "frame": {"status": "pending"},
    "architect": {"status": "pending"},
    "build": {"status": "pending"},
    "evaluate": {"status": "pending"},
    "release": {"status": "pending"}
  },
  "artifacts": {},
  "retries": {},
  "errors": []
}
EOF
)
fi

# Write state atomically
echo "$INITIAL_STATE" | "$SCRIPT_DIR/state-write.sh" "$STATE_FILE"

if [ -n "$RUN_ID" ]; then
    echo "✓ State initialized for run: $RUN_ID (work item: $WORK_ID)"
else
    echo "✓ State initialized for work item: $WORK_ID"
fi
exit 0
