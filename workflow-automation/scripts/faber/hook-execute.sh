#!/usr/bin/env bash
#
# hook-execute.sh - Execute a FABER hook with security validation
#
# Usage:
#   hook-execute.sh <hook-json> [context-json]
#
# Hook Types:
#   - document: Returns path for LLM to read
#   - script: Executes script with timeout
#   - skill: Returns skill invocation instruction
#
# Security Features:
#   - Path validation (prevents directory traversal)
#   - Audit logging (all executions logged)
#   - Restricted execution directories
#
# Example:
#   hook-execute.sh '{"type":"script","path":"./hook.sh"}' '{"work_id":"123","phase":"frame"}'

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${PWD}"
AUDIT_LOG_DIR=".fractary/logs/hooks"
AUDIT_LOG_FILE="${AUDIT_LOG_DIR}/hook-audit.log"

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Audit logging function
audit_log() {
    local status="$1"
    local message="$2"
    local timestamp
    timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)

    # Ensure audit log directory exists
    mkdir -p "$AUDIT_LOG_DIR"

    # Log entry format: timestamp | status | hook_type | path | message
    echo "${timestamp} | ${status} | ${HOOK_TYPE:-unknown} | ${HOOK_PATH:-n/a} | ${message}" >> "$AUDIT_LOG_FILE"
}

