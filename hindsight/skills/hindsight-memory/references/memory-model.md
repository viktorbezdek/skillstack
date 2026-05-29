# Hindsight memory model

A mental model of what Hindsight stores, so recall/retain choices make sense.

## Banks

A **bank** is an isolated memory store — a separate "brain." Memories never leak
across banks. This plugin uses one bank by default (`claude_code`); set
`HINDSIGHT_CC_BANK_ID` to scope memory per-project, per-agent, or per-user.

A bank carries:
- a **mission** — a short identity/purpose statement used to contextualize recall;
- a **disposition** — trait dials (empathy, literalism, skepticism, 1–5) that
  shape how `reflect` reasons;
- **config** — hierarchical overrides for extraction/recall behavior.

## The retain → extract → recall pipeline

1. **Retain** stores a raw **document** (a conversation transcript or a single
   fact) under a document id.
2. The server **extracts** structured **memories** and **entities** from that
   document — asynchronously when you pass `--async` (the Stop hook does). So a
   freshly retained doc may not appear in `memory list` for a few seconds; it is
   still being processed.
3. **Recall** does semantic search over the extracted memories and returns the
   ranked hits; **reflect** reasons over them to produce an answer.

Because extraction is async, the retain hook's job is only to *submit* the
document and exit — it never waits for extraction.

## Fact types

Recalled/extracted memories are typed:

| Type | Meaning | Example |
|------|---------|---------|
| `world` | General, durable fact | "The skillstack validator enforces a version trio." |
| `experience` | Something that happened, time-anchored | "I bumped skillstack-workflows 2.2.0 → 2.2.1 on Apr 27." |
| `opinion` | A stance or preference | "Prefer lean CLI-backed ports over bundled Python." |

This plugin recalls `world,experience` by default (durable facts + past actions)
and skips `opinion` to keep injected context factual. Override with
`HINDSIGHT_CC_RECALL_TYPES`.

## Entities, observations, mental models, directives

- **Entities** — people, files, projects, systems mentioned across memories;
  each accumulates observations over time (`entity list` / `entity get`).
- **Observations** — derived statements consolidated from memories
  (`bank consolidate` builds them).
- **Mental models** — user-curated summaries you maintain deliberately.
- **Directives** — behavioral rules attached to a bank.

## Document ids and idempotency

A document id makes retain **idempotent**: re-retaining with the same id
*replaces* the document rather than creating a duplicate. This plugin derives a
stable base id per session — `cc-<sha256("claude-code:" + session_id)[:16]>` — so
repeated Stop-hook fires within a session keep updating one document instead of
spawning many.

The transcript is passed to the CLI as a command-line argument, and the OS caps
a single argument (Linux `MAX_ARG_STRLEN` ≈ 128 KB). A long session with tool
calls exceeds that, so the transcript is split into chunks that each serialize
within an argv-safe size; chunk 0 uses the base id and chunk *i* uses
`<base>-c<i>`. Every Stop re-sends all chunks (idempotent replacement), so no
content is silently dropped on long sessions. (Trade-off: if a transcript shrinks
after compaction, the shorter chunk set overwrites the longer one for that
session — accepted to stay state-file-free.)

## The feedback-loop hazard (why stripping matters)

The recall hook injects memories into the prompt inside a `<hindsight_memories>`
block. That block becomes part of the transcript. If retain stored the raw
transcript, the block — old recalls — would be ingested as *new* memories, then
recalled next session, then re-stored: a self-amplifying loop that floods the
bank with echoes of its own output.

The retain path therefore strips `<hindsight_memories>` and `<relevant_memories>`
blocks before storing (`scripts/lib/transcript.py:strip_memory_tags`). This is
the one invariant that must never regress; `tests/test_transcript.py` guards it.
