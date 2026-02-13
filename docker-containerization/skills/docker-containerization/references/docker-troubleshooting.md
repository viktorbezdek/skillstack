# Troubleshooting Guide

## Common Issues and Solutions

### Port Conflicts

#### Issue: "Port already in use" Error
**Symptoms**: Docker services fail to start, error message indicates port is already allocated.

**Diagnosis**:
```bash
# Check which process is using the port
lsof -i :3001

# Check Docker containers using the port
docker ps -a | grep 3001

# View all worktree port allocations
@worktree ports
```

**Solutions**:

**Option 1: Stop Conflicting Service**
```bash
# If main project is running
cd /path/to/main/project
docker-compose down

# If another worktree is running
@worktree stop <other-worktree-name>

# If system process is using port
kill <process-id>  # Use PID from lsof output
```

**Option 2: Use Different Ports**
```bash
# Remove and recreate worktree (gets new ports)
@worktree remove <name>
@worktree create <name>
```

**Option 3: Manual Port Cleanup**
```bash
# Free ports in registry
vim ~/.claude/skills/worktree-management/port-registry.json
# Remove the worktree's port allocations

# Then recreate worktree
@worktree create <name>
```

### Docker Service Issues

#### Issue: Docker Services Won't Start
**Symptoms**: `docker-compose up` fails, containers exit immediately, health checks fail.

**Diagnosis**:
```bash
# Check container status
docker ps -a | grep <worktree-name>

# View container logs
docker logs backend-<worktree-name>
docker logs frontend-<worktree-name>

# Check Docker daemon
docker info
```

**Solutions**:

**Missing .env Files**:
```bash
# Check if .env files exist
ls -la backend/.env frontend/.env .env

# Copy from main project if missing
cp /path/to/main/backend/.env ./backend/.env
cp /path/to/main/frontend/.env ./frontend/.env
cp /path/to/main/.env ./.env
```

**Container Build Issues**:
```bash
# Rebuild containers
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml build --no-cache

# Pull fresh images
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml pull
```

**Permission Issues**:
```bash
# Fix volume permissions
sudo chown -R $USER:$USER ./backend ./frontend

# Check Docker socket permissions
ls -la /var/run/docker.sock
```

#### Issue: Can't Connect to Database
**Symptoms**: Backend can't connect to database, connection timeout or refused errors.

**Diagnosis**:
```bash
# Check database container
docker ps | grep db-<worktree-name>

# Check database logs
docker logs db-<worktree-name>

# Test connection from host
psql -h localhost -p 5434 -U user -d myapp
```

**Solutions**:

**Incorrect Connection String**:
```bash
# Verify backend/.env has correct database port
cat backend/.env | grep DATABASE_URL

# Should be: postgresql://user:password@localhost:5434/myapp
# NOT: postgresql://user:password@localhost:5433/myapp (main port)
```

**Database Not Running**:
```bash
# Start database container
docker start db-<worktree-name>

# Or restart all services
./start-worktree.sh
```

**Database Initialization Failed**:
```bash
# Remove database volume and recreate
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml down -v
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml up -d
```

### Browser Automation Issues

#### Issue: Browser Sessions Conflicting
**Symptoms**: Tests fail unexpectedly, cookies from one worktree affect another, authentication issues.

**Diagnosis**:
```bash
# Check browser data directories exist
ls -la .browser-data/

# Verify MCP configuration
cat .mcp.json | grep -A 5 "playwright"
cat .mcp.json | grep -A 5 "chrome-devtools"

# Check browser processes
ps aux | grep chrome
ps aux | grep playwright
```

**Solutions**:

**Browser Data Directory Missing**:
```bash
# Create directories manually
mkdir -p .browser-data/playwright
mkdir -p .browser-data/chrome-devtools
mkdir -p .browser-data/puppeteer

# Set permissions
chmod -R 755 .browser-data
```

**Incorrect MCP Configuration**:
```bash
# Regenerate .mcp.json from template
cp ~/.claude/skills/worktree-management/assets/mcp.template.json .mcp.json

# Update paths in .mcp.json to match worktree
# Replace <WORKTREE_PATH> with actual worktree path
```

**Browser Debugging Port Conflicts**:
```bash
# Check port allocations
@worktree ports <name>

# Verify unique debugging ports
# Playwright: 9224+ (even numbers)
# Chrome DevTools: 9226+ (even numbers)
# Puppeteer: 9228+ (even numbers)

# If conflicts, recreate worktree
@worktree remove <name>
@worktree create <name>
```

### Git Worktree Issues

#### Issue: Worktree Creation Failed
**Symptoms**: `git worktree add` fails, worktree directory partially created.

**Diagnosis**:
```bash
# Check existing worktrees
git worktree list

# Check for orphaned worktrees
git worktree prune

# Verify branch status
git branch -a
```

**Solutions**:

**Branch Already Exists**:
```bash
# Use different branch name
@worktree create feature-auth-v2 --branch=feature/auth-v2

# Or delete existing branch (if safe)
git branch -D feature/auth
@worktree create feature-auth
```

**Uncommitted Changes in Main**:
```bash
# Commit or stash changes
git add .
git commit -m "WIP"
# OR
git stash

# Then retry worktree creation
@worktree create <name>
```

**Insufficient Disk Space**:
```bash
# Check disk space
df -h

# Clean up Docker
docker system prune -a

# Remove unused worktrees
@worktree list
@worktree remove <unused-worktree>
```

#### Issue: Can't Remove Worktree
**Symptoms**: `@worktree remove` fails, worktree directory still exists, registry not updated.

