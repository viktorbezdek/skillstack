# Hook Event Reference

> Authoritative catalog of every documented Claude Code hook event. Sourced from [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks). SKILL.md body covers the 10 most-used events inline; this reference covers all 24+ events with schemas, blocking behavior, and matcher semantics.

---

## Blocking quick table

| Event | Can block? | How to block | Matcher? |
|---|---|---|---|
| `PreToolUse` | Yes | exit 2 OR `permissionDecision: "deny"` | Tool name |
| `PostToolUse` | No | — | Tool name |
| `PermissionRequest` | Yes | `decision.behavior: "deny"` | Tool name |
| `PermissionDenied` | No | — | Tool name |
| `UserPromptSubmit` | Yes | exit 2 (rejects prompt) | None |
| `SessionStart` | No | — | Source (`startup`/`resume`/`clear`/`compact`) |
| `SessionEnd` | No | — | None |
| `Stop` | Yes | exit 2 (forces Claude to continue) | None |
| `StopFailure` | No | — | None |
| `Notification` | No | — | Notification type |
| `SubagentStart` | No | — | Agent name |
| `SubagentStop` | Yes | exit 2 (forces subagent to continue) | Agent name |
| `TaskCreated` | No | — | None |
| `TaskCompleted` | No | — | None |
| `TeammateIdle` | No | — | None |
| `ConfigChange` | No | — | Config key |
| `CwdChanged` | No | — | None |
| `FileChanged` | No | — | File path (watch list + filter) |
| `PreCompact` | No | — | None |
| `PostCompact` | No | — | None |
| `Elicitation` | Yes | exit 2 (rejects elicitation) | None |
| `ElicitationResult` | No | — | None |
| `WorktreeCreate` | **Yes (always)** | Any non-zero exit fails creation | None |
| `WorktreeRemove` | No | — | None |
| `InstructionsLoaded` | No | — | None |
| `PostToolUseFailure` | No | — | Tool name |

---

## PreToolUse

**Fires**: Before any tool executes (built-in tools, MCP tools, subagent tools).

**Can block**: Yes. Two mechanisms:
1. Exit 2 — stderr becomes the block reason shown to Claude.
2. JSON output on stdout with `hookSpecificOutput.permissionDecision: "deny"` and `permissionDecisionReason`.

**Matcher**: Tool name (`Bash`, `Edit`, `Edit|Write`, `mcp__memory__.*`). See SKILL.md for matcher syntax.

**Input schema**:
```json
{
  "session_id": "string",
  "transcript_path": "string",
  "cwd": "string",
  "hook_event_name": "PreToolUse",
  "tool_name": "string",
  "tool_input": { /* tool-specific */ },
  "tool_use_id": "string"
}
```

**Decision output (JSON on stdout, exit 0)**:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow" | "deny" | "ask" | "defer",
    "permissionDecisionReason": "string",
    "updatedInput": { /* OPTIONAL — replaces ENTIRE tool_input */ }
  }
}
```

**Precedence across multiple hooks**: `deny > defer > ask > allow`. A single deny stops the tool; otherwise the most restrictive non-allow decision wins.

**`updatedInput` trap**: returning `updatedInput` replaces the full tool input object, not individual fields. Any field you omit is lost. Always echo unchanged fields back verbatim.

---

## PostToolUse

**Fires**: After a tool call succeeds. Does NOT fire on tool failure (use `PostToolUseFailure`).

**Can block**: No. Exit 2 and deny decisions are ignored — the tool already ran.

**Common uses**: auto-format after `Edit`/`Write`, append to audit log, trigger a background build.

**Input schema**:
```json
{
  "session_id": "string",
  "hook_event_name": "PostToolUse",
  "tool_name": "string",
  "tool_input": { ... },
  "tool_response": { ... }
}
```

**Matcher**: tool name.

**Prefer `async: true`** for PostToolUse format/lint hooks — the action is already done, there is no reason to block Claude waiting on prettier.

---

## PermissionRequest

**Fires**: When Claude would show a permission dialog for a tool call (because permission mode is `default` and the tool isn't pre-approved).

**Can block / auto-approve**: Yes. The hook can short-circuit the dialog entirely.

**Input**: same shape as `PreToolUse`.

**Decision output**:
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow" | "deny" | "defer",
      "reason": "string",
      "updatedInput": { ... }
    }
  }
}
```

