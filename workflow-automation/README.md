# Workflow Automation

> **v1.1.21** | Automate the processes your team runs manually -- releases, parallel development, multi-agent orchestration, and computation pipelines -- with structured patterns and ready-to-use scripts.
> Single skill + 6 modules + 21 references + 30+ FABER scripts + 10 CI/CD templates + 6 subskills + 6 git/release scripts | 13 trigger evals + 3 output evals

## Context to Provide

Workflow automation covers six distinct capability areas -- the skill routes to the right one based on what you describe. Precise context gets you directly to the scripts, patterns, and templates that fit your situation.

**What information to include in your prompt:**

- **The automation type** -- release management, parallel branch development, multi-agent orchestration, CI/CD pipelines, scientific computation scaling, or stateful process automation. If you are unsure, describe the manual process and let the skill route it.
- **Your current manual process** -- describe what you do today, including the steps you execute in order and where things go wrong. The failure mode (wrong version bump, mid-deploy crash, merge conflicts) determines which automation pattern to apply.
- **Language and tooling** -- "Node.js monorepo," "Python data pipeline," "Go services." Semantic release configuration differs by language; scientific workflow tool selection depends on what you are currently using.
- **Scale and constraints** -- number of packages (monorepo), number of parallel branches, number of agents in the workflow, cluster size (HPC), or stage count (state machine). These drive configuration choices.
- **What has already been tried** -- if you set up semantic release and it did nothing, if you tried conventional commits but versions did not bump, describing what failed prevents re-suggesting the same approach.

**What makes results better vs worse:**

- Better: for multi-agent orchestration, name each agent, what it does, and which agents depend on which
- Better: for release automation, describe whether this is a monorepo with independent versioning or a single package
- Better: for state machines, list the stages and what failure at each stage means (should it retry, rollback, or alert?)
- Worse: asking for "CI YAML" without workflow context -- use cicd-pipelines for platform-specific YAML syntax
- Worse: describing the tooling you want (FABER, Prefect) without describing the problem -- tool selection works backward from the problem
- Worse: asking about Docker, Dockerfiles, or container configuration -- that belongs to docker-containerization

**Template prompt:**

```
I want to automate: [describe the manual process in steps, including where it fails]

Current state:
- Language/platform: [e.g., Node.js monorepo with 3 packages, Python, Go]
- Scale: [e.g., 4 parallel feature branches, 3 agents, 200-node HPC cluster, 5-stage deployment]
- What has gone wrong: [the specific failure that motivated automation]

What I need from automation:
- [crash recovery / version bumps / parallel isolation / agent coordination / etc.]
```

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

---

## System Overview

```
User prompt (workflow automation request)
        |
        v
+-------------------------------+
|    workflow-automation         |  <-- Core skill with decision tree router
|         (SKILL.md)            |
+-------------------------------+
   |        |        |        |        |        |
   v        v        v        v        v        v
+------+ +------+ +------+ +------+ +------+ +------+
|Seman-| | Git  | |Multi-| |CI/CD | |Scien-| |FABER |
|tic   | |Work- | |Agent | |Pipe- | |tific | |State |
|Releas| |tree  | |Orch. | |lines | |Work- | |Mach. |
+------+ +------+ +------+ +------+ +------+ +------+
|11 refs| |3 sh  | |Alfred| |5 refs| |6 sub-| |30+   |
|3 setup| |scripts| |ref + | |10    | |skills| |shell |
|scripts| |GitFlow| |modules| |tmpl | |      | |scripts|
+------+ +------+ +------+ +------+ +------+ +------+

Development Workflow Modules:
  TDD (tdd-context7) | AI Debugging | Automated Code Review
  Smart Refactoring  | Performance Optimization
```

The core skill acts as a router -- its decision tree identifies what type of workflow you need and loads the relevant capability. Semantic release handles versioning and publishing. Git worktree scripts manage parallel development. Multi-agent orchestration coordinates agents. CI/CD references and templates handle pipelines. Scientific workflow subskills cover computation scaling. FABER scripts provide stateful automation building blocks.

