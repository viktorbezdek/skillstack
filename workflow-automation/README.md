# Workflow Automation

> **v1.1.21** | DevOps & Infrastructure | 23 iterations

> Automate the processes your team runs manually -- releases, parallel development, multi-agent orchestration, and computation pipelines -- with structured patterns and ready-to-use scripts.

## The Problem

Modern software delivery involves a web of interdependent processes that are easy to start manually and painful to scale. Releases require a human who remembers the right sequence: bump version, update changelog, tag, build, publish, notify. Miss a step and you ship a broken release or publish the wrong version. Run it out of order and the changelog references commits that do not exist in the tag.

Parallel feature development turns chaotic when teams work on overlapping files across long-lived branches. Merge conflicts pile up. Nobody tracks which worktrees are active and which are stale. When it is time to release, the integration pain is proportional to how long the branches lived.

Multi-agent workflows add another layer of complexity. Coordinating multiple agents with stage dependencies, error recovery, and performance monitoring requires patterns that most teams reinvent from scratch -- and reinvent poorly, with no locking, no state persistence, and no audit trail.

Scientific computation workflows face their own scaling wall. A data scientist starts with joblib on a laptop, then needs HPC cluster execution, then needs a DAG orchestrator with retries and monitoring. Each tool transition requires learning a new framework and rewriting existing jobs.

Teams end up with tribal knowledge encoded in one-off scripts, release checklists in wikis that nobody updates, and workflow coordination that depends on specific people being available. The common thread: processes that should be automated and reproducible are instead manual and fragile.

## The Solution

This plugin provides structured patterns and ready-to-use tooling for every layer of workflow automation. It is the largest skill in SkillStack by component count -- 6 development workflow modules, 5+ CI/CD references, 11 semantic release references, 30+ FABER state machine scripts, CI/CD templates for both GitHub Actions and GitLab CI, 6 scientific workflow subskills, git worktree management scripts, and example code for enterprise testing and browser automation.

Semantic release automation replaces manual version bumps with conventional commits (feat/fix/BREAKING CHANGE) that automatically determine version numbers, generate changelogs, and publish releases. The local-first workflow means you can release from your machine without depending on CI -- with setup scripts, multi-account authentication, and monorepo support built in.

Git worktree management provides scripts following GitFlow conventions for creating isolated worktrees (`create_worktree.sh feature email-notifications`), listing active worktrees with status, and cleaning up merged ones.

The FABER state machine provides 30+ shell scripts for state machine workflows with init, read, write, validate, lock, hook, phase management, and audit operations -- building blocks for any stateful automation process.

