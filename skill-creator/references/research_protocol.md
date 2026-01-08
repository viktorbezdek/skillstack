# Research Protocol for Skill Creation

Structured approach to researching domains before building skills, ensuring accuracy, currency, and evidence-based content.

---

## Core Principle

**Bad skills are worse than no skills.** They perpetuate errors, waste tokens, and damage trust.

Every skill MUST be:
- ✅ Based on official documentation
- ✅ Tested in real environments
- ✅ Using current package versions
- ✅ Preventing known, verified errors
- ✅ Documented with evidence

---

## When to Research

### Always Research (New Domain)
- Building skill for unfamiliar technology
- First skill in a technology category
- Major version change (v3 → v4)
- No working examples available

### Can Skip Research (Known Domain)
- Domain expert (use it daily)
- Already built working examples
- Minor version updates (patch/minor)
- Similar to existing skill

**Time Investment**: 1-3 hours for new domain, 15-30 min for known domain

---

## Pre-Build Research Checklist

Complete this BEFORE writing skill files:

### Step 1: Identify Official Sources (30 min)

**Find Primary Documentation**:
- [ ] Official docs website
- [ ] Official GitHub repository
- [ ] API documentation (if applicable)
- [ ] Package documentation (npm, PyPI, etc.)

**Verify Documentation Quality**:
- [ ] Last updated within 1 year
- [ ] Examples work when tested
- [ ] Version information present
- [ ] No conflicting information

**Use Available Tools**:
- [ ] Check Context7 MCP for library docs (if applicable)
- [ ] Use WebFetch for official docs
- [ ] Search GitHub for official repos
- [ ] Verify npm/PyPI package exists

**Document Sources**:
```markdown
## Official Sources
1. **Primary Docs**: https://...
   - Version: X.Y.Z
   - Last Updated: YYYY-MM-DD
2. **GitHub Repo**: https://github.com/...
   - Stars: XXX
   - Last Commit: YYYY-MM-DD
3. **Package**: npm/pypi package name
   - Current Version: X.Y.Z
```

### Step 2: Verify Package Versions (15 min)

**Check Latest Versions**:
```bash
# For npm packages
npm view <package-name> version
npm view <package-name> versions --json | tail -20

# For Python packages
pip index versions <package-name>
```

**Document Versions**:
- [ ] Latest stable version identified
- [ ] Breaking changes reviewed
- [ ] Deprecation warnings noted
- [ ] Migration guides read (if major version change)

**Version Documentation Template**:
```markdown
## Package Versions

| Package | Current | Tested | Status | Notes |
|---------|---------|--------|--------|-------|
| main-package | 4.0.0 | 4.0.0 | ✅ Stable | Latest |
| peer-dep-1 | 2.5.0 | 2.5.0 | ✅ Stable | No breaking changes |
| peer-dep-2 | 1.2.0 | 1.2.0 | ⚠️ Beta | Check for updates |

**Last Verified**: YYYY-MM-DD
```

### Step 3: Research Known Issues (30 min)

**Search GitHub Issues**:
- [ ] Search: `"<package-name> error"` (recent, open)
- [ ] Search: `"<package-name> doesn't work"` (recent, closed)
- [ ] Filter: High engagement (comments, reactions)
- [ ] Note: Common error patterns

**Check Community Discussions**:
- [ ] Official Discord/Slack
- [ ] Stack Overflow top questions
- [ ] Reddit r/<technology> posts
- [ ] Twitter/X for recent complaints

**Document Errors**:
```markdown
## Known Issues Discovered

### Issue 1: [Error message or description]
- **Frequency**: Common (50+ reports) / Occasional (10-50) / Rare (<10)
- **Source**: [GitHub Issue #123](link)
- **Cause**: [Root cause explanation]
- **Fix**: [Solution approach]
- **Verified**: ✅ Tested and working / ❌ Not yet tested
- **Affects Versions**: X.Y.Z to X.Y.Z

### Issue 2: ...
```

### Step 4: Build Working Example (1-3 hours)

**Create Test Project**:
```bash
mkdir test-<skill-name>
cd test-<skill-name>
# Follow official docs to set up
```

**Test Complete Workflow**:
- [ ] Initial setup
- [ ] Local development
- [ ] Production build (if applicable)
- [ ] Deployment (if applicable)
- [ ] Common use cases (3-5)