## What's Inside

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

### Component Spotlights

#### workflow-automation (skill)

**What it does:** Routes your workflow automation request to the right capability. The decision tree in SKILL.md identifies whether you need release automation, git worktree management, multi-agent orchestration, CI/CD pipeline templates, scientific computation scaling, FABER state machines, or development workflow modules. Then loads the relevant references, scripts, and patterns.

**Input -> Output:** You describe a manual or fragile process you want to automate -> You get specific patterns, scripts, configuration files, and step-by-step setup for the appropriate automation approach.

**When to use:**
- Automating releases with conventional commits and semantic versioning
- Managing parallel feature branches with git worktrees
- Coordinating multiple agents with dependencies and error recovery
- Scaling scientific computation from laptop to HPC cluster
- Building crash-resilient deployment pipelines with state persistence

**When NOT to use:**
- Writing CI/CD pipeline YAML from scratch -> use [cicd-pipelines](../cicd-pipelines/)
- Managing Docker containers or writing Dockerfiles -> use [docker-containerization](../docker-containerization/)
- Git branching strategy or commit conventions -> use [git-workflow](../git-workflow/)

**Try these prompts:**

```
Automate my release process for a Node.js monorepo with three packages: api, sdk, and dashboard-ui.
Right now I manually: check commits, decide the version bump, update three package.json files, write
the changelog, create a git tag, and publish each package to npm. Last month I published a breaking
change under a minor version bump because a "feat:" commit had breaking behavior. Set up semantic
release with independent versioning per package.
```

```
I need to coordinate three agents in a code generation pipeline:
1. spec-writer: reads a feature request and produces a technical spec
2. implementer: reads the spec and writes code
3. reviewer: evaluates the code and either approves or sends back to implementer with feedback

The reviewer can reject up to 3 times before escalating to a human. Agent 3 depends on agent 2,
which depends on agent 1. How do I wire this with error recovery and loop termination?
```

```
We have six active feature branches: payments-v2, auth-sso, admin-dashboard, api-versioning,
mobile-redesign, and notification-system. They share files in src/shared/ and merge conflicts
are a daily problem. Three developers working on payments-v2 need to stay isolated from the
others while sharing the main branch's security patches. Set up worktree isolation.
```

```
My Python materials science pipeline currently runs on my laptop using joblib for parallelism.
It processes molecular dynamics simulations: 500 independent jobs, each taking 10-30 minutes,
using custom Fortran binaries. I need to scale to a university SLURM cluster with 200 nodes.
Which workflow tool should I use -- Parsl, Prefect, or Covalent?
```

```
Build a deployment state machine for my four-stage pipeline: build (2 min), integration-test (8 min),
staging-deploy (3 min), and production-deploy (5 min). The pipeline has crashed twice mid-deploy:
once at staging-deploy, once at production-deploy. I need crash recovery (resume from the failed
stage, not start over), concurrent execution prevention (no two deploys at once), and an audit
trail for post-incident review.
```

#### FABER State Machine (scripts)

**CLI:** `scripts/faber/state-init.sh`, `state-read.sh`, `state-write.sh`, `lock-acquire.sh`, `phase-validate.sh`, etc.
**What it produces:** Persistent state files on disk, lock files for concurrency control, audit logs for post-incident review.
**Typical workflow:** Initialize state -> acquire lock -> validate phase -> write state at each transition -> release lock. On crash: read state to find where it stopped, run error-recovery for resume options.

#### Git Worktree Scripts (scripts)

**CLI:** `scripts/git/create_worktree.sh <type> <name>`, `list_worktrees.sh`, `cleanup_worktrees.sh [--merged]`
**What it produces:** Isolated working directories following GitFlow conventions (feature/, bugfix/, release/).
**Typical workflow:** Create worktrees for each active feature, list periodically for visibility, clean up after branches merge.

