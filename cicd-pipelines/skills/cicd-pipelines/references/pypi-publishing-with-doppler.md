**Skill**: [semantic-release](../SKILL.md)

> **Note**: For the canonical publish script with CI detection guards, see the [`pypi-doppler` skill](../../pypi-doppler/SKILL.md). This reference provides semantic-release integration context.

# PyPI Publishing with Doppler Secret Management

Comprehensive guide for integrating semantic-release with PyPI publishing using Doppler CLI for secure credential management. Validated workflow for Python packages using local-first publishing strategy.

## Overview

This workflow solves two key problems:

1. **Version Synchronization**: semantic-release is Node.js-centric and doesn't natively update Python version files (pyproject.toml)
2. **Secret Management**: PyPI tokens should never be stored in plaintext configuration files

**Solution**: @semantic-release/exec plugin + Doppler CLI + local publishing workflow

**Benefits**:

- 10x faster publishing (30 seconds vs 5 minutes with GitHub Actions)
- Encrypted secret storage with audit trails
- Easy token rotation without code changes
- Team access control via Doppler projects

## Problem Statement

### Traditional Workflow Issues

**GitHub-Only semantic-release**:

- Creates tags and releases on GitHub
- Updates package.json (Node.js standard)
- Does NOT update pyproject.toml (Python standard)
- Result: pyproject.toml stuck at v1.0.0 despite GitHub having v2.1.2

**GitHub Actions Publishing**:

- Build environment setup: 1-2 min
- Dependency installation: 1-2 min
- Actual publishing: 30 sec
- Total: 3-5 minutes per release
- Slow feedback loop for publish failures

**Plaintext Token Storage (~/.pypirc)**:

- No encryption at rest
- No centralized rotation capability
- Version control risk (accidental commits)
- No team access control

## Architecture

### Separation of Concerns

**GitHub Actions** (Automated, Fast):

- Analyze conventional commits
- Determine next version (major/minor/patch)
- Update pyproject.toml, package.json via @semantic-release/exec
- Update CHANGELOG.md
- Create git tag
- Create GitHub release
- Time: 1-2 minutes

**Local Workflow** (Manual, Controlled):

- Pull latest version from GitHub
- Build package with uv
- Publish to PyPI with Doppler-managed credentials
- Verify publication
- Time: 30 seconds

### Plugin Flow

```
1. @semantic-release/commit-analyzer
   └→ Determines next version (e.g., 2.1.3)

2. @semantic-release/release-notes-generator
   └→ Generates CHANGELOG.md content

3. @semantic-release/changelog
   └→ Writes CHANGELOG.md

4. @semantic-release/exec (NEW - Python integration)
   └→ Updates pyproject.toml + package.json versions

5. @semantic-release/npm
   └→ Updates package.json (npmPublish: false)

6. @semantic-release/github
   └→ Creates GitHub release

7. @semantic-release/git
   └→ Commits updated files
   └→ Creates git tag
```

## Setup

### Prerequisites

```bash
# Install dependencies
brew install dopplerhq/cli/doppler  # Doppler CLI
npm install -g semantic-release     # semantic-release CLI
pip install uv                       # Modern Python package manager

# Verify installations
doppler --version   # Should show v3.0+
semantic-release --version  # Should show v25+
uv --version        # Should show v0.5+
```

### Step 1: Configure semantic-release with @semantic-release/exec

**File**: `.releaserc.json`

```json
{
  "branches": ["main"],
  "plugins": [
    [
      "@semantic-release/commit-analyzer",
      {
        "preset": "conventionalcommits",
        "releaseRules": [
          { "type": "feat", "release": "minor" },
          { "type": "fix", "release": "patch" },
          { "type": "perf", "release": "patch" },
          { "type": "docs", "release": "patch" },
          { "breaking": true, "release": "major" }
        ]
      }
    ],
    [
      "@semantic-release/release-notes-generator",
      { "preset": "conventionalcommits" }
    ],
    [
      "@semantic-release/changelog",
      {
        "changelogFile": "CHANGELOG.md",
        "changelogTitle": "# Changelog\n\nAll notable changes to this project will be documented in this file. See [Conventional Commits](https://conventionalcommits.org) for commit guidelines."
      }
    ],
    [
      "@semantic-release/exec",
      {
        "prepareCmd": "sed -i.bak 's/^version = \".*\"/version = \"${nextRelease.version}\"/' pyproject.toml && sed -i.bak 's/\"version\": \".*\"/\"version\": \"${nextRelease.version}\"/' package.json && rm -f pyproject.toml.bak package.json.bak"
      }
    ],
    ["@semantic-release/npm", { "npmPublish": false }],
    [
      "@semantic-release/github",
      {
        "successComment": false,
        "failComment": false
      }
    ],
    [
      "@semantic-release/git",
      {
        "assets": ["CHANGELOG.md", "pyproject.toml", "package.json"],
        "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
      }
    ]
  ]
}
```

