# Code Review

> **v1.1.24** | Multi-agent swarm code review covering security, performance, style, tests, and documentation -- with PR comment analysis, TRUST 5 validation, and evidence-based findings.
> 1 skill | 19 references | 4 templates | 8 examples | 6 modules | 22 scripts | 13 trigger evals, 3 output evals

## The Problem

Code reviews in most teams are inconsistent. One reviewer checks for security issues, another focuses on style, a third skips the tests entirely. Pull requests with 500+ lines of changes get rubber-stamped because nobody has the bandwidth to review them thoroughly across all quality dimensions simultaneously. Critical security vulnerabilities pass review because the reviewer was focused on performance. Performance bottlenecks ship because the reviewer was focused on code style.

The feedback itself is often low-value. Comments like "looks good" or "maybe consider refactoring this" provide no actionable direction. When comments do identify real issues, they lack file and line references, making them hard to locate. When multiple reviewers leave feedback, nobody consolidates or prioritizes it -- the developer faces 30 unranked comments and must guess which ones matter most.

For teams that want automated code review, the tooling landscape is fragmented. You need separate tools for security scanning, performance analysis, style checking, test coverage, and documentation quality -- each with its own configuration, false positive rate, and output format. The overhead of maintaining five tools often means teams use zero, falling back to manual review that misses what it misses.

## The Solution

This plugin provides a comprehensive code review skill that uses a multi-agent swarm approach: five specialized review agents (security, performance, style, test coverage, documentation) analyze code in parallel, producing evidence-based findings with file:line references, severity levels, confidence scores, and specific fix suggestions. Every finding must cite direct evidence from the code -- no finding is valid without a code location and supporting observation.

The skill also handles PR comment analysis: extracting all comments from GitHub PRs, grouping them by file and code section, identifying high-consensus issues (where 2+ reviewers flagged the same concern), and generating prioritized action plans. The TRUST 5 validation framework (Truthfulness, Relevance, Usability, Safety, Timeliness) provides a structured quality assessment beyond line-level issues.

The plugin ships with 22 scripts for automated analysis, 19 reference files covering best practices, analysis prompts, and example reviews, and 6 deep-dive modules covering AI debugging, automated review, performance optimization, smart refactoring, and TDD.

## Context to Provide

The review produces better findings when you give the skill scope, code to examine, and specific concerns. Without actual code, the skill can only give generic patterns -- with code, it finds specific line-level issues.

**What information to include in your prompt:**

- **Code to review**: Paste the diff, file contents, or specific code snippet. For PR review, provide the diff or describe the changes made
- **Scope**: Which files, directories, or modules? What type of changes? (new feature, refactor, security fix, performance optimization)
- **Dimensions to focus on**: Security, performance, style, test coverage, or documentation -- or all five with a priority order
- **Severity threshold**: Do you want every NIT-level comment or only CRITICAL and MAJOR findings?
- **Language and framework**: Python/FastAPI, TypeScript/React, Go, Java/Spring -- determines applicable linting rules and patterns
- **Domain context**: What does this code do? (payment processing, authentication, data pipeline, public API endpoint) -- security review of payment code looks different from review of a utility function
- **Known concerns**: What specifically worries you? ("I'm not sure the JWT validation is correct" or "concerned about SQL injection in the query builder")
- **Multiple reviewer feedback**: If consolidating PR comments, describe the PR context and paste or describe the comments you received

**What makes results better:**
- Pasting actual code enables file:line references in findings -- "review my auth module" without code produces patterns, not findings
- Specifying the security concern ("worried about JWT algorithm confusion") directs the security agent to check exactly that pattern
- Describing the domain ("this endpoint handles payment processing, PCI-DSS applies") calibrates severity -- a minor input validation gap is CRITICAL in a payment handler, MINOR in an internal tool
- Providing PR comment text for consolidation enables the skill to identify which concerns are shared across reviewers

**What makes results worse:**
- "Review my entire codebase" -- the review surface is too broad; findings become unactionable
- Asking "is this code okay to merge?" -- the skill produces evidence-based findings, not approval stamps
- Not specifying severity thresholds -- you will receive NIT formatting comments alongside CRITICAL security vulnerabilities in the same list

