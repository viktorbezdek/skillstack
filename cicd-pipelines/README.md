# CI/CD Pipelines

> **v1.1.23** | DevOps & Infrastructure | 25 iterations

> Complete CI/CD pipeline design across GitHub Actions, GitLab CI, and Jenkins -- with ready-to-use templates, security scanning, Terraform modules, Kubernetes manifests, and enterprise release management.

## The Problem

Setting up a production CI/CD pipeline from scratch takes days. You start with a basic "run tests on push" workflow, then discover you need caching (builds are too slow), security scanning (the security team requires SAST/DAST), multi-environment deployments (dev/staging/prod with approval gates), container builds (Docker multi-stage with signing), and release automation (semantic versioning, changelogs, artifact provenance). Each addition requires learning platform-specific YAML syntax, debugging cryptic error messages, and discovering best practices through trial and error.

The mistakes are predictable and expensive. Hardcoded secrets in workflow files. No rollback strategy when deployments fail. Monolithic 45-minute pipelines that rebuild everything on every commit. Docker images running as root. Production deployments using `:latest` tags. YAML copy-pasted across repositories with subtle drift. Each mistake gets discovered in production, costs hours to fix, and could have been prevented with the right template from the start.

Even experienced DevOps engineers face this: every new project requires the same boilerplate across different platforms (GitHub Actions syntax differs from GitLab CI which differs from Jenkins), the same security setup (OIDC instead of static credentials, pinned action versions, minimal permissions), and the same optimization patterns (dependency caching, parallel jobs, path-based triggers). The knowledge transfers across projects, but the YAML does not.

## The Solution

This plugin provides the complete DevOps toolkit: CI/CD pipeline templates for GitHub Actions and GitLab CI across Node.js, Python, Go, Docker, and security scanning. Terraform modules for production infrastructure (EKS clusters). Kubernetes deployment manifests with HPA and ArgoCD integration. Security scanning pipelines covering SAST, DAST, SCA, container scanning, and secret detection. Enterprise readiness including OpenSSF badge criteria, signed releases, reproducible builds, and governance templates.

It ships 11 CI/CD workflow templates (6 GitHub Actions + 5 GitLab CI), 20+ runnable scripts (pipeline analyzer, CI health checker, coverage validators, security verifiers, deployment tools), 50+ reference documents covering every DevOps concern from Cloudflare Workers to Kubernetes basics, and enterprise templates for governance, architecture, and security audits.

You describe what you need -- "a Python CI pipeline with coverage and PyPI publishing" or "secure my GitHub Actions with OIDC and supply chain hardening" -- and get production-ready YAML with caching, security scanning, proper permissions, and deployment workflows. The pipeline analyzer script identifies optimization opportunities in existing pipelines. The security scripts verify badge criteria, signed tags, coverage thresholds, and TLS enforcement.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Days building CI/CD boilerplate from scratch for each project | Language-specific templates ready to use for GitHub Actions and GitLab CI |
| Monolithic 45-minute pipeline rebuilding everything on every commit | Parallel jobs, caching, path-based triggers cutting builds to minutes |
| Static AWS credentials stored as repository secrets | OIDC authentication with role assumption -- no static credentials |
| No security scanning until the security team complains | SAST, DAST, SCA, container scanning, and secret detection built into the pipeline |
| Manual release process with forgotten changelogs | semantic-release automating versions, changelogs, and artifact publishing |
| "It works on my machine" Docker builds | Multi-stage Dockerfiles with pinned versions, non-root users, and signed images |

## Installation

