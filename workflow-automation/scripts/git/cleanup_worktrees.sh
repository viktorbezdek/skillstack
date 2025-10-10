#!/bin/bash
# Cleanup Git Worktrees
#
# Usage:
#   ./cleanup_worktrees.sh [--merged] [--stale] [--dry-run]
#
# Options:
#   --merged:  Remove worktrees for branches that have been merged
#   --stale:   Remove stale worktree registrations
#   --dry-run: Show what would be removed without actually removing
#   --all:     Clean both merged and stale (equivalent to --merged --stale)

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

DRY_RUN=false
CLEAN_MERGED=false
CLEAN_STALE=false

# Parse arguments
if [ $# -eq 0 ]; then
    echo "Usage: $0 [--merged] [--stale] [--all] [--dry-run]"
    echo ""
    echo "Options:"
    echo "  --merged   Remove worktrees for merged branches"
    echo "  --stale    Remove stale worktree registrations"
    echo "  --all      Clean both merged and stale"
    echo "  --dry-run  Show what would be removed"
    echo ""
    echo "Example:"
    echo "  $0 --merged --dry-run"
    echo "  $0 --all"
    exit 1
fi

while [[ $# -gt 0 ]]; do
    case "$1" in
        --merged)
            CLEAN_MERGED=true
            shift
            ;;
        --stale)
            CLEAN_STALE=true
            shift
            ;;
        --all)
            CLEAN_MERGED=true
            CLEAN_STALE=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [--merged] [--stale] [--all] [--dry-run]"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Get repository info
REPO_ROOT=$(git rev-parse --show-toplevel)
REPO_NAME=$(basename "$REPO_ROOT")
MAIN_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || echo "main")

echo ""
log_info "Cleanup Worktrees for $REPO_NAME"
echo ""

if [ "$DRY_RUN" = true ]; then
    log_warn "DRY RUN MODE - No changes will be made"
    echo ""
fi

# Cleanup merged branches
if [ "$CLEAN_MERGED" = true ]; then
    log_info "Checking for merged branches..."

    # Get list of worktrees (excluding main)
    worktrees=$(git worktree list --porcelain)

    merged_count=0

    while IFS= read -r line; do
        if [[ "$line" == worktree\ * ]]; then
            path="${line#worktree }"
            branch=""

            # Read branch line
            while IFS= read -r subline; do
                if [[ "$subline" == branch\ * ]]; then
                    branch="${subline#branch }"
                    branch="${branch#refs/heads/}"
                    break
                elif [[ -z "$subline" ]]; then
                    break
                fi
            done

            # Skip main worktree
            if [ "$path" = "$REPO_ROOT" ]; then
                continue
            fi

            # Check if branch is merged into main
            if [ -n "$branch" ]; then
                if git branch --merged "$MAIN_BRANCH" | grep -q "^\s*$branch\$"; then
                    ((merged_count++))
                    echo -e "${YELLOW}→ Merged branch: ${BLUE}$branch${NC}"
                    echo "  Path: $path"

                    if [ "$DRY_RUN" = false ]; then
                        # Confirm removal
                        read -p "  Remove this worktree? (y/N): " -n 1 -r
                        echo ""
                        if [[ $REPLY =~ ^[Yy]$ ]]; then
                            if [ -d "$path" ]; then
                                git worktree remove "$path" --force
                                log_info "Removed worktree: $branch"
                            else
                                log_warn "Directory not found, removing registration only"
                                git worktree prune
                            fi

                            # Optionally delete branch
                            read -p "  Also delete branch $branch? (y/N): " -n 1 -r
                            echo ""
                            if [[ $REPLY =~ ^[Yy]$ ]]; then
                                git branch -d "$branch"
                                log_info "Deleted branch: $branch"
                            fi
                        else
                            log_info "Skipped"
                        fi
                    else
                        echo "  ${YELLOW}[DRY RUN] Would remove${NC}"
                    fi
                    echo ""
                fi
            fi
        fi
    done <<< "$worktrees"

    if [ $merged_count -eq 0 ]; then
        log_info "No merged worktrees found"
    else
        log_info "Found $merged_count merged worktree(s)"
    fi
    echo ""
fi

# Cleanup stale worktrees
if [ "$CLEAN_STALE" = true ]; then
    log_info "Checking for stale worktrees..."

    # Get worktree list
    worktrees=$(git worktree list --porcelain)

    stale_count=0

    while IFS= read -r line; do
        if [[ "$line" == worktree\ * ]]; then
            path="${line#worktree }"
            branch=""

            # Read branch line
            while IFS= read -r subline; do
                if [[ "$subline" == branch\ * ]]; then
                    branch="${subline#branch }"
                    branch="${branch#refs/heads/}"
                    break
                elif [[ -z "$subline" ]]; then
                    break
                fi
            done

            # Skip main worktree
            if [ "$path" = "$REPO_ROOT" ]; then
                continue
            fi

            # Check if directory exists
            if [ ! -d "$path" ]; then
                ((stale_count++))
                echo -e "${YELLOW}→ Stale worktree: ${BLUE}$branch${NC}"
                echo "  Path: $path (NOT FOUND)"

                if [ "$DRY_RUN" = false ]; then
                    log_info "Pruning stale registration..."
                    git worktree prune
                else
                    echo "  ${YELLOW}[DRY RUN] Would prune${NC}"
                fi
                echo ""
            fi
        fi
    done <<< "$worktrees"

    if [ $stale_count -eq 0 ]; then
        log_info "No stale worktrees found"
    else
        log_info "Found $stale_count stale worktree(s)"
        if [ "$DRY_RUN" = false ]; then
            log_info "Running final prune..."
            git worktree prune
        fi
    fi
    echo ""
fi

log_info "Cleanup complete!"
echo ""

# Show remaining worktrees
log_info "Remaining worktrees:"
git worktree list
echo ""
