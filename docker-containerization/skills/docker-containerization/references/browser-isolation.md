# Browser Isolation Reference

## Overview

Each worktree gets its own isolated browser environments to prevent interference between parallel development sessions. This enables running browser automation (Playwright, Puppeteer, Chrome DevTools) in multiple worktrees simultaneously without conflicts.

**✅ UPDATED**: As of the latest version, browser isolation uses a **shared Docker volume** approach for complete isolation between worktrees.

## Isolation Architecture

### Shared Docker Volume Pattern

**Key Design**: All MCP browser containers mount a shared Docker volume `browser-profiles` at `/browser-data/`. Each worktree gets a unique subdirectory named after the worktree.

```
Docker Volume: browser-profiles
└── /browser-data/
    ├── SoftTrak-feature-auth/
    │   ├── playwright/
    │   ├── chrome-devtools/
    │   └── puppeteer/
    ├── SoftTrak-bugfix-ui/
    │   ├── playwright/
    │   ├── chrome-devtools/
    │   └── puppeteer/
    └── SoftTrak-docs-api/
        ├── playwright/
        ├── chrome-devtools/
        └── puppeteer/
```

### Why Shared Volume?

1. **Container Accessibility**: Docker containers can directly access paths within mounted volumes
2. **Proper Isolation**: Each worktree name creates a unique namespace
3. **No Path Translation**: No need to map host paths to container paths
4. **Consistent Across Environments**: Works on Linux, macOS, Windows Docker hosts

### Environment Variables (Updated)

Each worktree's `.mcp.json` file configures browser isolation using **container-internal paths**:

```json
{
  "mcpServers": {
    "playwright": {
      "env": {
        "PLAYWRIGHT_USER_DATA_DIR": "/browser-data/SoftTrak-feature-auth/playwright",
        "PLAYWRIGHT_CHROMIUM_DEBUG_PORT": "9224",
        "PLAYWRIGHT_LAUNCH_OPTIONS": "{\"args\":[\"--remote-debugging-port=9224\",\"--user-data-dir=/browser-data/SoftTrak-feature-auth/playwright\"]}"
      }
    },
    "chrome-devtools": {
      "env": {
        "CHROME_USER_DATA_DIR": "/browser-data/SoftTrak-feature-auth/chrome-devtools",
        "CHROME_REMOTE_DEBUGGING_PORT": "9226",
        "CHROME_ARGS": "--remote-debugging-port=9226 --user-data-dir=/browser-data/SoftTrak-feature-auth/chrome-devtools",
        "CDP_PORT": "9226"
      }
    },
    "puppeteer": {
      "env": {
        "PUPPETEER_USER_DATA_DIR": "/browser-data/SoftTrak-feature-auth/puppeteer",
        "PUPPETEER_LAUNCH_OPTIONS": "{\"args\":[\"--remote-debugging-port=9228\",\"--user-data-dir=/browser-data/SoftTrak-feature-auth/puppeteer\"]}"
      }
    }
  }
}
```

**Key Changes from Previous Version**:
- ✅ Paths now use `/browser-data/{worktree-name}/` (container-internal)
- ✅ Each browser gets unique debugging port configuration
- ✅ Launch options explicitly pass both port and user-data-dir
- ✅ Multiple environment variables ensure compatibility with different MCP implementations

## Browser MCP Configurations

### Chrome DevTools MCP
**Isolation Method**: `--isolated=true` flag (primary) + separate user data directory (backup)
**Ports**: Auto-incremented with +4 offset (9226, 9227, 9228, ...)
**Profiles**: Temporary isolated profiles (auto-cleanup)

**Configuration**:
```json
{
  "args": ["npx", "chrome-devtools-mcp", "--isolated=true"]
}
```

**Isolation Mechanism**:
- `--isolated=true`: Creates temporary profile per browser instance
- Automatic cleanup: Profiles deleted when browser closes
- No profile path conflicts between worktrees
- Each Claude Code session gets completely independent browser

**Benefits**:
- Parallel debugging sessions without interference
- Separate DevTools instances per worktree
- Independent network recording
- No cookie/session conflicts
- Automatic cleanup (no manual maintenance)

**Why `--isolated` Over User Data Directory?**
- chrome-devtools-mcp runs on host (not in Docker), so Docker volume paths are inaccessible
- `--isolated` flag is built-in solution designed for this exact use case
- Temporary profiles prevent state persistence issues
- Simpler and more reliable than path-based isolation

