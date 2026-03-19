# Workflow Automation

> **v1.1.21** | DevOps & Infrastructure | 23 iterations

Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution, release automation, and git workflow management.

## What Problem Does This Solve

Comprehensive guide for workflow automation, task management, and productivity optimization in software development. This skill combines CI/CD pipelines, git workflow management, scientific workflow tools, multi-agent orchestration, TDD workflows, and release automation.

## When to Use This Skill

Workflow orchestration and release automation — use when the user asks to automate workflows, orchestrate multi-agent tasks, run parallel task execution, manage release automation, build state machines, or coordinate complex task dependencies.

## When NOT to Use This Skill

- CI/CD pipeline configuration or YAML -- use [cicd-pipelines](../cicd-pipelines/) instead

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

- **When to Use This Skill**
- **Quick Decision Guide**
- **Core Capabilities**
- **Quality Metrics**
- **Best Practices**
- **Resources Directory Structure**
- **See Also**

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
- **[Docker Containerization](../docker-containerization/)** -- Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration...
- **[Git Workflow](../git-workflow/)** -- Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file gro...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 46 production-grade plugins for Claude Code.
