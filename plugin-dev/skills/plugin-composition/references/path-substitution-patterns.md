# Path Substitution Patterns

> The four environment variables that make plugin paths portable, and how to choose between them. Sourced from [https://code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins) and [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks).

---

## The four variables at a glance

| Variable | Points to | Use for |
|---|---|---|
| `${CLAUDE_PLUGIN_ROOT}` | THIS plugin's install dir (read-only-ish) | Scripts, references, bundled assets |
| `${CLAUDE_PLUGIN_DATA}` | THIS plugin's persistent state dir | Counters, logs, cached responses, user prefs |
| `${CLAUDE_PROJECT_DIR}` | User's project root | Project-relative paths, reading `.claude/settings.json`, writing into the user's repo |
| `${CLAUDE_ENV_FILE}` | Hook-scoped scratch file for env vars | Persisting env vars from hooks to the Claude Code session |

---

## `${CLAUDE_PLUGIN_ROOT}`

### Where it points

The absolute path to the install directory of the plugin that registered the hook or is currently executing the skill. This is the directory containing `.claude-plugin/plugin.json`.

### Substitution rules

- Substituted in `hooks.json` command strings automatically
- Available as an environment variable inside hook scripts
- Available when a skill's body references a path (the tool-using flow resolves the path)

### Examples

**Hook command**:
```json
{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh"}
```

**Inside a hook script**:
```bash
#!/bin/bash
# Read a bundled config from the plugin install
config_file="$CLAUDE_PLUGIN_ROOT/config/defaults.json"
cat "$config_file"
```

**Skill body referencing a script**:
```markdown
Run `${CLAUDE_PLUGIN_ROOT}/scripts/validate_plugin.py --plugin-dir <path>`
```

### ⚠️ Wiped on plugin update

Everything under `CLAUDE_PLUGIN_ROOT` is wiped and replaced when the plugin is updated. **Never write persistent state here.** Use `CLAUDE_PLUGIN_DATA` for state, `CLAUDE_PROJECT_DIR` for project-relative writes.

### ⚠️ Only substituted for plugin hooks

`${CLAUDE_PLUGIN_ROOT}` is substituted in hooks defined inside a **plugin**'s `hooks/hooks.json`. It is NOT substituted in hooks defined in user settings (`~/.claude/settings.json`) — in that context, the variable is unset. Document this when shipping example hooks.

---

## `${CLAUDE_PLUGIN_DATA}`

### Where it points

A persistent per-plugin directory that survives plugin updates. Not shared with other plugins.

### Examples

**Counter persisted across runs**:
```bash
#!/bin/bash
# Hook script — increments a per-plugin counter on every edit
mkdir -p "$CLAUDE_PLUGIN_DATA"
count_file="$CLAUDE_PLUGIN_DATA/edit-count.txt"
count=$(cat "$count_file" 2>/dev/null || echo 0)
count=$((count + 1))
echo "$count" > "$count_file"
```

**Cached API response**:
```bash
cache_dir="$CLAUDE_PLUGIN_DATA/api-cache"
mkdir -p "$cache_dir"
if [[ ! -f "$cache_dir/$key.json" ]]; then
  curl -s https://api.example.com/thing/$key > "$cache_dir/$key.json"
fi
cat "$cache_dir/$key.json"
```

**User preference file**:
```bash
prefs="$CLAUDE_PLUGIN_DATA/user-prefs.json"
if [[ ! -f "$prefs" ]]; then
  echo '{"theme":"default"}' > "$prefs"
fi
```

### Isolation

`$CLAUDE_PLUGIN_DATA` is isolated per plugin — plugin A cannot read plugin B's data directory. If two plugins must share state, coordinate through `$CLAUDE_PROJECT_DIR` (project-scoped) or through an external store.

---

## `${CLAUDE_PROJECT_DIR}`

### Where it points

The root of the user's current project — the directory containing `.claude/settings.json` and usually the git repo root.

### Examples

**Read the user's CLAUDE.md**:
```bash
cat "$CLAUDE_PROJECT_DIR/CLAUDE.md" 2>/dev/null
```

**Write a project-scoped log**:
```bash
mkdir -p "$CLAUDE_PROJECT_DIR/.claude/logs"
echo "$(date -Iseconds): hook fired" >> "$CLAUDE_PROJECT_DIR/.claude/logs/hook.log"
```

**Load project-specific settings**:
```bash
settings="$CLAUDE_PROJECT_DIR/.claude/settings.json"
if [[ -f "$settings" ]]; then
  plugin_cfg=$(jq -r '.plugins."my-plugin" // empty' "$settings")
fi
```

### Scope rules

- Shared across all plugins (every plugin sees the same project dir for a given session)
- Persists across sessions (it's the user's repo, not a plugin artifact)
- Use for: reading user config, writing project-scoped artifacts, interoperating with the user's git workflow

### ⚠️ Writing here is visible

Anything you write under `$CLAUDE_PROJECT_DIR` shows up in the user's working directory. Be polite:
- Write under `.claude/` subdirectory (git-ignored by convention) or `.gitignore`'d paths
- Never overwrite files the user owns
- Document what you write, where, and why

---

## `${CLAUDE_ENV_FILE}`

### Where it points

A hook-scoped scratch file. Whatever you write to it is parsed as environment variables and persisted in the Claude Code session after the hook exits.

### Why it exists

Hook scripts run in a subprocess. Normal `export FOO=bar` inside a hook is lost when the subprocess exits. `$CLAUDE_ENV_FILE` solves this by giving hooks a way to "send back" env vars.

### Format

```
FOO=value
BAR=another
BAZ="value with spaces"
```

One `KEY=value` per line. Append mode is safe — Claude Code reads the file after the hook finishes.

### Examples

**FileChanged hook reloads direnv**:
```bash
#!/bin/bash
# Hook for .envrc changes — persist direnv output to Claude's env
direnv export bash | grep -E '^export ' | sed 's/^export //;s/; *$//' >> "$CLAUDE_ENV_FILE"
```

**SessionStart hook injects CI status**:
```bash
#!/bin/bash
ci_status=$(gh run list --limit 1 --json status -q '.[0].status' 2>/dev/null || echo "unknown")
echo "CI_STATUS=$ci_status" >> "$CLAUDE_ENV_FILE"
```

### Scope

- Hook-scoped: a new file per hook invocation (don't assume state persists across hooks)
- Session-persisted: env vars written to it remain set for the rest of the Claude Code session
- Not shared across plugins (each hook gets its own file)

---

## Common patterns

### Pattern 1: bundled script + persistent cache

```json
{
  "matcher": "Bash",
  "hooks": [{
    "type": "command",
    "command": "${CLAUDE_PLUGIN_ROOT}/scripts/policy-check.sh"
  }]
}
```

```bash
#!/bin/bash
# scripts/policy-check.sh
set -euo pipefail
input=$(cat)
hash=$(echo "$input" | sha256sum | awk '{print $1}')
cache_file="$CLAUDE_PLUGIN_DATA/policy-cache/$hash"
mkdir -p "$(dirname "$cache_file")"
if [[ -f "$cache_file" ]]; then
  cat "$cache_file"   # cached decision JSON
  exit 0
fi
decision=$(/"$CLAUDE_PLUGIN_ROOT/scripts/policy-engine.py" <<< "$input")
echo "$decision" > "$cache_file"
echo "$decision"
```

Uses `CLAUDE_PLUGIN_ROOT` for the bundled script and `CLAUDE_PLUGIN_DATA` for the persistent cache — the right tool for each job.

### Pattern 2: project-scoped config loader

```bash
#!/bin/bash
# SessionStart hook — loads project-specific plugin config
config="$CLAUDE_PROJECT_DIR/.claude/my-plugin.json"
if [[ -f "$config" ]]; then
  cat "$config"  # echoed as SessionStart context for Claude
fi
```

Uses `CLAUDE_PROJECT_DIR` because the config is user-owned, project-scoped, and survives plugin updates by design.

### Pattern 3: env injection

```bash
#!/bin/bash
# FileChanged hook for .envrc
if command -v direnv >/dev/null; then
  direnv export bash | sed 's/^export //; s/; *$//' >> "$CLAUDE_ENV_FILE"
fi
```

Uses `CLAUDE_ENV_FILE` because env vars must outlive the hook subprocess.

---

## Decision matrix

| Need | Use |
|---|---|
| Bundled script that doesn't change | `CLAUDE_PLUGIN_ROOT` |
| Per-user preference that survives updates | `CLAUDE_PLUGIN_DATA` |
| File in the user's repo | `CLAUDE_PROJECT_DIR` |
| Env var that persists to the session | `CLAUDE_ENV_FILE` |
| Shared state between plugin A and plugin B | `CLAUDE_PROJECT_DIR` or external store (not `CLAUDE_PLUGIN_DATA`) |
| Cache of expensive computation | `CLAUDE_PLUGIN_DATA` |
| Log of hook invocations | `CLAUDE_PLUGIN_DATA` (per plugin) or `CLAUDE_PROJECT_DIR/.claude/logs/` (project-wide) |
| Reading the user's CLAUDE.md | `CLAUDE_PROJECT_DIR` |

---

## Pitfalls

### Writing to `CLAUDE_PLUGIN_ROOT`

```bash
# ❌ Wiped on plugin update
echo "$count" > "$CLAUDE_PLUGIN_ROOT/counter.txt"
```

Use `CLAUDE_PLUGIN_DATA` instead.

### Forgetting to `mkdir -p` before writing

```bash
# ❌ Fails on first run — directory doesn't exist yet
echo "data" > "$CLAUDE_PLUGIN_DATA/state.txt"
```

```bash
# ✓ Safe
mkdir -p "$CLAUDE_PLUGIN_DATA"
echo "data" > "$CLAUDE_PLUGIN_DATA/state.txt"
```

### Expecting `CLAUDE_ENV_FILE` to persist across hook invocations

Each hook invocation gets a fresh `CLAUDE_ENV_FILE`. Don't read from it — only write. For persistent state across hook runs, use `CLAUDE_PLUGIN_DATA`.

### Assuming `CLAUDE_PLUGIN_ROOT` is set in user settings hooks

A hook copied into `~/.claude/settings.json` is NOT a plugin hook — `CLAUDE_PLUGIN_ROOT` is unset there. Substitute an absolute path when documenting hooks intended for user-settings usage.
