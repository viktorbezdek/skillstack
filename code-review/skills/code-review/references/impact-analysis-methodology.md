# Impact Analysis Methodology

## Overview

Impact analysis identifies how a proposed code change might affect code **outside the Pull Request** that reviewers wouldn't have seen. This prevents the "looks good in isolation, breaks in production" problem.

## Core Principle

**Reviewers see the PR diff. They don't see the 500 other files in your codebase.**

A suggested fix might be correct for the code in the PR but break assumptions made by code elsewhere. Impact analysis finds these hidden dependencies.

---

## Three-Phase Analysis

### Phase 1: Pattern Discovery
**Goal:** Find similar code patterns across the codebase

### Phase 2: Dependency Mapping
**Goal:** Identify what code depends on current behavior

### Phase 3: Risk Assessment
**Goal:** Determine if the change will break anything

---

## Phase 1: Pattern Discovery

### Why It Matters
If a reviewer suggests changing a pattern, that pattern might exist in 50 other files. Changing one instance creates inconsistency or requires changing all instances.

### How to Search

#### 1. Exact Pattern Match
```bash
# Find exact function/method names
grep -r "functionName(" --include="*.js" --exclude-dir=node_modules

# Count occurrences
grep -r "functionName(" --include="*.js" | wc -l
```

#### 2. Similar Logic Patterns
```bash
# Find similar approaches (e.g., validation patterns)
grep -r "if.*validate.*return null" --include="*.py"

# Find error handling patterns
grep -r "try.*except.*pass" --include="*.py"
```

#### 3. API Usage Patterns
```bash
# Find uses of specific library/framework pattern
grep -r "useState(" --include="*.jsx" --include="*.tsx"

# Find database query patterns
grep -r "execute(f\"SELECT" --include="*.py"
```

### What to Look For
- **Count**: How many files use this pattern?
- **Scope**: Are they all in the PR or are many outside it?
- **Consistency**: Would changing this one instance break consistency?

### Example
```bash
$ grep -r "authMiddleware" --include="*.js"
src/routes/user.js:15:  router.use(authMiddleware);
src/routes/admin.js:8:   router.use(authMiddleware);
src/routes/api.js:12:    router.use(authMiddleware);
# 23 more files...

Analysis: authMiddleware used in 26 files
PR changes: 1 file (src/routes/user.js)
Outside PR: 25 files

Implication: Changing authMiddleware signature will break 25 files not in this PR
```

---

## Phase 2: Dependency Mapping

### Why It Matters
Code depends on other code's behavior (return values, side effects, error handling). Changing behavior breaks these dependencies.

### Types of Dependencies

#### A. Direct Callers
Code that calls the function/method being changed

```bash
# Find all callers
grep -r "myFunction(" --include="*.js" -B 2 -A 2

# Look for:
# - How many call sites?
# - What do they expect (return value, side effects)?
# - Are they in the PR or outside it?
```

#### B. Data Flow Dependencies
Code that depends on data structure or format

```bash
# Find code expecting specific data shape
grep -r "\.userId" --include="*.js"

# If PR changes { userId: X } to { user_id: X }
# This finds all code accessing .userId (now broken)
```

#### C. Error Handling Dependencies
Code that depends on how errors are signaled

```bash
# Find code checking for null returns
grep -r "if.*myFunction.*===.*null" --include="*.js"

# If PR changes myFunction to throw instead of return null
# All these checks become dead code (and miss the exception)
```

#### D. Behavioral Dependencies
Code that depends on side effects or timing

```bash
# Find code assuming synchronous behavior
grep -r "myFunction().*someVar" --include="*.js"

# If PR changes myFunction to async
# Code assuming immediate result will break
```

### Analysis Template

For each dependency found:
```markdown
**Dependency:** [file path:line]
**Type:** [direct caller | data flow | error handling | behavioral]
**Current assumption:** [what code expects]
**Impact if changed:** [how will it break]
**In PR?** [yes/no]
```

### Example
```markdown
Found 12 callers of validateEmail():

**Dependency:** src/controllers/user-controller.js:45
**Type:** Direct caller, error handling dependency
**Current assumption:** validateEmail() returns null on failure
**Impact if changed:** Code checks `if (result === null)` - will miss exception
**In PR?** No

**Dependency:** src/services/auth-service.js:78
**Type:** Direct caller, error handling dependency
**Current assumption:** validateEmail() returns null on failure
**Impact if changed:** Code checks `if (!result)` - will miss exception
**In PR?** No

... 10 more similar dependencies outside PR ...

**Conclusion:** Changing validateEmail() to throw will break 12 files, 0 in PR.
```

