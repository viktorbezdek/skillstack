---
name: docker-containerization
description: Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration, container optimization, development environment setup, and infrastructure patterns.
triggers:
  - Docker
  - container
  - Dockerfile
  - Docker Compose
  - multi-stage build
  - DDEV
  - containerization
  - image optimization
license: MIT
---

# Docker Containerization Skill

Comprehensive guide for Docker containerization covering core concepts, multi-stage builds, Docker Compose orchestration, development environment setup, and advanced patterns for isolated development workflows.

## When to Use This Skill

Use this skill when:

- **Containerization**: Building Docker images, writing Dockerfiles, multi-stage builds
- **Docker Compose**: Setting up multi-container applications, local development environments
- **Development Environments**: Setting up DDEV for TYPO3/PHP projects, creating isolated worktrees
- **Container Optimization**: Analyzing and optimizing Dockerfile efficiency, image size reduction
- **Port Management**: Allocating ports for multiple containers, avoiding conflicts
- **Browser Automation**: Setting up isolated browser containers for testing
- **CI/CD**: Building container images for deployment pipelines
- **Meta-Configuration Systems**: Working with meta.json-driven Docker configurations (Ghostmind)

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
      - db
      - redis
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/app

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

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

See [Extended Patterns](references/extended-patterns.md) for Docker Compose patterns, DDEV setup, worktree isolation, container optimization, CI/CD pipelines, and troubleshooting.

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

## Resources

- **Docker Docs:** https://docs.docker.com
- **Docker Compose:** https://docs.docker.com/compose/
- **Dockerfile Reference:** https://docs.docker.com/engine/reference/builder/
- **DDEV:** https://ddev.readthedocs.io/
- **Docker Security:** https://docs.docker.com/engine/security/
