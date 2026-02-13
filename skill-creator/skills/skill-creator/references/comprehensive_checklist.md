# Comprehensive Skill Creation Checklist

Phase-based checklist organizing all quality requirements for skill creation. Use with TodoWrite to track progress.

---

## PRE-BUILD PHASE

**Before starting skill creation:**

### Planning
- [ ] Gathered 3-5 concrete usage examples
- [ ] Identified target user persona
- [ ] Noted trigger phrases users would say
- [ ] Verified skill doesn't already exist
- [ ] Confirmed this is atomic (one domain, not bundle)

### Research (if new domain)
- [ ] Read official documentation
- [ ] Checked Context7 MCP for library docs (if applicable)
- [ ] Verified latest package versions
- [ ] Reviewed GitHub issues for common problems
- [ ] Built working example project from scratch
- [ ] Documented all errors encountered

**Quality Checkpoint:**
✅ Have 3-5 examples, target persona identified, working example built (if applicable)

---

## EVALUATION PHASE

**Create evaluations BEFORE extensive documentation (EDD):**

### Baseline Testing
- [ ] Ran Claude WITHOUT skill
- [ ] Documented struggles and gaps
- [ ] Categorized gaps: information, efficiency, quality

### Test Scenarios
- [ ] Created 3-5 test scenarios from examples
- [ ] Each scenario is independent
- [ ] Success criteria defined clearly
- [ ] Scenarios are realistic (based on actual use)

