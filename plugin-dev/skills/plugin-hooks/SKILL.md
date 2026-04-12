---
name: plugin-hooks
description: Authoritative guide to Claude Code hooks — event-driven scripts that execute before or after tool calls, session events, file changes, and more. Use when writing a PreToolUse hook to block dangerous commands, a PostToolUse hook to auto-format after edits, a SessionStart hook to inject context, a Stop hook for session loops, a Notification hook for desktop alerts, a FileChanged hook for reactive environments, a WorktreeCreate hook for custom worktree provisioning, or any of the 24 documented hook events. Covers all 4 handler types (command, http, prompt, agent), matcher syntax (exact/OR-list/regex), exit code semantics, and JSON output schema. NOT for designing hook script content for a specific domain (use the domain skill) — this skill covers hook mechanics and authoring only.
---

# Plugin Hooks

> The most powerful and most trap-laden extension type. Exit code 1 does not block — only exit code 2 blocks. Matcher syntax has three modes. `updatedInput` replaces the entire tool input object, not just one field. These three facts cause most hook bugs. Learn them first.

Authoritative source: [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)

---

## When to use this skill

- Writing any hook configuration (hooks/hooks.json, settings.json)
- Debugging "my hook isn't blocking" or "my hook isn't firing"
- Choosing between hook event types for a specific capability
- Understanding exit code behavior (exit 1 vs exit 2 distinction)
- Designing safe auto-approve flows for PermissionRequest
- Setting up file-watching or cwd-change hooks

## When NOT to use this skill

- **What hook script logic to write** (domain-specific) → use the domain skill
- **MCP server authoring** → use `plugin-architecture` or `mcp-server`
- **Full plugin structure** → use `plugin-composition`

---

## Core principles

1. **Exit code 1 does not block.** Only exit code 2 blocks a tool call, prompt, or stop. Exit 1 is a non-blocking error — the action proceeds. This is the #1 source of hook bugs.
2. **Matcher syntax has three modes.** `*` or omitted = match all. Letters/digits/underscore/pipe only = exact string or `|`-separated list. Any other character = JavaScript regex. `mcp__memory` is an exact match (matches no real tool); use `mcp__memory__.*` for regex.
3. **`updatedInput` replaces the entire tool input.** In PreToolUse, returning `updatedInput` in `hookSpecificOutput` replaces ALL fields. You must echo back unchanged fields or they are lost.
4. **Async hooks cannot block.** If `async: true`, the hook runs after the action has already proceeded. Never use async for security/guardrail hooks.

---

## The 10 core events (most common in practice)

All 24 documented events are in `references/hook-event-reference.md`. These 10 are what practitioners actually use.

### PreToolUse
Fires before any tool call. Can block, modify input, or allow. The most powerful event.

```json
{
  "matcher": "Bash",
  "hooks": [{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/check.sh"}]
}
```

Input includes: `tool_name`, `tool_input` (full schema), `tool_use_id`.

Decision output:
```json
{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Blocked"}}
```
Precedence when multiple hooks run: deny > defer > ask > allow.

### PostToolUse
Fires after a tool succeeds. Cannot block. Common use: auto-format, logging, notifications.

```json
{"matcher": "Edit|Write", "hooks": [{"type": "command", "async": true, "command": "prettier --write \"$file_path\""}]}
```

### PermissionRequest
Fires when a permission dialog would appear. Can auto-approve or deny without showing the dialog.

```json
{"hookSpecificOutput": {"hookEventName": "PermissionRequest", "decision": {"behavior": "allow"}}}
```

### UserPromptSubmit
Fires before Claude processes a user prompt. Can block or add context. No matcher support — fires on every prompt.

### SessionStart
Fires at session start, resume, clear, or compact. Can inject context Claude will see.

```json
{"matcher": "compact", "hooks": [{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/inject-context.sh"}]}
```

Exit 0 stdout is added to Claude's context for `SessionStart`.

### Stop
Fires when Claude finishes responding. Can prevent Claude from stopping to continue working.

⚠️ **Infinite loop trap**: if your Stop hook always signals "keep going", Claude loops forever. Check `stop_hook_active` in input:
```bash
input=$(cat)
if echo "$input" | python3 -c "import json,sys; d=json.load(sys.stdin); sys.exit(0 if d.get('stop_hook_active') else 1)" 2>/dev/null; then
    exit 0  # already running a stop hook, don't loop
fi
```

### Notification
Fires for: `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog`. Common use: desktop notifications.

### FileChanged
Fires when a watched file changes on disk. The matcher **both** builds the watch list (literal filenames split by `|`) **and** filters which handlers run. Example watching `.envrc`:
```json
{"matcher": ".envrc", "hooks": [{"type": "command", "command": "direnv export bash >> \"$CLAUDE_ENV_FILE\""}]}
```

### SubagentStop
Fires when a subagent finishes. Useful for aggregating subagent results.

### WorktreeCreate
Fires when a worktree is created. **Any non-zero exit fails worktree creation.** The hook must print the absolute path of the created worktree to stdout:
```bash
echo "/absolute/path/to/worktree"
```

---

## Hook handler types (quick reference)

| Type | Use when | Key fields |
|---|---|---|
| `command` | Shell script, full OS access | `command`, `async`, `shell`, `timeout` |
| `http` | Remote service, shared state | `url`, `headers`, `allowedEnvVars`, `timeout` |
| `prompt` | LLM evaluation | `prompt` (use `$ARGUMENTS`), `model`, `timeout` (30s default) |
| `agent` | Multi-step tool-using verification | `prompt` (use `$ARGUMENTS`), `model`, `timeout` (60s default) |

See `references/hook-handler-types.md` for full schemas and examples.

---

## Matcher syntax (quick reference)

| Value | Interpreted as |
|---|---|
| `*`, `""`, or omitted | Match all — fires on every occurrence |
| Letters/digits/`_`/`\|` only | Exact string or `\|`-separated list: `Bash`, `Edit\|Write` |
| Any other character | JavaScript regex: `^Notebook`, `mcp__memory__.*` |

**Common mistake**: `mcp__memory` (underscores only) is evaluated as an exact string. It never matches any real tool because real tools are `mcp__memory__create_entities` etc. Use `mcp__memory__.*` (has `.*`) for regex.

---

## Exit code contract

```
Exit 0  → success; parse stdout for JSON output
Exit 2  → blocking error; ignore stdout; use stderr as the error message
Exit 1  → NON-BLOCKING error; the action proceeds anyway; stderr shown in transcript
Timeout → treated as non-blocking error
```

Not every event can be blocked. See `references/hook-event-reference.md` for the per-event blocking table.

---

## Plugin hooks configuration

Hooks ship with a plugin in `hooks/hooks.json` at the plugin root. Example:

```json
{
  "description": "Format TypeScript files after edits",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{"type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format.sh"}]
      }
    ]
  }
}
```

Use `${CLAUDE_PLUGIN_ROOT}` for paths to scripts bundled with the plugin. Use `${CLAUDE_PLUGIN_DATA}` for state that should survive plugin updates.

---

## References

| File | Contents |
|---|---|
| `references/hook-event-reference.md` | All 24+ events with schemas, blocking behavior, matcher semantics |
| `references/hook-handler-types.md` | Command, http, prompt, agent — full schemas, examples, security |
| `references/hook-anti-patterns.md` | Exit code 1 trap, infinite Stop loops, shell profile pollution, partial updatedInput, and 10+ more |
| `references/hook-testing-patterns.md` | `/hooks` menu, debug log, `test_hook.sh` usage, stdin replay |

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
