# Git Workflow

> **v1.1.20** | DevOps & Infrastructure | 22 iterations

> Unified Git workflow management -- conventional commits, intelligent file grouping, worktree operations, changelog generation, semantic versioning, and story backlog tracking in one plugin.

## The Problem

Git histories in real projects tell no story. They are sequences of "fix stuff", "wip", "minor changes", and "update" that make `git log` useless for understanding what happened and why. When release time comes, nobody can produce a changelog because the commit messages contain no structured information. When a production bug surfaces, `git bisect` finds the commit but the message says "refactoring" with no indication of what was refactored or why.

The branching situation is equally chaotic. Developers stash uncommitted work to switch branches, lose the stash, and recreate the work. Feature branches live for weeks without cleanup. Naming conventions vary by developer -- `my-feature`, `feature/my-feature`, `feat-my-feature` -- making branch management a manual exercise. And when the team tries to track which user stories have actually shipped, they fall back to manually checking Jira because there is no link between commits and story completion.

These are not separate problems -- they are symptoms of the same root cause: Git is used as a backup tool (save my work) rather than a communication tool (tell the team what happened). Fixing any one symptom (adopting conventional commits, for example) without addressing the others produces partial improvement: the commit messages are formatted but the branches are still chaotic, the changelog still is not generated, and stories still are not tracked.

## The Solution

This plugin unifies four previously separate Git workflows into a single skill with 13 reference files, 13 scripts, and a commit templates asset. The four workflows reinforce each other: conventional commits provide the structured data that changelog generation and semantic versioning consume; branch naming conventions align with worktree management scripts; issue references in commits feed story backlog tracking.

The commit management layer provides conventional commits format (Angular convention), intelligent file grouping that splits a 12-file changeset into atomic commits by scope, quality analysis that flags problems before they enter the history, and slash commands (`/commit`, `/validate`, `/changelog`, `/version`) for quick access. The branch and worktree layer provides GitFlow conventions with naming guidelines and scripts for parallel development without stashing. The release management layer generates grouped changelogs and calculates semantic version bumps from commit history. The story tree layer maintains a SQLite-backed hierarchical backlog that auto-marks stories as implemented based on commit references.

The scripts automate the tedious parts: `analyze-diff.py` reads the staged diff and suggests a commit message, `group-files.py` splits a large changeset into logical groups, `changelog.py` generates a release changelog from commit history, `version.py` determines the next version bump, and `validate.py` enforces commit format in CI.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Commit messages say "fix stuff" and "update" -- `git log` is useless for understanding history | Conventional commits format with type, scope, subject, body, and footer produce a readable, searchable history |
| 12 staged files become one massive commit that mixes auth changes, API fixes, and test updates | Intelligent file grouping splits the changeset into 3 atomic commits by scope, each reviewable independently |
| Release notes are written manually by reading the commit log and guessing what changed | `changelog.py` generates grouped markdown with breaking changes, features, and fixes -- ready for GitHub Releases |
| Developers stash work to switch branches, sometimes losing the stash | Worktree scripts create parallel directories for simultaneous feature work -- no stashing, just `cd` |
| Version bumps are debated ("is this a minor or a patch?") without clear rules | `version.py` determines the bump automatically: breaking change = major, feat = minor, fix = patch |
| Story completion is tracked manually in Jira with no connection to actual commits | Story tree auto-marks stories as implemented based on commit references, with ASCII tree visualization |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install git-workflow@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention git, commits, branches, conventional commits, changelog, worktree, or version bumping.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session in your project
3. Stage some changes: `git add -A`
4. Type: `Write a commit message for my staged changes`
5. Claude analyzes the diff, groups files by scope if needed, and produces a properly formatted conventional commit with type, scope, imperative subject, body explaining why, and footer linking issues

## What's Inside

Large single-skill plugin with one SKILL.md, 13 reference files, 13 scripts, a commit templates asset, 13 trigger eval cases, and 3 output eval cases.

| Part | What It Covers |
|---|---|
| **Commit Management** | Conventional commits format, type reference (feat/fix/docs/refactor/etc.), subject rules, footer conventions, quality standards |
| **Intelligent File Grouping** | Algorithms for grouping staged files by scope, type, and relationship to produce atomic commits |
| **Branch & Worktree Management** | GitFlow branch conventions with naming guidelines, worktree creation/listing/cleanup scripts |
| **Release Management** | Changelog generation from commit history, semantic version calculation |
| **Story Tree Management** | SQLite-backed hierarchical backlog with commit-based auto-marking and ASCII tree visualization |

