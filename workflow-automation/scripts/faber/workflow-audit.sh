#!/usr/bin/env bash
#
# workflow-audit.sh - Audit workflow completeness with scoring
#
# Usage:
#   workflow-audit.sh [workflow-id]
#   workflow-audit.sh --verbose
#
# Example:
#   workflow-audit.sh default
#   workflow-audit.sh default --verbose

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
VERBOSE=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --verbose)
            VERBOSE=true
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

echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${BLUE}  FABER Workflow Audit${NC}"
echo -e "${BLUE}  Workflow: $WORKFLOW_ID${NC}"
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo ""

# Scoring categories
SCORE_TOTAL=0
SCORE_MAX=0

# Category: Basic Configuration (20 points)
echo -e "${CYAN}[1/6] Basic Configuration${NC}"
SCORE_BASIC=0
SCORE_BASIC_MAX=20

# Workflow ID (2 points)
if [[ "$WORKFLOW_ID" =~ ^[a-z0-9-]+$ ]]; then
    SCORE_BASIC=$((SCORE_BASIC + 2))
    $VERBOSE && echo "  ✓ Valid workflow ID format (+2)"
fi

# Description (3 points)
DESCRIPTION=$(echo "$WORKFLOW" | jq -r '.description // empty')
if [ -n "$DESCRIPTION" ]; then
    SCORE_BASIC=$((SCORE_BASIC + 3))
    $VERBOSE && echo "  ✓ Workflow description present (+3)"
fi

# Autonomy configuration (5 points)
AUTONOMY=$(echo "$WORKFLOW" | jq -r '.autonomy.level // empty')
if [ -n "$AUTONOMY" ]; then
    SCORE_BASIC=$((SCORE_BASIC + 5))
    $VERBOSE && echo "  ✓ Autonomy level configured: $AUTONOMY (+5)"
fi

# Integration configuration (10 points)
CONFIG_DATA=$(cat "$CONFIG_FILE")
WORK_PLUGIN=$(echo "$CONFIG_DATA" | jq -r '.integrations.work_plugin // empty')
REPO_PLUGIN=$(echo "$CONFIG_DATA" | jq -r '.integrations.repo_plugin // empty')

if [ -n "$WORK_PLUGIN" ]; then
    SCORE_BASIC=$((SCORE_BASIC + 5))
    $VERBOSE && echo "  ✓ Work plugin configured: $WORK_PLUGIN (+5)"
fi

if [ -n "$REPO_PLUGIN" ]; then
    SCORE_BASIC=$((SCORE_BASIC + 5))
    $VERBOSE && echo "  ✓ Repo plugin configured: $REPO_PLUGIN (+5)"
fi

echo "  Score: $SCORE_BASIC/$SCORE_BASIC_MAX"
SCORE_TOTAL=$((SCORE_TOTAL + SCORE_BASIC))
SCORE_MAX=$((SCORE_MAX + SCORE_BASIC_MAX))
echo ""

# Category: Phase Configuration (40 points - 8 per phase)
echo -e "${CYAN}[2/6] Phase Configuration${NC}"
SCORE_PHASES=0
SCORE_PHASES_MAX=40

for PHASE_NAME in frame architect build evaluate release; do
    PHASE=$(echo "$WORKFLOW" | jq -c ".phases.$PHASE_NAME // empty")

    if [ -n "$PHASE" ] && [ "$PHASE" != "null" ]; then
        # Phase exists (2 points)
        PHASE_SCORE=2

        # Phase is enabled (1 point)
        PHASE_ENABLED=$(echo "$PHASE" | jq -r '.enabled // true')
        if [ "$PHASE_ENABLED" = "true" ]; then
            PHASE_SCORE=$((PHASE_SCORE + 1))
        fi

        # Has steps (3 points)
        PHASE_STEPS=$(echo "$PHASE" | jq '.steps // [] | length')
        if [ "$PHASE_STEPS" -gt 0 ]; then
            PHASE_SCORE=$((PHASE_SCORE + 3))
        fi

        # Has validation (2 points)
        PHASE_VALIDATION=$(echo "$PHASE" | jq '.validation // [] | length')
        if [ "$PHASE_VALIDATION" -gt 0 ]; then
            PHASE_SCORE=$((PHASE_SCORE + 2))
        fi

        SCORE_PHASES=$((SCORE_PHASES + PHASE_SCORE))

        if $VERBOSE; then
            echo "  ✓ $PHASE_NAME: $PHASE_STEPS step(s), $PHASE_VALIDATION validation(s) (+$PHASE_SCORE)"
        fi
    else
        $VERBOSE && echo "  ✗ $PHASE_NAME: missing (+0)"
    fi
