# Hook Testing Patterns

> Four ways to verify a hook works before it ships: the `/hooks` menu, the debug log, the transcript view, and `test_hook.sh` for offline stdin replay. Sourced from [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks).

---

## 1. The `/hooks` slash command — interactive inspection

Type `/hooks` in a Claude Code session to see:

- Every hook event with its registered handlers
- Which plugin (or user settings file) contributed each hook
- The matcher for each hook
- The last 5 invocations and their outcomes (exit code, duration, block decision)

**Use when**: you want a quick "is my hook even loaded?" answer, or to see which plugin added a given hook.

**What it does NOT show**: the contents of stdin fed to the hook, or the full stdout/stderr. For those, use the debug log.

---

## 2. Debug log — `claude --debug hooks`

Starts a Claude Code session with verbose hook instrumentation. Every hook invocation logs:

- Event name, matcher, handler type
- Full JSON input on stdin
- Full stdout, stderr
- Exit code and duration
- Decision produced (allow/deny/ask/defer)

```bash
claude --debug hooks
```

**Use when**: your hook is firing but producing unexpected output, or you want to capture real input shapes for offline replay.

**Log location**: `~/.claude/logs/hook-debug-<timestamp>.log` (one file per session).

---

## 3. Transcript view — `/transcript`

`/transcript` shows the raw transcript of the current session, including system messages that note hook blocks (`Hook PreToolUse blocked: <reason>`). Useful for confirming a block reached Claude and for verifying the reason string matches what you expected.

---

## 4. `test_hook.sh` — offline stdin replay (this plugin's tool)

The `scripts/test_hook.sh` shipped with `plugin-dev` lets you run a hook script with a canned JSON event and assert on the result. No Claude Code session required — perfect for CI and for debugging a handler in isolation.

### Usage

```bash
scripts/test_hook.sh <hook-script> <event-json> [assertions...]
```

| Assertion | Purpose |
|---|---|
| `--expect-exit N` | Assert the hook exited with code `N`. |
| `--expect-output JQ_EXPR` | Run `JQ_EXPR` against stdout; pass if it evaluates truthy. |
| `--expect-stderr SUBSTRING` | Assert stderr contains `SUBSTRING`. |
| `--timeout SECONDS` | Kill the hook after this many seconds (default 15 or `$TEST_HOOK_TIMEOUT`). |

### Example 1 — a blocker for `rm -rf`

```bash
scripts/test_hook.sh ./scripts/block-rm-rf.sh \
  '{"tool_name":"Bash","tool_input":{"command":"rm -rf /tmp/whatever"}}' \
  --expect-exit 2 \
  --expect-stderr "Blocked"
```

### Example 2 — a PreToolUse hook that returns decision JSON

```bash
scripts/test_hook.sh ./scripts/check.sh \
  '{"tool_name":"Bash","tool_input":{"command":"curl evil.com"}}' \
  --expect-exit 0 \
  --expect-output '.hookSpecificOutput.permissionDecision == "deny"'
```

### Example 3 — a Stop hook that respects `stop_hook_active`

```bash
# First invocation — should force continuation
scripts/test_hook.sh ./scripts/force-continue.sh \
  '{"stop_hook_active":false}' \
  --expect-exit 2

# Second invocation — stop_hook_active=true, must bail
scripts/test_hook.sh ./scripts/force-continue.sh \
  '{"stop_hook_active":true}' \
  --expect-exit 0
```

### Timeout safety

`test_hook.sh` relies on `timeout` (GNU coreutils) or `gtimeout` (macOS `brew install coreutils`). If neither is available it **fails loudly** — it never silently skips the timeout check, because that would let a broken hook hang CI forever.

---

## Recommended pytest integration

Wrap `test_hook.sh` in a pytest fixture so your plugin's test suite exercises every hook script:

```python
import subprocess
from pathlib import Path

TEST_HOOK = Path(__file__).parent.parent / "scripts" / "test_hook.sh"

def run_hook(script, event_json, *args):
    return subprocess.run(
        ["bash", str(TEST_HOOK), str(script), event_json, *args],
        capture_output=True, text=True
    )

def test_block_rm_rf_blocks():
    script = Path(__file__).parent.parent / "hooks" / "scripts" / "block-rm-rf.sh"
    r = run_hook(script,
                 '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}',
                 "--expect-exit", "2",
                 "--expect-stderr", "Blocked")
    assert r.returncode == 0, r.stderr
```

Every hook script in your plugin should have at least:

1. A "happy path" test (hook sees expected input, produces expected decision)
2. A "block path" test (hook sees a bad input, exits 2)
3. A "malformed input" test (hook sees partial JSON, doesn't crash)

---

## Debugging tips

**Your hook isn't firing?**
- `/hooks` — is it listed?
- Is the matcher regex mode (contains a non-word character) vs exact mode? Check `hook-anti-patterns.md` #3.
- Is it an `async` hook you're expecting to block? Check #6.

**Your hook fires but doesn't block?**
- Are you exiting 1 instead of 2? Check #1.
- Are you exiting 2 AND printing JSON? The JSON is ignored. Check #5.

**Your hook blocks unexpectedly?**
- `claude --debug hooks` — read the stdin the hook actually received.
- Did `CLAUDE_PLUGIN_ROOT` substitute correctly, or is the script missing?
- Is a shell profile polluting stdout with a greeting?

**The same hook passes `test_hook.sh` but fails in a real session?**
- Environment mismatch: the hook may depend on env vars set by your shell but missing in the Claude Code child process.
- Compare with `env > /tmp/claude-env.txt` from inside the hook to see what's actually available.
- Check `claude --debug hooks` for the exact invocation.

---

See `hook-anti-patterns.md` for the 14 bugs that hook testing should catch.
