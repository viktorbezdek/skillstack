---
name: hindsight-memory
description: >-
  Interact with and integrate Hindsight long-term AI memory in Claude Code via
  the `hindsight` CLI. Use for recalling past context, reflecting over a memory
  bank, retaining facts/decisions, managing banks/entities/mental-models, and
  understanding the auto-recall/auto-retain hooks this plugin installs. Trigger
  phrases: "what do I remember about", "recall from my memory", "reflect on my
  past work", "retain this", "save to my memory bank", "hindsight memory",
  "check my long-term memory", "is memory working". NOT for short-term session
  context (Claude already has the transcript), NOT for code/structural search
  (use CodeGraph/Semble/grep), NOT for building a memory framework from scratch
  (use the memory-systems skill).
allowed-tools: Bash, Read
---

# Hindsight Memory

Hindsight is a semantic long-term memory system. This plugin wires Claude Code
to a Hindsight server (external API) so that **relevant memories are recalled
before every prompt** and **the conversation is retained after every turn** —
and gives you a vocabulary for driving that memory by hand when you want to.

The transport is the installed `hindsight` CLI (verify with `hindsight version`).
It already knows the API endpoint from `HINDSIGHT_API_URL` / `HINDSIGHT_API_KEY`
or a named profile, so every command below "just works" against your server.

## How the automatic memory works

Three hooks (in `hooks/hooks.json`) run with no action from you:

| Hook | Event | Script | What it does |
|------|-------|--------|--------------|
| Recall | `UserPromptSubmit` | `scripts/recall.py` | Queries the bank for memories relevant to your prompt and injects them as an invisible `<hindsight_memories>` block — Claude sees them, the chat does not. |
| Retain | `Stop` (async) | `scripts/retain.py` | Reads the transcript, **strips any injected `<hindsight_memories>` block**, and stores it under a deterministic per-session document id. |
| Health | `SessionStart` | `scripts/session_start.py` | Silent reachability check; logs only with debug on. |

Every hook **fails open**: if the server is slow or unreachable, the turn is
never blocked and no error reaches you. The recall budget defaults to `mid` and
the query is capped, so latency stays bounded.

The single most important invariant: **retain strips the recalled-memory block
before storing.** Without it the bank would ingest its own prior recalls as new
memories — a compounding feedback loop. See `references/memory-model.md`.

## Manual interaction (the common moves)

Default bank is `claude_code` (override with `HINDSIGHT_CC_BANK_ID`).

```bash
# Recall — semantic search over memories (what the prompt hook calls)
hindsight memory recall claude_code "decisions about the retain doc-id" --budget mid

# Reflect — a synthesized ANSWER in the bank's voice, not just a list of hits
hindsight memory reflect claude_code "what have I decided about plugin versioning?"

# Retain — store a single fact/decision deliberately
hindsight memory retain claude_code "Chose lean CLI-backed port over full Python port for the skillstack hindsight plugin" -c claude-code

# List / inspect
hindsight bank stats claude_code
hindsight memory list claude_code
hindsight entity list claude_code
```

`recall` returns ranked hits (`text`, `type`, `mentioned_at`); `reflect` reasons
over them and answers. Use `reflect` when you want a conclusion, `recall` when
you want the raw evidence. Full command surface: `references/cli-reference.md`.

## When to reach for this skill

✅ **Use for:**
- "What do I remember / what did I decide about X" → `recall` or `reflect`
- Deliberately saving a durable fact or decision → `retain`
- Checking memory is healthy or seeing what a bank holds → `health`, `bank stats`
- Curating memory: entities, mental-models, directives, missions
- Explaining or tuning the auto-recall / auto-retain hooks

❌ **NOT for:**
- Recalling something said earlier **this** session — it's already in context
- Finding code, symbols, or callers → use CodeGraph / Semble / grep
- Designing a memory architecture or comparing frameworks → use `memory-systems`
- Generic web/doc lookup → use the research/docs skills

## Configuration (environment variables)

All knobs are namespaced `HINDSIGHT_CC_*` so they never clash with the CLI's own
`HINDSIGHT_*` variables. Defaults are production-sane; change nothing to start.

| Var | Default | Purpose |
|-----|---------|---------|
| `HINDSIGHT_CC_BANK_ID` | `claude_code` | Bank to recall from / retain to |
| `HINDSIGHT_CC_AUTO_RECALL` | `true` | Master switch for the recall hook |
| `HINDSIGHT_CC_AUTO_RETAIN` | `true` | Master switch for the retain hook |
| `HINDSIGHT_CC_RECALL_BUDGET` | `mid` | `low` / `mid` / `high` — latency vs thoroughness |
| `HINDSIGHT_CC_RECALL_MAX_TOKENS` | `1024` | Cap on the injected memory block |
| `HINDSIGHT_CC_RECALL_TYPES` | `world,experience` | Fact types to recall |
| `HINDSIGHT_CC_RETAIN_TOOL_CALLS` | `true` | Include tool calls in retained transcript |
| `HINDSIGHT_CC_PROFILE` | _(none)_ | Named CLI profile to pass as `-p` |
| `HINDSIGHT_CC_CLI_BIN` | _(PATH)_ | Explicit path to the `hindsight` binary |
| `HINDSIGHT_CC_DEBUG` | `false` | Log `[Hindsight]` lines to stderr |

The plugin assumes an **external Hindsight API** (the CLI's configured endpoint).
It does not start a local daemon or manage an LLM provider — the server handles
fact extraction.

## Anti-pattern: retaining the recalled-memory block

**Symptom:** the bank fills with near-duplicate memories that echo earlier
recalls; recall quality degrades over sessions as the same facts pile up.

**Problem:** the recall hook injects a `<hindsight_memories>` block into the
prompt. If a retain step stores the raw transcript, that block is ingested as
brand-new content. Next session it is recalled and re-injected, then re-stored —
a feedback loop that poisons the bank with its own output.

**Solution:** always strip `<hindsight_memories>` / `<relevant_memories>` blocks
before retaining (this plugin does it in `scripts/lib/transcript.py:strip_memory_tags`,
exercised by `tests/test_transcript.py`). If you write your own retain path,
strip first — it is non-negotiable, not an optimization.

## Anti-pattern: blocking the turn on a slow server

**Symptom:** prompts hang for seconds; sessions stall when the network is poor.

**Problem:** a recall hook that raises or waits indefinitely makes Hindsight a
hard dependency of every keystroke.

**Solution:** the recall hook is fail-open with a tight timeout and a bounded
budget — any error or timeout yields zero injected context and exit 0. Keep it
that way; never make memory a blocking dependency of the prompt.

## References

- `references/cli-reference.md` — full `hindsight` command surface used here
- `references/memory-model.md` — banks, fact types, entities, observations, mental models, directives
