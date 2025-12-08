# Validation Workflow Quick Reference

## At-a-Glance Process

```
PR Comments → Context Check → Fix Validation → Impact Analysis → Validated Action Plan
```

---

## Step-by-Step Checklist

### □ 1. Extract Comments
```bash
python pr-comment-grabber.py owner/repo PR_NUM
```

### □ 2. Read Project Context
```bash
cat .project-context.md
```
**Extract:** Stack, deprecated patterns, constraints, tech debt

### □ 3. Initial Consolidation
- Group by file
- Identify consensus issues
- Initial priority (L1: Critical, L2: Design, L3: Style)

### □ 4. Context Validation (Per Comment)
```markdown
**Comment:** [reviewer's suggestion]

**Context Check:**
- ❓ Uses deprecated stack? → Check .project-context.md
- ❓ Violates constraints? → Check project requirements
- ❓ Conflicts with tech debt plan? → Check known issues

**Verdict:** ✅ APPLICABLE | ❌ NOT APPLICABLE | ⚠️ DEFERRED
```

### □ 5. Fix Validation (Per Applicable Fix)
```bash
# Search documentation
mcp__ref__ref_search_documentation "technology approach"

# Search web for best practices
mcp__exasearch__web_search_exa "technology approach 2024"
```

**Document:**
- What docs say
- What current best practice is
- Any gotchas/warnings

**Verdict:** ✅ VALIDATED | ⚠️ NEEDS MODIFICATION | 🔄 BETTER ALTERNATIVE

### □ 6. Impact Analysis (Per Validated Fix)
```bash
# Find similar patterns
grep -r "pattern" --include="*.ext"

# Find dependencies
grep -r "functionName(" --include="*.ext" -C 3

# Read affected files
cat src/path/to/dependent-file.ext
```

**Assess:**
- Pattern usage count (in PR vs outside PR)
- Direct dependencies (callers, data consumers)
- Risk level (SAFE | MEDIUM | HIGH | CRITICAL)

**Generate Ripple Effect Warning if needed**

### □ 7. Generate Validated Action Plan
Include for each item:
- Context validation result
- Fix validation research
- Impact analysis findings
- Risk-aware recommendation

### □ 8. Execute Safely
- Start with SAFE items
- Handle MEDIUM risk with care
- Defer HIGH risk to separate PRs
- Reply to NOT APPLICABLE comments with context

---

## Decision Tree

```
┌─ Comment from PR
│
├─ Context Validation
│  ├─ Deprecated stack? ──→ ❌ NOT APPLICABLE → Reply with context
│  ├─ Violates constraint? ──→ ❌ NOT APPLICABLE → Reply with context
│  └─ Valid? ──→ ✅ Continue to Fix Validation
│
├─ Fix Validation
│  ├─ Research documentation ──→ What does official guidance say?
│  ├─ Research best practices ──→ Is this current advice?
│  └─ Verdict:
│     ├─ ❌ WRONG → Find better alternative
│     ├─ ⚠️ OUTDATED → Find current approach
│     └─ ✅ VALIDATED → Continue to Impact Analysis
│
└─ Impact Analysis
   ├─ Search for similar patterns ──→ How many instances?
   ├─ Find dependencies ──→ What depends on this?
   └─ Assess risk:
      ├─ 🟢 SAFE → Apply now
      ├─ 🟡 MEDIUM → Apply with testing
      ├─ 🔴 HIGH → Defer to separate PR
      └─ ⛔ CRITICAL → Redesign required
```

---

## Quick Commands

### Context Check
```bash
# Read project context
cat .project-context.md | grep -i "deprecated\|constraint\|tech.*debt"
```

### Fix Validation
```javascript
// MCP Tool: ref.tools search
mcp__ref__ref_search_documentation({
  query: "Node.js error handling async/await 2024"
})

// MCP Tool: Exa web search
mcp__exasearch__web_search_exa({
  query: "React hooks useState vs useReducer 2024 best practice",
  numResults: 5
})
```

### Impact Analysis
```bash
# Count pattern usage
grep -r "pattern" --include="*.js" | wc -l

# Find with context
grep -r "functionName(" --include="*.js" -B 2 -A 2

# Show only filenames
grep -rl "pattern" --include="*.js"

# Count files
grep -rl "pattern" --include="*.js" | wc -l
```

