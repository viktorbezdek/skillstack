# Workflow Automation

> **v1.1.21** | DevOps & Infrastructure | 23 iterations

Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution, release automation, and git workflow management.

## What Problem Does This Solve

Modern software delivery involves a web of interdependent processes — parallel feature branches, multi-agent task pipelines, versioned releases, scientific computation jobs — that are easy to start manually but painful to scale and reproduce. Ad-hoc automation accumulates as one-off scripts that break when contributors change, releases require human memory to execute correctly, and complex workflows get blocked on a single bottleneck. This skill provides structured patterns and tooling for orchestrating all of these: from git worktree management and multi-agent coordination to semantic release automation and FABER state machine workflows.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Automate my versioning and changelog so releases don't require manual steps" | Semantic Release setup with conventional commits, local-first release workflow, and version bump rules (feat/fix/BREAKING CHANGE) |
| "I need to run multiple agents in parallel with dependencies between stages" | WorkflowEngine patterns for multi-agent coordination with stage dependencies, error recovery, and performance monitoring |
| "We're doing parallel feature development and branches keep colliding" | Git worktree creation scripts following GitFlow conventions (feature/, fix/, hotfix/) with list and cleanup utilities |
| "My Python computation jobs need caching and parallel execution" | Scientific workflow tool selection guide: joblib for simple caching, Parsl for HPC clusters, Prefect for complex DAGs |
| "Set up automated code review that enforces our quality standards" | TRUST 5 framework (Test-first, Readable, Unified, Secured, Trackable) implemented via AutomatedCodeReviewer with configurable thresholds |
| "Coordinate a TDD cycle, debugging, and review as a single automated workflow" | TDDManager, AIDebugger, and AutomatedCodeReviewer modules that chain together as a development workflow pipeline |

## When NOT to Use This Skill

- CI/CD pipeline configuration or YAML -- use [cicd-pipelines](../cicd-pipelines/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install workflow-automation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the workflow-automation skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `automation`
- `ci-cd`
- `orchestration`
- `release-management`

## What's Inside

- **When to Use This Skill** -- Eight use case categories with specific examples for when to activate this skill vs. related ones.
- **Quick Decision Guide** -- Decision tree for routing to the right capability: CI/CD pipelines, git worktrees, scientific computation, multi-agent coordination, TDD/debug/review cycles, or release automation.
- **Core Capabilities** -- Detailed module breakdowns for all seven capabilities: CI/CD pipelines, git worktree management, scientific workflow tool selection, multi-agent orchestration, TDD/debug/review automation, semantic release, and FABER state management.
- **Quality Metrics** -- Threshold table for test coverage (>=85%), TRUST Score (>=0.85), critical issue count, performance regression limit, and API response time targets.
- **Best Practices** -- Concise rules for CI/CD pipeline design, git workflow hygiene, development workflow discipline, and release automation conventions.
- **Resources Directory Structure** -- Annotated directory tree of all modules, references, scripts, subskills, templates, and examples included in the skill.

## Key Capabilities

- **CI/CD Pipelines**
- **Git Workflows**
- **Scientific Workflows**
- **Multi-Agent Orchestration**
- **TDD/Development Cycles**
- **Code Review Automation**

## Version History

- `1.1.21` fix(devops): disambiguate cicd-pipelines vs workflow-automation vs docker-containerization (c60a8d7)
- `1.1.20` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.19` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.18` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.17` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.16` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.15` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.14` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.13` revert: restore faber/ subdirectory for FABER framework scripts (65a131e)
- `1.1.12` fix: resolve broken links, flatten faber scripts, add validate-patterns.py (4647f46)

## Related Skills

- **[Cicd Pipelines](../cicd-pipelines/)** -- Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise ...
- **[Cloud Finops](../cloud-finops/)** -- Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, cloud billing (AWS, Azure, GCP), comm...
- **[Docker Containerization](../docker-containerization/)** -- Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration...
- **[Git Workflow](../git-workflow/)** -- Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file gro...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