# Path validation function - ensures path is within allowed directories
validate_path() {
    local path="$1"
    local path_type="$2"

    # Resolve to absolute path
    local resolved_path
    resolved_path=$(cd "$(dirname "$path")" 2>/dev/null && pwd)/$(basename "$path")

    if [ -z "$resolved_path" ]; then
        audit_log "BLOCKED" "Path resolution failed: $path"
        echo -e "${RED}✗ Security: Cannot resolve path: $path${NC}" >&2
        return 1
    fi

    # Check for directory traversal attempts
    if [[ "$path" == *".."* ]]; then
        audit_log "BLOCKED" "Directory traversal attempt detected: $path"
        echo -e "${RED}✗ Security: Directory traversal not allowed in hook paths${NC}" >&2
        return 1
    fi

    # Allowed base directories:
    # 1. Project root (for project-specific hooks)
    # 2. .fractary directory (for plugin hooks)
    # 3. Plugin directories (for plugin-provided hooks)
    local allowed=false

    # Check if path is under project root
    if [[ "$resolved_path" == "${PROJECT_ROOT}"/* ]]; then
        allowed=true
    fi

    # Check if path is under home .claude/plugins (for installed plugins)
    if [[ "$resolved_path" == "${HOME}/.claude/plugins"/* ]]; then
        allowed=true
    fi

    if [ "$allowed" = false ]; then
        audit_log "BLOCKED" "Path outside allowed directories: $resolved_path"
        echo -e "${RED}✗ Security: Hook path must be within project or plugin directories${NC}" >&2
        echo -e "${RED}  Path: $resolved_path${NC}" >&2
        echo -e "${RED}  Allowed: ${PROJECT_ROOT}/* or ~/.claude/plugins/*${NC}" >&2
        return 1
    fi

    return 0
}

if [ $# -eq 0 ]; then
    echo "Usage: hook-execute.sh <hook-json> [context-json]" >&2
    exit 1
fi

HOOK_JSON="$1"
CONTEXT_JSON="${2:-{}}"
HOOK_PATH=""  # Will be set later for audit logging

# Default timeout (30 seconds)
DEFAULT_TIMEOUT=30

# Validate hook first
if ! "$SCRIPT_DIR/hook-validate.sh" "$HOOK_JSON" > /dev/null 2>&1; then
    echo -e "${RED}✗ Hook validation failed${NC}" >&2
    audit_log "FAILED" "Hook validation failed"
    "$SCRIPT_DIR/error-report.sh" FABER-302
    exit 1
fi

# Parse hook configuration
HOOK_TYPE=$(echo "$HOOK_JSON" | jq -r '.type')
HOOK_TIMEOUT=$(echo "$HOOK_JSON" | jq -r ".timeout // $DEFAULT_TIMEOUT")
HOOK_DESC=$(echo "$HOOK_JSON" | jq -r '.description // "Hook"')

echo -e "${BLUE}▶${NC} Executing hook: $HOOK_DESC"
echo "   Type: $HOOK_TYPE"

# Execute based on type
case "$HOOK_TYPE" in
    document)
        HOOK_PATH=$(echo "$HOOK_JSON" | jq -r '.path')

        # Security: Validate path before access
        if ! validate_path "$HOOK_PATH" "document"; then
            exit 1
        fi

        if [ ! -f "$HOOK_PATH" ]; then
            audit_log "FAILED" "Document not found: $HOOK_PATH"
            echo -e "${RED}✗ Document not found: $HOOK_PATH${NC}" >&2
            "$SCRIPT_DIR/error-report.sh" FABER-303
            exit 1
        fi

        audit_log "SUCCESS" "Document hook accessed: $HOOK_PATH"
        echo ""
        echo -e "${GREEN}✓ Document hook ready${NC}"
        echo ""
        echo "════════════════════════════════════════"
        echo "HOOK DOCUMENT: $HOOK_PATH"
        echo "════════════════════════════════════════"
        echo ""
        echo "ACTION REQUIRED: Read and process the document at:"
        echo "  $HOOK_PATH"
        echo ""
        echo "Context:"
        echo "$CONTEXT_JSON" | jq '.'
        echo ""
        ;;

    script)
        HOOK_PATH=$(echo "$HOOK_JSON" | jq -r '.path')

        # Security: Validate path before execution
        if ! validate_path "$HOOK_PATH" "script"; then
            exit 1
        fi

        if [ ! -f "$HOOK_PATH" ]; then
            audit_log "FAILED" "Script not found: $HOOK_PATH"
            echo -e "${RED}✗ Script not found: $HOOK_PATH${NC}" >&2
            "$SCRIPT_DIR/error-report.sh" FABER-303
            exit 1
        fi

        if [ ! -x "$HOOK_PATH" ]; then
            audit_log "FAILED" "Script not executable: $HOOK_PATH"
            echo -e "${RED}✗ Script is not executable: $HOOK_PATH${NC}" >&2
            echo "Run: chmod +x $HOOK_PATH" >&2
            exit 1
        fi

        audit_log "EXECUTING" "Script hook starting: $HOOK_PATH (timeout: ${HOOK_TIMEOUT}s)"
        echo "   Timeout: ${HOOK_TIMEOUT}s"
        echo ""

        # Create temp file for context
        CONTEXT_FILE=$(mktemp)
        echo "$CONTEXT_JSON" > "$CONTEXT_FILE"

        # Execute script with timeout
        set +e
        if timeout "${HOOK_TIMEOUT}s" "$HOOK_PATH" "$CONTEXT_FILE" 2>&1; then
            EXIT_CODE=$?
        else
            EXIT_CODE=$?
        fi
        set -e

        # Clean up temp file
        rm -f "$CONTEXT_FILE"

        echo ""

        if [ $EXIT_CODE -eq 124 ]; then
            # Timeout exit code
            audit_log "TIMEOUT" "Script hook exceeded timeout: $HOOK_PATH"
            echo -e "${RED}✗ Hook timeout exceeded${NC}" >&2
            "$SCRIPT_DIR/error-report.sh" FABER-301
            exit 1
        elif [ $EXIT_CODE -ne 0 ]; then
            audit_log "FAILED" "Script hook failed with exit code $EXIT_CODE: $HOOK_PATH"
            echo -e "${RED}✗ Hook execution failed (exit code: $EXIT_CODE)${NC}" >&2
            "$SCRIPT_DIR/error-report.sh" FABER-300
            exit 1
        else
            audit_log "SUCCESS" "Script hook completed: $HOOK_PATH"
            echo -e "${GREEN}✓ Hook completed successfully${NC}"
        fi
        ;;

    skill)
        SKILL_ID=$(echo "$HOOK_JSON" | jq -r '.skill')
        SKILL_PARAMS=$(echo "$HOOK_JSON" | jq -r '.parameters // {}')

        # Security: Validate skill ID format (prevent injection)
        if [[ ! "$SKILL_ID" =~ ^[a-zA-Z0-9_:-]+$ ]]; then
            audit_log "BLOCKED" "Invalid skill ID format: $SKILL_ID"
            echo -e "${RED}✗ Security: Invalid skill ID format${NC}" >&2
            exit 1
        fi

        audit_log "SUCCESS" "Skill hook ready: $SKILL_ID"
        echo ""
        echo -e "${GREEN}✓ Skill hook ready${NC}"
        echo ""
        echo "════════════════════════════════════════"
        echo "HOOK SKILL: $SKILL_ID"
        echo "════════════════════════════════════════"
        echo ""
        echo "ACTION REQUIRED: Invoke the skill using the Skill tool:"
        echo ""
        echo "Skill: $SKILL_ID"
        echo ""
        echo "Context:"
        echo "$CONTEXT_JSON" | jq '.'
        echo ""
        if [ "$SKILL_PARAMS" != "{}" ]; then
            echo "Parameters:"
            echo "$SKILL_PARAMS" | jq '.'
            echo ""
        fi
        ;;

    *)
        audit_log "BLOCKED" "Unknown hook type: $HOOK_TYPE"
        echo -e "${RED}✗ Unknown hook type: $HOOK_TYPE${NC}" >&2
        exit 1
        ;;
esac

exit 0