### Gap Analysis
- [ ] Information gaps documented (what Claude doesn't know)
- [ ] Efficiency gaps identified (repeated code patterns)
- [ ] Quality gaps noted (missing validation/error handling)
- [ ] Gaps prioritized by impact

**Quality Checkpoint:**
✅ 3-5 scenarios created, baseline tested, gaps categorized

---

## STRUCTURE PLANNING PHASE

**Plan before creating files:**

### Resource Planning
- [ ] Scripts identified (for efficiency gaps)
- [ ] References planned (for detailed docs)
- [ ] Assets determined (for output files)
- [ ] Progressive disclosure strategy defined (if >300 lines)

### Pattern Research
- [ ] Searched examples/ for similar skills
- [ ] Documented applicable patterns
- [ ] Noted script patterns
- [ ] Noted reference organization

**Quality Checkpoint:**
✅ Resources planned, patterns identified, structure clear

---

## INITIALIZATION PHASE

**Set up skill structure:**

### Template Setup
- [ ] Initialized from skill-skeleton template
- [ ] Directory structure verified
- [ ] Template files present
- [ ] Reviewed section markers (CORE vs optional)
- [ ] Identified sections to delete

**Quality Checkpoint:**
✅ Template initialized, structure verified

---

## CONTENT CREATION PHASE

**Write skill content:**

### YAML Frontmatter
- [ ] `name`: Present, lowercase with hyphens, gerund form
- [ ] `name`: Max 64 characters
- [ ] `name`: Matches directory name exactly
- [ ] `description`: Present, <1024 characters
- [ ] `description`: Third-person voice ("This skill..." not "You...")
- [ ] `description`: Includes WHAT skill does
- [ ] `description`: Includes WHEN to use (trigger scenarios)
- [ ] `description`: Includes key terms for discoverability
- [ ] `license`: Present (or LICENSE.txt reference)

### SKILL.md Body
- [ ] < 500 lines total
- [ ] < 5000 tokens total
- [ ] Imperative/infinitive form ("To do X, run Y" not "You should")
- [ ] Quick start section (< 5 minutes to first result)
- [ ] Clear resource references (if applicable)
- [ ] Examples for complex operations
- [ ] Error handling documented
- [ ] No hedge words (basically, essentially, typically, generally)
- [ ] No common concept definitions (Claude already knows)
- [ ] No excessive examples (consolidated)

### Scripts (if applicable)
- [ ] Single responsibility per script
- [ ] Explicit error handling with fallbacks
- [ ] No bare `except:` (specific exceptions)
- [ ] Helpful error messages for each exception
- [ ] Recovery guidance provided
- [ ] No silent failures
- [ ] Clear usage documentation
- [ ] All constants justified with comments

### References (if applicable)
- [ ] Table of contents for files > 100 lines
- [ ] Referenced directly from SKILL.md (one level deep)
- [ ] Organized by domain (if multi-domain)
- [ ] Grep patterns included (for large files)

### Assets (if applicable)
- [ ] Templates are complete
- [ ] Templates are tested
- [ ] No hardcoded paths
- [ ] README for asset usage

### README.md (if complex skill)
- [ ] Status badge present (Production Ready / Beta / Experimental)
- [ ] Last Updated date current
- [ ] Production tested evidence included (URL, screenshot, repo link)
- [ ] Auto-trigger keywords comprehensive
  - [ ] Primary keywords (3-5 exact tech names)
  - [ ] Secondary keywords (5-10 related terms)
  - [ ] Error-based keywords (2-5 common errors)
- [ ] "What This Skill Does" section clear
- [ ] "Known Issues Prevented" table with sources
- [ ] "When to Use / Not Use" sections present
- [ ] Token efficiency metrics documented
- [ ] Quick usage example included

**Quality Checkpoint:**
✅ Frontmatter complete, < 500 lines, imperative voice, scripts have error handling, README complete (if applicable)

---

## TOKEN EFFICIENCY PHASE

**Measure and document efficiency gains:**

### Measurement
- [ ] Manual setup tokens measured (without skill)
- [ ] With-skill tokens measured (using skill)
- [ ] Token savings ≥ 50%
- [ ] Time savings measured

### Error Prevention
- [ ] Errors encountered without skill documented
- [ ] Errors prevented with skill: 100%
- [ ] Each error has source link (GitHub issue, docs, etc.)
- [ ] Error messages/codes documented

### Documentation
- [ ] Token efficiency metrics in README.md or SKILL.md
- [ ] Calculation method documented
- [ ] Known issues table with sources

**Quality Checkpoint:**
✅ Token savings ≥50%, all known errors documented with sources

---

## TESTING PHASE

**Test thoroughly before packaging:**

### Local Testing
- [ ] Skill files in correct location
- [ ] SKILL.md valid (no YAML syntax errors)
- [ ] All referenced files exist
- [ ] Scripts execute successfully (if applicable)
- [ ] Templates work without errors (if applicable)

### Multi-Model Testing
- [ ] Tested with Haiku (enough guidance?)
- [ ] Tested with Sonnet (clear and efficient?)
- [ ] Tested with Opus (avoids over-explaining?)

### Scenario Testing
- [ ] Tested with 3+ scenarios from EDD phase
- [ ] Success rate > 90% on scenarios
- [ ] Claude discovers skill automatically
- [ ] Claude applies skill correctly

### Production Testing
- [ ] Built example project in fresh directory
- [ ] Example project runs without errors
- [ ] Example deployed (if applicable)
- [ ] Production evidence documented (URL, screenshot, repo link)

**Quality Checkpoint:**
✅ All models tested, scenarios pass >90%, production example works

---

## QUALITY GATES PHASE

**Final quality checks (DO NOT SKIP):**

### Minimum Requirements (Can't Skip)
- [ ] Frontmatter complete (name + description)
- [ ] Tested locally (skill actually works)
- [ ] No [TODO:] markers left in files
- [ ] Checklist items verified

### Read-Aloud Test
- [ ] Read entire SKILL.md out loud
- [ ] Awkward phrasing fixed
- [ ] Terminology consistent
- [ ] Flow is logical

### Fresh Directory Test
- [ ] Built example in completely fresh directory
- [ ] No dependencies on existing setup
- [ ] No hardcoded paths
- [ ] Works on clean machine

### Code Quality
- [ ] No errors in console
- [ ] No warnings about deprecated packages
- [ ] No placeholder text (TODO, FIXME, XXX, HACK)
- [ ] No debug code or console.log statements
- [ ] Git status clean (no untracked files)

### Content Quality
- [ ] All file paths use forward slashes
- [ ] All examples are runnable
- [ ] All links work
- [ ] Version numbers current

**Quality Checkpoint:**
✅ Read aloud, fresh directory build, no placeholders, no debug code

---

## VALIDATION PHASE

**Automated and manual validation:**

### Automated Validation
- [ ] Ran `validate_skill.py --check-structure`
- [ ] Ran `validate_skill.py --check-content`
- [ ] Ran `validate_skill.py --full-check`
- [ ] All validation checks pass

### Manual Validation
- [ ] Compared against best_practices_checklist.md
- [ ] Reviewed core_principles.md compliance
- [ ] Checked progressive_disclosure.md (if >300 lines)
- [ ] Verified degrees_of_freedom.md appropriate

### Compliance Verification
- [ ] Compared against official Anthropic standards (https://github.com/anthropics/skills/blob/main/agent_skills_spec.md)
- [ ] Reviewed working examples (official skills repo)
- [ ] No deprecated patterns used
- [ ] No non-standard frontmatter fields (except allowed-tools, metadata)
- [ ] Writing style consistent (imperative, third-person)
- [ ] Structure follows official conventions

### Security Check
- [ ] No hardcoded API keys or credentials
- [ ] No sensitive data in skill files
- [ ] Input validation in scripts
- [ ] Safe handling of user-provided data

**Quality Checkpoint:**
✅ All automated checks pass, manual review complete, security verified

---

## PACKAGING PHASE

**Prepare for distribution:**

### Package Creation
- [ ] Ran `package_skill.py <skill-dir>`
- [ ] Package created successfully
- [ ] Package contains all required files

### Documentation
- [ ] README complete (if complex skill)
- [ ] LICENSE information clear
- [ ] Usage examples provided
- [ ] "Last Updated" date current

**Quality Checkpoint:**
✅ Package created, documentation complete

---

## POST-PACKAGE PHASE

**After packaging:**

### Final Verification
- [ ] Installed from package
- [ ] Tested installation
- [ ] Skill discovered by Claude
- [ ] Example workflow tested

### Documentation
- [ ] Change log updated (if applicable)
- [ ] Research log saved (if created)
- [ ] Token metrics recorded

**Quality Checkpoint:**
✅ Package installs, skill discovered, example works

---

## MAINTENANCE PHASE

**Ongoing maintenance (quarterly):**

### Quarterly Review (Every 3 Months)
- [ ] Checked for package updates: `npm view <package> version`
- [ ] Reviewed GitHub issues for skill-related problems
- [ ] Re-tested skill in fresh environment
- [ ] Updated "Last Verified" date if still current
- [ ] Updated package versions if needed
- [ ] Documented breaking changes (if any)
- [ ] Re-measured token efficiency
- [ ] Checked official Anthropic skills for new patterns

### Trigger Events (On-Demand Review)
- [ ] New major version of key dependency released
- [ ] Security vulnerability reported
- [ ] Breaking change announced
- [ ] Official docs updated significantly
- [ ] Community reports skill doesn't work

### Update Process
- [ ] Re-run research checklist
- [ ] Update version numbers
- [ ] Test with new versions
- [ ] Update templates
- [ ] Update documentation
- [ ] Mark "Last Updated" date
- [ ] Commit with changelog

**Quality Checkpoint:**
✅ Skill current, versions updated, testing complete

---

## FINAL SIGN-OFF

**I certify that:**

- [ ] ✅ All checklists above are complete
- [ ] ✅ Skill tested and working in realistic scenarios
- [ ] ✅ Compliant with core principles and best practices
- [ ] ✅ Documentation accurate and current
- [ ] ✅ Token efficiency ≥ 50%
- [ ] ✅ Zero errors from documented issues
- [ ] ✅ Multi-model testing complete (Haiku, Sonnet, Opus)
- [ ] ✅ Production example working (if applicable)
- [ ] ✅ All validation checks pass
- [ ] ✅ Ready for distribution

**Skill Name**: _____________________
**Date**: _____________________
**Creator**: _____________________
**Verified By**: _____________________

---

## Quick Reference: Minimum Quality Gates

If time-constrained, these are the ABSOLUTE MINIMUM (but aim for full checklist):

1. ✅ **Frontmatter Complete**: name + description with trigger terms
2. ✅ **< 500 Lines**: SKILL.md body under 500 lines
3. ✅ **Tested Locally**: Skill actually works when Claude uses it
4. ✅ **Token Savings ≥ 50%**: Measured improvement over manual approach
5. ✅ **No Placeholders**: No [TODO:], FIXME, or unfinished content
6. ✅ **Validation Passes**: `validate_skill.py --full-check` succeeds
7. ✅ **3+ Scenarios**: Tested with at least 3 realistic scenarios

**If any of these fail, DO NOT PACKAGE. Fix and re-test.**

---

## Time Estimates

Realistic time estimates for completing this checklist:

| Phase | First Time | Experienced | Can Skip If |
|-------|-----------|-------------|-------------|
| Pre-Build Planning | 15-30 min | 5 min | Known domain |
| Research | 30-60 min | Skip | Domain expert |
| Evaluation (EDD) | 30-60 min | 20-30 min | Never |
| Structure Planning | 15 min | 5 min | Never |
| Initialization | 2 min | 1 min | Never |
| Content Creation | 30-90 min | 20-40 min | Never |
| Token Efficiency | 20-30 min | 10-15 min | Never |
| Testing | 30-60 min | 15-20 min | Never |
| Quality Gates | 20-30 min | 10 min | Minimum only |
| Validation | 5 min | 2 min | Never |
| Packaging | 2 min | 1 min | Never |
| **Total** | **3-6 hours** | **1.5-2.5 hours** | - |

**Note**: Times assume domain knowledge. Add 1-2 hours for unfamiliar domains.

---

## Usage with TodoWrite

Create TodoWrite todos for each phase:

```markdown
- [ ] Pre-build planning complete
- [ ] Evaluation phase complete (EDD)
- [ ] Structure planning complete
- [ ] Initialization complete
- [ ] Content creation complete
- [ ] Token efficiency measured
- [ ] Testing complete (all models)
- [ ] Quality gates passed
- [ ] Validation passed
- [ ] Packaging complete
- [ ] Final verification complete
```

Mark each as `in_progress` when starting, `completed` when done.

---

## Resources

- **Core Principles**: See references/core_principles.md
- **Best Practices**: See references/best_practices_checklist.md
- **EDD Methodology**: See references/evaluation_driven_development.md
- **Token Efficiency**: See references/token_efficiency.md
- **Research Protocol**: See references/research_protocol.md
- **Validation**: `python scripts/validate_skill.py --help`

---

**Remember**: This checklist exists to ensure quality. Skipping items = lower quality skills. Complete checklists = production-ready skills.
