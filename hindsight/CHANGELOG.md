# Changelog

All notable changes to the `hindsight` plugin are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/);
this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-29

### Added
- Initial release: a lean, CLI-backed Hindsight long-term-memory integration for Claude Code.
- `UserPromptSubmit` hook (`recall.py`) — recalls relevant memories and injects them as an invisible `<hindsight_memories>` block. Fail-open with bounded latency.
- `Stop` hook (`retain.py`, async) — strips injected memory blocks, then retains the transcript under a deterministic per-session document id (idempotent re-runs). Long transcripts are split into argv-safe chunks (each its own document) so sessions that exceed the OS command-line argument limit still persist fully.
- `SessionStart` hook (`session_start.py`) — silent reachability check.
- `hindsight-memory` skill — manual recall / reflect / retain and bank, entity, mental-model, directive management, with `cli-reference.md` and `memory-model.md` references.
- `/hindsight` command — one-shot recall / reflect / retain / stats.
- Env-var configuration namespaced `HINDSIGHT_CC_*`; external-API only (server-side fact extraction; no daemon, no local LLM).
- Behavioural test suite guarding the anti-feedback-loop strip, transcript parsing, and doc-id determinism.

### Notes
- Correctness-critical content logic (memory-block stripping, transcript extraction) adapted from vectorize-io's official `hindsight-memory` plugin (MIT).
