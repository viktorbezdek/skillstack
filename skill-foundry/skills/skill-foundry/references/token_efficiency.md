# Token Efficiency Measurement

Quantitative methodology for measuring and documenting skill value through token savings and error prevention.

---

## Why Measure Token Efficiency?

Skills must provide measurable value over manual approaches:

1. **Justifies Skill Existence**: Demonstrates concrete improvement
2. **Informs Iteration**: Shows where skill adds most value
3. **Validates Quality**: Skills with <50% savings may need improvement
4. **Guides Users**: Helps users understand when to use skill

**Core Principle**: A skill should save ≥50% tokens and prevent 100% of documented errors.

---

## Measurement Methodology

### Step 1: Establish Baseline (Without Skill)

**Procedure**:
1. Choose a representative task from your test scenarios
2. Ask Claude to complete it WITHOUT loading the skill
3. Track conversation until task completion
4. Document:
   - Total tokens used
   - Number of errors encountered
   - Time to completion
   - Number of retry cycles

**Example Baseline Session**:
```
Task: Set up Tailwind v4 with shadcn/ui in Vite + React
WITHOUT skill-creator/tailwind-v4-shadcn skill

Tokens: ~15,000 total
  - Initial planning: 2,000
  - Configuration attempts: 8,000
  - Error debugging: 5,000

Errors Encountered: 3
  1. CSS @theme inline parse error (1.5k tokens to debug)
  2. tw-animate-css import not found (2k tokens to debug)
  3. Dark mode toggle not working (1.5k tokens to debug)

Retry Cycles: 4
  - Try 1: CSS parse error
  - Try 2: Import error
  - Try 3: Dark mode issue
  - Try 4: Success

Time: ~45 minutes (multiple debugging cycles)
```

### Step 2: Measure With Skill

**Procedure**:
1. Same representative task
2. Ask Claude to complete it WITH the skill loaded
3. Track conversation until task completion
4. Document:
   - Total tokens used
   - Number of errors encountered
   - Time to completion
   - Number of retry cycles

**Example With-Skill Session**:
```
Task: Set up Tailwind v4 with shadcn/ui in Vite + React
WITH skill-creator/tailwind-v4-shadcn skill

Tokens: ~5,000 total
  - Skill discovery: 500
  - Skill content loading: 2,000
  - Implementation (templates): 2,000
  - Verification: 500

Errors Encountered: 0
  - Skill prevents CSS @theme error (correct syntax provided)
  - Skill prevents import error (correct dependencies listed)
  - Skill prevents dark mode issue (working template included)

Retry Cycles: 1 (success on first try)

Time: ~10 minutes (direct implementation)
```

### Step 3: Calculate Metrics

**Token Savings**:
```
Savings = (Baseline Tokens - With-Skill Tokens) / Baseline Tokens × 100%
Savings = (15,000 - 5,000) / 15,000 × 100%
Savings = 67%
```

**Error Prevention**:
```
Errors Prevented = Baseline Errors - With-Skill Errors
Errors Prevented = 3 - 0 = 3 (100% prevention)
```

**Time Savings**:
```
Time Savings = (Baseline Time - With-Skill Time) / Baseline Time × 100%
Time Savings = (45 min - 10 min) / 45 min × 100%
Time Savings = 78%
```

**Retry Reduction**:
```
Retry Reduction = Baseline Retries - With-Skill Retries
Retry Reduction = 4 - 1 = 3 fewer cycles
```

---

## Quality Thresholds

### Minimum Acceptable Metrics

| Metric | Minimum Threshold | Ideal Target |
|--------|------------------|--------------|
| Token Savings | ≥ 50% | ≥ 60% |
| Error Prevention | 100% of documented errors | 100% + unexpected |
| Time Savings | ≥ 50% | ≥ 70% |
| Success Rate | ≥ 90% on first try | ≥ 95% |

**If skill doesn't meet minimums**: Iterate on skill content, add missing information, improve templates.

---

## Documentation Requirements

### In SKILL.md or README.md

Include a metrics section:

