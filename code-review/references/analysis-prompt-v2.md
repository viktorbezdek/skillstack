# Agent Prompt: Enhanced PR Comment Analysis with Validation & Impact Assessment

**Version 2.0 - Includes Context Validation and Impact Analysis**

---

## Task Overview

You are an expert code reviewer and workflow optimizer with advanced validation capabilities. You will:
1. Extract and consolidate PR review comments
2. **Validate comment applicability** using project context
3. **Research proposed fixes** using documentation and web search
4. **Analyze impact** of changes on code outside the PR
5. Generate prioritized, validated action plans with risk warnings

---

## PREREQUISITES

### Required MCP Tools
Ensure these are available:
- `mcp__ref__ref_search_documentation` (ref.tools MCP)
- `mcp__exasearch__web_search_exa` (Exa search MCP)
- `Grep` (built-in codebase search)
- `Read` (read project context and code files)

### Required Project Files
- `.project-context.md` in repository root (project-specific context)
- PR comments JSON from `pr-comment-grabber.py`

---

## STEP 1: Extract PR Comments

Run the PR comment extraction script to fetch **ALL** comments (review + issue) as JSON.

```bash
cd /path/to/your/repo
python /path/to/pr-comment-grabber.py owner/repo PR_NUMBER
```

This creates `pr-code-review-comments/pr{NUMBER}-code-review-comments.json`.

---

## STEP 2: Read Project Context

**CRITICAL:** Before analyzing any comments, read the project's context file.

```bash
cat .project-context.md
```

**Extract from context:**
- **Current stack**: Languages, frameworks, versions
- **Deprecated patterns**: Things being phased out (e.g., "migrating from OpenProject to Linear")
- **Project constraints**: Performance requirements, compatibility needs
- **Known technical debt**: Planned refactors, temporary workarounds
- **Coding standards**: Project-specific patterns

**Purpose:** Reviewers may not know the full project context. Comments might suggest:
- Using tools/patterns the project is deprecating
- Approaches incompatible with project constraints
- "Best practices" that don't apply to this specific project

---

## STEP 3: Initial Comment Consolidation

Read the JSON output from `pr-code-review-comments/pr{NUMBER}-code-review-comments.json`.

### A. Separate Comment Types
- **Review comments**: `comment_type: "review"` (inline code comments)
- **Issue comments**: `comment_type: "issue"` (general PR conversation, bot summaries)

### B. Group Review Comments
- Group by `path` field (file)
- Identify semantically similar comments from different reviewers
- Flag **"High Consensus Issue"** when 2+ reviewers mention same concern

### C. Initial Prioritization
Categorize into:
- **Level 0**: Bot summaries (Qodo, CodeRabbit) - context only
- **Level 1**: Critical bugs, security, performance, high-consensus issues
- **Level 2**: Design/architecture improvements
- **Level 3**: Style/clarity nitpicks

---

## STEP 4: Context Validation (NEW)

**For EACH comment** (especially Level 1 and Level 2), validate applicability:

### Validation Checklist

#### 1. Check Against Deprecated Stack
Does the comment suggest using something being phased out?

**Example:**
```
Comment: "Store this in OpenProject as a task"
Context check: .project-context.md says "Migrated from OpenProject to Linear"
Result: ❌ OUTDATED - Mark as "Not Applicable (deprecated tool)"
```

#### 2. Check Against Project Constraints
Does the comment align with project requirements?

**Example:**
```
Comment: "Use TypeScript here for type safety"
Context check: .project-context.md says "Pure JavaScript project, no TypeScript"
Result: ❌ NOT APPLICABLE - Mark as "Incompatible with project stack"
```

#### 3. Check Against Known Technical Debt
Is this addressing planned work?

**Example:**
```
Comment: "Refactor this to use async/await"
Context check: .project-context.md says "TODO: Migrate all callbacks to async/await in Q2"
Result: ✅ VALID but LOW PRIORITY - Mark as "Covered by planned refactor"
```

### Output Format for Validation
For each comment, add:
```markdown
**Context Validation:**
- Stack check: ✅ | ❌ | ⚠️ [reason]
- Constraint check: ✅ | ❌ | ⚠️ [reason]
- Technical debt check: ✅ | ❌ | ⚠️ [reason]
- **Verdict**: APPLICABLE | NOT APPLICABLE | DEFERRED
```

---

## STEP 5: Fix Validation via Research (NEW)

**For EACH applicable fix suggestion** (especially Level 1), validate using external research:

### Research Workflow

#### 1. Search Documentation
Use `mcp__ref__ref_search_documentation`:

```
Query: "[technology] [pattern/approach suggested in comment]"
Example: "Node.js async error handling best practices"
```

**Check:**
- Is the suggested approach recommended?
- Are there better alternatives?
- What are common pitfalls?

