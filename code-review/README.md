# Code Review

> Perform thorough code reviews with multi-agent swarm analysis covering security, performance, style, tests, and documentation -- with evidence-based findings and actionable fix plans.

## Overview

Code review is a critical quality gate, but manual reviews are inconsistent, time-consuming, and prone to blind spots. Reviewers miss security vulnerabilities because they focus on style, or miss performance issues because they focus on correctness. This skill solves that problem with a systematic, multi-dimensional review approach that covers every angle -- security, performance, style, test coverage, and documentation -- with evidence-based findings tied to specific file locations.

The Code Review skill combines four complementary review methodologies: evidence-based multi-agent swarm review with five specialized reviewer agents, GitHub PR comment extraction and consolidation, a TRUST 5 validation framework (Truthfulness, Relevance, Usability, Safety, Timeliness), and AI-powered deep analysis for complex architectural decisions. Every finding includes file and line references, severity classification, confidence scores, and concrete fix suggestions.

Within the SkillStack collection, this skill integrates with CI/CD Pipelines (for automated review gates), API Design (for API-specific review criteria), and Critical Intuition (for detecting subtle architectural issues that automated tools miss).

## What's Included

### References
- `extended-patterns.md` -- Detailed finding templates, PR comment workflows, multi-agent execution, and quality gate configuration
- `analysis-prompt.md` -- LLM prompt template for PR comment analysis
- `analysis-prompt-v2.md` -- Enhanced analysis prompt with validation layers
- `github-api.md` -- GitHub API endpoints for PR comment fetching
- `impact-analysis-methodology.md` -- Risk assessment framework for prioritizing findings
- `validation-workflow.md` -- Three-phase validation process: consolidation, context validation, impact analysis
- `best-practices.md` -- Code review best practices and reviewer guidelines
- `review-categories.md` -- Severity and scope category definitions
- `advanced-patterns.md` -- Advanced review patterns and techniques
- `examples.md` -- Review example catalog
- `example-analysis.md` -- Detailed analysis walkthrough
- `glob-patterns.md` -- File pattern matching for targeted reviews
- `optimization.md` -- Review process optimization techniques
- `reference.md` -- General reference documentation
- `index.md` -- Reference documentation index
- `SKILL.md` -- Extended skill documentation
- `USAGE-GUIDE.md` -- Usage guide for the review system
- `COMPLETION-SUMMARY.md` -- Review completion summary template
- `README.md` -- Reference directory overview

### Templates
- `review-checklist.yaml` -- Comprehensive code review checklist covering all dimensions
- `security-rules.json` -- Security rule definitions for automated detection
- `performance-thresholds.json` -- Performance threshold configuration for bottleneck detection
- `alfred-integration.md` -- Integration guide for Alfred workflow automation

### Scripts
- `pr-comment-grabber.py` -- Extract all comments from a GitHub PR (inline and conversation)
- `pr-comment-filter.py` / `pr_comment_filter.py` -- Filter PR comments by criteria (severity, author, file)
- `analyze-pr.sh` -- Full PR analysis workflow orchestration
- `multi_agent_review.py` -- Multi-agent swarm review orchestrator
- `security_scan.sh` -- Security vulnerability scanning script
- `performance_check.py` -- Performance bottleneck detection
- `style_audit.py` -- Style and best practices audit
- `consultant_cli.py` -- AI-powered consultation CLI for deep analysis
- `review-loop.sh` -- Iterative review loop automation
- `show-with-status.py` -- Display review findings with status indicators
- `diagnose-qodo.py` -- Qodo integration diagnostics
- `config.py` -- Review system configuration
- `file_handler.py` -- File reading and processing utilities
- `litellm_client.py` -- LiteLLM client for multi-provider AI integration
- `model_selector.py` -- AI model selection logic
- `response_strategy.py` -- Response formatting strategy
- `session_manager.py` -- Review session state management
- `with_server.py` -- Server integration utilities

### Examples
- `example-1-security-review.md` -- Security-focused review walkthrough
- `example-2-performance-review.md` -- Performance-focused review walkthrough
- `example-3-style-review.md` -- Style and maintainability review walkthrough
- `ai-powered-testing.py` -- AI-powered test generation example
- `console_logging.py` -- Console logging pattern example
- `element_discovery.py` -- Element discovery automation example
- `static_html_automation.py` -- Static HTML automation example

### Modules
- `ai-debugging.md` -- AI-powered debugging with error classification and solution generation
- `automated-code-review.md` -- Automated review pipeline configuration
- `performance-optimization.md` -- Performance optimization patterns and techniques
- `smart-refactoring.md` -- Technical debt analysis and smart refactoring
- `tdd-context7.md` -- TDD workflow with Context7 integration

## Key Features

- **Multi-agent swarm review**: Five specialized agents (security, performance, style, tests, docs) analyze code in parallel
- **Evidence-based findings**: Every finding includes file:line references, evidence type, and confidence scores
- **Severity classification**: CRITICAL, MAJOR, MINOR, and NIT levels with clear escalation criteria
- **PR comment consolidation**: Extract, group, and prioritize feedback from multiple reviewers
- **TRUST 5 framework**: Validates Truthfulness, Relevance, Usability, Safety, and Timeliness
- **AI-powered deep analysis**: Supports 100+ LLM providers through LiteLLM for complex architectural reviews
- **Actionable fix plans**: Every finding includes concrete code changes, not just descriptions
- **Low false positive rate**: Findings require 2+ confirming signals; target is less than 5% false positives

## Usage Examples

**Perform a comprehensive code review:**
```
Review the changes in this PR for security vulnerabilities,
performance issues, and code quality problems.
```
Expected output: Categorized findings organized by severity (CRITICAL through NIT), each with file:line references, evidence type, confidence score, and a suggested fix with code diff.

**Extract and consolidate PR feedback:**
```
Analyze all comments on PR #142 and create a prioritized action plan.
```
Expected output: Grouped comments by file, high-consensus issues flagged, prioritized action items sorted by impact, and a clear implementation plan.

**Security-focused review:**
```
Audit this authentication module for security vulnerabilities,
focusing on injection attacks, auth bypasses, and data exposure.
```
Expected output: Security findings with CVE references where applicable, OWASP category mapping, specific vulnerable code locations, and remediation code.

**Performance review:**
```
Analyze this database query layer for performance bottlenecks
and N+1 query patterns.
```
Expected output: Identified bottlenecks with query execution analysis, N+1 pattern detection, index recommendations, and optimized query implementations.

**Review against a checklist:**
```
Review this API endpoint implementation against our code review
checklist for production readiness.
```
Expected output: Checklist-driven assessment with pass/fail for each criterion, specific findings for failures, and recommendations for improvement.

## Quick Start

1. **Start a review** -- Point the skill at a PR or set of changed files
2. **Choose review scope** -- Full multi-agent review, or focused on security/performance/style
3. **Examine findings** -- Review categorized findings sorted by severity
4. **Validate high-severity items** -- Cross-reference CRITICAL and MAJOR findings manually
5. **Generate action plan** -- Prioritize fixes based on impact and effort
6. **Iterate** -- Re-run after fixes to verify resolution

## Related Skills

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Integrate code review as an automated quality gate in your pipeline
- **[API Design](../api-design/)** -- Apply API-specific review criteria to endpoint implementations
- **[Critical Intuition](../critical-intuition/)** -- Detect subtle architectural issues and hidden patterns
- **[Consistency Standards](../consistency-standards/)** -- Enforce naming and style consistency during reviews

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install code-review@skillstack` — 46 production-grade plugins for Claude Code.