```markdown
## Token Efficiency

**Measured Against**: [Task description]
**Baseline** (without skill): ~15,000 tokens, 3 errors, 45 minutes
**With Skill**: ~5,000 tokens, 0 errors, 10 minutes
**Savings**: 67% tokens, 100% error prevention, 78% time

### Errors Prevented

This skill prevents 3 documented errors:

1. **CSS @theme inline parse error**
   - **Source**: [Tailwind v4 GitHub Issue #123](link)
   - **Cause**: Incorrect @theme syntax in CSS file
   - **Fix**: Use `@theme inline` directive as documented

2. **tw-animate-css import not found**
   - **Source**: [shadcn/ui Issue #456](link)
   - **Cause**: shadcn init adds non-existent import
   - **Fix**: Remove tw-animate-css import from index.css

3. **Dark mode toggle not working**
   - **Source**: [Common mistake in docs](link)
   - **Cause**: Missing ThemeProvider wrapper
   - **Fix**: Include ThemeProvider template with correct structure
```

### Required Elements

- [ ] **Baseline measurement**: Tokens, errors, time
- [ ] **With-skill measurement**: Tokens, errors, time
- [ ] **Savings percentages**: Token, error, time
- [ ] **Errors prevented table**: With sources
- [ ] **Source links**: GitHub issues, docs, Stack Overflow
- [ ] **Measurement date**: When metrics were captured
- [ ] **Task description**: What was measured

---

## Error Documentation Format

### Known Issues Table

```markdown
| Error | Why It Happens | Source | Fix |
|-------|---------------|---------|-----|
| "Cannot find module X" | Missing dependency | [Issue #123](link) | Add to package.json |
| "Build failed: Y" | Config missing | [Docs](link) | Include in config template |
| "Runtime error: Z" | API change | [Changelog](link) | Use updated syntax |
```

### Error Entry Requirements

Each documented error must have:

1. **Error Message**: Exact text or pattern
2. **Root Cause**: Why it happens
3. **Source**: Link to GitHub issue, docs, Stack Overflow, etc.
4. **Fix**: How skill prevents it
5. **Verification**: Tested that skill actually prevents it

**Example Complete Entry**:
```markdown
**Error**: `Error: Cannot find module 'hono'`
- **Cause**: Missing peer dependency not installed by package manager
- **Source**: [Hono GitHub Issue #789](https://github.com/honojs/hono/issues/789)
- **Fix**: Skill's package.json template includes hono explicitly
- **Tested**: ✅ Fresh install with template prevents error
```

---

## Measurement Best Practices

### 1. Use Realistic Tasks

❌ **Bad**: "Create a hello world app"
✅ **Good**: "Set up Tailwind v4 with shadcn/ui, dark mode, and form validation"

**Why**: Simple tasks don't reveal skill value. Use tasks that would normally cause errors.

### 2. Test Multiple Scenarios

❌ **Bad**: Measure one simple scenario
✅ **Good**: Measure 3-5 scenarios of varying complexity

**Example Scenarios**:
- Scenario 1: Basic setup (foundation)
- Scenario 2: Add advanced feature (intermediate)
- Scenario 3: Integrate with other service (complex)
- Scenario 4: Debug common issue (error-focused)
- Scenario 5: Deploy to production (complete workflow)

### 3. Document Methodology

Include in documentation:

```markdown
## Measurement Methodology

**Task**: Setup Next.js 15 with Clerk authentication and protected routes
**Baseline Approach**: Manual setup following official docs
**With-Skill Approach**: Using clerk-auth skill templates
**Model**: Claude Sonnet 3.5
**Date**: 2025-11-01
**Attempts**: 3 baseline, 3 with-skill (averaged)
```

### 4. Account for Variability

- Run 3+ attempts for both baseline and with-skill
- Average the results
- Note any outliers
- Document any anomalies

**Example**:
```markdown
**Baseline Attempts**:
- Attempt 1: 14,500 tokens, 2 errors
- Attempt 2: 16,200 tokens, 3 errors
- Attempt 3: 14,800 tokens, 2 errors
- **Average**: 15,167 tokens, 2.3 errors

**With-Skill Attempts**:
- Attempt 1: 5,200 tokens, 0 errors
- Attempt 2: 4,900 tokens, 0 errors
- Attempt 3: 5,100 tokens, 0 errors
- **Average**: 5,067 tokens, 0 errors

**Savings**: 67% tokens, 100% error prevention
```

---

## Calculating ROI (Return on Investment)

### Skill Creation Cost

```
Skill Creation Time: 2-6 hours (first skill in domain)
Skill Creation Tokens: ~10,000 (research + testing)
```

### Break-Even Analysis

```
Token Savings Per Use: 10,000 tokens (baseline 15k - skill 5k)
Uses to Break Even: 1 use (10,000 creation cost / 10,000 savings)
```

