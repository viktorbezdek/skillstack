> **v1.1.23** | DevOps & Infrastructure | 25 iterations

# Docker Containerization

> Build production-grade Docker images, orchestrate multi-container applications, and set up isolated development environments -- from Dockerfile basics to multi-stage builds, Docker Compose, DDEV, worktree isolation, and container optimization.
> Single skill + 13 reference documents + 7 scripts + 30+ templates | 13 trigger evals, 3 output evals

## The Problem

Docker containerization looks simple in tutorials and becomes complex in production. A basic Dockerfile runs in 5 minutes. A production-grade Dockerfile that handles multi-stage builds, non-root users, health checks, layer caching, security scanning, and image size optimization takes days of iteration. Multiply that by a Docker Compose setup with 5+ services, port allocation across worktrees, browser isolation for testing, CORS configuration, and DDEV integration for PHP projects -- and teams spend weeks on infrastructure that should be standardized.

The specific failure modes are well-documented but poorly prevented. Images ship with root users (security vulnerability), build tools included in production (attack surface), no health checks (silent failures in orchestration), hardcoded latest tags (non-reproducible builds), and 1GB+ sizes that slow CI/CD pipelines. Docker Compose configurations lack volume persistence (data loss on restart), have no resource limits (runaway containers starve the host), use default networks (no isolation), and have no restart policies (services stay down after crashes).

Development environment containerization adds another layer of complexity. Teams running multiple worktrees need isolated port allocations, separated browser state for parallel testing, CORS configuration that matches worktree-specific frontend ports, and environment file management across branches. Without systematic tooling for this, developers manually manage ports, accidentally clobber each other's containers, and waste hours on environment conflicts.

## The Solution

This plugin provides a comprehensive Docker containerization skill with 13 reference documents covering Docker basics, Docker Compose orchestration, multi-stage builds, DDEV for PHP/TYPO3 projects, worktree isolation strategies, port allocation, browser isolation, CORS configuration, container troubleshooting, and a meta-configuration system for managing Docker across complex project structures. It ships 7 operational scripts for Dockerfile optimization, prerequisite validation, worktree management, browser isolation setup, and connectivity testing. It includes 30+ templates for DDEV configurations, Docker Compose patterns, MCP isolation, and worktree startup.

The skill covers the full spectrum from first Dockerfile to advanced patterns: Dockerfile best practices (specific versions, non-root users, multi-stage builds, health checks, size limits), Docker Compose patterns (named volumes, health checks, restart policies, environment-specific configs, resource limits, network isolation), and development environment patterns (port allocation, browser isolation, CORS, DDEV integration, worktree management).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Docker images ship with root users and build tools in production | Best practices enforced: non-root users, multi-stage builds, security scanning, images under 500MB |
| Docker Compose loses data on restart, no health checks or restart policies | Named volumes for persistence, health checks on all services, restart policies, resource limits |
| Multiple worktrees conflict on ports, clobber each other's containers | Systematic port allocation, isolated container names per worktree, automated worktree manager |
| DDEV setup for PHP projects is manual and error-prone | Complete DDEV templates with configuration, commands, prerequisites validation, and troubleshooting |
| No way to test browser-dependent features in parallel worktrees | Browser isolation with separate user data directories and port ranges per worktree |
| Dockerfile optimization is trial and error | `docker_optimize.py` script analyzes Dockerfiles and recommends specific improvements |

## Context to Provide

Docker configuration quality depends entirely on knowing what you are containerizing. A generic "write a Dockerfile" request produces a generic result. Specifying the language, framework, build process, runtime requirements, and target environment enables the skill to apply the right patterns -- multi-stage vs. single-stage, Alpine vs. slim base, which files to exclude from the image, what health check to use.

**What to include in your prompt:**
- **Language and framework** (Node.js 20 with Express, Python 3.11 with FastAPI, Go 1.21) -- base image selection depends on this
- **Build process** (TypeScript compilation, wheel building, native extensions that need build tools) -- determines whether multi-stage is needed
- **Target image size constraint** if you have one -- forces the skill to apply size optimization
- **Services you need** (PostgreSQL version, Redis version, Nginx) -- each service has specific health check and volume patterns
- **Environment** (development vs. production vs. CI) -- determines which optimizations and security settings apply
- **Current Dockerfile or docker-compose.yml** if you are improving existing config -- paste it so the skill can analyze what to change rather than starting from scratch

