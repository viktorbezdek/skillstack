# PR Comment Analysis - Quick Start Guide

**Problem Solved**: Automates extraction, filtering, and presentation of PR code review comments (including Qodo, CodeRabbit, and other bots) directly to Claude, with iterative loops until all issues are addressed.

## 🎯 What This Skill Does

Extracts ALL comments from GitHub PRs (inline reviews + general comments), filters out verbose summaries, and presents actionable feedback to Claude in a readable format. Includes iterative review loops and progress tracking with strikethrough for addressed items.

## 🚀 Quick Start (Recommended Workflow)

### One-Time Setup

1. **Set GitHub Token**
   ```bash
   # Option 1: Environment variable
   export GITHUB_TOKEN=ghp_xxxxxxxxxxxx

   # Option 2: .env file in your repo
   echo "GITHUB_TOKEN=ghp_xxxxxxxxxxxx" >> .env
   ```

2. **Verify Token Permissions**
   - Your token must have `repo` scope (for private repos) or `public_repo` (for public repos)
   - Create at: https://github.com/settings/tokens/new

### Basic Usage: One-Time Analysis

```bash
cd /path/to/your/repo
/path/to/pr-comment-analysis/scripts/analyze-pr.sh owner/repo PR_NUMBER
```

**Example:**
```bash
cd ~/projects/my-app
~/skills/pr-comment-analysis/scripts/analyze-pr.sh myorg/my-app 456
```

**What it does:**
1. ✅ Fetches ALL PR comments from GitHub API
2. ✅ Filters to actionable items (removes verbose summaries)
3. ✅ Explicitly checks for Qodo comment preservation
4. ✅ Generates Claude-readable markdown summary
5. ✅ Shows preview and next steps

**Output:**
- `pr-code-review-comments/pr456-analysis.md` - Markdown summary for Claude
- `pr-code-review-comments/pr456-code-review-comments-filtered.json` - Structured JSON

### Advanced Usage: Iterative Review Loop

```bash
cd /path/to/your/repo
/path/to/pr-comment-analysis/scripts/review-loop.sh owner/repo PR_NUMBER
```

**What it does:**
1. Fetches and filters PR comments
2. Shows Claude the unaddressed comments
3. Waits for you to fix issues and commit
4. Marks addressed comments
5. **Repeats until no actionable comments remain**

**Interactive mode** (asks before each iteration):
```bash
./scripts/review-loop.sh owner/repo 456
```

**Auto mode** (waits 30 seconds between iterations):
```bash
./scripts/review-loop.sh owner/repo 456 --auto
```

### Checking Progress

```bash
# See all comments with status markers
python scripts/show-with-status.py 456

# See only pending comments
python scripts/show-with-status.py 456 --unaddressed-only

# Save report to file
python scripts/show-with-status.py 456 --output review-status.md
```

**Output format:**
```markdown
# PR #456 Code Review Status

**Progress**: 60% complete (6/10 comments addressed)

## 📝 Pending Comments

### 📝 [coderabbitai[bot]] Review Comment
**Location**: src/api/auth.ts:45
**Priority**: 🔴 CRITICAL
**Preview**: SQL injection vulnerability in authentication...

---

<details>
<summary>✅ Addressed Comments (6)</summary>

### ✅ [coderabbitai[bot]] Review Comment
**Location**: ~~src/models/user.ts:89~~
**Preview**: ~~Missing null check for user.email...~~

</details>
```

## 🔧 Available Scripts

| Script | Purpose | When to Use |
|--------|---------|-------------|
| **`analyze-pr.sh`** | One-time analysis with Claude-readable output | Initial PR review or checking current state |
| **`review-loop.sh`** | Iterative loop until all comments addressed | Working through all PR feedback systematically |
| **`show-with-status.py`** | Progress report with strikethrough | Checking what's left to do |
| **`diagnose-qodo.py`** | Debug Qodo comment filtering | Troubleshooting missing bot comments |
| **`pr-comment-grabber.py`** | Fetch raw comments from GitHub | Manual workflow or custom integrations |
| **`pr-comment-filter.py`** | Filter to actionable comments | Manual workflow or custom filtering |

