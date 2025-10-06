#!/bin/bash
# review-loop.sh - Iterative PR review loop until no comments remain
#
# Usage:
#   ./review-loop.sh owner/repo PR_NUMBER
#
# What it does:
#   1. Fetch PR comments
#   2. Filter to actionable items
#   3. Show Claude the comments
#   4. Wait for Claude to fix issues
#   5. Check if new comments appeared
#   6. Loop until no actionable comments remain

set -e  # Exit on error

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
MAX_ITERATIONS=10
COMMENT_DIR="pr-code-review-comments"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Usage
if [ $# -lt 2 ]; then
    echo "Usage: $0 owner/repo PR_NUMBER [--auto]"
    echo ""
    echo "Options:"
    echo "  --auto    Auto-commit fixes without asking"
    exit 1
fi

REPO=$1
PR_NUMBER=$2
AUTO_MODE=${3:-""}

# Validate repo format
if [[ ! "$REPO" =~ ^[^/]+/[^/]+$ ]]; then
    echo -e "${RED}Error: Repository must be in format owner/repo${NC}"
    exit 1
fi

# Check for GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${YELLOW}Warning: GITHUB_TOKEN not set. Reading from .env...${NC}"
    if [ -f ".env" ]; then
        export $(grep -v '^#' .env | grep GITHUB_TOKEN | xargs)
    fi
    if [ -z "$GITHUB_TOKEN" ]; then
        echo -e "${RED}Error: GITHUB_TOKEN required${NC}"
        exit 1
    fi
fi

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   PR Review Loop - Until Complete     ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""
echo -e "Repository: ${GREEN}$REPO${NC}"
echo -e "PR Number:  ${GREEN}#$PR_NUMBER${NC}"
echo ""

# State tracking file
STATE_FILE="$COMMENT_DIR/pr${PR_NUMBER}-review-state.json"

# Initialize state if doesn't exist
if [ ! -f "$STATE_FILE" ]; then
    echo '{"iteration": 0, "addressed_comments": []}' > "$STATE_FILE"
fi

# Function: Fetch and filter comments
fetch_comments() {
    echo -e "${BLUE}→${NC} Fetching PR comments..."
    python "$SCRIPT_DIR/pr-comment-grabber.py" "$REPO" "$PR_NUMBER"

    COMMENT_FILE="$COMMENT_DIR/pr${PR_NUMBER}-code-review-comments.json"

    if [ ! -f "$COMMENT_FILE" ]; then
        echo -e "${RED}Error: Comment file not found${NC}"
        exit 1
    fi

    # Count total comments
    TOTAL_COMMENTS=$(jq 'length' "$COMMENT_FILE")
    echo -e "${GREEN}✓${NC} Fetched $TOTAL_COMMENTS comments"

    # Filter comments
    echo -e "${BLUE}→${NC} Filtering actionable comments..."
    python "$SCRIPT_DIR/pr-comment-filter.py" "$COMMENT_FILE"

    FILTERED_FILE="$COMMENT_DIR/pr${PR_NUMBER}-code-review-comments-filtered.json"
    FILTERED_COUNT=$(jq 'length' "$FILTERED_FILE")
    echo -e "${GREEN}✓${NC} Filtered to $FILTERED_COUNT actionable comments"

    echo "$FILTERED_COUNT"
}

# Function: Mark comments as addressed
mark_addressed() {
    local comment_ids=$1

    # Update state file
    jq --argjson ids "$comment_ids" \
       '.addressed_comments += $ids | .addressed_comments |= unique' \
       "$STATE_FILE" > "${STATE_FILE}.tmp"
    mv "${STATE_FILE}.tmp" "$STATE_FILE"
}

# Function: Get unaddressed comments
get_unaddressed() {
    local filtered_file="$COMMENT_DIR/pr${PR_NUMBER}-code-review-comments-filtered.json"
    local state_file="$STATE_FILE"

    # Filter out already addressed comments
    jq --slurpfile state "$state_file" \
       '[.[] | select([.id] | inside($state[0].addressed_comments) | not)]' \
       "$filtered_file" > "$COMMENT_DIR/pr${PR_NUMBER}-unaddressed.json"

    jq 'length' "$COMMENT_DIR/pr${PR_NUMBER}-unaddressed.json"
}

# Main loop
iteration=0
while [ $iteration -lt $MAX_ITERATIONS ]; do
    iteration=$((iteration + 1))

    echo ""
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}  Iteration $iteration of $MAX_ITERATIONS${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    # Fetch comments
    actionable_count=$(fetch_comments)

    # Get unaddressed comments
    unaddressed_count=$(get_unaddressed)

    echo -e "${BLUE}Unaddressed comments:${NC} $unaddressed_count"

    if [ "$unaddressed_count" -eq 0 ]; then
        echo ""
        echo -e "${GREEN}╔════════════════════════════════════════╗${NC}"
        echo -e "${GREEN}║   🎉 ALL COMMENTS ADDRESSED!          ║${NC}"
        echo -e "${GREEN}╚════════════════════════════════════════╝${NC}"
        echo ""
        exit 0
    fi

    # Show unaddressed comments
    echo ""
    echo -e "${BLUE}═══ Unaddressed Comments ═══${NC}"
    jq -r '.[] | "[\(.user)] \(.comment_type) - \(.path // "general"):\(.line // "")\n  \(.body[0:100])...\n"' \
       "$COMMENT_DIR/pr${PR_NUMBER}-unaddressed.json"

    # Prompt user to fix issues
    echo ""
    echo -e "${YELLOW}Next steps:${NC}"
    echo "1. Review comments above"
    echo "2. Fix the issues in your code"
    echo "3. Commit and push your fixes"
    echo ""

    if [ "$AUTO_MODE" != "--auto" ]; then
        read -p "Press ENTER when fixes are committed and pushed (or Ctrl+C to abort): "
    else
        echo -e "${BLUE}Auto-mode: Waiting 30 seconds for fixes...${NC}"
        sleep 30
    fi

    # Mark current comments as addressed (user claims they fixed them)
    comment_ids=$(jq '[.[].id]' "$COMMENT_DIR/pr${PR_NUMBER}-unaddressed.json")
    mark_addressed "$comment_ids"

    echo -e "${GREEN}✓${NC} Marked $unaddressed_count comments as addressed"

    # Wait for CI/bots to respond
    echo -e "${BLUE}→${NC} Waiting 60 seconds for bots to analyze new commit..."
    sleep 60
done

echo ""
echo -e "${RED}╔════════════════════════════════════════╗${NC}"
echo -e "${RED}║   Max iterations reached!              ║${NC}"
echo -e "${RED}╚════════════════════════════════════════╝${NC}"
echo ""
echo "Still have unaddressed comments. Consider:"
echo "  - Increasing MAX_ITERATIONS"
echo "  - Manually reviewing remaining issues"
echo "  - Checking if bots are still posting"
