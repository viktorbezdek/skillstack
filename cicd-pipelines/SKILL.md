---
name: cicd-pipelines
description: "Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise release management. Use for: GitHub Actions, GitLab CI, Jenkins pipelines, Terraform/CloudFormation IaC, Kubernetes/Docker deployments, GitOps (ArgoCD/Flux), DevSecOps security scanning (SAST/DAST/SCA), semantic versioning, enterprise readiness assessment, and cloud platform deployments (AWS, Azure, GCP, Cloudflare)."
license: MIT
---

# CI/CD Pipelines - Comprehensive DevOps Skill

A unified skill for CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, security scanning, and enterprise release management across all major platforms.

## When to Use This Skill

Use this skill when:

### CI/CD Pipeline Development
- Creating new CI/CD workflows (GitHub Actions, GitLab CI, Jenkins)
- Debugging pipeline failures or flaky tests
- Optimizing slow builds or test suites
- Implementing caching strategies
- Setting up deployment workflows
- Implementing matrix builds or test sharding
- Configuring multi-environment deployments

### DevSecOps & Security
- Securing pipelines (secrets, OIDC, supply chain)
- Implementing security scanning (SAST, DAST, SCA)
- Container vulnerability scanning
- Secret detection and management
- Enterprise readiness assessment (OpenSSF compliance)

### Infrastructure as Code
- Terraform module development
- CloudFormation/CDK templates
- Kubernetes manifests and Helm charts
- GitOps workflows (ArgoCD, Flux)

### Container Orchestration
- Docker multi-stage builds
- Kubernetes deployments
- Container registry management
- Service mesh configuration

### Release Management
- Semantic versioning automation
- Changelog generation
- GitHub/GitLab release creation
- Artifact signing and provenance

## Quick Start

### 1. Creating a New Pipeline

**Decision tree:**
```
What are you building?
+-- Node.js/Frontend --> templates/github-actions/node-ci.yml | templates/gitlab-ci/node-ci.yml
+-- Python --> templates/github-actions/python-ci.yml | templates/gitlab-ci/python-ci.yml
+-- Go --> templates/github-actions/go-ci.yml | templates/gitlab-ci/go-ci.yml
+-- Docker Image --> templates/github-actions/docker-build.yml | templates/gitlab-ci/docker-build.yml
+-- Security Scanning --> templates/github-actions/security-scan.yml | templates/gitlab-ci/security-scan.yml
```

**Basic pipeline structure:**
```yaml
# 1. Fast feedback (lint, format) - <1 min
# 2. Unit tests - 1-5 min
# 3. Integration tests - 5-15 min
# 4. Build artifacts
# 5. E2E tests (optional, main branch only) - 15-30 min
# 6. Deploy (with approval gates)
```

### 2. Optimizing Pipeline Performance

**Quick wins checklist:**
- [ ] Add dependency caching (50-90% faster builds)
- [ ] Remove unnecessary `needs` dependencies
- [ ] Add path filters to skip unnecessary runs
- [ ] Use `npm ci` instead of `npm install`
- [ ] Add job timeouts to prevent hung builds
- [ ] Enable concurrency cancellation for duplicate runs

**Analyze existing pipeline:**
```bash
# Use the pipeline analyzer script
python3 scripts/pipeline_analyzer.py --platform github --workflow .github/workflows/ci.yml
```

### 3. Securing Your Pipeline

**Essential security checklist:**
- [ ] Use OIDC instead of static credentials
- [ ] Pin actions/includes to commit SHAs
- [ ] Use minimal permissions
- [ ] Enable secret scanning
- [ ] Add vulnerability scanning (dependencies, containers)
- [ ] Implement branch protection
- [ ] Separate test from deploy workflows

**OIDC Authentication (GitHub Actions to AWS):**
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

## Core Capabilities

