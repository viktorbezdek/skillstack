#!/bin/bash
# List Git worktrees.
#
# Usage:
#   ./list_worktrees.sh [--detailed]

set -e

DETAILED=false

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

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

REPO_ROOT=$(git rev-parse --show-toplevel)
REPO_NAME=$(basename "$REPO_ROOT")

echo ""
echo -e "${GREEN}Git Worktrees for ${CYAN}$REPO_NAME${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

worktrees=$(git worktree list --porcelain)
worktree_count=0

while IFS= read -r line; do
    if [[ "$line" == worktree\ * ]]; then
        path="${line#worktree }"
        branch=""
        commit=""

        while IFS= read -r subline; do
            if [[ "$subline" == HEAD\ * ]]; then
                commit="${subline#HEAD }"
            elif [[ "$subline" == branch\ * ]]; then
                branch="${subline#branch }"
                branch="${branch#refs/heads/}"
            elif [[ -z "$subline" ]]; then
                break
            fi
        done

        if [ "$path" = "$REPO_ROOT" ]; then
            echo -e "${GREEN}Main Worktree${NC}"
        else
            ((worktree_count++))
            echo -e "${CYAN}Worktree #$worktree_count${NC}"
        fi

        echo -e "  ${BLUE}Branch:${NC} $branch"
        echo -e "  ${BLUE}Path:${NC}   $path"

        if [ "$DETAILED" = true ]; then
            echo -e "  ${BLUE}Commit:${NC} ${commit:0:7}"
            if [ -d "$path" ]; then
                if git -C "$path" diff-index --quiet HEAD -- 2>/dev/null; then
                    echo -e "  ${GREEN}Status: Clean${NC}"
                else
                    echo -e "  ${YELLOW}Status: Dirty (uncommitted changes)${NC}"
                fi
            else
                echo -e "  ${RED}Status: Directory not found (stale)${NC}"
            fi
        fi

        echo ""
    fi
done <<< "$worktrees"

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
