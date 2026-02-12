#!/usr/bin/env bash
#
# hook-list.sh - List configured hooks for a workflow
#
# Usage:
#   hook-list.sh [workflow-id]
#   hook-list.sh [--phase <phase-name>]
#   hook-list.sh [--verbose]
#
# Example:
#   hook-list.sh                    # List all hooks for default workflow
#   hook-list.sh default            # List all hooks for 'default' workflow
#   hook-list.sh --phase frame      # List only frame phase hooks
#   hook-list.sh --verbose          # Show detailed hook information

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE=".fractary/plugins/faber/config.json"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Parse arguments
WORKFLOW_ID="${1:-default}"
PHASE_FILTER=""
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --phase)
            PHASE_FILTER="$2"
            shift 2
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        --help)
            echo "Usage: hook-list.sh [workflow-id] [--phase <phase>] [--verbose]"
            exit 0
            ;;
        *)
            WORKFLOW_ID="$1"
            shift
            ;;
    esac
done

# Check configuration exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Configuration file not found: $CONFIG_FILE" >&2
    "$SCRIPT_DIR/error-report.sh" FABER-001
    exit 1
fi

# Find workflow
WORKFLOW=$(jq --arg id "$WORKFLOW_ID" '.workflows[] | select(.id == $id)' "$CONFIG_FILE" 2>/dev/null)

if [ -z "$WORKFLOW" ]; then
    echo "Workflow not found: $WORKFLOW_ID" >&2
    exit 1
fi

# Extract hooks
HOOKS=$(echo "$WORKFLOW" | jq -r '.hooks // {}')

if [ "$HOOKS" = "{}" ]; then
    echo "No hooks configured for workflow: $WORKFLOW_ID"
    exit 0
fi

echo -e "${BLUE}Hooks for workflow: $WORKFLOW_ID${NC}"
echo ""

# Phase hook names
PHASE_HOOKS=(
    "pre_frame" "post_frame"
    "pre_architect" "post_architect"
    "pre_build" "post_build"
    "pre_evaluate" "post_evaluate"
    "pre_release" "post_release"
)

# Filter by phase if specified
if [ -n "$PHASE_FILTER" ]; then
    case "$PHASE_FILTER" in
        frame)
            PHASE_HOOKS=("pre_frame" "post_frame")
            ;;
        architect)
            PHASE_HOOKS=("pre_architect" "post_architect")
            ;;
        build)
            PHASE_HOOKS=("pre_build" "post_build")
            ;;
        evaluate)
            PHASE_HOOKS=("pre_evaluate" "post_evaluate")
            ;;
        release)
            PHASE_HOOKS=("pre_release" "post_release")
            ;;
        *)
            echo "Invalid phase: $PHASE_FILTER" >&2
            echo "Valid phases: frame, architect, build, evaluate, release" >&2
            exit 1
            ;;
    esac
fi

TOTAL_HOOKS=0

# List hooks
for HOOK_NAME in "${PHASE_HOOKS[@]}"; do
    HOOK_ARRAY=$(echo "$HOOKS" | jq -c ".$HOOK_NAME // []")

    if [ "$HOOK_ARRAY" = "[]" ]; then
        continue
    fi

    HOOK_COUNT=$(echo "$HOOK_ARRAY" | jq 'length')

    if [ "$HOOK_COUNT" -eq 0 ]; then
        continue
    fi

    # Display phase header
    PHASE_NAME=$(echo "$HOOK_NAME" | sed 's/_/ /g' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) tolower(substr($i,2))}1')
    echo -e "${GREEN}▶ $PHASE_NAME${NC} ($HOOK_COUNT hook(s))"

    # List each hook
    for i in $(seq 0 $((HOOK_COUNT - 1))); do
        HOOK=$(echo "$HOOK_ARRAY" | jq -c ".[$i]")
        HOOK_TYPE=$(echo "$HOOK" | jq -r '.type')
        HOOK_DESC=$(echo "$HOOK" | jq -r '.description // "No description"')

        echo "  $((i + 1)). [$HOOK_TYPE] $HOOK_DESC"

        if $VERBOSE; then
            case "$HOOK_TYPE" in
                document|script)
                    HOOK_PATH=$(echo "$HOOK" | jq -r '.path')
                    echo "     Path: $HOOK_PATH"
                    ;;
                skill)
                    SKILL_ID=$(echo "$HOOK" | jq -r '.skill')
                    echo "     Skill: $SKILL_ID"
                    ;;
            esac

            TIMEOUT=$(echo "$HOOK" | jq -r '.timeout // empty')
            if [ -n "$TIMEOUT" ]; then
                echo "     Timeout: ${TIMEOUT}s"
            fi
        fi

        TOTAL_HOOKS=$((TOTAL_HOOKS + 1))
    done

    echo ""
done

if [ $TOTAL_HOOKS -eq 0 ]; then
    if [ -n "$PHASE_FILTER" ]; then
        echo "No hooks configured for phase: $PHASE_FILTER"
    else
        echo "No hooks configured"
    fi
else
    echo -e "${BLUE}Total hooks: $TOTAL_HOOKS${NC}"
fi

exit 0
