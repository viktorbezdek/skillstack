#!/usr/bin/env bash
#
# phase-validate.sh - Validate individual phase configuration
#
# Usage:
#   phase-validate.sh <phase-json>
#   phase-validate.sh --name <phase-name> --workflow <workflow-id>
#
# Example:
#   phase-validate.sh '{"enabled":true,"steps":[...]}'
#   phase-validate.sh --name frame --workflow default

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE=".fractary/plugins/faber/config.json"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Parse arguments
if [ $# -eq 0 ]; then
    echo "Usage: phase-validate.sh <phase-json>" >&2
    echo "       phase-validate.sh --name <phase-name> --workflow <workflow-id>" >&2
    exit 1
fi

PHASE_JSON=""
PHASE_NAME=""
WORKFLOW_ID="default"

if [ "$1" = "--name" ]; then
    PHASE_NAME="$2"
    shift 2

    if [ "${1:-}" = "--workflow" ]; then
        WORKFLOW_ID="$2"
        shift 2
    fi

    # Load phase from configuration
    if [ ! -f "$CONFIG_FILE" ]; then
        echo -e "${RED}✗ Configuration file not found${NC}" >&2
        "$SCRIPT_DIR/error-report.sh" FABER-001
        exit 1
    fi

    PHASE_JSON=$(jq --arg wid "$WORKFLOW_ID" --arg phase "$PHASE_NAME" \
        '.workflows[] | select(.id == $wid) | .phases[$phase]' "$CONFIG_FILE" 2>/dev/null)

    if [ -z "$PHASE_JSON" ] || [ "$PHASE_JSON" = "null" ]; then
        echo -e "${RED}✗ Phase not found: $PHASE_NAME in workflow $WORKFLOW_ID${NC}" >&2
        exit 1
    fi
else
    PHASE_JSON="$1"
fi

ERRORS=0
WARNINGS=0

echo -e "${BLUE}Validating phase configuration...${NC}"
echo ""

# Check enabled field
ENABLED=$(echo "$PHASE_JSON" | jq -r '.enabled // empty')
if [ -z "$ENABLED" ]; then
    echo -e "${YELLOW}⚠${NC} Missing 'enabled' field (assuming true)" >&2
    WARNINGS=$((WARNINGS + 1))
    ENABLED="true"
else
    if [ "$ENABLED" = "true" ]; then
        echo -e "${GREEN}✓${NC} Phase is enabled"
    else
        echo -e "${BLUE}ℹ${NC} Phase is disabled"
        # Fewer checks needed for disabled phases
    fi
fi

# Check steps
STEPS=$(echo "$PHASE_JSON" | jq -c '.steps // []')
STEP_COUNT=$(echo "$STEPS" | jq 'length')

if [ "$STEP_COUNT" -eq 0 ]; then
    if [ "$ENABLED" = "true" ]; then
        echo -e "${YELLOW}⚠${NC} No steps defined (phase will do nothing)" >&2
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo -e "${GREEN}✓${NC} Steps defined: $STEP_COUNT"

    # Validate each step
    for i in $(seq 0 $((STEP_COUNT - 1))); do
        STEP=$(echo "$STEPS" | jq -c ".[$i]")

        # Check step has description
        STEP_DESC=$(echo "$STEP" | jq -r '.description // empty')
        if [ -z "$STEP_DESC" ]; then
            echo -e "${RED}✗${NC} Step $((i + 1)) missing 'description' field" >&2
            ERRORS=$((ERRORS + 1))
        fi

        # Check step has action or skill
        STEP_ACTION=$(echo "$STEP" | jq -r '.action // empty')
        STEP_SKILL=$(echo "$STEP" | jq -r '.skill // empty')

        if [ -z "$STEP_ACTION" ] && [ -z "$STEP_SKILL" ]; then
            echo -e "${RED}✗${NC} Step $((i + 1)) missing 'action' or 'skill' field" >&2
            ERRORS=$((ERRORS + 1))
        fi

        # Validate skill format if present
        if [ -n "$STEP_SKILL" ]; then
            if [[ ! "$STEP_SKILL" =~ ^[a-z0-9-]+:[a-z0-9-]+$ ]]; then
                echo -e "${RED}✗${NC} Step $((i + 1)) has invalid skill format: $STEP_SKILL" >&2
                echo "   Expected format: plugin-name:skill-name" >&2
                ERRORS=$((ERRORS + 1))
            fi
        fi
    done
fi

# Check validation criteria
VALIDATION=$(echo "$PHASE_JSON" | jq -c '.validation // []')
VALIDATION_COUNT=$(echo "$VALIDATION" | jq 'length')

if [ "$VALIDATION_COUNT" -eq 0 ]; then
    if [ "$ENABLED" = "true" ]; then
        echo -e "${YELLOW}⚠${NC} No validation criteria defined" >&2
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo -e "${GREEN}✓${NC} Validation criteria: $VALIDATION_COUNT"

    # Validate each criterion
    for i in $(seq 0 $((VALIDATION_COUNT - 1))); do
        CRITERION=$(echo "$VALIDATION" | jq -c ".[$i]")

        # Check criterion has description
        CRIT_DESC=$(echo "$CRITERION" | jq -r '.description // empty')
        if [ -z "$CRIT_DESC" ]; then
            echo -e "${RED}✗${NC} Validation $((i + 1)) missing 'description' field" >&2
            ERRORS=$((ERRORS + 1))
        fi

        # Check criterion has check field
        CRIT_CHECK=$(echo "$CRITERION" | jq -r '.check // empty')
        if [ -z "$CRIT_CHECK" ]; then
            echo -e "${RED}✗${NC} Validation $((i + 1)) missing 'check' field" >&2
            ERRORS=$((ERRORS + 1))
        fi
    done
fi

# Check optional fields
RETRY_COUNT=$(echo "$PHASE_JSON" | jq -r '.retry_count // empty')
if [ -n "$RETRY_COUNT" ]; then
    if [[ "$RETRY_COUNT" =~ ^[0-9]+$ ]]; then
        echo -e "${GREEN}✓${NC} Retry count: $RETRY_COUNT"
    else
        echo -e "${RED}✗${NC} Invalid retry_count: must be a positive integer" >&2
        ERRORS=$((ERRORS + 1))
    fi
fi

TIMEOUT=$(echo "$PHASE_JSON" | jq -r '.timeout // empty')
if [ -n "$TIMEOUT" ]; then
    if [[ "$TIMEOUT" =~ ^[0-9]+$ ]]; then
        echo -e "${GREEN}✓${NC} Timeout: ${TIMEOUT}s"
    else
        echo -e "${RED}✗${NC} Invalid timeout: must be a positive integer" >&2
        ERRORS=$((ERRORS + 1))
    fi
fi

# Summary
echo ""
if [ $ERRORS -gt 0 ]; then
    echo -e "${RED}Phase validation failed with $ERRORS error(s)${NC}" >&2
    if [ $WARNINGS -gt 0 ]; then
        echo -e "${YELLOW}$WARNINGS warning(s)${NC}" >&2
    fi
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo -e "${YELLOW}Phase validation passed with $WARNINGS warning(s)${NC}"
    exit 0
else
    echo -e "${GREEN}Phase validation passed${NC}"
    exit 0
fi
