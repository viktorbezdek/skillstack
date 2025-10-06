# Agent Prompt: PR Comment Analysis

**Copy this entire prompt and send to an LLM agent to analyze PR review comments.**

---

## Task Overview

You are an expert code reviewer and workflow optimizer. I have a GitHub Pull Request with review comments that need to be extracted, consolidated, and prioritized.

**Target PR:** https://github.com/auldsyababua/mac-workhorse-integration/pull/1

---

## STEP 1: Extract PR Comments

Run the PR comment extraction script to fetch **ALL** comments (review + issue) as JSON.

**What gets extracted:**
- **Review comments**: Inline code comments on specific files/lines
- **Issue comments**: General PR conversation (e.g., Qodo summaries, bot comments)

**Location:** `/Users/colinaulds/Desktop/projects/devlog/llm-tools/pr-comment-grabber.py`

**Prerequisites:**
1. Ensure `requests` library is installed:
   ```bash
   pip install requests
   ```

2. Set GitHub token (choose one method):
   ```bash
   # Option A: Export from environment
   export GITHUB_TOKEN=ghp_your_token_here

   # Option B: Retrieve from 1Password (if configured)
   export GITHUB_TOKEN=$(op item get "GitHub" --fields label="Personal Access Token")
   ```

**Run the script:**
```bash
cd /Users/colinaulds/Desktop/projects/devlog/llm-tools
python pr-comment-grabber.py auldsyababua/mac-workhorse-integration 1 > pr-comments.json
```

**Verify extraction:**
```bash
# Check comment count
cat pr-comments.json | python -m json.tool | grep '"id"' | wc -l

# View first comment
cat pr-comments.json | python -m json.tool | head -30
```

---

## STEP 2: Analyze and Prioritize Comments

Read the JSON output from `pr-comments.json` and perform systematic analysis.

**Input Data:**
```bash
cat pr-comments.json
```

**Analysis Tasks:**

### A. Consolidation and De-duplication

1. **Separate comment types:** Review comments have `comment_type: "review"`, issue comments have `comment_type: "issue"`
2. **Group review comments by file:** Group all review comments by their `path` field
3. **Keep issue comments separate:** Issue comments (Qodo summaries, bot analyses) go in their own section
4. **Identify duplicates:** Find semantically similar review comments from different reviewers
5. **Flag consensus:** Mark soft duplicates as **"High Consensus Issue"**
6. **Consolidate:** Create one entry per duplicate set, listing all reviewers

### B. Prioritization

Organize consolidated issues into three priority levels:

**Level 0 - Bot Summaries (Review First, Don't Execute):**
- Issue comments from Qodo, CodeRabbit, Copilot (general PR analysis)
- These provide high-level context but aren't actionable tasks themselves

**Level 1 - Critical (Tackle First):**
- Bugs, security issues, performance regressions
- Comments flagged as "High Consensus Issue" (multiple reviewers mentioned same thing)

**Level 2 - Design/Architecture (Tackle Second):**
- Major refactoring suggestions
- Structural changes
- Non-trivial logic improvements

**Level 3 - Style/Clarity (Tackle Last):**
- Nitpicks, variable renaming
- Minor documentation updates
- Formatting changes

---

## STEP 3: Generate Action Plan

Create a Markdown document with this exact structure:

```markdown
# Consolidated Pull Request Review Action Plan

**PR:** https://github.com/auldsyababua/mac-workhorse-integration/pull/1
**Total Comments:** [count]
**Review Comments (inline):** [count]
**Issue Comments (general):** [count]
**Analysis Date:** [YYYY-MM-DD]

---

## 0. Bot Analysis Summaries (Context Only)

### Qodo / CodeRabbit / Copilot Summaries

**[Bot Name]:**
[Paste full summary text from issue comment]

**Key Insights:**
- [Extract actionable insights if any]
- [Note: These are high-level - specific issues are in sections below]

---

## 1. High Consensus & Critical Issues (Tackle First)

### [File Path]: [Consolidated Issue Summary]

**Consensus:** [List of reviewers who raised this point]
**Tackle Priority:** High / Critical
**Original Comments (Examples):**
* [Reviewer A's body text]
* [Reviewer B's body text]

**Recommended Fix:** [Concise, actionable instruction]

**References:**
- Comment ID: [id]
- HTML URL: [html_url]
- Line: [line]

---

## 2. Design and Architectural Improvements (Tackle Second)

### [File Path]: [Issue Summary]

**Reviewer:** [User who made the comment]
**Tackle Priority:** Medium
**Original Comment:** [Full body text]

**Recommended Fix:** [Concise, actionable instruction]

**References:**
- Comment ID: [id]
- HTML URL: [html_url]
- Line: [line]

---

## 3. Style and Clarity Nitpicks (Tackle Last)

### [File Path]: [Issue Summary]

**Reviewer:** [User who made the comment]
**Tackle Priority:** Low
**Original Comment:** [Full body text]

**Recommended Fix:** [Concise, actionable instruction]

**References:**
- Comment ID: [id]
- HTML URL: [html_url]
- Line: [line]

---

## Summary Statistics

**By Priority:**
- Critical/Consensus: [count] issues
- Design/Architecture: [count] issues
- Style/Clarity: [count] issues

**By File:**
- [path]: [count] comments
- [path]: [count] comments
...

**By Reviewer:**
- [username]: [count] comments
- [username]: [count] comments
...

---

## Recommended Execution Order

1. Address all Critical/Consensus issues (Section 1)
2. Create follow-up issue for Design improvements (Section 2) if time-constrained
3. Batch-apply Style nitpicks (Section 3) or defer to later PR
```

---

## STEP 4: Save Output

Save the generated action plan to a file:

```bash
# Suggested filename format:
/Users/colinaulds/Desktop/projects/devlog/llm-tools/pr-1-action-plan-YYYY-MM-DD.md
```

---

## Expected Deliverables

1. ✅ `pr-comments.json` - Raw JSON output from script
2. ✅ `pr-1-action-plan-YYYY-MM-DD.md` - Consolidated, prioritized action plan
3. ✅ Summary of total comments, unique files, and priority breakdown

---

## Error Handling

**If script fails with "Authentication failed":**
```bash
# Verify token is set
echo $GITHUB_TOKEN

# Re-export token
export GITHUB_TOKEN=ghp_xxxxx
```

**If script fails with "PR not found":**
- Verify repository: `auldsyababua/mac-workhorse-integration`
- Verify PR number: `1`
- Check you have access to the repository

**If requests library missing:**
```bash
pip install requests
```

---

## Success Criteria

- [x] Script runs successfully and fetches ALL comments (handles pagination)
- [x] JSON output contains complete metadata (id, user, body, path, line, html_url, etc.)
- [x] Action plan consolidates duplicate/similar comments
- [x] Action plan prioritizes issues rationally (Critical → Design → Style)
- [x] Every issue has a "Recommended Fix" with actionable steps
- [x] Action plan includes comment IDs and URLs for easy reference

---

**READY TO EXECUTE:** Copy this prompt and run the script, then provide the analysis.
