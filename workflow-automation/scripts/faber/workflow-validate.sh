#!/usr/bin/env bash
#
# workflow-validate.sh - Validate complete workflow configuration
#
# Usage:
#   workflow-validate.sh [workflow-id]
#   workflow-validate.sh --all
#
# Example:
#   workflow-validate.sh default
#   workflow-validate.sh --all

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE=".fractary/plugins/faber/config.json"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Check configuration exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}✗ Configuration file not found${NC}" >&2
    "$SCRIPT_DIR/error-report.sh" FABER-001
    exit 1
fi

# Parse arguments
VALIDATE_ALL=false
WORKFLOW_ID="default"

if [ $# -gt 0 ]; then
    if [ "$1" = "--all" ]; then
        VALIDATE_ALL=true
    else
        WORKFLOW_ID="$1"
    fi
fi

TOTAL_ERRORS=0
TOTAL_WARNINGS=0

# Validate workflow(s)
if $VALIDATE_ALL; then
    WORKFLOW_IDS=$(jq -r '.workflows[].id' "$CONFIG_FILE")

    echo -e "${BLUE}Validating all workflows...${NC}"
    echo ""

    for WID in $WORKFLOW_IDS; do
        echo -e "${BLUE}═══════════════════════════════════════${NC}"
        echo -e "${BLUE}  Workflow: $WID${NC}"
        echo -e "${BLUE}═══════════════════════════════════════${NC}"
        echo ""

        set +e
        "$SCRIPT_DIR/workflow-validate.sh" "$WID"
        EXIT_CODE=$?
        set -e

        if [ $EXIT_CODE -ne 0 ]; then
            TOTAL_ERRORS=$((TOTAL_ERRORS + 1))
        fi

        echo ""
    done

    echo -e "${BLUE}═══════════════════════════════════════${NC}"
    echo -e "${BLUE}  Summary${NC}"
    echo -e "${BLUE}═══════════════════════════════════════${NC}"

    WORKFLOW_COUNT=$(echo "$WORKFLOW_IDS" | wc -l)
    echo "Total workflows: $WORKFLOW_COUNT"

    if [ $TOTAL_ERRORS -gt 0 ]; then
        echo -e "${RED}Failed workflows: $TOTAL_ERRORS${NC}"
        exit 1
    else
        echo -e "${GREEN}All workflows passed validation${NC}"
        exit 0
    fi
fi

# Validate single workflow
WORKFLOW=$(jq --arg id "$WORKFLOW_ID" '.workflows[] | select(.id == $id)' "$CONFIG_FILE" 2>/dev/null)

if [ -z "$WORKFLOW" ]; then
    echo -e "${RED}✗ Workflow not found: $WORKFLOW_ID${NC}" >&2
    exit 1
fi

echo -e "${BLUE}Validating workflow: $WORKFLOW_ID${NC}"
echo ""

ERRORS=0
WARNINGS=0

# Check workflow ID format
if [[ ! "$WORKFLOW_ID" =~ ^[a-z0-9-]+$ ]]; then
    echo -e "${RED}✗${NC} Invalid workflow ID format: $WORKFLOW_ID" >&2
    echo "   Must be lowercase alphanumeric with hyphens" >&2
    ERRORS=$((ERRORS + 1))
else
    echo -e "${GREEN}✓${NC} Workflow ID: $WORKFLOW_ID"
fi

# Check description
DESCRIPTION=$(echo "$WORKFLOW" | jq -r '.description // empty')
if [ -z "$DESCRIPTION" ]; then
    echo -e "${YELLOW}⚠${NC} Missing workflow description" >&2
    WARNINGS=$((WARNINGS + 1))
else
    echo -e "${GREEN}✓${NC} Description: $DESCRIPTION"
fi

# Check phases
PHASES=$(echo "$WORKFLOW" | jq -r '.phases // empty')
if [ -z "$PHASES" ] || [ "$PHASES" = "null" ]; then
    echo -e "${RED}✗${NC} Missing phases configuration" >&2
    ERRORS=$((ERRORS + 1))
else
    echo ""
    echo -e "${BLUE}Validating phases...${NC}"
    echo ""

    # Validate each phase
    for PHASE_NAME in frame architect build evaluate release; do
        PHASE=$(echo "$PHASES" | jq -c ".$PHASE_NAME // empty")

        if [ -z "$PHASE" ] || [ "$PHASE" = "null" ]; then
            echo -e "${RED}✗${NC} Missing phase: $PHASE_NAME" >&2
            ERRORS=$((ERRORS + 1))
        else
            echo "  ▶ $PHASE_NAME"

            # Validate phase using phase-validate.sh
            set +e
            PHASE_RESULT=$("$SCRIPT_DIR/phase-validate.sh" "$PHASE" 2>&1)
            PHASE_EXIT=$?
            set -e

            if [ $PHASE_EXIT -ne 0 ]; then
                # Count errors from phase validation
                PHASE_ERRORS=$(echo "$PHASE_RESULT" | grep -c "✗" || true)
                ERRORS=$((ERRORS + PHASE_ERRORS))
                echo "$PHASE_RESULT" | sed 's/^/    /'
            else
                # Count warnings
                PHASE_WARNINGS=$(echo "$PHASE_RESULT" | grep -c "⚠" || true)
                WARNINGS=$((WARNINGS + PHASE_WARNINGS))

                # Show summary only
                PHASE_ENABLED=$(echo "$PHASE" | jq -r '.enabled // true')
                PHASE_STEPS=$(echo "$PHASE" | jq '.steps // [] | length')
                echo "    Status: $([ "$PHASE_ENABLED" = "true" ] && echo "enabled" || echo "disabled"), $PHASE_STEPS step(s)"
            fi
        fi
        echo ""
    done
fi

# Validate step ID uniqueness across all phases
echo -e "${BLUE}Validating step ID uniqueness...${NC}"
echo ""

# Get workflow file path for step ID validation
WORKFLOW_FILE=$(jq -r --arg id "$WORKFLOW_ID" '.workflows[] | select(.id == $id) | .file' "$CONFIG_FILE" 2>/dev/null)

if [ -n "$WORKFLOW_FILE" ] && [ "$WORKFLOW_FILE" != "null" ]; then
    # Resolve relative path from config directory
    CONFIG_DIR=$(dirname "$CONFIG_FILE")
    WORKFLOW_FULL_PATH="$CONFIG_DIR/${WORKFLOW_FILE#./}"

    if [ -f "$WORKFLOW_FULL_PATH" ]; then
        set +e
        STEP_ID_RESULT=$("$SCRIPT_DIR/validate-step-ids.sh" "$WORKFLOW_FULL_PATH" 2>&1)
        STEP_ID_EXIT=$?
        set -e

        if [ $STEP_ID_EXIT -ne 0 ]; then
            echo "$STEP_ID_RESULT" | sed 's/^/  /'
            ERRORS=$((ERRORS + 1))
        else
            # Check for deprecation warnings in output
            if echo "$STEP_ID_RESULT" | grep -q "Warning:"; then
                STEP_WARNINGS=$(echo "$STEP_ID_RESULT" | grep -c "Warning:" || true)
                WARNINGS=$((WARNINGS + STEP_WARNINGS))
            fi
            echo -e "  ${GREEN}OK${NC} All step IDs are unique across phases"
        fi
    else
        echo -e "  ${YELLOW}!${NC} Workflow file not found for step ID validation: $WORKFLOW_FULL_PATH"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo -e "  ${BLUE}i${NC} Skipping step ID validation (embedded workflow)"
fi
echo ""

# Check hooks
HOOKS=$(echo "$WORKFLOW" | jq -r '.hooks // empty')
if [ -n "$HOOKS" ] && [ "$HOOKS" != "null" ]; then
    echo -e "${BLUE}Validating hooks...${NC}"
    echo ""

    HOOK_COUNT=0

    for HOOK_NAME in pre_frame post_frame pre_architect post_architect pre_build post_build pre_evaluate post_evaluate pre_release post_release; do
        HOOK_ARRAY=$(echo "$HOOKS" | jq -c ".$HOOK_NAME // []")
        HOOK_ARRAY_COUNT=$(echo "$HOOK_ARRAY" | jq 'length')

        if [ "$HOOK_ARRAY_COUNT" -gt 0 ]; then
            HOOK_COUNT=$((HOOK_COUNT + HOOK_ARRAY_COUNT))

            # Validate each hook
            for i in $(seq 0 $((HOOK_ARRAY_COUNT - 1))); do
                HOOK=$(echo "$HOOK_ARRAY" | jq -c ".[$i]")

                # Validate hook using hook-validate.sh
                set +e
                if ! "$SCRIPT_DIR/hook-validate.sh" "$HOOK" > /dev/null 2>&1; then
                    echo -e "${RED}✗${NC} Invalid hook in $HOOK_NAME[$i]" >&2
                    ERRORS=$((ERRORS + 1))
                fi
                set -e
            done
        fi
    done

    if [ $HOOK_COUNT -gt 0 ]; then
        echo -e "${GREEN}✓${NC} Hooks configured: $HOOK_COUNT"
    else
        echo -e "${BLUE}ℹ${NC} No hooks configured"
    fi
    echo ""
else
    echo -e "${BLUE}ℹ${NC} No hooks configured"
    echo ""
fi

# Check autonomy
AUTONOMY=$(echo "$WORKFLOW" | jq -r '.autonomy // empty')
if [ -n "$AUTONOMY" ] && [ "$AUTONOMY" != "null" ]; then
    AUTONOMY_LEVEL=$(echo "$AUTONOMY" | jq -r '.level // empty')

    if [ -z "$AUTONOMY_LEVEL" ]; then
        echo -e "${YELLOW}⚠${NC} Autonomy configured but missing 'level' field" >&2
        WARNINGS=$((WARNINGS + 1))
    else
        case "$AUTONOMY_LEVEL" in
            dry-run|assist|guarded|autonomous)
                echo -e "${GREEN}✓${NC} Autonomy level: $AUTONOMY_LEVEL"
                ;;
            *)
                echo -e "${RED}✗${NC} Invalid autonomy level: $AUTONOMY_LEVEL" >&2
                echo "   Must be: dry-run, assist, guarded, or autonomous" >&2
                ERRORS=$((ERRORS + 1))
                ;;
        esac
    fi
else
    echo -e "${YELLOW}⚠${NC} No autonomy configuration (will use defaults)" >&2
    WARNINGS=$((WARNINGS + 1))
fi

# Summary
echo ""
echo -e "${BLUE}═══════════════════════════════════════${NC}"

if [ $ERRORS -gt 0 ]; then
    echo -e "${RED}Workflow validation failed with $ERRORS error(s)${NC}" >&2
    if [ $WARNINGS -gt 0 ]; then
        echo -e "${YELLOW}$WARNINGS warning(s)${NC}" >&2
    fi
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo -e "${YELLOW}Workflow validation passed with $WARNINGS warning(s)${NC}"
    exit 0
else
    echo -e "${GREEN}Workflow validation passed${NC}"
    exit 0
fi
