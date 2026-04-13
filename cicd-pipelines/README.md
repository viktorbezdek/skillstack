# CI/CD Pipelines

> **v1.1.23** | DevOps & Infrastructure | 25 iterations

Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise release management.

## What Problem Does This Solve

Engineering teams building CI/CD pipelines from scratch repeatedly make the same costly mistakes: hardcoding secrets instead of using OIDC, building monolithic 45-minute pipelines instead of parallelized stages, using `FROM node:latest` in production Dockerfiles, and having no rollback strategy when deployments fail. Keeping pipelines consistent across GitHub Actions and GitLab CI while meeting security requirements (OpenSSF, SLSA, supply chain integrity) takes patterns most teams learn only after incidents.

This skill consolidates production-grade pipeline design, DevSecOps scanning, infrastructure automation, Kubernetes orchestration, and release management into a single reference with ready-to-use templates for both GitHub Actions and GitLab CI, analysis scripts that identify optimization opportunities, and compliance verification tools for OpenSSF badge criteria.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install cicd-pipelines@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention CI/CD topics, or you can invoke it explicitly with `Use the cicd-pipelines skill to ...`.

## What's Inside

This is a large single-skill plugin organized across six domains with 50+ reference files, templates, and scripts:

### References (50+ files across 5 categories)

| Category | Coverage |
|---|---|
| **CI/CD & Pipeline Design** | Pipeline design patterns, caching strategies, parallelization, build performance optimization, troubleshooting guide, GitHub Actions workflows and runners |
| **Security & DevSecOps** | Secrets management with OIDC, supply chain security, SAST/DAST/SCA scanning, container vulnerability scanning, security hardening (TLS, input validation, headers) |
| **Infrastructure & Cloud** | Terraform EKS modules, Kubernetes deployments with HPA, Docker basics and multi-stage builds, Docker Compose, AWS/GCP/Cloudflare platform overviews |
| **Enterprise Readiness** | OpenSSF badge criteria (silver and gold), signed releases, reproducible builds, DCO enforcement, GitHub-specific enterprise requirements |
| **Release Management** | Local release workflow, workflow patterns (personal/team/standalone), version alignment with git tags as SSoT, semantic-release configuration |

### Templates

| Platform | Templates Available |
|---|---|
| **GitHub Actions** | Node.js CI, Python CI, Go CI, Docker build (multi-platform + signing), security scan, DCO check |
| **GitLab CI** | Node.js CI, Python CI, Go CI, Docker build (DinD + multi-arch), security scan |
| **Release** | semantic-release config, package.json for releases, shareable semantic-release config |
| **Enterprise** | Governance documentation, architecture template, Code of Conduct, security audit template |

### Scripts

| Category | Scripts |
|---|---|
| **Pipeline Analysis** | Pipeline analyzer (optimization opportunities), CI health checker, DevOps config validator |
| **Security & Compliance** | OpenSSF badge verifier, coverage threshold checker, branch coverage analyzer, signed tag verifier, PR review requirements checker, TLS enforcement checker, SPDX header verifier and adder |
| **Infrastructure** | Cloudflare Worker deployment, Dockerfile analysis and optimization |
| **Release** | Project initialization for semantic-release, user config creator, org config creator, ADR-to-release-notes generator |

## Usage Scenarios

**1. "Set up CI/CD for my Node.js project from scratch."**
Start with the decision tree in the SKILL.md to select the right template (`templates/github-actions/node-ci.yml` or `templates/gitlab-ci/node-ci.yml`). The template includes fast feedback (lint + format in under 1 minute), unit tests, integration tests, build artifacts, and deployment stages. Apply the quick-wins checklist: add dependency caching (50-90% faster), use `npm ci` instead of `npm install`, add path filters, and enable concurrency cancellation.

**2. "My builds take 45 minutes -- how do I speed them up?"**
Run `python3 scripts/pipeline_analyzer.py --platform github --workflow .github/workflows/ci.yml` to identify bottlenecks. Common fixes: remove unnecessary `needs` dependencies to enable parallel jobs, add caching for dependencies and Docker layers, use path-based triggers to skip irrelevant runs, implement test sharding, and add job timeouts to prevent hung builds. The optimization reference covers all strategies with measured impact.

**3. "Switch from static AWS credentials to OIDC in our GitHub Actions."**
The security reference provides the exact OIDC setup: configure `permissions: id-token: write` and `contents: read`, use `aws-actions/configure-aws-credentials@v4` with `role-to-assume` pointing to your IAM role. Pin the action to a commit SHA, not a tag. The essential security checklist covers the remaining items: secret scanning, vulnerability scanning, branch protection, and separating test from deploy workflows.

**4. "We need to pass OpenSSF badge criteria for our open-source project."**
Run `scripts/verify-badge-criteria.sh` against your repository. The silver and gold badge references detail every criterion. Use the enterprise templates for governance documentation (`GOVERNANCE.md`), architecture documentation (`ARCHITECTURE.md`), and security audit (`SECURITY_AUDIT.md`). The signed releases reference covers artifact signing with Cosign and SLSA provenance.

**5. "Set up GitOps with ArgoCD for our Kubernetes deployments."**
The architecture patterns section shows the GitOps flow: App Repo pushes through CI to Config Repo, ArgoCD watches Config Repo and syncs to the Kubernetes cluster in a continuous loop. The Kubernetes deployment reference includes HPA configuration, security contexts (non-root, read-only filesystem), resource limits, and liveness/readiness probes. Use the platform selection guide to choose between EKS, AKS, and GKE based on your requirements.

## When to Use / When NOT to Use

**Use when:**
- Creating or optimizing CI/CD pipelines (GitHub Actions, GitLab CI)
- Implementing security scanning and DevSecOps practices
- Setting up Kubernetes deployments, Terraform modules, or GitOps workflows
- Configuring semantic versioning and automated releases
- Preparing for OpenSSF compliance or enterprise readiness audits
- Debugging pipeline failures or flaky tests

**Do NOT use when:**
- Automating release workflows or orchestration logic -- use [workflow-automation](../workflow-automation/) instead
- Writing Dockerfiles or optimizing container images -- use [docker-containerization](../docker-containerization/) instead
- Managing git branches, commits, or merge strategies -- use [git-workflow](../git-workflow/) instead

## Related Plugins

- **[Cloud FinOps](../cloud-finops/)** -- Cloud cost management across AWS, Azure, GCP, AI workloads, and Kubernetes
- **[Docker Containerization](../docker-containerization/)** -- Docker basics, multi-stage builds, Compose orchestration
- **[Git Workflow](../git-workflow/)** -- Conventional commits, branch management, worktree operations
- **[Workflow Automation](../workflow-automation/)** -- CI/CD orchestration, multi-agent parallel execution, release automation

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
