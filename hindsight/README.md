# hindsight

Long-term memory for Claude Code, backed by [Hindsight](https://vectorize.io/hindsight).

This plugin gives Claude Code persistent memory across sessions and a vocabulary
for driving that memory by hand. It is a **lean, CLI-backed integration**: the
installed `hindsight` CLI is the transport, so there is no bundled HTTP client,
no local daemon, and no LLM-provider configuration — your Hindsight **server**
does the fact extraction.

## What it does

| Component | Type | Behaviour |
|-----------|------|-----------|
| `recall.py` | `UserPromptSubmit` hook | Recalls memories relevant to your prompt and injects them as an invisible `<hindsight_memories>` block. |
| `retain.py` | `Stop` hook (async) | Strips injected memory blocks, then stores the transcript under a deterministic per-session document id. Long transcripts are split into argv-safe chunks (each retained as its own document) so nothing is lost. |
| `session_start.py` | `SessionStart` hook | Silent health check; never blocks the session. |
| `hindsight-memory` | skill | Knowledge for manual recall / reflect / retain and bank, entity, mental-model management. |
| `/hindsight` | command | One-shot `recall` / `reflect` / `retain` / `stats` against your bank. |

Every hook **fails open**: a slow or unreachable server never blocks a turn and
never surfaces an error.

## Prerequisites

1. The **`hindsight` CLI** installed and on `PATH` (`hindsight version`).
2. The CLI pointed at a reachable Hindsight server — set `HINDSIGHT_API_URL`
   (and `HINDSIGHT_API_KEY` if required), or configure a profile and pass it via
   `HINDSIGHT_CC_PROFILE`. Verify with `hindsight health`.

## Install

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install hindsight@skillstack
```

Start Claude Code — memory activates automatically. Confirm with
`HINDSIGHT_CC_DEBUG=1` and watch for `[Hindsight]` lines on stderr.

> ⚠️ **Do not run this alongside the official `hindsight-memory` plugin.** Both
> install recall/retain hooks, so running both fires recall twice per prompt
> (two `<hindsight_memories>` blocks) and retains the session twice (under
> different document-id schemes, so they accumulate rather than dedupe).
> Pick one: uninstall/disable `hindsight-memory` before using this, or vice
> versa.

## Manual use

```bash
# Ask what you remember
/hindsight reflect what did I decide about the retain doc-id?

# Or call the CLI directly (see the skill's references for the full surface)
hindsight memory recall  claude_code "plugin versioning decisions" --budget mid
hindsight memory reflect claude_code "what's my approach to skillstack ports?"
hindsight memory retain  claude_code "Decided X because Y" -c claude-code
hindsight bank stats     claude_code
```

## Configuration

Environment variables, all namespaced `HINDSIGHT_CC_*` (defaults are sane — change nothing to start):

| Var | Default | Purpose |
|-----|---------|---------|
| `HINDSIGHT_CC_BANK_ID` | `claude_code` | Bank to recall from / retain to |
| `HINDSIGHT_CC_AUTO_RECALL` | `true` | Toggle the recall hook |
| `HINDSIGHT_CC_AUTO_RETAIN` | `true` | Toggle the retain hook |
| `HINDSIGHT_CC_RECALL_BUDGET` | `mid` | `low` / `mid` / `high` (latency vs depth) |
| `HINDSIGHT_CC_RECALL_MAX_TOKENS` | `1024` | Cap on injected memory block |
| `HINDSIGHT_CC_RECALL_TYPES` | `world,experience` | Fact types to recall |
| `HINDSIGHT_CC_RETAIN_TOOL_CALLS` | `true` | Include tool calls in retained transcript |
| `HINDSIGHT_CC_PROFILE` | _(none)_ | Named CLI profile (`-p`) |
| `HINDSIGHT_CC_CLI_BIN` | _(PATH)_ | Explicit `hindsight` binary path |
| `HINDSIGHT_CC_DEBUG` | `false` | Log `[Hindsight]` lines to stderr |

## Why a CLI-backed port

The official [`hindsight-memory`](https://github.com/vectorize-io/hindsight)
plugin is a full, ~15-file Python integration with daemon management, local-LLM
providers, and three connection modes. This plugin targets the **external-API**
case only and delegates transport to the `hindsight` CLI, keeping it small and
true to this marketplace's markdown + JSON shape. The correctness-critical
content logic (memory-block stripping, transcript extraction) is adapted from
that plugin's `content.py` (MIT, vectorize-io). See `DECISIONS.md`.

## Development

```bash
python3 -m unittest discover -s tests   # behavioural tests (stdlib only)
```

## License

MIT. Content logic adapted from vectorize-io's `hindsight-memory` plugin (MIT).
