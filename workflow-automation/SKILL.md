---
name: workflow-automation
description: "Automate development workflows end-to-end: CI/CD pipelines, multi-agent orchestration, parallel task execution, release automation, and git workflow management. Use when: automating a workflow, building a CI/CD pipeline, orchestrating parallel tasks, setting up release automation, coordinating multi-agent workflows, or managing complex task dependencies. Triggers: 'automate workflow', 'CI/CD pipeline', 'parallel tasks', 'task orchestration', 'build pipeline', 'release automation', 'multi-agent workflow', 'automate deployment', 'pipeline setup', 'workflow orchestration', 'automate build'."
---

# Workflow Automation Skill

Comprehensive guide for workflow automation, task management, and productivity optimization in software development. This skill combines CI/CD pipelines, git workflow management, scientific workflow tools, multi-agent orchestration, TDD workflows, and release automation.

## When to Use This Skill

Use this skill when:
- **CI/CD Pipelines**: Creating, optimizing, or troubleshooting CI/CD workflows
- **Git Workflows**: Managing parallel development with worktrees and GitFlow
- **Scientific Workflows**: Choosing tools for computational workflows (joblib, Prefect, Parsl)
- **Multi-Agent Orchestration**: Coordinating multiple agents for complex tasks
- **TDD/Development Cycles**: Following RED-GREEN-REFACTOR with quality gates
- **Code Review Automation**: Implementing TRUST 5 framework validation
- **Release Automation**: Setting up semantic versioning and automated releases
- **Task Management**: Orchestrating complex dependencies and parallel execution

## Quick Decision Guide

### What are you trying to automate?

```
START: What type of workflow?

├── Build/Test/Deploy Pipeline
│   └── Use: CI/CD Pipelines → references/cicd/
│       ├── GitHub Actions → templates/github-actions/
│       └── GitLab CI → templates/gitlab-ci/

├── Parallel Feature Development
│   └── Use: Git Workflow Manager → scripts/git/
│       • create_worktree.sh
│       • GitFlow conventions

├── Scientific Computations
│   ├── Simple caching? → joblib (subskills/joblib.md)
│   ├── HPC cluster? → Parsl (subskills/parsl.md)
│   ├── Complex DAG? → Prefect (subskills/prefect.md)
│   └── Materials science? → quacc/FireWorks

├── Multi-Agent Coordination
│   └── Use: Alfred Workflow Orchestration
│       • WorkflowEngine patterns
│       • Context7 integration
│       • Error recovery

├── Development Workflow (TDD/Debug/Review)
│   └── Use: Development Workflow Specialist
│       • TDDManager → modules/tdd-context7.md
│       • AIDebugger → modules/ai-debugging.md
│       • AutomatedCodeReviewer → modules/automated-code-review.md

└── Automated Releases
    └── Use: Semantic Release → references/semantic-release/
        • Local-first releases
        • Conventional commits
```

## Core Capabilities

### 1. CI/CD Pipelines

Design, optimize, and troubleshoot CI/CD pipelines across GitHub Actions and GitLab CI.

**Key Features:**
- Pipeline design patterns (fail-fast, parallelize, cache)
- DevSecOps security scanning (SAST, DAST, SCA)
- Deployment strategies (blue-green, canary, rolling)
- Performance optimization and troubleshooting

**Quick Start:**
```yaml
# Basic pipeline structure
# 1. Fast feedback (lint, format) - <1 min
# 2. Unit tests - 1-5 min
# 3. Integration tests - 5-15 min
# 4. Build artifacts
# 5. Deploy (with approval gates)
```

**Resources:**
- `references/cicd/best_practices.md` - Pipeline design patterns
- `references/cicd/security.md` - Secrets management, OIDC
- `references/cicd/devsecops.md` - Security scanning guide
- `templates/github-actions/` - GitHub Actions templates
- `templates/gitlab-ci/` - GitLab CI templates

### 2. Git Workflow Management

Manage git worktrees following GitFlow conventions for parallel development.

**Key Features:**
- Worktree creation and management
- GitFlow branch conventions (feature/, fix/, hotfix/)
- Parallel feature development
- Clean branch organization

**Quick Start:**
```bash
# Create feature worktree
./scripts/git/create_worktree.sh feature email-notifications

# Result:
# - Branch: feature/email-notifications
# - Worktree: ../project-worktrees/feature/email-notifications/

# List all worktrees
./scripts/git/list_worktrees.sh

# Clean up merged worktrees
./scripts/git/cleanup_worktrees.sh --merged
```

**Directory Structure:**
```
project/                    ← Main repository (main branch)
project-worktrees/          ← Worktree parent
├── feature/
│   ├── email-notifications/
│   └── user-dashboard/
├── fix/
│   └── login-timeout/
└── hotfix/
    └── security-patch/
```

