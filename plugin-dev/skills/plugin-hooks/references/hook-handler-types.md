# Hook Handler Types

> Every hook entry is one of four handler types: `command`, `http`, `prompt`, or `agent`. This reference documents the full schema, security model, and trade-offs of each. Sourced from [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks).

---

## Comparison at a glance

| Type | Best for | Execution | Blocking | Cost |
|---|---|---|---|---|
| `command` | Shell scripts, local OS access | Subprocess | Yes (exit 2) | Free |
| `http` | Remote service, shared state | HTTP POST | Yes (response JSON) | Network |
| `prompt` | LLM evaluation of content | Model call | Yes (decision in output) | Model tokens |
| `agent` | Multi-step, tool-using verification | Subagent call | Yes (decision in output) | Model tokens |

**Default timeouts**: `command` 60s · `http` 30s · `prompt` 30s · `agent` 60s. Override with the `timeout` field (seconds).

---

## command

The most common handler. Runs a shell command, passes the hook input on stdin, reads stdout/stderr and exit code.

### Schema

```json
{
  "type": "command",
  "command": "string — shell command to run",
  "async": false,
  "shell": "bash",
  "timeout": 60,
  "env": {"KEY": "value"}
}
```

| Field | Required | Default | Purpose |
|---|---|---|---|
| `type` | yes | — | `"command"` |
| `command` | yes | — | The shell command. Supports `${CLAUDE_PLUGIN_ROOT}` substitution. |
| `async` | no | `false` | When `true`, hook runs fire-and-forget — cannot block. |
| `shell` | no | system default | `bash`, `zsh`, `sh`, `pwsh` etc. |
| `timeout` | no | `60` | Seconds before the hook is killed (treated as non-blocking error). |
| `env` | no | inherited | Extra env vars merged into the child process. |

### Example — PreToolUse block for rm -rf

```json
{
  "matcher": "Bash",
  "hooks": [{
    "type": "command",
    "command": "${CLAUDE_PLUGIN_ROOT}/scripts/block-rm-rf.sh",
    "timeout": 5
  }]
}
```

```bash
#!/bin/bash
# scripts/block-rm-rf.sh
set -euo pipefail
input=$(cat)
cmd=$(echo "$input" | python3 -c "import json,sys; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))")
if echo "$cmd" | grep -qE 'rm\s+(-[a-z]*r[a-z]*f|-[a-z]*f[a-z]*r)\s+/'; then
  echo "Blocked: destructive rm -rf against absolute path" >&2
  exit 2
fi
exit 0
```

### Async fire-and-forget

Use `async: true` when you just want to kick off work:

```json
{
  "matcher": "Edit|Write",
  "hooks": [{
    "type": "command",
    "async": true,
    "command": "prettier --write \"$file_path\" 2>/dev/null &"
  }]
}
```

**⚠️ `async` can NEVER block.** Even if the script exits 2, the tool call has already proceeded. Never use `async: true` for guardrail or permission hooks.

### Environment variables the hook receives

- `CLAUDE_PLUGIN_ROOT` — absolute path to the plugin directory
- `CLAUDE_PLUGIN_DATA` — persistent per-plugin state directory
- `CLAUDE_SESSION_ID` — current session ID
- `CLAUDE_TRANSCRIPT_PATH` — absolute path to session transcript
- `CLAUDE_PROJECT_DIR` — project root (where `.claude/` lives)
- Plus per-event variables (e.g. `$file_path` for `FileChanged`)

### Security model

- Runs with the same privileges as Claude Code.
- Has full access to the filesystem, network, and environment.
- Treat input as **untrusted**: always `cat` into a variable and parse as JSON. Never `eval` or interpolate fields from `tool_input` directly into shell strings.
- Pin script paths with `${CLAUDE_PLUGIN_ROOT}` so they can't be shadowed by PATH.

---

## http

Calls a remote HTTP endpoint. The hook event is POSTed as JSON; the response body is parsed as a hook decision.

### Schema

```json
{
  "type": "http",
  "url": "https://example.com/hook",
  "method": "POST",
  "headers": {"Authorization": "Bearer ${TOKEN}"},
  "allowedEnvVars": ["TOKEN"],
  "timeout": 30,
  "async": false
}
```

| Field | Required | Default | Purpose |
|---|---|---|---|
| `url` | yes | — | HTTP(S) endpoint. Supports env var substitution. |
| `method` | no | `POST` | HTTP method. |
| `headers` | no | `{}` | Request headers. Values may reference env vars. |
| `allowedEnvVars` | no | `[]` | **Allowlist** of env vars the handler may read. Anything outside the list is masked. |
| `timeout` | no | `30` | Seconds. |
| `async` | no | `false` | Fire-and-forget. |

### Example