#### Release Scripts (scripts)

**CLI:** `scripts/release/init_project.sh`, `init_user_config.sh`, `create_org_config.sh`
**What it produces:** `.releaserc.json` configuration, user-level auth config, org-level shared config.
**Typical workflow:** Run once per project to set up semantic release, once per developer for auth, once per organization for shared conventions.

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

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, may not activate) | Good (specific, activates reliably) |
|---|---|
| "Help me automate things" | "Automate my release process -- I want conventional commits to drive version bumps and changelog generation" |
| "Fix my deployment" | "Build a deployment state machine with crash recovery using FABER -- I have four stages that need to survive failures" |
| "Make branches work better" | "Set up worktree isolation for five parallel feature branches -- merge conflicts are killing us" |
| "Scale my Python script" | "My joblib pipeline needs to scale from laptop to a SLURM HPC cluster with 200 nodes -- which tool should I use?" |
| "Set up CI" | "I need to coordinate three agents where agent C depends on agents A and B finishing -- how do I wire the workflow?" |

### Structured Prompt Templates

**For release automation:**
```
Set up semantic release for my [language] [monorepo/single-package] project. I need [conventional commits / independent versioning per package / publishing to NPM+PyPI]. Currently I release manually and it takes [time].
```

**For multi-agent orchestration:**
```
I need to coordinate [N] agents: [list agents and what each does]. [Agent C] depends on [A and B] finishing. I need [error recovery / retry logic / performance monitoring]. How do I set up the workflow?
```

**For git worktree management:**
```
Set up worktree isolation for our team -- we have [N] feature branches active simultaneously and merge conflicts are [frequency]. We follow [GitFlow / trunk-based / custom] branching.
```

**For scientific workflow scaling:**
```
My [type of computation] pipeline currently runs on [laptop / single server] using [current tool, e.g., joblib]. I need to scale to [target, e.g., HPC cluster with N nodes]. Which workflow tool should I use and how do I migrate?
```

**For state machine workflows:**
```
Build a state machine for my [process, e.g., deployment workflow] with stages [list stages]. It needs to [survive crashes / prevent concurrent execution / maintain audit trail / validate stage order].
```

### Prompt Anti-Patterns

- **Asking for CI/CD YAML without mentioning automation context:** "Write me a GitHub Actions workflow" is a cicd-pipelines request. This skill handles the automation patterns and decision logic, not the YAML syntax. Ask about what you want to automate, not how to write pipeline config.
- **Conflating git workflow with workflow automation:** "Help me with git branching" is a git-workflow request. This skill provides worktree scripts and GitFlow conventions, but branch strategy and commit conventions belong to git-workflow.
- **Asking for a generic "best tool" without describing your workload:** "What's the best workflow tool?" is unanswerable. Describe your computation shape (tasks, parallelism, target infrastructure) so the decision tree can route to the right tool.
- **Requesting Dockerfile or container optimization:** Container concerns belong to docker-containerization. This skill handles the workflow that builds and deploys containers, not the containers themselves.

## Real-World Walkthrough

You are the lead engineer on a team of six building a B2B SaaS product. Your release process is a 12-step checklist in a Notion doc that only you know how to execute correctly. Last month, a junior developer tried to release while you were on vacation and published version 2.3.0 with breaking changes under a minor version bump because the changelog had "feat:" commits mixed with unlabeled breaking changes. Customers hit the breaking change with no migration guide.

**Step 1 -- Semantic release setup.** You ask:

```
Set up semantic release for my Node.js monorepo -- we have three packages (api, sdk, dashboard) and need independent versioning
```

The skill walks you through `scripts/release/init_project.sh` which creates `.releaserc.json` with conventional commit rules: `feat:` triggers minor, `fix:` triggers patch, `BREAKING CHANGE:` triggers major. The monorepo support reference configures independent versioning per package using `semantic-release-monorepo`. You set up `init_user_config.sh` for multi-account authentication.