**Key Points**:

- `@semantic-release/exec` MUST come before `@semantic-release/git`
- `prepareCmd` updates both pyproject.toml and package.json
- `.bak` files created for macOS/BSD sed compatibility, then deleted
- `${nextRelease.version}` is semantic-release template variable

**Install exec plugin**:

```bash
npm install --save-dev @semantic-release/exec
```

**Update GitHub Actions** (`.github/workflows/release.yml`):

```yaml
- name: Install semantic-release
  run: |
    npm install --global \
      semantic-release \
      @semantic-release/changelog \
      @semantic-release/commit-analyzer \
      @semantic-release/release-notes-generator \
      @semantic-release/github \
      @semantic-release/git \
      @semantic-release/npm \
      @semantic-release/exec \
      conventional-changelog-conventionalcommits
```

### Step 2: Set Up Doppler

**Initialize project**:

```bash
cd /path/to/your/python/project
doppler login  # First-time setup only

# Create project and config
doppler setup
# Interactive prompts:
# ? Select a project: [Create new project]
# ? Enter project name: your-package-name
# ? Select a config: dev
```

This creates `.doppler.yaml`:

```yaml
# Doppler configuration for your-package-name
# https://docs.doppler.com/docs/enclave-project-setup

setup:
  project: your-package-name
  config: dev
```

**Store PyPI token**:

```bash
# Get token from https://pypi.org/manage/account/token/
# Scope: Project "your-package-name" (NOT "Entire account")

doppler secrets set PYPI_TOKEN='pypi-AgEIcHlwaS5vcm...'
```

**Verify**:

```bash
doppler secrets get PYPI_TOKEN --plain | head -c 50
# Should output: pypi-AgEIcHlwaS5vcm... [then truncated]
```

### Step 3: Create Local Publishing Script

**File**: `scripts/publish-to-pypi.sh`

```bash
#!/bin/bash
# Quick PyPI Publishing Script
# Requires: Doppler CLI with PYPI_TOKEN secret

set -e

echo "🚀 Publishing to PyPI (Local Workflow)"
echo "======================================"

# Step 0: Verify Doppler token
echo -e "\n🔐 Step 0: Verifying Doppler credentials..."
if ! doppler secrets get PYPI_TOKEN --plain > /dev/null 2>&1; then
    echo "   ❌ ERROR: PYPI_TOKEN not found in Doppler"
    echo "   Run: doppler secrets set PYPI_TOKEN='your-token'"
    exit 1
fi
echo "   ✅ Doppler token verified"

# Step 1: Pull latest release
echo -e "\n📥 Step 1: Pulling latest release commit..."
git pull origin main
CURRENT_VERSION=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
echo "   Current version: v${CURRENT_VERSION}"

# Step 2: Clean old builds
echo -e "\n🧹 Step 2: Cleaning old builds..."
rm -rf dist/ build/ *.egg-info
echo "   ✅ Cleaned"

# Step 3: Build package
echo -e "\n📦 Step 3: Building package..."
uv build 2>&1 | grep -E "(Building|Successfully built)" || uv build
echo "   ✅ Built: dist/*-${CURRENT_VERSION}*"

# Step 4: Publish to PyPI
echo -e "\n📤 Step 4: Publishing to PyPI..."
echo "   Using PYPI_TOKEN from Doppler"
PYPI_TOKEN=$(doppler secrets get PYPI_TOKEN --plain)
uv publish --token "${PYPI_TOKEN}" 2>&1 | grep -E "(Uploading|succeeded|Failed)" || \
  uv publish --token "${PYPI_TOKEN}"
echo "   ✅ Published to PyPI"

# Step 5: Verify
echo -e "\n🔍 Step 5: Verifying on PyPI..."
sleep 3
PACKAGE_NAME=$(grep '^name = ' pyproject.toml | sed 's/name = "\(.*\)"/\1/')
curl -s https://pypi.org/pypi/${PACKAGE_NAME}/${CURRENT_VERSION}/json > /dev/null 2>&1 && \
  echo "   ✅ Verified: https://pypi.org/project/${PACKAGE_NAME}/${CURRENT_VERSION}/" || \
  echo "   ⏳ Still propagating (check in 30 seconds)"

echo -e "\n✅ Complete! Published v${CURRENT_VERSION} to PyPI"
```

