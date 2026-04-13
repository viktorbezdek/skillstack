# Workflow Automation

> **v1.1.21** | DevOps & Infrastructure | 23 iterations

Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution, release automation, and git workflow management.

## What Problem Does This Solve

Modern software delivery involves a web of interdependent processes -- parallel feature branches, multi-agent task pipelines, versioned releases, scientific computation jobs -- that are easy to start manually but painful to scale and reproduce. Ad-hoc automation accumulates as one-off scripts that break when contributors change, releases require human memory to execute correctly, and complex workflows get blocked on a single bottleneck. Teams end up with tribal knowledge about how to release, how to coordinate parallel work, and how to recover when automated pipelines fail.

This skill provides structured patterns and tooling for all of these: from git worktree management and multi-agent coordination to semantic release automation, FABER state machine workflows, and scientific computation tool selection. It is the largest skill in SkillStack by component count -- 6 modules, 11 reference docs, 30+ FABER scripts, CI/CD templates for both GitHub Actions and GitLab CI, 6 scientific workflow subskills, and example code for enterprise testing and browser automation.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install workflow-automation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

**Direct invocation:**

```
Use the workflow-automation skill to set up semantic release for my project
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `automation`
- `ci-cd`
- `orchestration`
- `release-management`

## What's Inside

This is a **single-skill plugin** with an unusually large supporting structure: modules, references, scripts, subskills, templates, examples, and docs.

### Core Capabilities

| Capability | Key resources | What it covers |
|---|---|---|
| CI/CD Pipelines | `references/cicd/`, `templates/github-actions/`, `templates/gitlab-ci/` | Pipeline design patterns, DevSecOps scanning (SAST, DAST, SCA), deployment strategies (blue-green, canary, rolling), troubleshooting |
| Git Worktree Management | `scripts/git/` | Worktree creation/listing/cleanup following GitFlow conventions (feature/, fix/, hotfix/) |
| Scientific Workflows | `subskills/` (joblib, Prefect, Parsl, Covalent, FireWorks, quacc) | Tool selection from simple joblib caching to HPC cluster orchestration with Parsl to complex DAGs with Prefect |
| Multi-Agent Orchestration | `references/alfred-workflow-reference.md` | WorkflowEngine patterns for coordinating multiple agents with stage dependencies, error recovery, and performance monitoring |
| TDD/Debug/Review | `modules/` (tdd-context7, ai-debugging, automated-code-review, smart-refactoring, performance-optimization) | TDDManager, AIDebugger, and AutomatedCodeReviewer with TRUST 5 framework (Test-first, Readable, Unified, Secured, Trackable) |
| Semantic Release | `references/semantic-release/`, `scripts/release/` | Local-first release workflow, conventional commits, version bump rules, monorepo support, PyPI publishing, troubleshooting |
| FABER State Management | `scripts/faber/` | 30+ shell scripts for state machine workflows: init, read, write, validate, lock, hook, phase, and audit operations |

### Component Inventory

| Type | Count | Examples |
|---|---|---|
| Modules | 6 | TDD, AI debugging, code review, refactoring, performance optimization |
| Reference docs | 11+ | CI/CD best practices, GitFlow conventions, semantic release guides, Playwright patterns |
| Scripts | 40+ | FABER state machine (30), git worktrees (3), release automation (4), workflow utilities (3) |
| Subskills | 6 | joblib, Prefect, Parsl, Covalent, FireWorks, quacc |
| CI/CD templates | 10 | GitHub Actions + GitLab CI for Node, Python, Go, Docker, security scanning |
| Examples | 5 | AI-powered testing, enterprise testing workflow, browser automation, console logging |

## Usage Scenarios

**1. "Automate my versioning and changelog so releases don't require manual steps"**
The semantic release section provides a local-first release workflow using conventional commits (feat/fix/BREAKING CHANGE) with automatic version bumps and changelog generation. Includes setup scripts (`scripts/release/init_project.sh`), multi-account authentication, and monorepo support patterns.

**2. "I need to run multiple agents in parallel with dependencies between stages"**
The multi-agent orchestration section provides WorkflowEngine patterns where you define agents by domain (spec-builder, tdd-implementer, quality-gate), wire them into stages with `depends_on` declarations, and let the engine handle execution order, error recovery, and performance monitoring.

**3. "We're doing parallel feature development and branches keep colliding"**
The git worktree scripts create isolated worktrees following GitFlow conventions. `create_worktree.sh feature email-notifications` creates a dedicated branch and working directory, `list_worktrees.sh` shows all active worktrees with status, and `cleanup_worktrees.sh --merged` removes stale ones.

**4. "My Python computation jobs need caching and parallel execution"**
The scientific workflow decision tree routes you to the right tool: joblib for simple function caching and 10-100 parallel tasks on a laptop, Parsl for 100+ tasks on HPC clusters, Prefect for complex DAGs with retries and a UI, Covalent for cloud-agnostic deployment, and quacc/FireWorks for materials science workflows.

**5. "Set up automated code review that enforces our quality standards"**
The TRUST 5 framework (Test-first, Readable, Unified, Secured, Trackable) is implemented via the AutomatedCodeReviewer module with configurable thresholds. Quality metrics target >=85% test coverage, >=0.85 TRUST score, zero critical issues, and API response times under specified limits.

## When to Use / When NOT to Use

**Use when:**
- Setting up or optimizing development workflow automation (releases, worktrees, task orchestration)
- Coordinating multi-agent workflows with stage dependencies
- Choosing between scientific computation tools (joblib vs Prefect vs Parsl)
- Implementing automated code review with quality gates
- Automating semantic versioning and changelog generation

**Do NOT use when:**
- Writing CI/CD pipeline YAML configuration -- use [cicd-pipelines](../cicd-pipelines/) instead
- Managing Docker containers or writing Dockerfiles -- use [docker-containerization](../docker-containerization/) instead
- Git branching strategy, commit quality, or conventional commits -- use [git-workflow](../git-workflow/) instead

## Related Plugins in SkillStack

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline YAML configuration that this skill's templates generate
- **[Git Workflow](../git-workflow/)** -- Conventional commits and branch management that feed into this skill's release automation
- **[Docker Containerization](../docker-containerization/)** -- Container builds that are the deployment target for workflows designed here
- **[Cloud FinOps](../cloud-finops/)** -- Cost monitoring for the infrastructure these workflows run on

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