**Security note**: a PermissionRequest hook that blindly allows everything defeats the permission system. Always match narrowly (specific tool + specific argument shape).

---

## PermissionDenied

**Fires**: When a permission request was denied (by user, by PermissionRequest hook, or by permission mode).

**Can block**: No. Purely informational — use to log, notify, or reshape your session.

**Matcher**: tool name.

---

## UserPromptSubmit

**Fires**: Before Claude processes a user-submitted prompt. Does NOT fire for tool-injected or hook-injected context.

**Can block**: Yes. Exit 2 rejects the prompt with the stderr message. Stdout (exit 0) is added to the prompt as extra context Claude sees.

**Matcher**: None — fires on every prompt.

**Input**:
```json
{
  "session_id": "string",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "string"
}
```

**Common uses**: inject repo facts (current branch, failing tests, open PR number); strip or redact sensitive patterns; block prompts that violate policy.

---

## SessionStart

**Fires**: At session start AND on `resume`, `clear`, `compact`.

**Can block**: No. Stdout (exit 0) is injected into Claude's context.

**Matcher**: the source: `startup`, `resume`, `clear`, `compact`, or `*` for all.

**Input**:
```json
{
  "session_id": "string",
  "hook_event_name": "SessionStart",
  "source": "startup" | "resume" | "clear" | "compact"
}
```

**Common uses**: inject project context on startup, re-inject summarized state after compact, announce current worktree branch on resume.

---

## SessionEnd

**Fires**: When a session ends (user quits, process terminates cleanly).

**Can block**: No.

**Common uses**: archive transcript, post summary to a channel, clean up temp state.

---

## Stop

**Fires**: When Claude signals it is done responding for this turn.

**Can block**: Yes — exit 2 forces Claude to keep working. Stderr becomes the "why keep going" message.

**⚠️ Infinite loop trap**: if your Stop hook ALWAYS blocks, Claude loops forever. Check `stop_hook_active` in the input and bail out if it's true (you're already inside a triggered continuation).

**Input**:
```json
{
  "session_id": "string",
  "hook_event_name": "Stop",
  "stop_hook_active": true | false
}
```

See `hook-anti-patterns.md` for the full safe-loop pattern.

---

## StopFailure

**Fires**: When the session stops due to an error (crash, rate limit, unexpected termination).

**Can block**: No. Purely observational.

**Common uses**: desktop alert, incident channel post, write crash state for next session to read.

---

## Notification

**Fires**: On notification events:
- `permission_prompt` — a permission dialog is about to be shown
- `idle_prompt` — Claude has been idle for the configured interval
- `auth_success` — an authentication flow succeeded
- `elicitation_dialog` — an elicitation dialog is being shown

**Matcher**: the notification type (`permission_prompt`, `idle_prompt`, etc.).

**Common uses**: desktop notification, audio cue, Slack ping.

**Input**:
```json
{
  "session_id": "string",
  "hook_event_name": "Notification",
  "notification_type": "permission_prompt" | "idle_prompt" | "auth_success" | "elicitation_dialog",
  "message": "string"
}
```

---

## SubagentStart

**Fires**: When a subagent (Task tool, explore/plan agents) starts.

**Matcher**: agent name.

**Input includes**: `agent_name`, `prompt`, `tools_allowed`, `session_id`.

**Common uses**: inject extra context into specific subagents, log which agents were spawned when, enforce per-agent tool restrictions via a matching PreToolUse hook.

---

## SubagentStop

**Fires**: When a subagent finishes.

**Can block**: Yes — exit 2 forces the subagent to continue (same trap as Stop; check `stop_hook_active`).

**Matcher**: agent name.

**Common uses**: aggregate subagent findings into a summary file, enforce "must produce X output" contracts.

---

## TaskCreated

**Fires**: When a new task is created in the session task list.

**Input**: `task_id`, `subject`, `description`, `status`.

**Common uses**: sync Claude's task list to an external tracker.

---

## TaskCompleted

**Fires**: When a task is marked complete.

**Common uses**: tick the external tracker, log duration, announce in chat.

---

## TeammateIdle

**Fires**: When a spawned teammate agent is idle and awaiting input.

**Common uses**: desktop notification that a review agent is waiting.

---

## ConfigChange

**Fires**: When a settings key changes (model, permission mode, environment overrides).