**Document Errors Encountered**:
```markdown
## Build Log

**Date**: YYYY-MM-DD
**Environment**: OS, Node version, etc.

### Setup
```bash
# Commands run
npm create vite@latest
cd project
npm install
```

**Errors Hit**: None / [list errors]

### Development
```bash
npm run dev
```

**Errors Hit**:
1. Error: "Cannot find module X"
   - **Fix**: Added to package.json
   - **Time to Debug**: 10 min
   - **Documented**: ✅

### Production Build
```bash
npm run build
```

**Errors Hit**: None

### Deployment
**Platform**: Cloudflare, Vercel, etc.
**URL**: https://...
**Status**: ✅ Working

**Total Time**: 2 hours
**Total Errors**: 1
```

### Step 5: Cross-Reference Sources (15 min)

**Compare Documentation**:
- [ ] Official docs vs official examples (consistent?)
- [ ] Official docs vs community examples (aligned?)
- [ ] Recent changes vs older tutorials (conflicts?)

**Identify Version-Specific Issues**:
- [ ] v4 works differently than v3?
- [ ] Deprecated patterns still in old docs?
- [ ] New features not widely documented?

**Verify with Multiple Sources**:
- [ ] Official docs ✅
- [ ] Official GitHub examples ✅
- [ ] Community-verified solutions ✅
- [ ] All sources agree on approach ✅

---

## Research Log Template

Create a research log for each skill:

