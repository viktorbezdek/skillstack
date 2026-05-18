---
name: code-review
description: Comprehensive code review skill combining TDD validation, debugging analysis, performance optimization, and quality assurance into unified review workflows. Use when the user asks to review code, conduct a code review, analyze code quality, perform a PR review, or validate implementation quality. NOT for CI/CD pipeline configuration (use cicd-pipelines), NOT for debugging specific bugs (use debugging).
---

# Code Review Skill

Systematic code review combining quality validation, debugging analysis, performance review, and test coverage assessment.

## When to Activate

- Reviewing pull requests or code changes
- Conducting automated or manual code reviews
- Analyzing code quality and technical debt
- Validating test coverage and TDD compliance
- Assessing performance implications of changes
- Reviewing security and error handling

## Decision Tree: Review Type

```
What are you reviewing?
+-- Pull request with specific changes --> Focused review (changed files only)
+-- Entire codebase quality --> Comprehensive review (full codebase scan)
+-- Security vulnerability --> Security-focused review (SAST patterns, injection, auth)
+-- Performance regression --> Performance review (hot paths, N+1, memory)
+-- Test coverage gaps --> Test review (coverage, TDD compliance, edge cases)
```

## Review Framework

### Priority Levels

| Level | Category | Examples |
|-------|----------|----------|
| P0 - Block | Correctness | Logic errors, data corruption, security vulnerabilities |
| P1 - Must Fix | Reliability | Unhandled errors, race conditions, resource leaks |
| P2 - Should Fix | Maintainability | Code duplication, poor naming, missing tests |
| P3 - Nice to Have | Style | Formatting, comment clarity, minor refactoring |

### Review Checklist

```
[ ] Logic correctness - does the code do what it claims?
[ ] Error handling - are failure modes covered?
[ ] Security - injection, auth, data exposure?
[ ] Performance - N+1 queries, unnecessary allocations, hot path impact?
[ ] Test coverage - are new paths tested? Edge cases covered?
[ ] Naming clarity - can a new team member understand intent?
[ ] DRY principle - is there duplicated logic that should be extracted?
[ ] API compatibility - are breaking changes documented and versioned?
[ ] Resource management - connections, file handles, memory properly managed?
[ ] Documentation - are public APIs and complex logic documented?
```

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Rubber-stamp reviews | "LGTM" without reading the code | Require specific observations; use structured checklist |
| Nitpicking style over substance | Debating naming while missing a race condition | Prioritize P0/P1 before P3 |
| Reviewing without context | Commenting on code without understanding the requirements | Read the issue/PR description and linked specs first |
| Scope creep in reviews | Requesting unrelated refactoring | Scope review to the PR's stated purpose; create follow-up issues |
| Ignoring test coverage | Approving code with untested new logic | Require tests for new conditional paths |
| Missing security review | Focusing only on logic and style | Check for injection, auth bypass, data exposure on every PR |
| Reviewing too much at once | 1000+ line PRs get superficial reviews | Request smaller PRs; batch by logical change |
| Author bias | Authors defend instead of considering feedback | Treat review as collaborative, not adversarial |

## References

- `references/best-practices.md` - Code review best practices and patterns
- `references/advanced-patterns.md` - Advanced review techniques
- `references/examples.md` - Review examples and templates
- `references/validation-workflow.md` - Validation workflow patterns
- `references/impact-analysis-methodology.md` - Impact analysis for changes
- `references/glob-patterns.md` - File matching patterns for review scope
- `references/github-api.md` - GitHub API integration for automated reviews

---

**Version:** 2.0.0
**Last Updated:** 2026-04-18
