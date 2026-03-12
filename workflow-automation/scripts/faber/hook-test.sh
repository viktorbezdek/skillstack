#!/usr/bin/env bash
#
# hook-test.sh - Test hook execution with sample data
#
# Usage:
#   hook-test.sh <hook-json>
#   hook-test.sh --file <hook-file.json>
#
# Example:
#   hook-test.sh '{"type":"script","path":"./hook.sh","description":"Test hook"}'
#   hook-test.sh --file my-hook.json

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Parse arguments
if [ $# -eq 0 ]; then
    echo "Usage: hook-test.sh <hook-json>" >&2
    echo "       hook-test.sh --file <hook-file.json>" >&2
    exit 1
fi

if [ "$1" = "--file" ]; then
    if [ ! -f "$2" ]; then
        echo "Hook file not found: $2" >&2
        exit 1
    fi
    HOOK_JSON=$(cat "$2")
else
    HOOK_JSON="$1"
fi

# Sample test context
TEST_CONTEXT=$(cat <<'EOF'
{
  "work_id": "123",
  "phase": "frame",
  "timestamp": "2025-11-20T12:00:00Z",
  "workflow_id": "default",
  "test_mode": true
}
EOF
)

echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${BLUE}       FABER Hook Test${NC}"
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo ""

# Step 1: Validate hook
echo -e "${BLUE}[1/3] Validating hook configuration...${NC}"
echo ""

if "$SCRIPT_DIR/hook-validate.sh" "$HOOK_JSON"; then
    echo ""
    echo -e "${GREEN}✓ Hook validation passed${NC}"
else
    echo ""
    echo -e "${RED}✗ Hook validation failed${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}─────────────────────────────────────${NC}"
echo ""

# Step 2: Display hook details
echo -e "${BLUE}[2/3] Hook details:${NC}"
echo ""

HOOK_TYPE=$(echo "$HOOK_JSON" | jq -r '.type')
HOOK_DESC=$(echo "$HOOK_JSON" | jq -r '.description // "No description"')

echo "  Type: $HOOK_TYPE"
echo "  Description: $HOOK_DESC"

case "$HOOK_TYPE" in
    document|script)
        HOOK_PATH=$(echo "$HOOK_JSON" | jq -r '.path')
        echo "  Path: $HOOK_PATH"
        ;;
    skill)
        SKILL_ID=$(echo "$HOOK_JSON" | jq -r '.skill')
        echo "  Skill: $SKILL_ID"
        ;;
esac

TIMEOUT=$(echo "$HOOK_JSON" | jq -r '.timeout // "30"')
echo "  Timeout: ${TIMEOUT}s"

echo ""
echo -e "${BLUE}─────────────────────────────────────${NC}"
echo ""

# Step 3: Execute hook
echo -e "${BLUE}[3/3] Executing hook with test context...${NC}"
echo ""
echo "Test context:"
echo "$TEST_CONTEXT" | jq '.'
echo ""
echo -e "${BLUE}─────────────────────────────────────${NC}"
echo ""

# Execute hook
set +e
if "$SCRIPT_DIR/hook-execute.sh" "$HOOK_JSON" "$TEST_CONTEXT"; then
    EXIT_CODE=0
else
    EXIT_CODE=$?
fi
set -e

echo ""
echo -e "${BLUE}═══════════════════════════════════════${NC}"

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✓ Hook test completed successfully${NC}"
    echo -e "${BLUE}═══════════════════════════════════════${NC}"
    exit 0
else
    echo -e "${RED}✗ Hook test failed (exit code: $EXIT_CODE)${NC}"
    echo -e "${BLUE}═══════════════════════════════════════${NC}"
    exit $EXIT_CODE
fi
