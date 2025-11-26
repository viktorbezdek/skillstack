**Skill**: [semantic-release](../SKILL.md)

# Local Release Workflow

Instructional workflow for executing local semantic-release. Follow these steps autonomously, resolving issues as encountered.

---

## Prerequisites Checklist

Before starting, verify each prerequisite. If any fails, resolve before proceeding.

| Check                       | Command                       | Expected                    | Resolution              |
| --------------------------- | ----------------------------- | --------------------------- | ----------------------- |
| gh CLI installed            | `command -v gh`               | Path to gh                  | `brew install gh`       |
| npx available               | `command -v npx`              | Path to npx                 | Install Node.js         |
| gh authenticated            | `gh auth status`              | "Logged in to github.com"   | `gh auth login`         |
| **gh account matches repo** | See Account Alignment section | Active account = repo owner | `gh auth switch`        |
| In git repo                 | `git rev-parse --git-dir`     | `.git`                      | Navigate to repo root   |
| On main branch              | `git branch --show-current`   | `main`                      | `git checkout main`     |
| Clean working directory     | `git status --porcelain`      | Empty output                | Commit or stash changes |

### Account Alignment Check (MANDATORY FIRST STEP)

**CRITICAL**: For multi-account GitHub setups, verify the active gh account matches the SSH-authenticated account BEFORE any release operation. This check is non-negotiable and must be performed first.

**Detection sequence** (execute autonomously):

1. **Determine expected account from SSH** (authoritative source):

   ```bash
   ssh -T git@github.com 2>&1
   # Output: "Hi <username>! You've successfully authenticated..."
   # Extract <username> - this is the expected account
   ```

   **Why SSH is authoritative**: If `~/.ssh/config` uses directory-based `Match` directives, the SSH key (and thus account) is automatically selected based on `$PWD`. Git push/pull will use this account.

2. **Identify active gh account**:

   ```bash
   gh auth status 2>&1 | grep -B1 "Active account: true" | head -1
   # Extract the account username from output
   ```

3. **Compare and auto-resolve**:
   - If SSH username ≠ active gh account → **MISMATCH DETECTED**
   - Auto-switch: `gh auth switch --user <ssh-username>`
   - If account not logged in → prompt: `gh auth login` for that account
   - Verify switch: `gh auth status` shows correct account active

4. **Fallback: Extract from repo owner** (if SSH detection unclear):
   - Parse `git remote get-url origin`
   - SSH format: `git@github.com:OWNER/repo.git` → extract OWNER
   - HTTPS format: `https://github.com/OWNER/repo.git` → extract OWNER

**Why alignment matters**: Git operations authenticate via SSH. GitHub API (semantic-release) authenticates via gh token. Different accounts = "Repository not found" errors even for valid repositories.

**Failure mode without this check**: Release fails with cryptic permission errors that don't indicate account mismatch as root cause.

---

## Workflow Steps

### Step 1: Verify Prerequisites

Run each check from the Prerequisites Checklist. Resolve any failures before proceeding.

### Step 2: Verify Releasable Commits Exist

**MANDATORY**: Before proceeding, verify commits since last tag include version-bumping types (`feat:`, `fix:`, or `BREAKING CHANGE:`).

**Autonomous check sequence**:

1. Identify latest version tag
2. List commits since that tag
3. Scan commit messages for releasable prefixes
4. If NO releasable commits → **STOP** and inform user

**If no releasable commits found**:

- Inform user: "No version-bumping commits since last release"
- Advise: Use `feat:` or `fix:` prefix for changes that warrant a release
- Do NOT proceed with semantic-release (it will produce no output)

**Why this matters**: Running semantic-release without releasable commits wastes time and creates confusion. Validate first, release second.

### Step 3: Sync with Remote

**Pull with rebase**:

```bash
git pull --rebase origin main
```

**If pull fails**:

- Check network connectivity
- Verify remote exists: `git remote -v`
- If conflicts: resolve, `git add .`, `git rebase --continue`

**Push local commits**:

```bash
git push origin main
```

**If SSH push fails**, try HTTPS fallback:

```bash
# Derive HTTPS URL from SSH
git remote get-url origin
# git@github.com:user/repo.git → https://github.com/user/repo.git
git push https://github.com/user/repo.git main
```

### Step 4: Execute Release

Set environment and run:

```bash
/usr/bin/env bash -c 'export GIT_OPTIONAL_LOCKS=0 && GITHUB_TOKEN=$(gh auth token) npx semantic-release --no-ci'
```

