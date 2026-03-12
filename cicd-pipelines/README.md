# CI/CD Pipelines

> Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise release management.

## Overview

Modern software delivery demands robust, secure, and fast CI/CD pipelines. Yet pipeline configuration is notoriously error-prone -- YAML sprawl, secret leaks, slow builds, and fragile deployments plague most teams. This skill provides production-tested templates, optimization scripts, and security hardening patterns for every major CI/CD platform and cloud provider.

The CI/CD Pipelines skill spans the entire DevOps lifecycle: pipeline design for GitHub Actions and GitLab CI, Docker multi-stage builds, Kubernetes deployments with Helm and ArgoCD, Terraform infrastructure as code, security scanning (SAST/DAST/SCA), enterprise readiness with OpenSSF compliance, and automated semantic versioning. It includes ready-to-use workflow templates, analyzer scripts that identify optimization opportunities, and comprehensive reference documentation for troubleshooting.

Within the SkillStack collection, this skill pairs naturally with API Design (deploying API services), Code Review (CI-integrated code quality gates), and Consistency Standards (enforcing uniform pipeline conventions across repositories).

## What's Included

### References

**CI/CD and Pipeline Design:**
- `best_practices.md` -- Pipeline design patterns, testing strategies, and deployment workflows
- `optimization.md` -- Caching strategies, parallelization, and build performance tuning
- `troubleshooting.md` -- Common pipeline issues, debugging techniques, and platform-specific fixes
- `cicd-github-actions.md` -- GitHub Actions workflows, runners, and secrets management

**Security and DevSecOps:**
- `security.md` -- Secrets management, OIDC authentication, and supply chain security
- `devsecops.md` -- SAST, DAST, SCA, and container scanning implementation guide
- `devsecops-basics.md` -- Security best practices and shift-left security principles
- `security-hardening.md` -- TLS enforcement, input validation, and security headers

**Infrastructure and Cloud Platforms:**
- `terraform-eks-module.tf` -- Production EKS cluster Terraform module
- `kubernetes-deployment.yaml` -- Kubernetes deployment with HPA and ArgoCD annotations
- `kubernetes-basics.md` -- Core Kubernetes concepts: pods, services, deployments
- `docker-basics.md` -- Dockerfile best practices and multi-stage build patterns
- `docker-compose.md` -- Multi-container application orchestration
- `dockerfile-multistage.dockerfile` -- Multi-stage Dockerfile reference
- `aws-overview.md` -- AWS fundamentals, IAM, and core services
- `gcloud-platform.md` -- GCP overview and gcloud CLI usage
- `gcloud-services.md` -- GCP service catalog and selection guide
- `cloudflare-workers-basics.md` -- Edge computing with Cloudflare Workers
- `cloudflare-workers-advanced.md` -- Advanced Worker patterns and APIs
- `cloudflare-workers-apis.md` -- Cloudflare Workers API reference
- `cloudflare-d1-kv.md` -- Cloudflare D1 database and KV storage
- `cloudflare-r2-storage.md` -- Cloudflare R2 object storage
- `cloudflare-platform.md` -- Cloudflare platform overview
- `finops-basics.md` -- Cloud cost optimization and FinOps practices
- `browser-rendering.md` -- Browser rendering pipeline reference

**Enterprise Readiness:**
- `general.md` -- Universal enterprise readiness checklist
- `github.md` -- GitHub-specific enterprise requirements
- `openssf-badge-silver.md` -- OpenSSF Silver badge criteria
- `openssf-badge-gold.md` -- OpenSSF Gold badge criteria
- `signed-releases.md` -- Artifact signing and tag signing patterns
- `reproducible-builds.md` -- Deterministic build patterns
- `2fa-enforcement.md` -- Two-factor authentication enforcement
- `dco-implementation.md` -- Developer Certificate of Origin implementation
- `badge-display.md` -- Badge display and compliance documentation
- `sonarcloud.md` -- SonarCloud integration guide
- `dynamic-analysis.md` -- Dynamic analysis and fuzzing

**Release Management:**
- `local-release-workflow.md` -- Step-by-step local release process
- `workflow-patterns.md` -- Personal, team, and standalone release patterns
- `version-alignment.md` -- Git tags as single source of truth
- `authentication.md` -- SSH keys and GitHub CLI authentication
- `quick-start-guide.md` -- Release workflow quick start
- `solo-maintainer-guide.md` -- Solo maintainer release workflow
- `monorepo-support.md` -- Monorepo release management
- `adr-release-linking.md` -- Linking ADRs to releases
- `pypi-publishing-with-doppler.md` -- PyPI publishing with Doppler secrets
- `python-projects-nodejs-semantic-release.md` -- semantic-release for Python projects
- `test-invocation.md` -- Test invocation patterns
- `resources.md` -- Additional resources and links
- `2025-updates.md` -- Latest platform updates and changes

**Additional:**
- `github-actions-patterns.yaml` -- GitHub Actions reusable workflow patterns
- `go.md` -- Go project CI/CD patterns
- `branch-coverage.md` -- Branch coverage analysis guide

### Templates

**GitHub Actions:**
- `github-actions/node-ci.yml` -- Complete Node.js CI/CD with security scanning
- `github-actions/python-ci.yml` -- Python pipeline with pytest, coverage, and PyPI publishing
- `github-actions/go-ci.yml` -- Go pipeline with multi-platform builds
- `github-actions/docker-build.yml` -- Docker build with multi-platform support and signing
- `github-actions/security-scan.yml` -- Comprehensive DevSecOps scanning pipeline
- `github-actions/dco-check.yml` -- Developer Certificate of Origin enforcement