**Resources:**
- `scripts/git/create_worktree.sh` - Create worktree with GitFlow conventions
- `scripts/git/list_worktrees.sh` - List worktrees with status
- `scripts/git/cleanup_worktrees.sh` - Clean up stale worktrees
- `references/gitflow-conventions.md` - Complete GitFlow reference

### 3. Scientific Workflow Management

Choose the right tool for computational workflows - from simple joblib caching to complex orchestration.

**Tool Selection:**

| Situation | Tool | Why |
|-----------|------|-----|
| Cache function calls | joblib.Memory | Dead simple caching |
| 10-100 tasks on laptop | joblib.Parallel | Built-in, no setup |
| 100+ tasks on HPC | Parsl | HPC-aware, implicit parallelism |
| Complex DAG with retries | Prefect | Modern, Pythonic, great UI |
| Cloud-agnostic deployment | Covalent | Infrastructure abstraction |
| Materials DFT workflows | quacc | Pre-built recipes |
| Production materials | FireWorks | Battle-tested |

**Quick Start:**
```python
# Simple caching
from joblib import Memory
memory = Memory("./cache")

@memory.cache
def expensive_computation(x):
    return result

# Parallel execution
from joblib import Parallel, delayed
results = Parallel(n_jobs=4)(
    delayed(compute)(i) for i in range(100)
)
```

**Resources:**
- `subskills/joblib.md` - Caching and parallelism
- `subskills/prefect.md` - Modern Python orchestration
- `subskills/parsl.md` - HPC scientific computing
- `subskills/covalent.md` - Cloud/quantum workflows
- `subskills/fireworks.md` - Materials production
- `subskills/quacc.md` - Materials high-throughput

### 4. Multi-Agent Workflow Orchestration

Coordinate multiple agents for complex development workflows with Context7 integration.

**Key Features:**
- Multi-agent coordination
- Task scheduling with priorities
- Error handling and recovery
- Performance monitoring

**Quick Start:**
```python
from alfred_workflow import WorkflowEngine, Agent

engine = WorkflowEngine()
spec_agent = Agent("spec-builder", domain="requirements")
impl_agent = Agent("tdd-implementer", domain="development")
test_agent = Agent("quality-gate", domain="testing")

workflow = engine.create_workflow("feature_development")
workflow.add_stage("specification", spec_agent)
workflow.add_stage("implementation", impl_agent, depends_on=["specification"])
workflow.add_stage("testing", test_agent, depends_on=["implementation"])

result = engine.execute(workflow, input_data={"feature": "user auth"})
```

**Workflow Templates:**
- Feature Development: spec → implementation → testing
- Bug Fix: diagnosis → fix → validation
- Code Review: analysis → feedback → approval

**Resources:**
- `references/alfred-workflow-patterns.md` - Orchestration patterns
- `examples/enterprise-testing-workflow.py` - Complete workflow example

### 5. Development Workflow (TDD/Debug/Review)

Implement TDD cycles, AI-powered debugging, and automated code review with TRUST 5 framework.

**Key Components:**

**TDDManager** - Test-driven development cycle:
```python
from workflow import TDDManager, TestSpecification

tdd = TDDManager(project_path, context7_client)

# RED: Generate failing test
# GREEN: Implement minimum code
# REFACTOR: Optimize with patterns
cycle_results = await tdd.run_full_tdd_cycle(
    specification=test_spec,
    target_function="authenticate_user"
)
```

**AIDebugger** - Intelligent error analysis:
```python
from workflow import AIDebugger

debugger = AIDebugger(context7_client)
analysis = await debugger.debug_with_context7_patterns(
    exception=e,
    context={"file": "app.py", "function": "main"},
    project_path="/project/src"
)
# Returns: root cause, solutions, code suggestions
```

**AutomatedCodeReviewer** - TRUST 5 validation:
```python
from workflow import AutomatedCodeReviewer

reviewer = AutomatedCodeReviewer(context7_client)
review = await reviewer.review_codebase(
    project_path="/project/src",
    changed_files=["src/auth/service.py"]
)
# TRUST 5: Test-first, Readable, Unified, Secured, Trackable
```

**Resources:**
- `modules/tdd-context7.md` - TDD with Context7
- `modules/ai-debugging.md` - AI-powered debugging
- `modules/automated-code-review.md` - TRUST 5 review
- `modules/smart-refactoring.md` - Technical debt analysis
- `modules/performance-optimization.md` - Profiling and optimization

### 6. Release Automation (Semantic Release)

Automate versioning and releases using semantic-release (Node.js) for any language.