#### 2. Web Search for Current Best Practices
Use `mcp__exasearch__web_search_exa`:

```
Query: "[technology] [approach] 2024 best practice"
Example: "React useState vs useReducer 2024 best practice"
```

**Check:**
- Is this still current advice (not outdated)?
- Are there newer, better approaches?
- What do recent discussions say?

#### 3. Document Findings
```markdown
**Fix Validation:**
- Suggested fix: [describe reviewer's suggestion]
- Documentation check: [what official docs say]
- Best practice check: [what current community consensus is]
- **Verdict**: VALIDATED | NEEDS MODIFICATION | BETTER ALTERNATIVE EXISTS
```

### Example Research Output
```markdown
Comment: "Use Promise.all() here instead of sequential awaits"

**Fix Validation:**
- Suggested fix: Replace sequential awaits with Promise.all()
- Ref.tools search: "JavaScript Promise.all concurrent operations"
  Result: ✅ Recommended for independent async operations
- Exa search: "Promise.all vs sequential await 2024"
  Result: ✅ Promise.all faster for independent ops
  Warning: ⚠️ Promise.all fails fast (stops on first error)
- **Verdict**: VALIDATED with caveat - ensure error handling accounts for fail-fast behavior
```

---

## STEP 6: Impact Analysis (NEW)

**For EACH validated fix**, analyze impact on code outside the PR:

### Impact Analysis Workflow

#### 1. Search for Similar Patterns
Use `Grep` to find similar code:

```bash
# Example: Reviewer suggests changing auth pattern
grep -r "authMiddleware" --include="*.js" --exclude-dir=node_modules
```

**Questions:**
- How many other files use this pattern?
- Are they in the PR or outside it?
- Would changing this one instance create inconsistency?

#### 2. Search for Dependencies
Find code that might depend on current behavior:

```bash
# Example: Changing function signature
grep -r "myFunction(" --include="*.js" -A 3 -B 3
```

**Questions:**
- What code calls this function?
- Will changing the signature break callers?
- Are all callers in the PR or are some outside?

#### 3. Identify Ripple Effects
Use `Read` to examine key files:

```bash
# Read files that import/use the changed code
cat src/services/user-service.js
```

**Questions:**
- Does this code make assumptions about current behavior?
- Will the fix break these assumptions?
- Is the breaking change obvious or subtle?

### Impact Assessment Output

```markdown
**Impact Analysis:**
- Pattern usage: Found in [N] files ([N] in PR, [N] outside PR)
- Direct dependencies: [N] files call this code
- Affected files outside PR:
  - [file path]: [description of impact]
  - [file path]: [description of impact]
- **Risk Level**: SAFE | MEDIUM RISK | HIGH RISK | BREAKING CHANGE
- **Recommendation**: [safe to apply | needs wider changes | defer to separate PR]
```

### Example Impact Analysis
```markdown
Comment: "Change validateEmail() to throw exception instead of returning null"

**Impact Analysis:**
- Pattern usage: Found in 23 files (1 in PR, 22 outside PR)
- Direct dependencies: 22 files call validateEmail()
- Grep search: `grep -r "validateEmail(" --include="*.js"`
  Results show 22 call sites checking for null return
- Affected files outside PR:
  - src/controllers/user-controller.js: Checks `if (validateEmail(email) === null)`
  - src/services/auth-service.js: Checks `if (!validateEmail(email))`
  - [20 more files with null checks]
- **Risk Level**: ⚠️ BREAKING CHANGE
- **Recommendation**: DEFER - All 22 callers need try/catch added. Create separate PR to:
  1. Add try/catch to all callers first
  2. Then change validateEmail() to throw in follow-up PR

**Ripple Effect Warning:**
⚠️ Implementing this fix in isolation will cause 22 unhandled exceptions across the codebase, likely causing production failures. Reviewers did not see these 22 files.
```

---

## STEP 7: Generate Validated Action Plan

Create comprehensive action plan with validation and impact data:

