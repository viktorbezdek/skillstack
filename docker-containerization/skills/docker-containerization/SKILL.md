---
name: docker-containerization
description: Docker and container development — use when the user mentions Dockerfiles, multi-stage builds, Docker Compose, container optimization, image size reduction, DDEV, containerization, or dev environment setup with containers. NOT for CI/CD pipeline YAML or pipeline configuration (use cicd-pipelines), NOT for workflow orchestration or release automation (use workflow-automation), NOT for Kubernetes or container orchestration platforms (use cloud-native tooling).
license: MIT
---

# Docker Containerization Skill

Comprehensive guide for Docker containerization: Dockerfiles, multi-stage builds, Docker Compose orchestration, development environments, and advanced patterns.

## When to Use / Not Use

**Use when:**
- Writing or optimizing Dockerfiles (multi-stage builds, layer caching, image size)
- Setting up Docker Compose for multi-container apps (health checks, volumes, networks)
- Creating isolated development environments with worktrees
- Configuring DDEV for PHP/TYPO3 projects
- Managing ports, browser isolation, and CORS in multi-worktree setups
- Running container optimization analysis (`scripts/docker_optimize.py`)

**Do NOT use when:**
- CI/CD pipeline YAML or pipeline configuration -> use `cicd-pipelines`
- Workflow orchestration or release automation -> use `workflow-automation`
- Kubernetes or container orchestration platforms -> use cloud-native tooling
- Debugging containerized applications -> use `debugging` (but this skill helps with environment setup)

## Decision Tree

```
What Docker task do you need?
├── Write a Dockerfile
│   ├── Single-language app, no build step -> Single-stage FROM + COPY + CMD
│   ├── Compiled/bundled app (TypeScript, Go, wheel) -> Multi-stage build (build + production)
│   ├── Need smallest image -> Alpine or distroless base, multi-stage
│   └── PHP/TYPO3 project -> DDEV (see references/ddev-quickstart.md)
├── Set up Docker Compose
│   ├── Single app + DB -> 2 services, health check on DB, depends_on with condition
│   ├── Multiple services (app + DB + cache + worker) -> Named volumes, health checks, resource limits
│   ├── Need worktree isolation -> Port ranges per worktree, prefixed container names
│   └── Environment-specific configs -> Override files: docker-compose.override.yml
├── Optimize existing image
│   ├── Image too large -> Run docker_optimize.py, add .dockerignore, reorder layers
│   ├── Build too slow -> Reorder: COPY deps first, RUN install, then COPY source
│   └── Security issues -> Non-root user, specific version tags, no build tools in production
├── Development environment
│   ├── Git worktree isolation -> references/docker-worktree-strategy.md + worktree-manager.sh
│   ├── Browser isolation for E2E -> references/browser-isolation.md + setup-mcp-isolation.sh
│   └── Port conflicts -> references/port-allocation.md (systematic ranges)
└── Troubleshooting
    ├── Build fails -> Check Dockerfile syntax, cache, .dockerignore
    ├── Container can't connect -> Check network, service names, health checks
    ├── Data lost on restart -> Use named volumes (not anonymous/binds)
    └── DDEV issues -> references/ddev-troubleshooting.md
```

## Quick Start

### Basic Docker Workflow

```bash
# Create Dockerfile
cat > Dockerfile <<EOF
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
EXPOSE 3000
USER node
CMD ["node", "server.js"]
EOF

# Build and run
docker build -t myapp:1.0 .
docker run -d -p 3000:3000 --name myapp myapp:1.0
```

See: `references/docker-basics.md`

### Docker Compose Multi-Container App

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      - DATABASE_URL=postgresql://user:***@db:5432/app

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "user"]
      interval: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      retries: 5

volumes:
  postgres_data:
```

See: `references/docker-compose.md`

## Core Docker Concepts

### Dockerfile Best Practices

```dockerfile
# Use specific versions (not latest)
FROM node:20.11.0-alpine3.19

# Set working directory
WORKDIR /app

# Copy dependency files first (better caching)
COPY package*.json ./
RUN npm ci --only=production

# Copy application code
COPY . .

# Set environment variables
ENV NODE_ENV=production

# Document exposed ports
EXPOSE 3000

# Create and use non-root user (security)
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

# Default command
CMD ["node", "server.js"]
```

### Multi-Stage Builds

```dockerfile
# Stage 1: Build
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production (smaller image)
FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

**Benefits:** Smaller images, improved security, no build tools in production.

### .dockerignore

