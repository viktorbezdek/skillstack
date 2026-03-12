#!/usr/bin/env bash
#
# step-validate.sh - Validate individual step configuration
#
# Usage:
#   step-validate.sh <step-json>
#
# Examples:
#   step-validate.sh '{"description":"Fetch work item","skill":"fractary-work:issue-fetch"}'
#   step-validate.sh '{"description":"Implement solution","prompt":"Implement based on specification"}'
#   step-validate.sh '{"prompt":"Run tests and report results"}'

set -euo pipefail

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

if [ $# -eq 0 ]; then
    echo "Usage: step-validate.sh <step-json>" >&2
    exit 1
fi

STEP_JSON="$1"
ERRORS=0
WARNINGS=0

echo -e "${BLUE}Validating step configuration...${NC}"
echo ""

# Check step identifier (id field preferred, name field for backward compatibility)
STEP_ID=$(echo "$STEP_JSON" | jq -r '.id // empty')
STEP_NAME=$(echo "$STEP_JSON" | jq -r '.name // empty')

if [ -z "$STEP_ID" ] && [ -z "$STEP_NAME" ]; then
    echo -e "${RED}X${NC} Step must have 'id' field (or 'name' for backward compatibility)" >&2
    ERRORS=$((ERRORS + 1))
elif [ -z "$STEP_ID" ] && [ -n "$STEP_NAME" ]; then
    # Using name as ID - deprecation warning
    echo -e "${YELLOW}!${NC} Step uses deprecated 'name' field as identifier: $STEP_NAME" >&2
    echo "   Add explicit 'id' field for forward compatibility" >&2
    WARNINGS=$((WARNINGS + 1))
    echo -e "${GREEN}OK${NC} Step identifier (from name): $STEP_NAME"
elif [ -n "$STEP_ID" ]; then
    echo -e "${GREEN}OK${NC} Step ID: $STEP_ID"
    if [ -n "$STEP_NAME" ]; then
        echo -e "${GREEN}OK${NC} Step display name: $STEP_NAME"
    fi
fi

# Check description and/or prompt (at least one recommended)
DESCRIPTION=$(echo "$STEP_JSON" | jq -r '.description // empty')
PROMPT=$(echo "$STEP_JSON" | jq -r '.prompt // empty')
SKILL=$(echo "$STEP_JSON" | jq -r '.skill // empty')

if [ -z "$DESCRIPTION" ] && [ -z "$PROMPT" ] && [ -z "$SKILL" ]; then
    echo -e "${RED}✗${NC} Step must have at least one of: description, prompt, or skill" >&2
    ERRORS=$((ERRORS + 1))
fi

# Validate description if present
if [ -n "$DESCRIPTION" ]; then
    echo -e "${GREEN}✓${NC} Description: $DESCRIPTION"
fi

# Validate prompt if present
if [ -n "$PROMPT" ]; then
    echo -e "${GREEN}✓${NC} Prompt: $PROMPT"
fi

# If no skill but no prompt either, suggest adding prompt
if [ -z "$SKILL" ] && [ -z "$PROMPT" ] && [ -n "$DESCRIPTION" ]; then
    echo -e "${YELLOW}⚠${NC} Step has no skill or prompt - description will be used as prompt" >&2
    WARNINGS=$((WARNINGS + 1))
fi

# If both prompt and description present without skill, that's fine (description for docs, prompt for execution)
if [ -n "$PROMPT" ] && [ -n "$DESCRIPTION" ] && [ -z "$SKILL" ]; then
    echo -e "${BLUE}ℹ${NC} Prompt will be used for execution, description for documentation"
fi

# Validate skill if present
if [ -n "$SKILL" ]; then
    # Check skill identifier format (plugin:skill)
    if [[ "$SKILL" =~ ^[a-z0-9-]+:[a-z0-9-]+$ ]]; then
        echo -e "${GREEN}✓${NC} Skill: $SKILL"
    else
        echo -e "${RED}✗${NC} Invalid skill identifier format: $SKILL" >&2
        echo "   Expected format: plugin-name:skill-name" >&2
        ERRORS=$((ERRORS + 1))
    fi
fi

# Check optional parameters
PARAMETERS=$(echo "$STEP_JSON" | jq -r '.parameters // empty')
if [ -n "$PARAMETERS" ] && [ "$PARAMETERS" != "null" ]; then
    # Validate it's a valid JSON object
    if echo "$PARAMETERS" | jq -e 'type == "object"' > /dev/null 2>&1; then
        PARAM_COUNT=$(echo "$PARAMETERS" | jq 'length')
        echo -e "${GREEN}✓${NC} Parameters: $PARAM_COUNT field(s)"
    else
        echo -e "${RED}✗${NC} Parameters must be a JSON object" >&2
        ERRORS=$((ERRORS + 1))
    fi
fi

# Check optional required flag
REQUIRED=$(echo "$STEP_JSON" | jq -r '.required // empty')
if [ -n "$REQUIRED" ]; then
    if [ "$REQUIRED" = "true" ] || [ "$REQUIRED" = "false" ]; then
        echo -e "${GREEN}✓${NC} Required: $REQUIRED"
    else
        echo -e "${RED}✗${NC} Invalid 'required' value: must be true or false" >&2
        ERRORS=$((ERRORS + 1))
    fi
fi

# Check optional condition
CONDITION=$(echo "$STEP_JSON" | jq -r '.condition // empty')
if [ -n "$CONDITION" ]; then
    echo -e "${GREEN}✓${NC} Condition: $CONDITION"
fi

# Check optional retry_count
RETRY_COUNT=$(echo "$STEP_JSON" | jq -r '.retry_count // empty')
if [ -n "$RETRY_COUNT" ]; then
    if [[ "$RETRY_COUNT" =~ ^[0-9]+$ ]]; then
        echo -e "${GREEN}✓${NC} Retry count: $RETRY_COUNT"
    else
        echo -e "${RED}✗${NC} Invalid retry_count: must be a positive integer" >&2
        ERRORS=$((ERRORS + 1))
    fi
fi

# Check optional timeout
TIMEOUT=$(echo "$STEP_JSON" | jq -r '.timeout // empty')
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
    echo -e "${RED}Step validation failed with $ERRORS error(s)${NC}" >&2
    if [ $WARNINGS -gt 0 ]; then
        echo -e "${YELLOW}$WARNINGS warning(s)${NC}" >&2
    fi
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo -e "${YELLOW}Step validation passed with $WARNINGS warning(s)${NC}"
    exit 0
else
    echo -e "${GREEN}Step validation passed${NC}"
    exit 0
fi
