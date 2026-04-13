# CI/CD Pipelines

> **v1.1.23** | Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, security scanning, and enterprise release management.
> 1 skill | 52 references | 15 templates | 21 scripts | 13 trigger evals, 3 output evals

## The Problem

CI/CD pipelines start as simple build-and-test workflows and grow into critical infrastructure that nobody fully understands. A typical trajectory: the original author writes a 50-line GitHub Actions workflow. Over months, other engineers bolt on security scanning, Docker builds, Kubernetes deployments, and release automation. The workflow balloons to 500 lines of YAML with hardcoded secrets, no caching, no parallelization, and implicit dependencies between jobs. Builds that should take 3 minutes take 30.

Security is the silent crisis. Teams hardcode API keys because "we'll fix it later." They use `:latest` tags in Dockerfiles because pinning versions feels tedious. They run containers as root because the non-root alternative requires fixing file permissions. Script injection vulnerabilities lurk in workflows that interpolate user input directly. Each shortcut is a deferred incident, and the compounding effect is a pipeline that is both slow and insecure.

The problem scales with platform diversity. A team using GitHub Actions for CI, Terraform for infrastructure, Kubernetes for orchestration, and ArgoCD for GitOps deployment needs expertise across four platforms. Each has its own configuration syntax, secret management approach, authentication model, and debugging workflow. Without unified guidance, teams copy-paste YAML from Stack Overflow, each snippet introducing its own assumptions about runner environment, secret availability, and network access. The result is a pipeline that works on the author's machine, fails on CI, and nobody can debug because nobody understands the whole system.

## The Solution

This plugin provides a unified CI/CD skill covering pipeline design, DevOps automation, infrastructure as code, container orchestration, security scanning, and enterprise release management across all major platforms. It ships with 52 reference files covering GitHub Actions, GitLab CI, Jenkins, Terraform, Kubernetes, Docker, Cloudflare Workers, AWS, GCP, DevSecOps, and release management. Fifteen production-ready templates provide starting points for Node.js, Python, Go, Docker, and security scanning pipelines on both GitHub Actions and GitLab CI. Twenty-one scripts automate pipeline analysis, security verification, coverage checking, and release initialization.

The skill covers the entire DevOps lifecycle: creating pipelines from templates, optimizing slow builds (caching, parallelization, path filters), securing pipelines (OIDC authentication, secret management, supply chain security), containerizing applications (multi-stage Docker builds, Kubernetes deployments), implementing GitOps (ArgoCD, Flux), and managing releases (semantic versioning, signed artifacts, SLSA provenance). It provides concrete, copy-pasteable configurations rather than abstract advice.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| 30-minute builds with no caching or parallelization | Dependency caching (50-90% faster), parallel jobs, path filters to skip unnecessary runs |
| Hardcoded secrets in workflow YAML | OIDC authentication to cloud providers; secrets in proper managers (Vault, AWS SM) |
| `:latest` tags in production Dockerfiles | Pinned versions with SHA digests; multi-stage builds with non-root users |
| Script injection via `${{ github.event.* }}` in run blocks | Environment variable sanitization pattern preventing injection |
| Copy-pasted YAML across 20 repos with drift | Reusable workflows, Helm charts, Kustomize bases, shared Terraform modules |
| No rollback strategy -- manual intervention on deploy failure | Blue/green, canary with automated rollback, ArgoCD auto-revert |

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install cicd-pipelines@skillstack
```

### Verify installation

After installing, test with:

```
Create a GitHub Actions CI pipeline for my Node.js monorepo with unit tests, linting, and Docker builds
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `I need a CI/CD pipeline for a Python FastAPI app deployed to AWS ECS`
3. The skill generates a GitHub Actions workflow with lint, test, build, push to ECR, and ECS deploy stages
4. Optimize: `My builds take 20 minutes -- help me add caching and parallelization`
5. Secure: `Add OIDC authentication to AWS and dependency vulnerability scanning`

---

## System Overview

