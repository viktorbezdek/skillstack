# Hook Anti-Patterns

> The 14 mistakes that account for ~95% of hook bugs. The exit-code-1 trap is #1; everything else is downstream. Read this before writing any new hook. Sourced from [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) and hard-won experience.

---

## 1. Exit code 1 does not block

**The #1 hook bug.** Exit 1 is a non-blocking error. The tool call, prompt, or stop **proceeds anyway** — stderr is shown in the transcript but nothing is stopped.

```bash
# ❌ Does NOT block
if is_dangerous "$cmd"; then
  echo "dangerous" >&2
  exit 1   # Claude runs it anyway
fi

# ✅ Blocks
if is_dangerous "$cmd"; then
  echo "dangerous" >&2
  exit 2   # Claude sees stderr and refuses
fi
```

**How to remember**: `0` = success, `2` = block, **everything else** = non-blocking error. There is no "exit 1 = soft fail" — it just means "the hook itself had a bug, proceed".

---

## 2. Infinite Stop-hook loop

A `Stop` hook that always forces Claude to continue locks the session forever. The input contains `stop_hook_active: true` when you're already inside a continuation — check it and bail.

```bash
# ❌ Infinite loop — always forces continuation
input=$(cat)
echo "keep going" >&2
exit 2

# ✅ Safe — bails on second invocation
input=$(cat)
if echo "$input" | python3 -c "
import json, sys
d = json.load(sys.stdin)
sys.exit(0 if d.get('stop_hook_active') else 1)
" 2>/dev/null; then
  exit 0   # Already running a stop loop — let it finish
fi
echo "tests still failing, keep going" >&2
exit 2
```

The same pattern applies to `SubagentStop`.

---

## 3. Matcher interpreted as exact string when you meant regex

The matcher has three interpretation modes (see SKILL.md). The rule: if your string contains ONLY letters, digits, `_`, `|`, it's an **exact match**. Any other character (including `.`, `*`, `^`, `\`) flips it to regex mode.

```json
// ❌ "mcp__memory" is letters+underscores only → exact match
// It never matches any real tool because real tools are "mcp__memory__create_entities" etc.
{"matcher": "mcp__memory"}

// ✅ Regex mode (contains ".")
{"matcher": "mcp__memory__.*"}
```

**Rule of thumb**: if you think you're writing a regex, include at least one regex character. Test with `/hooks` or `test_hook.sh` before relying on it.

---

## 4. `updatedInput` replaces the entire tool_input

When a PreToolUse hook returns `updatedInput` in `hookSpecificOutput`, it **replaces every field** of `tool_input`. Any field you omit is gone.

```python
# ❌ Drops every field except `command`
print(json.dumps({
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "updatedInput": {"command": sanitized_command}
  }
}))

# ✅ Echo unchanged fields back
updated = dict(event["tool_input"])
updated["command"] = sanitized_command
print(json.dumps({
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "updatedInput": updated
  }
}))
```

---

## 5. Mixing exit code 2 and JSON output

If you exit with code 2, the runtime **uses stderr as the block reason** and ignores stdout. If you print JSON on stdout AND exit 2, the JSON is thrown away.

```bash
# ❌ JSON is ignored
echo '{"hookSpecificOutput": {"permissionDecision": "deny", "permissionDecisionReason": "..."}}'
exit 2

# ✅ Use JSON + exit 0
echo '{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Blocked"}}'
exit 0

# ✅ Or use exit 2 + stderr
echo "Blocked" >&2
exit 2
```

Pick one lane per hook.

---

## 6. Async hooks expected to block

`async: true` means the hook runs fire-and-forget. It starts, Claude moves on, exit code and stdout are ignored.

```json
// ❌ Async blocker — can never block, only looks like it does
{"type": "command", "async": true, "command": "check-policy.sh"}

// ✅ Sync for guardrails
{"type": "command", "command": "check-policy.sh"}
// ✅ Async for fire-and-forget
{"type": "command", "async": true, "command": "post-to-slack.sh"}
```

**Never use `async: true` for PreToolUse, PermissionRequest, UserPromptSubmit, Stop, SubagentStop, Elicitation, or WorktreeCreate.** If your hook needs to block, it must be synchronous.

---

## 7. Over-broad matcher

`*` or omitted matcher fires on every tool call. A slow hook on `*` adds its latency to every single operation.

```json
// ❌ Runs for every Read, Edit, Grep, ... in a long session
{"matcher": "*", "hooks": [{"type": "command", "command": "heavy-check.sh"}]}

// ✅ Only where it's needed
{"matcher": "Bash", "hooks": [{"type": "command", "command": "heavy-check.sh"}]}
```

**Budget rule**: a matcher that fires >100×/session must complete in <50ms or it is a UX problem. Measure it.

---

## 8. Shell profile pollution

Hooks inherit your login shell's environment. A `.bashrc` that prints to stdout, sources slow plugins, or changes directory will break your hooks in surprising ways.