## 🐛 Troubleshooting

### "Claude never sees Qodo comments"

**Quick diagnostic:**
```bash
# 1. Fetch comments
python scripts/pr-comment-grabber.py owner/repo 456

# 2. Run diagnostic
python scripts/diagnose-qodo.py pr-code-review-comments/pr456-code-review-comments.json
```

**Common fixes:**
- **If Qodo comments have importance < 7**: Edit `scripts/pr-comment-filter.py` line 112 to lower threshold
- **If "PR Compliance Guide" triggers filtering**: Remove from `SUMMARY_MARKERS` in `pr-comment-filter.py`
- **If using auto mode**: Ensure `analyze-pr.sh` or `review-loop.sh` (not manual steps)

**See detailed troubleshooting**: [USAGE-GUIDE.md](USAGE-GUIDE.md)

### "Comments being discarded as summaries"

Edit `scripts/pr-comment-filter.py`:
```python
# Lines 27-39: Adjust SUMMARY_MARKERS
SUMMARY_MARKERS = [
    '<!-- This is an auto-generated comment: summarize',
    '## Walkthrough',
    # 'PR Compliance Guide',  # ← Comment out if Qodo uses this
]
```

### "Loop never completes"

- Increase `MAX_ITERATIONS` in `review-loop.sh` (default: 10)
- Check if bots are stuck in feedback loop
- Use `show-with-status.py` to see what's left

### "Missing inline review comments"

Lower priority threshold in `scripts/pr-comment-filter.py` line 112:
```python
# Was: if importance < 7: continue
# Try: if importance < 5: continue  # Keep medium+ priority
```

## 📚 Documentation

- **[SKILL.md](SKILL.md)** - Complete skill definition with advanced features
- **[USAGE-GUIDE.md](USAGE-GUIDE.md)** - Comprehensive troubleshooting and configuration guide
- **`scripts/`** - All automation scripts with inline documentation

## 🔑 Key Features

### ✅ Solves "Claude Never Sees Comments" Problem

**Before** (manual workflow):
1. Run `pr-comment-grabber.py`
2. Run `pr-comment-filter.py`
3. **Manual step**: Provide filtered JSON to Claude ← *Where comments got lost*

**After** (automated workflow):
1. Run `analyze-pr.sh` → *Automatically shows Claude the filtered comments*
2. Or run `review-loop.sh` → *Iterates until all comments addressed*

### ✅ Intelligent Content-Based Filtering

- Removes verbose bot summaries/walkthroughs
- Preserves actionable suggestions (even from bots)
- Extracts structured suggestions with priority levels
- Configurable markers and thresholds

### ✅ Iterative Review Loop

- Tracks addressed vs pending comments
- Waits for CI/bot responses
- Automatically detects new issues
- Stops when all comments resolved

### ✅ Progress Tracking

- Visual progress bars
- Strikethrough formatting for addressed items
- Collapsible sections for completed work
- JSON export for custom reporting

## 🎓 Example Workflows

### Scenario 1: Initial PR Review

```bash
# Fetch and analyze PR #123
cd ~/projects/my-app
~/skills/pr-comment-analysis/scripts/analyze-pr.sh myorg/my-app 123

# Claude reads the generated analysis:
# "Claude, please read: pr-code-review-comments/pr123-analysis.md"

# Fix issues, commit, done
```

### Scenario 2: Systematic Review Loop

```bash
# Start iterative loop for PR #123
cd ~/projects/my-app
~/skills/pr-comment-analysis/scripts/review-loop.sh myorg/my-app 123

# → Shows 15 actionable comments
# Fix issues, commit, press ENTER
# → Bot analyzes, shows 5 new comments
# Fix issues, commit, press ENTER
# → No comments remain
# "🎉 ALL COMMENTS ADDRESSED!"
```

### Scenario 3: Check Progress Mid-Review

```bash
# While working through PR #123 in another terminal:
python ~/skills/pr-comment-analysis/scripts/show-with-status.py 123

# See progress bar and pending items
# Focus on what's left to do
```

