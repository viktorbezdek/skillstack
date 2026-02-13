#!/usr/bin/env bash
#
# config-validate.sh - Validate FABER configuration against JSON Schema
#
# Usage:
#   config-validate.sh <config-file>
#
# Exit codes:
#   0 - Configuration is valid
#   1 - Validation failed
#   2 - Missing dependencies or file not found
#
# Dependencies:
#   - jq (>=1.6) for JSON validation

set -euo pipefail

# Script directory for resolving paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FABER_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
SCHEMA_PATH="$FABER_ROOT/config/config.schema.json"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function: Print error message
error() {
    echo -e "${RED}✗ Error:${NC} $1" >&2
}

# Function: Print success message
success() {
    echo -e "${GREEN}✓ Success:${NC} $1"
}

# Function: Print warning message
warning() {
    echo -e "${YELLOW}⚠ Warning:${NC} $1"
}

# Function: Check dependencies
check_dependencies() {
    if ! command -v jq &> /dev/null; then
        error "jq is not installed. Install with: brew install jq (macOS) or apt-get install jq (Linux)"
        exit 2
    fi

    # Check jq version (need >= 1.6 for proper schema validation)
    local jq_version
    jq_version=$(jq --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
    if [ -z "$jq_version" ]; then
        warning "Could not determine jq version. Proceeding anyway..."
    fi
}

# Function: Validate JSON syntax
validate_json_syntax() {
    local config_file="$1"

    if ! jq empty "$config_file" 2>/dev/null; then
        error "Invalid JSON syntax in $config_file"
        jq empty "$config_file" 2>&1
        return 1
    fi

    return 0
}

# Function: Validate required fields
validate_required_fields() {
    local config_file="$1"
    local errors=0

    # Check schema_version
    if ! jq -e '.schema_version' "$config_file" > /dev/null 2>&1; then
        error "Missing required field: schema_version"
        errors=$((errors + 1))
    else
        local schema_version
        schema_version=$(jq -r '.schema_version' "$config_file")
        if [[ ! "$schema_version" =~ ^2\. ]]; then
            error "Invalid schema_version: $schema_version (expected 2.x)"
            errors=$((errors + 1))
        fi
    fi

    # Check workflows array
    if ! jq -e '.workflows | type == "array"' "$config_file" > /dev/null 2>&1; then
        error "Missing or invalid required field: workflows (must be an array)"
        errors=$((errors + 1))
    elif [ "$(jq '.workflows | length' "$config_file")" -eq 0 ]; then
        error "workflows array is empty (must have at least one workflow)"
        errors=$((errors + 1))
    fi

    # Check integrations
    if ! jq -e '.integrations' "$config_file" > /dev/null 2>&1; then
        error "Missing required field: integrations"
        errors=$((errors + 1))
    else
        # Check required integration fields
        if ! jq -e '.integrations.work_plugin' "$config_file" > /dev/null 2>&1; then
            error "Missing required field: integrations.work_plugin"
            errors=$((errors + 1))
        fi
        if ! jq -e '.integrations.repo_plugin' "$config_file" > /dev/null 2>&1; then
            error "Missing required field: integrations.repo_plugin"
            errors=$((errors + 1))
        fi
    fi

    return $errors
}

# Function: Validate workflow structure
validate_workflows() {
    local config_file="$1"
    local errors=0
    local workflow_count
    workflow_count=$(jq '.workflows | length' "$config_file")

    for ((i=0; i<workflow_count; i++)); do
        local workflow_id
        workflow_id=$(jq -r ".workflows[$i].id" "$config_file")

        # Validate workflow ID format
        if [[ ! "$workflow_id" =~ ^[a-z][a-z0-9-]*$ ]]; then
            error "Invalid workflow ID format: '$workflow_id' (must be lowercase, hyphens allowed)"
            errors=$((errors + 1))
        fi

        # Check required phases
        local required_phases=("frame" "architect" "build" "evaluate" "release")
        for phase in "${required_phases[@]}"; do
            if ! jq -e ".workflows[$i].phases.$phase" "$config_file" > /dev/null 2>&1; then
                error "Workflow '$workflow_id': Missing required phase '$phase'"
                errors=$((errors + 1))
            fi
        done

        # Check autonomy level
        local autonomy_level
        autonomy_level=$(jq -r ".workflows[$i].autonomy.level" "$config_file" 2>/dev/null || echo "missing")
        case "$autonomy_level" in
            dry-run|assist|guarded|autonomous)
                ;;
            missing)
                error "Workflow '$workflow_id': Missing autonomy.level"
                errors=$((errors + 1))
                ;;
            *)
                error "Workflow '$workflow_id': Invalid autonomy.level '$autonomy_level' (must be: dry-run, assist, guarded, or autonomous)"
                errors=$((errors + 1))
                ;;
        esac
    done

    return $errors
}