Multi-agent orchestration uses WorkflowEngine patterns where you define agents by domain, wire them into stages with dependency declarations, and let the engine handle execution order, error recovery, and performance monitoring.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Releases require a human who remembers the right sequence -- version bump, changelog, tag, build, publish | Conventional commits drive automatic version bumps, changelog generation, and publishing via semantic release scripts |
| Parallel feature branches accumulate merge conflicts with no visibility into active work | Git worktree scripts create isolated worktrees, list active ones with status, and clean up stale branches |
| Multi-agent coordination is ad-hoc with no state persistence or error recovery | WorkflowEngine patterns provide stage dependencies, locking, error recovery, and audit trails |
| CI/CD pipelines are copy-pasted and hand-modified per project | Ready-to-use templates for Node, Python, Go, Docker, and security scanning on both GitHub Actions and GitLab CI |
| Scientific computation hits a scaling wall when moving from laptop to cluster | Decision tree routes you from joblib (laptop) to Parsl (HPC) to Prefect (DAGs) based on your actual requirements |
| Workflow state lives in variables that disappear when a script crashes | FABER state machine persists state to disk with validation, locking, backup, and phase management |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install workflow-automation@skillstack
```

### Prerequisites

No additional dependencies for the core skill. Individual capabilities may require specific tools:
- Semantic release: `npm install -g semantic-release`
- Git worktrees: Git 2.15+
- Scientific workflows: Python with the relevant library (joblib, Prefect, Parsl)

### Verify installation

After installing, test with:

```
Set up automated semantic versioning and changelog generation for my Node.js project
```

## Quick Start

1. Install the plugin with the commands above
2. Type: `Automate my release process -- I want to stop manually bumping versions and writing changelogs`
3. The skill walks you through setting up semantic release with conventional commits, configuring `init_project.sh`, and running your first automated release
4. Verify the generated changelog and version tag are correct
5. Next, try: `I need to coordinate three agents working on different parts of the codebase -- how do I set up the workflow?`

## What's Inside

This is a **single-skill plugin** with the largest supporting structure in SkillStack.

### Core Capabilities

| Capability | Key resources | What it covers |
|---|---|---|
| CI/CD Pipelines | `references/cicd/`, `templates/github-actions/`, `templates/gitlab-ci/` | Pipeline design patterns, DevSecOps scanning (SAST, DAST, SCA), deployment strategies (blue-green, canary, rolling), troubleshooting |
| Git Worktree Management | `scripts/git/` | Worktree creation, listing, and cleanup following GitFlow conventions |
| Scientific Workflows | `subskills/` (joblib, Prefect, Parsl, Covalent, FireWorks, quacc) | Tool selection from simple function caching to HPC cluster orchestration |
| Multi-Agent Orchestration | `references/alfred-workflow-reference.md` | WorkflowEngine patterns for coordinating agents with stage dependencies and error recovery |
| TDD/Debug/Review | `modules/` (tdd-context7, ai-debugging, automated-code-review, smart-refactoring, performance-optimization) | TDDManager, AIDebugger, AutomatedCodeReviewer with TRUST 5 framework |
| Semantic Release | `references/semantic-release/`, `scripts/release/` | Local-first releases, conventional commits, version bump rules, monorepo support, PyPI publishing |
| FABER State Management | `scripts/faber/` | 30+ shell scripts for state machine workflows: init, read, write, validate, lock, hook, phase, audit |

### Component Inventory

| Type | Count | Key files |
|---|---|---|
| Modules | 6 | TDD, AI debugging, code review, smart refactoring, performance optimization |
| CI/CD references | 5 | Best practices, DevSecOps, security, optimization, troubleshooting |
| Semantic release references | 11 | Local workflow, authentication, troubleshooting, monorepo support, PyPI publishing, version alignment |
| Other references | 5 | Alfred workflow orchestration, GitFlow conventions, Playwright patterns (3) |
| FABER scripts | 30+ | State init/read/write/validate, lock acquire/release/check, hook execute/validate, phase management, diagnostics, audit |
| Git scripts | 3 | create_worktree.sh, list_worktrees.sh, cleanup_worktrees.sh |
| Release scripts | 3 | init_project.sh, init_user_config.sh, create_org_config.sh |
| CI/CD templates | 10 | GitHub Actions + GitLab CI for Node, Python, Go, Docker, security scanning |
| Subskills | 6 | joblib, Prefect, Parsl, Covalent, FireWorks, quacc |
| Evals | 16 | 13 trigger scenarios + 3 output quality scenarios |

### workflow-automation

**What it does:** Activates when you need to automate workflows, orchestrate multi-agent tasks, run parallel task execution, manage release automation, build state machines, or coordinate complex task dependencies. Provides patterns and scripts covering the full spectrum from simple release automation to complex multi-agent state machine workflows.

**Try these prompts:**

```
Automate my release process -- I want conventional commits to drive version bumps and changelog generation automatically
```

```
I need to run three agents in parallel with the third depending on the first two finishing -- how do I wire this up?
```

```
We have five feature branches being worked on simultaneously and merge conflicts are killing us -- set up worktree isolation
```

```
My Python data pipeline needs to scale from my laptop to an HPC cluster -- which workflow tool should I use?
```

```
Set up automated code review that checks test coverage, security, and code quality before PRs can merge
```

```
I need a state machine for my deployment workflow -- it has stages (build, test, deploy, verify) and needs to survive crashes
```

**Key references:**

| Reference | Topic |
|---|---|
| `cicd/best_practices.md` | CI/CD pipeline design patterns and optimization |
| `cicd/devsecops.md` | Security scanning integration (SAST, DAST, SCA) |
| `semantic-release/local-release-workflow.md` | Local-first release automation setup |
| `semantic-release/monorepo-support.md` | Multi-package repository release coordination |
| `semantic-release/troubleshooting.md` | Common release automation problems and fixes |
| `alfred-workflow-reference.md` | Multi-agent orchestration with WorkflowEngine |
| `gitflow-conventions.md` | Branch naming and worktree conventions |
| `playwright-best-practices.md` | Browser automation testing patterns |

## Real-World Walkthrough

You are the lead engineer on a team of six building a B2B SaaS product. Your release process is a 12-step checklist in a Notion doc that only you know how to execute correctly. Last month, a junior developer tried to release while you were on vacation and published version 2.3.0 with breaking changes under a minor version bump because the changelog had "feat:" commits mixed with unlabeled breaking changes. Customers hit the breaking change with no migration guide because nobody wrote one.

You decide to automate the entire release pipeline.

**Step 1: Semantic release setup**

```
Set up semantic release for my Node.js monorepo -- we have three packages (api, sdk, dashboard) and need independent versioning
```

The skill walks you through the setup. You run `scripts/release/init_project.sh` which creates `.releaserc.json` with conventional commit rules: `feat:` triggers a minor bump, `fix:` triggers a patch, `BREAKING CHANGE:` in the commit body triggers a major bump. The monorepo support reference shows how to configure independent versioning per package using `semantic-release-monorepo` so the API can be on v3.1.0 while the SDK is on v2.5.0.

You set up `init_user_config.sh` for multi-account authentication so the release process can publish the API to your private registry and the SDK to npm public. The local-first workflow means releases run from your machine (not just CI), giving you control over timing while eliminating manual steps.

**Step 2: Git worktree isolation**

Your team is building four features in parallel and merge conflicts are a daily occurrence. You ask:

```
Set up worktree isolation for our parallel feature branches -- we have email-notifications, billing-v2, admin-dashboard, and api-v3 in progress
```

The skill provides the git worktree scripts. `create_worktree.sh feature email-notifications` creates a dedicated branch and working directory at `.worktrees/feature/email-notifications`. Each developer works in an isolated directory with its own `node_modules`, build output, and running dev server. No more "hold on, let me stash my changes" before switching contexts.

`list_worktrees.sh` gives the team visibility into all active worktrees with their branch status and last commit. `cleanup_worktrees.sh --merged` runs weekly to remove worktrees whose branches have been merged to main.

**Step 3: Multi-agent code review**

You want automated quality gates before code reaches main. You ask:

```
Set up automated code review with the TRUST 5 framework -- I want test coverage, security, and code quality checks on every PR
```

The skill configures the AutomatedCodeReviewer module with the TRUST 5 framework: Test-first (>=85% coverage), Readable (linting and formatting), Unified (consistent patterns), Secured (no secrets, no SQL injection), Trackable (conventional commits, linked issues). Each dimension gets a score from 0 to 1, and the overall TRUST score must be >=0.85 for the PR to pass.

**Step 4: FABER state machine for deployment**

Your deployment involves four stages (build, test, deploy to staging, promote to production) and the team has been burned by partial deployments -- the build succeeded, the deploy started, and then the process crashed, leaving staging in a half-deployed state with no record of what happened.

```
Build a deployment state machine using FABER -- I need crash recovery and an audit trail
```

The FABER scripts provide the building blocks. `state-init.sh` creates a state file for the deployment. `state-write.sh` records each stage transition. `lock-acquire.sh` prevents concurrent deployments. `phase-validate.sh` ensures stages execute in order. `state-backup.sh` creates snapshots before risky operations. If the process crashes, `state-read.sh` shows exactly where it stopped, and `error-recovery.sh` provides recovery options.

The result: your 12-step Notion checklist is replaced by an automated pipeline. Releases are triggered by conventional commits and execute without human intervention. Feature branches are isolated in worktrees. Code quality is enforced by automated review. Deployments are stateful with crash recovery. The junior developer who caused the breaking-change incident can now release safely because the automation enforces the rules that used to live in your head.

## Usage Scenarios

### Scenario 1: Automating releases for a monorepo

**Context:** You maintain a monorepo with three packages and release manually using a checklist. Each release takes 45 minutes and has gone wrong twice in the last quarter.

**You say:** `Set up semantic release for my monorepo with independent versioning per package -- api, sdk, and docs`

**The skill provides:**
- `init_project.sh` execution and `.releaserc.json` configuration
- Monorepo support with `semantic-release-monorepo` for independent package versions
- Conventional commit rules (feat/fix/BREAKING CHANGE) mapped to semver bumps
- Multi-account authentication for publishing to different registries

**You end up with:** Automated releases triggered by conventional commits, with each package versioned independently and published to its target registry.

### Scenario 2: Coordinating parallel agent workflows

**Context:** You are building an AI-powered code generation system where three agents (spec writer, implementer, reviewer) need to work in sequence with the reviewer's output potentially looping back to the implementer.

**You say:** `Set up a multi-agent workflow where spec-writer feeds implementer feeds reviewer, with the reviewer able to send work back to the implementer`

**The skill provides:**
- WorkflowEngine configuration with three agents and their dependencies
- Stage definitions with `depends_on` declarations
- Error recovery patterns for when an agent fails mid-stage
- Loop detection and termination criteria for the reviewer-implementer cycle
- Performance monitoring to identify bottleneck stages

**You end up with:** A coordinated agent pipeline with dependency management, error recovery, and monitoring -- not an ad-hoc script that breaks when any agent fails.

### Scenario 3: Choosing a scientific workflow tool

**Context:** You are a data scientist whose Python computation pipeline runs on your laptop with joblib caching. You need to scale to an HPC cluster with 200 nodes, but do not know which workflow framework to adopt.

**You say:** `I need to scale my Python pipeline from laptop (joblib) to HPC cluster -- which tool should I use and how do I migrate?`

**The skill provides:**
- Decision tree: joblib (10-100 tasks, single machine) vs Parsl (100+ tasks, HPC clusters) vs Prefect (complex DAGs with retries and UI) vs Covalent (cloud-agnostic deployment)
- Migration path from joblib to Parsl for HPC workloads
- Configuration examples for SLURM-based cluster execution
- Scaling considerations: task granularity, data transfer overhead, checkpoint frequency

**You end up with:** A clear tool choice with migration guidance and working configuration for your specific cluster setup.

### Scenario 4: Building a crash-resilient deployment pipeline

**Context:** Your deployment process has crashed twice mid-deploy, leaving staging in an inconsistent state. You need a deployment pipeline with state persistence and crash recovery.

**You say:** `Build a deployment state machine that survives crashes and tells me exactly where to resume`

**The skill provides:**
- FABER state machine setup with `state-init.sh` and stage definitions
- State persistence to disk with `state-write.sh` at each transition
- Lock management with `lock-acquire.sh` to prevent concurrent deploys
- Crash recovery with `state-read.sh` for diagnostics and `error-recovery.sh` for resume options
- Audit trail via `workflow-audit.sh` for post-incident review

**You end up with:** A deployment pipeline that persists its state, prevents concurrent execution, recovers from crashes, and maintains an audit trail.

## Ideal For

- **Teams releasing manually** -- semantic release automation replaces checklists with conventional commits and automated publishing
- **Teams doing parallel feature development** -- git worktree scripts isolate work and prevent merge-conflict pain
- **Engineers building multi-agent systems** -- WorkflowEngine patterns provide stage dependencies, error recovery, and monitoring
- **Data scientists scaling computation** -- the decision tree matches your workload to the right tool without trial-and-error adoption
- **Teams with fragile deployment processes** -- FABER state machine provides crash recovery and audit trails

## Not For

- **Writing CI/CD pipeline YAML configuration from scratch** -- use [cicd-pipelines](../cicd-pipelines/) for GitHub Actions, GitLab CI, Jenkins, and Terraform patterns
- **Managing Docker containers or writing Dockerfiles** -- use [docker-containerization](../docker-containerization/) for multi-stage builds, Compose, and container optimization
- **Git branching strategy, commit quality, or conventional commit format** -- use [git-workflow](../git-workflow/) for branch management and commit conventions

## How It Works Under the Hood

The plugin is a single skill with an unusually large supporting structure. The core `SKILL.md` provides a decision tree that routes your request to the right capability based on what you are trying to automate.

Six modules provide development workflow patterns (TDD, debugging, code review, refactoring, performance optimization). Five CI/CD references cover best practices, DevSecOps, security, optimization, and troubleshooting. Eleven semantic release references cover the full release automation lifecycle from setup through monorepo support to PyPI publishing. Five references cover Playwright patterns, GitFlow conventions, and multi-agent orchestration.

Thirty-plus FABER shell scripts implement a complete state machine toolkit. Three git scripts manage worktrees. Three release scripts handle project and user configuration. Ten CI/CD templates provide ready-to-use workflows for both GitHub Actions and GitLab CI across four languages plus security scanning. Six subskills cover scientific workflow tools from joblib to quacc.

The progressive disclosure approach means you never see the full component inventory -- the skill loads the relevant capability based on your request and pulls in the specific references, scripts, or templates that apply.

## Related Plugins

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline YAML configuration that this skill's templates generate
- **[Git Workflow](../git-workflow/)** -- Conventional commits and branch management that feed into this skill's release automation
- **[Docker Containerization](../docker-containerization/)** -- Container builds that are the deployment target for workflows designed here
- **[Cloud FinOps](../cloud-finops/)** -- Cost monitoring for the infrastructure these workflows run on

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — production-grade plugins for Claude Code.
