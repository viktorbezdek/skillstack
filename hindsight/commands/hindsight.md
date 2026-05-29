---
description: Interact with your Hindsight long-term memory — recall, reflect, retain, or inspect a bank.
argument-hint: "[recall|reflect|retain|stats] <text>"
allowed-tools: Bash, Read
---

# /hindsight — drive your Hindsight memory

Run the right `hindsight` CLI command for the user's intent. The bank defaults to
`claude_code` (or `$HINDSIGHT_CC_BANK_ID` if set). The CLI already knows the API
endpoint, so no configuration is needed.

Arguments: `$ARGUMENTS`

Dispatch on the first word:

- **`recall <query>`** → `hindsight memory recall "$BANK" "<query>" --budget mid -o json`
  then summarize the ranked hits for the user.
- **`reflect <question>`** → `hindsight memory reflect "$BANK" "<question>"` and
  present the synthesized answer.
- **`retain <fact>`** → `hindsight memory retain "$BANK" "<fact>" -c claude-code`
  to deliberately store a durable fact or decision.
- **`stats`** (or no/unknown verb) → `hindsight bank stats "$BANK"` and, if the
  user asked a question, fall back to `reflect`.

Resolve the bank first:

```bash
BANK="${HINDSIGHT_CC_BANK_ID:-claude_code}"
```

Guidelines:
- Prefer `reflect` when the user wants a conclusion; `recall` when they want the
  raw evidence (hits with `text`, `type`, `mentioned_at`).
- Never run destructive commands (`memory clear`, `memory delete`, `bank delete`)
  from this command — those require an explicit, separate, confirmed request.
- If `hindsight` is not on PATH, tell the user the CLI is required and stop.

For the full command surface and the memory model, the `hindsight-memory` skill's
references (`cli-reference.md`, `memory-model.md`) are authoritative.