```markdown
# Research Log: [Skill Name]

**Date**: YYYY-MM-DD
**Researcher**: [Your Name]
**Purpose**: Document research for [skill-name] skill

---

## Official Sources Consulted

### Primary Documentation
- **URL**: https://...
- **Version**: X.Y.Z
- **Last Checked**: YYYY-MM-DD
- **Key Pages**:
  - Getting Started: [link]
  - API Reference: [link]
  - Examples: [link]
- **Quality**: Excellent / Good / Poor
- **Notes**: [Any observations]

### GitHub Repository
- **URL**: https://github.com/...
- **Stars**: XXX
- **Latest Release**: vX.Y.Z (YYYY-MM-DD)
- **Open Issues**: XXX (filter: error, bug)
- **Key Issues Reviewed**:
  - #123: [issue title] - [relevance]
  - #456: [issue title] - [relevance]

### Package Registry
- **npm/PyPI**: package-name
- **Current Version**: X.Y.Z
- **Weekly Downloads**: XXX
- **Maintenance**: Active / Stale
- **Last Publish**: YYYY-MM-DD

### Additional Sources
- **Context7 MCP**: ✅ Used / ❌ Not available
- **Official Blog**: [links]
- **Community Forums**: [links]
- **Stack Overflow**: [key questions]

---

## Version Information

| Package | Current | Latest | Tested | Status | Notes |
|---------|---------|--------|--------|--------|-------|
| main-package | X.Y.Z | X.Y.Z | ✅ | Stable | No issues |
| dependency-1 | X.Y.Z | X.Y.Z | ✅ | Stable | Works well |
| dependency-2 | X.Y.Z | X.Y.Z+1 | ⚠️ | Update available | Breaking changes in +1 |

**Last Verified**: YYYY-MM-DD

---

## Known Issues Discovered

### Issue 1: [Error message/pattern]
- **Frequency**: Common / Occasional / Rare
- **Source**: [GitHub Issue #123](link) or [Stack Overflow](link)
- **Reported By**: XXX users / First reported YYYY-MM-DD
- **Cause**: [Root cause - why does it happen?]
- **Affects**: Versions X.Y.Z to X.Y.Z
- **Fix**: [Solution - how to prevent/resolve?]
- **Workaround**: [If fix not available]
- **Verified**: ✅ Tested working / ❌ Not tested yet
- **Priority**: High / Medium / Low (for skill inclusion)

### Issue 2: ...

### Issue 3: ...

**Total Issues Documented**: X
**High Priority**: X
**Will Include in Skill**: X

---

## Working Example

### Build Details
- **Built**: YYYY-MM-DD
- **Location**: /path/to/example or [GitHub repo](link)
- **Deployed**: ✅ [Live URL](https://...) / ❌ Not deployed
- **Time to Build**: X hours
- **Errors Encountered**: X
- **Retries Needed**: X

### Setup Commands
```bash
# Commands used to create working example
npm create vite@latest example -- --template react-ts
cd example
npm install package-name@X.Y.Z
# ... etc
```

### Configuration Files
- `package.json`: ✅ Saved
- `config-file.json`: ✅ Saved
- `.env.example`: ✅ Saved

### Test Results
- **Local Development**: ✅ Works
- **Production Build**: ✅ Works
- **Deployment**: ✅ Works
- **Common Use Cases**: ✅ All work

### Errors Hit During Build
1. **Error**: "Cannot find module X"
   - **Cause**: Missing peer dependency
   - **Fix**: Added to package.json
   - **Time**: 10 minutes
   - **Will Document**: ✅

2. **Error**: ...

**Total Debugging Time**: X minutes

---

## Community Verification

### Discussions Reviewed
- **Discord**: [Server name] - #help channel
  - Common questions: [list]
  - Solutions that work: [list]

- **Stack Overflow**: [Tag: package-name]
  - Top question: [link]
  - Common issues: [patterns]

- **Reddit**: r/[technology]
  - Recent threads: [links]
  - Community consensus: [observations]

### Patterns Identified
- Most users struggle with: [X]
- Common misconception: [Y]
- Best practices from community: [Z]

---

## Uncertainties / Questions

**Unresolved Questions**:
- [ ] [Question 1 - need to clarify]
- [ ] [Question 2 - conflicting information found]
- [ ] [Question 3 - need to test further]

**Action Items**:
- [ ] Test scenario X to confirm Y
- [ ] Contact maintainer about Z
- [ ] Wait for release X.Y.Z to resolve issue #123

---

## Token Savings Estimate

Based on research, estimated token savings:

**Manual Approach** (without skill):
- Baseline: ~XX,XXX tokens
- Expected errors: X
- Expected time: X hours

**With Skill** (estimated):
- With skill: ~X,XXX tokens
- Expected errors: 0
- Expected time: X minutes

**Estimated Savings**: ~XX% tokens, 100% errors

**Will Measure**: ✅ After skill creation

---

## Quality Assessment

### Documentation Quality
- **Official Docs**: ⭐⭐⭐⭐⭐ (5/5) / ⭐⭐⭐⭐☆ (4/5) / etc.
- **Examples Work**: ✅ All / ⚠️ Some / ❌ None
- **Up to Date**: ✅ Current / ⚠️ Mostly / ❌ Outdated
- **Complete**: ✅ Comprehensive / ⚠️ Gaps / ❌ Sparse

### Community Health
- **Active Maintenance**: ✅ Yes / ⚠️ Slow / ❌ Abandoned
- **Issue Response**: ✅ Fast / ⚠️ Slow / ❌ None
- **Community Size**: ✅ Large / ⚠️ Medium / ❌ Small
- **Recent Activity**: ✅ Daily / ⚠️ Weekly / ❌ Monthly+

### Skill Viability
- **Ready to Build**: ✅ Yes / ⚠️ With caveats / ❌ No
- **Expected Quality**: ✅ High / ⚠️ Medium / ❌ Low
- **Confidence Level**: ✅ High / ⚠️ Medium / ❌ Low

---

## Red Flags Encountered

### Documentation Red Flags
- [ ] Examples in docs don't work
- [ ] Multiple conflicting approaches
- [ ] Last updated >1 year ago
- [ ] "Experimental" warnings
- [ ] No version information

**Details**: [Explanation if any checked]

### Community Red Flags
- [ ] Many recent issues about same problem
- [ ] No official team response
- [ ] Community says "docs are wrong"
- [ ] Workarounds instead of fixes
- [ ] Deprecation warnings

**Details**: [Explanation if any checked]

### Technical Red Flags
- [ ] Security vulnerabilities
- [ ] Last publish >2 years ago
- [ ] Breaking changes not documented
- [ ] Conflicting dependencies
- [ ] Tests failing in official repo

**Details**: [Explanation if any checked]

**Action Taken**: [How red flags were addressed]

---

## Decision

### Proceed with Skill?
✅ **YES - Proceed**
- High-quality documentation
- Working example built
- Known issues documented
- Community healthy
- Confidence: High

OR

⚠️ **YES - With Caveats**
- [List caveats]
- [Mitigation strategies]
- Confidence: Medium

OR

❌ **NO - Do Not Proceed**
- [List blocking issues]
- [What would need to change]

---

## Sign-Off

Research complete and verified:

- [x] All official docs reviewed thoroughly
- [x] Latest package versions verified
- [x] Known issues researched on GitHub
- [x] Community discussions reviewed
- [x] Working example built and tested
- [x] All errors documented and fixed
- [x] Quality assessment complete
- [x] Red flags addressed or skill viable despite them
- [x] Ready to proceed with skill creation

**Researcher**: [Your Name]
**Date**: YYYY-MM-DD
**Confidence**: High / Medium / Low
**Estimated Skill Quality**: High / Medium / Low

---

**Next Steps**: Proceed to Step 1.1 (Create Test Evaluations) in main workflow
```

