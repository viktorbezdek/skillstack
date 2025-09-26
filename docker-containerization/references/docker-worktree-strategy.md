# Docker Compose Strategy Reference

## Overview

Worktrees use Docker Compose extension pattern to inherit services from the main project while customizing port mappings for isolation. This approach avoids duplicating service definitions and ensures consistency across worktrees.

## Extension Pattern

### Main Project Configuration
The main project's `docker-compose.yml` defines base services:

```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "3000:3000"
    env_file:
      - ./backend/.env
    volumes:
      - ./backend:/app
    depends_on:
      - db
      - redis

  frontend:
    build: ./frontend
    ports:
      - "4000:4000"
    env_file:
      - ./frontend/.env
    volumes:
      - ./frontend:/app
    depends_on:
      - backend

  db:
    image: postgres:14
    ports:
      - "5433:5432"
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### Worktree Override Configuration
Each worktree generates a `docker-compose.worktree.yml` that extends the main config:

```yaml
version: '3.8'

services:
  backend:
    extends:
      file: ../SoftTrak/docker-compose.yml
      service: backend
    ports:
      - "3001:3000"  # External port changed, internal port same
    container_name: backend-feature-auth  # Unique container name

  frontend:
    extends:
      file: ../SoftTrak/docker-compose.yml
      service: frontend
    ports:
      - "4001:4000"
    container_name: frontend-feature-auth

  db:
    extends:
      file: ../SoftTrak/docker-compose.yml
      service: db
    ports:
      - "5434:5432"
    container_name: db-feature-auth

  redis:
    extends:
      file: ../SoftTrak/docker-compose.yml
      service: redis
    ports:
      - "6380:6379"
    container_name: redis-feature-auth

# Volumes are shared with main project
# No need to redefine unless worktree needs isolation
```

### Combined Usage
Start worktree services with both config files:

```bash
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml up
```

## Service Isolation

### Container Names
Each worktree service gets a unique container name:
- Pattern: `<service>-<worktree-name>`
- Example: `backend-feature-auth`, `frontend-feature-auth`

**Benefits**:
- Prevents name conflicts with main project
- Enables targeted container management
- Allows parallel service execution

### Port Mappings
External ports are auto-incremented per worktree:
- Backend: `3001+` (maps to internal `3000`)
- Frontend: `4001+` (maps to internal `4000`)
- Database: `5434+` (maps to internal `5432`)
- Redis: `6380+` (maps to internal `6379`)

**Note**: Internal container ports remain the same; only external host ports change.

### Volume Management
Worktrees share volumes with the main project by default:
- `postgres_data` - Shared database volume
- Other named volumes inherit from main config

**Isolation option** (if needed):
```yaml
volumes:
  postgres_data_feature_auth:  # Worktree-specific volume
    driver: local
```

## Service Management

### Starting Services
**Option 1: Generated startup script**
```bash
cd /path/to/worktree
./start-worktree.sh
```

**Option 2: Direct docker-compose**
```bash
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml up -d
```

**Option 3: During worktree creation**
```bash
@worktree create feature-auth --start-services
```

### Stopping Services
**Option 1: Worktree command**
```bash
@worktree stop feature-auth
```

**Option 2: Direct docker-compose**
```bash
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml down
```

**Note**: Only stops worktree containers, does not affect main project.

### Checking Status
```bash
# View running containers
docker ps | grep feature-auth

# Check logs
docker logs backend-feature-auth
docker logs frontend-feature-auth

# Worktree status command
@worktree status feature-auth
```

## Configuration Patterns

### Environment Variables
Each worktree copies `.env` files from main project:

```bash
worktree/
├── backend/.env      # Copied from main/backend/.env
├── frontend/.env     # Copied from main/frontend/.env
└── .env             # Copied from main/.env
```

**Port override** (automatic):
```bash
# backend/.env (worktree)
PORT=3001             # Changed from 3000
DATABASE_URL=postgresql://user:password@localhost:5434/myapp  # Port updated

