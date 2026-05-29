# Decision log — hindsight plugin

Why each component exists and what type it is. Produced by the `build-a-plugin`
workflow (ideation → research → architecture → build → validation → evaluation).

## Phase 1 — ideation (kill gate: PASS)

- **Problem:** Claude Code sessions lose context across sessions; I want recall
  before each prompt + retain after each turn, plus manual control of my memory.
- **Audience:** me — a heavy Hindsight CLI user on the external API.
- **Existing alternatives:** the official `hindsight-memory` plugin already does
  auto-recall/auto-retain (it runs in my sessions). → fork the hard parts, do
  not rebuild wholesale.
- **Activation:** clear ("what do I remember", "recall", "retain this", "reflect").
- **Scope NOT:** no local daemon, no local-LLM provider, no bundled HTTP client,
  no short-term context (Claude already has the transcript), no code search.
- **Components:** 3 hooks + 1 skill + 1 command (genuine multi-component).
- **Value:** yes — installable, distributable, skillstack-native memory.

## Phase 2 — research & build-vs-fork

- The official plugin (`vectorize-io/hindsight`, MIT) is a ~15-file Python
  integration: `daemon.py`, `llm.py`, `client.py`, `content.py`, `state.py`,
  three connection modes. Heavy; fights skillstack's markdown + JSON identity.
- The `hindsight` CLI (v0.7.1) is installed and configured against the external
  API. On the external API the **server** does fact extraction — so the daemon,
  LLM-provider, and connection-mode machinery are all unnecessary.
- **Decision:** lean **CLI-backed port**. Delegate transport to the CLI; lift
  only the correctness-critical content logic (memory-block strip, transcript
  extraction) from the official `content.py`.

## Phase 3 — component map

| Capability | Extension type | Why |
|------------|----------------|-----|
| Recall relevant memories before each prompt | **hook** (UserPromptSubmit) | Event-driven, must run on every prompt, output as `additionalContext`. |
| Retain conversation after each turn | **hook** (Stop, async) | Event-driven, non-blocking, post-response. |
| Verify the server is reachable | **hook** (SessionStart) | Lifecycle event. |
| Teach manual memory interaction + the model | **skill** | Declarative knowledge Claude loads on demand. |
| One-shot manual recall/reflect/retain | **command** (`/hindsight`) | User-invoked action. |

Transport (HTTP client, daemon, LLM provider) is **not** a plugin component — it
is the installed CLI. State tracking (turn counters, `state.py`) is replaced by a
deterministic SHA-256 document id for idempotency.

## Key build decisions

- **Fail-open everywhere.** Any hook error/timeout → exit 0, no output. Memory is
  never a blocking dependency of a prompt.
- **Strip before retain (non-negotiable).** `strip_memory_tags` removes injected
  `<hindsight_memories>` blocks so the bank never ingests its own recalls.
  Guarded by `tests/test_transcript.py`.
- **Idempotent doc-id:** `cc-<sha256("claude-code:" + session_id)[:16]>` — re-runs
  replace, not duplicate. Accepted trade-off: post-compaction shrink overwrites.
- **Argv-safe chunked retain (post-review fix).** The transcript is passed to the
  CLI as a single argument; the OS caps one argv element (Linux `MAX_ARG_STRLEN`
  ≈ 128 KB). The first cut passed the whole transcript and would have *silently*
  failed to store long sessions (OSError caught → async Stop ignores the return).
  Fixed by `build_retain_chunks`: pack whole messages into argv-safe chunks, each
  retained under `<base>-c<i>` so nothing is dropped. `retain-files` was rejected
  because it offers no `-d/--doc-id` (would break idempotency). Verified live with
  a 260 KB transcript → 4 chunks, 4/4 stored.
- **Env-only config**, namespaced `HINDSIGHT_CC_*` to avoid clashing with the
  CLI's own `HINDSIGHT_*` vars.

## Deployment note — coexistence

The official `hindsight-memory` plugin installs the same recall/retain hooks. Do
not run both: recall would fire twice per prompt and retain twice per session
(different doc-id schemes → accumulation, not dedupe). Users must disable one.
Documented in README.

## Verification evidence (build)

- `recall.py` ran live → injected 18 real memories from the `claude_code` bank
  (recallability proven end-to-end).
- `retain.py` ran live → CLI accepted the retain and returned success
  (*submission* verified; async server-side fact extraction not confirmed within
  the test window). Injected memory block confirmed stripped.
- `retain.py` ran live on a **260 KB** transcript → split into 4 argv-safe chunks,
  4/4 submitted successfully (the size-ceiling regression case).
- `session_start.py` → `healthy`.
- 9/9 behavioural tests pass; `basedpyright` 0 errors on all modules.
- All throwaway test banks deleted; no test artifacts left on the server.