```
+-----------------------------------------------------------------------+
|                        cicd-pipelines skill                            |
+-----------------------------------------------------------------------+
|                                                                        |
|  Pipeline Design          Security & Compliance     Infrastructure     |
|  +------------------+     +------------------+     +----------------+  |
|  | GitHub Actions   |     | DevSecOps        |     | Terraform      |  |
|  | GitLab CI        |     | SAST/DAST/SCA    |     | Kubernetes     |  |
|  | Jenkins          |     | OIDC Auth        |     | Docker         |  |
|  | Optimization     |     | Supply Chain     |     | Helm/Kustomize |  |
|  +------------------+     | OpenSSF Badge    |     | ArgoCD/Flux    |  |
|                           +------------------+     +----------------+  |
|                                                                        |
|  Release Management       Cloud Platforms          Enterprise          |
|  +------------------+     +------------------+     +----------------+  |
|  | semantic-release  |     | AWS              |     | Governance     |  |
|  | Signing/Provenance|     | GCP              |     | OpenSSF Silver |  |
|  | Changelog         |     | Cloudflare       |     | OpenSSF Gold   |  |
|  +------------------+     +------------------+     +----------------+  |
|                                                                        |
|  Templates (15)  |  Scripts (21)  |  References (52)                   |
+-----------------------------------------------------------------------+
```

## What's Inside

| Component | Type | Count |
|---|---|---|
| `cicd-pipelines` | Skill | 1 comprehensive skill |
| References | CI/CD, security, infrastructure, cloud, enterprise | 52 files |
| Templates | GitHub Actions, GitLab CI, release config, enterprise docs | 15 files |
| Scripts | Analysis, security, coverage, release, infrastructure | 21 files |

### Reference Categories

| Category | Key References |
|---|---|
| **CI/CD & Pipeline** | `best_practices.md`, `optimization.md`, `troubleshooting.md`, `cicd-github-actions.md` |
| **Security & DevSecOps** | `security.md`, `devsecops.md`, `devsecops-basics.md`, `security-hardening.md`, `2fa-enforcement.md` |
| **Infrastructure** | `terraform-eks-module.tf`, `kubernetes-basics.md`, `kubernetes-deployment.yaml`, `docker-basics.md`, `docker-compose.md` |
| **Cloud Platforms** | `aws-overview.md`, `gcloud-platform.md`, `gcloud-services.md`, `cloudflare-workers-*.md` (6 files) |
| **Enterprise** | `general.md`, `github.md`, `openssf-badge-silver.md`, `openssf-badge-gold.md`, `signed-releases.md`, `reproducible-builds.md` |
| **Release Management** | `local-release-workflow.md`, `workflow-patterns.md`, `version-alignment.md`, `pypi-publishing-with-doppler.md` |

### Templates

| Template | Platform | Purpose |
|---|---|---|
| `github-actions/node-ci.yml` | GitHub | Node.js CI/CD with security scanning |
| `github-actions/python-ci.yml` | GitHub | Python with pytest, coverage, PyPI |
| `github-actions/go-ci.yml` | GitHub | Go with multi-platform builds |
| `github-actions/docker-build.yml` | GitHub | Docker multi-platform with signing |
| `github-actions/security-scan.yml` | GitHub | Comprehensive DevSecOps pipeline |
| `github-actions/dco-check.yml` | GitHub | DCO sign-off enforcement |
| `gitlab-ci/node-ci.yml` | GitLab | Node.js pipeline |
| `gitlab-ci/python-ci.yml` | GitLab | Python with parallel testing |
| `gitlab-ci/go-ci.yml` | GitLab | Go with Kubernetes deployment |
| `gitlab-ci/docker-build.yml` | GitLab | Docker with DinD, multi-arch |
| `gitlab-ci/security-scan.yml` | GitLab | DevSecOps with GitLab templates |
| `releaserc.yml` | Any | semantic-release configuration |
| `GOVERNANCE.md` | Any | Project governance documentation |
| `SECURITY_AUDIT.md` | Any | Security self-audit template |

### Scripts

