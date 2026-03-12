#!/usr/bin/env bash
#
# diagnostics.sh - FABER system health check and diagnostics
#
# Usage:
#   diagnostics.sh [--verbose]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FABER_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
CONFIG_FILE=".fractary/plugins/faber/config.json"
STATE_FILE=".fractary/plugins/faber/state.json"
VERBOSE=false

# Parse args
[[ "${1:-}" == "--verbose" ]] && VERBOSE=true

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "FABER System Diagnostics"
echo "========================"
echo ""

# Check dependencies
echo "Dependencies:"
if command -v jq &> /dev/null; then
    JQ_VERSION=$(jq --version 2>&1 | head -1)
    echo -e "  ${GREEN}✓${NC} jq: $JQ_VERSION"
else
    echo -e "  ${RED}✗${NC} jq: NOT FOUND (required)"
fi

if command -v flock &> /dev/null; then
    echo -e "  ${GREEN}✓${NC} flock: Available"
else
    echo -e "  ${YELLOW}⚠${NC} flock: NOT FOUND (concurrency control disabled)"
fi

# Check configuration
echo ""
echo "Configuration:"
if [ -f "$CONFIG_FILE" ]; then
    echo -e "  ${GREEN}✓${NC} Config file exists: $CONFIG_FILE"
    if "$SCRIPT_DIR/config-validate.sh" "$CONFIG_FILE" > /dev/null 2>&1; then
        echo -e "  ${GREEN}✓${NC} Configuration is valid"
    else
        echo -e "  ${RED}✗${NC} Configuration validation failed"
    fi
else
    echo -e "  ${YELLOW}⚠${NC} Config file not found: $CONFIG_FILE"
    echo "      Run: /fractary-faber:init"
fi

# Check state
echo ""
echo "State:"
if [ -f "$STATE_FILE" ]; then
    echo -e "  ${GREEN}✓${NC} State file exists: $STATE_FILE"
    if "$SCRIPT_DIR/state-validate.sh" "$STATE_FILE" > /dev/null 2>&1; then
        echo -e "  ${GREEN}✓${NC} State is valid"
        if $VERBOSE; then
            WORK_ID=$(jq -r '.work_id // "unknown"' "$STATE_FILE")
            STATUS=$(jq -r '.status // "unknown"' "$STATE_FILE")
            PHASE=$(jq -r '.current_phase // "unknown"' "$STATE_FILE")
            echo "      Work ID: $WORK_ID"
            echo "      Status: $STATUS"
            echo "      Phase: $PHASE"
        fi
    else
        echo -e "  ${RED}✗${NC} State validation failed"
    fi
else
    echo -e "  ${YELLOW}⚠${NC} No active workflow state"
fi

# Check lock
echo ""
echo "Concurrency:"
if "$SCRIPT_DIR/lock-check.sh" > /dev/null 2>&1; then
    echo -e "  ${GREEN}✓${NC} No workflow lock present"
else
    LOCK_INFO=$("$SCRIPT_DIR/lock-check.sh" 2>&1 || true)
    echo -e "  ${YELLOW}⚠${NC} $LOCK_INFO"
fi

# Check plugin integrations
echo ""
echo "Plugin Integrations:"
if [ -f "$CONFIG_FILE" ]; then
    WORK_PLUGIN=$(jq -r '.integrations.work_plugin // "not configured"' "$CONFIG_FILE")
    REPO_PLUGIN=$(jq -r '.integrations.repo_plugin // "not configured"' "$CONFIG_FILE")
    echo "  Work Plugin: $WORK_PLUGIN"
    echo "  Repo Plugin: $REPO_PLUGIN"
else
    echo -e "  ${YELLOW}⚠${NC} Configuration required to check integrations"
fi

echo ""
echo "Diagnostics complete"
exit 0