**Template prompt:**
```
Review [file path / PR diff / code snippet below] for [security / performance / style / tests / docs / all dimensions]. Language: [language and framework]. Severity threshold: [CRITICAL only / MAJOR+ / all]. Domain context: [what this code does -- payment processing, authentication, data export, etc.]. Specific concern: [what you are most worried about]. Format: file:line references with evidence and suggested fix for every finding.

[paste code or diff here]
```

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Reviews check whatever the reviewer thinks of -- inconsistent coverage | Five specialized agents cover security, performance, style, tests, and docs in parallel |
| "Looks good to me" on 500-line PRs | Evidence-based findings with file:line, severity, confidence, and suggested fix for every issue |
| PR comments from 3 reviewers -- unsorted, unranked, contradictory | Consolidated comments grouped by file, consensus issues highlighted, prioritized action plan |
| Security issues found in production, not in review | Dedicated security agent catches vulnerabilities, unsafe patterns, and exposed secrets |
| False positives waste developer time | Confidence scoring (0-1) and 2+ confirming signals required before flagging |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install code-review@skillstack
```

### Verify installation

After installing, test with:

```
Review my authentication module for security issues -- I'm worried about JWT handling and password storage
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Review this pull request: [paste diff or describe changes]`
3. The skill analyzes across all five dimensions and produces prioritized findings with file:line references
4. Drill down: `Explain the security finding on line 42 of auth.py and show me the fix`
5. Consolidate: `I have feedback from 3 reviewers on PR #123 -- extract and prioritize all their comments`

---

## System Overview

```
+------------------------------------------------------------------+
|                      code-review skill                            |
+------------------------------------------------------------------+
|                                                                    |
|  Multi-Agent Swarm Review                                          |
|  +----------------------------------------------------------+     |
|  |  +----------+ +----------+ +--------+ +------+ +-------+ |     |
|  |  | Security | | Perform. | | Style  | | Test | | Docs  | |     |
|  |  | Reviewer | | Analyst  | | Review | | Spec | | Review| |     |
|  |  +----+-----+ +----+-----+ +---+----+ +--+---+ +---+---+ |     |
|  |       |             |           |         |         |     |     |
|  |       +------+------+-----+-----+----+----+----+---+     |     |
|  |              |                        |                   |     |
|  |       +------v------+         +-------v-------+           |     |
|  |       | Consolidate |         | TRUST 5       |           |     |
|  |       | & Prioritize|         | Validation    |           |     |
|  |       +------+------+         +-------+-------+           |     |
|  +----------------------------------------------------------+     |
|                        |                                           |
|  +------------------+  |  +------------------+                     |
|  | PR Comment       |  |  | AI Consultation  |                     |
|  | Analysis         |  |  | (LiteLLM)        |                     |
|  +------------------+  |  +------------------+                     |
|                        v                                           |
|  Evidence-Based Findings: file:line, severity, confidence, fix     |
+------------------------------------------------------------------+
```

## What's Inside

| Component | Type | Count |
|---|---|---|
| `code-review` | Skill | 1 comprehensive skill |
| References | Best practices, analysis prompts, validation workflows | 19 files |
| Scripts | PR analysis, security scanning, performance checking, style audit | 22 files |
| Modules | Deep-dive guides: AI debugging, automated review, performance, refactoring, TDD | 6 files |
| Examples | Security, performance, and style review examples | 8 files |
| Templates | Review checklist, security rules, performance thresholds | 4 files |

### Key References

| Reference | Topic |
|---|---|
| `extended-patterns.md` | Detailed finding templates, PR comment workflow, multi-agent execution, CI/CD integration |
| `best-practices.md` | Code review best practices and methodology |
| `analysis-prompt-v2.md` | Enhanced LLM prompt for PR comment analysis with validation |
| `advanced-patterns.md` | Advanced review patterns for complex codebases |
| `impact-analysis-methodology.md` | Risk assessment framework for code changes |
| `validation-workflow.md` | Three-phase validation: Consolidation, Context Validation, Impact Analysis |

### Key Scripts