| Script | Purpose |
|---|---|
| `pipeline_analyzer.py` | Analyze workflows for optimization opportunities |
| `ci_health.py` | Check pipeline status and identify issues |
| `verify-badge-criteria.sh` | OpenSSF Badge verification |
| `check-coverage-threshold.sh` | Statement coverage validation |
| `check-branch-coverage.sh` | Branch coverage analysis |
| `verify-signed-tags.sh` | Git tag signature verification |
| `docker_optimize.py` | Dockerfile analysis and optimization |
| `cloudflare_deploy.py` | Cloudflare Worker deployments |
| `init_project.sh` | Initialize semantic-release for project |

### Component Spotlights

#### cicd-pipelines (skill)

**What it does:** Activates when you need to create, optimize, secure, or debug CI/CD pipelines across any platform. Covers the full DevOps lifecycle from initial pipeline creation through enterprise compliance and release management.

**Input -> Output:** Pipeline requirements (language, platform, deployment target, security needs) -> Complete workflow YAML, Dockerfile, Kubernetes manifests, Terraform modules, and security configurations.

**When to use:**
- Creating new CI/CD workflows (GitHub Actions, GitLab CI, Jenkins)
- Optimizing slow builds (caching, parallelization, path filters)
- Securing pipelines (OIDC, secret management, vulnerability scanning)
- Containerizing applications (Docker, Kubernetes, Helm)
- Implementing GitOps (ArgoCD, Flux)
- Setting up release automation (semantic-release, signing)
- Enterprise readiness assessment (OpenSSF compliance)

**When NOT to use:**
- Automating release orchestration workflows -> use `workflow-automation`
- Writing Dockerfiles from scratch -> use `docker-containerization`
- Managing git branches and commits -> use `git-workflow`

**Try these prompts:**

```
Create a GitHub Actions pipeline for a Python monorepo with 3 packages -- each needs separate testing but shared Docker builds
```

```
My CI takes 25 minutes -- analyze it and suggest optimizations. Here's my workflow file: [paste]
```

```
Secure my pipeline: add OIDC auth to AWS, enable Dependabot, add container scanning, and pin all action versions to SHAs
```

```
Set up ArgoCD GitOps for my Kubernetes cluster with automatic rollback on failed health checks
```