```bash
# .bashrc contains:
echo "Welcome, $USER!"   # ❌ This is now in your hook's stdout — corrupts JSON output

# Fix #1: guard login-only output
if [[ $- == *i* ]]; then
  echo "Welcome, $USER!"
fi

# Fix #2: explicit non-interactive shell in the hook
{"type": "command", "shell": "bash", "command": "bash --noprofile --norc -c 'my-hook.sh'"}
```

---

## 9. Interpolating untrusted input into shell strings

Tool input fields are **untrusted** — they contain whatever Claude decided to send, including quotes, backticks, and `$()`. Never splice them directly into a shell command.

```bash
# ❌ Command injection
cmd=$(echo "$input" | jq -r '.tool_input.command')
eval "check-policy $cmd"   # $cmd can contain `; rm -rf /`

# ✅ Parse into a variable, quote it, never eval
cmd=$(echo "$input" | jq -r '.tool_input.command')
if [[ "$cmd" == *"rm -rf"* ]]; then
  echo "blocked" >&2
  exit 2
fi
```

---

## 10. Assuming `$CLAUDE_PLUGIN_ROOT` is set in user settings hooks

`${CLAUDE_PLUGIN_ROOT}` is only substituted for hooks defined in **plugin** `hooks/hooks.json`. If a user drops your example hook into `~/.claude/settings.json`, `${CLAUDE_PLUGIN_ROOT}` is unset and the hook fails silently.

```json
// Plugin hook — this works
{"command": "${CLAUDE_PLUGIN_ROOT}/scripts/check.sh"}

// User settings hook — this does NOT
// Must use an absolute path
{"command": "/Users/alice/.claude/scripts/check.sh"}
```

Document this distinction when shipping example hooks.

---

## 11. Ignoring timeouts as errors

A hook timeout is treated as a **non-blocking** error. Your guardrail hook that takes too long lets the action through.

```bash
# ❌ 60s default timeout, network call that sometimes hangs → tool runs unchecked
curl https://policy.example.com/check

# ✅ Set a tight timeout AND handle it
timeout 5 curl -s https://policy.example.com/check || {
  echo "policy server unreachable — failing closed" >&2
  exit 2   # Explicit block if the check fails
}
```

For security hooks, **fail closed** on timeout (exit 2), not open.

---

## 12. FileChanged matcher that doesn't actually watch

The `FileChanged` matcher both builds the watch list and filters which handlers run. If your matcher is a regex (contains non-word characters), you may not be watching any file at all — regex matchers do not implicitly register watches.

```json
// ❌ Regex-only matcher — may never fire
{"matcher": ".*\\.env.*", "hooks": [...]}

// ✅ Literal filenames (split by `|`) register the watches
{"matcher": ".envrc|.env.local", "hooks": [...]}
```

When in doubt, list the literal files you want to watch.

---

## 13. Writing state to `CLAUDE_PLUGIN_ROOT` instead of `CLAUDE_PLUGIN_DATA`

`CLAUDE_PLUGIN_ROOT` is the **install** directory — it's wiped and replaced on plugin update. State written there is lost on upgrade.

```bash
# ❌ Blown away on plugin update
echo "$count" > "$CLAUDE_PLUGIN_ROOT/counter.txt"

# ✅ Persists across updates
mkdir -p "$CLAUDE_PLUGIN_DATA"
echo "$count" > "$CLAUDE_PLUGIN_DATA/counter.txt"
```

---

## 14. Plugin-shipped `agent` hooks assuming full tool access

Agent-type hooks shipped from a plugin run with a **restricted toolset** — only tools in the hook's `tools:` allowlist (if specified) or a default subagent toolset. They cannot spawn arbitrary tools.

```json
// ❌ Assumes full tool access — Write and Edit may be unavailable
{"type": "agent", "prompt": "Read the file, Write a summary"}

// ✅ Explicit allowlist
{"type": "agent", "tools": ["Read", "Grep", "Bash"], "prompt": "..."}
```

Design your agent hooks around a small, explicit tool list.

---

## Bonus: cargo-culting from old docs

The hooks system is evolving. Copying a `hooks.json` snippet from an old blog post or GitHub issue often gives you an obsolete schema — key names change, new fields appear, event names get added. **Always cross-check against [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) before shipping.**

---

## Quick audit checklist

Before shipping a hook:

- [ ] Does it exit 2 (not 1) to block?
- [ ] If it's a Stop/SubagentStop hook, does it check `stop_hook_active`?
- [ ] If the matcher looks like a regex, does it contain at least one regex character?
- [ ] If it returns `updatedInput`, does it echo ALL unchanged fields back?
- [ ] Is it sync (not `async: true`) if it needs to block?
- [ ] Is the matcher narrow enough to avoid firing on every tool?
- [ ] Does it parse JSON from stdin instead of eval'ing fields?
- [ ] Does it use `${CLAUDE_PLUGIN_ROOT}` for scripts and `${CLAUDE_PLUGIN_DATA}` for state?
- [ ] Does it fail closed on timeout for security-critical checks?
- [ ] Has it been tested with `test_hook.sh` or the `/hooks` menu?
