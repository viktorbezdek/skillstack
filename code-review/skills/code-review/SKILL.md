---
name: code-review
description: Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and documentation. Analyze PRs, extract and prioritize comments, and generate actionable fix plans.
triggers:
  - code review
  - PR review
  - pull request
  - review code
  - security audit
  - code quality
  - review changes
  - code feedback
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

# Comprehensive Code Review Skill

This skill is a curated merge of four complementary code review skills:

1. **Evidence-Based Code Review**: Evidence-based multi-agent swarm review with specialized reviewers
2. **PR Comment Analysis**: Extract, consolidate, and prioritize GitHub PR comments
3. **Development Workflow Specialist**: TDD, debugging, performance optimization, and automated code review
4. **Consultant**: AI-powered deep analysis for complex architectural and security reviews

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

**Do NOT use for:**
- Simple formatting fixes (use linter/prettier directly)
- Non-code files (documentation, configuration without logic)
- Trivial changes (typo fixes, comment updates)
- Generated code (build artifacts, vendor dependencies)

---

## Core Capabilities

### 1. Evidence-Based Code Review
Every finding MUST include:
- Code location: `[file:line]` with surrounding context (5 lines before/after)
- Evidence type: DIRECT, STYLE_RULE, or BEST_PRACTICE
- Severity: CRITICAL, MAJOR, MINOR, or NIT
- Confidence score: 0.0-1.0
- Suggested fix with specific code changes

### 2. PR Comment Analysis
- Fetches ALL comments from GitHub PR (inline + conversation)
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
- Async operation with session management

### 5. TRUST 5 Validation Framework
- **Truthfulness**: Code does what it claims
- **Relevance**: Changes are appropriate for the context
- **Usability**: Code is maintainable and understandable
- **Safety**: No security vulnerabilities or data risks
- **Timeliness**: Follows current best practices

---

## Severity Levels

- **CRITICAL**: Architecture-level issues (security vulnerabilities, data loss risks)
- **MAJOR**: Module-level issues (performance bottlenecks, maintainability problems)
- **MINOR**: Function-level improvements (code style, readability)
- **NIT**: Line-level suggestions (formatting, naming)

## Validation Rules

- NEVER approve code without evidence
- ALWAYS provide line numbers with every finding
- VALIDATE findings against multiple perspectives
- DISTINGUISH symptoms from root causes
- AVOID false confidence: flag uncertain findings as "needs manual review"
- Findings require 2+ confirming signals before flagging as violations

See [Extended Patterns](references/extended-patterns.md) for detailed finding templates, PR comment workflow, multi-agent swarm execution, CI/CD integration, and quality gate configuration.

---

## Success Criteria

- **Violations Detected**: All quality issues found with ZERO false negatives
- **False Positive Rate**: <5% (95%+ findings are genuine issues)
- **Actionable Feedback**: Every finding includes file path, line number, and fix guidance
- **Root Cause Identified**: Issues traced to underlying causes, not just symptoms

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

### References

| Reference | Description |
|-----------|-------------|
| `extended-patterns.md` | Detailed examples and workflow patterns |
| `analysis-prompt.md` | LLM prompt for PR comment analysis |
| `analysis-prompt-v2.md` | Enhanced analysis with validation |
| `github-api.md` | GitHub API endpoints reference |
| `impact-analysis-methodology.md` | Risk assessment framework |
| `validation-workflow.md` | Three-phase validation process |
| `best-practices.md` | Code review best practices |
| `review-categories.md` | Severity and scope categories |

### Templates

| Template | Purpose |
|----------|---------|
| `review-checklist.yaml` | Code review checklist |
| `security-rules.json` | Security rule definitions |
| `performance-thresholds.json` | Performance thresholds |
