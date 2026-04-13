# Code Review

> **v1.1.24** | Quality & Testing | 26 iterations

> Multi-agent swarm code review covering security, performance, style, tests, and documentation -- with evidence-based findings, PR comment analysis, and actionable fix plans.

## The Problem

Code reviews are inconsistent. One reviewer catches security issues but misses performance problems. Another focuses on style but overlooks test gaps. PR comments from three reviewers conflict, lack file/line references, and nobody synthesizes them into a prioritized action plan. When a reviewer writes "this might have a performance issue," there is no evidence, no measurement, and no specific fix -- just a vague concern that gets marked "resolved" without actually being addressed.

The review quality depends entirely on who reviews it and how much time they have that day. Security vulnerabilities slip through because the reviewer is not a security expert. Performance bottlenecks pass because nobody profiles. Test coverage gaps are invisible because nobody checks which lines the tests actually exercise. And when a PR has 30 comments from four reviewers, the author spends more time triaging and deduplicating feedback than fixing the actual issues.

Systematic review that covers all quality dimensions -- security, performance, style, tests, documentation -- on every PR, with evidence for every finding and prioritized action plans, is what teams want but rarely achieve with manual-only review processes.

## The Solution

This plugin provides a multi-agent swarm review system where five specialized reviewers analyze code in parallel: security (vulnerabilities, unsafe patterns, secrets), performance (bottlenecks, optimization opportunities), style (best practices, maintainability), tests (coverage, quality, edge cases), and documentation (comments, API docs, README updates). Every finding includes a file:line reference, evidence type, severity level, confidence score, and suggested fix with specific code changes.

The PR comment analysis capability extracts all comments from GitHub PRs, groups them by file and code section, identifies high-consensus issues (where 2+ reviewers flagged the same concern), and runs a three-phase validation: consolidation, context validation, and impact analysis. The output is a prioritized action plan, not a pile of disconnected comments.