### Scripts

| Script | Purpose |
|---|---|
| `analyze-diff.py` | Analyze staged diff and suggest commit message |
| `commit-analyzer.py` | Evaluate commit quality against standards |
| `conventional-commits.py` | Generate conventional commit messages |
| `validate.py` | Validate commit message format (type, scope, subject, length) |
| `group-files.py` | Group staged files by scope for atomic commits |
| `changelog.py` | Generate grouped markdown changelog from commit history |
| `version.py` | Calculate next semantic version from commits |
| `create_worktree.sh` | Create a Git worktree with GitFlow conventions |
| `list_worktrees.sh` | List active worktrees with status |
| `cleanup_worktrees.sh` | Clean up merged or stale worktrees |
| `issue-tracker.py` | Integrate commit references with issue tracking |
| `tree-view.py` | Render story tree with ASCII visualization |
| `init-environment.py` | Initialize the Git workflow environment |

### git-workflow

**What it does:** Activates when you ask about Git operations, commit messages, branch management, worktree operations, changelog generation, semantic versioning, or story backlog tracking. Applies conventional commits format, groups files intelligently for atomic commits, manages worktrees for parallel development, generates changelogs and version bumps from commit history, and maintains a story tree that tracks which features have shipped.

**Try these prompts:**

```
Write a commit message for these staged changes -- I've modified auth, API, and test files
```

```
Generate the changelog for our v3.0 release based on commits since v2.5
```

```
I need to work on a hotfix while my feature branch has uncommitted changes -- set up a worktree
```

```
Validate this commit message: "Added new feature for user login"
```

```
What should the next version number be based on our recent commits?
```

```
Show me the story tree and which stories have been implemented based on recent commits
```

**Key references:**

| Reference | Topic |
|---|---|
| `conventional-commits.md` | Full conventional commits specification |
| `commit-patterns.md` | Real-world commit message patterns and examples |
| `common-mistakes.md` | Frequent commit message errors and how to fix them |
| `gitflow-conventions.md` | Branch naming and workflow conventions |
| `slash-commands.md` | `/commit`, `/validate`, `/changelog`, `/version` command reference |
| `examples.md` | Worked examples of good and bad commits |
| `epic-decomposition.md` | Breaking epics into story trees |
| `schema.sql` | SQLite schema for the story tree database |
| `sql-queries.md` | Queries for story tree management |
| `workflow-diagrams.md` | Visual workflow diagrams |

## Real-World Walkthrough

You are the tech lead on a team of six building a B2B SaaS platform. It is Wednesday afternoon, the v2.0 release is Friday, and the Git history is a mess. Looking at the last 50 commits, you see: "wip", "fix", "more fixes", "update tests", "refactor stuff", "merge main", "fix lint", "wip again". The PM asks for release notes and you have no idea where to start. Meanwhile, two developers are fighting over stash conflicts and a third cannot figure out which stories from the sprint actually shipped.

You start by asking Claude: **"Help me clean up our Git workflow -- I need conventional commits, a changelog, and story tracking."**

Claude activates the git-workflow skill and begins with **commit standards**. It sets up the conventional commits format for your team: every commit must use the `type(scope): subject` format with imperative mood, no period, lowercase, under 100 characters. It provides the type reference (`feat`, `fix`, `docs`, `refactor`, `perf`, `test`, `chore`, `ci`, `build`, `revert`) and explains the footer conventions (`BREAKING CHANGE:` for breaking changes, `Closes #N` for issue closure, `Refs #N` for references).

To enforce this going forward, Claude shows you how to add `validate.py` to your CI pipeline. The script checks type validity, scope format, subject rules, and footer syntax -- rejecting any commit that violates the format before it reaches `main`. You add it as a pre-commit hook locally and as a CI check for PRs.

Next, you have a problem right now: you have 15 staged files from today's work and you are not sure how to split them into commits. You ask Claude: **"Group these staged files into atomic commits."**

Claude runs the intelligent file grouping analysis. It identifies three logical groups:

```
Group 1: feat(auth) - 5 files, 245 LOC
  src/auth/oauth.ts, src/auth/token.ts, src/auth/middleware.ts,
  src/types/auth.ts, src/config/oauth.ts

Group 2: test(auth) - 4 files, 180 LOC
  tests/auth/oauth.test.ts, tests/auth/token.test.ts,
  tests/auth/middleware.test.ts, tests/fixtures/auth.ts

Group 3: fix(api) - 2 files, 35 LOC
  src/api/users.ts, src/api/middleware.ts
```

