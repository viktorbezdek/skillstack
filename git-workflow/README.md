# Git Workflow

> Comprehensive Git workflow management covering conventional commits, commit quality analysis, intelligent file grouping, worktree management with GitFlow conventions, issue tracking integration, changelog generation, semantic versioning, and hierarchical story backlog management.

## Overview

Git is the universal version control tool, but using it effectively requires discipline around commit messages, branch strategies, release management, and project tracking. Most teams use Git inconsistently -- vague commit messages, tangled branches, manual changelogs, and disconnected issue tracking. This skill automates and enforces professional Git practices across the entire workflow.

The Git Workflow skill is for individual developers who want clean commit histories, teams that need consistent conventional commits, release managers generating changelogs and versioning, and project leads managing story backlogs. It combines four previously separate skills (story-tree, managing-commits, git-commit-assistant, git-workflow-manager) into a unified toolkit with 13 automation scripts and 13 reference documents.

As part of the SkillStack collection, this skill integrates with debugging for tracking regressions through commit history, docker-containerization for worktree-based parallel development with isolated environments, and documentation-generator for automated changelog and release documentation.

## What's Included

### References

- `references/conventional-commits.md` - Full conventional commits specification and rules
- `references/commit-patterns.md` - Commit message patterns and anti-patterns
- `references/examples.md` - Real-world commit message examples across all types
- `references/slash-commands.md` - Detailed slash command workflows (/commit, /validate, /changelog, etc.)
- `references/gitflow-conventions.md` - GitFlow branch naming and workflow reference
- `references/schema.sql` - Story tree database schema (closure table pattern)
- `references/sql-queries.md` - SQL query patterns for story tree operations
- `references/common-mistakes.md` - Common story tree and commit mistakes with prevention
- `references/rationales.md` - Design decisions and rationale for the skill's architecture
- `references/epic-decomposition.md` - Epic decomposition workflow and patterns
- `references/workflow-diagrams.md` - Visual workflow diagrams for key processes
- `references/orchestrator-workflow-complete.md` - Full orchestrator workflow specification
- `references/orchestrator-workflow-current.md` - Current active orchestrator workflow

### Scripts

- `scripts/analyze-diff.py` - Analyze staged changes and suggest conventional commit messages
- `scripts/validate.py` - Validate commit message format against conventional commits spec
- `scripts/changelog.py` - Generate changelog from git commit history
- `scripts/version.py` - Calculate next semantic version based on commits
- `scripts/commit-analyzer.py` - Full commit quality analysis with scoring
- `scripts/conventional-commits.py` - Conventional commits helper and formatter
- `scripts/group-files.py` - Intelligent file grouping for atomic commits
- `scripts/issue-tracker.py` - Issue sync, detection, and reference suggestion
- `scripts/create_worktree.sh` - Create git worktree with GitFlow branch conventions
- `scripts/list_worktrees.sh` - List all worktrees with detailed status information
- `scripts/cleanup_worktrees.sh` - Clean up merged or stale worktrees
- `scripts/init-environment.py` - Initialize GitHub workflow environment
- `scripts/tree-view.py` - ASCII visualization of the story tree with capacity indicators

### Assets

- `assets/commit-templates.json` - Template patterns for all conventional commit types

## Key Features

- Conventional commits enforcement with automatic validation and format suggestions
- Intelligent file grouping that analyzes staged changes and recommends atomic commit splits
- Commit quality scoring with detailed analysis of message clarity, scope, and issue linking
- GitFlow-compliant worktree management for parallel feature development
- Automated changelog generation from commit history with breaking changes, features, and fixes
- Semantic version calculation based on commit types (major/minor/patch)
- Issue tracking integration with automatic detection from branch names and keyword matching
- Hierarchical story tree with SQLite-backed closure table for backlog management
- Slash commands (/commit, /validate, /changelog, /version, /fix) for quick access to workflows

## Usage Examples

**Write a commit message for staged changes:**
```
/commit
```
Analyzes the staged diff, detects the appropriate type and scope, suggests an issue reference from the branch name, and generates a properly formatted conventional commit message.

**Validate a commit message:**
```
/validate "feat(auth): add OAuth2 login flow"
```
Checks the message against conventional commits specification, validates type, scope format, subject rules (imperative mood, no period, lowercase), and reports any violations.

**Generate a changelog for a release:**
```
/changelog
```
Scans commit history since the last tag, groups commits by type (breaking changes, features, fixes), formats them with scope prefixes and issue references, and outputs a Keep a Changelog-formatted document.

**Determine the next version:**
```
/version
```
Analyzes all commits since the last version tag, identifies the highest-impact change type (breaking = major, feat = minor, fix = patch), and outputs the recommended next version number.

**Split a large set of changes into atomic commits:**
```
I have 15 modified files staged. Help me group them into proper atomic commits.
```
Runs group-files.py to analyze file relationships by scope, type, and dependency, then recommends 3-5 atomic commit groups with suggested messages for each.

## Quick Start

1. **Analyze your staged changes** and get a commit suggestion:
   ```bash
   python scripts/analyze-diff.py --analyze
   ```

2. **Validate a commit message** before committing:
   ```bash
   python scripts/validate.py "feat(auth): add JWT refresh"
   ```

3. **Group files** for atomic commits when you have many changes:
   ```bash
   python scripts/group-files.py --analyze
   ```

4. **Create a worktree** for parallel development:
   ```bash
   ./scripts/create_worktree.sh feature email-notifications
   ```

5. **Generate a changelog** from your commit history:
   ```bash
   python scripts/changelog.py --version 2.0.0
   ```

6. **Calculate the next version**:
   ```bash
   python scripts/version.py --verbose
   ```

7. **Visualize your story tree**:
   ```bash
   python scripts/tree-view.py --show-capacity
   ```

## Related Skills

- **debugging** -- Track down regressions through commit history and git bisect
- **docker-containerization** -- Manage isolated Docker environments per git worktree
- **documentation-generator** -- Generate changelogs and release documentation automatically
- **edge-case-coverage** -- Ensure commits for edge case fixes are properly categorized and linked

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — `claude plugin add github:viktorbezdek/skillstack/git-workflow` -- 34 production-grade skills for Claude Code.
