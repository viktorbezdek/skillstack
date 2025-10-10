#!/usr/bin/env bash
#
# hook-validate.sh - Validate hook configuration
#
# Usage:
#   hook-validate.sh <hook-json>
#
# Example:
#   hook-validate.sh '{"type":"script","path":"./scripts/hook.sh"}'

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

if [ $# -eq 0 ]; then
    echo "Usage: hook-validate.sh <hook-json>" >&2
    exit 1
fi

HOOK_JSON="$1"
ERRORS=0

# Parse hook type
HOOK_TYPE=$(echo "$HOOK_JSON" | jq -r '.type // empty' 2>/dev/null)

if [ -z "$HOOK_TYPE" ]; then
    echo -e "${RED}✗${NC} Hook type is required" >&2
    ERRORS=$((ERRORS + 1))
else
    # Validate hook type
    case "$HOOK_TYPE" in
        document|script|skill)
            echo -e "${GREEN}✓${NC} Hook type: $HOOK_TYPE"
            ;;
        *)
            echo -e "${RED}✗${NC} Invalid hook type: $HOOK_TYPE (must be: document, script, or skill)" >&2
            ERRORS=$((ERRORS + 1))
            ;;
    esac
fi

# Type-specific validation
case "$HOOK_TYPE" in
    document)
        HOOK_PATH=$(echo "$HOOK_JSON" | jq -r '.path // empty' 2>/dev/null)
        if [ -z "$HOOK_PATH" ]; then
            echo -e "${RED}✗${NC} Document hook requires 'path' field" >&2
            ERRORS=$((ERRORS + 1))
        elif [ ! -f "$HOOK_PATH" ]; then
            echo -e "${RED}✗${NC} Document not found: $HOOK_PATH" >&2
            ERRORS=$((ERRORS + 1))
        else
            # Check if it's a markdown file
            if [[ "$HOOK_PATH" =~ \.md$ ]]; then
                echo -e "${GREEN}✓${NC} Document exists: $HOOK_PATH"
            else
                echo -e "${YELLOW}⚠${NC} Document is not markdown: $HOOK_PATH" >&2
            fi
        fi
        ;;

    script)
        HOOK_PATH=$(echo "$HOOK_JSON" | jq -r '.path // empty' 2>/dev/null)
        if [ -z "$HOOK_PATH" ]; then
            echo -e "${RED}✗${NC} Script hook requires 'path' field" >&2
            ERRORS=$((ERRORS + 1))
        elif [ ! -f "$HOOK_PATH" ]; then
            echo -e "${RED}✗${NC} Script not found: $HOOK_PATH" >&2
            ERRORS=$((ERRORS + 1))
        else
            echo -e "${GREEN}✓${NC} Script exists: $HOOK_PATH"

            # Check if executable
            if [ ! -x "$HOOK_PATH" ]; then
                echo -e "${YELLOW}⚠${NC} Script is not executable: $HOOK_PATH" >&2
                echo "   Run: chmod +x $HOOK_PATH" >&2
            else
                echo -e "${GREEN}✓${NC} Script is executable"
            fi
        fi
        ;;

    skill)
        SKILL_ID=$(echo "$HOOK_JSON" | jq -r '.skill // empty' 2>/dev/null)
        if [ -z "$SKILL_ID" ]; then
            echo -e "${RED}✗${NC} Skill hook requires 'skill' field" >&2
            ERRORS=$((ERRORS + 1))
        else
            # Validate skill identifier format (plugin:skill)
            if [[ "$SKILL_ID" =~ ^[a-z0-9-]+:[a-z0-9-]+$ ]]; then
                echo -e "${GREEN}✓${NC} Skill identifier: $SKILL_ID"
            else
                echo -e "${RED}✗${NC} Invalid skill identifier format: $SKILL_ID" >&2
                echo "   Expected format: plugin-name:skill-name" >&2
                ERRORS=$((ERRORS + 1))
            fi
        fi
        ;;
esac

# Validate optional timeout
TIMEOUT=$(echo "$HOOK_JSON" | jq -r '.timeout // empty' 2>/dev/null)
if [ -n "$TIMEOUT" ]; then
    if [[ "$TIMEOUT" =~ ^[0-9]+$ ]]; then
        echo -e "${GREEN}✓${NC} Timeout: ${TIMEOUT}s"
    else
        echo -e "${RED}✗${NC} Invalid timeout value: $TIMEOUT (must be a positive integer)" >&2
        ERRORS=$((ERRORS + 1))
    fi
fi

# Validate optional description
DESCRIPTION=$(echo "$HOOK_JSON" | jq -r '.description // empty' 2>/dev/null)
if [ -n "$DESCRIPTION" ]; then
    echo -e "${GREEN}✓${NC} Description: $DESCRIPTION"
fi

# Exit with error if validation failed
if [ $ERRORS -gt 0 ]; then
    echo ""
    echo -e "${RED}Validation failed with $ERRORS error(s)${NC}" >&2
    exit 1
fi

echo ""
echo -e "${GREEN}Hook validation passed${NC}"
exit 0
