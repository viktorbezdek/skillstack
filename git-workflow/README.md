# Git Workflow

> **v1.1.20** | DevOps & Infrastructure | 22 iterations

Comprehensive Git workflow management skill covering conventional commits, commit quality analysis, intelligent file grouping, worktree management with GitFlow conventions, issue tracking integration, changelog generation, semantic versioning, and hierarchical story backlog management.

## What Problem Does This Solve

Git histories in real projects become unreadable messes of "fix stuff" and "wip" commits, changelogs never get written, and teams lose track of which user stories have actually shipped. This skill unifies four previously separate workflows — conventional commit authoring, branch and worktree management, changelog and semantic versioning, and a self-updating story backlog — into a single reference with scripts that automate the tedious parts.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Help me write a good commit message for these changes" | `/commit` smart helper with staged-diff analysis, conventional commit format, and issue auto-detection from branch name |
| "Validate this commit message before I push" | `/validate` command and `validate.py` script checking type, scope, subject rules, and length |
| "Generate a changelog for the v2.0.0 release" | `changelog.py` script producing grouped markdown with breaking changes, features, and bug fixes |
| "What should the next version number be?" | `version.py` semantic version calculator based on presence of breaking changes, features, or fixes |
| "I need to work on two features simultaneously without stashing" | Worktree creation script with GitFlow directory conventions and list/cleanup commands |
| "Show me which user stories have been implemented based on recent commits" | Story tree management with SQLite database, commit-analysis for auto-marking stories implemented, and ASCII tree visualisation |

## When NOT to Use This Skill

- CI/CD pipelines or pipeline YAML -- use [cicd-pipelines](../cicd-pipelines/) instead

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/git-workflow
```

## How to Use

**Direct invocation:**

```
Use the git-workflow skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `git`
- `conventional-commits`
- `changelog`
- `worktree`

## What's Inside

- **Overview** -- Summary of the five capability areas: commit management, branch workflows, issue integration, release management, and story backlog.
- **Part 1: Commit Management** -- Conventional commits format reference, quality criteria, size guidelines, slash command table (`/commit`, `/validate`, `/changelog`, etc.), intelligent file grouping by scope and type, and issue-reference integration.
- **Part 2: Branch & Worktree Management** -- GitFlow branch type conventions with naming guidelines, and worktree scripts for creating, listing, and cleaning up parallel workspaces.
- **Part 3: Release Management** -- `changelog.py` for structured markdown changelogs and `version.py` for semantic version calculation from commit history.
- **Part 4: Story Tree Management** -- SQLite-backed hierarchical story backlog with commit-based auto-marking, capacity management, and ASCII tree visualisation via status symbols.
- **Scripts Reference** -- Tables listing every commit script, workflow script, and story tree script with its purpose.

## Key Capabilities

- **auth**
- **auth**
- **api**
- **api**
- **Major**
- **Minor**

## Version History

- `1.1.20` fix(languages+tools): optimize descriptions for git-workflow, mcp-server, python, typescript (b65bc7d)
- `1.1.19` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.1.18` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.1.17` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.1.16` refactor: remove old file locations after plugin restructure (a26a802)
- `1.1.15` docs: update README and install commands to marketplace format (af9e39c)
- `1.1.14` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.1.13` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.1.12` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.1.11` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)

## Related Skills

- **[Cicd Pipelines](../cicd-pipelines/)** -- Comprehensive CI/CD pipeline design, DevOps automation, infrastructure as code, container orchestration, and enterprise ...
- **[Cloud Finops](../cloud-finops/)** -- Expert Cloud FinOps guidance covering AI cost management, GenAI capacity planning, cloud billing (AWS, Azure, GCP), comm...
- **[Docker Containerization](../docker-containerization/)** -- Comprehensive Docker and containerization skill covering Docker basics, multi-stage builds, Docker Compose orchestration...
- **[Workflow Automation](../workflow-automation/)** -- Automate development workflows end-to-end including CI/CD pipelines, multi-agent orchestration, parallel task execution,...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
