# Git Workflow

> **v1.1.20** | DevOps & Infrastructure | 22 iterations

> Unified Git workflow management -- conventional commits, intelligent file grouping, worktree operations, changelog generation, semantic versioning, and story backlog tracking in one plugin.

## The Problem

Git is the most widely used version control system, yet most teams use it poorly. Commit messages are inconsistent ("fix stuff", "wip", "updates"), making changelogs impossible to generate and bisection useless for finding regressions. When a developer has 15 changed files, they dump everything into a single commit instead of grouping logically -- and the resulting commit is un-reviewable and un-revertable. Branch management is ad hoc: some developers use feature branches, others commit to main, and nobody has a consistent naming convention.

The consequences compound over time. Without conventional commits, changelogs must be written manually -- and they are always incomplete. Without intelligent file grouping, code reviews cover too much surface area and miss bugs in the noise. Without worktree management, developers stash and unstash constantly, losing context and occasionally losing work. Without issue tracking integration, the link between code changes and business requirements lives only in developers' heads, and it leaves with them.

The deeper problem is that each of these concerns (commits, branches, changelogs, versioning, story tracking) is typically addressed by a separate tool or convention, with no integration between them. A commit's type determines the version bump. A branch's pattern determines the commit scope. An issue reference in the commit determines the changelog entry. These relationships exist but are enforced manually, which means they break constantly.

## The Solution

This plugin unifies five aspects of Git workflow management into a single skill: commit management (conventional commits, quality analysis, intelligent file grouping), branch workflows (GitFlow conventions, worktree operations), issue integration (automatic detection and linking), release management (changelog generation, semantic versioning), and story backlog management (hierarchical story tree with commit-based implementation tracking).

The skill ships with 13 automation scripts covering the full workflow: diff analysis and commit suggestion, message validation, intelligent file grouping by scope and type, changelog generation from commit history, semantic version calculation, worktree creation and cleanup, issue synchronization, and tree visualization. It includes 13 reference files covering the full conventional commits specification, commit patterns and anti-patterns, GitFlow conventions, story tree database schema, SQL query patterns, and orchestrator workflow diagrams. A commit templates JSON asset provides structured templates for every commit type.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Commit messages are inconsistent ("fix stuff", "updates") making changelogs impossible to generate | Conventional commits enforced with type/scope/subject format, validated by automation scripts |
| 15 changed files dumped into one commit -- un-reviewable, un-revertable | Intelligent file grouping sorts changes by scope and type into atomic commits |
| Branch naming is ad hoc; some use feature/, some use feat-, some use nothing | GitFlow conventions with consistent branch types (feature/, fix/, hotfix/, release/) |
| Changelogs written manually and always incomplete | Changelog auto-generated from conventional commits with breaking changes, features, and fixes |
| Version bumps are guesswork; someone picks a number | Semantic versioning calculated automatically from commit types (breaking -> major, feat -> minor, fix -> patch) |
| No connection between code changes and user stories | Story tree database links commits to hierarchical user stories with acceptance criteria |

## Context to Provide

Git workflow requests are most effective when you describe what you have changed, not just what you want to do. The skill can work with staged diffs, file lists, and commit history -- give it the raw material.

**What information to include in your prompt:**
- **For commit writing:** the output of `git diff --staged --stat` or a list of changed files with their scope (auth, api, ui); the issue or ticket number you are closing; whether any changes are breaking
- **For changelog generation:** the previous version tag or date range to cover; which audiences the changelog is for (users, developers, operators); whether you need a GitHub release format
- **For version calculation:** the previous version string; any commits since that version that include `BREAKING CHANGE` or `feat!` footers
- **For worktree operations:** the feature name, base branch, and whether you need it inside the repo root or alongside it
- **For story tree management:** your project structure and whether you are initializing fresh or linking commits to existing stories

**What makes results better:**
- Running `git diff --staged --stat` and pasting the output -- the skill uses file paths to infer scope automatically
- Including the branch name (which often contains the issue number or feature name for auto-linking)
- Specifying the audience for changelogs (end users want plain language; developers want commit-level detail)
- Listing commits since the last tag with `git log v1.3.0..HEAD --oneline` for accurate version and changelog generation