**GitLab CI:**
- `gitlab-ci/node-ci.yml` -- GitLab CI Node.js pipeline
- `gitlab-ci/python-ci.yml` -- Python pipeline with parallel testing
- `gitlab-ci/go-ci.yml` -- Go pipeline with Kubernetes deployment
- `gitlab-ci/docker-build.yml` -- Docker build with DinD and multi-arch support
- `gitlab-ci/security-scan.yml` -- DevSecOps with GitLab security templates

**Release Configuration:**
- `releaserc.yml` -- semantic-release configuration
- `releaserc-pypi-doppler.json` -- PyPI release config with Doppler
- `package.json` -- Node.js package for release automation
- `shareable-config/` -- Shareable semantic-release configuration package
- `doppler.yaml` -- Doppler secrets management configuration
- `github-workflow.yml` -- General GitHub workflow template

**Enterprise Templates:**
- `GOVERNANCE.md` -- Project governance documentation template
- `ARCHITECTURE.md` -- Technical architecture documentation template
- `CODE_OF_CONDUCT.md` -- Contributor Covenant v2.1
- `SECURITY_AUDIT.md` -- Security self-audit template
- `BADGE_EXCEPTIONS.md` -- Badge criteria exception documentation
- `ROADMAP.md` -- Project roadmap template

### Scripts

**Pipeline Analysis:**
- `pipeline_analyzer.py` -- Analyze workflows for optimization opportunities
- `ci_health.py` -- Check pipeline health status and identify issues
- `validate-devops-skill.sh` -- Validate DevOps configurations

**Security and Compliance:**
- `verify-badge-criteria.sh` -- OpenSSF Badge criteria verification
- `check-coverage-threshold.sh` -- Statement coverage threshold validation
- `check-branch-coverage.sh` -- Branch coverage analysis
- `verify-signed-tags.sh` -- Git tag signature verification
- `verify-review-requirements.sh` -- PR review requirements check
- `check-tls-minimum.sh` -- TLS 1.2+ enforcement verification
- `verify-spdx-headers.sh` -- SPDX license header verification
- `add-spdx-headers.sh` -- Add SPDX headers to source files
- `verify-reproducible-build.sh` -- Reproducible build verification
- `analyze-bus-factor.sh` -- Bus factor analysis for contributor risk

**Infrastructure:**
- `cloudflare_deploy.py` -- Cloudflare Worker deployment automation
- `docker_optimize.py` -- Dockerfile analysis and optimization recommendations

**Release Management:**
- `init_project.sh` -- Initialize semantic-release for a project
- `init_user_config.sh` -- Create user-level release configuration
- `create_org_config.sh` -- Create organization-level release configuration
- `generate-adr-notes.mjs` -- Auto-link ADRs in release notes

## Key Features

- **Multi-platform pipelines**: Ready-to-use templates for GitHub Actions, GitLab CI, and Jenkins
- **Language-specific CI**: Optimized workflows for Node.js, Python, and Go projects
- **Security-first DevSecOps**: Integrated SAST, DAST, SCA, and container vulnerability scanning
- **Infrastructure as Code**: Terraform modules, Kubernetes manifests, and Helm chart patterns
- **Enterprise compliance**: OpenSSF badge criteria verification and automated compliance checks
- **Pipeline optimization**: Analyzer scripts that identify caching, parallelization, and speed improvements
- **Automated releases**: semantic-release configuration with changelog generation and artifact signing
- **Multi-cloud support**: AWS, GCP, Azure, and Cloudflare deployment patterns

## Usage Examples

**Create a CI pipeline for a new project:**
```
Set up a GitHub Actions CI/CD pipeline for a Node.js project with
linting, testing, security scanning, and Docker deployment.
```
Expected output: Complete workflow YAML with caching, matrix testing, security scanning stage, Docker build with multi-platform support, and deployment to staging/production with approval gates.

**Optimize a slow pipeline:**
```
Our CI pipeline takes 25 minutes. Analyze it and suggest optimizations.
```
Expected output: Analysis of bottlenecks, specific caching recommendations, parallelization opportunities, path-based filtering suggestions, and estimated time savings for each improvement.

**Add security scanning to an existing pipeline:**
```
Add DevSecOps security scanning to our GitLab CI pipeline, including
dependency scanning, SAST, and container scanning.
```
Expected output: GitLab CI configuration with security scanning stages, vulnerability thresholds, and reporting configuration.

**Set up Kubernetes deployment with GitOps:**
```
Create a Kubernetes deployment for our API with ArgoCD GitOps,
including HPA, health checks, and canary deployments.
```
Expected output: Kubernetes manifests, ArgoCD application definition, HPA configuration, and rollback strategy.

**Achieve OpenSSF compliance:**
```
What do we need to achieve OpenSSF Silver badge compliance for our
open source project?
```
Expected output: Gap analysis against Silver badge criteria, specific actions needed, and verification scripts to validate compliance.

## Quick Start

1. **Identify your platform** -- GitHub Actions or GitLab CI
2. **Pick a language template** -- Copy from `templates/github-actions/` or `templates/gitlab-ci/`
3. **Add security scanning** -- Include the `security-scan.yml` template
4. **Optimize performance** -- Run `python scripts/pipeline_analyzer.py --workflow .github/workflows/ci.yml`
5. **Set up releases** -- Run `bash scripts/init_project.sh` for semantic versioning
6. **Harden security** -- Review `references/security.md` and implement OIDC authentication
7. **Validate compliance** -- Run `bash scripts/verify-badge-criteria.sh` for enterprise readiness

## Related Skills

- **[API Design](../api-design/)** -- Design the APIs that your pipelines will build and deploy
- **[Code Review](../code-review/)** -- Integrate code quality gates into your CI pipeline
- **[Consistency Standards](../consistency-standards/)** -- Enforce uniform pipeline conventions across repos

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 34 production-grade skills for Claude Code.