```
I need to achieve OpenSSF Silver badge for my open-source project -- what's missing and how do I fix each item?
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Set up CI" | "Create a GitHub Actions pipeline for a Go microservice deployed to EKS with Terraform-managed infrastructure" |
| "Make it faster" | "My GitHub Actions workflow takes 18 minutes. I'm using npm install instead of npm ci, no caching, and tests run sequentially. Help me optimize." |
| "Add security" | "Add OIDC authentication to AWS, pin all GitHub Actions to SHA, enable CodeQL scanning, and add Trivy container scanning to my Docker build workflow" |
| "Deploy my app" | "Set up blue/green deployment to AWS ECS with automatic rollback if the health check fails within 5 minutes of deploy" |

### Structured Prompt Templates

**For new pipeline creation:**
```
Create a [GitHub Actions/GitLab CI] pipeline for a [language] [project type]. It should: lint, test with [test framework], build [artifact type], deploy to [target]. Security requirements: [list]. Caching: [yes/no].
```

**For pipeline optimization:**
```
Optimize this CI workflow: [paste YAML]. Current build time: [N] minutes. Target: [M] minutes. I suspect the bottleneck is [area].
```

**For security hardening:**
```
Harden the security of my [platform] pipeline. Current state: [describe]. I need: [OIDC/scanning/signing/compliance]. My cloud provider is [provider]. Target compliance: [OpenSSF Silver/Gold/custom].
```

### Prompt Anti-Patterns

- **Platform-agnostic requests**: "Create a CI pipeline" -- the skill needs to know GitHub Actions vs GitLab CI vs Jenkins because their configuration, runners, and capabilities differ fundamentally. Always specify the platform.
- **Optimizing without diagnosis**: "Make my build faster" -- optimization requires understanding current bottlenecks. Share the workflow file or describe the current state (build time, what runs, what's cached).
- **Security as a separate phase**: "First build the pipeline, then we'll add security" -- OIDC auth, secret management, and supply chain security affect pipeline structure. Design them together.

## Real-World Walkthrough

**Starting situation:** You maintain a Node.js API deployed to AWS ECS. The current CI is a single GitHub Actions workflow that runs `npm install`, `npm test`, builds a Docker image, pushes to ECR, and deploys to ECS. It takes 22 minutes, uses hardcoded AWS credentials, runs Docker as root, and has no security scanning.

**Step 1: Analyze current pipeline.** You share your workflow and ask: "This takes 22 minutes and I know it's insecure. Help me fix everything." The skill runs through a quick-wins checklist: no dependency caching (saves 2-5 minutes), `npm install` instead of `npm ci` (saves 30 seconds + reproducibility), sequential lint and test that could run parallel (saves 3-4 minutes), no path filters (pipeline runs on documentation changes), and no concurrency cancellation (duplicate runs waste resources).

**Step 2: Optimize build time.** The skill restructures the workflow: dependency caching with `actions/cache` for `node_modules`, parallel lint and test jobs, path filters to skip CI on `docs/**` and `*.md` changes, and `concurrency` group to cancel in-progress runs when new commits push. The Docker build adds layer caching with `docker/build-push-action` and build cache export. Estimated new time: 7-8 minutes.

**Step 3: Security hardening.** The skill replaces hardcoded AWS credentials with OIDC:
```yaml
permissions:
  id-token: write
  contents: read
steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::123456789:role/GitHubActionsRole
      aws-region: us-east-1
```
It pins all actions to SHA commits instead of version tags, adds Trivy container scanning before ECR push, adds CodeQL for code analysis, and adds `npm audit --audit-level=high` to the test stage.

**Step 4: Docker hardening.** The Dockerfile gets a multi-stage build (builder stage with dev dependencies, production stage with only runtime), a non-root USER instruction, pinned base image versions with SHA digests, and a `.dockerignore` to reduce build context.

**Step 5: Deployment safety.** The skill adds a health check after ECS deploy that polls the `/health` endpoint for 5 minutes. If it fails, the deploy automatically rolls back to the previous task definition. A manual approval gate is added between staging and production environments.

**Step 6: Release automation.** The skill sets up semantic-release with conventional commits: `feat:` commits trigger minor version bumps, `fix:` commits trigger patch bumps, `BREAKING CHANGE:` triggers major bumps. Releases are signed with Cosign and include SLSA provenance metadata.

**Final result:** Build time dropped from 22 minutes to 8 minutes. Zero hardcoded credentials. Container runs as non-root with no known vulnerabilities. Automated rollback on failed deploys. Signed releases with provenance.

**Gotchas discovered:** The OIDC trust policy needed the specific repository and branch conditions -- a permissive policy would let any GitHub Actions workflow assume the role. Also, Trivy scanning caught a critical CVE in the base Node.js image that had been there for 6 months.

## Usage Scenarios

### Scenario 1: Setting up CI for a Python monorepo

**Context:** You have a Python monorepo with 5 packages, shared dependencies, and need separate test suites per package but unified coverage reporting.

**You say:** "Create GitHub Actions CI for my Python monorepo with 5 packages. Each needs its own test suite but I want unified coverage and a single Docker build."

**The skill provides:**
- Matrix strategy running tests for each package in parallel
- Shared dependency caching with hash-based keys
- Coverage collection per package, merged in a final job
- Single Dockerfile with multi-stage build pulling from monorepo root
- Path-based triggers so package A changes only run package A tests

**You end up with:** A workflow that runs 5 test suites in parallel (total time = slowest package, not sum), with unified coverage reporting and efficient Docker builds.

### Scenario 2: Achieving OpenSSF Silver badge

**Context:** Your open-source project wants to earn the OpenSSF Silver badge for credibility with enterprise users.

**You say:** "I need to achieve OpenSSF Silver badge for my project. Run the assessment and tell me what's missing."

**The skill provides:**
- Gap analysis against Silver badge criteria using `verify-badge-criteria.sh`
- Specific fixes for each missing criterion (signed commits, branch protection, security policy, vulnerability disclosure)
- Template files for GOVERNANCE.md, SECURITY_AUDIT.md, CODE_OF_CONDUCT.md
- Workflow additions for DCO checking and signed releases

**You end up with:** A checklist with every Silver badge criterion addressed, the necessary template files committed, and CI workflows updated to enforce the requirements automatically.

### Scenario 3: Implementing GitOps with ArgoCD

**Context:** Your team deploys to Kubernetes by running `kubectl apply` from laptops. You need a proper GitOps workflow.

**You say:** "Move our Kubernetes deployments from kubectl-apply-from-laptops to ArgoCD GitOps with automatic sync and rollback."

**The skill provides:**
- ArgoCD Application manifests for each service
- Config repo structure separating app code from deployment config
- CI pipeline that updates image tags in the config repo after successful builds
- ArgoCD sync policy with auto-healing and automatic rollback on degraded health
- RBAC configuration for team-based access control

**You end up with:** A GitOps pipeline where merging to the config repo triggers deployment, ArgoCD monitors cluster state, and any drift from the desired state is automatically corrected.

---

## Decision Logic

**GitHub Actions vs GitLab CI vs Jenkins?**

GitHub Actions for teams already on GitHub who want tight integration with PRs, Issues, and the marketplace. GitLab CI for teams using GitLab who want built-in container registry, security scanning, and deployment environments. Jenkins for teams with complex pipeline requirements, existing Jenkins infrastructure, or need to run on self-hosted hardware with specific constraints.

**When to use reusable workflows vs composite actions vs shared Terraform modules?**

Reusable workflows for entire CI/CD pipelines that multiple repos need identically. Composite actions for individual steps that are shared (e.g., "setup our dev environment"). Terraform modules for infrastructure that follows a standard pattern across environments.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Hardcoded secrets in workflow | Credentials visible in logs or repo history | Rotate immediately; switch to OIDC for cloud auth; use secrets manager for others |
| Script injection via event data | Attacker can execute arbitrary commands via PR title/body | Never use `${{ github.event.* }}` in `run:` blocks; assign to env vars first |
| `:latest` tags in production | Unexpected container behavior after upstream image update | Pin specific versions with SHA digests; automate base image update PRs |
| No rollback strategy | Failed deploy requires manual intervention at 2 AM | Implement blue/green or canary with health check-based automatic rollback |
| YAML copy-paste drift | 20 repos with slightly different workflows; fixes applied unevenly | Extract to reusable workflows; version them in a shared repo |

## Ideal For

- **Backend engineers setting up CI/CD from scratch** who need production-ready templates instead of starting from an empty YAML file
- **DevOps engineers optimizing slow pipelines** who need systematic analysis and proven optimization patterns
- **Security engineers hardening build pipelines** who need OIDC, supply chain security, vulnerability scanning, and compliance checklists
- **Platform teams standardizing across repositories** who need reusable workflows, shared configs, and enterprise governance templates
- **Open-source maintainers seeking compliance badges** who need gap analysis and fixes for OpenSSF Silver and Gold criteria

## Not For

- **Release orchestration workflows** -- for complex release processes with approvals and notifications, use `workflow-automation`
- **Writing Dockerfiles from scratch** -- for Docker-specific patterns, multi-stage builds, and container optimization, use `docker-containerization`
- **Git branching strategies** -- for branch management, commit conventions, and merge strategies, use `git-workflow`

## Related Plugins

- **docker-containerization** -- Container-specific patterns that complement pipeline Docker build stages
- **git-workflow** -- Branch management and commit conventions that feed into CI triggers
- **workflow-automation** -- Release orchestration and approval workflows
- **code-review** -- Code quality gates that integrate with CI pipeline checks
- **cloud-finops** -- Cost optimization for CI/CD infrastructure (runners, build minutes, storage)
- **api-design** -- API deployment pipelines

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
