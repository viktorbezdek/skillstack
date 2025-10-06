# PR Comment Analysis - Complete Usage Guide

## 🚨 Problem: Missing Qodo Comments

**Symptom**: Claude never sees Qodo (or other bot) comments, must paste manually.

**Diagnosis Steps**:

```bash
# 1. Fetch PR comments
python scripts/pr-comment-grabber.py owner/repo PR_NUMBER

# 2. Run diagnostic
python scripts/diagnose-qodo.py pr-code-review-comments/prPR_NUMBER-code-review-comments.json
```

**What to look for**:
- ❌ "NO QODO COMMENTS FOUND" → Qodo isn't commenting on this PR
- ⚠️ "X Qodo comments will be DISCARDED" → Being filtered as summaries
- ⚠️ "Only suggestions with importance >= 7 are kept" → Low-priority items filtered out

**Fixes**:

### Fix 1: Lower Priority Threshold
If Qodo suggestions have importance < 7, edit `scripts/pr-comment-filter.py`:

```python
# Line 112: Change from
if importance < 7:
    continue

# To
if importance < 5:  # Keep medium+ priority
    continue
```

### Fix 2: Adjust Summary Markers
If Qodo compliance guides are being discarded, edit `scripts/pr-comment-filter.py`:

```python
# Lines 27-32: Remove 'PR Compliance Guide' if needed
SUMMARY_MARKERS = [
    '<!-- This is an auto-generated comment: summarize',
    '## Walkthrough',
    '<!-- walkthrough_start -->',
    # 'PR Compliance Guide',  # ← Comment out if Qodo uses this
]
```

### Fix 3: Whitelist Specific Bots
If you only want CodeRabbit + Qodo (no other bots):

```bash
# Create bot whitelist
cat > ~/.pr-review-bots.txt << 'EOF'
coderabbitai[bot]
coderabbitai
qodo-merge
qodo-merge-pro[bot]
qodo[bot]
EOF

# Then filter before processing
jq --slurpfile bots <(jq -R . ~/.pr-review-bots.txt | jq -s .) \
   '[.[] | select(.user as $u | $bots[0] | map(. == $u) | any)]' \
   pr-code-review-comments/prPR_NUMBER-code-review-comments.json \
   > pr-code-review-comments/prPR_NUMBER-bots-only.json

# Now filter this file instead
python scripts/pr-comment-filter.py pr-code-review-comments/prPR_NUMBER-bots-only.json
```

---

## 🔁 Iterative Review Loop

**Problem**: Claude fixes issues → commits → new issues appear → manual re-run required.

**Solution**: Automated loop until no comments remain.

### Usage

```bash
# Interactive mode (asks before each iteration)
./scripts/review-loop.sh owner/repo PR_NUMBER

# Auto mode (waits 30 seconds between iterations)
./scripts/review-loop.sh owner/repo PR_NUMBER --auto
```

### What It Does

1. **Fetch** → Grabs all PR comments via GitHub API
2. **Filter** → Extracts actionable items (discards summaries)
3. **Show** → Displays unaddressed comments to Claude
4. **Wait** → Pauses for you to fix issues
5. **Mark** → Tracks which comments you've addressed
6. **Loop** → Repeats until no unaddressed comments remain

### State Tracking

The script maintains state in:
```
pr-code-review-comments/prPR_NUMBER-review-state.json
```

**Format**:
```json
{
  "iteration": 3,
  "addressed_comments": [123456789, 987654321, ...]
}
```

**Reset state** (start fresh):
```bash
rm pr-code-review-comments/pr*-review-state.json
```

---

## ✅ Comment Status Display

**Problem**: Can't see which comments have been addressed vs still pending.

**Solution**: Markdown report with strikethrough for addressed items.

### Usage

```bash
# Generate markdown report
python scripts/show-with-status.py PR_NUMBER

# Save to file
python scripts/show-with-status.py PR_NUMBER --output review-status.md

# Show only unaddressed (pending work)
python scripts/show-with-status.py PR_NUMBER --unaddressed-only

# JSON output (for scripts)
python scripts/show-with-status.py PR_NUMBER --format json
```

### Example Output

```markdown
# PR #123 Code Review Status

**Progress**: 60% complete (6/10 comments addressed)

## 📝 Pending Comments

### 📝 [coderabbitai[bot]] Review Comment
**Location**: src/api/auth.ts:45
**Priority**: 🔴 CRITICAL
**Preview**: SQL injection vulnerability in authentication validator...

### 📝 [qodo-merge[bot]] Review Comment
**Location**: src/utils/helpers.ts:12
**Priority**: 🟡 MEDIUM
**Preview**: Consider using const instead of let for immutable values...

---

<details>
<summary>✅ Addressed Comments (6)</summary>

### ✅ [coderabbitai[bot]] Review Comment
**Location**: ~~src/models/user.ts:89~~
**Preview**: ~~Missing null check for user.email property...~~

</details>
```

