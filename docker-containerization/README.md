# Docker Containerization

> Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration, container optimization, development environment setup, and infrastructure patterns.

## Overview

Containerization is the backbone of modern development and deployment workflows, yet writing efficient Dockerfiles, orchestrating multi-container applications, and managing development environments involves a steep learning curve with many subtle pitfalls. This skill provides battle-tested patterns, automation scripts, and reference materials to get containerization right the first time.

Whether you are writing your first Dockerfile, setting up a multi-service Docker Compose stack, configuring DDEV for PHP/TYPO3 development, or optimizing production images for size and security, this skill has the templates, scripts, and references you need. It covers the full lifecycle from development environments through CI/CD builds to production deployment.

As part of the SkillStack collection, this skill integrates with the debugging skill for CI/CD pipeline troubleshooting, the git-workflow skill for worktree-based parallel development with isolated Docker environments, and the frontend-design skill for containerized frontend build pipelines.

## What's Included

### References

- `references/docker-basics.md` - Core Docker concepts, Dockerfile instructions, and best practices
- `references/docker-compose.md` - Docker Compose orchestration patterns and configuration
- `references/extended-patterns.md` - Advanced patterns for Compose, DDEV, optimization, and troubleshooting
- `references/docker-meta-config.md` - Ghostmind meta.json-driven Docker configuration system
- `references/docker-worktree-strategy.md` - Strategy for Docker in git worktree environments
- `references/port-allocation.md` - Port allocation conventions for multi-container setups
- `references/browser-isolation.md` - Browser container isolation for parallel testing
- `references/cors-configuration.md` - CORS configuration for worktree frontend ports
- `references/docker-troubleshooting.md` - Common Docker issues and their solutions
- `references/ddev-quickstart.md` - Quick start guide for DDEV development environments
- `references/ddev-advanced-options.md` - Advanced DDEV configuration and customization
- `references/ddev-prerequisites.md` - DDEV installation prerequisites and system requirements
- `references/ddev-troubleshooting.md` - DDEV-specific troubleshooting guide

### Scripts

- `scripts/docker_optimize.py` - Analyze and optimize Dockerfiles for size, security, and caching
- `scripts/validate-prerequisites.sh` - Validate Docker and DDEV installation prerequisites
- `scripts/worktree-manager.sh` - Manage isolated worktree Docker environments
- `scripts/setup-mcp-isolation.sh` - Configure browser MCP isolation for testing
- `scripts/validate-worktree-connectivity.sh` - Test service connectivity across worktrees
- `scripts/test-isolation.sh` - Verify browser isolation between environments
- `scripts/migrate-browser-isolation.sh` - Migrate to updated browser isolation configuration

### Templates

- `templates/docker-compose.worktree.template.yml` - Docker Compose template for worktree environments
- `templates/ghostmind-compose.yaml` - Ghostmind Docker Compose configuration
- `templates/ghostmind-meta.json` - Ghostmind meta.json configuration template
- `templates/mcp.template.json` - MCP isolation configuration template
- `templates/start-worktree.template.sh` - Worktree startup script template
- `templates/ddev/config.yaml` - DDEV project configuration template
- `templates/ddev/apache/apache-site.conf` - Apache virtual host configuration
- `templates/ddev/docker-compose.web.yaml` - DDEV web container Compose override
- `templates/ddev/docker-compose.git-info.yaml` - DDEV git info Compose override
- `templates/ddev/docker-compose.ofelia.yaml.optional` - Optional Ofelia job scheduler config
- `templates/ddev/docker-compose.services-redis.yaml.optional` - Optional Redis service config
- `templates/ddev/docker-compose.services.yaml.optional` - Optional additional services config
- `templates/ddev/config.redis.php.example` - PHP Redis configuration example
- `templates/ddev/README-SERVICES.md.optional` - Optional services documentation
- `templates/ddev/index.html.template` - Default index page template
- `templates/ddev/Makefile.template` - DDEV project Makefile template
- `templates/ddev/web-build/Dockerfile` - Custom web container Dockerfile
- `templates/ddev/web-build/install-cron.sh.optional` - Optional cron installation script
- `templates/ddev/web-entrypoint.d/10-cleanup-index.sh` - Web container entrypoint cleanup
- `templates/ddev/commands/` - DDEV custom commands (host, web, install scripts)

## Key Features

- Dockerfile analysis and optimization with automated size, security, and caching recommendations
- Multi-stage build patterns for minimal production images
- Docker Compose orchestration templates for multi-service applications
- DDEV development environment setup for PHP/TYPO3 projects with full template suite
- Git worktree isolation with per-worktree Docker environments and port management
- Browser container isolation for parallel E2E testing
- Prerequisite validation scripts to ensure correct Docker/DDEV installation
- Meta.json-driven configuration system for Ghostmind projects
- Port allocation conventions to prevent conflicts across parallel environments

## Usage Examples

**Write an optimized Dockerfile:**
```
I need a Dockerfile for my Node.js API that's production-ready with multi-stage builds.
```
Generates a multi-stage Dockerfile with dependency caching, non-root user, health checks, and minimal production image following all best practices from the references.

**Set up Docker Compose for local development:**
```
Set up Docker Compose with PostgreSQL, Redis, and my Node.js app for local development.
```
Creates a docker-compose.yml with named volumes, health checks, environment variables, proper networking, and restart policies using the templates and patterns.

**Optimize an existing Dockerfile:**
```
Analyze my Dockerfile and suggest optimizations to reduce image size.
```
Runs the `docker_optimize.py` script to identify layer caching issues, unnecessary dependencies, missing multi-stage opportunities, and security improvements.

**Set up DDEV for a TYPO3 project:**
```
Initialize DDEV for my TYPO3 12 project with Redis and Apache.
```
Uses DDEV templates to generate configuration, Apache vhost, Redis service, custom commands, and Makefile with a complete development environment.

**Create isolated worktree environments:**
```
I need to run two feature branches simultaneously with separate Docker environments.
```
Uses the worktree manager to create isolated Docker Compose environments with unique port allocations, preventing conflicts between parallel development streams.

## Quick Start

1. **Validate prerequisites** to ensure Docker is properly installed:
   ```bash
   ./scripts/validate-prerequisites.sh
   ```

2. **For a new project**, start with a basic Dockerfile following the patterns in `references/docker-basics.md`:
   ```bash
   docker build -t myapp:1.0 .
   docker run -d -p 3000:3000 --name myapp myapp:1.0
   ```

3. **For multi-container apps**, use Docker Compose with patterns from `references/docker-compose.md`:
   ```bash
   docker compose up -d
   docker compose logs -f
   ```

4. **To optimize an existing Dockerfile**, run the analyzer:
   ```bash
   python3 scripts/docker_optimize.py path/to/Dockerfile
   ```

5. **For DDEV projects**, copy the DDEV templates and customize:
   ```bash
   cp -r templates/ddev/ .ddev/
   ddev start
   ```

## Related Skills

- **debugging** -- Debug CI/CD pipeline Docker builds and container runtime issues
- **git-workflow** -- Manage worktrees with isolated Docker environments per branch
- **frontend-design** -- Containerize frontend build pipelines with optimized images
- **documentation-generator** -- Generate deployment and operations documentation

---

Part of [SkillStack](https://github.com/viktorbezdek/claude-skills) — `/plugin install docker-containerization@claude-skills` -- 34 production-grade skills for Claude Code.