**What makes results worse:**
- Asking the skill to "just commit everything" -- it will push back and suggest grouping; save time by asking for grouping upfront
- Requesting changelogs without specifying the version range -- "make a changelog" with no context produces a placeholder
- Using relative time references ("last week's commits") instead of tag names or SHAs

**Template prompt -- commit writing:**
```
Help me write commits for these staged changes. Output of git diff --staged --stat:
[paste stat output here]

Branch: [branch name]
Closes: [issue #N, or "none"]
Breaking changes: [yes/no -- describe if yes]
```

**Template prompt -- changelog:**
```
Generate a changelog for version [X.Y.Z] covering all commits since [previous tag or SHA]:
[paste: git log v1.3.0..HEAD --oneline]

Audience: [end users / developers / both]
Format: [GitHub release markdown / CHANGELOG.md / Slack announcement]
```

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install git-workflow@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention git, commits, branches, changelogs, versioning, worktrees, or story management.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session in your project
3. Type: `Help me write a commit for these staged changes` -- Claude analyzes the diff and suggests properly formatted conventional commits
4. After a few commits, try: `Generate a changelog for the next release`
5. Then: `What should the next version be?` -- Claude calculates the semantic version bump from commit history

---

## System Overview

```
User prompt (commit / branch / changelog / version / story management)
        |
        v
+------------------+
|  git-workflow    |
|  skill (SKILL.md)|
+------------------+
        |
        +---> Part 1: Commit Management
        |     - Conventional commits format
        |     - Quality standards
        |     - Intelligent file grouping
        |     - Issue integration
        |
        +---> Part 2: Branch & Worktree Management
        |     - GitFlow branch conventions
        |     - Worktree operations (create/list/cleanup)
        |
        +---> Part 3: Release Management
        |     - Changelog generation
        |     - Semantic versioning
        |
        +---> Part 4: Story Tree Management
        |     - Hierarchical backlog in SQLite
        |     - Commit-based implementation tracking
        |     - Tree visualization
        |
        +---> 13 Scripts (automation)
        |     - analyze-diff, validate, changelog, version
        |     - group-files, commit-analyzer, issue-tracker
        |     - create_worktree, list_worktrees, cleanup_worktrees
        |     - tree-view, init-environment, conventional-commits
        |
        +---> 13 References (deep knowledge)
        |     - Conventional commits spec, commit patterns, examples
        |     - GitFlow conventions, workflow diagrams
        |     - Story tree schema, SQL queries, rationales
        |
        +---> 1 Asset
              - commit-templates.json (structured commit templates)
```

Single-skill plugin with 13 references, 13 scripts, and 1 asset file. The skill covers five distinct workflow areas unified by their shared dependency on Git.

## What's Inside

| Component | Type | What It Provides |
|---|---|---|
| **git-workflow** | Skill | Unified Git workflow skill covering commits, branches, releases, and story management |
| **commit-templates.json** | Asset | Structured templates for all conventional commit types |
| **13 scripts** | Script | Automation for diff analysis, validation, grouping, changelog, version, worktrees, issues, tree view |
| **13 references** | Reference | Conventional commits spec, commit patterns, GitFlow, story tree schema, SQL, workflow diagrams |
| **trigger-evals** | Eval | 13 trigger eval cases (8 positive, 5 negative) |
| **output-evals** | Eval | 3 output quality eval cases |

### Component Spotlights

#### git-workflow (skill)

**What it does:** Activates when you work with git commits, branches, changelogs, versioning, worktrees, or story backlogs. Provides conventional commit formatting, intelligent file grouping, GitFlow branch conventions, automated changelog generation, semantic version calculation, and hierarchical story management with a SQLite database.

**Input -> Output:** You describe a git operation (writing a commit, creating a branch, generating a changelog, managing stories) -> The skill provides the proper format, automates the analysis, and produces the output using its suite of scripts.