**For dry-run** (no changes):

```bash
/usr/bin/env bash -c 'GITHUB_TOKEN=$(gh auth token) npx semantic-release --no-ci --dry-run'
```

### Step 5: Verify Post-Release State

**Check for uncommitted changes**:

```bash
git status --porcelain
```

- **Empty output** → Release successful, state is pristine
- **Has output** → Unexpected changes; investigate what semantic-release modified

**Verify release created**:

```bash
gh release list --limit 1
```

### Step 6: Update Local Tracking Refs

**IMPORTANT**: After semantic-release pushes via GitHub API, local git tracking refs may be stale. This causes shell prompts and status lines to show incorrect ahead/behind counts (e.g., `↑:3` when actually in sync).

**Update tracking refs without full fetch**:

```bash
git fetch origin main:refs/remotes/origin/main --no-tags
```

This command:

- Updates only `origin/main` ref (fast, no network overhead for other branches)
- Skips tag fetch (tags already created by semantic-release)
- Ensures local tracking matches remote state

**Verify sync**:

```bash
git status -sb
# Should show: ## main...origin/main (no ahead/behind counts)
```

**Why this matters**: Tools like Claude Code status line, shell prompts (p10k, starship), and IDE git integrations rely on local tracking refs. Stale refs cause confusing indicators that persist until the next `git fetch`.

**Alternative - Add to npm scripts** (automate for future releases):

```json
{
  "scripts": {
    "release": "semantic-release --no-ci",
    "postrelease": "git fetch origin main:refs/remotes/origin/main --no-tags"
  }
}
```

---

## Issue Resolution

### "No GitHub token specified"

**Cause**: `GH_TOKEN` not set or gh CLI not authenticated

**Resolution**:

1. Verify: `gh auth status`
2. If not authenticated: `gh auth login`
3. Verify token retrieval: `gh auth token` (should output token)

### "Repository not found" (with valid repo URL)

**Cause**: gh CLI authenticated with wrong GitHub account for this repository. Common in multi-account setups where developer has personal, work, or organization accounts.

**Symptoms**:

- Repository URL is correct and repo exists
- SSH test shows different username than repo owner
- gh auth shows multiple accounts with wrong one active

**Resolution**:

1. Extract repo owner from remote URL
2. List available gh accounts to find matching account
3. Switch gh CLI to the account matching repository owner
4. Re-fetch token after account switch
5. If account not logged in, authenticate with `gh auth login` for that account

**Prevention**: Always verify account alignment as first pre-flight check before any release operation.

### "Permission denied (publickey)"

**Cause**: SSH key issue for git push

**Resolution**:

1. Test SSH: `ssh -T git@github.com`
2. Check SSH config: `cat ~/.ssh/config | grep -A5 github`
3. Add key to agent: `ssh-add ~/.ssh/id_ed25519`
4. Check for ControlMaster cache (see next section)
5. Fallback: Use HTTPS push with gh token authentication (see Step 2)

### ControlMaster Cache Issues

**Cause**: SSH ControlMaster maintains persistent connections that cache authentication. In multi-account setups, the cached connection may use a different account than expected based on current directory.

**Symptoms**:

- Account alignment check passes (SSH and gh show same username)
- `ssh -T git@github.com` shows correct account
- `git push` or semantic-release still fails with "Repository not found"
- Error persists even after `gh auth switch`

**Root Cause Explained**: SSH ControlMaster caches connections by **hostname**, not by identity file or directory. When you connect to `github.com` from directory A (using account-A's key), then switch to directory B (which should use account-B's key), SSH reuses the cached account-A connection instead of creating a new connection with account-B's key.

**Detection Sequence**:

```bash
# 1. Check if ControlMaster is enabled
grep -i "ControlMaster" ~/.ssh/config

# 2. List active control sockets for GitHub
ls -la ~/.ssh/control*github* 2>/dev/null
ls -la ~/.ssh/controlmasters/*github* 2>/dev/null

# 3. Test with fresh connection (bypass cache)
ssh -o ControlMaster=no -T git@github.com
# Compare output to:
ssh -T git@github.com
# If different → stale cache is the issue
```

**Resolution**:

```bash
# Option 1: Kill cached connection via SSH
ssh -O exit git@github.com

# Option 2: Remove control socket file directly
rm -f ~/.ssh/control-git@github.com:22

# Option 3: Kill all SSH processes for github.com
pkill -f 'ssh.*github.com'

# Verify fix
ssh -T git@github.com
# Should show expected account

# Retry release
/usr/bin/env bash -c 'GITHUB_TOKEN=$(gh auth token) npx semantic-release --no-ci'
```

**Prevention (Recommended for Multi-Account Setups)**:

Add to `~/.ssh/config`:

```sshconfig
# Disable ControlMaster for GitHub to prevent account caching
Host github.com
    ControlMaster no
```

**Trade-offs**:

- ✅ Eliminates stale authentication cache
- ✅ Each git operation uses fresh account-aware SSH connection
- ⚠️ Slightly slower SSH operations (no connection reuse)
- For multi-account setups, **correctness > speed**

### "Not on main branch"

**Cause**: Attempting release from non-main branch

**Resolution**:

1. Check current branch: `git branch --show-current`
2. Switch to main: `git checkout main`
3. Ensure main is up-to-date: `git pull --rebase origin main`

### "Working directory not clean"

**Cause**: Uncommitted changes prevent release

**Resolution options**:

1. **Commit changes**: `git add . && git commit -m "..."`
2. **Stash temporarily**: `git stash` (then `git stash pop` after release)
3. **Discard changes**: `git checkout -- .` (⚠️ destructive)

### "No release published"

**Cause**: No releasable commits since last tag

**Check commit types**:

```bash
git log $(git describe --tags --abbrev=0)..HEAD --oneline
```

Only these trigger releases:

- `feat:` → minor bump
- `fix:` → patch bump
- `BREAKING CHANGE:` or `feat!:` → major bump

`docs:`, `chore:`, `style:`, `refactor:`, `test:` → no release

### Stale Ahead/Behind Indicators After Release

**Symptom**: After successful release, shell prompt or status line shows `↑:N` (commits ahead) when actually in sync with remote.

**Cause**: semantic-release pushes via GitHub API, but local git tracking refs (`origin/main`) aren't updated. Tools that display ahead/behind counts rely on these local refs.

**Affected tools**:

- Claude Code status line
- Shell prompts (p10k, starship, oh-my-zsh)
- IDE git integrations (VS Code, IntelliJ)

**Resolution**:

```bash
# Update local tracking ref without full fetch
git fetch origin main:refs/remotes/origin/main --no-tags

# Verify
git status -sb
# Should show: ## main...origin/main (no ahead/behind)
```

**Prevention**: Always run Step 6 (Update Local Tracking Refs) after release.

---

## Decision Tree

```
Start Release
    │
    ├── Prerequisites pass?
    │   ├── No → Resolve each failure, retry
    │   └── Yes ↓
    │
    ├── gh account matches repo owner?
    │   ├── No → Switch account, re-fetch token
    │   ├── Account not available → gh auth login for that account
    │   └── Yes ↓
    │
    ├── Releasable commits exist? (feat:/fix:/BREAKING)
    │   ├── No → STOP, inform user "no version-bumping commits"
    │   └── Yes ↓
    │
    ├── Working directory clean?
    │   ├── No → Commit, stash, or discard
    │   └── Yes ↓
    │
    ├── Pull succeeds?
    │   ├── No → Resolve conflicts or network issues
    │   └── Yes ↓
    │
    ├── Push succeeds (SSH)?
    │   ├── No → Try HTTPS with token auth
    │   └── Yes ↓
    │
    ├── Run semantic-release
    │   │
    │   ├── Token error? → Verify account alignment first
    │   ├── Repo not found? → Wrong account, switch and retry
    │   ├── No commits to release? → Inform user
    │   └── Success ↓
    │
    ├── Verify pristine state
    │   ├── Unexpected changes → Investigate
    │   └── Clean ↓
    │
    └── Update local tracking refs
        │   git fetch origin main:refs/remotes/origin/main --no-tags
        │
        └── Verify: git status -sb (no ahead/behind) → ✅ Complete
```

---

## Success Criteria

- [ ] All prerequisites verified (including account alignment)
- [ ] Releasable commits confirmed (feat:/fix:/BREAKING present)
- [ ] Remote synced (pull + push successful)
- [ ] semantic-release executed without error
- [ ] **Version incremented** (new tag > previous tag)
- [ ] New release visible: `gh release list --limit 1`
- [ ] Working directory pristine after release
- [ ] Local tracking refs updated (no stale ahead/behind indicators)