done

echo "  Score: $SCORE_PHASES/$SCORE_PHASES_MAX"
SCORE_TOTAL=$((SCORE_TOTAL + SCORE_PHASES))
SCORE_MAX=$((SCORE_MAX + SCORE_PHASES_MAX))
echo ""

# Category: Steps Quality (20 points)
echo -e "${CYAN}[3/6] Steps Quality${NC}"
SCORE_STEPS=0
SCORE_STEPS_MAX=20

TOTAL_STEPS=0
STEPS_WITH_SKILLS=0
STEPS_WITH_PARAMS=0
STEPS_WITH_PROMPTS=0
STEPS_WITH_CONDITIONS=0

for PHASE_NAME in frame architect build evaluate release; do
    PHASE=$(echo "$WORKFLOW" | jq -c ".phases.$PHASE_NAME // empty")
    if [ -n "$PHASE" ] && [ "$PHASE" != "null" ]; then
        STEPS=$(echo "$PHASE" | jq -c '.steps // []')
        STEP_COUNT=$(echo "$STEPS" | jq 'length')
        TOTAL_STEPS=$((TOTAL_STEPS + STEP_COUNT))

        for i in $(seq 0 $((STEP_COUNT - 1))); do
            STEP=$(echo "$STEPS" | jq -c ".[$i]")

            # Count steps with skills
            SKILL=$(echo "$STEP" | jq -r '.skill // empty')
            if [ -n "$SKILL" ]; then
                STEPS_WITH_SKILLS=$((STEPS_WITH_SKILLS + 1))
            fi

            # Count steps with explicit prompts
            PROMPT=$(echo "$STEP" | jq -r '.prompt // empty')
            if [ -n "$PROMPT" ]; then
                STEPS_WITH_PROMPTS=$((STEPS_WITH_PROMPTS + 1))
            fi

            # Count steps with parameters
            PARAMS=$(echo "$STEP" | jq -r '.parameters // empty')
            if [ -n "$PARAMS" ] && [ "$PARAMS" != "null" ]; then
                STEPS_WITH_PARAMS=$((STEPS_WITH_PARAMS + 1))
            fi

            # Count steps with conditions
            CONDITION=$(echo "$STEP" | jq -r '.condition // empty')
            if [ -n "$CONDITION" ]; then
                STEPS_WITH_CONDITIONS=$((STEPS_WITH_CONDITIONS + 1))
            fi
        done
    fi
done

# Scoring
if [ $TOTAL_STEPS -gt 0 ]; then
    # Has steps (5 points)
    SCORE_STEPS=$((SCORE_STEPS + 5))

    # Steps use skills (8 points scaled)
    SKILL_PERCENTAGE=$((STEPS_WITH_SKILLS * 100 / TOTAL_STEPS))
    SCORE_STEPS=$((SCORE_STEPS + (SKILL_PERCENTAGE * 8 / 100)))

    # Steps have explicit prompts (3 points scaled)
    if [ $STEPS_WITH_PROMPTS -gt 0 ]; then
        PROMPT_PERCENTAGE=$((STEPS_WITH_PROMPTS * 100 / TOTAL_STEPS))
        SCORE_STEPS=$((SCORE_STEPS + (PROMPT_PERCENTAGE * 3 / 100)))
    fi

    # Steps have parameters (2 points scaled)
    if [ $STEPS_WITH_PARAMS -gt 0 ]; then
        PARAM_PERCENTAGE=$((STEPS_WITH_PARAMS * 100 / TOTAL_STEPS))
        SCORE_STEPS=$((SCORE_STEPS + (PARAM_PERCENTAGE * 2 / 100)))
    fi

    # Steps have conditions (2 points scaled)
    if [ $STEPS_WITH_CONDITIONS -gt 0 ]; then
        CONDITION_PERCENTAGE=$((STEPS_WITH_CONDITIONS * 100 / TOTAL_STEPS))
        SCORE_STEPS=$((SCORE_STEPS + (CONDITION_PERCENTAGE * 2 / 100)))
    fi