The TRUST 5 framework validates every finding against five dimensions: Truthfulness (code does what it claims), Relevance (changes fit the context), Usability (maintainable and understandable), Safety (no security vulnerabilities), and Timeliness (follows current best practices). Findings require 2+ confirming signals before being flagged, keeping the false positive rate below 5%.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Review quality depends on which reviewer has time today | Five specialized agents review security, performance, style, tests, and docs on every PR |
| Vague comments like "this might be slow" with no evidence | Evidence-based findings with file:line references, severity, confidence scores, and specific fixes |
| 30 PR comments from 4 reviewers with duplicates and conflicts | Consolidated, deduplicated feedback with high-consensus issues identified and prioritized |
| Security vulnerabilities slip through non-expert reviewers | Dedicated security scanner checking for vulnerabilities, unsafe patterns, and secrets |
| No systematic way to prioritize which review comments to fix first | Severity classification (CRITICAL/MAJOR/MINOR/NIT) with impact analysis and action plans |
| Review coverage depends on reviewer expertise | Consistent coverage across all five quality dimensions on every review |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install code-review@skillstack
```

### Verify Installation

After installing, test with:

```
Review the code changes in my current branch for security and performance issues
```

The skill activates automatically when you ask to review code, audit a PR, or assess code quality.

## Quick Start

1. Install the plugin using the commands above.
2. Ask for a review:
   ```
   Review the changes in my latest PR -- focus on security and performance
   ```
3. The skill runs specialized reviewers in parallel, producing findings with file:line references, severity levels, and suggested fixes.
4. Get a prioritized action plan:
   ```
   Prioritize the findings and create a fix plan I can work through
   ```
5. Each finding includes the exact code location, evidence, and a specific fix so you can address issues systematically from CRITICAL to NIT.

## What's Inside

This is a comprehensive single-skill plugin combining four review methodologies, backed by scripts, references, templates, examples, and modules.

| Component | Purpose |
|---|---|
| **code-review** skill | Core methodology: evidence-based review, PR comment analysis, multi-agent swarm, AI consultation, TRUST 5 validation, severity levels, validation rules |
| **8 scripts** | PR comment extraction/filtering, full PR analysis workflow, multi-agent swarm orchestration, security scanning, performance checking, style auditing, AI consultation CLI |
| **8+ reference documents** | Extended patterns, analysis prompts, GitHub API, impact analysis methodology, validation workflows, best practices, review categories |
| **3 templates** | Review checklist (YAML), security rules (JSON), performance thresholds (JSON) |
| **4 examples** | Security review, performance review, style review walkthrough examples |
| **6 modules** | AI debugging, automated code review, performance optimization, smart refactoring, TDD with Context7 |

**Eval coverage:** 13 trigger eval cases + 3 output eval cases.

### How to Use: code-review

**What it does:** Performs systematic code reviews using multi-agent swarm analysis, covering security, performance, style, test coverage, and documentation quality. Also extracts and prioritizes PR comments from GitHub, consolidating feedback from multiple reviewers into action plans. Every finding is evidence-based with file:line references, severity classification, and suggested fixes.

**Try these prompts:**

```
Review all the changes in this branch for security vulnerabilities -- I'm about to merge to production
```

```
Analyze the PR comments on our GitHub PR #142 -- consolidate the feedback and create a prioritized fix plan
```

```
Do a full code review of src/auth/ -- check security, performance, test coverage, and code style
```

```
I need a security audit of our payment processing module before the compliance review next week
```

```
Review my API endpoints for performance bottlenecks -- we're seeing slow response times on the /search endpoint
```

**Key resources:**

| Resource | Topic |
|---|---|
| `extended-patterns.md` | Finding templates, PR comment workflows, swarm execution, CI/CD integration, quality gates |
| `impact-analysis-methodology.md` | Risk assessment framework for evaluating finding severity |
| `validation-workflow.md` | Three-phase validation: consolidation, context validation, impact analysis |
| `best-practices.md` | Code review best practices and reviewer guidelines |
| `review-categories.md` | Severity and scope category definitions |
| `security-rules.json` | Security rule definitions for automated scanning |
| `performance-thresholds.json` | Performance threshold configuration |

**Shipped scripts:**

| Script | What it does |
|---|---|
| `pr-comment-grabber.py` | Extracts all PR comments from GitHub (inline + conversation) |
| `pr-comment-filter.py` | Filters PR comments by criteria (severity, file, reviewer) |
| `analyze-pr.sh` | Full PR analysis workflow |
| `multi_agent_review.py` | Orchestrates multi-agent swarm review |
| `security_scan.sh` | Security vulnerability scanning |
| `performance_check.py` | Performance bottleneck detection |
| `style_audit.py` | Style and best practices audit |
| `consultant_cli.py` | AI consultation CLI supporting 100+ LLM providers |

## Real-World Walkthrough

Your team is preparing to merge a large PR that adds OAuth 2.0 authentication to your FastAPI application. The PR has 847 lines changed across 12 files, and three reviewers have left 28 comments over the past two days. The tech lead wants to ship by Friday but is worried about security -- this is a payment processing application.

You start with the PR comment analysis:

```
Analyze the comments on our GitHub PR -- consolidate the feedback from the three reviewers and identify the highest-priority issues
```

The skill extracts all 28 comments using `pr-comment-grabber.py`, groups them by file, and runs the three-phase analysis. Phase 1 (consolidation) reduces 28 comments to 14 unique issues -- 6 comments were duplicates where two reviewers flagged the same concern. Phase 2 (context validation) checks each finding against the actual code to verify the concern is valid. Phase 3 (impact analysis) scores each finding for severity.

The output identifies three high-consensus issues (2+ reviewers agreed): token storage in localStorage (security concern -- should use httpOnly cookies), missing rate limiting on the token endpoint (DoS vulnerability), and no token rotation on privilege escalation. These get CRITICAL severity because they are security issues in a payment application.

Now you run the full multi-agent swarm review:

```
Run a full code review on the OAuth PR -- all five dimensions: security, performance, style, tests, and documentation
```

Five specialized agents analyze the code in parallel:

**Security Reviewer** finds four issues:
- CRITICAL [src/auth/token.py:47]: JWT secret key loaded from environment variable without fallback -- if env var is missing, the application starts with an empty secret. Evidence: DIRECT. Confidence: 0.95. Fix: add validation that raises on startup if the secret is missing.
- CRITICAL [src/auth/routes.py:23]: Token endpoint has no rate limiting -- attacker could brute-force tokens. Evidence: BEST_PRACTICE. Confidence: 0.90. Fix: add rate limiter middleware.
- MAJOR [src/auth/middleware.py:89]: Token validation does not check the `aud` (audience) claim -- tokens from other applications could be accepted. Evidence: DIRECT. Confidence: 0.85. Fix: add audience validation.
- MINOR [src/auth/utils.py:12]: Password hashing uses bcrypt with default rounds -- acceptable but should document the choice. Evidence: STYLE_RULE. Confidence: 0.70.

**Performance Analyst** finds two issues:
- MAJOR [src/auth/middleware.py:15]: Token validation hits the database on every request to check revocation -- should use a cached revocation list with TTL. Evidence: DIRECT. Confidence: 0.88. Fix: implement Redis-backed revocation cache.
- MINOR [src/auth/routes.py:67]: User lookup during login does two separate queries (email lookup, then role fetch) -- should be a single joined query. Evidence: DIRECT. Confidence: 0.80.

**Test Specialist** finds three gaps:
- MAJOR: No tests for token expiration handling -- what happens when a token expires mid-request?
- MAJOR: No tests for concurrent token refresh -- race condition risk when multiple tabs refresh simultaneously.
- MINOR: Missing edge case test for malformed JWT tokens.

**Style Reviewer** and **Documentation Reviewer** identify four MINOR and NIT issues about naming conventions and missing docstrings.

The prioritized action plan groups findings by severity: fix the 2 CRITICAL issues first (JWT secret validation, rate limiting), then the 4 MAJOR issues (audience claim, revocation cache, test gaps), then the MINOR and NIT issues as time permits.

You work through the CRITICAL issues first, fixing both in under two hours with the specific code changes from the findings. The MAJOR issues take another half day. By Thursday afternoon, the PR passes all review criteria. The tech lead merges confidently on Friday, knowing every security concern was caught, validated, and fixed with evidence.

## Usage Scenarios

### Scenario 1: Pre-merge security audit

**Context:** You are merging a PR that touches authentication code in a healthcare application. HIPAA compliance requires documented security review before deployment.

**You say:** "Run a security audit on this PR -- it touches patient authentication and we need compliance documentation"

**The skill provides:**
- Security reviewer findings with CRITICAL/MAJOR severity for every vulnerability
- File:line references with evidence type (DIRECT, STYLE_RULE, BEST_PRACTICE)
- TRUST 5 validation focusing on Safety dimension
- Specific fix suggestions with code changes
- Compliance-ready finding report with severity, evidence, and resolution status

**You end up with:** A documented security audit with every finding linked to specific code, severity-classified, and accompanied by fix guidance -- ready for the compliance team to review.

### Scenario 2: Consolidating PR feedback from multiple reviewers

**Context:** Your PR has 35 comments from 5 reviewers. Half overlap, some conflict, and you cannot figure out what to fix first.

**You say:** "Analyze the PR comments on our GitHub PR #287 -- consolidate the duplicates and tell me what to fix first"

**The skill provides:**
- All 35 comments extracted and grouped by file
- Duplicate detection: comments addressing the same issue from different reviewers
- High-consensus identification: issues flagged by 2+ reviewers
- Conflict resolution: where reviewers disagree, the analysis notes the disagreement
- Prioritized action plan from CRITICAL to NIT

**You end up with:** 35 comments reduced to 18 unique issues, sorted by priority, with the 4 high-consensus issues flagged for immediate attention.

### Scenario 3: Performance review of a slow endpoint

**Context:** Your /search endpoint responds in 3 seconds when it should be under 500ms. You suspect the code changes from last sprint introduced the regression.

**You say:** "Review the search endpoint code for performance bottlenecks -- it went from 500ms to 3 seconds after last sprint's changes"

**The skill provides:**
- Performance analyst findings with specific bottleneck identification
- File:line references showing the slow code paths
- N+1 query detection, missing index suggestions, caching opportunities
- Before/after performance estimates for each suggested fix
- Prioritized by expected impact (fix the 80% bottleneck first)

**You end up with:** Identified bottlenecks (e.g., N+1 query in the filter logic, missing database index on the search column) with specific fixes and estimated performance improvement per fix.

### Scenario 4: Full quality review before a release

**Context:** You are cutting a release and want a comprehensive review of all changes since the last release. The changes span 40 files across 15 PRs.

**You say:** "Review all changes since our last release tag -- full review across security, performance, style, tests, and docs"

**The skill provides:**
- Multi-agent swarm review across all five dimensions
- Findings aggregated across the full changeset (not per-PR)
- Cross-cutting issues that span multiple files or PRs
- Release readiness assessment based on finding severity
- Go/no-go recommendation with blocking issues listed

**You end up with:** A release readiness report with all CRITICAL and MAJOR findings that must be addressed before release, plus MINOR/NIT items for the next sprint.

## Ideal For

- **Teams with inconsistent review quality** -- the multi-agent swarm ensures security, performance, style, tests, and documentation are covered on every review regardless of who reviews
- **PRs with many comments from multiple reviewers** -- the consolidation and prioritization turns comment chaos into an actionable plan
- **Security-sensitive applications** -- the dedicated security reviewer catches vulnerabilities, secrets, and unsafe patterns with evidence-based findings
- **Pre-release quality gates** -- the severity classification and TRUST 5 validation provide structured go/no-go criteria
- **Compliance-driven organizations** -- evidence-based findings with file:line references and severity levels produce audit-ready review documentation

## Not For

- **Writing new code or implementing features** -- use the relevant development skill (react-development, python-development, etc.)
- **Finding and fixing runtime bugs** -- use [debugging](../debugging/) for systematic root cause analysis
- **Writing tests or setting up test infrastructure** -- use [testing-framework](../testing-framework/) for test design and infrastructure
- **TDD methodology** -- use [test-driven-development](../test-driven-development/) for red-green-refactor workflow

## How It Works Under the Hood

The plugin is a single skill that merges four complementary review methodologies into one unified system.

The **core skill** defines the review framework: evidence-based findings (every finding must have file:line, evidence type, severity, confidence, and fix), the five-agent swarm (security, performance, style, tests, documentation), PR comment analysis (extract, consolidate, validate, prioritize), AI-powered consultation for complex architectural decisions, and the TRUST 5 validation framework.

The **scripts** provide automation: `pr-comment-grabber.py` and `pr-comment-filter.py` extract and filter GitHub PR comments, `multi_agent_review.py` orchestrates the swarm review, `security_scan.sh` and `performance_check.py` run specialized analysis, and `consultant_cli.py` provides AI consultation through 100+ LLM providers via LiteLLM.

The **references** provide depth: extended patterns for finding templates and CI/CD integration, analysis prompts for LLM-based review, impact analysis methodology for risk assessment, and validation workflows for the three-phase process.

The **modules** add specialized capabilities: AI-powered debugging, automated code review, performance optimization patterns, smart refactoring, and TDD integration with Context7 documentation.

Simple requests ("review this file") trigger a single-pass review with all five agents. Complex requests ("analyze the PR comments and create a fix plan") use the PR comment analysis pipeline. Full pre-release reviews combine both approaches across the entire changeset.

## Related Plugins

- **[Testing Framework](../testing-framework/)** -- Test infrastructure setup and suite authoring for the test gaps identified during review
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline integration for automated review gates
- **[Debugging](../debugging/)** -- Root cause analysis for bugs discovered during review
- **[API Design](../api-design/)** -- API design patterns for endpoints identified as needing redesign during review

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
