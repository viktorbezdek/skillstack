#!/usr/bin/env bash
#
# template-apply.sh - Apply variable substitution to FABER configuration template
#
# Usage:
#   template-apply.sh <template-file> <output-file> [VAR=value ...]
#
# Examples:
#   template-apply.sh config.template.json config.json WORK_PLUGIN=fractary-work REPO_PLUGIN=fractary-repo
#
# Exit codes:
#   0 - Success
#   1 - Error

set -euo pipefail

if [ $# -lt 2 ]; then
    echo "Usage: template-apply.sh <template-file> <output-file> [VAR=value ...]"
    echo ""
    echo "Apply variable substitution to template file."
    echo ""
    echo "Variables in template use {{VARIABLE_NAME}} syntax."
    echo ""
    echo "Example:"
    echo "  template-apply.sh config.template.json config.json \\"
    echo "    WORK_PLUGIN=fractary-work \\"
    echo "    REPO_PLUGIN=fractary-repo"
    exit 1
fi

TEMPLATE_FILE="$1"
OUTPUT_FILE="$2"
shift 2

# Check if template exists
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "Error: Template file not found: $TEMPLATE_FILE"
    exit 1
fi

# Read template
CONTENT=$(cat "$TEMPLATE_FILE")

# Apply variable substitutions
for arg in "$@"; do
    if [[ "$arg" =~ ^([A-Z_]+)=(.*)$ ]]; then
        VAR_NAME="${BASH_REMATCH[1]}"
        VAR_VALUE="${BASH_REMATCH[2]}"

        # Replace {{VAR_NAME}} with VAR_VALUE
        CONTENT="${CONTENT//\{\{${VAR_NAME}\}\}/${VAR_VALUE}}"
    fi
done

# Create output directory if needed
OUTPUT_DIR=$(dirname "$OUTPUT_FILE")
mkdir -p "$OUTPUT_DIR"

# Write output
echo "$CONTENT" > "$OUTPUT_FILE"

echo "✓ Template applied successfully"
echo "  Input: $TEMPLATE_FILE"
echo "  Output: $OUTPUT_FILE"

exit 0
