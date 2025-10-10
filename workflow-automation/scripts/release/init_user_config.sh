#!/usr/bin/env bash
set -euo pipefail

# Initialize user-level semantic-release configuration
#
# Creates a publishable shareable config in user's home directory
# Following XDG-like conventions and npm package structure
#
# Usage:
#   ./init_user_config.sh [--username USERNAME]
#
# Output:
#   ~/semantic-release-config/  (publishable as @USERNAME/semantic-release-config)

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

USERNAME="${USER}"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --username)
            USERNAME="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

USER_CONFIG_DIR="$HOME/semantic-release-config"

echo "==================================================================="
echo "User-Level semantic-release Configuration"
echo "==================================================================="
echo ""
echo "Username: $USERNAME"
echo "Location: $USER_CONFIG_DIR"
echo "Package:  @$USERNAME/semantic-release-config"
echo ""

# Check if already exists - idempotent skip
# ADR: /docs/adr/2025-12-07-idempotency-backup-traceability.md
if [ -d "$USER_CONFIG_DIR" ]; then
    echo "INFO: $USER_CONFIG_DIR already exists, skipping initialization"
    echo ""
    echo "To reinitialize from scratch:"
    echo "  rm -rf $USER_CONFIG_DIR"
    echo "  $0"
    exit 0
fi

# Create directory
mkdir -p "$USER_CONFIG_DIR"

# Copy templates
cp "$TEMPLATE_DIR/package.json" "$USER_CONFIG_DIR/"
cp "$TEMPLATE_DIR/index.js" "$USER_CONFIG_DIR/"
cp "$TEMPLATE_DIR/README.md" "$USER_CONFIG_DIR/"

# Update placeholders
cd "$USER_CONFIG_DIR"

# Update package.json
portable_sed_i "s|@USER/semantic-release-config|@$USERNAME/semantic-release-config|g" package.json
portable_sed_i "s|USER|$USERNAME|g" package.json

# Update README
portable_sed_i "s|@USER/semantic-release-config|@$USERNAME/semantic-release-config|g" README.md
portable_sed_i "s|USER|$USERNAME|g" README.md

# Initialize git repository
git init
git add .
git commit -m "chore: initialize user semantic-release config"

# Create .gitignore
cat > .gitignore <<EOF
node_modules/
*.log
EOF

git add .gitignore
git commit -m "chore: add .gitignore"

echo ""
echo "==================================================================="
echo "✅ User config initialized at: $USER_CONFIG_DIR"
echo "==================================================================="
echo ""
echo "This is YOUR personal semantic-release configuration."
echo ""
echo "Separation of Concerns:"
echo "  - Skill:        $SKILL_DIR  (tool, read-only)"
echo "  - User config:  ~/semantic-release-config/          (your defaults, git-tracked)"
echo "  - Org config:   @company/semantic-release-config   (team standards, npm registry)"
echo "  - Project:      .releaserc.yml                      (project overrides)"
echo ""
echo "Next steps:"
echo ""
echo "1. Customize your defaults:"
echo "   cd $USER_CONFIG_DIR"
echo "   vim index.js"
echo ""
echo "2. Version control (recommended):"
echo "   cd $USER_CONFIG_DIR"
echo "   git remote add origin https://github.com/$USERNAME/semantic-release-config.git"
echo "   git push -u origin main"
echo ""
echo "3. Publish to npm (optional, for sharing):"
echo "   npm publish --access public"
echo ""
echo "4. Use in projects:"
echo "   npm install --save-dev @$USERNAME/semantic-release-config"
echo "   echo \"extends: '@$USERNAME/semantic-release-config'\" > .releaserc.yml"
echo ""