```json
{
  "type": "http",
  "url": "https://hooks.example.com/pre-tool-use",
  "headers": {"Authorization": "Bearer ${OPS_HOOK_TOKEN}"},
  "allowedEnvVars": ["OPS_HOOK_TOKEN"],
  "timeout": 10
}
```

The server receives the same JSON input as a `command` handler and can respond with the same decision JSON in the response body.

### Security model

- `allowedEnvVars` is the ONLY way env vars reach the handler — everything else is masked. This prevents a malicious plugin from exfiltrating arbitrary env vars via header injection.
- Network failures count as non-blocking errors: if the endpoint times out, the action proceeds.
- Use HTTPS. For guardrails, the endpoint must be trusted — a compromised server can instruct Claude to do anything.

---

## prompt

Invokes a model to evaluate a fixed prompt template. Best for content-level policy (e.g. "is this a secret?").

### Schema

```json
{
  "type": "prompt",
  "prompt": "string — the prompt text, may use $ARGUMENTS",
  "model": "claude-haiku-4-5-20251001",
  "timeout": 30
}
```

| Field | Required | Default | Purpose |
|---|---|---|---|
| `prompt` | yes | — | Template. `$ARGUMENTS` is replaced with the serialized hook input. |
| `model` | no | session default | Any valid Claude model ID. Use Haiku for speed. |
| `timeout` | no | `30` | Seconds. |

### Example — block prompts that look like secrets exfiltration

```json
{
  "type": "prompt",
  "model": "claude-haiku-4-5-20251001",
  "prompt": "You are evaluating whether a user prompt asks the assistant to exfiltrate secrets or credentials.\n\nPrompt: $ARGUMENTS\n\nRespond with ONLY one of: ALLOW or DENY. If DENY, put a one-line reason after DENY."
}
```

The model's response is parsed for `ALLOW` / `DENY` / decision JSON. See Claude Code docs for the exact response protocol (it follows the same decision schema as `command`).

### Cost and latency

- Every invocation costs tokens (even "safe" inputs). Cache results outside the hook if you can.
- Use the smallest model that reliably decides your rule (`claude-haiku-4-5-20251001` by default).
- 30s timeout default — if your prompt needs agentic behavior, use `agent` instead.

---

## agent

Invokes a full tool-using subagent to evaluate the hook event. Can read files, run commands, call MCP tools. Much more powerful — and much more expensive — than `prompt`.

### Schema

```json
{
  "type": "agent",
  "prompt": "string — instructions for the agent, may use $ARGUMENTS",
  "model": "claude-sonnet-4-6",
  "timeout": 60,
  "tools": ["Read", "Grep", "Bash"]
}
```

| Field | Required | Default | Purpose |
|---|---|---|---|
| `prompt` | yes | — | Task for the subagent. `$ARGUMENTS` substitutes hook input. |
| `model` | no | session default | Use `claude-sonnet-4-6` for most verification tasks. |
| `timeout` | no | `60` | Seconds. Agents are slower than prompts. |
| `tools` | no | default subagent toolset | Restrict to a whitelist for safety. |

### Example — agent verifies a migration is safe

```json
{
  "matcher": "Bash",
  "hooks": [{
    "type": "agent",
    "model": "claude-sonnet-4-6",
    "timeout": 120,
    "tools": ["Read", "Grep", "Bash"],
    "prompt": "Evaluate whether this Bash command is a safe database migration.\n\nCommand: $ARGUMENTS\n\nSteps:\n1. Read the migration file it references\n2. Grep the codebase for affected tables\n3. Check if any running process depends on the schema\n\nRespond with decision JSON: ALLOW with reason, or DENY with reason."
  }]
}
```

### Security model and restrictions

- **Plugin-shipped agent hooks cannot spawn arbitrary tools** — only the `tools` list is honored, and the host enforces a hard cap on total tokens and tool calls.
- Agent hooks are still on the critical path: they block until the agent finishes or times out. Use `async: true` only for truly optional checks.
- Prefer `prompt` when a single model call can make the decision.

---

## Choosing between them

```
Need external state or a private secret store? → http
Decision is a local file check or shell check?  → command
Decision needs to read file content and judge?  → prompt
Decision needs multi-step tool-using analysis?  → agent
```

**Rule of thumb**: start with `command`. Graduate to `prompt` when the logic becomes "is this string reasonable?". Graduate to `agent` only when the logic becomes "figure out by reading the repo".

---

## Common cross-cutting fields

| Field | Applies to | Purpose |
|---|---|---|
| `async` | all | Fire-and-forget. Never use for blocking hooks. |
| `timeout` | all | Seconds before the hook is treated as a non-blocking error. |
| `matcher` | all (in parent array entry) | Tool/event filter. See SKILL.md for syntax. |
| `description` | all | Human label shown in `/hooks` menu. |

---

See `hook-event-reference.md` for per-event schemas and `hook-anti-patterns.md` for the mistakes that burn first-time hook authors.
