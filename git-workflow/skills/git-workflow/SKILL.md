---
name: git-workflow
description: Git workflow management — use when the user mentions git, conventional commits, commit quality, branch management, worktree operations, GitFlow, changelog generation, semantic versioning, backlog management, or issue tracking integration. NOT for CI/CD pipelines or pipeline YAML (use cicd-pipelines), NOT for workflow orchestration or release automation (use workflow-automation), NOT for code review content or PR quality assessment (use code-review).
allowed-tools: Bash, Read, Grep, Glob, Write
---

# Git Workflow - Comprehensive Git Management Skill

Unified skill for commit management, branch workflows, worktree operations, and story backlog management.

## When to Use / Not Use

**Use when:**
- Writing, validating, or reviewing commit messages for conventional commits compliance
- Grouping changed files into logical atomic commits
- Managing feature branches and worktrees with GitFlow conventions
- Generating changelogs from commit history
- Calculating next semantic version from commit types
- Managing a hierarchical story backlog linked to code changes
- Running `/commit`, `/validate`, `/changelog`, `/version` commands

**Do NOT use when:**
- CI/CD pipeline configuration or deployment YAML -> use `cicd-pipelines`
- Workflow orchestration or release automation -> use `workflow-automation`
- Code review content (security, performance, design) -> use `code-review`

## Decision Tree

```
What Git workflow task do you need?
├── Write commits
│   ├── Single logical change -> /commit (auto-analyze staged diff)
│   ├── Multiple changed files, unclear grouping -> python scripts/group-files.py --analyze
│   ├── Validate message format -> /validate "feat(auth): add JWT refresh"
│   └── Amend/fix last commit -> /fix
├── Branch management
│   ├── New feature branch -> feature/{name}, use GitFlow conventions
│   ├── New fix branch -> fix/{name}
│   ├── Critical production fix -> hotfix/{name} from main
│   └── Need parallel work -> git worktree (scripts/create_worktree.sh)
├── Release workflow
│   ├── Generate changelog -> python scripts/changelog.py --version X.Y.Z
│   ├── Determine next version -> python scripts/version.py --verbose
│   │   ├── Has BREAKING CHANGE -> major (X.0.0)
│   │   ├── Has feat commits -> minor (0.X.0)
│   │   └── Only fix/other -> patch (0.0.X)
│   └── Clean up merged worktrees -> scripts/cleanup_worktrees.sh --merged
├── Story backlog
│   ├── Initialize tree -> "Initialize story tree"
│   ├── Generate stories -> "Generate stories for [epic-id]"
│   ├── View tree -> python scripts/tree-view.py --show-capacity
│   └── Update from commits -> "Update story tree"
├── Issue integration
│   ├── Sync issues -> python scripts/issue-tracker.py sync assigned
│   └── Suggest refs for staged changes -> python scripts/issue-tracker.py suggest-refs
└── Not a Git workflow question? -> See related skills
```

## Part 1: Commit Management

### Conventional Commits Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types** (from Angular convention):
| Type | Purpose |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, whitespace |
| `refactor` | Code change without behavior change |
| `perf` | Performance improvement |
| `test` | Adding or correcting tests |
| `chore` | Build/tooling changes |
| `ci` | CI/CD changes |
| `build` | Build system/dependencies |
| `revert` | Reverts a previous commit |

**Subject Rules:**
- Imperative mood: "add feature" not "added feature"
- No period at end
- Lowercase
- Under 100 characters

**Footer:**
- `BREAKING CHANGE:` - Breaking changes
- `Closes #N` / `Fixes #N` - Closes issue on merge
- `Refs #N` - References issue without closing
- `Co-authored-by:` - Multiple authors

### Commit Quality Standards

**Good commit message:**
```
feat(auth): add JWT token refresh mechanism

Implements automatic token refresh 5 minutes before expiration
to maintain seamless user sessions.

Closes #142
```

**Commit size guidelines:**
| Size | LOC | Action |
|---|---|---|
| Tiny | < 10 | Single logical change |
| Small | 10-50 | Typical atomic commit |
| Medium | 50-200 | Feature component |
| Large | 200-500 | Consider splitting |
| Too Large | > 500 | Definitely split |

### Slash Commands

| Command | Action |
|---------|--------|
| `/commit` | Smart commit helper with auto-analysis |
| `/validate <msg>` | Validate commit message format |
| `/types` | Show all commit types |
| `/scopes` | Explain scopes with examples |
| `/breaking` | Breaking change guide |
| `/changelog` | Generate changelog from commits |
| `/version` | Determine next semantic version |
| `/examples` | Show commit examples |
| `/fix` | Help amend/fix last commit |