**When to use:**
- Writing or reviewing commit messages for conventional commits compliance
- Grouping changed files into logical atomic commits
- Managing feature branches and worktrees with GitFlow conventions
- Generating changelogs from commit history
- Calculating the next semantic version from commit types
- Managing a hierarchical story backlog linked to code changes

**When NOT to use:**
- CI/CD pipeline configuration or deployment YAML -> use [cicd-pipelines](../cicd-pipelines/)
- Workflow orchestration or release automation -> use [workflow-automation](../workflow-automation/)
- Code review (the content, not the commit format) -> use [code-review](../code-review/)

**Try these prompts:**

```
Help me write commits for these staged changes. git diff --staged --stat output:
 src/auth/jwt.ts    | 89 ++++++++++++++++++++++++
 src/auth/refresh.ts | 45 ++++++++++++
 tests/auth/jwt.test.ts | 112 +++++++++++++++++++++++++++++++
 src/api/users.ts   | 12 +--
 tests/api/users.test.ts | 28 ++++----
 docs/auth.md        | 34 +++++++++
Branch: feature/142-jwt-refresh. Closes #142.
```

```
Group my 14 changed files into atomic commits. Files changed: src/auth/ (3 files: new JWT refresh feature), src/api/users.ts (null pointer fix), tests/ (4 test files covering both), docs/ (auth endpoint docs updated, migration guide added).
```

```
Generate a changelog for version 2.0.0. Commits since v1.5.0:
[paste: git log v1.5.0..HEAD --oneline]
Audience: end users and API consumers. Format: GitHub release markdown. Breaking changes: the /auth endpoint now requires Bearer tokens.
```

```
Create a feature worktree for the email-notifications feature. Base branch: main. I want it at ../project-worktrees/feature/email-notifications following GitFlow conventions.
```

```
Initialize a story tree for our project. We are starting a new sprint. Here are our epics: user authentication (JWT), notification system (email + push), and admin dashboard. Generate the story hierarchy from these epics.
```

**Key references:**

| Reference | Topic |
|---|---|
| `conventional-commits.md` | Full conventional commits specification |
| `commit-patterns.md` | Commit patterns and anti-patterns |
| `examples.md` | Commit examples for each type |
| `slash-commands.md` | Detailed command workflows |
| `gitflow-conventions.md` | GitFlow branch reference |
| `schema.sql` | Story tree database schema |
| `sql-queries.md` | SQL query patterns for story operations |
| `common-mistakes.md` | Error prevention for story tree |
| `rationales.md` | Design decisions and rationale |
| `epic-decomposition.md` | Epic breakdown workflow |
| `workflow-diagrams.md` | Visual workflow diagrams |
| `orchestrator-workflow-complete.md` | Full orchestrator target state |
| `orchestrator-workflow-current.md` | Current orchestrator implementation |

#### Scripts (automation tools)

| Script | What It Does |
|---|---|
| `analyze-diff.py` | Analyzes staged changes, suggests commit messages |
| `validate.py` | Validates commit message against conventional commits format |
| `group-files.py` | Groups changed files by scope and type for atomic commits |
| `commit-analyzer.py` | Full commit quality analysis |
| `conventional-commits.py` | Conventional commits helper |
| `changelog.py` | Generates changelog from commit history |
| `version.py` | Calculates next semantic version from commit types |
| `issue-tracker.py` | Syncs and detects related issues |
| `create_worktree.sh` | Creates worktree with GitFlow conventions |
| `list_worktrees.sh` | Lists all worktrees with status |
| `cleanup_worktrees.sh` | Cleans up merged/stale worktrees |
| `init-environment.py` | Initializes GitHub workflow environment |
| `tree-view.py` | ASCII visualization of story tree |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Commit my changes" | "Help me write a conventional commit for these 8 changed files -- group them by scope" |
| "What version should this be?" | "Calculate the next semantic version based on the commits since v1.3.2" |
| "Make a changelog" | "Generate a changelog for v2.0.0 covering all commits since v1.5.0, grouped by type" |
| "Manage my branches" | "Create a feature worktree for user-preferences following GitFlow conventions" |
| "Help with stories" | "Initialize a story tree and generate user stories from the commits in the last sprint" |