fi

if $VERBOSE; then
    echo "  Total steps: $TOTAL_STEPS"
    echo "  Steps with skills: $STEPS_WITH_SKILLS ($SKILL_PERCENTAGE%)"
    [ $STEPS_WITH_PROMPTS -gt 0 ] && echo "  Steps with explicit prompts: $STEPS_WITH_PROMPTS ($PROMPT_PERCENTAGE%)"
    [ $STEPS_WITH_PARAMS -gt 0 ] && echo "  Steps with parameters: $STEPS_WITH_PARAMS"
    [ $STEPS_WITH_CONDITIONS -gt 0 ] && echo "  Steps with conditions: $STEPS_WITH_CONDITIONS"
fi

echo "  Score: $SCORE_STEPS/$SCORE_STEPS_MAX"
SCORE_TOTAL=$((SCORE_TOTAL + SCORE_STEPS))
SCORE_MAX=$((SCORE_MAX + SCORE_STEPS_MAX))
echo ""

# Category: Hooks (10 points)
echo -e "${CYAN}[4/6] Hooks${NC}"
SCORE_HOOKS=0
SCORE_HOOKS_MAX=10

HOOKS=$(echo "$WORKFLOW" | jq -r '.hooks // empty')
HOOK_COUNT=0

if [ -n "$HOOKS" ] && [ "$HOOKS" != "null" ]; then
    for HOOK_NAME in pre_frame post_frame pre_architect post_architect pre_build post_build pre_evaluate post_evaluate pre_release post_release; do
        HOOK_ARRAY=$(echo "$HOOKS" | jq -c ".$HOOK_NAME // []")
        HOOK_ARRAY_COUNT=$(echo "$HOOK_ARRAY" | jq 'length')
        HOOK_COUNT=$((HOOK_COUNT + HOOK_ARRAY_COUNT))
    done
fi

if [ $HOOK_COUNT -gt 0 ]; then
    # Score scales with hook count (max 10 points at 5+ hooks)
    SCORE_HOOKS=$((HOOK_COUNT * 2))
    [ $SCORE_HOOKS -gt 10 ] && SCORE_HOOKS=10

    $VERBOSE && echo "  ✓ Hooks configured: $HOOK_COUNT (+$SCORE_HOOKS)"
else
    $VERBOSE && echo "  ℹ No hooks configured"
fi

echo "  Score: $SCORE_HOOKS/$SCORE_HOOKS_MAX"
SCORE_TOTAL=$((SCORE_TOTAL + SCORE_HOOKS))
SCORE_MAX=$((SCORE_MAX + SCORE_HOOKS_MAX))
echo ""

# Category: Safety & Error Handling (5 points)
echo -e "${CYAN}[5/6] Safety & Error Handling${NC}"
SCORE_SAFETY=0
SCORE_SAFETY_MAX=5

# Check for retry configuration (2 points)
RETRY_COUNT=0
for PHASE_NAME in frame architect build evaluate release; do
    PHASE_RETRY=$(echo "$WORKFLOW" | jq -r ".phases.$PHASE_NAME.retry_count // 0")
    RETRY_COUNT=$((RETRY_COUNT + PHASE_RETRY))
done

if [ $RETRY_COUNT -gt 0 ]; then
    SCORE_SAFETY=$((SCORE_SAFETY + 2))
    $VERBOSE && echo "  ✓ Retry configuration present (+2)"
fi

# Check for safety settings (3 points)
SAFETY=$(echo "$CONFIG_DATA" | jq -r '.safety // empty')
if [ -n "$SAFETY" ] && [ "$SAFETY" != "null" ]; then
    SCORE_SAFETY=$((SCORE_SAFETY + 3))
    $VERBOSE && echo "  ✓ Safety settings configured (+3)"