### Intelligent File Grouping

When multiple files need committing, group by:

1. **Scope-Based** - Group by functional area (auth, api, ui)
2. **Type-Based** - Separate implementation, tests, docs
3. **Relationship-Based** - Keep related files together

**Workflow:**
```bash
# Analyze all changes
python {baseDir}/scripts/group-files.py --analyze

# Output example:
# Group 1: feat(auth) - 3 impl files, 245 LOC
# Group 2: test(auth) - 2 test files, 128 LOC
# Group 3: fix(api) - 2 files, 15 LOC
```

### Issue Integration

**Automatic issue detection from:**
1. Branch name: `feature/issue-42` -> #42
2. Keyword matching with file paths
3. Label correlation with file patterns

**Issue reference types:**
- `Closes #N` - Auto-closes on merge
- `Fixes #N` - Same as Closes (for bugs)
- `Refs #N` - References without closing
- `Progresses #N` - Partial progress

## Part 2: Branch & Worktree Management

### GitFlow Branch Conventions

**Branch Types:**
| Type | Pattern | Purpose |
|------|---------|---------|
| Feature | `feature/{name}` | New features |
| Fix | `fix/{name}` | Bug fixes |
| Hotfix | `hotfix/{name}` | Critical production fixes |
| Release | `release/{version}` | Release preparation |

**Naming Guidelines:**
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise (2-4 words)
- No spaces or special characters

### Worktree Operations

**Directory Structure:**
```
project-root/               <- Main repository
project-root-worktrees/     <- Worktree parent
  feature/
    email-notifications/    <- feature/email-notifications
  fix/
    login-timeout/          <- fix/login-timeout
```

**Commands:**
```bash
# Create worktree
./scripts/create_worktree.sh feature email-notifications

# List worktrees
./scripts/list_worktrees.sh --detailed

# Cleanup merged worktrees
./scripts/cleanup_worktrees.sh --merged --dry-run
```

**Benefits:**
- Parallel development on multiple features
- No stashing needed
- Fast switching (just `cd`)
- Isolated build artifacts

## Part 3: Release Management

### Changelog Generation

```bash
python {baseDir}/scripts/changelog.py --version 2.0.0
```

**Output format:**
```markdown
## [2.0.0] - 2025-01-18

### BREAKING CHANGES
- **auth**: change token format to JWT (#234)

### Features
- **auth**: add OAuth2 login (#123)
- **api**: add user search endpoint (#145)

### Bug Fixes
- **api**: prevent null pointer in user lookup (#156)
```

### Semantic Versioning

```bash
python {baseDir}/scripts/version.py --verbose
```

**Bump rules:**
- **Major** (X.0.0) - Has breaking changes
- **Minor** (0.X.0) - Has features/fixes, no breaking
- **Patch** (0.0.X) - Only other changes

## Part 4: Story Tree Management

### Purpose

Maintain a self-managing tree of user stories where:
- Each node represents a story at some granularity level
- Nodes have capacity (target child count)
- Git commits are analyzed to mark stories as implemented
- Under-capacity nodes are identified for story generation

### Database

**Location:** `.claude/data/story-tree.db`
**Pattern:** Closure table for hierarchical data

**CRITICAL:** Use Python's sqlite3 module (NOT `sqlite3` CLI):
```python
python -c "
import sqlite3
conn = sqlite3.connect('.claude/data/story-tree.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM story_nodes')
print(cursor.fetchall())
conn.close()
"
```

### Story Format

```markdown
### [ID]: [Title]

**As a** [specific user role]
**I want** [specific capability]
**So that** [specific benefit]

**Acceptance Criteria:**
- [ ] [Specific, testable criterion]
- [ ] [Specific, testable criterion]

**Related context**: [Git commits or patterns]
```

### Workflow Commands

| Command | Action |
|---------|--------|
| "Update story tree" | Run full workflow |
| "Show story tree" | Visualize current tree |
| "Tree status" | Show metrics only |
| "Set capacity for [id] to [N]" | Adjust capacity |
| "Mark [id] as [status]" | Change status |
| "Generate stories for [id]" | Force generation |
| "Initialize story tree" | Create new database |

### Tree Visualization

```bash
python {baseDir}/scripts/tree-view.py --show-capacity
```

