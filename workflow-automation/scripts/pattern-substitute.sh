#!/bin/bash
# FABER Core: Pattern Substitution
# Replaces template variables in strings

set -euo pipefail

# Check arguments
if [ $# -lt 3 ]; then
    echo "Usage: $0 <template> <work_id> <issue_id> [environment] [work_type] [slug]" >&2
    exit 2
fi

TEMPLATE="$1"
WORK_ID="$2"
ISSUE_ID="$3"
ENVIRONMENT="${4:-}"
WORK_TYPE="${5:-}"
SLUG="${6:-}"

# Perform substitutions
RESULT="$TEMPLATE"

# Replace {work_id}
RESULT="${RESULT//\{work_id\}/$WORK_ID}"

# Replace {issue_id}
RESULT="${RESULT//\{issue_id\}/$ISSUE_ID}"

# Replace {environment}
if [ -n "$ENVIRONMENT" ]; then
    RESULT="${RESULT//\{environment\}/$ENVIRONMENT}"
fi

# Replace {work_type} (strip leading / if present)
if [ -n "$WORK_TYPE" ]; then
    WORK_TYPE_CLEAN="${WORK_TYPE#/}"
    RESULT="${RESULT//\{work_type\}/$WORK_TYPE_CLEAN}"
fi

# Replace {slug}
if [ -n "$SLUG" ]; then
    RESULT="${RESULT//\{slug\}/$SLUG}"
fi

# Replace {timestamp} with current timestamp
TIMESTAMP=$(date -u +"%Y%m%d-%H%M%S")
RESULT="${RESULT//\{timestamp\}/$TIMESTAMP}"

# Replace {date} with current date
DATE=$(date -u +"%Y-%m-%d")
RESULT="${RESULT//\{date\}/$DATE}"

# Output result
echo "$RESULT"
exit 0