Make executable:

```bash
chmod +x scripts/publish-to-pypi.sh
```

### Step 4: Disable GitHub Actions Publishing (Optional)

If you have a `publish.yml` workflow for automatic PyPI publishing, disable it:

```bash
mv .github/workflows/publish.yml .github/workflows/publish.yml.disabled
```

**Rationale**: Local workflow is 10x faster and gives you manual control over when packages are published.

## Usage

### Complete Release Workflow

```bash
# 1. Develop and commit with conventional commits
git add .
git commit -m "feat: add new feature"
git push origin main

# 2. Wait for GitHub Actions (1-2 minutes)
# - Analyzes commits
# - Determines version (e.g., 2.1.3)
# - Updates pyproject.toml, package.json, CHANGELOG.md
# - Creates tag v2.1.3
# - Creates GitHub release

# 3. Publish to PyPI (30 seconds)
./scripts/publish-to-pypi.sh
```

### Expected Output

```
🚀 Publishing to PyPI (Local Workflow)
======================================

🔐 Step 0: Verifying Doppler credentials...
   ✅ Doppler token verified

📥 Step 1: Pulling latest release commit...
   Current version: v2.1.3

🧹 Step 2: Cleaning old builds...
   ✅ Cleaned

📦 Step 3: Building package...
   ✅ Built: dist/*-2.1.3*

📤 Step 4: Publishing to PyPI...
   Using PYPI_TOKEN from Doppler
   ✅ Published to PyPI

🔍 Step 5: Verifying on PyPI...
   ✅ Verified: https://pypi.org/project/your-package/2.1.3/

✅ Complete! Published v2.1.3 to PyPI
```

## Troubleshooting

### Issue: "Invalid or non-existent authentication information"

**Symptom**: 403 Forbidden when publishing to PyPI

**Causes**:

1. Token format error (missing `pypi-` prefix)
2. Token has extra quotes or newlines
3. Token expired or revoked

**Solution**:

```bash
# Verify token format
doppler secrets get PYPI_TOKEN --plain | od -c
# Should start with: p y p i - A g E I

# If wrong, reset with single quotes
doppler secrets set PYPI_TOKEN='pypi-AgEIcHlwaS5vcm...'

# Verify no newlines (should be one line)
doppler secrets get PYPI_TOKEN --plain | wc -l
# Should output: 1
```

### Issue: "PYPI_TOKEN not found in Doppler"

**Symptom**: Script fails at Step 0

**Causes**:

1. Wrong Doppler project/config selected
2. Token never set
3. Insufficient Doppler permissions

**Solution**:

```bash
# Check current project
doppler configure get project config
# Should show your project name and "dev"

# If wrong, reinitialize
doppler setup

# Verify token exists
doppler secrets
# Should list PYPI_TOKEN in output

# If missing, set it
doppler secrets set PYPI_TOKEN='pypi-...'
```

### Issue: pyproject.toml version not updated

**Symptom**: GitHub release shows v2.1.3 but pyproject.toml still shows v1.0.0

**Causes**:

1. @semantic-release/exec not installed
2. Plugin order wrong (exec after git)
3. sed command syntax error

**Solution**:

```bash
# Verify plugin is installed
grep '@semantic-release/exec' package.json
# Should show in devDependencies

# Check .releaserc.json plugin order
# @semantic-release/exec MUST come before @semantic-release/git

# Test sed command manually
sed -i.bak 's/^version = ".*"/version = "TEST"/' pyproject.toml
grep 'version = ' pyproject.toml
# Should show: version = "TEST"
git checkout pyproject.toml  # Revert test
```

### Issue: CDN propagation delay

**Symptom**: Verification step shows "Still propagating" but package was uploaded

**Cause**: PyPI CDN caching (normal behavior)

**Solution**: Wait 30-60 seconds and verify manually:

```bash
curl -s https://pypi.org/pypi/YOUR_PACKAGE/VERSION/json | jq -r '.info.version'
```

