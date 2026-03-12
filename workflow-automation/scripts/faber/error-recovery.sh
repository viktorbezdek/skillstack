#!/usr/bin/env bash
# error-recovery.sh - Suggest recovery actions for error codes
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ERROR_CODES="$(cd "$SCRIPT_DIR/../../.." && pwd)/config/error-codes.json"

ERROR_CODE="${1:?Error code required}"

if [ ! -f "$ERROR_CODES" ]; then
    echo "Error: error-codes.json not found" >&2
    exit 1
fi

RECOVERY=$(jq -r ".\"$ERROR_CODE\".recovery" "$ERROR_CODES" 2>/dev/null)

if [ "$RECOVERY" = "null" ] || [ -z "$RECOVERY" ]; then
    echo "No recovery suggestion available for $ERROR_CODE"
    exit 1
fi

echo "$RECOVERY"
exit 0
