# Docker Containerization

> **v1.1.22** | DevOps & Infrastructure | 24 iterations

Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration, container optimization, development environment setup, and infrastructure patterns.

## What Problem Does This Solve

Containerization solves "works on my machine" problems, but poorly written Dockerfiles create their own problems: bloated images that slow CI/CD pipelines, security vulnerabilities from running as root, cache misses that rebuild everything on every change, and port conflicts when running multiple services locally. This skill covers Dockerfile best practices, multi-stage builds for production-sized images, Docker Compose orchestration for local development environments, and specialized patterns for isolated worktree development and DDEV-based PHP/TYPO3 setups.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My Docker image is 2GB and I need to reduce it" | Multi-stage build patterns separating build-time and runtime dependencies, with dockerignore configuration and a target of images under 500MB |
| "Write me a Dockerfile for this Node.js app" | Dockerfile best practices: pinned base image versions, dependency-first layer ordering for cache efficiency, non-root user creation, and health check patterns |
| "I need to run my app with a database and Redis locally" | Docker Compose multi-container setup with named volumes for data persistence, health checks, restart policies, and environment-specific compose file patterns |
| "I'm running multiple git worktrees and the services conflict" | Worktree isolation strategy: consistent port allocation across worktrees, isolated browser state for parallel testing, CORS configuration, and worktree manager scripts |
| "Set up a DDEV environment for my TYPO3/PHP project" | DDEV quickstart, prerequisites validation, advanced options, and troubleshooting references for PHP-based development environments |
| "My Dockerfile is inefficient — how do I analyze it?" | `docker_optimize.py` script for automated Dockerfile analysis plus a quick reference command table for build, run, logs, shell, and cleanup operations |

## When NOT to Use This Skill

- CI/CD pipeline YAML or pipeline configuration -- use [cicd-pipelines](../cicd-pipelines/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/docker-containerization
```

## How to Use

**Direct invocation:**

```
Use the docker-containerization skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `docker`
- `containers`
- `compose`
- `multi-stage`

## What's Inside

- **When to Use This Skill** -- Eight use cases: containerization, Compose orchestration, development environments, optimization, port management, browser automation, CI/CD image building, and meta-configuration systems.
- **Quick Start** -- Ready-to-run basic Dockerfile and Docker Compose examples for immediate use.
- **Core Docker Concepts** -- Dockerfile best practices with security (non-root user), caching (dependency-first ordering), and multi-stage builds with benefits explained; dockerignore patterns.
- **Best Practices** -- Organized checklist for Dockerfiles (versioning, security, size), Docker Compose (volumes, health checks, resource limits), and development environments (port isolation, worktree setup).
- **Quick Reference** -- Command table for the nine most common Docker and Compose operations.
- **Reference Navigation** -- Thirteen reference files covering Docker basics, Compose, extended patterns, Ghostmind meta.json config, worktree strategy, port allocation, browser isolation, CORS, troubleshooting, and DDEV guides.
- **Scripts Reference** -- Seven scripts: Dockerfile optimizer, prerequisites validator, worktree manager, MCP isolation setup, connectivity validator, isolation tester, and migration tool.
- **Resources** -- Official documentation links for Docker, Docker Compose, Dockerfile reference, DDEV, and Docker security.

## Version History

- `1.1.22` fix(devops): disambiguate cicd-pipelines vs workflow-automation vs docker-containerization (c60a8d7)
- `1.1.21` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.20` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.19` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.18` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.17` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.16` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.15` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.14` fix: make all shell scripts executable and fix Python syntax errors (61ac964)
- `1.1.13` docs: add detailed README documentation for all 34 skills (7ba1274)

## Related Skills

- **[Cicd Pipelines](../cicd-pipelines/)** -- Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise ...
- **[Cloud Finops](../cloud-finops/)** -- Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, cloud billing (AWS, Azure, GCP), comm...
- **[Git Workflow](../git-workflow/)** -- Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file gro...
- **[Workflow Automation](../workflow-automation/)** -- Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution,...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
