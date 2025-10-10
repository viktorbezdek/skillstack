#!/usr/bin/env bash
# state-backup.sh - Create timestamped backup of state file
#
# Usage:
#   state-backup.sh --run-id <run-id>
#   state-backup.sh [<state-file>]  # Legacy mode
#
set -euo pipefail

# Parse arguments
if [[ "${1:-}" == "--run-id" ]]; then
    RUN_ID="${2:?Run ID required with --run-id flag}"
    STATE_FILE=".fractary/plugins/faber/runs/$RUN_ID/state.json"
else
    STATE_FILE="${1:-.fractary/plugins/faber/state.json}"
fi

if [ ! -f "$STATE_FILE" ]; then
    exit 0  # No file to backup
fi

BACKUP_DIR="$(dirname "$STATE_FILE")/backups"
mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/state_${TIMESTAMP}.json"

cp "$STATE_FILE" "$BACKUP_FILE"
echo "✓ State backed up to: $BACKUP_FILE" >&2
exit 0