```
node_modules
.git
.env
*.log
.DS_Store
README.md
docker-compose.yml
dist
coverage
```

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Using `FROM:latest` tag | Non-reproducible builds; breakage when base image updates | Pin specific version: `node:20.11.0-alpine3.19` |
| Running as root in production | Security vulnerability; container escape risk | Create non-root user: `RUN adduser -S appuser` then `USER appuser` |
| Single-stage build for compiled apps | Build tools and dev deps in production image (1GB+ vs 200MB) | Multi-stage build: compile in build stage, copy artifacts to slim production stage |
| No .dockerignore | `node_modules`, `.git`, build artifacts copied into image, bloating size | Create .dockerignore excluding `node_modules`, `.git`, `dist`, `coverage`, `.env` |
| No health checks in Compose | Services start before dependencies ready; connection refused errors | Add `healthcheck` to each service, use `depends_on: condition: service_healthy` |
| Anonymous volumes for data | `docker compose down` removes data; data loss on cleanup | Use named volumes: `volumes: { postgres_data: }` and reference by name |
| COPY all files before RUN install | Any source change invalidates dependency cache; slow rebuilds | COPY `package*.json` first, RUN install, then COPY source (dependency layer caches) |
| No restart policy in production | Container stays down after crash or host reboot | Add `restart: unless-stopped` to production services |
| No resource limits | Runaway container starves host; OOM kills other services | Set `deploy.resources.limits.memory` and `cpus` per service |
| Missing `EXPOSE` documentation | Unclear which ports the container uses; conflicts | Document with `EXPOSE` even though it doesn't publish ports |
| Separate `RUN chown` after COPY | Creates extra layer; wastes image space | Use `COPY --chown=appuser:appgroup` in one step |

## Best Practices

### Dockerfiles
- Use specific image versions, not `latest`
- Run as non-root user
- Multi-stage builds to minimize size
- Implement health checks
- Set resource limits
- Keep images under 500MB
- Scan for vulnerabilities regularly

### Docker Compose
- Use named volumes for data persistence
- Implement health checks for all services
- Set restart policies for production
- Use environment-specific compose files
- Configure resource limits
- Enable logging with size limits
- Network isolation with custom networks

### Development Environments
- Use consistent port allocation across worktrees
- Isolate browser state for parallel testing
- Copy .env files when creating worktrees
- Configure CORS for worktree frontend ports
- Stop services when not in use

## Quick Reference

| Task | Command |
|------|---------|
| Build | `docker build -t myapp:1.0 .` |
| Run | `docker run -d -p 8080:3000 myapp:1.0` |
| Logs | `docker logs -f myapp` |
| Shell | `docker exec -it myapp /bin/sh` |
| Stop | `docker stop myapp` |
| Remove | `docker rm myapp` |
| Compose up | `docker compose up -d` |
| Compose down | `docker compose down` |
| Clean all | `docker system prune -a --volumes` |

## Scripts Reference

| Script | Purpose |
|--------|---------|
| `scripts/docker_optimize.py` | Analyze and optimize Dockerfiles |
| `scripts/validate-prerequisites.sh` | Check Docker, DDEV installation |
| `scripts/worktree-manager.sh` | Manage isolated worktree environments |
| `scripts/setup-mcp-isolation.sh` | Configure browser MCP isolation |
| `scripts/validate-worktree-connectivity.sh` | Test worktree service connectivity |
| `scripts/test-isolation.sh` | Test browser isolation |
| `scripts/migrate-browser-isolation.sh` | Migrate to new isolation config |

## Reference Navigation

| Topic | Reference File |
|-------|----------------|
| Docker basics and Dockerfile | `references/docker-basics.md` |
| Docker Compose orchestration | `references/docker-compose.md` |
| Extended patterns and examples | `references/extended-patterns.md` |
| Ghostmind meta.json config | `references/docker-meta-config.md` |
| Worktree Docker strategy | `references/docker-worktree-strategy.md` |
| Port allocation | `references/port-allocation.md` |
| Browser isolation | `references/browser-isolation.md` |
| CORS configuration | `references/cors-configuration.md` |
| Docker troubleshooting | `references/docker-troubleshooting.md` |
| DDEV quickstart | `references/ddev-quickstart.md` |
| DDEV advanced options | `references/ddev-advanced-options.md` |
| DDEV prerequisites | `references/ddev-prerequisites.md` |
| DDEV troubleshooting | `references/ddev-troubleshooting.md` |

## Resources

- **Docker Docs:** https://docs.docker.com
- **Docker Compose:** https://docs.docker.com/compose/
- **Dockerfile Reference:** https://docs.docker.com/engine/reference/builder/
- **DDEV:** https://ddev.readthedocs.io/
- **Docker Security:** https://docs.docker.com/engine/security/

## Integration

- **cicd-pipelines** -- Build and deploy Docker images this skill creates
- **workflow-automation** -- Automate deployment workflows using Docker containers
- **debugging** -- Debug containerized applications and CI/CD failures
- **testing-framework** -- Set up testing infrastructure inside containers
