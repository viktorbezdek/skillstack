# Installation Guide

Complete installation instructions for {{PROJECT_NAME}} across all supported platforms and package managers.

## System Requirements

### Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| OS | {{MIN_OS}} |
| Memory | {{MIN_RAM}} |
| Disk Space | {{MIN_DISK}} |
| {{RUNTIME}} | {{MIN_RUNTIME_VERSION}} |

### Recommended Requirements

| Component | Recommendation |
|-----------|----------------|
| OS | {{REC_OS}} |
| Memory | {{REC_RAM}} |
| Disk Space | {{REC_DISK}} |
| {{RUNTIME}} | {{REC_RUNTIME_VERSION}} |

## Installation Methods

### Method 1: Package Manager (Recommended)

{{#PACKAGE_MANAGERS}}
#### {{MANAGER_NAME}}

```bash
{{INSTALL_COMMAND}}
```

Verify installation:
```bash
{{VERIFY_COMMAND}}
```
{{/PACKAGE_MANAGERS}}

### Method 2: From Source

```bash
# Clone the repository
git clone {{REPO_URL}}
cd {{PROJECT_NAME}}

# Install dependencies
{{BUILD_DEPS_COMMAND}}

# Build from source
{{BUILD_COMMAND}}

# Install
{{INSTALL_FROM_SOURCE_COMMAND}}
```

### Method 3: Docker

```bash
# Pull the image
docker pull {{DOCKER_IMAGE}}

# Run the container
docker run -d \
  --name {{PROJECT_NAME}} \
  -p {{PORT}}:{{CONTAINER_PORT}} \
  {{DOCKER_RUN_FLAGS}} \
  {{DOCKER_IMAGE}}
```

#### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  {{SERVICE_NAME}}:
    image: {{DOCKER_IMAGE}}
    ports:
      - "{{PORT}}:{{CONTAINER_PORT}}"
    environment:
      {{#DOCKER_ENV_VARS}}
      - {{VAR_NAME}}={{VAR_VALUE}}
      {{/DOCKER_ENV_VARS}}
    volumes:
      - {{VOLUME_MAPPING}}
```

```bash
docker-compose up -d
```

### Method 4: Binary Release

1. Download the latest release for your platform:

| Platform | Download |
|----------|----------|
| Linux (x64) | [{{PROJECT_NAME}}-linux-x64.tar.gz]({{LINUX_URL}}) |
| macOS (x64) | [{{PROJECT_NAME}}-darwin-x64.tar.gz]({{MACOS_URL}}) |
| macOS (ARM) | [{{PROJECT_NAME}}-darwin-arm64.tar.gz]({{MACOS_ARM_URL}}) |
| Windows | [{{PROJECT_NAME}}-win-x64.zip]({{WINDOWS_URL}}) |

2. Extract and install:

```bash
# Linux/macOS
tar -xzf {{PROJECT_NAME}}-*.tar.gz
sudo mv {{PROJECT_NAME}} /usr/local/bin/

# Windows (PowerShell)
Expand-Archive {{PROJECT_NAME}}-win-x64.zip -DestinationPath C:\Program Files\{{PROJECT_NAME}}
```

## Post-Installation Setup

### 1. Initialize Configuration

```bash
{{INIT_COMMAND}}
```

This creates:
- `{{CONFIG_FILE}}` - Main configuration file
- `{{DATA_DIR}}` - Data storage directory

### 2. Verify Installation

```bash
{{VERSION_COMMAND}}
```

Expected output:
```
{{PROJECT_NAME}} version {{VERSION}}
```

### 3. Run Health Check

```bash
{{HEALTH_CHECK_COMMAND}}
```

## Platform-Specific Notes

### Linux

{{LINUX_NOTES}}

### macOS

{{MACOS_NOTES}}

### Windows

{{WINDOWS_NOTES}}

## Upgrading

### From Package Manager

```bash
{{UPGRADE_COMMAND}}
```

### From Source

```bash
cd {{PROJECT_NAME}}
git pull
{{REBUILD_COMMAND}}
```

### Migration Notes

{{#MIGRATION_NOTES}}
#### Upgrading from {{FROM_VERSION}} to {{TO_VERSION}}

{{MIGRATION_STEPS}}
{{/MIGRATION_NOTES}}

## Uninstalling

### Package Manager

```bash
{{UNINSTALL_COMMAND}}
```

### Manual Cleanup

```bash
# Remove binary
rm {{BINARY_PATH}}

# Remove configuration (optional)
rm -rf {{CONFIG_DIR}}

# Remove data (optional - WARNING: destroys all data)
rm -rf {{DATA_DIR}}
```

## Troubleshooting Installation

### "Command not found" after installation

**Cause:** Binary not in PATH

**Solution:**
```bash
# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="{{INSTALL_PATH}}:$PATH"
```

### Permission denied errors

**Cause:** Insufficient permissions

**Solution:**
```bash
# Linux/macOS
sudo chown -R $(whoami) {{INSTALL_DIR}}

# Or install with user permissions
{{USER_INSTALL_COMMAND}}
```

### Dependency conflicts

**Cause:** Incompatible dependency versions

**Solution:**
```bash
# Check for conflicts
{{DEPS_CHECK_COMMAND}}

# Force reinstall dependencies
{{DEPS_REINSTALL_COMMAND}}
```

## Getting Help

If you encounter issues not covered here:

1. Check [Common Issues](./troubleshooting.md)
2. Search [existing issues]({{ISSUES_URL}})
3. Ask in [community chat]({{CHAT_URL}})
4. [Open a new issue]({{NEW_ISSUE_URL}})