fi

echo "  Score: $SCORE_SAFETY/$SCORE_SAFETY_MAX"
SCORE_TOTAL=$((SCORE_TOTAL + SCORE_SAFETY))
SCORE_MAX=$((SCORE_MAX + SCORE_SAFETY_MAX))
echo ""

# Category: Documentation (5 points)
echo -e "${CYAN}[6/6] Documentation${NC}"
SCORE_DOCS=0
SCORE_DOCS_MAX=5

# Workflow description (2 points - already checked)
if [ -n "$DESCRIPTION" ]; then
    SCORE_DOCS=$((SCORE_DOCS + 2))
fi

# Step descriptions (3 points)
STEPS_WITH_DESC=0
for PHASE_NAME in frame architect build evaluate release; do
    PHASE=$(echo "$WORKFLOW" | jq -c ".phases.$PHASE_NAME // empty")
    if [ -n "$PHASE" ] && [ "$PHASE" != "null" ]; then
        STEPS=$(echo "$PHASE" | jq -c '.steps // []')
        STEP_COUNT=$(echo "$STEPS" | jq 'length')

        for i in $(seq 0 $((STEP_COUNT - 1))); do
            STEP_DESC=$(echo "$STEPS" | jq -r ".[$i].description // empty")
            if [ -n "$STEP_DESC" ]; then
                STEPS_WITH_DESC=$((STEPS_WITH_DESC + 1))
            fi
        done
    fi
done

if [ $TOTAL_STEPS -gt 0 ] && [ $STEPS_WITH_DESC -eq $TOTAL_STEPS ]; then
    SCORE_DOCS=$((SCORE_DOCS + 3))
    $VERBOSE && echo "  ✓ All steps have descriptions (+3)"
elif [ $STEPS_WITH_DESC -gt 0 ]; then
    DOC_PERCENTAGE=$((STEPS_WITH_DESC * 100 / TOTAL_STEPS))
    PARTIAL_SCORE=$((DOC_PERCENTAGE * 3 / 100))
    SCORE_DOCS=$((SCORE_DOCS + PARTIAL_SCORE))
    $VERBOSE && echo "  ⚠ Partial step documentation: $DOC_PERCENTAGE% (+$PARTIAL_SCORE)"
fi

echo "  Score: $SCORE_DOCS/$SCORE_DOCS_MAX"
SCORE_TOTAL=$((SCORE_TOTAL + SCORE_DOCS))
SCORE_MAX=$((SCORE_MAX + SCORE_DOCS_MAX))
echo ""

# Final Score
SCORE_PERCENTAGE=$((SCORE_TOTAL * 100 / SCORE_MAX))

echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${BLUE}  Final Score${NC}"
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo ""
echo -e "  Total: ${CYAN}$SCORE_TOTAL${NC} / $SCORE_MAX points (${CYAN}$SCORE_PERCENTAGE%${NC})"
echo ""

# Rating
if [ $SCORE_PERCENTAGE -ge 90 ]; then
    echo -e "  Rating: ${GREEN}Excellent${NC} ⭐⭐⭐⭐⭐"
    echo "  Your workflow is comprehensive and well-configured!"
elif [ $SCORE_PERCENTAGE -ge 75 ]; then
    echo -e "  Rating: ${GREEN}Good${NC} ⭐⭐⭐⭐"
    echo "  Your workflow is solid with room for minor improvements."
elif [ $SCORE_PERCENTAGE -ge 60 ]; then
    echo -e "  Rating: ${YELLOW}Fair${NC} ⭐⭐⭐"
    echo "  Your workflow is functional but could be enhanced."
elif [ $SCORE_PERCENTAGE -ge 40 ]; then
    echo -e "  Rating: ${YELLOW}Basic${NC} ⭐⭐"
    echo "  Your workflow is minimal. Consider adding more detail."
else
    echo -e "  Rating: ${RED}Incomplete${NC} ⭐"
    echo "  Your workflow needs significant configuration work."
fi

echo ""
echo "Run 'workflow-recommend.sh $WORKFLOW_ID' for improvement suggestions."
echo ""

exit 0
