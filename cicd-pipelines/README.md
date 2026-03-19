# CI/CD Pipelines

> **v1.1.23** | DevOps & Infrastructure | 25 iterations

Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise release management.

## What Problem Does This Solve

A unified skill for CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, security scanning, and enterprise release management across all major platforms.

## When to Use This Skill

CI/CD pipeline design and DevOps automation — use when the user mentions GitHub Actions, GitLab CI, Jenkins, Terraform, infrastructure as code, DevSecOps, ArgoCD, Kubernetes manifests, or pipeline configuration YAML.

## When NOT to Use This Skill

- automating release workflows or orchestration -- use [workflow-automation](../workflow-automation/) instead

## How to Use

**Direct invocation:**

```
Use the cicd-pipelines skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `ci-cd`
- `github-actions`
- `gitlab-ci`
- `terraform`
- `devops`

## What's Inside

- **When to Use This Skill**
- **Quick Start**
- **Core Capabilities**
- **Architecture Patterns**
- **Reference Documentation**
- **Templates**
- **Scripts**
- **Anti-Patterns to Avoid**

## Key Capabilities

- **GitHub Actions**
- **GitLab CI**
- **Terraform**
- **Kubernetes**
- **ArgoCD**
- **OpenSSF Scorecard**

## Version History

- `1.1.23` fix(devops): disambiguate cicd-pipelines vs workflow-automation vs docker-containerization (c60a8d7)
- `1.1.22` fix(cicd-pipelines): repair broken cross-reference and update plugin count (d466398)
- `1.1.21` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.20` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.19` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.18` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.17` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.16` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.15` fix: make all shell scripts executable and fix Python syntax errors (61ac964)
- `1.1.14` docs: add detailed README documentation for all 34 skills (7ba1274)

## Related Skills

- **[Docker Containerization](../docker-containerization/)** -- Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration...
- **[Git Workflow](../git-workflow/)** -- Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file gro...
- **[Workflow Automation](../workflow-automation/)** -- Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution,...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 46 production-grade plugins for Claude Code.
