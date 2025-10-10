#!/usr/bin/env bash
#
# workflow-recommend.sh - Generate recommendations for workflow improvements
#
# Usage:
#   workflow-recommend.sh [workflow-id]
#   workflow-recommend.sh --priority
#
# Example:
#   workflow-recommend.sh default
#   workflow-recommend.sh default --priority

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE=".fractary/plugins/faber/config.json"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Check configuration exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}✗ Configuration file not found${NC}" >&2
    "$SCRIPT_DIR/error-report.sh" FABER-001
    exit 1
fi

# Parse arguments
WORKFLOW_ID="default"
PRIORITY_ONLY=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --priority)
            PRIORITY_ONLY=true
            shift
            ;;
        *)
            WORKFLOW_ID="$1"
            shift
            ;;
    esac
done

# Load workflow
WORKFLOW=$(jq --arg id "$WORKFLOW_ID" '.workflows[] | select(.id == $id)' "$CONFIG_FILE" 2>/dev/null)

if [ -z "$WORKFLOW" ]; then
    echo -e "${RED}✗ Workflow not found: $WORKFLOW_ID${NC}" >&2
    exit 1
fi

CONFIG_DATA=$(cat "$CONFIG_FILE")

echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${BLUE}  FABER Workflow Recommendations${NC}"
echo -e "${BLUE}  Workflow: $WORKFLOW_ID${NC}"
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo ""

RECOMMENDATIONS=()
PRIORITY_RECOMMENDATIONS=()

# Check basic configuration
DESCRIPTION=$(echo "$WORKFLOW" | jq -r '.description // empty')
if [ -z "$DESCRIPTION" ]; then
    PRIORITY_RECOMMENDATIONS+=("🔴 HIGH: Add a description to document the workflow purpose")
fi

AUTONOMY=$(echo "$WORKFLOW" | jq -r '.autonomy.level // empty')
if [ -z "$AUTONOMY" ]; then
    PRIORITY_RECOMMENDATIONS+=("🔴 HIGH: Configure autonomy level (recommended: guarded)")
    RECOMMENDATIONS+=("   Set workflows[].autonomy.level to: dry-run, assist, guarded, or autonomous")
fi

# Check integrations
WORK_PLUGIN=$(echo "$CONFIG_DATA" | jq -r '.integrations.work_plugin // empty')
REPO_PLUGIN=$(echo "$CONFIG_DATA" | jq -r '.integrations.repo_plugin // empty')
SPEC_PLUGIN=$(echo "$CONFIG_DATA" | jq -r '.integrations.spec_plugin // empty')
LOGS_PLUGIN=$(echo "$CONFIG_DATA" | jq -r '.integrations.logs_plugin // empty')

if [ -z "$WORK_PLUGIN" ]; then
    PRIORITY_RECOMMENDATIONS+=("🔴 HIGH: Configure work plugin integration (fractary-work)")
    RECOMMENDATIONS+=("   Run: /fractary-work:init")
fi

if [ -z "$REPO_PLUGIN" ]; then
    PRIORITY_RECOMMENDATIONS+=("🔴 HIGH: Configure repo plugin integration (fractary-repo)")
    RECOMMENDATIONS+=("   Run: /fractary-repo:init")
fi

if [ -z "$SPEC_PLUGIN" ]; then
    RECOMMENDATIONS+=("🟡 MEDIUM: Consider configuring spec plugin for documentation")
fi

if [ -z "$LOGS_PLUGIN" ]; then
    RECOMMENDATIONS+=("🟡 MEDIUM: Consider configuring logs plugin for audit trail")
fi

# Check each phase
for PHASE_NAME in frame architect build evaluate release; do
    PHASE=$(echo "$WORKFLOW" | jq -c ".phases.$PHASE_NAME // empty")

    if [ -z "$PHASE" ] || [ "$PHASE" = "null" ]; then
        PRIORITY_RECOMMENDATIONS+=("🔴 HIGH: Phase '$PHASE_NAME' is missing - FABER requires all 5 phases")
        continue
    fi

    PHASE_ENABLED=$(echo "$PHASE" | jq -r '.enabled // true')
    PHASE_STEPS=$(echo "$PHASE" | jq '.steps // [] | length')
    PHASE_VALIDATION=$(echo "$PHASE" | jq '.validation // [] | length')

    if [ "$PHASE_ENABLED" = "true" ]; then
        if [ "$PHASE_STEPS" -eq 0 ]; then
            PRIORITY_RECOMMENDATIONS+=("🟠 MEDIUM: Phase '$PHASE_NAME' has no steps - add implementation steps")
        fi

        if [ "$PHASE_VALIDATION" -eq 0 ]; then
            RECOMMENDATIONS+=("🟡 LOW: Phase '$PHASE_NAME' has no validation criteria")
        fi

        # Check for skill and prompt usage
        STEPS=$(echo "$PHASE" | jq -c '.steps // []')
        STEPS_WITH_SKILLS=0
        STEPS_WITH_PROMPTS=0
        STEPS_WITHOUT_SKILL_OR_PROMPT=0
        for i in $(seq 0 $((PHASE_STEPS - 1))); do
            SKILL=$(echo "$STEPS" | jq -r ".[$i].skill // empty")
            PROMPT=$(echo "$STEPS" | jq -r ".[$i].prompt // empty")
            if [ -n "$SKILL" ]; then
                STEPS_WITH_SKILLS=$((STEPS_WITH_SKILLS + 1))
            fi
            if [ -n "$PROMPT" ]; then
                STEPS_WITH_PROMPTS=$((STEPS_WITH_PROMPTS + 1))
            fi
            if [ -z "$SKILL" ] && [ -z "$PROMPT" ]; then
                STEPS_WITHOUT_SKILL_OR_PROMPT=$((STEPS_WITHOUT_SKILL_OR_PROMPT + 1))
            fi
        done

        if [ $PHASE_STEPS -gt 0 ] && [ $STEPS_WITH_SKILLS -eq 0 ]; then
            RECOMMENDATIONS+=("🟡 LOW: Phase '$PHASE_NAME' has no skill-based steps - consider using plugin skills")
        fi

        if [ $STEPS_WITHOUT_SKILL_OR_PROMPT -gt 0 ]; then
            RECOMMENDATIONS+=("🟡 LOW: Phase '$PHASE_NAME' has $STEPS_WITHOUT_SKILL_OR_PROMPT step(s) with neither skill nor prompt - add explicit prompts for clarity")
        fi
    fi