## ⚙️ Configuration

### Environment Variables

- **`GITHUB_TOKEN`** (required) - Personal access token with `repo` or `public_repo` scope
- **`MAX_ITERATIONS`** (optional) - Max review loop iterations (default: 10)

### Customizing Filters

Edit `scripts/pr-comment-filter.py` to adjust:
- **Priority threshold** (line 112) - Default: importance >= 7
- **Summary markers** (lines 27-39) - What counts as verbose summary
- **Actionable markers** (lines 27-39) - What counts as actionable content

### Bot Whitelisting

If you only want specific bots:
```bash
# Create whitelist
cat > ~/.pr-review-bots.txt << 'EOF'
coderabbitai[bot]
qodo-merge-pro[bot]
EOF

# Filter before processing
jq --slurpfile bots <(jq -R . ~/.pr-review-bots.txt | jq -s .) \
   '[.[] | select(.user as $u | $bots[0] | map(. == $u) | any)]' \
   pr-code-review-comments/pr123-code-review-comments.json \
   > pr-code-review-comments/pr123-bots-only.json

# Now analyze filtered file
python scripts/pr-comment-filter.py pr-code-review-comments/pr123-bots-only.json
```

## 📦 Requirements

- **Python 3.6+**
- **`requests` library**: `pip install requests`
- **`jq` (for shell scripts)**: `sudo apt install jq` or `brew install jq`
- **GitHub Personal Access Token** with `repo` or `public_repo` scope

## 🔗 Integration

### With Claude Code

```bash
# In your .claude/commands/ directory
cat > analyze-pr.sh << 'EOF'
#!/bin/bash
SKILL_DIR="/path/to/pr-comment-analysis"
$SKILL_DIR/scripts/analyze-pr.sh $@
EOF
chmod +x .claude/commands/analyze-pr.sh

# Now use: /analyze-pr owner/repo PR_NUMBER
```

### With CI/CD

```yaml
# .github/workflows/pr-analysis.yml
name: PR Comment Analysis
on: pull_request_review

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Fetch PR comments
        run: |
          python scripts/pr-comment-grabber.py ${{ github.repository }} ${{ github.event.pull_request.number }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - uses: actions/upload-artifact@v2
        with:
          name: pr-comments
          path: pr-code-review-comments/
```

## 📝 Output Files

All output goes to `pr-code-review-comments/` in your repository:

- **`prNN-code-review-comments.json`** - Raw fetched comments
- **`prNN-code-review-comments-filtered.json`** - Actionable comments only
- **`prNN-analysis.md`** - Claude-readable markdown summary
- **`prNN-review-state.json`** - Iterative loop state tracking
- **`prNN-unaddressed.json`** - Comments still pending

## 🎯 Best Practices

1. **Run `analyze-pr.sh` immediately after review** - Don't wait, context is fresh
2. **Use `review-loop.sh` for systematic cleanup** - Ensures nothing is missed
3. **Check `show-with-status.py` for progress** - Know what's left before asking for re-review
4. **Lower priority threshold if needed** - Some bots use different importance scales
5. **Commit with comment references** - `git commit -m "fix: address SQL injection (comment #123)"`

## 🆘 Getting Help

1. **Read diagnostics output** - Scripts provide detailed error messages
2. **Run `diagnose-qodo.py`** - Understand why comments disappear
3. **Check [USAGE-GUIDE.md](USAGE-GUIDE.md)** - Comprehensive troubleshooting
4. **Review [SKILL.md](SKILL.md)** - Full skill capabilities and advanced features

## 📄 License

Part of the Instructor Workflow project.

---

**Quick Reference Card:**

```bash
# Initial setup
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx

# One-time analysis
./scripts/analyze-pr.sh owner/repo 123

# Iterative loop
./scripts/review-loop.sh owner/repo 123

# Check progress
python scripts/show-with-status.py 123

# Debug Qodo comments
python scripts/diagnose-qodo.py pr-code-review-comments/pr123-code-review-comments.json
```
