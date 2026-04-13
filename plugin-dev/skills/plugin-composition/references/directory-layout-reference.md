# Directory Layout Reference

> The canonical directory tree for a Claude Code plugin, with notes on each location. Sourced from [https://code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins) and the working plugins in this repo.

---

## Canonical tree (all component types)

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json              # REQUIRED — manifest
├── README.md                    # REQUIRED — user-facing documentation
├── CHANGELOG.md                 # recommended
├── LICENSE                      # recommended
│
├── skills/                      # OPTIONAL — if plugin contains skills
│   ├── <skill-1>/
│   │   ├── SKILL.md             # required per skill
│   │   ├── references/          # progressive disclosure (0..n .md files)
│   │   │   └── *.md
│   │   ├── scripts/             # skill-private scripts (0..n)
│   │   │   └── *.py / *.sh
│   │   ├── evals/               # plugin-evaluation format
│   │   │   ├── trigger-evals.json
│   │   │   └── evals.json
│   │   └── fixtures/            # test fixtures (0..n)
│   └── <skill-2>/
│       └── SKILL.md
│
├── hooks/                       # OPTIONAL — if plugin contains hooks
│   ├── hooks.json               # hook configuration
│   └── scripts/                 # hook scripts
│       └── *.sh / *.py
│
├── agents/                      # OPTIONAL — if plugin ships subagents
│   └── <agent-name>.md          # agent definition + frontmatter
│
├── commands/                    # OPTIONAL — if plugin ships slash commands
│   └── <command-name>.md        # slash command definition
│
├── .mcp.json                    # OPTIONAL — if plugin ships an MCP server
│
├── scripts/                     # OPTIONAL — shared scripts across multiple skills
│   └── *.py / *.sh
│
└── bin/                         # OPTIONAL — alternative to scripts/ for CLI wrappers
    └── plugin-cli
```

---

## Location rules

### `.claude-plugin/plugin.json` — the manifest

Must live in `.claude-plugin/`, not at the plugin root. This directory exists specifically to scope plugin metadata and avoid colliding with the plugin's own files.

**Wrong**:
```
my-plugin/plugin.json       ❌
```

**Right**:
```
my-plugin/.claude-plugin/plugin.json   ✓
```

### `README.md` — at the plugin root

The root README is user-facing. It describes what the plugin does, how to install it, and how to use its main capabilities. It should NOT duplicate SKILL.md content — the README explains the plugin, SKILL.md teaches the skill.

### `skills/<name>/SKILL.md` — one per skill

Each skill gets its own directory under `skills/`, named exactly like the skill's `name` in frontmatter. For single-skill plugins, convention is to match the plugin name (`plugin-name/skills/plugin-name/SKILL.md`).

### `skills/<name>/references/*.md` — progressive disclosure

Reference files are loaded on demand when the skill body mentions them. They exist to keep SKILL.md under ~500 lines while preserving depth. Filenames should be descriptive (`eval-file-formats.md`, not `ref1.md`).

### `skills/<name>/scripts/` — skill-private scripts

Scripts used ONLY by this skill. If two skills need the same script, promote it to the plugin-level `scripts/` directory.

### `skills/<name>/evals/` — activation and output tests

Two files: `trigger-evals.json` (activation testing) and `evals.json` (output testing). Format documented in `plugin-evaluation` skill.

### `hooks/hooks.json` — hook configuration

Single file listing all hooks the plugin registers. Each hook entry has `matcher`, `hooks` array, and optional `description`.

### `hooks/scripts/` — hook scripts

Bash/Python scripts referenced by `hooks.json`. Live under `hooks/` not `scripts/` to make it clear they are hook-specific and to avoid accidental sharing with skill code.

### `agents/<name>.md` — subagent definitions

Each subagent is one markdown file with YAML frontmatter (`name`, `description`, `tools`, `model`) and a body describing the agent's task.

### `commands/<name>.md` — slash command definitions

Each slash command is one markdown file. The file body becomes the command's prompt when invoked.

### `.mcp.json` — MCP server config

A single file at the plugin root declaring the MCP server's command, args, env, and metadata. The actual server code can live anywhere — `mcp-server/`, `server/`, or embedded in `scripts/`.

### `scripts/` (plugin root) — shared scripts

For scripts used by multiple skills OR by both skills and hooks. Reference with `${CLAUDE_PLUGIN_ROOT}/scripts/X`.

### `bin/` — executable wrappers

Alternative to `scripts/` for tools the user may run directly. Convention: files here are executable (`chmod +x`) and have a shebang.

---

## Common layout mistakes

### Skills directly under plugin root

```
my-plugin/
├── SKILL.md                     ❌ missing skills/<name>/ wrapper
└── .claude-plugin/plugin.json
```

Skills must be inside `skills/<name>/`, even for single-skill plugins.

### Multiple plugin.json files

```
my-plugin/
├── .claude-plugin/plugin.json
└── skills/my-skill/
    └── plugin.json              ❌ no — the skill uses SKILL.md, not plugin.json
```

Only one `plugin.json` per plugin. Skills use SKILL.md with frontmatter.

### Scripts in the wrong level

```
my-plugin/
├── scripts/format.sh            # ❌ if only one skill uses it
└── skills/my-skill/
    └── SKILL.md
```

If only one skill uses `format.sh`, move it to `skills/my-skill/scripts/format.sh`.

### Hooks dir with no hooks.json

```
my-plugin/
└── hooks/
    └── scripts/some.sh          ❌ missing hooks.json
```

A `hooks/` directory is meaningless without `hooks.json` to wire the scripts to events.

### MCP config inside .claude-plugin/

```
my-plugin/.claude-plugin/
├── plugin.json
└── .mcp.json                    ❌ wrong location
```

`.mcp.json` lives at the plugin root, not inside `.claude-plugin/`.

### Multi-level skill nesting

```
my-plugin/skills/category/skill-1/SKILL.md   ❌
```

Skills are one level deep under `skills/`. No subcategories.

---

## Layout for each plugin shape

### Shape 1: single-skill plugin

```
skill-forge/
├── .claude-plugin/plugin.json
├── README.md
└── skills/skill-forge/
    ├── SKILL.md
    └── references/
```

### Shape 2: multi-skill plugin (shared scripts)

```
plugin-dev/
├── .claude-plugin/plugin.json
├── README.md
├── scripts/                     # shared across all skills
│   ├── validate_plugin.py
│   ├── scaffold_plugin.py
│   ├── run_eval.py
│   └── test_hook.sh
└── skills/
    ├── plugin-ideation/
    ├── plugin-research/
    ├── plugin-architecture/
    ├── plugin-hooks/
    ├── plugin-composition/
    ├── plugin-validation/
    └── plugin-evaluation/
```

### Shape 3: hooks + skill

```
repo-linter/
├── .claude-plugin/plugin.json
├── README.md
├── hooks/
│   ├── hooks.json
│   └── scripts/run-linter.sh
└── skills/lint-fixing/
    └── SKILL.md
```

### Shape 4: MCP + skill

```
customer-data/
├── .claude-plugin/plugin.json
├── README.md
├── .mcp.json
├── mcp-server/
│   ├── package.json
│   └── server.js
└── skills/customer-lookup/
    └── SKILL.md
```

### Shape 5: full composition

```
pr-toolkit/
├── .claude-plugin/plugin.json
├── README.md
├── skills/
│   ├── pr-review/
│   ├── pr-risk-assessment/
│   └── pr-changelog-gen/
├── hooks/
│   ├── hooks.json
│   └── scripts/on-pr-open.sh
├── commands/
│   └── review-pr.md
├── agents/
│   └── pr-reviewer.md
└── .mcp.json
```

---

## Validation

The structural validator (`plugin-validation` skill) walks this layout and reports:

- Missing `plugin.json` or `README.md`
- Missing `SKILL.md` in each skill directory
- Frontmatter errors in SKILL.md
- Dead `references/X.md` citations
- Mismatches between `plugin.json:name` and skill frontmatter `name` (for single-skill plugins)

Run `python3 plugin-dev/scripts/validate_plugin.py --plugin-dir <path>` before committing layout changes.