| Domain | Tools & Technologies |
|--------|---------------------|
| **CI/CD Platforms** | GitHub Actions, GitLab CI, Jenkins |
| **Infrastructure as Code** | Terraform, AWS CDK, CloudFormation, Pulumi |
| **Containers** | Docker, Kubernetes, Helm, Kustomize |
| **GitOps** | ArgoCD, Flux |
| **Security Scanning** | CodeQL, Semgrep, Trivy, Snyk, TruffleHog |
| **Cloud Platforms** | AWS, Azure, GCP, Cloudflare |
| **Release Management** | semantic-release, Cosign, SLSA |

## Architecture Patterns

### CI/CD Pipeline Flow
```
Code Commit --> Build --> Test --> Security Scan --> Package
                                                       |
Monitor <-- Release Staging <-- Smoke Tests <-- Deploy Dev
                 |
         Manual Approval
                 |
         Deploy Production
```

### GitOps Architecture
```
App Repo --CI--> Config Repo --ArgoCD--> K8s Cluster
                     ^                        |
                     +----Continuous Sync-----+
```

## Reference Documentation

### CI/CD & Pipeline Design
- `references/best_practices.md` - Pipeline design patterns, testing strategies, deployment workflows
- `references/optimization.md` - Caching strategies, parallelization, build performance
- `references/troubleshooting.md` - Common issues, debugging, platform-specific problems
- `references/cicd-github-actions.md` - GitHub Actions workflows, runners, secrets

### Security & DevSecOps
- `references/security.md` - Secrets management, OIDC, supply chain security
- `references/devsecops.md` - SAST, DAST, SCA, container scanning guide
- `references/devsecops-basics.md` - Security best practices, shift-left security
- `references/security-hardening.md` - TLS enforcement, input validation, headers

### Infrastructure & Cloud Platforms
- `references/terraform-eks-module.tf` - Production EKS cluster Terraform
- `references/kubernetes-deployment.yaml` - K8s deployment with HPA and ArgoCD
- `references/kubernetes-basics.md` - Core K8s concepts, pods, services
- `references/docker-basics.md` - Dockerfile best practices, multi-stage builds
- `references/docker-compose.md` - Multi-container applications
- `references/aws-overview.md` - AWS fundamentals, IAM, services
- `references/gcloud-platform.md` - GCP overview, gcloud CLI
- `references/cloudflare-workers-basics.md` - Edge computing, Workers

### Enterprise Readiness
- `references/general.md` - Universal enterprise readiness checks
- `references/github.md` - GitHub-specific enterprise requirements
- `references/openssf-badge-silver.md` - Silver badge criteria
- `references/openssf-badge-gold.md` - Gold badge criteria
- `references/signed-releases.md` - Artifact and tag signing
- `references/reproducible-builds.md` - Deterministic build patterns

### Release Management
- `references/local-release-workflow.md` - Step-by-step release process
- `references/workflow-patterns.md` - Personal, team, standalone patterns
- `references/version-alignment.md` - Git tags as SSoT
- `references/authentication.md` - SSH keys, GitHub CLI auth

## Templates

### GitHub Actions
| Template | Description |
|----------|-------------|
| `templates/github-actions/node-ci.yml` | Complete Node.js CI/CD with security scanning |
| `templates/github-actions/python-ci.yml` | Python pipeline with pytest, coverage, PyPI |
| `templates/github-actions/go-ci.yml` | Go pipeline with multi-platform builds |
| `templates/github-actions/docker-build.yml` | Docker build with multi-platform, signing |
| `templates/github-actions/security-scan.yml` | Comprehensive DevSecOps pipeline |
| `templates/github-actions/dco-check.yml` | DCO sign-off enforcement |

### GitLab CI
| Template | Description |
|----------|-------------|
| `templates/gitlab-ci/node-ci.yml` | GitLab CI Node.js pipeline |
| `templates/gitlab-ci/python-ci.yml` | Python pipeline with parallel testing |
| `templates/gitlab-ci/go-ci.yml` | Go pipeline with Kubernetes deployment |
| `templates/gitlab-ci/docker-build.yml` | Docker build with DinD, multi-arch |
| `templates/gitlab-ci/security-scan.yml` | DevSecOps with GitLab security templates |

