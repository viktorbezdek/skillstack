#!/bin/bash
# Create Git Worktree with GitFlow conventions.
#
# Usage:
#   ./create_worktree.sh <type> <name> [base-branch]

set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

if [ $# -lt 2 ]; then
    log_error "Usage: $0 <type> <name> [base-branch]"
    echo ""
    echo "Types: feature, fix, hotfix, release"
    echo "Name: descriptive name (kebab-case)"
    echo "Base: main, develop, etc. (default: main)"
    echo ""
    echo "Example:"
    echo "  $0 feature email-notifications"
    echo "  $0 fix login-timeout develop"
    exit 1
fi

TYPE="$1"
NAME="$2"
BASE_BRANCH="${3:-main}"

case "$TYPE" in
    feature|fix|bugfix|hotfix|release)
        ;;
    *)
        log_error "Invalid type: $TYPE"
        echo "Valid types: feature, fix, bugfix, hotfix, release"
        exit 1
        ;;
esac

if [ "$TYPE" = "bugfix" ]; then
    TYPE="fix"
fi

if ! [[ "$NAME" =~ ^[a-z0-9-]+$ ]]; then
    log_warn "Name should be kebab-case (lowercase, hyphens): $NAME"
    echo "Recommended format: feature-name-here"
fi

REPO_ROOT=$(git rev-parse --show-toplevel)
REPO_NAME=$(basename "$REPO_ROOT")
WORKTREE_PARENT="$(dirname "$REPO_ROOT")/${REPO_NAME}-worktrees"
WORKTREE_PATH="$WORKTREE_PARENT/$TYPE/$NAME"
BRANCH_NAME="$TYPE/$NAME"

log_info "Creating worktree..."
log_info "  Repository: $REPO_NAME"
log_info "  Branch: $BRANCH_NAME"
log_info "  Base: $BASE_BRANCH"
log_info "  Path: $WORKTREE_PATH"

if git show-ref --verify --quiet "refs/heads/$BRANCH_NAME"; then
    log_error "Branch already exists: $BRANCH_NAME"
    echo ""
    echo "Options:"
    echo "  1. Use different name"
    echo "  2. Delete existing branch: git branch -D $BRANCH_NAME"
    echo "  3. Use existing branch: git worktree add \"$WORKTREE_PATH\" $BRANCH_NAME"
    exit 1
fi

if [ -d "$WORKTREE_PATH" ]; then
    log_error "Worktree directory already exists: $WORKTREE_PATH"
    exit 1
fi

if ! git show-ref --verify --quiet "refs/heads/$BASE_BRANCH"; then
    log_error "Base branch does not exist: $BASE_BRANCH"
    echo "Available branches:"
    git branch -a
    exit 1
fi

mkdir -p "$WORKTREE_PARENT/$TYPE"

log_info "Creating git worktree..."
git worktree add -b "$BRANCH_NAME" "$WORKTREE_PATH" "$BASE_BRANCH"

echo ""
log_info "Worktree created successfully!"
echo ""
echo "Branch: $BRANCH_NAME"
echo "Path:   $WORKTREE_PATH"
echo ""
echo "Next steps:"
echo "  cd $WORKTREE_PATH"
echo "  git add ."
echo "  git commit -m \"Your message\""
echo "  git push -u origin $BRANCH_NAME"
echo ""
echo "To switch back to main worktree:"
echo "  cd $REPO_ROOT"
echo ""
echo "To remove this worktree when done:"
echo "  git worktree remove $WORKTREE_PATH"
