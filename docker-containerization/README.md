> **v1.1.22** | DevOps & Infrastructure | 24 iterations

# Docker Containerization

> Build production-grade Docker images, orchestrate multi-container applications, and set up isolated development environments -- from Dockerfile basics to advanced patterns.

## The Problem

Docker is deceptively simple to start and surprisingly hard to get right. Developers write a Dockerfile that works, build a 2GB image with root privileges and no health checks, and deploy it. The image contains the entire build toolchain, uses `latest` tags that break silently on updates, and has no `.dockerignore` so the build context includes `node_modules`, `.git`, and every temporary file in the project.

Docker Compose setups are worse. Services lack health checks so dependent containers start before databases are ready. No resource limits mean one runaway container starves the others. Data volumes are unnamed so a `docker compose down` destroys production data. Port conflicts between projects force developers to manually track which ports are in use. And when running multiple development environments in parallel (feature branches, code review worktrees), each one fights the others for ports and container names.

Teams also struggle with the gap between development and production containers. Dev containers have hot reload and debug tools but no resemblance to production. Production containers are built from scratch with different base images, different build steps, and different configurations. Bugs that only appear in the production container go undetected until deployment. The "works on my machine" problem is exactly what Docker was supposed to solve, but poorly structured containerization recreates it inside Docker itself.

## The Solution

This plugin provides comprehensive Docker guidance from basics through advanced patterns, covering Dockerfile best practices (specific versions, non-root users, multi-stage builds, health checks, layer caching optimization), Docker Compose orchestration (named volumes, health checks, restart policies, resource limits, network isolation, environment-specific overrides), and development environment patterns (DDEV for PHP/TYPO3, worktree isolation, port allocation, browser isolation, CORS configuration).

The skill ships with 13 reference documents covering every Docker domain: basic Dockerfiles, Compose patterns, extended patterns (CI/CD, troubleshooting), meta-configuration systems, worktree strategy, port allocation, browser isolation, CORS, DDEV setup and troubleshooting. It also includes 7 executable scripts: a Dockerfile optimizer that analyzes and suggests improvements, a prerequisites validator, a worktree manager for isolated development environments, browser MCP isolation setup, connectivity testing, and migration tooling.