**After 1 use**: Skill has paid for itself
**After 10 uses**: 100,000 tokens saved (minus 10k creation = 90k net savings)

### Value Increases Over Time

```
Month 1: 5 uses × 10k savings = 50k tokens saved
Month 2: 8 uses × 10k savings = 80k tokens saved
Month 3: 12 uses × 10k savings = 120k tokens saved
Total: 250k tokens saved (25x creation cost)
```

**Plus**: Error prevention value (time saved debugging, frustration avoided)

---

## Real-World Examples

### Example 1: Cloudflare Workers Skill

```markdown
## Token Efficiency

**Task**: Set up Cloudflare Worker with Hono, Static Assets, D1, R2
**Baseline**: 18,000 tokens, 5 errors, 90 minutes
**With Skill**: 6,000 tokens, 0 errors, 20 minutes
**Savings**: 67% tokens, 100% errors, 78% time

**Errors Prevented** (5):
1. Wrangler config incorrect format
2. Static assets 404 in production
3. D1 bindings not accessible
4. R2 bucket permissions error
5. CORS issues with frontend

**Sources**:
- [Wrangler docs](link)
- [GitHub Issue #123](link)
- [Cloudflare Community thread](link)

**Measured**: 2025-10-20 with Claude Sonnet 3.5
```

### Example 2: React Hook Form + Zod Skill

```markdown
## Token Efficiency

**Task**: Setup form with validation, error handling, submit
**Baseline**: 12,000 tokens, 4 errors, 60 minutes
**With Skill**: 4,500 tokens, 0 errors, 15 minutes
**Savings**: 62% tokens, 100% errors, 75% time

**Errors Prevented** (4):
1. Zod schema type mismatch with form
2. useForm resolver not configured
3. Error messages not displaying
4. Form submission not typed correctly

**Sources**: All from react-hook-form GitHub issues

**Measured**: 2025-10-15 with Claude Sonnet 3.5
```

---

## When Metrics Are Poor

### If Token Savings < 50%

**Diagnoses**:
- Skill too verbose (trim content)
- Task too simple (doesn't need skill)
- Skill doesn't address main pain points (research gaps)

**Actions**:
1. Run `analyze_conciseness.py` - find verbose sections
2. Re-run EDD - identify what actually helps
3. Remove content that doesn't improve outcomes
4. Test again

### If Errors Not Prevented

**Diagnoses**:
- Missing critical information
- Templates don't include fixes
- Error only documented, not actually prevented

**Actions**:
1. Review each documented error
2. Test that skill actually prevents it
3. If not prevented, add template/config/instruction
4. Re-test until 100% prevention

### If Time Savings < 50%

**Diagnoses**:
- Skill takes too long to read
- Templates require significant modification
- Process still has retry cycles

**Actions**:
1. Simplify skill content
2. Make templates more copy-paste ready
3. Add quick start section
4. Test workflow end-to-end

---

## Maintenance: Re-Measure Quarterly

When maintaining skills, re-measure metrics:

```markdown
## Token Efficiency History

**Latest (2025-11-01)**: 67% savings, 0 errors
**Previous (2025-08-01)**: 65% savings, 1 error
**Trend**: ✅ Improving

**Changes Since Last Measurement**:
- Updated package versions (Hono 4.5.0 → 4.6.0)
- Added error handling example
- Improved quick start section

**Baseline Shift**: No significant change (still ~15k tokens manual)
```

**Why Re-Measure**:
- Package updates may change baseline
- Skill improvements should increase savings
- New errors may emerge (need documentation)
- Validates skill remains valuable

---

## Summary Checklist

Before marking skill complete:

- [ ] Baseline measurement completed (tokens, errors, time)
- [ ] With-skill measurement completed (tokens, errors, time)
- [ ] Token savings ≥ 50%
- [ ] Error prevention = 100% of documented errors
- [ ] Each error has source link
- [ ] Metrics documented in SKILL.md or README.md
- [ ] Measurement methodology documented
- [ ] Task description included
- [ ] Date recorded
- [ ] Multiple scenarios tested (3+)

**If any item unchecked**: Complete before packaging.

---

## Resources

- **EDD Methodology**: See evaluation_driven_development.md
- **Research Protocol**: See research_protocol.md
- **Comprehensive Checklist**: See comprehensive_checklist.md
- **Analysis Tool**: `python scripts/analyze_conciseness.py`

---

**Remember**: Token efficiency proves skill value. Without measurement, you can't validate quality or justify skill existence.