Claude suggests committing each group separately with specific messages:

```
feat(auth): add OAuth2 login with token refresh

Implements OAuth2 authorization code flow with automatic token refresh
5 minutes before expiration. Supports Google and GitHub providers.

Closes #89
```

```
test(auth): add OAuth2 and token refresh test coverage

Tests cover the full OAuth2 flow including redirect, callback, token
storage, refresh timing, and provider-specific error handling.
```

```
fix(api): prevent null pointer in user lookup when email is missing

The user search endpoint crashed when the email field was null because
the query builder assumed non-null. Added null check with appropriate
404 response.

Fixes #102
```

Now the two developers fighting over stash conflicts. You ask Claude: **"Set up worktrees so Sarah and Mike can work on their features without stashing."**

Claude walks you through the worktree scripts. Sarah is working on `feature/email-notifications` and needs to fix a bug on `main`:

```bash
# Create a worktree for the bugfix
./scripts/create_worktree.sh fix login-timeout

# Directory structure now:
# project/                          <- main repo (Sarah's feature branch)
# project-worktrees/fix/login-timeout/  <- bugfix worktree
```

Sarah can now `cd ../project-worktrees/fix/login-timeout/`, fix the bug, commit with `fix(auth): handle session timeout during OAuth redirect`, push, and `cd` back to her feature branch. No stashing, no conflicts, no lost work. When the bugfix PR is merged, `cleanup_worktrees.sh --merged` removes the worktree directory.

With the commit history now structured, you tackle the release. You ask Claude: **"Generate the v2.0 changelog and determine the version bump."**

Claude runs `version.py --verbose` against the commits since v1.5. The output shows:

```
Breaking changes: 1 (auth: change token format to JWT)
Features: 4
Bug fixes: 7
Other: 12

Recommended bump: MAJOR (1.5.0 -> 2.0.0)
Reason: Contains BREAKING CHANGE
```

Then `changelog.py --version 2.0.0` generates:

```markdown
## [2.0.0] - 2025-01-18

### BREAKING CHANGES
- **auth**: change token format to JWT (#78)

### Features
- **auth**: add OAuth2 login with token refresh (#89)
- **api**: add user search endpoint with pagination (#91)
- **dashboard**: add real-time metrics widget (#95)
- **notifications**: add email notification system (#97)

### Bug Fixes
- **api**: prevent null pointer in user lookup (#102)
- **auth**: handle session timeout during OAuth redirect (#105)
...
```

You paste this directly into the GitHub Release. The PM reads it and asks: "Did the email notification story ship completely?" You ask Claude to show the story tree, and it renders:

```
[+] Epic: User Communication (4/4 implemented)
  [+] Email notifications
  [+] In-app notifications
  [+] Notification preferences
  [+] Delivery status tracking
```

All four stories under the User Communication epic show `[+]` (implemented), auto-marked based on the commit references. The PM has their answer without checking Jira.

## Usage Scenarios

### Scenario 1: Writing a commit for a complex changeset

**Context:** You have 12 staged files spanning authentication, API, and test directories. You are not sure whether this should be one commit or several.

**You say:** "Write commit messages for my staged changes -- group them if they should be separate commits"

**The skill provides:**
- Intelligent file grouping analysis splitting the changeset by scope and type
- A conventional commit message for each group with type, scope, imperative subject, explanatory body, and footer
- Quality check against commit size guidelines (flagging any group over 500 LOC for further splitting)

**You end up with:** 2-4 atomic commits, each with a properly formatted message that explains what changed and why.

### Scenario 2: Generating a release changelog

**Context:** You are tagging v3.0.0 and need release notes for the GitHub Release page. There are 87 commits since v2.5.0.

**You say:** "Generate the changelog for v3.0 based on commits since v2.5"

**The skill provides:**
- Grouped markdown with breaking changes at the top, followed by features, bug fixes, performance improvements, and other changes
- Issue references linked for each entry
- Semantic version validation confirming that 3.0.0 is correct (breaking changes present = major bump)

**You end up with:** A formatted changelog ready to paste into GitHub Releases, with every entry linked to the relevant issue or PR.

### Scenario 3: Parallel development with worktrees

**Context:** You are mid-feature on a branch with uncommitted work. A critical production bug needs an immediate fix on `main`.

