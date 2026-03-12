#!/bin/bash
# List Git Worktrees
#
# Usage:
#   ./list_worktrees.sh [--detailed]
#
# Options:
#   --detailed: Show additional information (commit hash, status)

set -e

DETAILED=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --detailed|-d)
            DETAILED=true
            shift
            ;;
        --help|-h)
            echo "Usage: $0 [--detailed]"
            echo ""
            echo "List all git worktrees"
            echo ""
            echo "Options:"
            echo "  --detailed, -d    Show detailed information"
            echo "  --help, -h        Show this help"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Get repository root
REPO_ROOT=$(git rev-parse --show-toplevel)
REPO_NAME=$(basename "$REPO_ROOT")

echo ""
echo -e "${GREEN}Git Worktrees for ${CYAN}$REPO_NAME${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Get worktree list
worktrees=$(git worktree list --porcelain)

# Parse worktrees
main_found=false
worktree_count=0

while IFS= read -r line; do
    if [[ "$line" == worktree\ * ]]; then
        # Start of new worktree
        path="${line#worktree }"
        branch=""
        commit=""
        is_bare=false

        # Read associated lines
        while IFS= read -r subline; do
            if [[ "$subline" == HEAD\ * ]]; then
                commit="${subline#HEAD }"
            elif [[ "$subline" == branch\ * ]]; then
                branch="${subline#branch }"
                branch="${branch#refs/heads/}"
            elif [[ "$subline" == bare ]]; then
                is_bare=true
            elif [[ -z "$subline" ]]; then
                break
            fi
        done

        # Display worktree
        if [ "$path" = "$REPO_ROOT" ]; then
            # Main worktree
            echo -e "${GREEN}Main Worktree${NC}"
            echo -e "  ${BLUE}Branch:${NC} $branch"
            echo -e "  ${BLUE}Path:${NC}   $path"
            if [ "$DETAILED" = true ]; then
                echo -e "  ${BLUE}Commit:${NC} ${commit:0:7}"
                # Check if dirty
                cd "$path"
                if ! git diff-index --quiet HEAD -- 2>/dev/null; then
                    echo -e "  ${YELLOW}Status: Dirty (uncommitted changes)${NC}"
                else
                    echo -e "  ${GREEN}Status: Clean${NC}"
                fi
            fi
            echo ""
            main_found=true
        else
            # Regular worktree
            ((worktree_count++))
            echo -e "${CYAN}Worktree #$worktree_count${NC}"
            echo -e "  ${BLUE}Branch:${NC} $branch"
            echo -e "  ${BLUE}Path:${NC}   $path"
            if [ "$DETAILED" = true ]; then
                echo -e "  ${BLUE}Commit:${NC} ${commit:0:7}"
                # Check if directory exists and status
                if [ -d "$path" ]; then
                    cd "$path"
                    if ! git diff-index --quiet HEAD -- 2>/dev/null; then
                        echo -e "  ${YELLOW}Status: Dirty (uncommitted changes)${NC}"
                    else
                        echo -e "  ${GREEN}Status: Clean${NC}"
                    fi
                else
                    echo -e "  ${RED}Status: Directory not found (stale)${NC}"
                fi
            fi
            echo ""
        fi
    fi
done <<< "$worktrees"

# Summary
if [ $worktree_count -eq 0 ]; then
    echo -e "${YELLOW}No additional worktrees found${NC}"
    echo ""
    echo "Create a worktree with:"
    echo "  ./create_worktree.sh feature my-feature"
else
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo -e "${GREEN}Total: 1 main + $worktree_count worktree(s)${NC}"
fi

echo ""
