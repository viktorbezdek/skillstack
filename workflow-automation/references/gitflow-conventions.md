# GitFlow Conventions Reference

## Branch Types

### feature/*
**Purpose:** New features and enhancements
**Base:** main or develop
**Naming:** `feature/descriptive-name`
**Examples:**
- `feature/email-notifications`
- `feature/user-dashboard`
- `feature/real-time-updates`

**Workflow:**
```bash
git checkout main
git checkout -b feature/my-feature
# Make changes
git commit -m "Add feature"
git push origin feature/my-feature
# Create PR to main
```

### fix/* or bugfix/*
**Purpose:** Bug fixes
**Base:** main or develop
**Naming:** `fix/descriptive-name`
**Examples:**
- `fix/login-timeout`
- `fix/validation-error`
- `bugfix/memory-leak`

### hotfix/*
**Purpose:** Critical production fixes
**Base:** main
**Naming:** `hotfix/descriptive-name`
**Examples:**
- `hotfix/security-patch`
- `hotfix/data-corruption`
- `hotfix/critical-bug`

**Workflow:**
```bash
git checkout main
git checkout -b hotfix/critical-fix
# Fix issue
git commit -m "Fix critical bug"
# Merge to main AND develop
git checkout main && git merge hotfix/critical-fix
git checkout develop && git merge hotfix/critical-fix
```

### release/*
**Purpose:** Release preparation
**Base:** develop
**Naming:** `release/version`
**Examples:**
- `release/1.2.0`
- `release/v2.0.0-beta`

## Naming Best Practices

### Good Names ✅
- `feature/email-notifications` - Clear and specific
- `fix/login-timeout-error` - Describes the problem
- `hotfix/security-vulnerability` - Urgent and clear

### Bad Names ❌
- `feature/stuff` - Too vague
- `feature/My Feature` - Has spaces
- `feature/implement-email-notifications-system-with-queue` - Too long

### Guidelines
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise
- 2-4 words ideal
- No spaces, underscores, or special characters (except hyphens)

## Merge Strategy

**Feature → Main:**
```bash
# Create PR
gh pr create --base main --head feature/my-feature

# After approval
git checkout main
git merge feature/my-feature
git branch -d feature/my-feature
```

**Hotfix → Main + Develop:**
```bash
git checkout main
git merge hotfix/critical-fix
git checkout develop
git merge hotfix/critical-fix
git branch -d hotfix/critical-fix
```

## Branch Lifecycle

1. **Create** branch from base (main/develop)
2. **Develop** feature in branch
3. **Push** to remote regularly
4. **Create PR** when ready
5. **Review** and approve
6. **Merge** to base branch
7. **Delete** branch after merge

## Worktree Integration

With worktrees, each branch has its own directory:

```
my-project/                    ← main branch
my-project-worktrees/
  feature/
    email-notifications/       ← feature/email-notifications
    user-dashboard/            ← feature/user-dashboard
  fix/
    login-timeout/             ← fix/login-timeout
```

Work in parallel without switching branches!
