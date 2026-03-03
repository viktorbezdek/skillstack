# Workflow Automation

> Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution, release automation, and git workflow management.

## Overview

Modern software development involves dozens of interconnected workflows: build pipelines, test automation, release management, branch coordination, code review, and deployment orchestration. Managing these manually is slow, error-prone, and does not scale. This skill provides a comprehensive automation toolkit covering CI/CD pipelines (GitHub Actions, GitLab CI), git worktree management with GitFlow, scientific workflow orchestration (joblib, Prefect, Parsl), multi-agent coordination, TDD-integrated development workflows, FABER state management, and semantic release automation.

The skill is designed for teams and individual developers who want to reduce manual toil, enforce quality gates automatically, and ship with confidence. It includes ready-to-use pipeline templates, shell scripts for git worktree operations, Python-based workflow engines, and detailed reference documentation for every automation pattern.

As part of the SkillStack collection, this skill connects with test-driven-development and testing-framework for test automation, code-review for automated review workflows, and git-workflow for branch management conventions.

## What's Included

### References

**CI/CD**
- `references/cicd/best_practices.md` - Pipeline design patterns: fail-fast, parallelize, cache
- `references/cicd/security.md` - Secrets management, OIDC authentication, credential rotation
- `references/cicd/devsecops.md` - Security scanning guide (SAST, DAST, SCA)
- `references/cicd/optimization.md` - Pipeline performance optimization techniques
- `references/cicd/troubleshooting.md` - Common pipeline failures and fixes

**Git Workflow**
- `references/gitflow-conventions.md` - Complete GitFlow reference with branch naming and merge strategies

**Multi-Agent Orchestration**
- `references/alfred-workflow-reference.md` - Alfred workflow orchestration patterns and coordination strategies

**Playwright Automation**
- `references/playwright-best-practices.md` - Playwright automation best practices
- `references/playwright-advanced-patterns.md` - Advanced Playwright patterns for complex scenarios
- `references/playwright-optimization.md` - Playwright performance optimization

**Semantic Release**
- `references/semantic-release/local-release-workflow.md` - Local-first release workflow guide
- `references/semantic-release/authentication.md` - SSH and gh CLI authentication setup
- `references/semantic-release/troubleshooting.md` - Release troubleshooting guide
- `references/semantic-release/workflow-patterns.md` - Release workflow patterns
- `references/semantic-release/monorepo-support.md` - Monorepo release configuration
- `references/semantic-release/version-alignment.md` - Version alignment across packages
- `references/semantic-release/python-projects-nodejs-semantic-release.md` - Using semantic-release for Python projects
- `references/semantic-release/pypi-publishing-with-doppler.md` - PyPI publishing with Doppler secrets
- `references/semantic-release/adr-release-linking.md` - ADR release linking patterns
- `references/semantic-release/2025-updates.md` - Latest semantic-release updates
- `references/semantic-release/resources.md` - External resources and documentation links

### Modules

- `modules/tdd-context7.md` - TDDManager class for test-driven development cycles with Context7 integration
- `modules/ai-debugging.md` - AIDebugger class for intelligent error analysis and root cause identification
- `modules/automated-code-review.md` - AutomatedCodeReviewer with TRUST 5 framework validation
- `modules/smart-refactoring.md` - Technical debt analysis and refactoring recommendations
- `modules/performance-optimization.md` - Profiling, bottleneck detection, and optimization strategies

### Subskills

- `subskills/joblib.md` - Simple function caching and parallel execution for Python
- `subskills/prefect.md` - Modern Python workflow orchestration with DAG support
- `subskills/parsl.md` - HPC-aware scientific computing with implicit parallelism
- `subskills/covalent.md` - Cloud-agnostic and quantum workflow orchestration
- `subskills/fireworks.md` - Battle-tested materials science production workflows
- `subskills/quacc.md` - High-throughput materials DFT workflow recipes

### Templates

**GitHub Actions**
- `templates/github-actions/node-ci.yml` - Node.js CI pipeline with testing and linting
- `templates/github-actions/python-ci.yml` - Python CI pipeline with pytest and coverage
- `templates/github-actions/go-ci.yml` - Go CI pipeline with testing and vet
- `templates/github-actions/docker-build.yml` - Docker build and push pipeline
- `templates/github-actions/security-scan.yml` - Security scanning pipeline (SAST, SCA)