### Structured Prompt Templates

**For commit writing:**
```
Help me write [a commit / commits] for [my staged changes / these files: ...]. The changes are in [scope area]. [Link to issue #N if applicable].
```

**For changelog generation:**
```
Generate a changelog for version [version] covering commits since [previous version / date / tag]. Include breaking changes, features, and bug fixes.
```

**For worktree operations:**
```
Create a [feature / fix / hotfix] worktree for [descriptive-name]. [Base branch if not main].
```

### Prompt Anti-Patterns

- **Dumping all changes in one commit:** "Just commit everything" -- the skill will push back and suggest grouping by scope and type for reviewable, revertable commits.
- **Vague commit messages:** "Save my work" or "wip" -- the skill enforces conventional commits format with imperative mood, lowercase, and no trailing period.
- **Asking for CI/CD pipeline setup:** "Set up GitHub Actions for my releases" -- this skill handles the git workflow (commits, branches, changelogs), not the CI/CD pipeline. Use [cicd-pipelines](../cicd-pipelines/) for that.

## Real-World Walkthrough

You are midway through a sprint. You have been working on an authentication feature and a related API fix, plus you updated some documentation. Your working tree shows 14 changed files across `src/auth/`, `src/api/`, `tests/`, and `docs/`. You need to commit these properly before your PR review.

**Step 1: Intelligent file grouping.** You ask Claude: **"Group my 14 changed files into atomic commits."**

Claude activates the git-workflow skill and runs the grouping analysis. It identifies three logical groups:

- **Group 1: `feat(auth)` -- 5 files, 245 LOC** -- The new JWT token refresh mechanism (3 implementation files + 2 test files)
- **Group 2: `fix(api)` -- 4 files, 45 LOC** -- The null pointer fix in user lookup (2 implementation files + 2 test files)
- **Group 3: `docs` -- 5 files, 120 LOC** -- Updated API documentation for the auth endpoints

**Step 2: Commit message writing.** For each group, Claude suggests a properly formatted conventional commit:

```
feat(auth): add JWT token refresh mechanism

Implements automatic token refresh 5 minutes before expiration
to maintain seamless user sessions. Refresh tokens are stored
in HTTP-only cookies with 30-day expiry.

Closes #142
```

The commit has an imperative subject ("add" not "added"), a body explaining *why* (not just *what*), and an issue reference that auto-closes the ticket on merge.

**Step 3: Version calculation.** After committing, you ask: **"What should the next version be?"**

Claude analyzes the commits since the last tag (v1.3.2). It finds:
- 1 `feat` commit (minor bump)
- 1 `fix` commit (patch bump)
- 0 breaking changes

Result: next version is **v1.4.0** (minor bump from the feature; the fix is included).

**Step 4: Changelog generation.** You ask: **"Generate the changelog for v1.4.0."**

Claude produces:

```markdown
## [1.4.0] - 2026-04-12

### Features
- **auth**: add JWT token refresh mechanism (#142)

### Bug Fixes
- **api**: prevent null pointer in user lookup (#156)
```

**Step 5: Story tree update.** Finally, you update the story tree: **"Mark the auth refresh story as implemented based on the commit."**

Claude updates the SQLite story tree database, linking the `feat(auth)` commit to the corresponding user story and marking it as `implemented`.

You have gone from 14 unsorted changed files to 3 atomic commits, a version bump, a changelog entry, and an updated story tree -- all following consistent conventions.

## Usage Scenarios

### Scenario 1: Writing quality commits for a PR

**Context:** You have 20 changed files and need to create a clean PR with logical, atomic commits.

**You say:** "Analyze my staged changes and group them into atomic commits with conventional commit messages"

**The skill provides:**
- File grouping by scope (auth, api, ui) and type (implementation, tests, docs)
- Conventional commit message for each group with proper type, scope, subject, body, and footer
- Issue reference detection from branch name and file paths
- Size warnings for commits over 200 LOC (suggesting further splitting)