**Step 2 -- Git worktree isolation.** Your team is building four features in parallel and merge conflicts are daily. You ask:

```
Set up worktree isolation for our parallel feature branches -- email-notifications, billing-v2, admin-dashboard, and api-v3
```

`create_worktree.sh feature email-notifications` creates a dedicated branch and working directory. Each developer works in isolation. `list_worktrees.sh` gives visibility. `cleanup_worktrees.sh --merged` runs weekly.

**Step 3 -- Multi-agent code review.** You ask:

```
Set up automated code review with the TRUST 5 framework -- test coverage, security, and code quality on every PR
```

The AutomatedCodeReviewer module configures TRUST 5: Test-first (>=85% coverage), Readable, Unified, Secured, Trackable. Each dimension gets a 0-1 score, overall must be >=0.85.

**Step 4 -- FABER state machine for deployment.** Your deployment has crashed mid-deploy twice. You ask:

```
Build a deployment state machine using FABER -- I need crash recovery and an audit trail
```

FABER scripts provide: `state-init.sh` creates state, `state-write.sh` records transitions, `lock-acquire.sh` prevents concurrent deploys, `phase-validate.sh` enforces order, `state-backup.sh` snapshots before risky operations, `error-recovery.sh` provides resume options on crash.

**Step 5 -- Result.** Your 12-step Notion checklist is replaced by automation. Releases are triggered by conventional commits. Features are isolated in worktrees. Code quality is enforced by TRUST 5. Deployments are stateful with crash recovery. The junior developer can now release safely.

**Gotchas discovered:** The biggest win was the local-first release workflow -- running releases from dev machines instead of only through CI gave the team immediate feedback and faster iteration on the release configuration itself.

## Usage Scenarios

### Scenario 1: Automating releases for a monorepo

**Context:** You maintain a monorepo with three packages and release manually using a checklist. Each release takes 45 minutes and has gone wrong twice in the last quarter.

**You say:** `Set up semantic release for my monorepo with independent versioning per package -- api, sdk, and docs`

**The skill provides:**
- `init_project.sh` execution and `.releaserc.json` configuration
- Monorepo support with `semantic-release-monorepo` for independent package versions
- Conventional commit rules mapped to semver bumps
- Multi-account authentication for different registries

**You end up with:** Automated releases triggered by conventional commits, with each package versioned independently.

### Scenario 2: Coordinating parallel agent workflows

**Context:** You are building an AI-powered code generation system where three agents (spec writer, implementer, reviewer) need to work in sequence with the reviewer able to loop back to the implementer.

**You say:** `Set up a multi-agent workflow where spec-writer feeds implementer feeds reviewer, with the reviewer able to send work back`

**The skill provides:**
- WorkflowEngine configuration with three agents and dependencies
- Stage definitions with `depends_on` declarations
- Error recovery patterns for agent failures
- Loop detection and termination criteria

**You end up with:** A coordinated agent pipeline with dependency management, error recovery, and monitoring.

### Scenario 3: Choosing a scientific workflow tool

**Context:** You are a data scientist whose Python pipeline runs on your laptop with joblib. You need HPC cluster execution with 200 nodes.

**You say:** `I need to scale my Python pipeline from laptop (joblib) to HPC cluster -- which tool should I use?`

**The skill provides:**
- Decision tree: joblib (single machine) vs Parsl (HPC) vs Prefect (complex DAGs) vs Covalent (cloud-agnostic)
- Migration path from joblib to Parsl
- SLURM configuration examples
- Scaling considerations: task granularity, data transfer, checkpointing

**You end up with:** A clear tool choice with migration guidance and working cluster configuration.

### Scenario 4: Building a crash-resilient deployment pipeline

**Context:** Your deployment has crashed twice mid-deploy, leaving staging inconsistent. You need state persistence and crash recovery.

**You say:** `Build a deployment state machine that survives crashes and tells me exactly where to resume`