**GitLab CI**
- `templates/gitlab-ci/node-ci.yml` - Node.js CI pipeline for GitLab
- `templates/gitlab-ci/python-ci.yml` - Python CI pipeline for GitLab
- `templates/gitlab-ci/go-ci.yml` - Go CI pipeline for GitLab
- `templates/gitlab-ci/docker-build.yml` - Docker build pipeline for GitLab
- `templates/gitlab-ci/security-scan.yml` - Security scanning pipeline for GitLab

**Other Templates**
- `templates/status-card.template.md` - FABER workflow status card template
- `templates/faber-status-card.template.md` - Detailed FABER status card with phase tracking
- `templates/alfred-integration.md` - Alfred multi-agent integration template

### Scripts

**Git Worktree Management**
- `scripts/git/create_worktree.sh` - Create worktree with GitFlow branch conventions
- `scripts/git/list_worktrees.sh` - List all worktrees with status information
- `scripts/git/cleanup_worktrees.sh` - Clean up stale or merged worktrees

**FABER Workflow (29 scripts)**
- `scripts/faber/config-init.sh` - Initialize FABER configuration
- `scripts/faber/config-loader.sh` - Load FABER configuration
- `scripts/faber/config-validate.sh` - Validate FABER configuration
- `scripts/faber/state-init.sh` - Initialize workflow state
- `scripts/faber/state-read.sh` - Read current workflow state
- `scripts/faber/state-write.sh` - Write workflow state
- `scripts/faber/state-update-phase.sh` - Update phase status
- `scripts/faber/state-validate.sh` - Validate state consistency
- `scripts/faber/state-backup.sh` - Backup current state
- `scripts/faber/state-cancel.sh` - Cancel workflow gracefully
- `scripts/faber/status-card-post.sh` - Post status card to PR/issue
- `scripts/faber/phase-validate.sh` - Validate phase transitions
- `scripts/faber/step-validate.sh` - Validate step completion
- `scripts/faber/validate-step-ids.sh` - Validate step ID uniqueness
- `scripts/faber/workflow-validate.sh` - Validate complete workflow
- `scripts/faber/workflow-audit.sh` - Audit workflow history
- `scripts/faber/workflow-recommend.sh` - Recommend workflow improvements
- `scripts/faber/hook-execute.sh` - Execute workflow hooks
- `scripts/faber/hook-list.sh` - List registered hooks
- `scripts/faber/hook-test.sh` - Test hook execution
- `scripts/faber/hook-validate.sh` - Validate hook definitions
- `scripts/faber/lock-acquire.sh` - Acquire workflow lock
- `scripts/faber/lock-check.sh` - Check lock status
- `scripts/faber/lock-release.sh` - Release workflow lock
- `scripts/faber/template-apply.sh` - Apply workflow templates
- `scripts/faber/pattern-substitute.sh` - Substitute patterns in templates
- `scripts/faber/error-recovery.sh` - Recover from workflow errors
- `scripts/faber/error-report.sh` - Generate error reports
- `scripts/faber/diagnostics.sh` - Run workflow diagnostics

**CI/CD Analysis**
- `scripts/cicd/pipeline_analyzer.py` - Analyze pipeline performance and bottlenecks
- `scripts/cicd/ci_health.py` - Check CI health metrics

**Release**
- `scripts/release/init_project.sh` - Initialize semantic-release for a project
- `scripts/release/init_user_config.sh` - Initialize user-level release configuration
- `scripts/release/create_org_config.sh` - Create organization-level release config
- `scripts/release/generate-adr-notes.mjs` - Generate ADR release notes

**Workflow Utilities**
- `scripts/workflow/spec_status_hooks.py` - Specification status tracking hooks
- `scripts/workflow/with_server.py` - Run workflows with a live server process

### Examples

- `examples/enterprise-testing-workflow.py` - Complete multi-agent enterprise testing workflow
- `examples/ai-powered-testing.py` - AI-powered test generation and execution
- `examples/console_logging.py` - Console logging patterns for workflow debugging
- `examples/element_discovery.py` - UI element discovery for E2E automation
- `examples/static_html_automation.py` - Static HTML page automation example

### Docs

