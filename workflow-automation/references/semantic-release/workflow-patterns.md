**Skill**: [semantic-release](../SKILL.md)

## Workflow Patterns

**Default: Local releases** - Fast, immediate file updates, no CI/CD wait time.

**GitHub Actions**: Optional backup only (2-5 minute delay not recommended for primary workflow).

### Pattern A: Personal Projects (Level 2 + Level 4)

Use for solo projects where you want consistent personal defaults.

**1. Create User Config** (One-time setup)

```bash
# Environment-agnostic path
PLUGIN_DIR="${CLAUDE_PLUGIN_ROOT:-$HOME/.claude/plugins/marketplaces/cc-skills/plugins/itp}"
cd "$PLUGIN_DIR/skills/semantic-release"
./scripts/init_user_config.sh
```

Creates `~/semantic-release-config/` with:

- Git repository (version control your defaults)
- npm package structure (`@username/semantic-release-config`)
- 2025-compliant plugin versions

**2. Customize Defaults** (Optional)

```bash
cd ~/semantic-release-config
vim index.js  # Edit your personal defaults
git add . && git commit -m "feat: customize defaults"
```

**3. Publish** (Optional, for sharing)

```bash
cd ~/semantic-release-config
npm publish --access public
```

**4. Use in Projects**

```bash
cd /path/to/project
PLUGIN_DIR="${CLAUDE_PLUGIN_ROOT:-$HOME/.claude/plugins/marketplaces/cc-skills/plugins/itp}"
"$PLUGIN_DIR/skills/semantic-release/scripts/init_project.sh" --user
```

This creates project `.releaserc.yml`:

```yaml
extends: "@username/semantic-release-config"
```

**5. Run Releases Locally** (Primary workflow)

```bash
# Test release (no changes)
npm run release:dry

# Create release locally (instant, files update immediately)
npm run release

# Push release commit and tags
git push --follow-tags origin main
```

**Advantages over GitHub Actions:**

- ⚡ Instant (vs 2-5 minute CI/CD wait)
- ✅ Immediate local file sync
- ✅ No `git pull` required to continue working

### Pattern B: Team Projects (Level 3 + Level 4)

Use for company/team projects requiring shared standards.

**1. Create Organization Config** (Team lead, one-time)

```bash
# Environment-agnostic path
PLUGIN_DIR="${CLAUDE_PLUGIN_ROOT:-$HOME/.claude/plugins/marketplaces/cc-skills/plugins/itp}"
cd "$PLUGIN_DIR/skills/semantic-release"
./scripts/create_org_config.sh mycompany semantic-release-config ~/org-configs/
```

Creates `~/org-configs/semantic-release-config/` with npm package structure.

**2. Customize for Organization**

```bash
cd ~/org-configs/semantic-release-config
vim index.js  # Set company standards
git remote add origin https://github.com/mycompany/semantic-release-config.git
git push -u origin main
```

**3. Publish to npm**

```bash
npm publish --access public
```

**4. Use in Team Projects** (All team members)

```bash
cd /path/to/team-project
PLUGIN_DIR="${CLAUDE_PLUGIN_ROOT:-$HOME/.claude/plugins/marketplaces/cc-skills/plugins/itp}"
"$PLUGIN_DIR/skills/semantic-release/scripts/init_project.sh" --org mycompany/semantic-release-config
```

This creates project `.releaserc.yml`:

```yaml
extends: "@mycompany/semantic-release-config"
```

**5. Run Releases Locally** (Recommended)

```bash
# Test release
npm run release:dry

# Create release locally (faster than GitHub Actions)
npm run release
git push --follow-tags origin main
```

**Note**: GitHub Actions option available but not recommended due to 2-5 minute delay vs instant local releases.

### Pattern C: Standalone Projects (Level 4 Only)

Use for one-off projects with unique requirements.

**Initialize with Inline Config**

```bash
cd /path/to/project
PLUGIN_DIR="${CLAUDE_PLUGIN_ROOT:-$HOME/.claude/plugins/marketplaces/cc-skills/plugins/itp}"
"$PLUGIN_DIR/skills/semantic-release/scripts/init_project.sh" --inline
```

This creates self-contained `.releaserc.yml` with all configuration inline (no extends).

**Run Releases Locally**

```bash
# Test release
npm run release:dry

# Create release (instant local execution)
npm run release
git push --follow-tags origin main
```

**Local releases recommended** - Avoid GitHub Actions 2-5 minute wait, get instant file updates.

### All-in-One Release Function

Single command that handles prerequisites, sync, release, and push with SSH/HTTPS fallback:

```bash
release() {
    # Prerequisites
    command -v gh &>/dev/null || { echo "❌ gh CLI not installed"; return 1; }
    command -v npx &>/dev/null || { echo "❌ npx not found"; return 1; }
    gh auth status &>/dev/null || { echo "❌ gh not authenticated"; return 1; }
    git rev-parse --git-dir &>/dev/null || { echo "❌ Not a git repo"; return 1; }
    export GIT_OPTIONAL_LOCKS=0

    local branch=$(git branch --show-current)
    [[ "$branch" == "main" ]] || { echo "❌ Not on main (on: $branch)"; return 1; }

    # Require clean working directory before release
    if [[ -n $(git status --porcelain) ]]; then
        echo "❌ Working directory not clean. Commit or discard changes first:"
        git status --short
        return 1
    fi

    # Get remote URL and derive HTTPS fallback
    local remote_url=$(git remote get-url origin)
    local https_url=$(echo "$remote_url" | sed -E 's|git@github\.com:|https://github.com/|; s|\.git$||').git

    # Sync with remote (SSH first, fallback to HTTPS)
    git pull --rebase origin main --quiet || { echo "❌ Pull failed"; return 1; }

    if ! git push origin main --quiet 2>/dev/null; then
        echo "⚠️  SSH push failed, trying HTTPS..."
        git push "$https_url" main --quiet || { echo "❌ Push failed (SSH and HTTPS)"; return 1; }
    fi

    # Release
    GITHUB_TOKEN=$(gh auth token) npx semantic-release --no-ci "$@"
    local rc=$?

    # Post-release: verify pristine state
    if [[ -n $(git status --porcelain) ]]; then
        echo "⚠️  Post-release: unexpected uncommitted changes"
        git status --short
    else
        echo "✅ Pristine"
    fi

    return $rc
}
```

**Features**:

- Validates prerequisites (gh CLI, npx, authentication, git repo)
- Enforces main branch requirement
- **Pre-flight**: Blocks release if working directory not clean
- Syncs with remote before release (`git pull --rebase`)
- SSH → HTTPS automatic fallback for push
- Passes additional args to semantic-release (`release --dry-run`)
- **Post-flight**: Verifies pristine state after release

**SSH/HTTPS Fallback**:

- Derives HTTPS URL from SSH remote (`git@github.com:user/repo.git` → `https://github.com/user/repo.git`)
- If SSH push fails, automatically retries with HTTPS
- Clear error messages indicating which method failed

**Pristine State Guarantee**:

- Pre-release: Refuses to run with modified/staged/untracked files
- Post-release: Confirms `✅ Pristine` or warns of unexpected changes
- Exit code preserved from semantic-release for scripting
