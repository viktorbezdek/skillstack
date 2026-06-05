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

---

## Skillstack Restructure & Hardening — Phase 1 Decisions (2026-06-05)

### D-001: Domain taxonomy — 4 domains replacing 9 categories

**Verdict:** Adopt 4-domain taxonomy (Engineering / Meta-Infra / Managerial-Product / Marketing-Comms).

**Rationale:** Current `category` field is empty on all 59 plugin.json files — the 9 "categories" exist only as collection names auto-generated by `build-registry.py` from an empty field. No existing partitioning to preserve. 4 domains map cleanly to user population segments (dev / CC-power-user / PM / marketer) and reduce discovery friction compared to 9 fine-grained categories.

**Evidence:** `grep '"category"' */.claude-plugin/plugin.json | sort -u` returns `"category": ""` for all 59. `scripts/build-registry.py` lines 34-71 show collections are generated from the category field; currently all plugins fall into a single empty-string bucket.

**Distribution:** E=24 / I=17 / P=13 / M=5. M is under-represented; monitor whether more plugins belong there.

---

### D-002: context-suite — keep all 4, mark as suite

**Verdict:** Keep `context-compression`, `context-degradation`, `context-fundamentals`, `context-optimization` as distinct plugins.

**Rationale:** Trigger surfaces are non-overlapping by design: compression=reduce, degradation=diagnose failures, fundamentals=theory, optimization=extend capacity. Merging would produce a 4-skill plugin with contradictory trigger intent. Suite design confirmed by ref counts (fundamentals=10, optimization=9).

**Evidence:** Trigger excerpts from `_groundtruth.json`: compression starts "REDUCING context size", degradation starts "Diagnosing context FAILURES", optimization starts "EXTENDING effective context capacity", fundamentals starts "Foundational theory". Zero trigger surface overlap.

---

### D-003: filesystem-context — merge-candidate (Phase 2 confirmation needed)

**Verdict:** Provisional merge-candidate into `memory-systems` OR re-scope as `workspace-context`.

**Rationale:** `filesystem-context` trigger ("Using the FILE SYSTEM for context — scratch pads, plan persistence, dynamic skill loading") partially overlaps `memory-systems` on the 'track state' trigger surface. Requires full trigger-evals comparison in Phase 2 before committing to merge.

**Evidence:** `filesystem-context` trigger excerpt from groundtruth. `memory-systems` ref-count=10 vs `filesystem-context` ref-count=5. Needs trigger-evals.json side-by-side read to confirm or reject overlap.

---

### D-004: outcome-orientation — merge-candidate (Phase 2 confirmation needed)

**Verdict:** Provisional merge-candidate into `product-thinking`.

**Rationale:** `outcome-orientation` trigger ("Reframe work around measurable outcomes using OKRs, KPIs, and the outcome-vs-output distinction") mirrors `product-thinking` skill trigger ("Apply outcome-over-output product thinking"). Near-identical intent signals possible duplication.

**Evidence:** Both trigger excerpts quoted in `docs/audit/01-inventory.md` overlap-cluster `outcome-product`. Full confirmation requires reading both skills' trigger-evals.json in Phase 2.

---

### D-005: persona-definition vs persona-mapping — keep distinct

**Verdict:** Keep both.

**Rationale:** Output artifacts are fundamentally different. `persona-definition` produces empathy maps and customer archetypes (UX/research artifact). `persona-mapping` produces RACI charts and Power-Interest matrices (org-design artifact). Different user populations, different deliverables.

**Evidence:** Trigger excerpts: definition="Create individual user personas...demographics, goals, pain points, empathy maps"; mapping="Map stakeholders...Power-Interest matrices, RACI charts, influence analysis". Zero functional overlap.

---

### D-006: skillstack-workflows granularity — flag for Phase 7 split review

**Verdict:** Keep as-is for Phase 1-4. Flag for post-Phase-5 split.

**Rationale:** 20 skills in one plugin is the largest non-trivial package. Some skills (spec-plan, spec-implement, spec-verify) form a sub-workflow; others (git-workflow, code-review) may belong in Engineering domain plugins. Splitting is architectural — deferred to post-migration review.

