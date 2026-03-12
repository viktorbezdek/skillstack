# Docker Containerization - Extended Patterns & Examples

Detailed Docker configurations, compose patterns, development environment setup, and troubleshooting extracted from the core skill.

## Docker Compose Patterns

### Environment-Specific Configs

**compose.yml (base):**
```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
```

**compose.override.yml (dev, auto-loaded):**
```yaml
services:
  web:
    volumes:
      - ./src:/app/src  # Live reload
    environment:
      - NODE_ENV=development
    command: npm run dev
```

**compose.prod.yml (production):**
```yaml
services:
  web:
    image: registry.example.com/myapp:1.0
    restart: always
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

**Usage:**
```bash
# Development (uses compose.yml + compose.override.yml)
docker compose up

# Production
docker compose -f compose.yml -f compose.prod.yml up -d
```

### Health Checks

```yaml
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 3s
      start_period: 40s
      retries: 3
```

---

## Development Environment Setup

### DDEV for PHP/TYPO3 Projects

DDEV creates Docker-based development environments with:
- Automatic TYPO3 multi-version testing (11.5, 12.4, 13.4)
- Apache/Nginx configuration
- Database services (MariaDB/PostgreSQL)
- Redis/Valkey caching

**Generated Structure:**
```
.ddev/
  config.yaml
  docker-compose.web.yaml
  apache/apache-site.conf
  web-build/Dockerfile
  commands/web/
    install-v11
    install-v12
    install-v13
    install-all
```

**Access URLs:**
| Environment | URL Pattern |
|-------------|-------------|
| Overview | `https://{sitename}.ddev.site/` |
| TYPO3 v13 | `https://v13.{sitename}.ddev.site/typo3/` |
| Docs | `https://docs.{sitename}.ddev.site/` |

See: `references/ddev-quickstart.md`, `references/ddev-advanced-options.md`

### Worktree Isolation Strategy

For parallel development, each Git worktree gets isolated Docker services:

**Port Allocation:**
| Service | Main | Worktree 1 | Worktree 2 |
|---------|------|------------|------------|
| Backend | 3000 | 3001 | 3002 |
| Frontend | 4000 | 4001 | 4002 |
| Database | 5433 | 5434 | 5435 |
| Chrome DevTools | 9222 | 9223 | 9224 |

**Worktree Docker Compose:**
```yaml
# docker-compose.worktree.yml
services:
  backend-feature-auth:
    container_name: backend-feature-auth
    ports:
      - "3001:3000"

  frontend-feature-auth:
    container_name: frontend-feature-auth
    ports:
      - "4001:4000"

  chrome-devtools-mcp-feature-auth:
    container_name: chrome-devtools-mcp-feature-auth
    ports:
      - "9223:9222"
    volumes:
      - chrome_devtools_data_feature-auth:/data
```

See: `references/docker-worktree-strategy.md`, `references/port-allocation.md`

### Browser Isolation for Testing

Each worktree/environment can have isolated browser containers:

```yaml
# Chrome DevTools container per worktree
chrome-devtools-mcp:
  container_name: chrome-devtools-mcp-{worktree-name}
  image: zenika/alpine-chrome:with-node
  ports:
    - "{allocated-port}:9222"
  volumes:
    - chrome_devtools_data_{worktree-name}:/data
  command: ["chromium-browser", "--remote-debugging-port=9222", "--headless"]
```

**MCP Configuration:**
```json
{
  "chrome-devtools": {
    "command": "docker",
    "args": ["exec", "-i", "chrome-devtools-mcp-{worktree-name}", "..."],
    "env": {
      "CHROME_USER_DATA_DIR": "/data",
      "CHROME_REMOTE_DEBUGGING_PORT": "9222"
    }
  }
}
```

See: `references/browser-isolation.md`

---

## Container Optimization

### Image Size Reduction

```bash
# Analyze Dockerfile
python scripts/docker_optimize.py Dockerfile

# Common optimizations:
# 1. Use alpine base images
# 2. Multi-stage builds
# 3. Combine RUN commands
# 4. Clean package manager cache
# 5. Remove unnecessary files
```

**Before/After Example:**
```dockerfile
# Before: 850MB
FROM node:20
RUN npm install
COPY . .

# After: 150MB
FROM node:20-alpine AS build
RUN npm ci --only=production
COPY . .

FROM node:20-alpine
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
```

### Security Hardening

```dockerfile
# Use specific versions
FROM node:20.11.0-alpine3.19

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Set ownership
COPY --chown=nodejs:nodejs . .

# Switch to non-root
USER nodejs

# Scan for vulnerabilities
# docker scout cves myapp:1.0
```

---

## Meta-Configuration Systems

### Ghostmind meta.json Docker Config

For systems using meta.json as central configuration:

```json
{
  "docker": {
    "image": "${PROJECT}/${APP}:${VERSION}",
    "context": ".",
    "dockerfile": "Dockerfile"
  },
  "compose": {
    "file": "compose.yaml",
    "services": ["app", "db"]
  }
}
```

**Run commands:**
```bash
run docker build
run compose up
run compose down
```

See: `references/docker-meta-config.md`

---

## Common Workflows

### Development to Production

```yaml
# 1. Local Development
docker compose up -d  # Uses compose.override.yml

# 2. Build Production Image
docker build -t myapp:1.0 .

# 3. Test Production Image
docker run -p 3000:3000 myapp:1.0

# 4. Push to Registry
docker push registry.example.com/myapp:1.0

# 5. Deploy
docker compose -f compose.yml -f compose.prod.yml up -d
```

### CI/CD Pipeline

```yaml
# GitHub Actions example
name: Build and Deploy
on: push

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Run tests
        run: docker run myapp:${{ github.sha }} npm test

      - name: Push to registry
        run: |
          docker tag myapp:${{ github.sha }} registry/myapp:latest
          docker push registry/myapp:latest
```

---

## Troubleshooting

### Container exits immediately
```bash
docker logs myapp
docker run -it myapp /bin/sh
docker run -it --entrypoint /bin/sh myapp
```

### Port conflicts
```bash
# Check what's using a port
lsof -i :3000
docker ps --format "{{.Names}}\t{{.Ports}}"

# Stop conflicting services
docker stop <container>
```

### Out of disk space
```bash
docker system df
docker system prune -a
docker volume prune
```

### Build cache issues
```bash
docker build --no-cache -t myapp .
docker builder prune
```

See: `references/docker-troubleshooting.md`

---

## Templates Reference

| Template | Purpose |
|----------|---------|
| `templates/docker-compose.worktree.template.yml` | Worktree Docker Compose |
| `templates/mcp.template.json` | MCP browser isolation config |
| `templates/start-worktree.template.sh` | Worktree startup script |
| `templates/ghostmind-compose.yaml` | Ghostmind Compose template |
| `templates/ghostmind-meta.json` | Ghostmind meta.json template |
| `templates/ddev/*` | DDEV configuration templates |