---

## Red Flags

### Context Validation Red Flags
- ⚠️ Comment mentions tool in "deprecated" list
- ⚠️ Comment suggests approach that violates documented constraints
- ⚠️ Comment is already addressed in "known tech debt"
- ⚠️ Reviewer may not know full project history

### Fix Validation Red Flags
- ⚠️ Documentation shows different approach
- ⚠️ Recent discussions show this is outdated advice
- ⚠️ Multiple sources disagree
- ⚠️ Approach was popular but is now deprecated

### Impact Analysis Red Flags
- ⚠️ Pattern exists in 10+ files outside PR
- ⚠️ Found 20+ callers, most outside PR
- ⚠️ Dependencies use fragile assumptions
- ⚠️ Breaking change requires updating many files
- ⚠️ Reviewers likely didn't see affected code

---

## Example: Quick Validation

### Comment
"Use Promise.all() instead of sequential awaits"

### Context Check
```bash
$ cat .project-context.md | grep -i node
Stack: Node.js 18.x
```
✅ Node 18 supports Promise.all() → APPLICABLE

### Fix Validation
```
ref.tools search: "JavaScript Promise.all concurrent"
→ MDN: Promise.all runs promises concurrently ✅

Exa search: "Promise.all vs sequential await 2024"
→ Best practice: Use Promise.all for independent operations ✅
→ Warning: Fails fast on first rejection ⚠️
```
✅ VALIDATED with caveat

### Impact Analysis
```bash
$ grep -r "await.*await.*await" --include="*.js" | wc -l
47

$ grep -rl "await.*await.*await" --include="*.js" | wc -l
23 files have sequential awaits
PR contains: 1 file
Outside PR: 22 files
```
🟡 MEDIUM RISK - Creates inconsistency, but safe to apply

### Recommendation
✅ **Apply in this PR**
⚠️ **Consider**: Separate PR to convert all 23 files for consistency

---

## Common Validation Patterns

### Pattern: "Use TypeScript"
```
Context check: Is project TypeScript? → .project-context.md
If no TypeScript: ❌ NOT APPLICABLE
```

### Pattern: "Extract to shared utility"
```
Impact analysis: Search for similar code
If found in 3+ places: ✅ Good suggestion
If unique to PR: ❌ Premature abstraction
```

### Pattern: "Change error handling"
```
Impact analysis: Find all callers
Check: What do callers expect?
If 20+ callers outside PR: 🔴 HIGH RISK - Defer
```

### Pattern: "Use newer library version"
```
Context check: What's current version? → package.json
Fix validation: Check breaking changes in changelog
Impact analysis: Search for uses of deprecated API
```

### Pattern: "Add validation"
```
Impact analysis: Check production data
Will existing data fail new validation? → 🔴 HIGH RISK
Need data migration plan
```

---

## Output Template

```markdown
### [File]: [Issue]

**Original Comment:** [text]

**Context Validation:**
Stack: ✅ | ❌
Constraints: ✅ | ❌
Tech debt: ✅ | ❌
**Verdict:** APPLICABLE | NOT APPLICABLE | DEFERRED

**Fix Validation:**
Docs say: [summary]
Best practice: [summary]
**Verdict:** VALIDATED | NEEDS MODIFICATION | ALTERNATIVE

**Impact Analysis:**
Patterns: [N in PR, N outside]
Dependencies: [N callers]
Risk: 🟢 | 🟡 | 🔴 | ⛔
**Ripple Effect:** [if applicable]

**Recommendation:**
[Action with risk awareness]
```

---

## Time Estimates

- **Context check**: 30 seconds per comment
- **Fix validation**: 2-3 minutes per fix (research time)
- **Impact analysis**: 3-5 minutes per significant change (grep + read)
- **Total for 10 comments**: ~45-60 minutes (including research)

**Worth it?** Yes - catches issues that would cause production failures

---

## Success Criteria

- ✅ All comments validated against project context
- ✅ Outdated comments flagged with reasoning
- ✅ Fixes researched via multiple sources
- ✅ Impact on code outside PR assessed
- ✅ Risk levels clearly communicated
- ✅ Safe/risky changes separated
- ✅ Evidence provided (grep results, research links)

---

## Version
- **Workflow Version:** 1.0
- **Last Updated:** 2025-10-24