Instead of learning Docker patterns through production incidents, you get them upfront: multi-stage builds that produce images under 500MB, Compose configurations with proper dependency management, and development environment setups that support parallel workflows without conflicts.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| 2GB Docker images containing build tools, test dependencies, and debug utilities | Multi-stage builds produce production images under 500MB with only runtime dependencies |
| Containers run as root with full system privileges | Non-root user configuration with minimal privileges by default |
| `latest` tags that break silently when upstream images update | Specific version pinning (e.g., `node:20.11.0-alpine3.19`) with documented upgrade paths |
| Docker Compose services fail because databases are not ready when apps start | Health checks on every service with proper `depends_on` conditions |
| Port conflicts between projects require manual tracking | Systematic port allocation strategy across worktrees and projects |
| Development and production containers are completely different | Multi-stage builds share the same Dockerfile with dev and prod stages |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install docker-containerization@skillstack
```

### Verify installation

After installing, test with:

```
Help me write a Dockerfile for my Node.js API with multi-stage build, non-root user, and health checks
```

## Quick Start

1. Install the plugin using the commands above
2. Describe what you need to containerize: `I have a Node.js app with a PostgreSQL database and Redis cache -- set up Docker Compose for local development`
3. The skill generates a complete Docker Compose configuration with health checks, named volumes, resource limits, and proper dependency management
4. It also generates a multi-stage Dockerfile for your Node.js app with build and production stages
5. Test it: `docker compose up -d` -- all services start in the correct order with health-checked dependencies

## What's Inside

| Component | Description |
|---|---|
| `docker-containerization` skill | Core skill covering Dockerfiles, multi-stage builds, Compose orchestration, development environments, DDEV, best practices, and quick reference commands |
| 13 reference documents | Docker basics, Compose patterns, extended patterns, meta-configuration, worktree strategy, port allocation, browser isolation, CORS, DDEV quickstart/advanced/prerequisites/troubleshooting, and Docker troubleshooting |
| 7 scripts | Dockerfile optimizer, prerequisites validator, worktree manager, browser MCP isolation setup, connectivity testing, isolation testing, and migration tooling |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests Dockerfile quality, Compose configuration, and optimization guidance |

### docker-containerization

**What it does:** Activates when you need to build Docker images, write Dockerfiles, set up Docker Compose applications, optimize container size, configure development environments with DDEV, manage port allocation across projects, or set up isolated browser containers for testing. Provides best practices, templates, and executable optimization tools.

**Try these prompts:**

```
Write a production-ready Dockerfile for my Python Django app with multi-stage build and security hardening
```

```
Set up Docker Compose for a microservices architecture with API gateway, 3 services, PostgreSQL, Redis, and RabbitMQ
```

```
My Docker image is 1.8GB -- help me analyze and optimize it down to a reasonable size
```

```
I need to run multiple development environments in parallel using git worktrees -- set up isolated Docker containers for each
```

```
Help me set up DDEV for a TYPO3 project with custom PHP configuration and database imports
```

**Key references:**

| Reference | Topic |
|---|---|
| `docker-basics.md` | Dockerfile fundamentals, layer caching, `.dockerignore`, image tagging |
| `docker-compose.md` | Multi-container orchestration, service definitions, volumes, networks, environment management |
| `extended-patterns.md` | Docker Compose patterns, DDEV setup, worktree isolation, container optimization, CI/CD pipelines, and troubleshooting |
| `docker-worktree-strategy.md` | Running isolated Docker environments per git worktree with port allocation |
| `port-allocation.md` | Systematic port assignment strategy to prevent conflicts across projects |
| `browser-isolation.md` | Isolated browser containers for parallel E2E testing |
| `cors-configuration.md` | Cross-origin configuration for containerized frontend/backend setups |
| `ddev-quickstart.md` | DDEV setup for PHP/TYPO3 development environments |
| `docker-troubleshooting.md` | Common Docker issues and their solutions |
| `docker-meta-config.md` | Meta-configuration systems for Ghostmind-style Docker setups |

## Real-World Walkthrough

You are building a SaaS application with a Node.js API, a React frontend, PostgreSQL, Redis for caching, and MinIO for file storage. Your current setup uses a single `Dockerfile` that produces a 1.6GB image, a `docker-compose.yml` without health checks, and developers constantly hit port conflicts because everyone runs their containers on the same default ports.

You open Claude Code:

```
I need to containerize my SaaS app properly. Right now I have a 1.6GB image, no health checks, port conflicts between developers, and the dev container is nothing like production. Help me set this up right.
```

The docker-containerization skill activates and starts with the Dockerfile. Your current setup copies everything into a single stage:

```dockerfile
FROM node:20
COPY . .
RUN npm install
CMD ["npm", "start"]
```

The skill rewrites it as a multi-stage build. The build stage installs all dependencies (including devDependencies), compiles TypeScript, and runs the build step. The production stage starts from a clean `node:20-alpine` base, copies only the compiled output and production dependencies, creates a non-root user, and adds a health check:

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
COPY package*.json ./
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
USER nodejs
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:3000/health || exit 1
CMD ["node", "dist/server.js"]
```

The image drops from 1.6GB to 180MB. No build tools, no TypeScript compiler, no devDependencies in the production image.

Next, Docker Compose. The skill generates a complete configuration with health checks on every service, named volumes for data persistence, resource limits, a custom network, and environment-specific overrides. PostgreSQL has a health check that verifies the database is ready to accept connections. The API service depends on PostgreSQL with `condition: service_healthy`, so it does not start until the database is actually ready -- not just until the container is running.

For the port conflict problem, the skill implements a port allocation strategy. Each developer gets a port range based on their worktree. The main branch uses ports 3000-3009, feature branches use a hash-based offset. A shared `.env.template` documents the port allocation, and the worktree manager script (`scripts/worktree-manager.sh`) automatically assigns ports when creating new development environments.

You run the Dockerfile optimizer script against your existing images:

```bash
python3 scripts/docker_optimize.py --dockerfile Dockerfile
```

It identifies three additional optimizations: consolidating RUN commands to reduce layers, using `.dockerignore` to exclude test files and documentation from the build context (saving 40MB), and switching the `COPY . .` to targeted copies for better cache utilization.

After implementing all changes, your development workflow is transformed. `docker compose up -d` brings up all five services in the correct order with health-checked dependencies. Each developer runs isolated environments on different port ranges. The production image is 180MB and runs as a non-root user with health checks. And the development compose file extends the production one with hot reload and debug tools, so the containers are structurally identical to production.

## Usage Scenarios

### Scenario 1: First-time containerization

**Context:** You have a working application that runs directly on your machine. You need to containerize it for the first time for deployment.

**You say:** `I have a Python FastAPI app with a PostgreSQL database -- help me containerize it for the first time with Docker best practices`

