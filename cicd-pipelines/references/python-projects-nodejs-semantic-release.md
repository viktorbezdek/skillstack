**Skill**: [semantic-release](../SKILL.md)

# Python Projects with semantic-release (Node.js) - 2025 Production Pattern

## Overview

**Production-ready**: Validated with Python projects using uv, poetry, and setuptools

This guide shows how to use semantic-release v25+ (Node.js) for Python projects. This is the **production-grade approach** used by 126,000+ projects.

## ⚠️ Do NOT Use python-semantic-release

**Use semantic-release (Node.js) instead.** Here's why:

- **23.5x smaller community** (975 vs 22,900 GitHub stars)
- **100x+ less adoption** (~unknown vs 1.9M weekly downloads)
- **Small maintainer team** (136 vs 251 contributors)
- **Independent project** (NOT affiliated with semantic-release organization)
- **Version divergence** (v10 vs v25 - confusing and not in sync)
- **Python-only** (locked to single language, no future flexibility)
- **Sustainability risk** (smaller backing = long-term concerns)

**Bottom line**: semantic-release (Node.js) is proven at scale (126,000 projects), battle-tested, and future-proof. The Node.js dependency is trivial compared to the benefits.

## Complete Setup Guide

### 1. Project Structure

```
your-python-project/
├── .github/
│   └── workflows/
│       └── release.yml          # GitHub Actions workflow
├── .releaserc.yml               # semantic-release config
├── package.json                 # Node.js dependencies
├── pyproject.toml               # Python package metadata
├── .gitignore                   # Exclude node_modules
├── src/
│   └── your_package/
└── tests/
```

### 2. Create package.json

```json
{
  "name": "your-package-name",
  "version": "0.0.0-development",
  "description": "Your package description",
  "repository": {
    "type": "git",
    "url": "https://github.com/username/repo.git"
  },
  "engines": {
    "node": ">=22.14.0"
  },
  "scripts": {
    "release": "semantic-release"
  },
  "devDependencies": {
    "@semantic-release/changelog": "^6.0.3",
    "@semantic-release/commit-analyzer": "^13.0.0",
    "@semantic-release/exec": "^6.0.3",
    "@semantic-release/git": "^10.0.1",
    "@semantic-release/github": "^11.0.1",
    "@semantic-release/release-notes-generator": "^14.0.1",
    "semantic-release": "^25.0.2"
  },
  "private": true
}
```

**Key points**:

- `version`: Always `"0.0.0-development"` (managed by git tags)
- `private: true`: Prevents accidental npm publish
- `engines.node`: Minimum Node.js 22.14.0 (v24.10.0+ recommended for CI)

### 3. Create .releaserc.yml

```yaml
branches:
  - main

plugins:
  # Analyze commits to determine version bump
  - "@semantic-release/commit-analyzer"

  # Generate release notes from commits
  - "@semantic-release/release-notes-generator"

  # Update CHANGELOG.md
  - - "@semantic-release/changelog"
    - changelogFile: CHANGELOG.md

  # Update version in pyproject.toml and build package
  - - "@semantic-release/exec"
    - prepareCmd: 'sed -i.bak ''s/^version = ".*"/version = "${nextRelease.version}"/'' pyproject.toml && rm pyproject.toml.bak && uv build'
      publishCmd: "echo 'Python package built successfully'"

  # Commit version changes back to repository
  - - "@semantic-release/git"
    - assets:
        - pyproject.toml
        - CHANGELOG.md
      message: "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"

  # Create GitHub release
  - - "@semantic-release/github"
    - assets:
        - path: "dist/*.whl"
        - path: "dist/*.tar.gz"
```

**Platform-specific sed commands**:

- macOS/BSD: `sed -i.bak 's/pattern/replacement/' file && rm file.bak`
- GNU/Linux: `sed -i 's/pattern/replacement/' file`

**For cross-platform compatibility**, use the macOS version (works on both).

### 4. Update pyproject.toml

```toml
[project]
name = "your-package"
version = "0.2.0"  # Will be updated by semantic-release
description = "Your package description"
# ... rest of your package metadata
```

**Important**:

- Do NOT use dynamic versioning (no `setuptools-scm`, `hatchling.version`)
- Version will be updated directly by semantic-release via `sed`

### 5. Update .gitignore

```gitignore
# Node.js (for semantic-release)
node_modules/

# Python
__pycache__/
*.py[cod]
.venv/
dist/
build/
*.egg-info/

# OS
.DS_Store
```

**Important**: Do NOT ignore `package-lock.json`. The GitHub Actions workflow uses `npm ci`, which requires `package-lock.json` to be committed to the repository. Ignoring it will cause CI failures.

### 6. Create GitHub Actions Workflow

`.github/workflows/release.yml`:

