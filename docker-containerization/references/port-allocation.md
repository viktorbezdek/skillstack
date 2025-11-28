# Port Allocation Reference

## Port Ranges

### Main Project Ports
- Backend: `3000`
- Frontend: `4000`
- Database: `5433`
- Playwright: `9223`
- Chrome DevTools: `9222`
- Puppeteer: `9224`
- Redis: `6379`

### Worktree Port Ranges
Each worktree gets auto-incremented ports starting from:
- Backend: `3001+`
- Frontend: `4001+`
- Database: `5434+`
- Playwright: `9224+` (even numbers)
- Chrome DevTools: `9226+` (even numbers, offset by +4 from main)
- Puppeteer: `9228+` (even numbers, offset by +4 from Playwright)
- Redis: `6380+`

## Port Allocation Algorithm

### Sequential Scanning
The port allocator scans up to 50 sequential ports to find the first available port:

1. **Start from base port** (e.g., 3001 for backend)
2. **Check registry** - Is port already allocated to another worktree?
3. **Check system** - Is port in use by any process? (via `lsof`)
4. **Check Docker** - Is port bound by any container?
5. **If available** - Allocate and register
6. **If occupied** - Increment and repeat (up to 50 attempts)

### Registry Management
The `port-registry.json` file tracks all allocated ports:

```json
{
  "allocations": [
    {
      "worktree": "SoftTrak-feature-auth",
      "ports": {
        "backend": 3001,
        "frontend": 4001,
        "database": 5434,
        "playwright": 9224,
        "chrome_devtools": 9226,
        "puppeteer": 9228,
        "redis": 6380
      }
    }
  ],
  "next_available": {
    "backend": 3002,
    "frontend": 4002,
    "database": 5435
  }
}
```

## Port Conflict Detection

### Pre-Flight Validation
Before starting Docker services, the system validates all 7 required ports:

1. **System Process Check** - `lsof -i :PORT` checks for any process using the port
2. **Docker Container Check** - `docker ps` checks for containers with port bindings
3. **Port Registry Check** - Validates against recorded allocations

### Conflict Resolution

When conflicts are detected, four resolution options are provided:

**Option 1: Stop Specific Containers**
```bash
docker stop <container-name>
```

**Option 2: Stop Main Project**
```bash
cd /path/to/main/project
docker-compose down
```

**Option 3: Stop Other Worktrees**
```bash
@worktree list
@worktree stop <name>
```

**Option 4: Manual Service Startup**
```bash
cd /path/to/worktree
./start-worktree.sh
```

## Best Practices

### Port Management
1. **Stop unused worktrees** - Free ports with `@worktree stop <name>`
2. **Check allocations** - Use `@worktree ports` to see current usage
3. **Keep main stopped** - When working in worktrees, stop main project services
4. **Conflicts are normal** - Follow resolution options provided

### Port Exhaustion Prevention
- Maximum 50 worktrees per project (port range limit)
- Remove unused worktrees to free ports
- Consider using different main project port ranges if exhausted

### Performance
- Port scanning: < 1 second for typical scenarios
- Validation: < 0.5 seconds for all 7 service ports
- Total overhead: < 2 seconds added to worktree creation

## Troubleshooting

### "Port already in use" Error
```bash
# Check what's using the port
lsof -i :3001

# Check Docker containers
docker ps | grep 3001

# Check port registry
@worktree ports
```

### Registry Out of Sync
If the port registry becomes out of sync with actual usage:

```bash
# Manually edit port-registry.json
~/.claude/skills/worktree-management/port-registry.json

# Or remove and recreate worktree
@worktree remove <name>
@worktree create <name>
```

### Port Range Exhaustion
If all ports in range are exhausted (50+ worktrees):

1. Remove unused worktrees: `@worktree remove <name>`
2. Change main project base ports in docker-compose.yml
3. Clear port registry and recreate worktrees