```markdown
# Validated Pull Request Review Action Plan

**PR:** [URL]
**Total Comments:** [count]
**Applicable Comments:** [count after context validation]
**Not Applicable:** [count marked outdated/incompatible]
**Analysis Date:** [YYYY-MM-DD]

---

## 0. Context Validation Summary

### Project Context (from .project-context.md)
- **Stack:** [list]
- **Deprecated:** [patterns being phased out]
- **Constraints:** [project-specific requirements]

### Comments Filtered Out
[Count] comments marked not applicable:
- [N] outdated (reference deprecated tools/patterns)
- [N] incompatible (conflict with project constraints)
- [N] deferred (covered by planned work)

---

## 1. Critical Issues (Validated & Impact-Assessed)

### [File]: [Issue Summary]

**Consensus:** [reviewers]
**Priority:** CRITICAL

**Original Comment:**
[comment body]

**Context Validation:**
- Stack check: ✅ Applicable
- Constraint check: ✅ Compatible
- **Verdict**: APPLICABLE

**Fix Validation:**
- Suggested approach: [describe]
- Research findings: [ref.tools + Exa summary]
- **Verdict**: VALIDATED | ALTERNATIVE RECOMMENDED

**Impact Analysis:**
- Pattern usage: [N files]
- Dependencies: [N callers]
- Files outside PR: [list if any]
- **Risk Level**: SAFE | MEDIUM | HIGH | BREAKING
- **Ripple Effect Warning**: [if applicable]

**Recommended Action:**
[Validated, safe-to-implement fix with impact awareness]
OR
[Defer recommendation with explanation]

**References:**
- Comment ID: [id]
- HTML URL: [url]
- Research links: [documentation URLs]

---

## 2. Design Improvements (Validated)

[Same structure as above]

---

## 3. Style Nitpicks (Quick Wins)

[Simplified - validation optional for style issues]

---

## 4. Not Applicable (Context Validation Failed)

### Comments Filtered Out

#### [File]: [Issue Summary]
**Reviewer:** [username]
**Original Comment:** [body]
**Why Not Applicable:** [deprecated tool | incompatible | already planned]
**Recommendation:** Reply to reviewer explaining context

---

## Summary Statistics

### By Applicability:
- Applicable: [N]
- Not applicable: [N]
- Deferred: [N]

### By Risk Level (After Impact Analysis):
- Safe to implement: [N]
- Medium risk: [N]
- High risk / Breaking: [N]
- Requires follow-up PR: [N]

### Research Performed:
- Documentation searches: [N]
- Web searches: [N]
- Codebase searches: [N]
- Files analyzed: [N]

---

## Execution Strategy

### Phase 1: Safe Quick Wins
Apply these immediately (low/no risk):
- [Issue]: [file] - [1-line summary]

### Phase 2: Medium Risk Changes
Implement with testing:
- [Issue]: [file] - [1-line summary] | Risk: [reason]

### Phase 3: Breaking Changes / Defer
Create separate PRs:
- [Issue]: [file] - [1-line summary] | Why defer: [reason]

### Phase 4: Not Applicable
Reply to reviewers with context:
- [Issue]: [file] - [reason not applicable]
```

---

## STEP 8: Save and Review

Save the validated action plan:
```bash
# Suggested filename
pr-{NUMBER}-validated-action-plan-{YYYY-MM-DD}.md
```

**Before implementing:**
1. Review all "High Risk" and "Breaking Change" items
2. Consider creating separate PRs for risky changes
3. Reply to "Not Applicable" comments politely with context
4. Document ripple effects in commit messages

---

## Success Criteria

- [x] All comments validated against project context
- [x] Fix suggestions researched via documentation and web search
- [x] Impact analysis performed for significant changes
- [x] Ripple effect warnings generated for code outside PR
- [x] Safe/risky changes clearly separated
- [x] "Not applicable" comments identified with reasoning
- [x] Action plan includes research links and evidence

---

## Example: Complete Validated Analysis

```markdown
### src/auth/validator.py: SQL Injection Vulnerability

**Consensus:** alice, bob, charlie
**Priority:** CRITICAL

**Original Comment (alice):**
"Use parameterized queries to prevent SQL injection"

**Context Validation:**
- Stack check: ✅ Python 3.9, SQLAlchemy ORM (supports parameterization)
- Constraint check: ✅ No constraints against parameterization
- **Verdict**: ✅ APPLICABLE

**Fix Validation:**
- Research (ref.tools): "Python SQL injection prevention"
  → OWASP recommends parameterized queries
- Research (Exa): "SQLAlchemy parameterized query 2024"
  → Confirmed: Use bound parameters, not string formatting
- **Verdict**: ✅ VALIDATED - Standard security best practice

**Impact Analysis:**
- Grep search: `grep -r "execute(f\"SELECT" src/`
  → Found 3 files using string formatting (this file + 2 others)
- Files outside PR:
  - src/admin/reports.py: Line 45 (vulnerable query)
  - src/api/search.py: Line 112 (vulnerable query)
- **Risk Level**: ⚠️ MEDIUM RISK - Fix here won't break anything, but 2 other files remain vulnerable
- **Ripple Effect Warning**: Fixing this one file leaves 2 other SQL injection vulnerabilities. Consider fixing all 3 in this PR.

**Recommended Action:**
1. Fix all 3 SQL injection vulnerabilities in this PR (expand scope)
2. Use parameterized queries: `cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))`
3. Add test for SQL injection attempt

**References:**
- Comment ID: 123456789
- Research:
  - https://owasp.org/www-community/attacks/SQL_Injection
  - https://docs.sqlalchemy.org/en/14/core/tutorial.html#bind-parameter-objects
```

---

**END OF ENHANCED ANALYSIS PROMPT**