**What makes results better:**
- Specifying non-root user requirements (almost always needed for production)
- Mentioning whether you use git worktrees or parallel development environments -- triggers port allocation and isolation guidance
- Describing your build artifacts (compiled binary, dist/ folder, wheel files) so the production stage copies only what is needed
- Stating whether you need DDEV (PHP/TYPO3 projects) -- activates a completely different set of templates

**What makes results worse:**
- "Help with Docker" without language/framework -- produces generic patterns rather than language-specific optimizations
- "Make it smaller" without knowing the current size and what is in the image -- optimization strategy differs for a 1.5GB Python image vs. a 500MB Node.js image
- Asking for CI/CD pipeline configuration -- that is `cicd-pipelines`; this skill handles the Dockerfile and Compose that pipelines build

**Template prompt:**
```
Write a production Dockerfile for a [language/version] application using [framework]. The build process: [describe how the app is built, e.g., TypeScript compilation, pip wheel building]. Runtime requirements: [what must be present at runtime]. Target image size: under [N]MB. Additional requirements: non-root user, health check on [endpoint], expose port [N].

Current Dockerfile (if improving existing):
[paste existing Dockerfile]
```

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install docker-containerization@skillstack
```

### Prerequisites

Docker Engine installed and running. Docker Compose (included with modern Docker Desktop). For DDEV: DDEV CLI installed. For optimization script: Python 3.

### Verify installation

After installing, test with:

```
Help me write a production Dockerfile for a Node.js 20 application with multi-stage builds, non-root user, and health checks.
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `"Create a Docker Compose setup for a Node.js app with PostgreSQL and Redis, including health checks and volume persistence."`
3. The skill generates a production-grade docker-compose.yml with best practices applied
4. Follow up with: `"Optimize the Dockerfile to reduce image size below 200MB."`
5. The skill applies multi-stage builds, alpine bases, and layer caching optimization

---

## System Overview

