---
name: code-review
description: "Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and documentation. Analyze PRs, extract and prioritize comments, and generate actionable fix plans. Use when: reviewing code, auditing a pull request, checking code quality, analyzing PR comments, performing a security audit, or validating changes before merge. Triggers: 'code review', 'review code', 'PR review', 'pull request', 'review my PR', 'check code quality', 'analyze PR', 'review changes', 'security audit', 'review this diff', 'code feedback', 'what should I fix'."
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# Comprehensive Code Review Skill

This skill is a curated merge of four complementary code review skills:

1. **Kanitsal Kod Incelemesi**: Evidence-based multi-agent swarm review with specialized reviewers
2. **PR Comment Analysis**: Extract, consolidate, and prioritize GitHub PR comments
3. **Development Workflow Specialist**: TDD, debugging, performance optimization, and automated code review
4. **Consultant**: AI-powered deep analysis for complex architectural and security reviews

## Table of Contents

- [Quick Reference](#quick-reference)
- [When to Use](#when-to-use)
- [Core Capabilities](#core-capabilities)
- [Evidence-Based Review Framework](#evidence-based-review-framework)
- [PR Comment Analysis Workflow](#pr-comment-analysis-workflow)
- [Multi-Agent Swarm Review](#multi-agent-swarm-review)
- [AI-Powered Consultation](#ai-powered-consultation)
- [Development Workflow Integration](#development-workflow-integration)
- [Quality Gates and TRUST 5 Validation](#quality-gates-and-trust-5-validation)
- [Resources Reference](#resources-reference)
- [Integration Examples](#integration-examples)

---

## Quick Reference

**Core Capabilities:**
- Multi-Agent Swarm Review: 5 specialized reviewers (security, performance, style, tests, docs)
- PR Comment Extraction: Comprehensive GitHub API-based comment fetching
- Comment Consolidation: Group by file, identify consensus, prioritize by severity
- Impact Analysis: Assess if proposed fixes might break code elsewhere
- AI Consultation: Deep analysis using LiteLLM for complex decisions
- TRUST 5 Validation: Truthfulness, Relevance, Usability, Safety, Timeliness

**Severity Levels (Hierarchical Organization):**
- **SONKEIGO (CRITICAL)**: Architecture-level issues (security vulnerabilities, data loss risks)
- **TEINEIGO (MAJOR)**: Module-level issues (performance bottlenecks, maintainability problems)
- **CASUAL (MINOR)**: Function-level improvements (code style, readability)
- **NIT**: Line-level suggestions (formatting, naming)

**Evidence Types:**
- **DIRECT**: Code location with [file:line] reference
- **STYLE_RULE**: Style guide reference with [rule_id]
- **BEST_PRACTICE**: Industry best practice citation [reference]

---

## When to Use

**Use this skill when:**
- Reviewing PRs systematically with multiple quality dimensions
- Extracting and consolidating feedback from multiple reviewers
- Need evidence-based findings with file:line references
- Assessing security vulnerabilities, performance bottlenecks, or code quality
- Creating action plans from PR comments
- Complex architectural decisions requiring deep analysis
- Audit requirements mandate systematic review (compliance, release gates)
- Quality metrics indicate degradation (test coverage drop, complexity increase)

**Do NOT use for:**
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)
- Questions answerable by reading 1-2 files

---

## Core Capabilities

### 1. Evidence-Based Code Review
Every finding MUST include:
- Code location: `[file:line]` with surrounding context (5 lines before/after)
- Evidence type: DIRECT, STYLE_RULE, or BEST_PRACTICE
- Reference source: Style guide section, security advisory, performance benchmark
- Severity: CRITICAL, MAJOR, MINOR, or NIT
- Confidence score: 0.0-1.0
- Suggested fix with specific code changes

### 2. PR Comment Analysis
- Fetches ALL comments from GitHub PR (inline + conversation)
- Handles pagination (works with 100s of comments)
- Groups comments by file path and code section
- Identifies "High Consensus Issues" (2+ reviewers same concern)
- Three-phase analysis: Consolidation, Context Validation, Impact Analysis

### 3. Multi-Agent Swarm Review
Five specialized review agents working in parallel:
- **Security Reviewer**: Vulnerabilities, unsafe patterns, secrets
- **Performance Analyst**: Bottlenecks, optimization opportunities
- **Style Reviewer**: Code style, best practices, maintainability
- **Test Specialist**: Test coverage, quality, edge cases
- **Documentation Reviewer**: Comments, API docs, README updates

### 4. AI-Powered Consultation
- Supports 100+ LLM providers through LiteLLM
- Deep analysis for complex architectural decisions
- Security vulnerability analysis across large codebases
- Async operation with session management
- Token counting and context overflow protection

### 5. TRUST 5 Validation Framework
- **Truthfulness**: Code does what it claims
- **Relevance**: Changes are appropriate for the context
- **Usability**: Code is maintainable and understandable
- **Safety**: No security vulnerabilities or data risks
- **Timeliness**: Follows current best practices

---

## Evidence-Based Review Framework

### Finding Template

Every review finding MUST use this structure:

```yaml
finding:
  issue: "[description of problem]"
  evidence:
    location: "[file:line]"
    code_snippet: |
      [5 lines before]
      > [problematic line(s)]
      [5 lines after]
    evidence_type: "DIRECT | STYLE_RULE | BEST_PRACTICE"
  reference:
    source: "[style_guide | security_advisory | benchmark | standard]"
    citation: "[specific section or rule ID]"
    url: "[optional reference link]"
  severity: "CRITICAL | MAJOR | MINOR | NIT"
  scope: "ARCHITECTURE | MODULE | FUNCTION | LINE"
  confidence: number (0.0-1.0)
  suggested_fix: |
    [specific code change or approach]
```

### Example Finding

```yaml
finding:
  issue: "SQL injection vulnerability in user query"
  evidence:
    location: "src/api/users.js:42"
    code_snippet: |
      40: app.get('/users', (req, res) => {
      41:   const userId = req.query.id;
      > 42:   const sql = `SELECT * FROM users WHERE id = ${userId}`;
      43:   db.query(sql, (err, results) => {
      44:     res.json(results);
    evidence_type: "DIRECT"
  reference:
    source: "OWASP Top 10 2021"
    citation: "A03:2021 - Injection"
    url: "https://owasp.org/Top10/A03_2021-Injection/"
  severity: "CRITICAL"
  scope: "FUNCTION"
  confidence: 1.0
  suggested_fix: |
    Use parameterized queries:
    const sql = 'SELECT * FROM users WHERE id = ?';
    db.query(sql, [userId], (err, results) => {
```

### Validation Rules

**CRITICAL RULES - ALWAYS FOLLOW:**
- NEVER approve code without evidence: Require actual execution, not assumptions
- ALWAYS provide line numbers: Every finding MUST include file:line reference
- VALIDATE findings against multiple perspectives: Cross-check with complementary tools
- DISTINGUISH symptoms from root causes: Report underlying issues, not just manifestations
- AVOID false confidence: Flag uncertain findings as "needs manual review"
- PRESERVE context: Show surrounding code (5 lines before/after minimum)
- TRACK false positives: Learn from mistakes to improve detection accuracy

**Validation Threshold**: Findings require 2+ confirming signals before flagging as violations.

---

## PR Comment Analysis Workflow

### Step 1: Extract PR Comments

```bash
cd /path/to/your/repo
python scripts/pr-comment-grabber.py owner/repo PR_NUMBER
```

Creates `pr-code-review-comments/pr{NUM}-code-review-comments.json`

### Step 2: Analyze with Three-Phase Validation

**Phase A: Initial Consolidation**
- Group comments by file and identify consensus
- Categorize by type (critical/design/style)

**Phase B: Context Validation**
- Check `.project-context.md` for project-specific constraints
- Validate comment applicability
- Flag outdated comments based on wrong assumptions

**Phase C: Impact Analysis**
- Search codebase for similar patterns using Grep
- Identify dependencies and potential breaking changes
- Generate "ripple effect" warnings for risky changes

### Step 3: Generate Action Plan

Priority levels:
1. **Critical**: Bugs, security issues, performance problems, high-consensus issues
2. **Design**: Architecture improvements, refactoring suggestions
3. **Style**: Code style, naming conventions, documentation nitpicks

### Comment JSON Schema

**Review comment (inline):**
```json
{
  "comment_type": "review",
  "id": 123456789,
  "user": "reviewer-username",
  "body": "Consider using a constant here instead of magic number",
  "path": "src/utils/constants.py",
  "line": 42,
  "diff_hunk": "@@ -40,6 +40,8 @@ ...",
  "created_at": "2025-01-15T14:30:00Z",
  "html_url": "https://github.com/owner/repo/pull/42#discussion_r123456789"
}
```

**Issue comment (general):**
```json
{
  "comment_type": "issue",
  "id": 987654321,
  "user": "qodo-merge",
  "body": "## PR Analysis Summary\n...",
  "created_at": "2025-01-15T12:00:00Z",
  "html_url": "https://github.com/owner/repo/pull/42#issuecomment-987654321"
}
```

---

## Multi-Agent Swarm Review

### Execution Flow

```bash
#!/bin/bash
PR_NUMBER="$1"
FOCUS_AREAS="${2:-security,performance,style,tests,documentation}"

# Phase 1: PR Information Gathering
gh pr view "$PR_NUMBER" --json title,body,files,additions,deletions > pr-info.json
gh pr checkout "$PR_NUMBER"

# Phase 2: Initialize Review Swarm (5 specialized agents)
# Security, Performance, Style, Tests, Documentation

# Phase 3: Parallel Specialized Reviews
# All 5 reviews run concurrently

# Phase 4: Quality Audit Pipeline
# Run complete audit with evidence collection

# Phase 5: Aggregate Findings
# Merge all reviews, calculate scores

# Phase 6: Generate Fix Suggestions
# Use AI for automated fix recommendations

# Phase 7: Assess Merge Readiness
# Apply quality gates

# Phase 8: Create Review Comment
# Post evidence-based review to PR
```

### Review Output Format

```markdown
# Automated Code Review (Evidence-Based)

**Overall Score**: 85/100
**Merge Ready**: Yes/No

## Review Summary
| Category | Score | Status |
|----------|-------|--------|
| Security | 90/100 | PASS |
| Performance | 85/100 | PASS |
| Style | 80/100 | PASS |
| Tests | 75/100 | FAIL |
| Quality | 88/100 | PASS |

## SONKEIGO (CRITICAL) - Architecture-Level Issues
[Critical findings with evidence]

## TEINEIGO (MAJOR) - Module-Level Issues
[Major findings with evidence]

## CASUAL (MINOR) - Function-Level Improvements
[Minor findings with evidence]

## NIT - Line-Level Suggestions
[Nits with references]
```

---

## AI-Powered Consultation

For complex analysis requiring deep reasoning, use the Consultant tool.

### Basic Usage

```bash
uvx --from {SCRIPTS_PATH} consultant-cli \
  --prompt "Analyze this code for security vulnerabilities" \
  --file src/**/*.py \
  --slug "security-audit"
```

### Use Cases

- Complex architectural decisions requiring deep analysis
- Security vulnerability analysis across large codebases
- Comprehensive code reviews before production deployment
- Understanding intricate patterns in unfamiliar code
- Expert-level domain analysis (distributed systems, concurrency)

### Session Management

Sessions stored in `~/.consultant/sessions/{session-id}/`:
- `metadata.json`: Status, timestamps, token counts
- `prompt.txt`: Original user prompt
- `output.txt`: Streaming response
- `file_*`: Copies of all attached files

---

## Development Workflow Integration

### Unified Workflow

```
Debug -> Refactor -> Optimize -> Review -> Test -> Profile
   |         |          |          |        |        |
  AI-      AI-        AI-        AI-      AI-      AI-
Powered  Powered    Powered    Powered  Powered  Powered
```

### Integration Example

```python
from moai_workflow_testing import (
    AIDebugger, AIRefactorer, PerformanceProfiler,
    TDDManager, AutomatedCodeReviewer
)

# 1. AI-Powered Debugging
debugger = AIDebugger(context7_client=context7)
analysis = await debugger.debug_with_context7_patterns(error, context, path)

# 2. Smart Refactoring
refactorer = AIRefactorer(context7_client=context7)
refactor_plan = await refactorer.refactor_with_intelligence('/project/src')

# 3. Performance Optimization
profiler = PerformanceProfiler(context7_client=context7)
profiler.start_profiling(['cpu', 'memory', 'line'])
profile_results = profiler.stop_profiling()
bottlenecks = await profiler.detect_bottlenecks(profile_results)

# 4. TDD with Context7
tdd_manager = TDDManager('/project/src', context7_client=context7)
cycle_results = await tdd_manager.run_full_tdd_cycle(spec, target_function)

# 5. Automated Code Review
reviewer = AutomatedCodeReviewer(context7_client=context7)
review_report = await reviewer.review_codebase('/project/src')
print(f"Overall TRUST Score: {review_report.overall_trust_score:.2f}")
```

### CI/CD Integration

```yaml
# .github/workflows/code-review.yml
name: Code Review
on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Extract PR Comments
        run: python scripts/pr-comment-grabber.py ${{ github.repository }} ${{ github.event.pull_request.number }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - name: Run Code Review
        run: |
          moai-workflow review --project . --trust-score-min 0.8
      - uses: actions/upload-artifact@v3
        with:
          name: review-results
          path: pr-code-review-comments/
```

---

## Quality Gates and TRUST 5 Validation

### Quality Gate Configuration

```python
workflow = EnterpriseWorkflow(
    project_path="/project",
    quality_gates={
        'min_trust_score': 0.85,
        'max_critical_issues': 0,
        'required_coverage': 0.80
    }
)

results = await workflow.execute_with_validation()
if results.quality_passed:
    print("Ready for deployment")
else:
    workflow.show_quality_issues()
```

### TRUST 5 Categories

1. **Truthfulness**: Code correctness and accuracy
2. **Relevance**: Appropriate for the context
3. **Usability**: Maintainability and clarity
4. **Safety**: Security and data protection
5. **Timeliness**: Current best practices

---

## Resources Reference

### Scripts

| Script | Purpose |
|--------|---------|
| `pr-comment-grabber.py` | Extract all PR comments from GitHub |
| `pr-comment-filter.py` | Filter comments by criteria |
| `analyze-pr.sh` | Full PR analysis workflow |
| `multi_agent_review.py` | Multi-agent swarm orchestration |
| `security_scan.sh` | Security vulnerability scanning |
| `performance_check.py` | Performance bottleneck detection |
| `style_audit.py` | Style and best practices audit |
| `consultant_cli.py` | AI consultation CLI |
| `with_server.py` | Server integration utilities |

### References

| Reference | Description |
|-----------|-------------|
| `analysis-prompt.md` | LLM prompt for PR comment analysis |
| `analysis-prompt-v2.md` | Enhanced analysis with validation |
| `github-api.md` | GitHub API endpoints reference |
| `impact-analysis-methodology.md` | Risk assessment framework |
| `validation-workflow.md` | Three-phase validation process |
| `best-practices.md` | Code review best practices |
| `review-categories.md` | Severity and scope categories |
| `glob-patterns.md` | File pattern matching guide |

### Templates

| Template | Purpose |
|----------|---------|
| `review-checklist.yaml` | Code review checklist |
| `security-rules.json` | Security rule definitions |
| `performance-thresholds.json` | Performance thresholds |
| `alfred-integration.md` | Alfred workflow integration |

### Examples

| Example | Description |
|---------|-------------|
| `example-1-security-review.md` | Security review example |
| `example-2-performance-review.md` | Performance review example |
| `example-3-style-review.md` | Style review example |
| `ai-powered-testing.py` | AI-enhanced testing example |
| `console_logging.py` | Logging utilities |

### Modules

| Module | Description |
|--------|-------------|
| `automated-code-review.md` | TRUST 5 validation implementation |
| `ai-debugging.md` | AI-powered debugging with Context7 |
| `smart-refactoring.md` | Technical debt analysis |
| `performance-optimization.md` | Performance profiling |
| `tdd-context7.md` | TDD with Context7 patterns |

---

## Integration Examples

### Security Audit

```bash
uvx --from {SCRIPTS_PATH} consultant-cli \
  --prompt "Identify SQL injection vulnerabilities. For each: location, attack vector, fix." \
  --file "apps/*/src/**/*.{service,controller}.ts" \
  --slug "security-audit" \
  --model "claude-opus-4-5"
```

### PR Review

```bash
# Extract comments
python scripts/pr-comment-grabber.py owner/repo 42

# Generate diff
git diff origin/main...HEAD > /tmp/pr-diff.txt

# Consult AI for deep review
uvx --from {SCRIPTS_PATH} consultant-cli \
  --prompt "Review this PR for production deployment. Flag blockers and suggest regression tests." \
  --file /tmp/pr-diff.txt \
  --slug "pr-review"
```

### Automated Workflow

```bash
# Run complete code review workflow
moai-workflow execute --project /project/src --mode full

# Or individual components
moai-workflow review --project /project/src --trust-score-min 0.8
moai-workflow test --spec auth.spec --mode tdd
moai-workflow profile --target function_name --types cpu,memory
```

---

## Success Criteria

This skill succeeds when:
- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms
- **Fix Verification**: Proposed fixes validated against codebase constraints

---

## Changelog

### v2.0.0 (Merged Skill)
- Combined 4 complementary skills into unified code review skill
- Integrated: Kanitsal Kod Incelemesi, PR Comment Analysis, Development Workflow Specialist, Consultant
- 55+ resource files covering all aspects of code review
- Evidence-based framework with TRUST 5 validation
- Multi-agent swarm review with 5 specialists
- AI-powered consultation for complex analysis
- Three-phase PR comment analysis workflow
- CI/CD integration examples

### Source Skills
- **Kanitsal Kod Incelemesi v1.1.0**: Evidence-based multi-agent review
- **PR Comment Analysis v1.0**: GitHub PR comment extraction and analysis
- **Development Workflow Specialist v1.0.0**: TDD, debugging, optimization workflows
- **Consultant v1.0**: LiteLLM-based AI consultation