---

## 🎯 Complete Workflow Example

### Scenario: Working on PR #456

```bash
# 1. Start review loop
cd /path/to/your/repo
./skills/pr-comment-analysis/scripts/review-loop.sh myorg/myrepo 456

# → Fetches 15 comments
# → Filters to 8 actionable comments
# → Shows you the list

# 2. Fix issues in your code
# (Claude or you makes changes, commits, pushes)

# 3. Script waits 60 seconds for bots to respond

# 4. Loop continues - fetches new comments
# → Fetches 20 comments (5 new ones appeared!)
# → Filters to 10 actionable (2 new issues)
# → Marks previous 8 as addressed
# → Shows you the 2 new issues

# 5. Fix new issues, repeat

# 6. Eventually: "🎉 ALL COMMENTS ADDRESSED!"
```

### During the loop, in another terminal:

```bash
# Check progress
python skills/pr-comment-analysis/scripts/show-with-status.py 456

# See what's left to do
python skills/pr-comment-analysis/scripts/show-with-status.py 456 --unaddressed-only
```

---

## 🔧 Configuration

### Environment Variables

Required:
- `GITHUB_TOKEN` - Personal access token with `repo` scope

Optional:
- `MAX_ITERATIONS` - Max loop iterations (default: 10)

### Set GitHub Token

```bash
# Option 1: Environment variable
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx

# Option 2: .env file
echo "GITHUB_TOKEN=ghp_xxxxxxxxxxxx" >> .env
```

### Token Permissions

Your GitHub PAT must have:
- ✅ `repo` - Full repo access (for private repos)
- ✅ `public_repo` - Public repo access (for public repos)

**How to create**: https://github.com/settings/tokens/new
- Select scopes: `repo` or `public_repo`
- Generate token
- Copy and save to `.env`

---

## 🐛 Troubleshooting

### "No Qodo comments found"

**Check**: Does Qodo actually comment on this PR?
- Visit PR on GitHub
- Check "Conversation" tab for Qodo comments
- Check "Files changed" tab for inline Qodo reviews

**If yes, but script says no**: Run diagnostic:
```bash
python scripts/diagnose-qodo.py pr-code-review-comments/prPR_NUMBER-code-review-comments.json
```

### "Comments being discarded as summaries"

Qodo compliance guides might trigger `SUMMARY_MARKERS`. Edit filter.py:
```python
# Remove or comment out markers that catch Qodo
SUMMARY_MARKERS = [
    '<!-- This is an auto-generated comment: summarize',
    '## Walkthrough',
    # 'PR Compliance Guide',  # ← Disable if Qodo uses this
]
```

### "Loop never completes"

**Scenario**: Bots keep posting new comments after each commit.

**Solutions**:
1. Increase `MAX_ITERATIONS` in `review-loop.sh`
2. Manually review remaining issues outside loop
3. Check if bot is stuck in feedback loop (e.g., reformatting suggestions)

### "Missing inline review comments"

**Check**: Are they being filtered due to priority?

```bash
# Lower priority threshold
# Edit scripts/pr-comment-filter.py line 112:
if importance < 5:  # Was 7, now 5
    continue
```

---

## 📊 All Available Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `pr-comment-grabber.py` | Fetch all PR comments | `python pr-comment-grabber.py owner/repo PR_NUM` |
| `pr-comment-filter.py` | Filter to actionable items | `python pr-comment-filter.py comments.json` |
| `diagnose-qodo.py` | Debug Qodo filtering | `python diagnose-qodo.py comments.json` |
| `review-loop.sh` | Iterative review until complete | `./review-loop.sh owner/repo PR_NUM` |
| `show-with-status.py` | Display addressed vs pending | `python show-with-status.py PR_NUM` |

---

## 🎯 Quick Reference Card

```bash
# Initial setup
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx

# Diagnose missing Qodo comments
python scripts/diagnose-qodo.py pr-code-review-comments/pr123-code-review-comments.json

# Run iterative review loop
./scripts/review-loop.sh owner/repo 123

# Check progress
python scripts/show-with-status.py 123

# Show only what's left
python scripts/show-with-status.py 123 --unaddressed-only
```