**You end up with:** A PR with 3-5 clean, atomic commits that are individually reviewable and revertable.

### Scenario 2: Managing parallel feature development with worktrees

**Context:** You need to work on two features simultaneously without stashing and context-switching.

**You say:** "Create feature worktrees for user-preferences and email-notifications"

**The skill provides:**
- Two worktree directories following GitFlow conventions
- Proper branch creation from the base branch
- Directory structure: `project-root-worktrees/feature/user-preferences/`
- Listing and cleanup commands for when the features are merged

**You end up with:** Two independent working directories where you can switch by simply `cd`-ing, with no stashing needed.

### Scenario 3: Automating release changelog and versioning

**Context:** You are preparing a release and need a changelog and version number based on the commit history.

**You say:** "Generate the changelog and next version for a release covering all commits since v2.1.0"

**The skill provides:**
- Semantic version calculation (major if breaking changes, minor if features, patch if fixes only)
- Formatted changelog with breaking changes, features, bug fixes, and other sections
- Issue references extracted from commit footers
- Release notes template ready for the GitHub release page

**You end up with:** A release changelog and version number that are correct by construction -- no manual counting of features or guessing of versions.

---

## Decision Logic

The skill covers five workflow areas. Claude selects the relevant area based on your request:

| Your request mentions... | Workflow area | Key tools |
|---|---|---|
| Commits, commit messages, staged changes | Commit Management | `analyze-diff.py`, `validate.py`, `group-files.py` |
| Branches, worktrees, feature branches | Branch Management | `create_worktree.sh`, `list_worktrees.sh`, `cleanup_worktrees.sh` |
| Issues, ticket references, issue linking | Issue Integration | `issue-tracker.py` |
| Changelog, release notes, version | Release Management | `changelog.py`, `version.py` |
| Stories, backlog, user stories, story tree | Story Management | SQLite database, `tree-view.py` |

Multiple areas can be combined in a single workflow (e.g., commit -> version -> changelog).

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| No staged changes when running commit analysis | Script reports no changes to analyze | Stage files first with `git add`, then run the commit analysis |
| Commit message fails validation | Validation script reports format violations (missing type, wrong mood, too long) | The skill suggests the corrected message; common fixes: imperative mood, lowercase, no trailing period |
| Story tree database not initialized | SQLite queries fail with "no such table" | Run "Initialize story tree" to create the database schema |
| Changelog has no commits since last tag | Empty changelog generated | Verify the tag name is correct and commits exist between the specified versions |
| Worktree creation fails on existing branch | Git error: branch already exists | Use an existing worktree or delete the stale branch first |

## Ideal For

- **Teams adopting conventional commits** who need enforcement and automation, not just documentation
- **Solo developers** who want to maintain professional git hygiene with minimal effort -- the automation scripts handle grouping, formatting, and changelog generation
- **Release managers** who need changelogs and version numbers derived from code history, not manual tracking
- **Teams with parallel feature development** who need worktree management with consistent conventions
- **Product teams** who want to link code changes to user stories automatically through commit analysis

## Not For

- **CI/CD pipeline configuration** -- YAML files, GitHub Actions, deployment automation. Use [cicd-pipelines](../cicd-pipelines/)
- **Workflow orchestration** -- release automation, multi-stage deployment. Use [workflow-automation](../workflow-automation/)
- **Code review content** -- reviewing the actual code quality, security, and performance. Use [code-review](../code-review/)

## Related Plugins

- **[CI/CD Pipelines](../cicd-pipelines/)** -- Configure GitHub Actions, GitLab CI, and deployment pipelines that consume the commits and changelogs this plugin produces
- **[Workflow Automation](../workflow-automation/)** -- Orchestrate release workflows that use the version calculation and changelog from this plugin
- **[Code Review](../code-review/)** -- Review the code content that goes into the atomic commits this plugin helps create
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions for branches, commits, and tags

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