```
docker-containerization (plugin)
└── docker-containerization (skill)
    ├── Core Docker
    │   ├── references/docker-basics.md (Dockerfile, images, containers)
    │   └── references/docker-compose.md (multi-container orchestration)
    ├── Advanced patterns
    │   ├── references/extended-patterns.md (Compose patterns, optimization, CI/CD)
    │   └── references/docker-meta-config.md (Ghostmind meta.json system)
    ├── Development environments
    │   ├── references/docker-worktree-strategy.md (isolated worktrees)
    │   ├── references/port-allocation.md (port range management)
    │   ├── references/browser-isolation.md (parallel browser testing)
    │   └── references/cors-configuration.md (worktree CORS)
    ├── DDEV (PHP/TYPO3)
    │   ├── references/ddev-quickstart.md
    │   ├── references/ddev-advanced-options.md
    │   ├── references/ddev-prerequisites.md
    │   └── references/ddev-troubleshooting.md
    ├── Troubleshooting
    │   └── references/docker-troubleshooting.md
    ├── Scripts (7)
    │   ├── docker_optimize.py (Dockerfile analyzer)
    │   ├── validate-prerequisites.sh (Docker/DDEV check)
    │   ├── worktree-manager.sh (isolated environments)
    │   ├── setup-mcp-isolation.sh (browser MCP config)
    │   ├── validate-worktree-connectivity.sh
    │   ├── test-isolation.sh
    │   └── migrate-browser-isolation.sh
    └── Templates (30+)
        ├── DDEV configs, commands, and services
        ├── docker-compose.worktree.template.yml
        ├── ghostmind-compose.yaml
        ├── mcp.template.json
        └── start-worktree.template.sh
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `docker-containerization` | Skill | Dockerfile best practices, Compose orchestration, dev environments, DDEV |
| `docker-basics.md` | Reference | Core Docker concepts, Dockerfile patterns, image management |
| `docker-compose.md` | Reference | Multi-container orchestration, service dependencies, volumes, networks |
| `extended-patterns.md` | Reference | Advanced Compose patterns, container optimization, CI/CD pipelines, troubleshooting |
| `docker-meta-config.md` | Reference | Ghostmind meta.json-driven Docker configuration system |
| `docker-worktree-strategy.md` | Reference | Isolated Docker environments per git worktree |
| `port-allocation.md` | Reference | Port range management for multi-worktree projects |
| `browser-isolation.md` | Reference | Parallel browser testing with isolated user data |
| `cors-configuration.md` | Reference | CORS setup for worktree-specific frontend ports |
| `ddev-quickstart.md` | Reference | DDEV setup for PHP/TYPO3 projects |
| `ddev-advanced-options.md` | Reference | Advanced DDEV configuration |
| `ddev-prerequisites.md` | Reference | DDEV prerequisite validation |
| `ddev-troubleshooting.md` | Reference | DDEV common issues and solutions |
| `docker-troubleshooting.md` | Reference | Common Docker issues: port conflicts, build failures, networking |
| `docker_optimize.py` | Script | Analyzes Dockerfiles and recommends optimizations |
| `validate-prerequisites.sh` | Script | Checks Docker and DDEV installation |
| `worktree-manager.sh` | Script | Creates and manages isolated worktree environments |
| `setup-mcp-isolation.sh` | Script | Configures browser MCP isolation |
| Templates (30+) | Templates | DDEV configs, Compose templates, worktree startup scripts |
| Trigger evals | Test suite | 13 trigger evaluation cases |
| Output evals | Test suite | 3 output quality evaluation cases |

### Component Spotlights

#### docker-containerization (skill)

**What it does:** Activates when users work with Docker in any capacity -- writing Dockerfiles, setting up Docker Compose, optimizing images, configuring DDEV, managing worktree environments, or troubleshooting container issues. Provides best practices, templates, and automation for the full Docker lifecycle.

**Input -> Output:** Docker requirements (application type, services needed, environment constraints) -> Production-grade Dockerfiles, Compose configurations, development environment setup, and optimization recommendations.

**When to use:**
- Writing or optimizing Dockerfiles (multi-stage builds, image size)
- Setting up Docker Compose for multi-container apps
- Creating isolated development environments with worktrees
- Configuring DDEV for PHP/TYPO3 projects
- Optimizing container performance and size
- Managing ports, browser isolation, and CORS in multi-worktree setups

**When NOT to use:**
- CI/CD pipeline YAML or pipeline configuration (use `cicd-pipelines`)
- Workflow orchestration or release automation (use `workflow-automation`)

**Try these prompts:**

```
Write a production Dockerfile for a Python 3.11 FastAPI application. The build uses pip with a requirements.txt file -- some packages have native extensions that need build tools. Target: non-root user, health check on /health, under 200MB, no build tools in the final image.
```

```
Set up Docker Compose for a Node.js 20 Express app with PostgreSQL 15 and Redis 7. Include: health checks so the app waits for both services to be ready, named volumes for database persistence, resource limits (512MB memory per service), and separate .env files for dev and CI.
```

```
I run 3 git worktrees simultaneously -- main, feature-auth, and feature-payments. Each needs its own PostgreSQL, Redis, and API container. How do I allocate ports, name containers, and manage environment files so the worktrees never conflict? I want to be able to start and stop each worktree independently.
```

```
Set up DDEV for a TYPO3 13 project. We need PHP 8.2, Redis for caching, Xdebug for local development, and a Makefile with common commands. Show me the config.yaml and any Docker Compose overrides needed.
```

**Key references:**

| Reference | Topic |
|---|---|
| `docker-basics.md` | Core Docker concepts, Dockerfile syntax, image and container lifecycle |
| `docker-compose.md` | Service definitions, volumes, networks, dependencies, environment configs |
| `extended-patterns.md` | Multi-stage build patterns, optimization, CI/CD, troubleshooting |
| `port-allocation.md` | Systematic port range allocation for multi-worktree projects |
| `docker-worktree-strategy.md` | Isolated Docker environments per git worktree |

#### docker_optimize.py (script)

**CLI:** `python3 scripts/docker_optimize.py <Dockerfile>`

**What it produces:** Analysis report identifying optimization opportunities: image size reduction, layer caching improvements, security fixes (root user, exposed secrets), and best practice violations.

**Typical workflow:** Run on an existing Dockerfile before deployment. Apply recommended changes. Rebuild and compare image sizes.

#### worktree-manager.sh (script)

**CLI:** `./scripts/worktree-manager.sh create|start|stop|destroy <worktree-name>`

**What it produces:** Creates an isolated Docker environment for a git worktree with unique port allocation, separate container names, and environment file management.

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "Help with Docker" | "Write a multi-stage Dockerfile for a Node.js 20 TypeScript app with separate build and production stages" |
| "Set up my app" | "Create a Docker Compose setup with PostgreSQL 15, Redis 7, and my Express app with health checks and named volumes" |
| "Docker isn't working" | "My Docker build fails with 'npm ci' returning exit code 1. The error says 'node-gyp' can't find Python. Here's my Dockerfile." |
| "Make it smaller" | "My Docker image is 1.2GB. It's a Node.js app with TypeScript compilation. How do I get it under 200MB?" |

### Structured Prompt Templates

**For Dockerfile creation:**
```
Write a production Dockerfile for a [language/framework] application. Requirements: multi-stage build, non-root user, health check, image under [size]MB, [additional requirements].
```

**For Docker Compose setup:**
```
Set up Docker Compose for [app description] with these services: [service list]. Include health checks, named volumes, restart policies, and [environment-specific requirements].
```

**For development environment:**
```
I need isolated Docker environments for [N] git worktrees running [services]. How do I manage port allocation, container naming, and environment files to avoid conflicts?
```

### Prompt Anti-Patterns

- **Requesting CI/CD pipeline configuration:** "Set up my GitHub Actions Docker build" is a CI/CD question. Use `cicd-pipelines` for pipeline YAML. This skill handles the Dockerfile and Compose that pipelines build.
- **Asking about orchestration platforms:** "Set up Kubernetes for my Docker containers" is beyond this skill's scope. This skill covers Docker and Docker Compose, not orchestrators.
- **Providing no application context:** "Write a Dockerfile" without specifying the language, framework, or requirements produces generic results. Always specify the application stack.

## Real-World Walkthrough

**Starting situation:** You are setting up containerization for a team project: a TypeScript API server with PostgreSQL, Redis, and a background worker. Three developers work in parallel using git worktrees. The project also has a TYPO3 admin panel that requires DDEV. You need everything containerized with isolation between worktrees.

**Step 1: Production Dockerfile.** You ask: "Write a production Dockerfile for our TypeScript Express API. We need multi-stage build, non-root user, health check, and under 300MB image."

The skill produces a three-stage Dockerfile: (1) Build stage with full Node.js, TypeScript compilation, npm ci with dev dependencies. (2) Dependency stage with production-only npm ci. (3) Production stage: Alpine base, copy compiled dist and production node_modules only, create non-root user, add health check endpoint, expose port, set NODE_ENV=production. The resulting image is ~180MB instead of the 1.2GB single-stage would produce.

**Step 2: Docker Compose orchestration.** You ask: "Set up Docker Compose with PostgreSQL 15, Redis 7, the API, and a background worker. Include health checks, named volumes, and environment-specific configs."

The skill generates docker-compose.yml with all four services. PostgreSQL has a named volume for data persistence, a health check using `pg_isready`, and resource limits. Redis has an alpine image, persistence via appendonly, and health check via `redis-cli ping`. The API depends on both with `condition: service_healthy`. The worker shares the same image but different command. Environment variables use `.env` files with overrides for development vs. production.

**Step 3: Worktree isolation.** You ask: "Three developers need isolated environments. How do we manage ports across worktrees?"

The skill applies the worktree strategy from `docker-worktree-strategy.md`. Each worktree gets a port range: main uses 3000-3099, worktree-feature-a uses 3100-3199, worktree-feature-b uses 3200-3299. Container names are prefixed with the worktree slug. The `worktree-manager.sh` script automates creation, copying .env files, setting port offsets, and managing lifecycle. `validate-worktree-connectivity.sh` verifies all services are reachable.

**Step 4: Browser isolation for testing.** You ask: "Each worktree runs E2E tests with Playwright. How do I prevent browser state from leaking between worktrees?"

The skill sets up browser isolation: each worktree gets a unique user-data directory and debug port range. The `setup-mcp-isolation.sh` script configures the MCP server to use the worktree-specific browser profile. `test-isolation.sh` verifies that sessions are actually isolated.

**Step 5: DDEV for the TYPO3 panel.** You ask: "Set up DDEV for the TYPO3 admin panel with Redis and custom PHP 8.2."

The skill generates the DDEV configuration from templates: `config.yaml` with PHP 8.2 and web type, custom Docker Compose files for Redis integration, Makefile for common operations, and install commands for TYPO3 versions 11-13. `validate-prerequisites.sh` checks that Docker and DDEV are installed before setup.

**Step 6: Optimize.** You run `python3 scripts/docker_optimize.py Dockerfile` on the initial Dockerfile and get recommendations: add .dockerignore (missing node_modules), use specific alpine version tag (was using just `alpine`), add COPY with --chown instead of separate RUN chown (fewer layers). Applied changes reduce build time by 30% through better layer caching.

**Gotchas discovered:** Port conflicts were the biggest pain point before the worktree manager. Two developers both starting their environments defaulted to port 3000, breaking each other silently. Systematic port allocation eliminated this entirely.

## Usage Scenarios

### Scenario 1: Optimizing a bloated Docker image

**Context:** Your Docker image is 1.5GB and slowing down CI/CD. It is a Python FastAPI application.

**You say:** "My Python Docker image is 1.5GB. How do I get it under 300MB?"

**The skill provides:**
- Multi-stage build pattern: compile wheels in build stage, copy only wheels to slim production stage
- Alpine vs. slim-bookworm comparison for Python images
- .dockerignore template to exclude test data, docs, and development files
- Layer ordering for optimal caching

**You end up with:** A ~250MB production image with multi-stage build and layer caching optimization.

### Scenario 2: Setting up a development environment from scratch

**Context:** New developer joining the team. Project uses Docker Compose with 5 services. Setup takes a full day.

**You say:** "Streamline our Docker development setup so a new developer can be running in 15 minutes with all 5 services."

**The skill provides:**
- Docker Compose with health checks ensuring services start in order
- Single `docker compose up -d` command with everything configured
- Environment file template with sensible defaults
- `validate-prerequisites.sh` that checks Docker version, available ports, and disk space

**You end up with:** A one-command setup that starts all services in dependency order with health checks, reducing onboarding from a day to 15 minutes.

### Scenario 3: Debugging container networking issues

**Context:** Your app container cannot connect to the database container. `curl` from inside the container times out.

**You say:** "My app container can't reach the database. Docker Compose networking seems broken. How do I diagnose this?"

**The skill provides:**
- Systematic troubleshooting: verify both containers are on the same network, check container name resolution, test port binding
- Common causes: wrong service name in connection string, database not ready when app starts (missing health check), custom network not attached
- Docker troubleshooting reference with port conflict resolution, DNS debugging, and volume mount fixes

**You end up with:** The specific networking issue identified and fixed, plus health checks that prevent the timing issue from recurring.

---

## Decision Logic

**When does docker-containerization activate vs. cicd-pipelines?**

These skills have a clear boundary:
- **docker-containerization:** Everything inside the container -- Dockerfiles, Compose files, image optimization, development environments, DDEV
- **cicd-pipelines:** Everything that builds and deploys the container -- GitHub Actions workflows, GitLab CI pipelines, deployment automation

If you are writing a Dockerfile -> docker-containerization. If you are writing a CI workflow that builds that Dockerfile -> cicd-pipelines.

**When should I use DDEV vs. raw Docker Compose?**

- PHP/TYPO3 projects where DDEV provides out-of-the-box support: use DDEV
- Custom service topologies, non-PHP projects, or fine-grained control: use Docker Compose
- DDEV with custom services (Redis, Elasticsearch): DDEV for the base, Docker Compose overrides for additional services

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Port conflicts between worktrees | "Port already in use" errors when starting second worktree | Use the port allocation reference to assign non-overlapping ranges; validate with `validate-worktree-connectivity.sh` |
| Docker layer cache invalidation | Every build reinstalls all dependencies, taking 10+ minutes | Reorder Dockerfile: COPY dependency files first, RUN install, then COPY source code; dependency layer caches unless dependencies change |
| DDEV environment corruption | DDEV commands fail with cryptic errors after system update | `ddev poweroff` to stop all containers, `ddev delete --omit-snapshot` to clean up, then `ddev start` to rebuild |
| Docker Compose volume data loss | Database data disappears on `docker compose down` | Always use named volumes, not anonymous volumes; `docker compose down` does not remove named volumes unless `--volumes` is passed |

## Ideal For

- **Backend developers** containerizing applications who need production-grade Dockerfiles with multi-stage builds, security, and size optimization
- **Full-stack teams** managing multi-service applications who need Docker Compose orchestration with health checks, volumes, and networking
- **Teams using git worktrees** for parallel development who need isolated Docker environments with port management and browser separation
- **PHP/TYPO3 developers** who need DDEV setup with custom services, configuration templates, and troubleshooting guides

## Not For

- **CI/CD pipeline configuration** -- if you need GitHub Actions or GitLab CI workflows, use `cicd-pipelines`
- **Workflow orchestration or release automation** -- use `workflow-automation` for deployment pipelines
- **Kubernetes or container orchestration platforms** -- this skill covers Docker and Docker Compose, not cluster orchestrators

## Related Plugins

- **cicd-pipelines** -- Build and deploy the Docker images this skill creates; CI/CD pipeline design and optimization
- **workflow-automation** -- Automate deployment workflows that use Docker containers
- **debugging** -- Debug containerized applications; includes CI/CD debugging that overlaps with container issues
- **testing-framework** -- Set up testing infrastructure that runs inside containers

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