```yaml
name: Semantic Release

on:
  push:
    branches:
      - main

jobs:
  release:
    runs-on: ubuntu-latest
    concurrency: release
    permissions:
      id-token: write
      contents: write
      issues: write
      pull-requests: write

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "24"

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true

      - name: Install Node.js dependencies
        run: npm ci

      - name: Verify repository configuration
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

      - name: Run semantic-release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: npm run release
```

**Key points**:

- `fetch-depth: 0`: Required for semantic-release to analyze commit history
- Node.js 24: Latest LTS version (22+ works)
- `npm ci`: Faster than `npm install`, uses package-lock.json
- `git config`: Required for semantic-release to commit changes

### 7. Create Initial Tag

```bash
git tag -a v0.1.0 -m "chore(release): 0.1.0 [skip ci]"
git push origin v0.1.0
```

This establishes the baseline version for semantic-release.

## Usage

### Local Testing

```bash
# Install dependencies
npm install

# Dry run (no changes, just preview)
GITHUB_TOKEN=dummy npx semantic-release --dry-run

# Real release (local, use gh CLI - ⚠️ AVOID manual tokens)
/usr/bin/env bash -c 'GITHUB_TOKEN=$(gh auth token) npx semantic-release'
```

### Automated Releases via GitHub Actions

```bash
# 1. Make changes with conventional commits
git commit -m "feat: add new feature"

# 2. Push to main
git push origin main

# 3. GitHub Actions automatically:
#    - Analyzes commits
#    - Determines version bump (MAJOR.MINOR.PATCH)
#    - Updates pyproject.toml
#    - Runs uv build
#    - Updates CHANGELOG.md
#    - Creates git tag
#    - Creates GitHub release with wheel + tarball
```

## Conventional Commits

### Version Bump Rules

| Commit Type                                              | Version Bump          | Example                          |
| -------------------------------------------------------- | --------------------- | -------------------------------- |
| `feat:`                                                  | MINOR (0.1.0 → 0.2.0) | `feat: add Ethereum collector`   |
| `fix:`                                                   | PATCH (0.1.0 → 0.1.1) | `fix: correct timestamp parsing` |
| `BREAKING CHANGE:`                                       | MAJOR (0.1.0 → 1.0.0) | See below                        |
| `docs:`, `chore:`, `ci:`, `style:`, `refactor:`, `test:` | No bump               | Ignored                          |

### Breaking Changes

```bash
# Method 1: ! suffix
git commit -m "feat!: change API signature

BREAKING CHANGE: API now requires authentication parameter"

# Method 2: Footer only
git commit -m "refactor: restructure module

BREAKING CHANGE: Module imports have changed from old_name to new_name"
```

## Troubleshooting

### "No release will be made"

**Cause**: No conventional commits since last tag

**Solution**: Add a `feat:` or `fix:` commit

### "The local branch is behind the remote"

**Cause**: Local commits not pushed or remote has changes

**Solution**:

```bash
git fetch
git status
git push  # If ahead
```

### "ENOGHTOKEN No GitHub token specified"

**Error message from semantic-release** - Not a recommendation to create tokens!

**Cause**: Running locally without GITHUB_TOKEN from gh CLI

**Solution** (⚠️ AVOID manual tokens):

```bash
# For testing (dry-run doesn't need real credentials)
GITHUB_TOKEN=dummy npx semantic-release --dry-run

# For real release - use gh CLI web auth (⚠️ NEVER create manual tokens)
# First authenticate: gh auth login
/usr/bin/env bash -c 'GITHUB_TOKEN=$(gh auth token) npx semantic-release'
```

### sed command fails on Linux

**Cause**: GNU sed syntax differs from BSD sed (macOS)

**Solution**: Use macOS-compatible syntax (works on both):

```bash
sed -i.bak 's/pattern/replacement/' file && rm file.bak
```

## PyPI Publishing (Optional)

Add after the `@semantic-release/github` plugin in `.releaserc.yml`:

```yaml
# Publish to PyPI
- - "@semantic-release/exec"
  - publishCmd: |
      python -m pip install --upgrade twine
      python -m twine upload dist/*
```

Set `TWINE_USERNAME` and `TWINE_PASSWORD` in GitHub Secrets.

**Better: Use OIDC trusted publishing** (recommended 2025):

1. Configure at https://pypi.org/manage/account/publishing/
2. Update workflow to use `pypa/gh-action-pypi-publish@release/v1`

## References

- [semantic-release documentation](https://semantic-release.gitbook.io/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Actions setup-node](https://github.com/actions/setup-node)
- [Python Packaging Guide](https://packaging.python.org/)

## Compatibility

- **semantic-release**: v25.0.0 or higher
- **Node.js**: v22.14.0 or higher (v24.10.0+ recommended)
- **Python**: 3.9 or higher
- **Package managers**: uv, poetry, pip, setuptools
- **Build backends**: hatchling, setuptools, flit, pdm