- `docs/quick-reference.md` - Quick reference card for all workflow commands
- `docs/alfred-workflow-examples.md` - Alfred multi-agent workflow examples
- `docs/configuration.md` - Configuration guide for all workflow tools
- `docs/development-workflow-examples.md` - Development workflow pattern examples
- `docs/development-workflow-reference.md` - Complete development workflow reference
- `docs/scientific-workflows-quick-reference.md` - Scientific workflow tool comparison
- `docs/status-cards.md` - Status card usage and formatting guide

## Key Features

- **CI/CD pipeline templates** for GitHub Actions and GitLab CI covering Node.js, Python, Go, Docker, and security scanning
- **Git worktree management** with GitFlow conventions for parallel feature development
- **Scientific workflow orchestration** with guides for joblib, Prefect, Parsl, Covalent, FireWorks, and quacc
- **Multi-agent coordination** using the Alfred WorkflowEngine pattern for complex task orchestration
- **FABER state management** with 29 shell scripts for Frame-Architect-Build-Evaluate-Release workflow phases
- **Semantic release automation** with local-first releases, conventional commits, and multi-account support
- **DevSecOps integration** with SAST, DAST, and SCA security scanning in pipelines
- **Development workflow modules** for TDD, AI debugging, automated code review, and performance optimization

## Usage Examples

### Set up a CI/CD pipeline for a Node.js project

```
Set up a GitHub Actions CI/CD pipeline for my Node.js TypeScript project with linting, testing, Docker build, and deployment to staging/production.
```

Produces a multi-stage pipeline using templates from `templates/github-actions/` with caching, parallel test execution, and environment-based deployment gates.

### Manage parallel feature development with worktrees

```
I need to work on three features in parallel: email notifications, user dashboard, and API rate limiting. Set up git worktrees for each.
```

Creates three worktrees using GitFlow conventions, each with an isolated branch and working directory, plus commands for listing and cleaning up when done.

### Automate releases with semantic versioning

```
Set up semantic-release for my Python library so that conventional commits automatically bump versions and publish to PyPI.
```

Configures semantic-release with conventional commits, generates the .releaserc file, sets up authentication, and provides the local dry-run and release commands.

### Orchestrate a multi-agent development workflow

```
Design a multi-agent workflow for implementing a new feature: one agent writes specs, another implements with TDD, and a third runs code review.
```

Produces a WorkflowEngine configuration with three coordinated agents, dependency ordering, error recovery patterns, and quality gate thresholds.

### Analyze and optimize a slow CI pipeline

```
My GitHub Actions pipeline takes 25 minutes. Analyze it and suggest optimizations to get it under 10 minutes.
```

Runs pipeline analysis, identifies bottlenecks (missing caching, serial jobs that could parallelize, redundant steps), and provides specific optimization recommendations with expected time savings.

## Quick Start

1. **Identify your workflow need** - Use the Quick Decision Guide in SKILL.md to find the right section: CI/CD, git workflows, scientific computing, multi-agent, development, or releases.
2. **Copy a template** - Grab the relevant template from `templates/` for your CI platform (GitHub Actions or GitLab CI) or workflow type.
3. **Configure** - Adapt the template to your project using guidance from `references/` and `docs/configuration.md`.
4. **Add scripts** - Copy the relevant scripts from `scripts/` into your project (git worktree helpers, FABER scripts, or release tools).
5. **Test locally** - Use dry-run modes (e.g., `npx semantic-release --no-ci --dry-run`) and local script execution before pushing to CI.
6. **Monitor** - Use `scripts/cicd/ci_health.py` and `scripts/cicd/pipeline_analyzer.py` to track pipeline health over time.

## Related Skills

- [test-driven-development](../test-driven-development/) - TDD methodology integrated with the development workflow modules
- [testing-framework](../testing-framework/) - Multi-language test infrastructure for CI/CD pipeline integration
- [code-review](../code-review/) - Automated code review that complements the TRUST 5 framework
- [git-workflow](../git-workflow/) - Git workflow conventions and branch management strategies
- [cicd-pipelines](../cicd-pipelines/) - Focused CI/CD pipeline design patterns
- [docker-containerization](../docker-containerization/) - Docker patterns for build and deployment pipelines

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `/plugin install workflow-automation@skillstack` — 46 production-grade plugins for Claude Code.