**You say:** "Set up a worktree so I can fix this production bug without touching my feature branch"

**The skill provides:**
- Worktree creation script with GitFlow naming conventions
- The parallel directory structure so you can `cd` between feature and bugfix
- Cleanup instructions for removing the worktree after the fix is merged

**You end up with:** Two separate working directories -- your feature branch untouched, and a fresh checkout of `main` for the hotfix. No stashing, no risk of losing work.

### Scenario 4: Validating commit messages in CI

**Context:** Your team agreed to use conventional commits but compliance is spotty -- developers forget the format under deadline pressure.

**You say:** "Set up commit message validation in our CI pipeline so non-conforming commits are rejected"

**The skill provides:**
- `validate.py` script that checks type validity, scope format, subject rules (imperative mood, no period, lowercase, under 100 chars), and footer syntax
- Integration instructions for pre-commit hooks and CI pipeline steps
- Common mistakes reference showing the most frequent violations and their corrections

**You end up with:** Automated enforcement that catches format violations before they reach `main`, with clear error messages telling the developer exactly what to fix.

### Scenario 5: Tracking story completion from commits

**Context:** Your PM asks which user stories from the current sprint have actually shipped, and your team has been inconsistent about updating Jira.

**You say:** "Show me which stories have been implemented based on our recent commits"

**The skill provides:**
- Story tree initialization and population from your backlog
- Commit analysis that matches issue references in commits to story nodes
- ASCII tree visualization with status symbols showing implemented, in-progress, and planned stories
- Capacity analysis identifying stories that need further decomposition

**You end up with:** A visual story tree showing exactly which stories shipped (based on commit evidence, not manual status updates) and which are still pending.

## Ideal For

- **Teams adopting conventional commits** -- the format reference, validation script, and CI integration provide a complete adoption path from "we should do this" to "it is enforced automatically"
- **Release managers generating changelogs** -- the changelog script produces formatted, grouped release notes from commit history, eliminating the manual process
- **Developers juggling multiple features** -- worktree scripts enable parallel development without stashing, losing work, or context-switching pain
- **Tech leads tracking delivery** -- the story tree connects Git commits to user stories, providing evidence-based completion tracking
- **Teams scaling their Git practices** -- the unified workflow ensures commits, branches, releases, and stories work together as a system rather than four separate tools

## Not For

- **CI/CD pipeline configuration** -- this plugin manages the Git workflow that feeds CI/CD, not the pipelines themselves. Use [cicd-pipelines](../cicd-pipelines/) for GitHub Actions, GitLab CI, and Jenkins
- **Workflow orchestration and release automation** -- use [workflow-automation](../workflow-automation/) for multi-step release processes, parallel task execution, and deployment pipelines
- **Docker and container workflows** -- use [docker-containerization](../docker-containerization/) for Dockerfiles, multi-stage builds, and Docker Compose

## How It Works Under the Hood

The plugin is a large single-skill architecture with 13 reference files and 13 scripts. The SKILL.md is organized into four parts:

1. **Commit Management** -- conventional commits format, quality standards, intelligent file grouping, issue integration, and slash commands
2. **Branch & Worktree Management** -- GitFlow conventions, worktree creation/listing/cleanup with shell scripts
3. **Release Management** -- changelog generation and semantic version calculation with Python scripts
4. **Story Tree Management** -- SQLite-backed hierarchical backlog using the closure table pattern, with commit-based auto-marking and ASCII tree visualization

The reference files provide depth behind each part: full conventional commits specification, real-world commit patterns, common mistakes, GitFlow conventions, epic decomposition guidance, SQLite schema and queries, and orchestrator workflows. The scripts provide automation: diff analysis, commit validation, file grouping, changelog generation, version calculation, worktree management, issue tracking, and tree visualization.

The four parts reinforce each other: conventional commits produce the structured data that changelog generation consumes; GitFlow branch naming aligns with worktree scripts; issue references in commit footers feed story tree auto-marking.

## Related Plugins

- **[CI/CD Pipelines](../cicd-pipelines/)** -- GitHub Actions, GitLab CI, Jenkins, and infrastructure as code -- consumes the structured commits this plugin produces
- **[Workflow Automation](../workflow-automation/)** -- Multi-agent orchestration and release automation
- **[Docker Containerization](../docker-containerization/)** -- Dockerfiles, multi-stage builds, and Docker Compose
- **[Cloud FinOps](../cloud-finops/)** -- AI cost management, cloud billing, and FinOps practices

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
