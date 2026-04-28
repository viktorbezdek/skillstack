# Changelog — technical-copywriting

All notable changes to this plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-04-28

### Added

- **engaging-craft / AI-prose tells (humanization pass).** Elevated AI-prose detection from a single anti-pattern bullet to its own section in `engaging-craft/SKILL.md`, with the full vocabulary catalog (high-frequency AI words, AI transitions, reflex hedges, academic filler verbs, buzzwords) inline plus the six structural fingerprints and the seven-step sniff test.
- **engaging-craft / `references/ai-tells-and-substitutions.md`** — new reference (5th in the skill) cataloging the explicit blacklist with concrete substitutions, structural anti-patterns, worked humanization transformations, and guidance on when AI-coded vocabulary is legitimately the right word.
- New trigger keywords in `engaging-craft` description: humanization, AI-prose, AI-tells, AI-buzzwords. Surfaces activation for queries like "humanize this AI-generated prose," "remove AI tells," "fix robotic copy."

### Changed

- `engaging-craft` SKILL.md description, `✅ Use for` list, and references table updated for the new humanization scope.
- Plugin-level keywords / tags in marketplace and registry add: `humanization`, `ai-prose-detection`, `ai-tells`, `ai-buzzwords`.

### Notes

- Benchmarks against sonnet-4-6 on canonical one-shot prompts (run 2026-04-28) showed no measurable lift (Δ pass-rate 0.00 on engaging-craft, −0.11 on distribution-craft) — modern Claude has internalized many of the anti-patterns this plugin teaches via RLHF. The plugin's value is as structured reference for human authors during iteration, audit, and critique cycles. The new AI-tells catalog targets the residual leak-through that even strong models exhibit.

## [1.0.0] - 2026-04-28

### Added

- Initial release.
- Five composable skills for long-form technical writing:
  - **technical-research** — audience profiling, source tiering, triangulation, evidence types, citation discipline.
  - **long-form-structure** — article anatomy (hook → promise → setup → development → payoff), templates for deep-dive / tutorial / opinion / case study / whitepaper / technical narrative, section transitions, length strategy.
  - **engaging-craft** — proven copywriting formulas (AIDA, PAS, Before-After-Bridge, Bencivenga's pyramid, Sugarman's slippery slide, Schwartz awareness levels), hooks, voice and tonality, concrete-over-abstract.
  - **long-form-polish** — pacing and rhythm, scan-ability, the 30% cut discipline, the read-aloud test.
  - **distribution-craft** — title formulas, dek and meta description, social pull-quotes for X/LinkedIn/HN/Reddit, channel framing.
- Per-skill `references/` for progressive disclosure (4 references per skill, 20 total).
- Per-skill `evals/trigger-evals.json` and `evals/evals.json`.
