#!/bin/bash
# analyze-pr.sh - Automated PR comment analysis with Claude
#
# Usage:
#   ./analyze-pr.sh owner/repo PR_NUMBER
#
# What it does:
#   1. Fetches PR comments from GitHub API
#   2. Filters to actionable items (removes verbose summaries)
#   3. Shows filtered comments to Claude for analysis
#   4. Generates prioritized action plan

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

if [ $# -lt 2 ]; then
    echo "Usage: $0 owner/repo PR_NUMBER"
    exit 1
fi

REPO=$1
PR_NUMBER=$2

# Check GitHub token
if [ -z "$GITHUB_TOKEN" ]; then
    if [ -f ".env" ]; then
        export $(grep -v '^#' .env | grep GITHUB_TOKEN | xargs)
    fi
    if [ -z "$GITHUB_TOKEN" ]; then
        echo -e "${RED}Error: GITHUB_TOKEN required${NC}"
        exit 1
    fi
fi

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     PR Comment Analysis for Claude    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""
echo -e "Repository: ${GREEN}$REPO${NC}"
echo -e "PR Number:  ${GREEN}#$PR_NUMBER${NC}"
echo ""

# Step 1: Fetch comments
echo -e "${BLUE}→${NC} Fetching PR comments from GitHub..."
python3 "$SCRIPT_DIR/pr-comment-grabber.py" "$REPO" "$PR_NUMBER"

COMMENT_FILE="pr-code-review-comments/pr${PR_NUMBER}-code-review-comments.json"
if [ ! -f "$COMMENT_FILE" ]; then
    echo -e "${RED}Error: Comment file not found${NC}"
    exit 1
fi

TOTAL_COMMENTS=$(jq 'length' "$COMMENT_FILE")
echo -e "${GREEN}✓${NC} Fetched $TOTAL_COMMENTS comments"

# Step 2: Filter comments
echo -e "${BLUE}→${NC} Filtering actionable comments..."
python3 "$SCRIPT_DIR/pr-comment-filter.py" "$COMMENT_FILE"

FILTERED_FILE="pr-code-review-comments/pr${PR_NUMBER}-code-review-comments-filtered.json"
FILTERED_COUNT=$(jq 'length' "$FILTERED_FILE")
echo -e "${GREEN}✓${NC} Filtered to $FILTERED_COUNT actionable comments"

# Step 3: Check for Qodo comments specifically
QODO_COUNT=$(jq '[.[] | select(.user | contains("qodo"))] | length' "$FILTERED_FILE")
if [ "$QODO_COUNT" -gt 0 ]; then
    echo -e "${GREEN}✓${NC} Qodo comments preserved: $QODO_COUNT"
else
    echo -e "${YELLOW}⚠${NC}  No Qodo comments found in filtered output"
    echo "  Check if Qodo commented on this PR"
fi

# Step 4: Generate Claude-readable summary
echo -e "${BLUE}→${NC} Generating Claude analysis..."

OUTPUT_FILE="pr-code-review-comments/pr${PR_NUMBER}-analysis.md"

cat > "$OUTPUT_FILE" << EOF
# PR #$PR_NUMBER Code Review Comments

**Repository**: $REPO
**Total Comments**: $TOTAL_COMMENTS
**Actionable Comments**: $FILTERED_COUNT
**Qodo Comments**: $QODO_COUNT

---

## 📝 All Actionable Comments

Below are ALL actionable comments after filtering out summaries/walkthroughs.
This includes CodeRabbit, Qodo, and all other bot reviews.

EOF

# Append formatted comments
jq -r '.[] |
"### [\(.user)] \(.comment_type | ascii_upcase) Comment

**File**: \(.path // "General comment")
**Line**: \(.line // "N/A")
**Created**: \(.created_at)
**Link**: \(.html_url)

\(.body)

---

"' "$FILTERED_FILE" >> "$OUTPUT_FILE"

echo -e "${GREEN}✓${NC} Analysis saved to: $OUTPUT_FILE"

# Step 5: Show preview
echo ""
echo -e "${YELLOW}═══ Preview (first 20 lines) ═══${NC}"
head -20 "$OUTPUT_FILE"
echo ""
echo -e "${YELLOW}... (see $OUTPUT_FILE for complete analysis)${NC}"
echo ""

# Step 6: Instructions for Claude
echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║      Next Steps for Claude            ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""
echo "✅ Filtered comments ready for Claude analysis"
echo ""
echo "OPTION 1: Read the markdown summary"
echo "  Claude, please read: $OUTPUT_FILE"
echo ""
echo "OPTION 2: Read the raw JSON (more structured)"
echo "  Claude, please read: $FILTERED_FILE"
echo ""
echo "OPTION 3: Copy to clipboard (macOS/Linux)"
if command -v pbcopy &> /dev/null; then
    cat "$OUTPUT_FILE" | pbcopy
    echo "  ✓ Copied to clipboard! Just paste into Claude"
elif command -v xclip &> /dev/null; then
    cat "$OUTPUT_FILE" | xclip -selection clipboard
    echo "  ✓ Copied to clipboard! Just paste into Claude"
else
    echo "  Install pbcopy (macOS) or xclip (Linux) to enable auto-copy"
fi
