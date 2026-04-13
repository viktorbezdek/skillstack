# Git Workflow

> **v1.1.20** | DevOps & Infrastructure | 22 iterations

Comprehensive Git workflow management covering conventional commits, commit quality analysis, intelligent file grouping, worktree management with GitFlow conventions, issue tracking integration, changelog generation, semantic versioning, and hierarchical story backlog management.

## What Problem Does This Solve

Git histories in real projects become unreadable messes of "fix stuff" and "wip" commits, changelogs never get written, and teams lose track of which user stories have actually shipped. This skill unifies four previously separate workflows -- conventional commit authoring, branch and worktree management, changelog and semantic versioning, and a self-updating story backlog -- into a single reference with scripts that automate the tedious parts.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install git-workflow@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

A large single-skill plugin with a SKILL.md, 13 reference files, 13 scripts, and a commit templates asset.

### SKILL.md Structure

| Part | What It Covers |
|---|---|
| **Commit Management** | Conventional commits format (Angular convention), type reference (`feat`, `fix`, `docs`, `refactor`, etc.), subject rules (imperative mood, no period, lowercase, under 100 chars), footer conventions (`BREAKING CHANGE`, `Closes #N`), and quality standards |
| **Intelligent File Grouping** | Algorithms for grouping staged files by scope and type to produce atomic, reviewable commits |
| **Branch & Worktree Management** | GitFlow branch type conventions with naming guidelines, and scripts for creating, listing, and cleaning up parallel worktrees |
| **Release Management** | Changelog generation and semantic version calculation from commit history |
| **Story Tree Management** | SQLite-backed hierarchical backlog with commit-based auto-marking, capacity management, and ASCII tree visualisation |

### Reference Files (13 files)

- `conventional-commits.md` -- Format specification and rules
- `commit-patterns.md` -- Real-world commit message patterns and examples
- `common-mistakes.md` -- Frequent commit message errors and fixes
- `gitflow-conventions.md` -- Branch naming and workflow conventions
- `slash-commands.md` -- `/commit`, `/validate`, `/changelog`, `/version` command reference
- `examples.md` -- Worked examples of good and bad commits
- `rationales.md` -- Why conventional commits matter
- `epic-decomposition.md` -- Breaking epics into story trees
- `schema.sql` -- SQLite schema for the story tree database
- `sql-queries.md` -- Queries for story tree management
- `workflow-diagrams.md` -- Visual workflow diagrams
- `orchestrator-workflow-current.md` / `orchestrator-workflow-complete.md` -- Full orchestration workflows

### Scripts (13 files)

| Script | Purpose |
|---|---|
| `analyze-diff.py` | Analyse staged diff to suggest commit message |
| `commit-analyzer.py` | Evaluate commit quality against standards |
| `conventional-commits.py` | Generate conventional commit messages |
| `validate.py` | Validate commit message format (type, scope, subject, length) |
| `group-files.py` | Group staged files by scope for atomic commits |
| `changelog.py` | Generate grouped markdown changelog from commit history |
| `version.py` | Calculate next semantic version from commits |
| `create_worktree.sh` | Create a new Git worktree with GitFlow conventions |
| `list_worktrees.sh` | List active worktrees |
| `cleanup_worktrees.sh` | Clean up stale worktrees |
| `issue-tracker.py` | Integrate commit references with issue tracking |
| `tree-view.py` | Render story tree with ASCII visualisation |
| `init-environment.py` | Initialise the Git workflow environment |

## How to Use

**Direct invocation:**

```
Use the git-workflow skill to write a commit message for these staged changes
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`git` · `conventional-commits` · `changelog` · `worktree`

## Usage Scenarios

**1. Writing a commit message for a complex changeset.** You have 12 staged files spanning auth, API, and tests. The skill analyses the diff, groups files by scope, and suggests splitting into separate commits -- `feat(auth): add JWT refresh` and `test(auth): add token expiry tests` -- each with a properly formatted body and footer.

**2. Generating a release changelog.** You are tagging v2.0.0 and need a changelog for the release notes. Run `changelog.py` against the commit history since the last tag and get grouped markdown with breaking changes at the top, followed by features, bug fixes, and everything else -- ready to paste into your GitHub release.

**3. Working on two features simultaneously without stashing.** You need to fix a bug on `main` while your feature branch has uncommitted work. Use `create_worktree.sh` to create a parallel worktree for the bugfix, work on both in separate directories, and clean up with `cleanup_worktrees.sh` when done.

**4. Tracking which user stories have shipped.** Your team's story backlog lives in a SQLite database managed by the story tree scripts. After a release, run the commit analyser against recent history to auto-mark stories as "implemented" based on commit references, then render the updated tree with status symbols showing what shipped and what remains.

**5. Validating commit messages in CI.** Add `validate.py` to your CI pipeline to reject commits that violate the conventional format before they reach `main`. The script checks type validity, scope format, subject rules (imperative mood, no period, under 100 chars), and footer syntax.

## When to Use / When NOT to Use

**Use when:** You need help with commit messages, branch management, worktree operations, changelog generation, semantic versioning, or story backlog tracking.

**Do NOT use for:**
- **CI/CD pipelines or pipeline YAML** -- use [cicd-pipelines](../cicd-pipelines/)
- **Workflow orchestration or release automation** -- use [workflow-automation](../workflow-automation/)

## Related Plugins in SkillStack

- **[CI/CD Pipelines](../cicd-pipelines/)** -- GitHub Actions, GitLab CI, Jenkins, Terraform, and infrastructure as code
- **[Cloud FinOps](../cloud-finops/)** -- AI cost management, cloud billing, and FinOps practices
- **[Docker Containerization](../docker-containerization/)** -- Dockerfiles, multi-stage builds, and Docker Compose orchestration
- **[Workflow Automation](../workflow-automation/)** -- CI/CD pipelines, multi-agent orchestration, and parallel task execution

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
