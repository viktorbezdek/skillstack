---
name: workflow-automation
description: Workflow orchestration and release automation — use when the user asks to automate workflows, orchestrate multi-agent tasks, run parallel task execution, manage release automation, build state machines, or coordinate complex task dependencies. NOT for CI/CD pipeline configuration or YAML (use cicd-pipelines), NOT for Docker containers or Dockerfiles (use docker-containerization), NOT for git branching or commits (use git-workflow).
---

# Workflow Automation Skill

Comprehensive guide for workflow automation, task management, and productivity optimization in software development. This skill combines CI/CD pipelines, git workflow management, scientific workflow tools, multi-agent orchestration, TDD workflows, and release automation.

## When to Use This Skill

- **CI/CD Pipelines**: Creating, optimizing, or troubleshooting CI/CD workflows
- **Git Workflows**: Managing parallel development with worktrees and GitFlow
- **Scientific Workflows**: Choosing tools for computational workflows (joblib, Prefect, Parsl)
- **Multi-Agent Orchestration**: Coordinating multiple agents for complex tasks
- **TDD/Development Cycles**: Following RED-GREEN-REFACTOR with quality gates
- **Code Review Automation**: Implementing TRUST 5 framework validation
- **Release Automation**: Setting up semantic versioning and automated releases
- **Task Management**: Orchestrating complex dependencies and parallel execution

## When NOT to Use This Skill

- **CI/CD YAML configuration** → use `cicd-pipelines`
- **Docker containers or Dockerfiles** → use `docker-containerization`
- **Git branching strategy or commit conventions** → use `git-workflow`

---

## Decision Tree

```
START: What type of workflow?

├── Build/Test/Deploy Pipeline
│   └── Use: CI/CD Pipelines → references/cicd/
│       ├── GitHub Actions → templates/github-actions/
│       └── GitLab CI → templates/gitlab-ci/

├── Parallel Feature Development
│   └── Use: Git Workflow Manager → scripts/git/
│       • create_worktree.sh
│       • GitFlow conventions

├── Scientific Computations
│   ├── Simple caching? → joblib (subskills/joblib.md)
│   ├── HPC cluster? → Parsl (subskills/parsl.md)
│   ├── Complex DAG? → Prefect (subskills/prefect.md)
│   └── Materials science? → quacc/FireWorks

├── Multi-Agent Coordination
│   └── Use: Alfred Workflow Orchestration
│       • WorkflowEngine patterns
│       • Context7 integration
│       • Error recovery

├── Development Workflow (TDD/Debug/Review)
│   └── Use: Development Workflow Specialist
│       • TDDManager → modules/tdd-context7.md
│       • AIDebugger → modules/ai-debugging.md
│       • AutomatedCodeReviewer → modules/automated-code-review.md

└── Automated Releases
    └── Use: Semantic Release → references/semantic-release/
        • Local-first releases
        • Conventional commits
```

---

## Core Capabilities

### 1. CI/CD Pipelines

Design, optimize, and troubleshoot CI/CD pipelines across GitHub Actions and GitLab CI.

**Key Features:** Pipeline design patterns (fail-fast, parallelize, cache), DevSecOps security scanning (SAST, DAST, SCA), deployment strategies (blue-green, canary, rolling), performance optimization.

**Pipeline structure:** Fast feedback (<1 min) → Unit tests (1-5 min) → Integration tests (5-15 min) → Build artifacts → Deploy (with approval gates).

**Resources:** `references/cicd/best_practices.md`, `references/cicd/security.md`, `references/cicd/devsecops.md`, `templates/github-actions/`, `templates/gitlab-ci/`

### 2. Git Workflow Management

Manage git worktrees following GitFlow conventions for parallel development.

**Quick Start:**
- `./scripts/git/create_worktree.sh feature email-notifications` → branch `feature/email-notifications`, worktree `../project-worktrees/feature/email-notifications/`
- `./scripts/git/list_worktrees.sh` → visibility into all active worktrees
- `./scripts/git/cleanup_worktrees.sh --merged` → clean up stale branches

