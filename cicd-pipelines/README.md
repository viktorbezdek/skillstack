# CI/CD Pipelines

> **v1.1.23** | DevOps & Infrastructure | 25 iterations

Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise release management.

## What Problem Does This Solve

Engineering teams building CI/CD pipelines from scratch repeatedly make the same mistakes: hardcoding secrets instead of using OIDC, building monolithic 45-minute pipelines instead of parallelized stages, and having no rollback strategy when production deployments fail. Keeping pipelines consistent across GitHub Actions, GitLab CI, and Kubernetes while meeting security requirements (OpenSSF, SLSA, supply chain integrity) requires patterns most teams learn only after incidents. This skill consolidates production-grade pipeline design, DevSecOps practices, and infrastructure automation into templates and analysis scripts ready for immediate use.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Set up a GitHub Actions CI pipeline for my Node.js project" | Complete node-ci.yml template with caching, test parallelization, security scanning, and deployment stages |
| "My builds take 45 minutes — how do I speed them up?" | Pipeline optimizer script, caching strategy guide, parallel job patterns, and path-based trigger configuration |
| "How do I stop using static AWS credentials in CI and use OIDC instead?" | OIDC authentication setup for GitHub Actions to AWS with minimal IAM permissions example |
| "I need Kubernetes deployments managed via GitOps with ArgoCD" | ArgoCD GitOps architecture pattern, Kubernetes manifest with HPA, and Terraform EKS module |
| "My pipeline needs vulnerability scanning and secret detection" | DevSecOps pipeline template with CodeQL, Trivy, Semgrep, and TruffleHog integration |
| "How do I set up automated semantic versioning and releases?" | semantic-release configuration, init scripts, changelog generation, and artifact signing with Cosign |

## When NOT to Use This Skill

- automating release workflows or orchestration -- use [workflow-automation](../workflow-automation/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/cicd-pipelines
```

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

- **When to Use This Skill** -- Categorized scenarios across CI/CD development, DevSecOps, infrastructure as code, container orchestration, and release management
- **Quick Start** -- Platform decision tree for selecting templates, pipeline performance quick-wins checklist, and essential security checklist with OIDC example
- **Core Capabilities** -- Table mapping domains to tools: CI/CD platforms, IaC, containers, GitOps, security scanning, cloud platforms, and release management
- **Architecture Patterns** -- CI/CD pipeline flow diagram and GitOps architecture showing App Repo → Config Repo → ArgoCD → Kubernetes sync loop
- **Reference Documentation** -- Index of all reference files across pipeline design, DevSecOps, infrastructure, enterprise readiness, and release management
- **Templates** -- GitHub Actions templates (Node.js, Python, Go, Docker, security, DCO), GitLab CI equivalents, release configuration, and enterprise governance templates
- **Scripts** -- Pipeline analyzer, CI health checker, OpenSSF badge verifier, coverage validators, TLS checker, SPDX header tools, and release initialization scripts
- **Anti-Patterns to Avoid** -- Seven common failures (YAML proliferation, hardcoded secrets, no rollback, monolithic pipelines, running as root, latest tags, script injection) with specific fixes

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

- **[Cloud Finops](../cloud-finops/)** -- Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, cloud billing (AWS, Azure, GCP), comm...
- **[Docker Containerization](../docker-containerization/)** -- Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration...
- **[Git Workflow](../git-workflow/)** -- Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file gro...
- **[Workflow Automation](../workflow-automation/)** -- Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution,...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