# frontend/.env (worktree)
PORT=4001             # Changed from 4000
BACKEND_URL=http://localhost:3001  # Points to worktree backend
```

### Network Configuration
Worktrees use the default Docker network from main project:

```yaml
networks:
  default:
    name: softtrak_default  # Shared network
```

**Benefits**:
- Services across main and worktrees can communicate
- Shared DNS resolution
- No additional network configuration needed

### Custom Service Configuration
If a worktree needs additional configuration:

```yaml
# docker-compose.worktree.yml
services:
  backend:
    extends:
      file: ../SoftTrak/docker-compose.yml
      service: backend
    ports:
      - "3001:3000"
    environment:
      - DEBUG=true                    # Extra env var
      - LOG_LEVEL=verbose
    volumes:
      - ./custom-config:/app/config  # Additional volume
```

## Troubleshooting

### Service Won't Start
**Issue**: Container fails to start in worktree

**Solutions**:
```bash
# Check port conflicts
lsof -i :3001
@worktree ports feature-auth

# Check container logs
docker logs backend-feature-auth

# Verify .env files exist
ls -la backend/.env frontend/.env

# Restart with fresh containers
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml down
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml up -d
```

### Can't Access Service
**Issue**: Service running but not accessible

**Solutions**:
```bash
# Verify port mapping
docker ps | grep feature-auth

# Check if service is listening
docker exec backend-feature-auth netstat -tuln

# Test connection
curl http://localhost:3001/health
```

### Database Connection Issues
**Issue**: Backend can't connect to database

**Solutions**:
```bash
# Check database is running
docker ps | grep db-feature-auth

# Verify connection string in backend/.env
# Should use worktree's database port (5434)
DATABASE_URL=postgresql://user:password@localhost:5434/myapp

# Test database connection
docker exec db-feature-auth psql -U user -d myapp -c "SELECT 1"
```

### Volume Permission Issues
**Issue**: Services can't write to volumes

**Solutions**:
```bash
# Check volume permissions
docker exec backend-feature-auth ls -la /app

# Fix permissions (if needed)
sudo chown -R $USER:$USER ./backend

# Or run containers with user context
# Add to docker-compose.worktree.yml:
services:
  backend:
    user: "${UID}:${GID}"
```

## Best Practices

1. **Use generated startup script**: `./start-worktree.sh` handles all configuration automatically
2. **Don't modify main docker-compose.yml**: Keep main project config unchanged
3. **Stop services when done**: Free resources with `@worktree stop <name>`
4. **Check logs regularly**: Monitor container health with `docker logs`
5. **Clean up unused containers**: Remove stopped containers with `docker container prune`
6. **Use separate volumes**: For worktrees needing database isolation
7. **Test port availability**: Before starting services, verify ports are free
8. **Keep main project stopped**: When working in worktrees to avoid conflicts

## Advanced Patterns

### Database Isolation
For complete database isolation:

```yaml
# docker-compose.worktree.yml
services:
  db:
    extends:
      file: ../SoftTrak/docker-compose.yml
      service: db
    ports:
      - "5434:5432"
    volumes:
      - postgres_data_feature_auth:/var/lib/postgresql/data

volumes:
  postgres_data_feature_auth:
    driver: local
```

### Additional Services
Add worktree-specific services:

```yaml
# docker-compose.worktree.yml
services:
  # ... existing services ...

  test-runner:
    build: ./test-runner
    ports:
      - "8080:8080"
    depends_on:
      - backend
    volumes:
      - ./tests:/tests
```

### Production-like Staging
Use worktree for staging environment:

```yaml
# docker-compose.worktree.yml
services:
  backend:
    extends:
      file: ../SoftTrak/docker-compose.yml
      service: backend
    environment:
      - NODE_ENV=staging
      - ENABLE_MONITORING=true
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```