**Evidence:** `skillstack-workflows` has 20 skills per `_groundtruth.json`. Cross-referenced by 2 other plugins only — low coupling makes eventual split low-risk.

---

### D-007: Ground-truth build approach — Python script over workflow agents

**Verdict:** Use deterministic Python scripts (`_gen_inventory.py`) for Phase 1 document generation instead of multi-agent workflows with StructuredOutput schema.

**Rationale:** First attempt with workflow agents (wf_00e2c383-ec1) failed — all 10 parallel batch agents completed without calling StructuredOutput tool after 2 in-conversation nudges. Schema-based structured output is unreliable for long-context batch tasks. Python script over pre-built JSON produces identical output deterministically at zero additional token cost.

**Evidence:** wf_00e2c383-ec1 run log shows "subagent completed without calling StructuredOutput (after 2 in-conversation nudges)" x10 agents. `_gen_inventory.py` ran successfully and produced 176-line inventory on first attempt.

---

## Skillstack Restructure & Hardening — Phase 2 Decisions (2026-06-05)

### D-008: filesystem-context merge rejected — keep distinct

**Verdict:** Keep `filesystem-context` as a standalone plugin. Do NOT merge into `memory-systems`.

**Rationale:** Trigger surfaces operate at different abstraction levels. `filesystem-context` = OS filesystem as a context mechanism during Claude Code sessions (scratch pads, plan persistence, dynamic skill loading). `memory-systems` = production agent memory frameworks (Mem0, Zep, GraphRAG, vector stores). A user asking "how do I persist agent plans" wants FS patterns; a user asking "implement agent memory" wants framework architecture.

**Evidence:** `filesystem-context` NOT-for excludes KV-cache and summarization (context-engineering concerns). `memory-systems` NOT-for excludes hosted agent infrastructure (production deployment concern). Descriptions and trigger-evals confirm different output artifacts and different user intents.

---

### D-009: outcome-orientation merge rejected — keep distinct

**Verdict:** Keep `outcome-orientation` as a standalone plugin. Do NOT merge into `product-thinking`.

**Rationale:** Complementary handoff, not duplication. `outcome-orientation` handles OKR/KPI mechanics (write the OKRs, define the metrics). `product-thinking/outcome-oriented-thinking` skill handles philosophical product validation (is this really an outcome?). The two are explicitly designed to hand off: `product-thinking` trigger-evals FALSE entry routes "Write OKRs for the engineering team" AWAY from product-thinking and toward outcome-orientation.

**Evidence:** `product-thinking/outcome-oriented-thinking` trigger-evals: `"Write OKRs for the engineering team this quarter."` has `should_trigger: false`. This query routes to `outcome-orientation`. Handoff is intentional.

---

### D-010: E/I/P/M boundary rules — canonical definitions

**Verdict:** Adopt these boundary definitions as the stable rule for future plugin categorization.

**Engineering (E):** Plugin helps you BUILD something — code, APIs, agents, infrastructure, pipelines. Output = working software artifact.

**Meta-Infra (I):** Plugin helps Claude Code or LLM agents OPERATE BETTER — evaluate, remember, reason, manage context, author plugins. Output = improved CC/LLM behavior or process.

**Managerial-Product (P):** Plugin helps make DECISIONS and PLANS — product strategy, prioritization, risk, stakeholder management. Output = decision artifact (PRD, OKR, risk register, journey map).

**Marketing-Comms (M):** Plugin helps create CONTENT for human audiences — copy, editorial, interface text, narrative. Output = human-facing written content.

**Boundary rules:**
- Agent plugins: BUILD (multi-agent-patterns, agent-project-development) -> E; EVALUATE/OPERATE (agent-evaluation, memory-systems, prompt-engineering) -> I.
- "Thinking" plugins: strategic/PM use (creative-problem-solving, systems-thinking) -> P; meta-cognitive/LLM reasoning (critical-intuition) -> I.
- Ambiguous assignments (osint, gws-cli) noted in 02-taxonomy.md with monitoring notes.