# Function: Validate hooks
validate_hooks() {
    local config_file="$1"
    local errors=0
    local workflow_count
    workflow_count=$(jq '.workflows | length' "$config_file")

    for ((i=0; i<workflow_count; i++)); do
        local workflow_id
        workflow_id=$(jq -r ".workflows[$i].id" "$config_file")

        if jq -e ".workflows[$i].hooks" "$config_file" > /dev/null 2>&1; then
            local hook_phases=("pre_frame" "post_frame" "pre_architect" "post_architect" "pre_build" "post_build" "pre_evaluate" "post_evaluate" "pre_release" "post_release")

            for hook_phase in "${hook_phases[@]}"; do
                if jq -e ".workflows[$i].hooks.$hook_phase | length > 0" "$config_file" > /dev/null 2>&1; then
                    local hook_count
                    hook_count=$(jq ".workflows[$i].hooks.$hook_phase | length" "$config_file")

                    for ((j=0; j<hook_count; j++)); do
                        local hook_type
                        hook_type=$(jq -r ".workflows[$i].hooks.$hook_phase[$j].type" "$config_file" 2>/dev/null || echo "missing")

                        case "$hook_type" in
                            document|script)
                                if ! jq -e ".workflows[$i].hooks.$hook_phase[$j].path" "$config_file" > /dev/null 2>&1; then
                                    error "Workflow '$workflow_id', hook '$hook_phase[$j]': Missing 'path' for $hook_type hook"
                                    errors=$((errors + 1))
                                fi
                                ;;
                            skill)
                                if ! jq -e ".workflows[$i].hooks.$hook_phase[$j].skill" "$config_file" > /dev/null 2>&1; then
                                    error "Workflow '$workflow_id', hook '$hook_phase[$j]': Missing 'skill' for skill hook"
                                    errors=$((errors + 1))
                                fi
                                ;;
                            missing)
                                error "Workflow '$workflow_id', hook '$hook_phase[$j]': Missing 'type'"
                                errors=$((errors + 1))
                                ;;
                            *)
                                error "Workflow '$workflow_id', hook '$hook_phase[$j]': Invalid hook type '$hook_type' (must be: document, script, or skill)"
                                errors=$((errors + 1))
                                ;;
                        esac
                    done
                fi
            done
        fi
    done

    return $errors
}

# Main validation function
main() {
    if [ $# -eq 0 ]; then
        echo "Usage: config-validate.sh <config-file>"
        echo ""
        echo "Validates FABER configuration file against JSON Schema."
        echo ""
        echo "Examples:"
        echo "  config-validate.sh .fractary/plugins/faber/config.json"
        echo "  config-validate.sh config/templates/standard.json"
        exit 2
    fi

    local config_file="$1"

    # Check if config file exists
    if [ ! -f "$config_file" ]; then
        error "Configuration file not found: $config_file"
        exit 2
    fi

    # Check if schema exists
    if [ ! -f "$SCHEMA_PATH" ]; then
        error "JSON Schema not found: $SCHEMA_PATH"
        exit 2
    fi

    echo "Validating FABER configuration..."
    echo "Config: $config_file"
    echo "Schema: $SCHEMA_PATH"
    echo ""

    # Check dependencies
    check_dependencies

    # Validate JSON syntax
    if ! validate_json_syntax "$config_file"; then
        exit 1
    fi
    success "JSON syntax is valid"

    # Validate required fields
    if ! validate_required_fields "$config_file"; then
        error "Required field validation failed"
        exit 1
    fi
    success "Required fields are present"

    # Validate workflow structure
    if ! validate_workflows "$config_file"; then
        error "Workflow validation failed"
        exit 1
    fi
    success "Workflow structure is valid"

    # Validate hooks
    if ! validate_hooks "$config_file"; then
        error "Hook validation failed"
        exit 1
    fi
    success "Hooks are valid"

    echo ""
    success "Configuration is valid!"
    echo ""
    echo "Summary:"
    echo "  - Schema version: $(jq -r '.schema_version' "$config_file")"
    echo "  - Workflows: $(jq '.workflows | length' "$config_file")"
    echo "  - Autonomy level: $(jq -r '.workflows[0].autonomy.level' "$config_file")"
    echo "  - Integrations: $(jq -r '.integrations | keys | join(", ")' "$config_file")"

    exit 0
}

main "$@"