### Release Configuration
| Template | Description |
|----------|-------------|
| `templates/releaserc.yml` | semantic-release configuration |
| `templates/package.json` | Node.js package for releases |
| `templates/shareable-config/` | Shareable semantic-release config |

### Enterprise Templates
| Template | Description |
|----------|-------------|
| `templates/GOVERNANCE.md` | Project governance documentation |
| `templates/ARCHITECTURE.md` | Technical architecture template |
| `templates/CODE_OF_CONDUCT.md` | Contributor Covenant v2.1 |
| `templates/SECURITY_AUDIT.md` | Security self-audit template |

## Scripts

### Pipeline Analysis
| Script | Description |
|--------|-------------|
| `scripts/pipeline_analyzer.py` | Analyze workflows for optimization opportunities |
| `scripts/ci_health.py` | Check pipeline status and identify issues |
| `scripts/validate-devops-skill.sh` | Validate DevOps configurations |

### Security & Compliance
| Script | Description |
|--------|-------------|
| `scripts/verify-badge-criteria.sh` | OpenSSF Badge verification |
| `scripts/check-coverage-threshold.sh` | Statement coverage validation |
| `scripts/check-branch-coverage.sh` | Branch coverage analysis |
| `scripts/verify-signed-tags.sh` | Git tag signature verification |
| `scripts/verify-review-requirements.sh` | PR review requirements check |
| `scripts/check-tls-minimum.sh` | TLS 1.2+ enforcement check |
| `scripts/verify-spdx-headers.sh` | SPDX license header verification |
| `scripts/add-spdx-headers.sh` | Add SPDX headers to files |

### Infrastructure
| Script | Description |
|--------|-------------|
| `scripts/cloudflare_deploy.py` | Cloudflare Worker deployments |
| `scripts/docker_optimize.py` | Dockerfile analysis and optimization |

### Release Management
| Script | Description |
|--------|-------------|
| `scripts/init_project.sh` | Initialize semantic-release for project |
| `scripts/init_user_config.sh` | Create user-level release config |
| `scripts/create_org_config.sh` | Create organization release config |
| `scripts/generate-adr-notes.mjs` | Auto-link ADRs in release notes |

## Anti-Patterns to Avoid

### 1. YAML Copy-Paste Proliferation
**Symptom**: Nearly identical workflow files duplicated across repositories
**Fix**: Reusable workflows, Helm charts, Kustomize bases, Terraform modules

### 2. Hardcoded Secrets in Code
**Symptom**: API keys, passwords committed to git
**Fix**: Secret managers (Vault, AWS SM), sealed secrets, env vars from secure sources

### 3. No Rollback Strategy
**Symptom**: No plan for deployment failure, manual intervention required
**Fix**: Blue/green, canary with automated rollback, ArgoCD auto-revert

### 4. Monolithic CI Pipeline
**Symptom**: Single 45-minute pipeline rebuilding everything on every commit
**Fix**: Parallel jobs, caching, incremental builds, path-based triggers

### 5. Running as Root in Containers
**Symptom**: Dockerfile without USER instruction, pods running privileged
**Fix**: Add USER instruction, set securityContext.runAsNonRoot: true

### 6. Using :latest Tags
**Symptom**: `FROM node:latest` or `image: app:latest` in production
**Fix**: Pin specific versions, use immutable tags with SHA digests

### 7. Script Injection Vulnerability
**Symptom**: Using `${{ github.event.* }}` directly in workflow `run:` blocks
**Fix**: Use environment variables:
```yaml
# DANGEROUS - Script injection vulnerability
- run: echo "Title: ${{ github.event.issue.title }}"

# SAFE - Use environment variables
- name: Process issue
  env:
    TITLE: ${{ github.event.issue.title }}
  run: echo "Title: $TITLE"
```

## Quick Reference Commands

### GitHub Actions
```bash
gh workflow list                    # List workflows
gh run list --limit 20              # View recent runs
gh run view <run-id>                # View specific run
gh run rerun <run-id> --failed      # Re-run failed jobs
gh run view <run-id> --log > logs.txt  # Download logs
gh workflow run ci.yml              # Trigger workflow manually
```