**Resources:** `scripts/git/`, `references/gitflow-conventions.md`

### 3. Scientific Workflow Management

Choose the right tool for computational workflows.

| Situation | Tool | Why |
|-----------|------|-----|
| Cache function calls | joblib.Memory | Dead simple caching |
| 10-100 tasks on laptop | joblib.Parallel | Built-in, no setup |
| 100+ tasks on HPC | Parsl | HPC-aware, implicit parallelism |
| Complex DAG with retries | Prefect | Modern, Pythonic, great UI |
| Cloud-agnostic deployment | Covalent | Infrastructure abstraction |
| Materials DFT workflows | quacc | Pre-built recipes |
| Production materials | FireWorks | Battle-tested |

**Resources:** `subskills/joblib.md`, `subskills/prefect.md`, `subskills/parsl.md`, `subskills/covalent.md`, `subskills/fireworks.md`, `subskills/quacc.md`

### 4. Multi-Agent Workflow Orchestration

Coordinate multiple agents with WorkflowEngine: `engine.create_workflow()` → `workflow.add_stage(agent, depends_on=[...])` → `engine.execute(workflow, input_data)`. Error handling, performance monitoring, and stage dependencies built in.

**Workflow Templates:** Feature Development (spec → implementation → testing), Bug Fix (diagnosis → fix → validation), Code Review (analysis → feedback → approval).

**Resources:** `references/alfred-workflow-reference.md`, `examples/enterprise-testing-workflow.py`

### 5. Development Workflow (TDD/Debug/Review)

- **TDDManager** (`modules/tdd-context7.md`): RED-GREEN-REFACTOR cycle with `tdd.run_full_tdd_cycle(specification, target_function)`
- **AIDebugger** (`modules/ai-debugging.md`): Root cause analysis with `debugger.debug_with_context7_patterns(exception, context, project_path)` → returns root cause, solutions, code suggestions
- **AutomatedCodeReviewer** (`modules/automated-code-review.md`): TRUST 5 validation (Test-first, Readable, Unified, Secured, Trackable) with `reviewer.review_codebase(project_path, changed_files)`

**Also:** `modules/smart-refactoring.md` (technical debt), `modules/performance-optimization.md` (profiling)

### 6. Release Automation (Semantic Release)

Automate versioning with conventional commits: `feat:` → MINOR, `fix:` → PATCH, `BREAKING CHANGE:` → MAJOR. Local-first releases for instant feedback.

**Quick Start:** `GITHUB_TOKEN=*** npx semantic-release --no-ci --dry-run` (test) then `--no-ci` (release).

**Resources:** `references/semantic-release/` (local workflow, authentication, troubleshooting, monorepo support, PyPI publishing)

### 7. FABER Workflow State Management

Stateful workflow automation: `config-loader.sh` → `state-read.sh` → `state-update-phase.sh` → `status-card-post.sh`. 29 scripts for init, read, write, validate, lock, hook, phase management, audit, and backup.

**Resources:** `scripts/faber/`, `templates/status-card.template.md`

---

## Quality Metrics

| Metric | Threshold | Description |
|--------|-----------|-------------|
| Test Coverage | >= 85% | Minimum code coverage |
| TRUST Score | >= 0.85 | 5 quality criteria combined |
| Critical Issues | 0 | No critical security/bugs |
| Performance Regression | < 10% | Max allowed degradation |
| Response Time | < 100ms | API response target |

## Anti-Patterns