## Token Rotation

**Recommended Frequency**: Every 90 days or when team member leaves

**Steps**:

```bash
# 1. Generate new token at https://pypi.org/manage/account/token/
#    Scope: Project "your-package-name"
#    Permissions: Upload packages

# 2. Update Doppler
doppler secrets set PYPI_TOKEN='NEW-TOKEN-HERE'

# 3. Verify
doppler secrets get PYPI_TOKEN --plain | head -c 50

# 4. Test publish
./scripts/publish-to-pypi.sh

# 5. Revoke old token on PyPI
```

**No code changes needed** - next publish automatically uses new token from Doppler.

## Security Best Practices

1. **Use project-scoped tokens** (not account-wide)
   - Limits blast radius if compromised
   - Easier to track usage per project

2. **Never commit tokens to git**
   - Add `.env` to `.gitignore`
   - Use Doppler for all secrets
   - Review `.gitignore` includes common secret files

3. **Enable 2FA on PyPI account**
   - Prevents unauthorized token generation
   - Required for high-value packages

4. **Use Doppler service tokens in CI/CD**
   - For GitHub Actions that need Doppler access
   - Scope to specific project/config

5. **Rotate tokens regularly**
   - Every 90 days minimum
   - Immediately when team member leaves
   - After suspected compromise

## GitHub Actions Integration (Advanced)

If you want GitHub Actions to publish automatically using Doppler:

**Add Doppler service token to GitHub secrets**:

```bash
# Generate service token
doppler configs tokens create github-actions --max-age 90d --plain
# Copy the output token

# Add to GitHub repo secrets as DOPPLER_TOKEN
```

**Update publish.yml**:

```yaml
- name: Publish to PyPI
  env:
    DOPPLER_TOKEN: ${{ secrets.DOPPLER_TOKEN }}
  run: |
    PYPI_TOKEN=$(doppler secrets get PYPI_TOKEN --plain --token $DOPPLER_TOKEN)
    uv publish --token "$PYPI_TOKEN"
```

**Security Note**: GitHub secrets are encrypted, but Doppler service token has expiration and can be revoked instantly if compromised.

## Comparison: OIDC vs API Tokens

| Feature               | OIDC Trusted Publishing         | API Tokens (this guide)       |
| --------------------- | ------------------------------- | ----------------------------- |
| Setup complexity      | Medium (GitHub + PyPI config)   | Low (just generate token)     |
| Security              | Highest (no long-lived secrets) | High (encrypted in Doppler)   |
| Rotation              | Automatic (short-lived)         | Manual (90 days)              |
| Local publishing      | ❌ Not supported                | ✅ Fully supported            |
| CI/CD publishing      | ✅ Ideal for automation         | ✅ Requires secret management |
| Token compromise risk | None (ephemeral tokens)         | Low (encrypted, revocable)    |

**Recommendation**:

- **Local publishing**: Use API tokens + Doppler (this guide)
- **CI/CD-only publishing**: Use OIDC trusted publishing

## Production Evidence

This workflow was validated with gapless-crypto-clickhouse v2.1.3:

- **Commits**: 8976e90 → 4ea992c (2025-11-19)
- **Result**: Successfully published to PyPI with zero failures
- **Metrics**:
  - GitHub Actions versioning: 1-2 minutes
  - Local publishing: 30 seconds
  - Total time: ~2 minutes (vs 5+ minutes with GitHub Actions publishing)

**Key Files**:

- `.releaserc.json` - semantic-release config with @semantic-release/exec
- `scripts/publish-to-pypi.sh` - Local publishing script with Doppler
- `.doppler.yaml` - Project configuration
- `.github/workflows/release.yml` - Versioning workflow (GitHub Actions)
- `.github/workflows/publish.yml.disabled` - Disabled auto-publish workflow

## References

- [semantic-release Documentation](https://semantic-release.gitbook.io/semantic-release/)
- [@semantic-release/exec Plugin](https://github.com/semantic-release/exec)
- [Doppler CLI Documentation](https://docs.doppler.com/docs/cli)
- [PyPI Trusted Publishing (OIDC)](https://docs.pypi.org/trusted-publishers/)
- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [uv Package Manager](https://github.com/astral-sh/uv)

---

**Last Updated**: 2025-11-19
**Validated**: gapless-crypto-clickhouse v2.1.3
**Workflow Status**: Production-Ready
