---
name: plugin-composition
description: Integrates multiple components inside a single Claude Code plugin — skills, hooks, MCPs, subagents, and commands — using the canonical directory layout and path substitution variables. Use when building a multi-component plugin, combining skills and hooks, laying out the plugin directory structure, working with CLAUDE_PLUGIN_ROOT or CLAUDE_PLUGIN_DATA, choosing where to put shared scripts inside a plugin, or debugging why a path reference is not resolving at runtime. Covers the canonical directory tree, path substitution variables (CLAUDE_PLUGIN_ROOT vs CLAUDE_PLUGIN_DATA vs CLAUDE_PROJECT_DIR vs CLAUDE_ENV_FILE), the bin/ shared-scripts pattern, namespacing rules, hook merge semantics, and MCP auto-start lifecycle. NOT for choosing WHICH component type to use (that's plugin-architecture) or writing an individual component's content.
---

# Plugin Composition

> **A plugin is more than the sum of its components.** Shared conventions — path substitution, namespacing, directory layout, hook merge order — make the difference between a plugin that "just works" and one that breaks the moment it meets another installed plugin.

---

## When to use this skill

- Building a plugin that contains more than one component type (e.g. skills + hooks)
- Deciding where to put shared scripts that multiple skills use
- Confused about `${CLAUDE_PLUGIN_ROOT}` vs `${CLAUDE_PLUGIN_DATA}` vs `${CLAUDE_PROJECT_DIR}`
- A path reference in a hook or skill script is not resolving at runtime
- Your plugin breaks when installed alongside another plugin that has a similar hook
- Designing an MCP server alongside a skill and unsure how they should share state

## When NOT to use this skill

- **Deciding which component type to use** → `plugin-architecture`
- **Writing a single skill's content** → `skill-foundry`
- **Writing hook scripts** → `plugin-hooks`
- **Designing MCP tools** → `mcp-server`

---

## The canonical directory layout

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json              # REQUIRED — plugin manifest
├── README.md                    # REQUIRED — user-facing docs
├── CHANGELOG.md                 # recommended
├── LICENSE                      # recommended
│
├── skills/                      # if plugin has skills
│   └── <skill-name>/
│       ├── SKILL.md             # required per skill
│       ├── references/          # progressive disclosure
│       ├── scripts/             # skill-private scripts
│       ├── evals/               # plugin-evaluation format
│       └── fixtures/
│
├── hooks/                       # if plugin has hooks
│   ├── hooks.json               # hook configuration
│   └── scripts/                 # hook scripts
│
├── agents/                      # if plugin has subagents
│   └── <agent-name>.md
│
├── commands/                    # if plugin has slash commands
│   └── <command-name>.md
│
├── .mcp.json                    # if plugin ships an MCP server
│
├── scripts/                     # SHARED scripts across multiple skills
│   └── *.py / *.sh              # referenced as ${CLAUDE_PLUGIN_ROOT}/scripts/X
│
└── bin/                         # alternative: executable wrappers
    └── plugin-cli               # invoked as ${CLAUDE_PLUGIN_ROOT}/bin/plugin-cli
```

**Rules**:
1. `plugin.json` lives in `.claude-plugin/`, not the root
2. A skill's private scripts live inside the skill directory (`skills/X/scripts/`)
3. Scripts used by multiple skills live at the plugin root (`scripts/`)
4. Hook scripts live under `hooks/scripts/` — they are not shared with skills even if the code is similar

Full annotated layout: `references/directory-layout-reference.md`.

---

## Path substitution variables

Claude Code substitutes these in `hooks.json` command strings and in skill bodies (when the skill is executed by a tool-using flow). The difference between them matters:

| Variable | Points to | Survives plugin update? | Shared across plugins? |
|---|---|:---:|:---:|
| `${CLAUDE_PLUGIN_ROOT}` | The install directory of THIS plugin | No — wiped on update | No |
| `${CLAUDE_PLUGIN_DATA}` | Persistent state dir for THIS plugin | Yes | No |
| `${CLAUDE_PROJECT_DIR}` | The user's project root (where `.claude/` lives) | N/A | Yes |
| `${CLAUDE_ENV_FILE}` | Scratch file hooks can write into to set env vars | Per-event | Per-event |

### `CLAUDE_PLUGIN_ROOT` — the install dir

Use for read-only bundled assets: scripts, hook scripts, reference files, bundled fixtures.

```json
{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh"}
```

**⚠️ Wiped on plugin update.** Anything you write here is gone after `/plugin update`. For state, use `CLAUDE_PLUGIN_DATA`.

### `CLAUDE_PLUGIN_DATA` — persistent per-plugin state

Use for: counters, cached responses, per-user preferences, log files.

```bash
mkdir -p "$CLAUDE_PLUGIN_DATA"
echo "$count" > "$CLAUDE_PLUGIN_DATA/run-count.txt"
```

**Not shared across plugins.** If plugin A needs to see plugin B's state, they must coordinate through `CLAUDE_PROJECT_DIR` or an external store.

### `CLAUDE_PROJECT_DIR` — the user's project

Use for: project-relative paths in hook scripts, reading `.claude/settings.json`, writing into the user's repo.

```bash
# Read current project's CLAUDE.md
cat "$CLAUDE_PROJECT_DIR/CLAUDE.md"
```

### `CLAUDE_ENV_FILE` — set env vars that persist beyond the hook

Hook scripts run in a subprocess — normal `export FOO=bar` is lost when the subprocess exits. Writing to `$CLAUDE_ENV_FILE` persists the env var to the Claude Code session:

```bash
# FileChanged hook for .envrc → persist direnv env to Claude
direnv export bash >> "$CLAUDE_ENV_FILE"
```

Full examples and the common pitfalls are in `references/path-substitution-patterns.md`.

---

## The `scripts/` vs `bin/` pattern

Both are valid patterns for shared executables.

**`scripts/`**: interpreted scripts called explicitly with their interpreter or with a `#!` shebang. Good for Python/Ruby/Bash tools.

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/validate_plugin.py
```

**`bin/`**: pre-wrapped executables, often a thin shim that forwards to the interpreter. Good when users may want to invoke the tool outside of Claude Code (e.g. CLI usage).

```bash
${CLAUDE_PLUGIN_ROOT}/bin/plugin-cli validate
```

**This plugin (`plugin-dev`)** uses `scripts/` because the scripts are intended for skill-internal use, not for direct user invocation.

---

## Namespacing

Two plugins with the same component name collide. Namespace defensively:

- **Skill names**: prefix with the plugin's domain (`plugin-dev-validation`, not `validation`)
- **Slash commands**: same — `/plugin-dev-scaffold` not `/scaffold`
- **Subagent names**: same — `plugin-dev-validator` not `validator`
- **Hook matchers**: no namespacing needed — matchers filter by tool name, not plugin name
- **MCP tools**: prefix with the plugin name — `plugin_dev_validate`, not `validate`

**Exception**: single-skill plugins can use an unprefixed name if it's already distinctive (`skill-foundry`, `plugin-dev`). Multi-skill plugins should consider prefixing internally (`plugin-dev/skills/plugin-hooks` rather than `plugin-dev/skills/hooks`).

---

## Hook merge semantics (when multiple plugins install)

When two plugins register hooks for the same event, they BOTH run. The order is not guaranteed — don't rely on it.

**Precedence for decisions** (from plugin-hooks SKILL.md):
```
deny > defer > ask > allow
```

A single `deny` decision stops the tool call. `allow` decisions are overridden by any non-allow from another hook.

**Rule**: write your hooks assuming other hooks also fire on the same event. Do not assume yours is the only one.

---

## MCP auto-start lifecycle

If your plugin ships `.mcp.json`, the MCP server:

1. Is auto-started when the plugin is enabled
2. Is auto-restarted if it crashes
3. Is stopped when the plugin is disabled or uninstalled

**Implications**:
- Your server must be idempotent (restarting must not corrupt state)
- Store persistent state in `$CLAUDE_PLUGIN_DATA` so it survives restarts
- Don't assume exclusive access to resources — two users with the same plugin installed are running two separate server processes

---

## How components integrate inside one plugin

The canonical integration pattern:

1. **Skill description** says "use when X" and references the MCP tool or hook behavior
2. **Hook** enforces automation or guardrails around the domain
3. **MCP server** exposes the concrete tools the skill's body instructs the model to call
4. **Command** provides a user-triggered entry point for the full workflow
5. **All share** `${CLAUDE_PLUGIN_ROOT}/scripts/` for any deterministic helper scripts

**Example** — a hypothetical `linting-toolkit` plugin:
- Skill `lint-fixing` — methodology for fixing lint errors (activates on "my code has errors")
- Hook `PostToolUse` on `Edit|Write` — runs linter in background, writes results to `$CLAUDE_ENV_FILE`
- Script `scripts/run-linter.sh` — shared by both the hook and (if the user asks explicitly) by the skill

All three reference `${CLAUDE_PLUGIN_ROOT}/scripts/run-linter.sh`. They don't duplicate the script.

---

## References

| File | Contents |
|---|---|
| `references/directory-layout-reference.md` | Canonical directory tree with notes on each location, what goes where, common layout mistakes |
| `references/path-substitution-patterns.md` | Full reference for CLAUDE_PLUGIN_ROOT, CLAUDE_PLUGIN_DATA, CLAUDE_PROJECT_DIR, CLAUDE_ENV_FILE with examples |

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
