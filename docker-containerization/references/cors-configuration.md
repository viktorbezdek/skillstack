# CORS Configuration in Worktrees

## Overview

The worktree management skill automatically configures Cross-Origin Resource Sharing (CORS) to ensure your worktree's frontend can communicate with the backend API without errors.

## What Gets Configured

When you create a new worktree, the skill automatically:

1. **Updates `backend/.env`**
   - Adds your worktree's frontend port to `ALLOWED_ORIGINS`
   - Example: `ALLOWED_ORIGINS=http://localhost:4000,...,http://localhost:4004`

2. **Updates `backend/config/initializers/cors.rb`**
   - Adds your worktree's frontend port to the development defaults array
   - Ensures CORS works even if environment variable isn't loaded
   - Example: `allowed_origins = ["http://localhost:4000", ..., "http://localhost:4004"]`

## Why This Matters

Without proper CORS configuration, you would encounter errors like:

```
Access to XMLHttpRequest at 'http://localhost:3000/api/v1/auth/login'
from origin 'http://localhost:4004' has been blocked by CORS policy:
No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

These errors prevent:
- Login functionality
- API calls
- Authentication
- Data fetching
- Form submissions

## Automatic Configuration Process

During worktree creation:

```bash
@worktree create feature-branch --start-services
```

The skill performs these steps:

1. **Copies `.env` file** from main project to worktree
2. **Detects allocated frontend port** (e.g., 4004)
3. **Checks if `ALLOWED_ORIGINS` exists** in `.env`
4. **Adds frontend port** to `ALLOWED_ORIGINS` if not already present
5. **Updates `cors.rb`** with the same frontend port
6. **Provides console feedback** showing CORS was configured

Console output example:
```
📋 Copying environment files...
🔧 Configuring CORS for worktree port 4004...
   ✅ Added http://localhost:4004 to ALLOWED_ORIGINS
   ✅ Added http://localhost:4004 to cors.rb development defaults
   ✅ Copied backend/.env
```

## Configuration Files

### backend/.env
```bash
# CORS Settings
ALLOWED_ORIGINS=http://localhost:4000,http://localhost:4001,http://localhost:4002,http://localhost:4003,http://localhost:4004,http://localhost:5173,http://localhost:3000
```

### backend/config/initializers/cors.rb
```ruby
if Rails.env.development? && allowed_origins.empty?
  allowed_origins = [
    "http://localhost:4000",
    "http://localhost:4001",
    "http://localhost:4002",
    "http://localhost:4003",
    "http://localhost:4004",  # Your worktree port
    "http://localhost:5173",
    "http://localhost:3000"
  ]
  puts "CORS: No ALLOWED_ORIGINS environment variable set, using development defaults: #{allowed_origins.join(', ')}"
end
```

## Idempotency

The CORS configuration is **idempotent**, meaning:
- Running worktree creation multiple times won't duplicate ports
- Existing ports are detected and skipped
- Safe to re-run without issues

## Manual Verification

To verify CORS is properly configured in your worktree:

### 1. Check .env file
```bash
cd /path/to/worktree
grep ALLOWED_ORIGINS backend/.env
```

Should show your worktree's frontend port.

### 2. Check cors.rb
```bash
grep -A3 "Rails.env.development" backend/config/initializers/cors.rb
```

Should include your worktree's frontend port in the array.

### 3. Check backend logs
```bash
docker logs <worktree-backend-container> 2>&1 | grep "CORS: Configured"
```

Should show: `CORS: Configured allowed origins: http://localhost:4000, ..., http://localhost:4004`

## Troubleshooting

### Issue: CORS errors despite configuration

**Symptom:**
```
No 'Access-Control-Allow-Origin' header is present
```

**Solutions:**

1. **Restart backend container** to pick up configuration changes:
```bash
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml restart backend
```

2. **Verify environment variables loaded:**
```bash
docker exec <worktree-backend-container> printenv | grep ALLOWED_ORIGINS
```

3. **Force recreate container** to reload .env:
```bash
docker-compose -f docker-compose.yml -f docker-compose.worktree.yml up -d --force-recreate backend
```

### Issue: Port not in ALLOWED_ORIGINS

**Symptom:** Your frontend port is missing from CORS configuration

**Solutions:**

1. **Manually add to .env:**
```bash
cd /path/to/worktree
# Edit backend/.env and add your port:
ALLOWED_ORIGINS=http://localhost:4000,...,http://localhost:YOUR_PORT
```

2. **Manually add to cors.rb:**
```bash
# Edit backend/config/initializers/cors.rb
# Add your port to the development defaults array:
allowed_origins = ["http://localhost:4000", ..., "http://localhost:YOUR_PORT"]
```

3. **Recreate worktree** with latest skill version that includes auto-configuration

### Issue: Multiple ports for same worktree

**Symptom:** Duplicate port entries in CORS configuration

**Solutions:**

1. **Edit .env manually** and remove duplicates
2. **Edit cors.rb manually** and remove duplicates
3. **Restart backend container** after cleanup

## Best Practices

1. **Always use `--start-services` flag** when creating worktrees to ensure CORS is configured before backend starts
2. **Verify CORS after creation** by checking backend logs
3. **Don't manually edit CORS configs** in worktrees unless necessary (auto-configuration handles it)
4. **Keep worktree `.env` files in `.gitignore`** to prevent committing worktree-specific configs
5. **Update main project first** if adding new common ports, then create worktrees

## Related Documentation

- [Port Allocation Strategy](port-allocation.md)
- [Docker Strategy](docker-strategy.md)
- [Troubleshooting Guide](troubleshooting.md)
- [Main Skill Documentation](../SKILL.md)

## Technical Implementation

The CORS auto-configuration uses:
- `sed` for in-place file modifications
- `grep` for detecting existing configuration
- Backup files (`.bak`) that are automatically cleaned up
- Conditional logic to ensure idempotency
- Clear console feedback for visibility

Implementation location: `scripts/worktree-manager.sh` lines 520-554