| # | Anti-Pattern | Symptom | Fix |
|---|---|---|---|
| 1 | **Manual release checklist** | Human remembers steps, misses one under pressure | Semantic release with conventional commits drives automatic version bumps, changelogs, and publishing |
| 2 | **Ad-hoc multi-agent coordination** | No state persistence, no error recovery, no audit trail | Use WorkflowEngine with `depends_on` declarations, error recovery patterns, and audit logging |
| 3 | **Stale worktrees accumulating** | Disk fills up, developers forget which worktrees are active | Run `cleanup_worktrees.sh --merged` weekly via cron or CI schedule; use `list_worktrees.sh` for visibility |
| 4 | **Non-semantic commits breaking releases** | `feat:` commit with breaking behavior published under minor bump | Use `BREAKING CHANGE:` footer in commit body; enforce with commit-msg hook (see git-workflow) |
| 5 | **Wrong scientific workflow tool** | joblib on HPC cluster (slow) or Parsl for 10 tasks (overkill) | Follow the decision tree before committing. Subskills provide migration paths if already wrong |
| 6 | **FABER state file corruption** | `state-read.sh` returns invalid data after crash | `state-backup.sh` snapshots before risky operations. Restore from latest backup or `state-init.sh` to reset |
| 7 | **Infinite reviewer-implementer loop** | Reviewer keeps rejecting, implementer keeps revising, tokens wasted | Set maximum iteration count in WorkflowEngine config (typically 3). After max, escalate to human |
| 8 | **CI/CD without security scanning** | Pipeline builds and deploys but never scans for vulnerabilities | Add DevSecOps stage: SAST (code), SCA (dependencies), DAST (runtime). See `references/cicd/devsecops.md` |
| 9 | **Local-only release without CI backup** | Developer's machine is the only release path; vacation blocks releases | Local-first is the default, but add CI as a backup. See `references/semantic-release/local-release-workflow.md` |
| 10 | **TDD without coverage gate** | Tests written but coverage still below 50% | Enforce >= 85% in AutomatedCodeReviewer TRUST 5 score; fail the build below threshold |

## Best Practices

### CI/CD Pipelines
- Fail fast: Run cheap validation first
- Parallelize: Remove unnecessary job dependencies
- Cache dependencies: 50-90% faster builds
- Use OIDC: No static credentials
- Pin actions: Use commit SHAs

### Git Workflows
- One feature per worktree
- Descriptive branch names
- Commit before switching
- Push regularly for backup
- Clean up after merge

### Development Workflows
- Write tests before implementation (TDD)
- Maintain 85%+ coverage
- Use meaningful test names
- Mock external dependencies
- Profile before optimizing

### Release Automation
- Use conventional commits
- Run dry-run before release
- Verify account alignment
- Local releases for speed
- CI backup optional

## Resources Directory Structure

```
workflow-automation/
├── SKILL.md                     # This file
├── modules/
│   ├── ai-debugging.md          # AIDebugger class
│   ├── automated-code-review.md # TRUST 5 framework
│   ├── performance-optimization.md
│   ├── smart-refactoring.md
│   └── tdd-context7.md          # TDDManager class
├── references/
│   ├── cicd/
│   │   ├── best_practices.md
│   │   ├── devsecops.md
│   │   ├── optimization.md
│   │   ├── security.md
│   │   └── troubleshooting.md
│   ├── gitflow-conventions.md
│   ├── alfred-workflow-reference.md
│   └── semantic-release/
├── scripts/
│   ├── git/                     # Git worktree scripts
│   ├── faber/                   # FABER workflow framework (29 scripts)
│   ├── cicd/                    # Pipeline analysis scripts
│   └── workflow/                # Workflow utilities
├── subskills/
│   ├── joblib.md
│   ├── prefect.md
│   ├── parsl.md
│   ├── covalent.md
│   ├── fireworks.md
│   └── quacc.md
├── templates/
│   ├── github-actions/
│   └── gitlab-ci/
├── examples/
│   └── enterprise-testing-workflow.py
└── docs/
    └── quick-reference.md
```

## See Also

- `references/cicd/` - CI/CD deep-dive documentation
- `modules/` - Development workflow modules
- `subskills/` - Scientific workflow tool guides
- `templates/` - Pipeline starter templates
- `scripts/` - Automation scripts

---

**Version**: 1.0.0
**Last Updated**: 2025-01-18
**Sources**: development-workflow-specialist, git-workflow-manager, scientific-workflow-management, alfred-workflow-orchestration, faber-core, cicd-pipelines, semantic-release