**The skill provides:**
- FABER state machine setup with stage definitions
- State persistence at each transition
- Lock management to prevent concurrent deploys
- Crash recovery with diagnostics and resume options
- Audit trail for post-incident review

**You end up with:** A deployment pipeline that persists state, prevents concurrency, recovers from crashes, and maintains an audit trail.

---

## Decision Logic

**How does the skill route requests to capabilities?**

The decision tree in SKILL.md branches on what you are automating:
- Build/test/deploy pipeline -> CI/CD references + templates
- Parallel feature development -> Git worktree scripts + GitFlow conventions
- Scientific computation -> Subskill selection (joblib -> Parsl -> Prefect -> Covalent)
- Multi-agent coordination -> Alfred WorkflowEngine patterns + development modules
- Version/release management -> Semantic release references + setup scripts
- Stateful process automation -> FABER state machine scripts

**When does this skill activate vs cicd-pipelines, git-workflow, or docker-containerization?**

This skill handles workflow orchestration and automation patterns. cicd-pipelines handles YAML configuration syntax for specific CI platforms. git-workflow handles branch strategy and commit conventions. docker-containerization handles container builds and optimization. The boundary: if you are asking about how to automate a process or coordinate multiple stages, use this skill. If you are asking about specific platform configuration (GitHub Actions YAML, Dockerfile syntax, branch naming), use the specialized skill.

**Scientific workflow tool selection logic:**

| Your situation | Tool | Why |
|---|---|---|
| 10-100 tasks, single machine, need caching | joblib | Minimal setup, `@memory.cache` decorator |
| 100+ tasks, HPC cluster, SLURM/PBS | Parsl | Native HPC executors, scales to thousands of nodes |
| Complex DAG, need retries and UI monitoring | Prefect | Visual flow builder, built-in retry/scheduling |
| Cloud-agnostic, multiple providers | Covalent | Dispatch to AWS/GCP/Azure without rewriting |
| Materials science domain | quacc/FireWorks | Domain-specific calculators and job management |

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Semantic release commits do not follow conventional format | No version bump occurs, release pipeline runs but publishes nothing | Enforce conventional commits with a commit-msg hook (git-workflow provides this). Audit recent commits with `git log --oneline` and rewrite non-conforming ones before release. |
| FABER state file corrupted during a crash | `state-read.sh` returns invalid data, deployment cannot resume | `state-backup.sh` creates snapshots before risky operations. Restore from the latest backup. If no backup exists, `state-init.sh` resets state and you restart from the beginning of the current phase. |
| Git worktrees accumulate without cleanup | Disk fills up, developers forget which worktrees are active, stale branches linger | Run `cleanup_worktrees.sh --merged` weekly (automate with a cron job or CI schedule). `list_worktrees.sh` provides visibility for manual review. |
| Multi-agent workflow enters infinite reviewer-implementer loop | Reviewer keeps rejecting, implementer keeps revising, tokens and time are wasted | Set a maximum iteration count in the WorkflowEngine configuration (typically 3). After max iterations, escalate to human review instead of looping. |
| Wrong scientific workflow tool chosen | joblib pipeline works on laptop but does not scale, or Parsl is too heavy for a simple pipeline | Use the decision tree before committing. If you already committed to the wrong tool, the subskills provide migration paths (joblib -> Parsl is documented; Parsl -> Prefect requires rewriting task definitions). |

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

## Related Plugins

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline YAML configuration that this skill's templates generate
- **[Git Workflow](../git-workflow/)** -- Conventional commits and branch management that feed into this skill's release automation
- **[Docker Containerization](../docker-containerization/)** -- Container builds that are the deployment target for workflows designed here
- **[Cloud FinOps](../cloud-finops/)** -- Cost monitoring for the infrastructure these workflows run on
- **[Multi-Agent Patterns](../multi-agent-patterns/)** -- Higher-level agent coordination patterns that complement this skill's WorkflowEngine

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