**Diagnosis**:
```bash
# Check for running containers
docker ps | grep <worktree-name>

# Check for uncommitted changes
cd /path/to/worktree
git status

# Check for locked files
lsof +D /path/to/worktree
```

**Solutions**:

**Services Still Running**:
```bash
# Stop services first
@worktree stop <name>

# Then retry removal
@worktree remove <name>
```

**Uncommitted Changes**:
```bash
# Commit changes
cd /path/to/worktree
git add .
git commit -m "Save work"

# Or force removal (loses changes)
@worktree remove <name> --force
```

**Manual Cleanup Required**:
```bash
# Force remove Git worktree
git worktree remove <path> --force

# Manually delete directory
rm -rf /path/to/worktree

# Update registry
vim ~/.claude/skills/worktree-management/worktrees.json
# Remove the worktree entry
```

### State Management Issues

#### Issue: Registry Out of Sync
**Symptoms**: `@worktree list` shows incorrect information, port conflicts despite available ports.

**Diagnosis**:
```bash
# Check registry files
cat ~/.claude/skills/worktree-management/worktrees.json
cat ~/.claude/skills/worktree-management/port-registry.json

# Check actual Git worktrees
git worktree list

# Check actual Docker containers
docker ps -a
```

**Solutions**:

**Manual Registry Repair**:
```bash
# Edit worktree registry
vim ~/.claude/skills/worktree-management/worktrees.json

# Remove entries for non-existent worktrees
# Update status for existing worktrees

# Edit port registry
vim ~/.claude/skills/worktree-management/port-registry.json

# Free ports for removed worktrees
```

**Full Registry Reset** (CAUTION):
```bash
# Backup registries
cp ~/.claude/skills/worktree-management/worktrees.json ~/worktrees.json.backup
cp ~/.claude/skills/worktree-management/port-registry.json ~/port-registry.json.backup

# Reset registries
echo '{"main_project":"","worktrees":[]}' > ~/.claude/skills/worktree-management/worktrees.json
echo '{"allocations":[],"next_available":{}}' > ~/.claude/skills/worktree-management/port-registry.json

# Recreate worktrees
# (This will lose worktree tracking but not the Git worktrees themselves)
```

### Environment File Issues

#### Issue: Missing .env Files
**Symptoms**: Services fail with "env file not found", environment variables undefined.

**Diagnosis**:
```bash
# Check if .env files exist in worktree
ls -la backend/.env frontend/.env .env

# Check if .env files exist in main project
ls -la /path/to/main/backend/.env

# Check Docker logs for env var errors
docker logs backend-<worktree-name>
```

**Solutions**:

**Copy from Main Project**:
```bash
# Copy all .env files
cp /path/to/main/backend/.env ./backend/.env
cp /path/to/main/frontend/.env ./frontend/.env
cp /path/to/main/.env ./.env

# Restart services
./start-worktree.sh
```

**Create Minimal .env Files**:
```bash
# backend/.env
cat > backend/.env << 'EOF'
PORT=3001
DATABASE_URL=postgresql://user:password@localhost:5434/myapp
NODE_ENV=development
EOF

# frontend/.env
cat > frontend/.env << 'EOF'
PORT=4001
BACKEND_URL=http://localhost:3001
NODE_ENV=development
EOF
```

#### Issue: Incorrect Port Configuration
**Symptoms**: Services start but frontend can't reach backend, database connections fail.

**Diagnosis**:
```bash
# Check port configuration in .env files
grep -r "PORT\|URL" backend/.env frontend/.env

# Check actual ports services are using
docker ps | grep <worktree-name>
```

**Solutions**:

**Update .env Files**:
```bash
# Update backend/.env
# Change PORT to match worktree's allocated backend port
PORT=3001  # Not 3000

# Update DATABASE_URL to use worktree's database port
DATABASE_URL=postgresql://user:password@localhost:5434/myapp  # Not 5433

# Update frontend/.env
# Change PORT to match worktree's allocated frontend port
PORT=4001  # Not 4000

# Update BACKEND_URL to point to worktree's backend
BACKEND_URL=http://localhost:3001  # Not 3000

# Restart services
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml restart
```

## Diagnostic Commands

### Quick Health Check
```bash
# Check worktree status
@worktree status <name>

# Check all port allocations
@worktree ports

# Check Docker containers
docker ps | grep <worktree-name>

# Check Git worktrees
git worktree list
```

### Detailed Investigation
```bash
# View all service logs
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml logs

# Check specific service
docker logs --tail 100 backend-<worktree-name>

# Check network connectivity
docker network inspect softtrak_default

# Check volume mounts
docker inspect backend-<worktree-name> | grep -A 10 Mounts
```

## Getting Help

If issues persist after trying these solutions:

1. **Check skill version**: Ensure using latest worktree-management skill
2. **Review recent changes**: Check `git log` for any project configuration changes
3. **Test with fresh worktree**: Create new worktree to isolate issue
4. **Check Docker health**: Run `docker info` and `docker version`
5. **Review system resources**: Check available disk space, memory, CPU

## Prevention Best Practices

1. **Always check status**: Run `@worktree status <name>` before starting work
2. **Stop when done**: Free resources with `@worktree stop <name>`
3. **Sync regularly**: Update with `@worktree sync <name>` to avoid merge conflicts
4. **Keep registries clean**: Remove unused worktrees promptly
5. **Monitor disk space**: Worktrees and Docker volumes consume storage
6. **Document custom changes**: Note any manual configuration for team reference
7. **Test port availability**: Verify ports before creating new worktrees
8. **Backup registries**: Periodically backup worktrees.json and port-registry.json