---

## Phase 3: Risk Assessment

### Risk Levels

#### 🟢 SAFE - Low Risk
- Pattern used only in PR files
- All dependencies in PR
- Breaking change is impossible or easily caught by tests
- No callers outside PR

**Example:**
```
Function renamed, all 3 callers in PR
Tests cover all usage → SAFE
```

#### 🟡 MEDIUM RISK - Requires Care
- Some dependencies outside PR but manageable
- Breaking change possible but testable
- Can verify impact manually
- Alternative: expand PR scope slightly

**Example:**
```
Function signature changed, 5 callers (3 in PR, 2 outside)
Can add 2 files to PR and update callers → MEDIUM RISK
```

#### 🔴 HIGH RISK - Breaking Change
- Many dependencies outside PR
- Breaking change will cascade
- Not feasible to fix in single PR
- Requires staged rollout

**Example:**
```
Error handling changed, 47 callers (1 in PR, 46 outside)
Cannot reasonably update all 46 files in this PR → HIGH RISK
Defer to separate PR or create migration plan
```

#### ⛔ DO NOT MERGE - Critical Risk
- Will definitely break production
- No safe way to apply in isolation
- Requires architecture change or major refactor

**Example:**
```
API contract changed, 200+ callers across entire codebase
External APIs depend on current contract → DO NOT MERGE
Requires API versioning strategy
```

### Risk Assessment Checklist

```markdown
**Files affected outside PR:** [N]
**Feasible to include in PR?** [yes/no]
**Test coverage:** [good/partial/none]
**Breaking change obvious?** [yes/no - will compiler/tests catch it?]
**Rollback complexity:** [easy/hard/impossible]
**Production impact:** [none/limited/widespread/catastrophic]

**Risk Level:** [SAFE | MEDIUM | HIGH | CRITICAL]
**Recommendation:** [apply now | expand PR | defer | redesign]
```

---

## Ripple Effect Warnings

When a change has medium-to-high risk, generate **Ripple Effect Warning**:

### Warning Template
```markdown
⚠️ **Ripple Effect Warning**

**Change:** [what's being changed]
**Direct impact:** [immediate effect]
**Indirect impact:** [cascading effects]
**Hidden dependencies:** [N files outside PR]
**Why reviewers missed this:** [they didn't see affected files]
**Recommended action:** [how to safely handle]
```

### Example Warning
```markdown
⚠️ **Ripple Effect Warning**

**Change:** validateEmail() now throws exception instead of returning null

**Direct impact:**
- 12 callers expecting null return will miss exceptions

**Indirect impact:**
- Unhandled exceptions will crash request handlers
- User-facing error messages will leak stack traces
- Logging won't capture validation failures (currently logs null returns)

**Hidden dependencies:** 12 files outside PR
- 8 controllers (will crash on invalid email)
- 3 services (will propagate exception to unexpected layers)
- 1 background job (will fail silently)

**Why reviewers missed this:**
Reviewers saw the validateEmail() change in isolation. They didn't see:
- How many places call it
- That all callers assume null return
- That no callers have try/catch

**Recommended action:**
1. **Defer this change** to separate PR
2. Add try/catch to all 12 callers first (PR #1)
3. Change validateEmail() to throw (PR #2)
4. Verify no regressions (PR #2)

Applying this fix now will cause 12 production crashes.
```

---

## Common Impact Scenarios

### Scenario 1: Function Signature Change
**Risk:** Breaks all callers expecting old signature

**Search for:**
- All call sites
- Parameter usage
- Return value assumptions

**Example:**
```bash
# Old: getUserData(userId)
# New: getUserData(userId, includeProfile = false)

grep -r "getUserData(" --include="*.js"
# Check if any callers break with new parameter
```

### Scenario 2: Error Handling Change
**Risk:** Code expecting one error signal gets another

**Search for:**
- Return value checks (null, undefined, false)
- Try/catch blocks
- Error callbacks

**Example:**
```bash
# Old: returns null on error
# New: throws exception on error

grep -r "getUserData.*===.*null" --include="*.js"
# All these null checks now miss exceptions
```

### Scenario 3: Async Conversion
**Risk:** Code assuming synchronous breaks

**Search for:**
- Sequential code after function call
- Variable usage immediately after call
- No await keywords