### Playwright MCP
**Isolation**: Separate user data directory per worktree (Docker volume-based)
**Ports**: Auto-incremented (9224, 9225, 9226, ...)
**Profiles**: Isolated Chromium, Firefox, and WebKit profiles

**Benefits**:
- Parallel test execution across worktrees
- Separate browser state and cookies
- Independent screenshot/video recordings
- No interference between test runs

### Puppeteer MCP
**Isolation**: Separate user data directory per worktree (Docker volume-based)
**Ports**: Auto-incremented with +4 offset from Playwright (9228, 9229, 9230, ...)
**Profiles**: Isolated Chromium profiles

**Benefits**:
- Parallel scraping/automation
- Separate browser context
- Independent cache and storage
- No authentication conflicts

## Shared vs Isolated MCPs

### Browser MCPs (Isolated)
These MCPs share the Docker container but isolate browser data:
- **Playwright MCP** - Isolated browser profiles per worktree
- **Chrome DevTools MCP** - Isolated user data per worktree
- **Puppeteer MCP** - Isolated profiles per worktree

### Stateless MCPs (Fully Shared)
These MCPs are stateless and safe to share across worktrees:
- Serena MCP
- Context7 MCP
- Sequential Thinking MCP
- Magic MCP
- Tavily Search MCP
- Gmail MCP
- Task Master MCP
- All other stateless MCPs

## Benefits of Isolation

### Parallel Development
- Run E2E tests in multiple worktrees simultaneously
- Debug different features in parallel without interference
- Test same feature with different configurations

### State Management
- Each worktree maintains separate:
  - Cookies and local storage
  - Browser cache
  - Authentication sessions
  - Form autofill data
  - Browser extensions state

### Debugging Independence
- Separate remote debugging ports per worktree
- Independent DevTools Network panels
- Isolated console logs
- Non-overlapping breakpoints

## Configuration Details

### Automatic Setup
Browser isolation is configured automatically during worktree creation:

1. **Create directory**: `.browser-data/` with subdirectories
2. **Generate `.mcp.json`**: Environment variables with worktree-specific paths
3. **Set permissions**: Ensure browser processes can write to directories
4. **Allocate ports**: Assign unique debugging ports per browser MCP

### Manual Configuration
If browser isolation needs manual adjustment:

```bash
# Check current configuration
cat .mcp.json | grep -A 10 "playwright"

# Verify directory exists
ls -la .browser-data/

# Test browser isolation
# Playwright should create files in .browser-data/playwright/
# Chrome DevTools should use .browser-data/chrome-devtools/
```

## Troubleshooting

### Browser Data Directory Not Created
```bash
# Manually create directories
mkdir -p .browser-data/playwright
mkdir -p .browser-data/chrome-devtools
mkdir -p .browser-data/puppeteer

# Set permissions
chmod -R 755 .browser-data
```

### Port Conflicts Between Browser MCPs
```bash
# Check port allocations
@worktree ports <name>

# Verify no overlap in debugging ports
# Playwright: 9224+ (even numbers)
# Chrome DevTools: 9226+ (even numbers, +4 offset)
# Puppeteer: 9228+ (even numbers, +4 offset from Playwright)
```

### Browser State Not Isolated
```bash
# Verify environment variables in .mcp.json
grep -i "USER_DATA_DIR" .mcp.json

# Check browser processes are using correct directories
ps aux | grep chrome
ps aux | grep playwright
```

### Permission Issues
```bash
# Fix directory permissions
chmod -R 755 .browser-data

# Ensure Docker can access directories
# (May need to adjust Docker volume permissions)
```

## Performance Impact

### Storage
- Each worktree: ~50-200MB browser data (depending on usage)
- Chromium profiles: ~30-100MB
- Firefox profiles: ~20-50MB
- WebKit profiles: ~10-30MB

### Startup Time
- First browser launch: +2-5 seconds (profile initialization)
- Subsequent launches: Normal speed (profiles cached)

### Memory Usage
- Each browser instance: +100-300MB RAM
- Multiple worktrees: Linear memory increase
- Recommendation: 2GB RAM per active worktree with browser automation

## Best Practices

1. **Clean up old browser data**: Remove `.browser-data/` when removing worktrees
2. **Monitor storage usage**: Browser profiles can grow large over time
3. **Use headless mode**: Reduce memory/CPU usage when visual browser not needed
4. **Close unused browsers**: Free resources by closing browser sessions in inactive worktrees
5. **Separate debugging ports**: Ensure unique ports prevent connection conflicts