done

# Check hooks
HOOKS=$(echo "$WORKFLOW" | jq -r '.hooks // empty')
HOOK_COUNT=0

if [ -n "$HOOKS" ] && [ "$HOOKS" != "null" ]; then
    for HOOK_NAME in pre_frame post_frame pre_architect post_architect pre_build post_build pre_evaluate post_evaluate pre_release post_release; do
        HOOK_ARRAY=$(echo "$HOOKS" | jq -c ".$HOOK_NAME // []")
        HOOK_ARRAY_COUNT=$(echo "$HOOK_ARRAY" | jq 'length')
        HOOK_COUNT=$((HOOK_COUNT + HOOK_ARRAY_COUNT))
    done
fi

if [ $HOOK_COUNT -eq 0 ]; then
    RECOMMENDATIONS+=("🟢 OPTIONAL: Consider adding phase hooks for custom behavior")
    RECOMMENDATIONS+=("   Examples: pre_release approval, post_frame work item comments")
fi

# Check safety configuration
SAFETY=$(echo "$CONFIG_DATA" | jq -r '.safety // empty')
if [ -z "$SAFETY" ] || [ "$SAFETY" = "null" ]; then
    RECOMMENDATIONS+=("🟡 LOW: Consider adding safety configuration for protected paths")
fi

# Check retry configuration
RETRY_COUNT=0
for PHASE_NAME in frame architect build evaluate release; do
    PHASE_RETRY=$(echo "$WORKFLOW" | jq -r ".phases.$PHASE_NAME.retry_count // 0")
    RETRY_COUNT=$((RETRY_COUNT + PHASE_RETRY))
done

if [ $RETRY_COUNT -eq 0 ]; then
    RECOMMENDATIONS+=("🟡 LOW: Consider adding retry_count to phases for resilience")
    RECOMMENDATIONS+=("   Recommended: 2-3 retries for frame, architect, evaluate phases")
fi

# Display recommendations
if [ ${#PRIORITY_RECOMMENDATIONS[@]} -gt 0 ]; then
    echo -e "${RED}Priority Recommendations:${NC}"
    echo ""
    for rec in "${PRIORITY_RECOMMENDATIONS[@]}"; do
        echo "  $rec"
    done
    echo ""
fi

if ! $PRIORITY_ONLY; then
    if [ ${#RECOMMENDATIONS[@]} -gt 0 ]; then
        echo -e "${YELLOW}Additional Recommendations:${NC}"
        echo ""
        for rec in "${RECOMMENDATIONS[@]}"; do
            echo "  $rec"
        done
        echo ""
    fi
fi

# Summary
TOTAL_RECOMMENDATIONS=$((${#PRIORITY_RECOMMENDATIONS[@]} + ${#RECOMMENDATIONS[@]}))

if [ $TOTAL_RECOMMENDATIONS -eq 0 ]; then
    echo -e "${GREEN}✓ No recommendations - workflow is well-configured!${NC}"
    echo ""
else
    echo -e "${BLUE}═══════════════════════════════════════${NC}"
    echo "  Total recommendations: $TOTAL_RECOMMENDATIONS"
    echo "  Priority: ${#PRIORITY_RECOMMENDATIONS[@]}"
    echo "  Optional: ${#RECOMMENDATIONS[@]}"
    echo -e "${BLUE}═══════════════════════════════════════${NC}"
    echo ""
fi

# Quick start suggestions
if [ ${#PRIORITY_RECOMMENDATIONS[@]} -gt 3 ]; then
    echo -e "${CYAN}Quick Start:${NC}"
    echo ""
    echo "  Your workflow needs significant configuration. Consider:"
    echo ""
    echo "  1. Use a preset template:"
    echo "     cp plugins/faber/config/templates/standard.json $CONFIG_FILE"
    echo ""
    echo "  2. Or run the initialization wizard:"
    echo "     /fractary-faber:init"
    echo ""
fi

echo "For detailed analysis, run: workflow-audit.sh $WORKFLOW_ID --verbose"
echo ""

exit 0
