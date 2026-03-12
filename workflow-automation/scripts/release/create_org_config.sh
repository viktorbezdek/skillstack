#!/usr/bin/env bash
set -euo pipefail

# Create organization-level semantic-release configuration
#
# Creates a publishable shareable config for team/company use
# Intended to be published to npm registry and shared across organization
#
# Usage:
#   ./create_org_config.sh <org-name> <config-name> [output-directory]
#
# Example:
#   ./create_org_config.sh mycompany semantic-release-config ~/org-configs/

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_DIR="$SKILL_DIR/assets/templates/shareable-config"

# Portable sed -i (works on both BSD/macOS and GNU/Linux)
portable_sed_i() {
    local pattern="$1"
    local file="$2"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "$pattern" "$file"
    else
        sed -i "$pattern" "$file"
    fi
}

if [ $# -lt 2 ]; then
    echo "Usage: $0 <org-name> <config-name> [output-directory]"
    echo ""
    echo "Example:"
    echo "  $0 mycompany semantic-release-config ~/org-configs/"
    echo ""
    echo "Creates: @mycompany/semantic-release-config"
    exit 1
fi

ORG_NAME="$1"
CONFIG_NAME="$2"
OUTPUT_DIR="${3:-$HOME/org-configs}"

FULL_PATH="$OUTPUT_DIR/$CONFIG_NAME"

echo "==================================================================="
echo "Organization-Level semantic-release Configuration"
echo "==================================================================="
echo ""
echo "Organization: $ORG_NAME"
echo "Config name:  $CONFIG_NAME"
echo "Output:       $FULL_PATH"
echo "Package:      @$ORG_NAME/$CONFIG_NAME"
echo ""

# Create output directory
mkdir -p "$FULL_PATH"

# Copy templates
cp "$TEMPLATE_DIR/package.json" "$FULL_PATH/"
cp "$TEMPLATE_DIR/index.js" "$FULL_PATH/"
cp "$TEMPLATE_DIR/README.md" "$FULL_PATH/"

# Update placeholders
cd "$FULL_PATH"

# Update package.json
portable_sed_i "s|@USER/semantic-release-config|@$ORG_NAME/$CONFIG_NAME|g" package.json
portable_sed_i "s|USER|$ORG_NAME|g" package.json

# Update README
portable_sed_i "s|@USER/semantic-release-config|@$ORG_NAME/$CONFIG_NAME|g" README.md
portable_sed_i "s|USER|$ORG_NAME|g" README.md

# Initialize git repository - idempotent check
# ADR: /docs/adr/2025-12-07-idempotency-backup-traceability.md
if [ ! -d ".git" ]; then
    git init
    git add .
    git commit -m "chore: initialize org semantic-release config" || true  # Allow clean tree
else
    echo "INFO: Git repository already initialized"
fi

cat > .gitignore <<EOF
node_modules/
*.log
EOF

git add .gitignore
git commit -m "chore: add .gitignore"

echo ""
echo "==================================================================="
echo "✅ Organization config created at: $FULL_PATH"
echo "==================================================================="
echo ""
echo "This is your ORGANIZATION's semantic-release configuration."
echo ""
echo "Separation of Concerns:"
echo "  - Skill:        $SKILL_DIR  (tool)"
echo "  - User config:  ~/semantic-release-config/          (personal)"
echo "  - Org config:   $FULL_PATH  (team, THIS)"
echo "  - Project:      .releaserc.yml                      (project)"
echo ""
echo "Next steps:"
echo ""
echo "1. Customize for your organization:"
echo "   cd $FULL_PATH"
echo "   vim index.js"
echo ""
echo "2. Create repository:"
echo "   cd $FULL_PATH"
echo "   gh repo create $ORG_NAME/$CONFIG_NAME --public --source=. --remote=origin"
echo "   git push -u origin main"
echo ""
echo "3. Publish to npm:"
echo "   npm publish --access public"
echo ""
echo "4. Use in projects:"
echo "   npm install --save-dev @$ORG_NAME/$CONFIG_NAME"
echo "   echo \"extends: '@$ORG_NAME/$CONFIG_NAME'\" > .releaserc.yml"
echo ""