| Script | Purpose |
|---|---|
| `pr-comment-grabber.py` | Extract all comments from a GitHub PR |
| `pr-comment-filter.py` | Filter and categorize PR comments |
| `analyze-pr.sh` | Full PR analysis workflow |
| `multi_agent_review.py` | Multi-agent swarm orchestration |
| `security_scan.sh` | Security vulnerability scanning |
| `performance_check.py` | Performance bottleneck detection |
| `style_audit.py` | Style and best practices audit |
| `consultant_cli.py` | AI consultation CLI for deep analysis |

### Component Spotlights

#### code-review (skill)

**What it does:** Activates when you need to review code, analyze PRs, audit for security, assess quality, or consolidate review feedback. Uses five specialized review agents working in parallel to cover all quality dimensions with evidence-based findings.

**Input -> Output:** Code diff, PR number, or code snippet -> Prioritized findings with file:line references, severity (CRITICAL/MAJOR/MINOR/NIT), confidence scores (0-1), evidence citations, and specific fix suggestions.

**When to use:**
- Reviewing pull requests with systematic multi-dimensional analysis
- Security auditing code for vulnerabilities, unsafe patterns, and exposed secrets
- Performance reviewing code for bottlenecks and optimization opportunities
- Extracting and prioritizing feedback from multiple PR reviewers
- Assessing code quality before release (compliance, security gates)
- Deep architectural analysis requiring AI-powered consultation

**When NOT to use:**
- Writing new code or implementing features -> use development skills
- Finding and fixing runtime bugs -> use `debugging`
- Writing tests or test infrastructure -> use `testing-framework`
- TDD methodology -> use `test-driven-development`

**Try these prompts:**

```
Review this PR diff for security, performance, and maintainability. The PR adds a new payment endpoint that creates orders and charges via Stripe. Language: Python/FastAPI. Focus on CRITICAL and MAJOR findings only -- I don't need NIT-level style comments before this merge. Specific concern: the Stripe webhook handler and the order query builder.

[paste diff here]
```

```
I have 28 comments from 3 reviewers on PR #456 (adds user invitation system). Reviewer 1 focuses on security, reviewer 2 on tests, reviewer 3 on API design. Consolidate all comments, identify where 2+ reviewers flag the same issue, and give me a prioritized action plan ordered by severity. I want to fix the top 5 issues before merging.
```

```
Security audit src/auth/ and src/middleware/auth_middleware.py. This is our authentication layer for a HIPAA-regulated health data API. Check for: JWT algorithm confusion, missing expiry validation, session fixation, CSRF gaps, and OWASP Top 10 patterns. Report: CRITICAL findings with exploitation scenario first, then MAJOR, then MINOR. Include file:line for every finding.
```