**Status symbols:**
| Status | Symbol | Meaning |
|--------|--------|---------|
| concept | . | Idea, not approved |
| approved | v | Human approved |
| epic | E | Needs decomposition |
| planned | o | Plan created |
| in-progress | D | Partially complete |
| implemented | + | Complete/done |
| ready | # | Production ready |

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Dumping all changes in one commit | Un-reviewable, un-revertable; hides logical changes | Group by scope/type using `group-files.py`; one logical change per commit |
| Vague commit messages ("wip", "fix stuff", "updates") | Cannot generate changelog; bisect useless | Use conventional commits: type(scope): imperative subject |
| Non-imperative subject ("added feature") | Inconsistent with conventional commits; reads as past tense | Use imperative mood: "add feature" not "added feature" |
| Missing issue references | No link between code and requirements; lost knowledge | Include `Closes #N` or `Refs #N` in commit footer |
| Commit too large (>500 LOC) | Too much surface area for review; hard to revert independently | Split into atomic commits; group-files.py suggests groupings |
| Mixing concerns in one commit (impl + tests + docs) | Hard to revert just tests or just docs; bloats review | Separate: feat commit, test commit, docs commit |
| Breaking change without `BREAKING CHANGE:` footer | Changelog misses breaking changes; version bump wrong | Always document breaking changes in footer; triggers major version |
| Working on main instead of feature branch | No isolation; hard to revert; messy history | Use GitFlow: feature/ for new work, fix/ for bugs, hotfix/ for prod |
| Stashing instead of worktrees | Lost context; stash conflicts; no parallel work | Use `git worktree` for parallel feature development |
| Missing changelog before release | Manual, incomplete release notes | Run `changelog.py` auto-generated from conventional commits |
| Guessing version number | Incorrect semver; surprises in release | Run `version.py` -- auto-calculated from commit types |

## Scripts Reference

### Commit Scripts

| Script | Purpose |
|--------|---------|
| `analyze-diff.py` | Analyze staged changes, suggest commits |
| `validate.py` | Validate commit message format |
| `changelog.py` | Generate changelog from commits |
| `version.py` | Calculate next semantic version |
| `commit-analyzer.py` | Full commit quality analysis |
| `conventional-commits.py` | Conventional commits helper |
| `group-files.py` | Intelligent file grouping |
| `issue-tracker.py` | Issue sync and detection |

### Workflow Scripts

| Script | Purpose |
|--------|---------|
| `create_worktree.sh` | Create worktree with GitFlow conventions |
| `list_worktrees.sh` | List all worktrees with status |
| `cleanup_worktrees.sh` | Clean up merged/stale worktrees |
| `init-environment.py` | Initialize GitHub workflow environment |

### Story Tree Scripts

| Script | Purpose |
|--------|---------|
| `tree-view.py` | ASCII tree visualization |

## References

### Commit References
- `references/conventional-commits.md` - Full specification
- `references/commit-patterns.md` - Patterns and anti-patterns
- `references/examples.md` - Commit examples
- `references/slash-commands.md` - Detailed command workflows

### Workflow References
- `references/gitflow-conventions.md` - GitFlow reference

### Story Tree References
- `references/schema.sql` - Database schema
- `references/sql-queries.md` - SQL query patterns
- `references/common-mistakes.md` - Error prevention
- `references/rationales.md` - Design decisions
- `references/epic-decomposition.md` - Epic workflow
- `references/workflow-diagrams.md` - Visual workflows
- `references/orchestrator-workflow-complete.md` - Full orchestrator flow
- `references/orchestrator-workflow-current.md` - Current workflow

## Assets

- `assets/commit-templates.json` - Template patterns for commit types

## Integration Points

### With Issue Tracking
```bash
# Sync issues before committing
python {baseDir}/scripts/issue-tracker.py sync assigned

# Find related issues for staged changes
python {baseDir}/scripts/issue-tracker.py suggest-refs
```

### With PR Reviews
- Validate commits in PRs
- Report format violations
- Suggest improvements before merge

### With CI/CD
- Generate changelogs automatically
- Determine version bumps
- Validate commit messages in pipeline

## Error Handling

**Common issues:**
| Issue | Recovery |
|---|---|
| Empty commit message | Generate from changes |
| No staged changes | Prompt to stage |
| Format violations | Suggest correction |
| Missing issue reference | Search and suggest |
| Commit too large | Recommend splitting |
| Database not found | Initialize first |
| Checkpoint rebased | Run full scan |

## Source Skills

This skill was merged from:
1. `story-tree---autonomous-hierarchical-backlog-manager`
2. `managing-commits-skill`
3. `git-commit-assistant`
4. `git-workflow-manager-skill`