**Example:**
```bash
# Old: const data = processData(input);
# New: const data = await processData(input);

grep -r "processData(" --include="*.js"
# Find calls without await (will get Promise, not data)
```

### Scenario 4: Data Structure Change
**Risk:** Code expecting old structure breaks

**Search for:**
- Property access
- Object destructuring
- Type checks

**Example:**
```bash
# Old: { userId: 123 }
# New: { user_id: 123 }

grep -r "\.userId" --include="*.js"
# All these property accesses now return undefined
```

### Scenario 5: Validation/Security Tightening
**Risk:** Previously valid code now fails validation

**Search for:**
- Existing usage patterns
- Test data
- Production data

**Example:**
```bash
# Old: email regex allows no TLD (.com, .org)
# New: email regex requires TLD

grep -r "@.*\"" src/ tests/
# Check if any test/prod emails lack TLD (now invalid)
```

---

## Tools and Commands

### Essential Grep Patterns

```bash
# Find function/method calls
grep -r "functionName(" --include="*.ext"

# Find property access
grep -r "\.propertyName" --include="*.ext"

# Find imports
grep -r "import.*ModuleName" --include="*.ext"

# Find error handling
grep -r "try.*catch" --include="*.ext" -A 5

# Find null checks
grep -r "=== null\|== null\|!= null\|!== null" --include="*.ext"

# Count occurrences
grep -r "pattern" --include="*.ext" | wc -l

# Show context (3 lines before/after)
grep -r "pattern" --include="*.ext" -C 3
```

### Reading Files for Deep Analysis
```bash
# Read file to understand usage
cat src/path/to/file.js

# Read multiple files
cat src/file1.js src/file2.js src/file3.js
```

### Combining Tools
```bash
# Find pattern, then read all matching files
grep -l "pattern" src/**/*.js | xargs cat
```

---

## Output Format

For each analyzed change:

```markdown
## Impact Analysis: [Change Description]

### Pattern Search
**Query:** `grep -r "pattern" ...`
**Results:** Found [N] instances
- In PR: [N] files
- Outside PR: [N] files

**Pattern consistency:**
[Will this change create inconsistency? Do all instances need updating?]

### Dependency Mapping
**Dependencies found:** [N]

**In PR:**
- [file:line] - [impact description]

**Outside PR:**
- [file:line] - [impact description] ⚠️
- [file:line] - [impact description] ⚠️

### Risk Assessment
**Risk Level:** 🟢 SAFE | 🟡 MEDIUM | 🔴 HIGH | ⛔ CRITICAL

**Reasoning:**
[Why this risk level]

**Recommendation:**
[Apply now | Expand PR to include X files | Defer to separate PR | Redesign]

### Ripple Effect Warning
[If medium-to-high risk, include warning]
```

---

## Best Practices

1. **Always grep before implementing** - Don't assume isolated change
2. **Check outside PR first** - That's where the hidden risk is
3. **Count, don't just find** - Knowing "23 instances" is different from "3 instances"
4. **Read the code, don't just grep** - Context matters
5. **Err on side of caution** - If unsure, mark as higher risk
6. **Document your analysis** - Show evidence, don't just assert
7. **Update .project-context.md** - If you find patterns worth documenting

---

## Example: Complete Impact Analysis

```markdown
## Impact Analysis: Change Authentication Middleware

### Change Proposed
Reviewer suggests: "Add rate limiting to authMiddleware"

### Pattern Search
**Query:** `grep -r "authMiddleware" --include="*.js"`
**Results:** Found 26 instances
- In PR: 1 file (src/routes/user.js)
- Outside PR: 25 files

**Pattern consistency:**
All 26 files use authMiddleware the same way:
```javascript
router.use(authMiddleware);
```

Adding rate limiting won't break this usage pattern. ✅

### Dependency Mapping
**Dependencies found:** 25 outside PR

**All dependencies are identical:**
- src/routes/admin.js:8 - router.use(authMiddleware)
- src/routes/api.js:12 - router.use(authMiddleware)
- [23 more similar usages]

**None depend on specific behavior** - they just pass requests through middleware.

### Risk Assessment
**Risk Level:** 🟢 SAFE

**Reasoning:**
- Adding rate limiting is additive (doesn't change existing behavior)
- All usages are identical and simple
- No code depends on absence of rate limiting
- Middleware interface unchanged (still req, res, next)

**Recommendation:**
✅ Apply now - Safe to implement in this PR

No ripple effect warning needed.
```

---

## Version
- **Methodology Version:** 1.0
- **Last Updated:** 2025-10-24