```
Review this function for injection vulnerabilities. It takes user-submitted search terms and builds a database query. Language: Python with SQLAlchemy. Show exactly what is unsafe, how an attacker would exploit it, and the correct parameterized query replacement.

[paste function here]
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Review my code" | "Review the authentication module in src/auth/ -- focus on JWT validation, password hashing, and session management" |
| "Is this PR good?" | "Review PR #123: it adds a new payment endpoint. Check for SQL injection, improper error handling, and missing input validation" |
| "Find bugs" | "Audit src/api/handlers.py for security issues. I need CRITICAL findings with file:line, evidence, and fix code." |
| "Check the PR comments" | "Extract all comments from PR #456 on github.com/org/repo, group by file, identify consensus issues, and prioritize by severity" |

### Structured Prompt Templates

**For comprehensive code review:**
```
Review [file/directory/PR] focusing on [dimensions: security, performance, style, tests, docs]. Severity threshold: [CRITICAL only / MAJOR+ / all]. I care most about [specific concern]. Evidence format: file:line with code context.
```

**For PR comment analysis:**
```
Analyze comments from PR #[number] on [repo]. Consolidate duplicate feedback, identify where 2+ reviewers agree, and produce a prioritized action plan. Group by: [file / severity / reviewer].
```

**For security audit:**
```
Security audit [scope: file, module, or full repo]. Check for: [injection, auth bypass, secrets, SSRF, XSS, etc.]. Report format: CRITICAL findings first with exploitation scenario, then MAJOR, then MINOR.
```

### Prompt Anti-Patterns

- **Reviewing without scope**: "Review my entire codebase" -- focus on specific changes, modules, or concerns. A codebase-wide review produces too many findings to be actionable.
- **Asking for approval instead of analysis**: "Is this code okay to merge?" -- the skill produces evidence-based findings, not approval stamps. Ask for specific quality dimension analysis.
- **Ignoring severity guidance**: Not specifying which severity levels matter means the review includes every NIT-level formatting suggestion alongside CRITICAL security vulnerabilities. Set a threshold.

## Real-World Walkthrough

**Starting situation:** Your team is preparing to launch a payment processing feature. The PR has 800 lines across 12 files: new API endpoints, database models, Stripe integration, and tests. Three team members have reviewed it and left a total of 28 comments. You need to consolidate the feedback, ensure nothing critical was missed, and create an action plan before merge.

**Step 1: PR comment consolidation.** You ask: "Extract and consolidate all 28 comments from PR #789 on our repo. Group by file and identify consensus issues." The skill processes all comments and identifies: 4 high-consensus issues (where 2+ reviewers flagged the same concern), 8 unique findings, and 16 comments that are acknowledgments or discussions. The high-consensus issues are: (1) SQL injection risk in the order query builder, (2) missing rate limiting on the payment endpoint, (3) Stripe API key handling concern, (4) insufficient error logging on payment failures.

**Step 2: Multi-agent swarm review.** You ask: "Now run a full review on the same PR. The human reviewers might have missed things." The five specialized agents analyze in parallel:
- **Security agent** confirms the SQL injection risk (CRITICAL, confidence 0.95) and finds an additional issue: the Stripe webhook signature verification is missing, allowing spoofed webhook events (CRITICAL, confidence 0.9).
- **Performance agent** finds that the order history query lacks an index on `customer_id + created_at` (MAJOR) and that the payment confirmation loop polls synchronously instead of using webhooks (MAJOR).
- **Style agent** identifies inconsistent error handling (some handlers return structured errors, others return raw strings) (MINOR) and unused imports (NIT).
- **Test agent** notes that the happy-path tests are good but edge cases are missing: expired cards, duplicate payments, partial refunds (MAJOR).
- **Documentation agent** flags that the new endpoints are undocumented in the API docs (MINOR).

**Step 3: TRUST 5 validation.** The skill applies the validation framework: Truthfulness (code does what it claims -- mostly, but the webhook handler does not actually verify signatures), Relevance (changes are appropriate for the feature), Usability (code is readable but error handling is inconsistent), Safety (two CRITICAL security issues), Timeliness (follows current Stripe API patterns).

**Step 4: Prioritized action plan.** The skill produces a prioritized list:
1. **CRITICAL**: Add Stripe webhook signature verification (security agent finding + human reviewer #3 concern = high confidence)
2. **CRITICAL**: Parameterize the order query to prevent SQL injection (security agent + 2 human reviewers)
3. **MAJOR**: Add rate limiting to payment endpoint (human consensus + security best practice)
4. **MAJOR**: Add database index on customer_id + created_at (performance agent)
5. **MAJOR**: Add edge case tests for expired cards, duplicate payments, partial refunds (test agent)
6. **MINOR**: Standardize error handling across all new handlers (style agent)
7. **MINOR**: Add API documentation for new endpoints (documentation agent)

**Step 5: Fix verification.** After the developer addresses findings, you ask: "Review the fixes for the 2 CRITICAL and 3 MAJOR issues." The skill verifies that the SQL injection fix uses parameterized queries correctly, the webhook verification calls `stripe.webhooks.constructEvent()` with the correct signing secret, and the rate limiter is configured appropriately.

**Gotchas discovered:** The initial webhook signature verification fix used the wrong Stripe signing secret (test key instead of production key). The security agent caught this in the fix review because it cross-referenced the environment variable name against the Stripe documentation pattern.

## Usage Scenarios

### Scenario 1: Pre-release security audit

**Context:** Your compliance team requires a security review before any user-facing feature launches. The authentication module was last reviewed 6 months ago and has had 40 commits since.

**You say:** "Security audit src/auth/ and src/middleware/auth.py. Check for JWT validation issues, password storage, session management, and OWASP Top 10 patterns."

**The skill provides:**
- CRITICAL/MAJOR findings with file:line references and exploitation scenarios
- JWT-specific checks: algorithm confusion, missing expiry validation, weak signing keys
- Password storage verification: bcrypt/argon2 usage, salt handling
- Session fixation and CSRF checks in middleware
- OWASP Top 10 coverage report

**You end up with:** A security report with evidence-based findings the compliance team can audit, each with severity, exploitation risk, and specific fix code.

### Scenario 2: Onboarding code quality assessment

**Context:** A new developer joined the team and submitted their first PR. You want to give thorough, constructive feedback covering all quality dimensions without overwhelming them.

**You say:** "Review PR #234 from a new team member. Give comprehensive feedback but calibrate for onboarding -- emphasize learning over nitpicking. Focus on patterns they should adopt."

**The skill provides:**
- Findings organized as learning opportunities rather than defects
- Best practice suggestions with links to team conventions
- Pattern-level feedback (not just line-level fixes)
- Positive callouts where the code follows good patterns

**You end up with:** A review that teaches rather than criticizes, with clear patterns the developer can apply to future work.

### Scenario 3: Performance-focused review of a hot path

**Context:** Your API endpoint handling search queries is slow. The PR claims to optimize it by adding caching and query restructuring.

**You say:** "Review this performance optimization PR for our search endpoint. Verify the caching strategy is correct and the query changes actually improve performance. Check for race conditions in the cache layer."

**The skill provides:**
- Cache invalidation analysis: is the TTL appropriate, are cache keys correct, what about stampede protection?
- Query optimization verification: does the new query use indexes, are joins efficient?
- Race condition analysis in concurrent cache access
- Before/after performance characteristic comparison
- Missing edge cases: cache miss thundering herd, stale cache serving

**You end up with:** Verification that the optimization is sound or specific issues to fix before merge, with performance implications quantified.

---

## Decision Logic

**How does the multi-agent swarm work?**

Five specialized agents run in parallel, each focused on one quality dimension. The security reviewer looks for vulnerabilities, the performance analyst identifies bottlenecks, the style reviewer checks patterns and readability, the test specialist assesses coverage, and the documentation reviewer checks inline and API docs. Results are consolidated with deduplication (same issue found by multiple agents counts once with higher confidence).

**When does a finding meet the evidence threshold?**

Every finding requires: (1) a code location (file:line), (2) an evidence type (DIRECT observation, STYLE_RULE violation, or BEST_PRACTICE deviation), (3) a severity level, and (4) a confidence score. Findings require 2+ confirming signals before being flagged -- a single ambiguous indicator is marked "needs manual review" instead of reported as a violation.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| False positives overwhelming developers | More than 5% of findings are not genuine issues | Raise confidence threshold; require 2+ confirming signals; tune security rules |
| Missing context for PR analysis | Review misses business logic issues because it only sees the diff | Provide broader context: describe the feature, link to the spec, identify the hot path |
| Stale review rules | Findings reference outdated patterns or deprecated APIs | Update reference files; the skill uses `best-practices.md` which should track current standards |
| Over-reliance on automated review | Human reviewers defer to the tool and stop thinking critically | Use the tool to augment human review, not replace it; always have a human approve |

## Ideal For

- **Engineering teams with high PR volume** who need consistent, thorough reviews across all quality dimensions without bottlenecking on senior reviewers
- **Security-conscious teams** who need systematic vulnerability scanning with evidence-based findings, not just linter warnings
- **Tech leads consolidating feedback** from multiple reviewers into prioritized action plans
- **Teams with compliance requirements** who need documented, auditable code review evidence with severity and confidence ratings

## Not For

- **Writing new code** -- this skill reviews existing code. For implementation, use language-specific development skills.
- **Runtime bug diagnosis** -- finding and fixing bugs that manifest at runtime. Use `debugging`.
- **Setting up test infrastructure** -- configuring test frameworks, fixtures, and CI test stages. Use `testing-framework`.

## Related Plugins

- **testing-framework** -- Complement code review findings with test coverage improvements
- **debugging** -- Investigate runtime issues that code review identifies as risks
- **cicd-pipelines** -- Integrate automated code review into CI/CD quality gates
- **api-design** -- Review API designs before implementing endpoints
- **git-workflow** -- Branch protection and merge strategies that enforce review requirements

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