### GitLab CI
```bash
gl project-pipelines list           # View pipelines
gl project-pipeline get <id>        # Pipeline status
gl project-pipeline retry <id>      # Retry failed jobs
gl project-pipeline cancel <id>     # Cancel pipeline
```

### Docker
```bash
docker build -t myapp .             # Build image
docker run -p 3000:3000 myapp       # Run container
docker compose up -d                # Start multi-container app
docker scout cves myapp             # Scan for vulnerabilities
```

### Kubernetes
```bash
kubectl apply -f deployment.yaml    # Apply manifest
kubectl get pods,services           # Check status
kubectl logs -f <pod>               # Stream logs
kubectl rollout status deployment/app  # Check rollout
```

### Terraform
```bash
terraform init                      # Initialize
terraform plan                      # Preview changes
terraform apply                     # Apply changes
terraform state list                # List resources
```

## Quality Checklist

```
[ ] All secrets in secret management (not in code)
[ ] Resource limits defined for all containers
[ ] Health checks configured (liveness, readiness)
[ ] Horizontal pod autoscaling enabled
[ ] Security contexts set (non-root, read-only)
[ ] Monitoring and alerting configured
[ ] Rollback strategy documented
[ ] Multi-environment support (dev, staging, prod)
[ ] Concurrency controls in CI pipelines
[ ] Remote state backend for Terraform
[ ] Vulnerability scanning in pipeline
[ ] Version pinning for all dependencies
[ ] Branch protection enabled
[ ] Code review required before merge
```

## Platform Selection Guide

| Need | Choose |
|------|--------|
| **Sub-50ms latency globally** | Cloudflare Workers |
| **Serverless functions (AWS)** | AWS Lambda |
| **Containerized workloads** | AWS ECS/Fargate, GKE, AKS |
| **Kubernetes at scale** | AWS EKS, Azure AKS, GCP GKE |
| **Object storage (zero egress)** | Cloudflare R2 |
| **Managed SQL** | AWS RDS, Azure SQL, Cloud SQL |
| **GitHub-integrated CI/CD** | GitHub Actions |
| **Self-hosted CI/CD** | GitLab CI, Jenkins |
| **Kubernetes GitOps** | ArgoCD, Flux |
| **Predictable workloads** | Reserved Instances, Savings Plans |
| **Fault-tolerant workloads** | Spot Instances, Preemptible VMs |

## Getting Started

1. **New pipeline**: Start with a template from `templates/`
2. **Add security scanning**: Use DevSecOps templates or add security stages
3. **Optimize existing**: Run `scripts/pipeline_analyzer.py`
4. **Debug issues**: Check `references/troubleshooting.md`
5. **Improve security**: Review `references/security.md` and `references/devsecops.md`
6. **Enterprise readiness**: Follow `references/general.md` checklist
7. **Set up releases**: Use `scripts/init_project.sh` for semantic versioning

## Source Skills

This curated skill combines content from:
- **CI/CD Pipelines** - Pipeline design, DevSecOps, optimization
- **DevOps Automator** - IaC, Kubernetes, deployment automation
- **DevOps Skill** - Cloud platforms, Docker, Cloudflare
- **Infrastructure Engineering Skill** - Multi-cloud, FinOps, comprehensive DevOps
- **Enterprise Readiness Assessment** - OpenSSF compliance, security assessment
- **semantic-release** - Automated versioning and releases

## Resources

- **GitHub Actions**: https://docs.github.com/actions
- **GitLab CI**: https://docs.gitlab.com/ee/ci/
- **Terraform**: https://developer.hashicorp.com/terraform
- **Kubernetes**: https://kubernetes.io/docs
- **ArgoCD**: https://argo-cd.readthedocs.io
- **OpenSSF Scorecard**: https://securityscorecards.dev/
- **SLSA Framework**: https://slsa.dev/
- **semantic-release**: https://semantic-release.gitbook.io/


