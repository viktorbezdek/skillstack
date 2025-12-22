#!/usr/bin/env bash
set -euo pipefail

# Initialize semantic-release in a project
# Level 4 (Project): Creates .releaserc.yml with optional extends
# See SKILL.md for complete 4-level architecture
# Usage:
#   ./init_project.sh [OPTIONS]
#
# Options:
#   --user              Use user config (@username/semantic-release-config)
#   --org ORG/CONFIG    Use org config (@org/config-name)
#   --inline            Use inline config (no extends)
#
# Examples:
#   ./init_project.sh --user
#   ./init_project.sh --org mycompany/semantic-release-config
#   ./init_project.sh --inline

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATES_DIR="$SKILL_DIR/assets/templates"

MODE=""
CONFIG_PACKAGE=""

# Check authentication (Priority 1: SSH, Priority 2: gh CLI)
echo "🔍 Checking authentication..."
echo ""

# Priority 1: Check SSH authentication
echo "Priority 1: SSH Keys (git operations)"
if git remote -v 2>/dev/null | grep -q "git@github.com"; then
    echo "✅ Git remote uses SSH"
    if ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
        echo "✅ SSH authentication working"
    else
        echo "⚠️  SSH remote configured but authentication may not be working"
        echo "   Test: ssh -T git@github.com"
        echo "   See: $SKILL_DIR/references/authentication.md"
    fi
else
    echo "ℹ️  Git remote not using SSH (or not in a git repo yet)"
fi
echo ""

# Priority 2: Check GitHub CLI web authentication
echo "Priority 2: GitHub CLI (GitHub API operations)"
if command -v gh &> /dev/null; then
    if gh auth status &> /dev/null; then
        echo "✅ GitHub CLI authenticated (web-based)"
        echo "   ⚠️  AVOID creating manual tokens - gh CLI handles credentials"
    else
        echo "⚠️  GitHub CLI installed but not authenticated"
        echo "   Run: gh auth login"
        echo "   See: $SKILL_DIR/references/authentication.md"
        echo ""
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
else
    echo "⚠️  GitHub CLI (gh) not found"
    echo "   Install: brew install gh"
    echo "   Then run: gh auth login (web-based, AVOID manual tokens)"
    echo "   See: $SKILL_DIR/references/authentication.md"
    echo ""
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi
echo ""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --user)
            MODE="user"
            CONFIG_PACKAGE="@${USER}/semantic-release-config"
            shift
            ;;
        --org)
            MODE="org"
            CONFIG_PACKAGE="@$2"
            shift 2
            ;;
        --inline)
            MODE="inline"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo ""
            echo "Usage: $0 [--user | --org ORG/CONFIG | --inline]"
            exit 1
            ;;
    esac
done

# Default to inline if not specified
if [ -z "$MODE" ]; then
    MODE="inline"
fi

echo "==================================================================="
echo "semantic-release Project Initialization (Level 4)"
echo "==================================================================="
echo ""

# Check if package.json exists
if [ ! -f "package.json" ]; then
    echo "ERROR: package.json not found"
    echo "Run 'npm init' first"
    exit 1
fi

# Install semantic-release
echo "Installing semantic-release v25+..."
case $MODE in
    user|org)
        echo "  Mode: Shareable config ($CONFIG_PACKAGE)"
        npm install --save-dev semantic-release@^25.0.0 "$CONFIG_PACKAGE"
        ;;
    inline)
        echo "  Mode: Inline configuration"
        npm install --save-dev \
            semantic-release@^25.0.0 \
            @semantic-release/changelog@^6.0.3 \
            @semantic-release/commit-analyzer@^13.0.0 \
            @semantic-release/exec@^6.0.3 \
            @semantic-release/git@^10.0.1 \
            @semantic-release/github@^11.0.1 \
            @semantic-release/release-notes-generator@^14.0.1
        ;;
esac

# Configure package.json
echo "Configuring package.json..."
npm pkg set scripts.release="semantic-release"
npm pkg set version="0.0.0-development"
npm pkg set engines.node=">=22.14.0"

# Create .releaserc.yml with backup + traceability
# ADR: /docs/adr/2025-12-07-idempotency-backup-traceability.md
echo "Creating .releaserc.yml..."
BACKUP_REF="none"
if [ -f .releaserc.yml ]; then
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    BACKUP=".releaserc.yml.bak.${TIMESTAMP}"
    cp .releaserc.yml "$BACKUP"
    BACKUP_REF="./$BACKUP"
    echo "INFO: Backed up existing .releaserc.yml to $BACKUP"
fi

case $MODE in
    user|org)
        cat > .releaserc.yml <<EOF
# Previous version: $BACKUP_REF
# Extends: $CONFIG_PACKAGE
# Level: Project (extends Level 2/3)
extends: "$CONFIG_PACKAGE"
EOF
        ;;
    inline)
        cat > .releaserc.yml <<EOF
# Previous version: $BACKUP_REF
# Inline configuration
# Level: Project (standalone)

branches:
  - main
  - name: beta
    prerelease: true

plugins:
  - "@semantic-release/commit-analyzer"
  - "@semantic-release/release-notes-generator"
  - - "@semantic-release/changelog"
    - changelogFile: CHANGELOG.md
  - "@semantic-release/exec"
  - - "@semantic-release/git"
    - assets:
        - CHANGELOG.md
        - package.json
  - "@semantic-release/github"
EOF
        ;;
esac

# Create GitHub Actions workflow
echo "Creating .github/workflows/release.yml..."
mkdir -p .github/workflows
cp "$TEMPLATES_DIR/github-workflow.yml" .github/workflows/release.yml

# Update .gitignore - exact line match to prevent false positives
# ADR: /docs/adr/2025-12-07-idempotency-backup-traceability.md
if [ -f .gitignore ]; then
    grep -qx "node_modules/" .gitignore || echo "node_modules/" >> .gitignore
else
    echo "node_modules/" > .gitignore
fi

echo ""
echo "==================================================================="
echo "✅ Project initialized successfully!"
echo "==================================================================="
echo ""
echo "Configuration Level: 4 (Project)"
case $MODE in
    user)
        echo "  Extends: Level 2 (User - $CONFIG_PACKAGE)"
        echo ""
        echo "  If $CONFIG_PACKAGE doesn't exist:"
        echo "    cd $SKILL_DIR"
        echo "    ./scripts/init_user_config.sh"
        ;;
    org)
        echo "  Extends: Level 3 (Organization - $CONFIG_PACKAGE)"
        echo ""
        echo "  If $CONFIG_PACKAGE doesn't exist:"
        echo "    cd $SKILL_DIR"
        echo "    ./scripts/create_org_config.sh ORG CONFIG"
        ;;
    inline)
        echo "  Standalone: No extends (all config in .releaserc.yml)"
        ;;
esac
echo ""
echo "Next steps:"
echo "  1. git add ."
echo "  2. git commit -m 'chore: setup semantic-release'"
echo "  3. git push origin main"
echo ""
echo "Conventional Commits format:"
echo "  feat: → MINOR (0.1.0 → 0.2.0)"
echo "  fix: → PATCH (0.1.0 → 0.1.1)"
echo "  BREAKING CHANGE: → MAJOR (0.1.0 → 1.0.0)"
echo ""