**Key Features:**
- Local-first releases (instant feedback vs 2-5 min CI wait)
- Conventional commits for automatic version bumps
- GitHub releases and changelog generation
- Multi-account authentication support

**Quick Start:**
```bash
# Dry-run first
GITHUB_TOKEN=$(gh auth token) npx semantic-release --no-ci --dry-run

# Create release
GITHUB_TOKEN=$(gh auth token) npx semantic-release --no-ci
```

**Version Bump Rules:**
- `feat:` → MINOR (0.1.0 → 0.2.0)
- `fix:` → PATCH (0.1.0 → 0.1.1)
- `BREAKING CHANGE:` → MAJOR (0.1.0 → 1.0.0)

**Resources:**
- `references/semantic-release/` - Complete release workflow
- `references/semantic-release/local-release-workflow.md` - Local release guide
- `references/semantic-release/authentication.md` - SSH and gh CLI setup

### 7. FABER Workflow State Management

Manage workflow state with FABER (Frame, Architect, Build, Evaluate, Release) methodology.

**Key Operations:**
```bash
# Load configuration
./scripts/faber/config-loader.sh

# Read workflow state
./scripts/faber/state-read.sh ".faber/state.json"

# Update phase state
./scripts/faber/state-update-phase.sh frame completed '{"work_type": "feature"}'

# Post status card
./scripts/faber/status-card-post.sh abc12345 123 evaluate "Build is green"
```

**Resources:**
- `scripts/faber/` - Complete script collection (29 scripts)
- `templates/status-card.template.md` - Status card template

## Quality Metrics

| Metric | Threshold | Description |
|--------|-----------|-------------|
| Test Coverage | >= 85% | Minimum code coverage |
| TRUST Score | >= 0.85 | 5 quality criteria combined |
| Critical Issues | 0 | No critical security/bugs |
| Performance Regression | < 10% | Max allowed degradation |
| Response Time | < 100ms | API response target |

## Best Practices

### CI/CD Pipelines
- Fail fast: Run cheap validation first
- Parallelize: Remove unnecessary job dependencies
- Cache dependencies: 50-90% faster builds
- Use OIDC: No static credentials
- Pin actions: Use commit SHAs

### Git Workflows
- One feature per worktree
- Descriptive branch names
- Commit before switching
- Push regularly for backup
- Clean up after merge

### Development Workflows
- Write tests before implementation (TDD)
- Maintain 85%+ coverage
- Use meaningful test names
- Mock external dependencies
- Profile before optimizing

### Release Automation
- Use conventional commits
- Run dry-run before release
- Verify account alignment
- Local releases for speed
- CI backup optional

## Resources Directory Structure

```
workflow-automation/
├── SKILL.md                     # This file
├── modules/
│   ├── ai-debugging.md          # AIDebugger class
│   ├── automated-code-review.md # TRUST 5 framework
│   ├── performance-optimization.md
│   ├── smart-refactoring.md
│   └── tdd-context7.md          # TDDManager class
├── references/
│   ├── cicd/
│   │   ├── best_practices.md
│   │   ├── devsecops.md
│   │   ├── optimization.md
│   │   ├── security.md
│   │   └── troubleshooting.md
│   ├── gitflow-conventions.md
│   ├── alfred-workflow-patterns.md
│   └── semantic-release/
├── scripts/
│   ├── git/                     # Git worktree scripts
│   ├── faber/                   # FABER workflow scripts
│   ├── cicd/                    # Pipeline analysis scripts
│   └── workflow/                # Workflow utilities
├── subskills/
│   ├── joblib.md
│   ├── prefect.md
│   ├── parsl.md
│   ├── covalent.md
│   ├── fireworks.md
│   └── quacc.md
├── templates/
│   ├── github-actions/
│   │   ├── node-ci.yml
│   │   ├── python-ci.yml
│   │   ├── go-ci.yml
│   │   ├── docker-build.yml
│   │   └── security-scan.yml
│   └── gitlab-ci/
│       ├── node-ci.yml
│       ├── python-ci.yml
│       ├── go-ci.yml
│       ├── docker-build.yml
│       └── security-scan.yml
├── examples/
│   └── enterprise-testing-workflow.py
└── docs/
    └── quick-reference.md
```

## See Also

- `references/cicd/` - CI/CD deep-dive documentation
- `modules/` - Development workflow modules
- `subskills/` - Scientific workflow tool guides
- `templates/` - Pipeline starter templates
- `scripts/` - Automation scripts

---

**Version**: 1.0.0
**Last Updated**: 2025-01-18
**Sources**: development-workflow-specialist, git-workflow-manager, scientific-workflow-management, alfred-workflow-orchestration, faber-core, cicd-pipelines, semantic-release







