#!/usr/bin/env bash
#
# validate-step-ids.sh - Validate that all step IDs are unique across a workflow
#
# Usage:
#   validate-step-ids.sh <workflow-json-file>
#   validate-step-ids.sh --json <workflow-json-string>
#
# Description:
#   Validates that all step identifiers (id field, or name field for backward
#   compatibility) are unique across all phases in a workflow. This is required
#   because step IDs are used for:
#   - Step targeting via --step argument
#   - Logging and event tracking
#   - State management
#   - Resume functionality
#
# Exit codes:
#   0 - All step IDs are unique
#   1 - Duplicate step IDs found
#   2 - Invalid input or usage error
#
# Example:
#   validate-step-ids.sh .fractary/plugins/faber/workflows/default.json
#   validate-step-ids.sh --json '{"phases":{"build":{"steps":[{"id":"impl"}]}}}'

set -euo pipefail

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Parse arguments
WORKFLOW_JSON=""
INPUT_MODE="file"

if [ $# -eq 0 ]; then
    echo "Usage: validate-step-ids.sh <workflow-json-file>" >&2
    echo "       validate-step-ids.sh --json <workflow-json-string>" >&2
    exit 2
fi

if [ "$1" = "--json" ]; then
    if [ $# -lt 2 ]; then
        echo -e "${RED}Error:${NC} --json requires a JSON string argument" >&2
        exit 2
    fi
    WORKFLOW_JSON="$2"
    INPUT_MODE="json"
else
    if [ ! -f "$1" ]; then
        echo -e "${RED}Error:${NC} File not found: $1" >&2
        exit 2
    fi
    WORKFLOW_JSON=$(cat "$1")
    INPUT_MODE="file"
fi

# Validate JSON
if ! echo "$WORKFLOW_JSON" | jq -e '.' > /dev/null 2>&1; then
    echo -e "${RED}Error:${NC} Invalid JSON" >&2
    exit 2
fi

echo -e "${BLUE}Validating step ID uniqueness...${NC}"
echo ""

# Extract all step IDs across all phases
# For each step, use 'id' if present, otherwise fall back to 'name'
# Track which phase each ID came from for error reporting
STEP_IDS=""
DUPLICATES=""
WARNINGS=""

for phase in frame architect build evaluate release; do
    # Get steps for this phase
    STEPS=$(echo "$WORKFLOW_JSON" | jq -c ".phases.$phase.steps // []")
    STEP_COUNT=$(echo "$STEPS" | jq 'length')

    if [ "$STEP_COUNT" -eq 0 ]; then
        continue
    fi

    for i in $(seq 0 $((STEP_COUNT - 1))); do
        STEP=$(echo "$STEPS" | jq -c ".[$i]")

        # Get ID (prefer 'id' field, fall back to 'name' for backward compatibility)
        STEP_ID=$(echo "$STEP" | jq -r '.id // empty')
        USING_NAME_AS_ID=false

        if [ -z "$STEP_ID" ]; then
            STEP_ID=$(echo "$STEP" | jq -r '.name // empty')
            USING_NAME_AS_ID=true

            if [ -z "$STEP_ID" ]; then
                echo -e "${RED}Error:${NC} Step $i in $phase phase has no 'id' or 'name' field" >&2
                exit 1
            fi
        fi

        # Check for deprecation warning
        if [ "$USING_NAME_AS_ID" = true ]; then
            WARNINGS="${WARNINGS}${YELLOW}Warning:${NC} Step '$STEP_ID' in $phase uses deprecated 'name' as identifier. Add explicit 'id' field.\n"
        fi

        # Check for duplicate
        FULL_KEY="${phase}:${STEP_ID}"

        # Check if this ID was already seen in any phase
        for existing_key in $STEP_IDS; do
            existing_id="${existing_key#*:}"
            if [ "$existing_id" = "$STEP_ID" ]; then
                existing_phase="${existing_key%%:*}"
                DUPLICATES="${DUPLICATES}${RED}Duplicate:${NC} Step ID '$STEP_ID' found in both '$existing_phase' and '$phase' phases\n"
            fi
        done

        STEP_IDS="${STEP_IDS} ${FULL_KEY}"
    done
done

# Report warnings (deprecation)
if [ -n "$WARNINGS" ]; then
    echo -e "${YELLOW}Deprecation Warnings:${NC}"
    echo -e "$WARNINGS"
fi

# Report duplicates and exit with error if found
if [ -n "$DUPLICATES" ]; then
    echo -e "${RED}Step ID Validation Failed${NC}"
    echo ""
    echo -e "$DUPLICATES"
    echo ""
    echo -e "${BLUE}Suggestion:${NC} Rename duplicate step IDs to be unique across all phases."
    echo "Example: 'inspect' -> 'initial-inspect' and 'final-inspect'"
    exit 1
fi

# Count unique IDs
UNIQUE_COUNT=$(echo "$STEP_IDS" | tr ' ' '\n' | grep -v '^$' | wc -l)

echo -e "${GREEN}Step ID Validation Passed${NC}"
echo "  Total steps: $UNIQUE_COUNT"
echo "  All step IDs are unique across phases"
exit 0