---

## Red Flags System

### Documentation Red Flags

| Red Flag | Severity | Action |
|----------|----------|--------|
| Examples don't work | 🔴 High | Test thoroughly, document fixes |
| Multiple conflicting approaches | 🟡 Medium | Research which is current |
| Last updated >1 year | 🟡 Medium | Verify still accurate |
| "Experimental" warnings | 🟡 Medium | Note in skill, test carefully |
| No version information | 🟠 Low | Cross-reference with package registry |

### Community Red Flags

| Red Flag | Severity | Action |
|----------|----------|--------|
| Many issues, same problem | 🔴 High | Document issue, provide fix in skill |
| No official team response | 🟡 Medium | Rely on community solutions |
| "Docs are wrong" comments | 🟡 Medium | Verify, document correct approach |
| Only workarounds available | 🟠 Low | Include best workaround |
| Deprecation warnings | 🟠 Low | Note deprecated patterns to avoid |

### Technical Red Flags

| Red Flag | Severity | Action |
|----------|----------|--------|
| Security vulnerabilities | 🔴 High | Do not proceed until patched |
| Last publish >2 years | 🟡 Medium | Check if still maintained |
| Breaking changes undocumented | 🟡 Medium | Document in skill |
| Conflicting dependencies | 🟠 Low | Test resolution, document |
| Tests failing in official repo | 🟠 Low | Note limitations |

**Severity Levels**:
- 🔴 **High**: May block skill creation or require significant caveats
- 🟡 **Medium**: Skill viable but needs extra documentation/testing
- 🟠 **Low**: Note and document, proceed normally

---

## Time Estimates

Realistic time for each research step:

| Step | First Time | Known Domain | Can Skip If |
|------|-----------|--------------|-------------|
| Find Official Sources | 30 min | 10 min | Domain expert |
| Verify Package Versions | 15 min | 5 min | Recently verified |
| Research Known Issues | 30 min | 15 min | No changes since last |
| Build Working Example | 1-3 hours | 30-60 min | Have recent example |
| Cross-Reference Sources | 15 min | 5 min | Single source only |
| **Total** | **2-4 hours** | **1-1.5 hours** | - |

**Add Time If**:
- Complex technology (+1-2 hours)
- Poor documentation (+1 hour)
- Many known issues (+30 min)
- No working examples available (+1 hour)

---

## Quality Gates

Research can only proceed to skill creation if:

### Research Complete
- [x] Official documentation reviewed thoroughly
- [x] Context7 MCP checked (if applicable)
- [x] Latest package versions verified
- [x] Known issues researched on GitHub
- [x] Community discussions reviewed

### Example Working
- [x] Test project built from scratch
- [x] Local development tested
- [x] Production build succeeds (if applicable)
- [x] Deployed (if applicable)
- [x] All errors documented and fixed

### Documentation Accurate
- [x] Official docs linked (specific pages)
- [x] Version numbers documented
- [x] Known issues have sources
- [x] Breaking changes noted
- [x] Last verified date recorded

**If any gate fails**: Address issues before proceeding to skill creation.

---

## Integration with Skill Creation Workflow

Research protocol fits into overall workflow:

```
Step 0: Initialize
  ↓
Step 1: Understand the Skill
  ↓
>>> Step 1.1: Research Protocol <<<  [YOU ARE HERE]
  - Complete Pre-Build Research Checklist
  - Create Research Log
  - Build Working Example
  - Sign Off
  ↓
Step 1.2: Create Test Evaluations (EDD)
  ↓
Step 1.3: Plan Structure
  ↓
... continue with skill creation ...
```

**Time Investment**: 2-4 hours for new domain
**Value**: Prevents building skills on outdated/incorrect information
**Output**: Research log, working example, known issues list

---

## Summary Checklist

Before moving to next step (Create Test Evaluations):

- [ ] Official sources identified and reviewed
- [ ] Package versions verified and documented
- [ ] Known issues researched and documented (3+)
- [ ] Working example built and tested
- [ ] All errors encountered documented with fixes
- [ ] Sources cross-referenced for consistency
- [ ] Research log created and complete
- [ ] Quality assessment shows skill is viable
- [ ] No blocking red flags (or addressed)
- [ ] Sign-off complete

**If all checked**: Proceed to Step 1.1 (Create Test Evaluations)

**If any unchecked**: Complete research before proceeding

---

## After Research: Next Steps

✅ **Research phase complete when you have:**
- [ ] Research log in `planning/research-logs/<skill-name>.md`
- [ ] Working example built and tested
- [ ] ≥3 documented patterns/lessons from GitHub analysis
- [ ] Package versions verified current
- [ ] Known errors documented with GitHub issue links

---

### Transition to Build Phase

**Now proceed in this exact order:**

#### Step 1: Initialize Skill Structure (2 minutes)

```bash
# Create skill directory with template
python /path/to/skill-creator/scripts/init_skill.py <skill-name> \
  --path . \
  --template skill-skeleton \
  --auto-fill \
  --create-research-log
```

**Output**: Skill directory with SKILL.md, README.md, template structure

---

#### Step 2: Create Evaluations - EDD (15-30 minutes)

**Before filling any TODOs**, create test scenarios.

See **[evaluation_driven_development.md](evaluation_driven_development.md)** for complete process.

**Quick summary**:
1. Test Claude WITHOUT the skill (baseline)
2. Document struggles and gaps
3. Create 3-5 realistic scenarios
4. Define success criteria
5. Identify what docs to write

**Output**:
- Gap analysis (what information is missing?)
- Test scenarios (how to verify skill works?)
- Priority list (what to document first?)

---

#### Step 3: Fill Template Based on Gaps (20-60 minutes)

Now use your research findings and evaluation gaps to fill SKILL.md:

**Your research findings go into these sections:**

| Research Output | SKILL.md Section | Example |
|----------------|------------------|---------|
| Known errors from GitHub | "Known Issues Prevention" | Issue #123: Missing API key |
| Patterns from repo analysis | "Common Patterns" | Authentication pattern |
| Working example steps | "Quick Start" | 1. Install, 2. Configure, 3. Run |
| Error messages encountered | README "Known Issues Prevented" | "Missing secret key" |
| Package versions | SKILL.md frontmatter | "Latest Versions: pkg@1.2.3" |

**Your evaluation gaps guide what to write:**
- Gap: "Claude didn't know about X" → Add X to SKILL.md
- Gap: "Claude asked about Y" → Add Y to Quick Start
- Gap: "Claude made error Z" → Add Z to Critical Rules

---

#### Visual Workflow

```
Research Phase Complete
         ↓
   [Initialize]
    init_skill.py → Creates template with [TODO:] markers
         ↓
   [Evaluate - EDD]
    Test without skill → Identify gaps → Create scenarios
         ↓
   [Fill Template]
    Use gaps to guide what to write → Fill [TODO:] markers
         ↓
   [Validate]
    validate_skill.py → Fix issues → Test discovery
         ↓
   [Package]
    DONE ✅
```

---

**Next:** See [evaluation_driven_development.md](evaluation_driven_development.md) for detailed EDD process.

---

## Resources

- **Evaluation-Driven Development**: See evaluation_driven_development.md
- **Comprehensive Checklist**: See comprehensive_checklist.md
- **Token Efficiency**: See token_efficiency.md
- **Research Log Template**: Above (copy to planning/research-logs/)

---

**Remember**: 2-4 hours of research saves days of rework. Always verify before building.
