#!/usr/bin/env bash
#
# error-report.sh - Format and report FABER errors with codes
#
# Usage:
#   error-report.sh <error-code> [additional-context]
#
# Example:
#   error-report.sh FABER-001
#   error-report.sh FABER-501 "Work item #123"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ERROR_CODES="$(cd "$SCRIPT_DIR/../../.." && pwd)/config/error-codes.json"

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

if [ $# -eq 0 ]; then
    echo "Usage: error-report.sh <error-code> [context]"
    exit 1
fi

ERROR_CODE="$1"
CONTEXT="${2:-}"

# Load error details
if [ ! -f "$ERROR_CODES" ]; then
    echo -e "${RED}✗ Error:${NC} Error codes file not found" >&2
    exit 1
fi

ERROR_DATA=$(jq -r ".\"$ERROR_CODE\"" "$ERROR_CODES" 2>/dev/null)

if [ "$ERROR_DATA" = "null" ] || [ -z "$ERROR_DATA" ]; then
    echo -e "${RED}✗ Unknown Error Code:${NC} $ERROR_CODE" >&2
    exit 1
fi

# Extract error details
MESSAGE=$(echo "$ERROR_DATA" | jq -r '.message')
SEVERITY=$(echo "$ERROR_DATA" | jq -r '.severity')
CATEGORY=$(echo "$ERROR_DATA" | jq -r '.category')
RECOVERY=$(echo "$ERROR_DATA" | jq -r '.recovery')

# Format severity
case "$SEVERITY" in
    error)
        SEVERITY_COLOR="$RED"
        SEVERITY_ICON="✗"
        ;;
    warning)
        SEVERITY_COLOR="$YELLOW"
        SEVERITY_ICON="⚠"
        ;;
    *)
        SEVERITY_COLOR="$NC"
        SEVERITY_ICON="•"
        ;;
esac

# Report error
echo ""
echo -e "${SEVERITY_COLOR}${SEVERITY_ICON} $ERROR_CODE${NC}: $MESSAGE"
echo -e "${BLUE}Category:${NC} $CATEGORY"
[ -n "$CONTEXT" ] && echo -e "${BLUE}Context:${NC} $CONTEXT"
echo -e "${BLUE}Recovery:${NC} $RECOVERY"
echo ""

# Exit with appropriate code
[ "$SEVERITY" = "error" ] && exit 1 || exit 0