**The skill provides:**
- Multi-stage Dockerfile with build and production stages
- Non-root user configuration and security hardening
- Docker Compose setup with PostgreSQL, health checks, named volumes, and resource limits
- `.dockerignore` template to keep the build context clean
- Verification commands to test the containerized setup

**You end up with:** A complete, production-ready containerized application following Docker best practices from day one.

### Scenario 2: Optimizing oversized Docker images

**Context:** Your Docker images have grown to 1-2GB over time. Build times are slow, deployment takes forever, and container registry costs are climbing.

**You say:** `My Docker images are huge -- the API is 1.8GB and the frontend is 1.2GB. How do I shrink them?`

**The skill provides:**
- Dockerfile optimizer script that analyzes your current Dockerfile and suggests improvements
- Multi-stage build refactoring to separate build-time and runtime dependencies
- Alpine base image migration guide
- Layer optimization: consolidating RUN commands, ordering for cache efficiency
- `.dockerignore` audit to exclude unnecessary files from build context

**You end up with:** Optimized images typically 70-90% smaller, with faster builds and lower registry costs.

### Scenario 3: Setting up parallel development environments

**Context:** Your team uses git worktrees for feature branches but Docker containers conflict because they all use the same ports and container names.

**You say:** `We use git worktrees but our Docker containers conflict -- every branch tries to use port 3000 and the same container names. Fix this.`

**The skill provides:**
- Worktree-aware Docker strategy with hash-based port allocation
- Worktree manager script for creating isolated environments
- Container naming conventions that include the branch name
- `.env` template with port variables
- Connectivity validation script to test each environment independently

**You end up with:** Multiple parallel development environments running simultaneously without conflicts, each with its own port range and container names.

### Scenario 4: DDEV setup for PHP development

**Context:** You are starting a TYPO3 project and need a local development environment with PHP, MySQL, and the right extensions configured.

**You say:** `Set up DDEV for a TYPO3 12 project with custom PHP extensions, database imports, and SSL`

**The skill provides:**
- DDEV quickstart configuration for TYPO3
- Custom PHP configuration with required extensions
- Database import workflow from production dumps
- SSL certificate setup for local development
- Troubleshooting guide for common DDEV issues

**You end up with:** A fully configured DDEV environment that matches your production setup, with one-command startup.

## Ideal For

- **Developers containerizing for the first time** who want to start with best practices instead of learning them through production incidents
- **Teams with oversized Docker images** consuming excessive build time, deployment time, and registry storage
- **Organizations running parallel development** with git worktrees or multiple feature branches that need isolated Docker environments
- **PHP/TYPO3 developers** setting up DDEV-based development environments with custom configurations
- **DevOps engineers** standardizing Docker practices across teams with optimization scripts and templates

## Not For

- **CI/CD pipeline YAML** or pipeline configuration workflows -- use [cicd-pipelines](../cicd-pipelines/) instead
- **Workflow orchestration** or release automation -- use [workflow-automation](../workflow-automation/) instead
- **Kubernetes deployment** configuration and cluster management -- this plugin covers containers, not orchestration platforms

## How It Works Under the Hood

The plugin is a single-skill architecture with extensive references, executable scripts, and development environment tooling.

The **core skill** (`SKILL.md`) covers Dockerfile best practices (version pinning, non-root users, multi-stage builds, layer caching, health checks), Docker Compose orchestration (service definitions, health checks, named volumes, dependency management, resource limits, network isolation), development environment patterns (DDEV, worktree isolation, port allocation, browser isolation, CORS), and a quick reference command table.

The **reference library** (13 documents) provides depth across five domains:
- **Docker fundamentals** -- basics, Compose patterns, extended patterns, meta-configuration, and troubleshooting
- **Development environments** -- DDEV quickstart, advanced options, prerequisites, and troubleshooting for PHP/TYPO3 workflows
- **Isolation patterns** -- worktree Docker strategy, port allocation, browser isolation, and CORS configuration
- **Advanced patterns** -- CI/CD integration, optimization techniques, and meta-configuration for complex setups

The **scripts directory** (7 tools) provides executable automation: `docker_optimize.py` analyzes Dockerfiles and suggests improvements, `validate-prerequisites.sh` checks Docker and DDEV installation, `worktree-manager.sh` creates isolated development environments, and connectivity/isolation testing scripts verify that environments are properly isolated.

## Related Plugins

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline design and DevOps automation for GitHub Actions, GitLab CI, Jenkins, and Terraform
- **[Workflow Automation](../workflow-automation/)** -- Workflow orchestration, release automation, and parallel agent coordination
- **[Debugging](../debugging/)** -- Includes CI/CD pipeline debugging and E2E testing with containerized browsers

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