**Matcher**: the config key that changed (supports regex).

**Input includes**: `key`, `old_value`, `new_value`.

**Common uses**: audit who changed what, re-run setup when the model or cwd changes.

---

## CwdChanged

**Fires**: When the working directory changes mid-session.

**Common uses**: re-source direnv / `.envrc`, refresh project context, invalidate caches keyed on cwd.

---

## FileChanged

**Fires**: When a watched file changes on disk.

**The matcher is dual-purpose**:
1. It **builds the watch list** — literal filenames (split by `|`) are registered as files to watch.
2. It **filters** — only hooks whose matcher matches the changed file run.

**You cannot watch arbitrary files without listing them in a matcher.** Regex matchers (containing non-word characters) still require an explicit watch list elsewhere — consult `code.claude.com/docs/en/hooks` for the current regex-vs-literal semantics.

**Example — watch `.envrc` and reload direnv**:
```json
{
  "matcher": ".envrc",
  "hooks": [
    {"type": "command", "command": "direnv export bash >> \"$CLAUDE_ENV_FILE\""}
  ]
}
```

---

## PreCompact

**Fires**: Before Claude compacts the transcript.

**Common uses**: dump important state to disk so SessionStart(compact) can re-inject it.

---

## PostCompact

**Fires**: After compaction finishes.

**Common uses**: log the compaction ratio, record summary length.

---

## Elicitation

**Fires**: When Claude is about to present an elicitation dialog to the user.

**Can block**: Yes — exit 2 cancels the elicitation.

**Common uses**: pre-fill answers from config, skip dialogs in automated runs.

---

## ElicitationResult

**Fires**: After the user answers an elicitation dialog.

**Input includes**: `question`, `answer`.

**Common uses**: log the answer, sync to a decision log.

---

## WorktreeCreate

**Fires**: When a worktree is created (via `/worktree`, `pilot worktree create`, or IDE).

**⚠️ Unique blocking semantics**: ANY non-zero exit fails worktree creation. There is no `permissionDecision` JSON. The hook MUST print the absolute path of the created worktree to stdout so Claude knows where it is:

```bash
#!/bin/bash
set -euo pipefail
path="/some/computed/absolute/path"
git worktree add "$path" HEAD
echo "$path"  # REQUIRED — this is what Claude sees as the new cwd
```

**Use case**: custom worktree provisioning — e.g., create worktrees on a shared NFS path, pre-seed with `.env` files, or route them through a sandboxing tool.

---

## WorktreeRemove

**Fires**: When a worktree is removed.

**Common uses**: archive artifacts from the worktree before it's gone, unregister from an external tracker.

---

## InstructionsLoaded

**Fires**: When CLAUDE.md / AGENTS.md / GEMINI.md instructions are loaded or reloaded.

**Input includes**: which files were loaded, how many lines each contributed.

**Common uses**: verify that expected instructions made it in, warn if a CLAUDE.md is missing.

---

## PostToolUseFailure

**Fires**: After a tool call fails. Counterpart to `PostToolUse`.

**Matcher**: tool name.

**Input includes**: `tool_name`, `tool_input`, `error_message`, `error_type`.

**Common uses**: auto-retry transient failures, log flaky external calls, notify on repeated failures.

---

## Choosing the right event

| Goal | Best event |
|---|---|
| Block a dangerous shell command before it runs | `PreToolUse` (matcher `Bash`) |
| Auto-format after file edits | `PostToolUse` (matcher `Edit\|Write`, `async: true`) |
| Inject context at session start | `SessionStart` |
| Re-hydrate context after auto-compact | `SessionStart` (matcher `compact`) |
| Audit every permission dialog | `PermissionRequest` |
| Desktop alert when a permission prompt appears | `Notification` (matcher `permission_prompt`) |
| Reload `.envrc` automatically | `FileChanged` (matcher `.envrc`) + `CwdChanged` |
| Force Claude to keep working until tests pass | `Stop` + `stop_hook_active` guard |
| Aggregate subagent results | `SubagentStop` |
| Provision a custom worktree | `WorktreeCreate` |
| Strip secrets from user prompts | `UserPromptSubmit` |
| Notify when Claude crashed overnight | `StopFailure` |

---

See `hook-handler-types.md` for the four handler shapes (command/http/prompt/agent) and `hook-anti-patterns.md` for the traps that catch most first-time hook authors.