Add the SkillStack marketplace, then install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install cicd-pipelines@skillstack
```

### Verify Installation

After installing, test with:

```
Set up a GitHub Actions CI pipeline for my Node.js project with testing, linting, and Docker build
```

The skill activates automatically when you mention CI/CD, GitHub Actions, GitLab CI, or pipeline topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe your project:
   ```
   I need a CI/CD pipeline for a Python FastAPI project -- tests, coverage, security scanning, and deploy to AWS
   ```
3. The skill produces a GitHub Actions workflow with pytest, coverage thresholds, security scanning, and OIDC-based AWS deployment.
4. Optimize an existing pipeline:
   ```
   My CI pipeline takes 25 minutes -- help me speed it up
   ```
5. The pipeline analyzer identifies bottlenecks and produces an optimized version with caching, parallel jobs, and path filters.

## What's Inside

This is a comprehensive single-skill plugin with 50+ references, 11 workflow templates, 20+ scripts, and enterprise document templates.

| Component | Purpose |
|---|---|
| **cicd-pipelines** skill | Core methodology: pipeline design patterns, platform decision trees, optimization checklists, security hardening, architecture patterns (CI/CD flow, GitOps), anti-patterns |
| **50+ reference documents** | CI/CD platforms, DevSecOps, infrastructure, cloud platforms, enterprise readiness, release management (see table below) |
| **11 workflow templates** | 6 GitHub Actions + 5 GitLab CI: Node.js, Python, Go, Docker, security scanning, DCO check |
| **20+ scripts** | Pipeline analysis, security verification, coverage checking, deployment, release initialization |
| **Enterprise templates** | GOVERNANCE.md, ARCHITECTURE.md, CODE_OF_CONDUCT.md, SECURITY_AUDIT.md, semantic-release configs |

**Eval coverage:** 13 trigger eval cases + 3 output eval cases.

### How to Use: cicd-pipelines

**What it does:** Guides you through designing, implementing, and optimizing CI/CD pipelines across GitHub Actions, GitLab CI, and Jenkins. Covers the full DevOps spectrum: pipeline creation, security hardening, infrastructure as code (Terraform, Kubernetes), container orchestration, release management, and enterprise compliance (OpenSSF). Ships templates that generate working YAML and scripts that analyze existing pipelines.

**Try these prompts:**

```
Create a GitHub Actions workflow for my Go microservice -- I need tests, linting, Docker build, and Kubernetes deployment with ArgoCD
```

```
My CI pipeline takes 30 minutes and blocks the team -- analyze it and suggest optimizations
```

```
Secure my GitHub Actions pipelines -- I'm using static AWS credentials and unpinned action versions
```

```
Set up a DevSecOps pipeline with SAST, DAST, dependency scanning, and container vulnerability checks
```

```
I need to achieve OpenSSF Silver badge compliance -- what am I missing and how do I fix it?
```

**Key references by area:**

| Area | References |
|---|---|
| CI/CD & Pipelines | `best_practices.md`, `optimization.md`, `troubleshooting.md`, `cicd-github-actions.md`, `workflow-patterns.md`, `github-actions-patterns.yaml` |
| DevSecOps | `security.md`, `devsecops.md`, `devsecops-basics.md`, `security-hardening.md` |
| Infrastructure | `terraform-eks-module.tf`, `kubernetes-deployment.yaml`, `kubernetes-basics.md`, `docker-basics.md`, `docker-compose.md` |
| Cloud Platforms | `aws-overview.md`, `gcloud-platform.md`, `gcloud-services.md`, `cloudflare-workers-basics.md`, `cloudflare-workers-advanced.md`, `cloudflare-d1-kv.md`, `cloudflare-r2-storage.md` |
| Enterprise | `general.md`, `github.md`, `openssf-badge-silver.md`, `openssf-badge-gold.md`, `signed-releases.md`, `reproducible-builds.md` |
| Release | `local-release-workflow.md`, `version-alignment.md`, `authentication.md`, `pypi-publishing-with-doppler.md` |

**Shipped templates:**

| Template | Platform | What it generates |
|---|---|---|
| `node-ci.yml` | GitHub Actions / GitLab CI | Node.js CI with tests, lint, security scanning |
| `python-ci.yml` | GitHub Actions / GitLab CI | Python pipeline with pytest, coverage, PyPI |
| `go-ci.yml` | GitHub Actions / GitLab CI | Go pipeline with multi-platform builds |
| `docker-build.yml` | GitHub Actions / GitLab CI | Docker multi-stage with signing |
| `security-scan.yml` | GitHub Actions / GitLab CI | Comprehensive DevSecOps pipeline |
| `dco-check.yml` | GitHub Actions | DCO sign-off enforcement |

## Real-World Walkthrough

Your team is building a Python FastAPI application deployed on AWS EKS. You have been running tests manually and deploying from laptops. The CTO wants proper CI/CD before the next release, with security scanning to satisfy the compliance team, and it needs to be done this week.

You start with the basics:

```
Set up a complete CI/CD pipeline for our Python FastAPI project -- we use pytest, need 80% coverage, and deploy to AWS EKS
```

The skill starts with the decision tree and selects the Python CI template. The generated GitHub Actions workflow has six stages: fast feedback (ruff linting, mypy type checking -- under 1 minute), unit tests (pytest with coverage report, fail if below 80%), integration tests (against a PostgreSQL service container), security scanning (dependency audit, secret detection, SAST with CodeQL), Docker build (multi-stage Dockerfile, non-root user, pinned base image), and deployment (to EKS using OIDC authentication).

The OIDC setup is critical. You mention you currently use static AWS credentials stored as GitHub secrets:

```
We have AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY as repository secrets -- how do we switch to OIDC?
```

The skill produces the Terraform configuration for the OIDC identity provider and IAM role, the GitHub Actions workflow with `id-token: write` permissions and `aws-actions/configure-aws-credentials` using role assumption. You delete the static credentials from repository secrets. No more credential rotation, no more risk of leaked keys.

The security team wants scanning. The skill references `devsecops.md` and adds a security scanning job that runs in parallel with tests: Trivy for container vulnerabilities, TruffleHog for secret detection in the codebase, and CodeQL for SAST analysis. Findings above "high" severity block the pipeline.

Next, optimization. The initial pipeline takes 12 minutes:

```
The pipeline takes 12 minutes -- I need it under 5
```

You run the pipeline analyzer script: `python3 scripts/pipeline_analyzer.py --platform github --workflow .github/workflows/ci.yml`. It identifies three bottlenecks: no dependency caching (pip install takes 2 minutes every run), sequential test stages (unit and integration could run in parallel), and no path filters (documentation changes trigger the full pipeline).

The optimized pipeline adds pip caching (saves 2 minutes per run), runs unit tests, integration tests, and security scanning in parallel (saves 4 minutes), and adds path filters so changes to `docs/**` or `*.md` skip the full pipeline. The result: 4.5 minutes for the common case, 12 minutes only when the Dockerfile changes and requires a full build.

For deployment, the skill sets up a two-environment flow:

```
Set up dev and production deployments with approval gates
```

Pushes to `main` auto-deploy to the dev EKS cluster. The production deployment requires manual approval through a GitHub Environment protection rule, then runs smoke tests before completing. If smoke tests fail, the deployment rolls back automatically using the Kubernetes deployment rollback strategy.

Finally, release management:

```
Set up semantic-release for automated versioning and changelogs
```

The skill produces a `.releaserc.yml` configuration with conventional commits analysis, changelog generation, GitHub release creation, and Docker image tagging with the release version. Merge to `main` triggers a release if there are releasable commits (feat/fix/breaking). The CHANGELOG is generated automatically, and the GitHub Release includes links to the deployment.

By Thursday, you have: a CI pipeline that runs in under 5 minutes, security scanning that satisfies the compliance team, OIDC authentication with no static credentials, two-environment deployment with approval gates and automated rollback, and semantic-release for hands-off versioning. The CTO gets the demo Friday morning.

## Usage Scenarios

### Scenario 1: Setting up CI/CD for a new project

**Context:** You are starting a new Node.js project and need CI/CD from day one. You want tests, linting, Docker build, and deployment to work before writing any application code.

**You say:** "Set up GitHub Actions for a new TypeScript project -- I need lint, test, build, Docker image push, and deploy to Kubernetes"

**The skill provides:**
- Node.js CI template with TypeScript compilation, ESLint, Vitest
- Docker build template with multi-stage build, non-root user, pinned versions
- Kubernetes deployment manifest with HPA and health checks
- Caching configuration for npm dependencies
- Deployment workflow with dev/staging/production environments

**You end up with:** A complete CI/CD pipeline committed to the repository on day one, with all stages working before writing application logic.

### Scenario 2: Hardening pipeline security

**Context:** Your security team flagged that your CI pipelines use static AWS credentials, unpinned third-party actions, and have no security scanning. You need to fix all of this before the next audit.

**You say:** "Our security team wants us to harden our GitHub Actions -- we use static credentials, unpinned actions, and have no security scanning"

**The skill provides:**
- OIDC authentication setup (Terraform + workflow changes) to eliminate static credentials
- Action pinning script to replace version tags with commit SHAs
- Security scanning pipeline template (SAST, SCA, container scanning, secret detection)
- Minimal permission configuration for each workflow
- Branch protection rules for pipeline bypass prevention

**You end up with:** A hardened pipeline with no static credentials, all actions pinned to SHAs, comprehensive security scanning, and minimal permissions -- ready for the security audit.

### Scenario 3: Achieving OpenSSF badge compliance

**Context:** Your open source project needs OpenSSF Silver badge to meet a client's procurement requirements. You have no idea what criteria to meet.

**You say:** "We need OpenSSF Silver badge for our open source project -- what do we need and how do we get there?"

**The skill provides:**
- OpenSSF Silver badge criteria checklist with current compliance status
- Verification scripts for signed tags, coverage thresholds, review requirements, TLS enforcement
- GOVERNANCE.md, SECURITY_AUDIT.md, and CODE_OF_CONDUCT.md templates
- DCO sign-off enforcement workflow
- SPDX license header tools (verification and auto-addition)

**You end up with:** All Silver badge criteria met with evidence scripts that verify ongoing compliance, plus templates for required governance documentation.

### Scenario 4: Migrating from GitLab CI to GitHub Actions

**Context:** Your company is moving from GitLab to GitHub. You have 15 GitLab CI pipelines that need to be converted to GitHub Actions without disrupting deployments.

**You say:** "We're migrating from GitLab to GitHub -- I need to convert our Python and Docker CI pipelines to GitHub Actions"

**The skill provides:**
- Side-by-side templates for both platforms showing equivalent patterns
- Key syntax differences (stages vs jobs, variables vs env, artifacts vs actions/upload-artifact)
- GitLab-specific features and their GitHub Actions equivalents (services, includes, rules)
- Migration checklist for secrets, environment variables, and deployment targets
- Parallel running strategy for validating GitHub Actions before decommissioning GitLab CI

**You end up with:** Equivalent GitHub Actions workflows with the same stages, caching, security scanning, and deployment targets as the original GitLab CI pipelines.

## Ideal For

- **Teams setting up CI/CD for the first time** -- language-specific templates provide production-ready pipelines without the days of YAML trial and error
- **DevOps engineers hardening pipeline security** -- OIDC, pinned actions, security scanning, and minimal permissions in ready-to-use configurations
- **Open source maintainers pursuing OpenSSF compliance** -- badge criteria checklists, verification scripts, and governance templates reduce certification from weeks to days
- **Organizations standardizing across projects** -- shareable configurations and reusable workflow patterns prevent YAML copy-paste drift
- **Engineers optimizing slow pipelines** -- the pipeline analyzer script and optimization checklist identify specific bottlenecks with fixes

## Not For

- **Automating release workflows and orchestration** -- use [workflow-automation](../workflow-automation/) for cross-tool workflow orchestration
- **Docker container best practices and Dockerfile optimization** -- use [docker-containerization](../docker-containerization/) for deep Docker expertise
- **Git branching strategies and commit conventions** -- use [git-workflow](../git-workflow/) for branching models, conventional commits, and worktree management

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through a deep resource tree organized by concern area.

The **SKILL.md** body provides the decision trees (which template for which language/platform), quick-start checklists (security, optimization, new pipeline), architecture patterns (CI/CD flow, GitOps), and anti-patterns to avoid. This handles the most common questions without touching the references.

The **50+ reference documents** are organized into six areas: CI/CD platforms (GitHub Actions, GitLab CI patterns), DevSecOps (scanning, hardening, secrets), infrastructure (Terraform, Kubernetes, Docker), cloud platforms (AWS, GCP, Cloudflare), enterprise readiness (OpenSSF, signed releases, reproducible builds), and release management (semantic-release, version alignment, authentication).

The **templates** generate working YAML for both GitHub Actions and GitLab CI. They are not minimal starters -- they include caching, security scanning, proper permissions, and deployment stages. Each template is available for both platforms so teams can use whichever they need.

The **scripts** provide automation for analysis and verification: the pipeline analyzer identifies optimization opportunities, the CI health checker monitors pipeline status, and the security scripts verify badge criteria, coverage thresholds, signed tags, and license headers.

## Related Plugins

- **[Docker Containerization](../docker-containerization/)** -- Deep Docker expertise for Dockerfiles, multi-stage builds, and container optimization
- **[Git Workflow](../git-workflow/)** -- Git branching strategies, conventional commits, and worktree management
- **[Workflow Automation](../workflow-automation/)** -- Cross-tool workflow orchestration and release automation
- **[Cloud FinOps](../cloud-finops/)** -- Cloud cost optimization for the infrastructure your pipelines deploy to
- **[Code Review](../code-review/)** -- Multi-agent review for pipeline configuration and infrastructure code

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
