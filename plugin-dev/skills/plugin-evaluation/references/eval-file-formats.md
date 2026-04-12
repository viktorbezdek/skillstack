# Eval File Formats

> The two JSON files that drive every plugin evaluation: `trigger-evals.json` (does the model pick the skill?) and `evals.json` (does the skill produce correct output?). This reference documents the full schema, gives annotated examples, and cites Anthropic's skill-creator as the source.

Primary source: Anthropic's `skill-creator` bundled skill (`skills/skill-creator/scripts/run_loop.py`, `skills/skill-creator/README.md`).

---

## Where eval files live

Inside each skill directory:

```
plugin-dev/skills/plugin-evaluation/
├── SKILL.md
├── references/
└── evals/
    ├── trigger-evals.json       ← activation testing
    └── evals.json               ← output testing
```

**Per-skill, not per-plugin.** A plugin with 5 skills has 5 `evals/` directories. This keeps the blast radius of an eval change scoped to one skill.

---

## `trigger-evals.json` — activation testing

### Schema

```json
[
  {
    "query": "string — the user query the model will see",
    "should_trigger": true,
    "note": "optional — why this case matters"
  }
]
```

| Field | Required | Type | Purpose |
|---|---|---|---|
| `query` | yes | string | The exact query the evaluator sends in a fresh session |
| `should_trigger` | yes | boolean | `true` if the skill SHOULD be invoked; `false` if it should NOT |
| `note` | no | string | Human-readable why; ignored by the harness, preserved across iterations |

### Example

```json
[
  {
    "query": "validate my claude code plugin structure",
    "should_trigger": true,
    "note": "Direct hit — 'validate' + 'plugin' is the primary trigger"
  },
  {
    "query": "check my SKILL.md frontmatter for issues",
    "should_trigger": true,
    "note": "Same domain via synonym (check vs validate)"
  },
  {
    "query": "write a react hook",
    "should_trigger": false,
    "note": "Unrelated — 'hook' here means React hook, not Claude Code hook"
  },
  {
    "query": "why doesn't my claude code skill activate",
    "should_trigger": false,
    "note": "Near-miss — sounds like validation but is actually plugin-evaluation territory"
  }
]
```

### Minimum size

Per this plugin's validation rules (matching Anthropic's guidance): **≥8 positive + ≥5 negative cases per skill**. Fewer than that and the signal is too noisy — a single flaky case dominates the pass rate.

### Near-miss negatives

The most valuable negative cases are ones that sound close to the positive domain but actually belong to a different skill (or no skill). They are how you catch "description collision" — two skills whose triggers overlap.

```json
{
  "query": "test my hook script before I ship it",
  "should_trigger": false,
  "note": "Near-miss for plugin-evaluation, belongs to plugin-hooks"
}
```

---

## `evals.json` — output testing

### Schema

```json
[
  {
    "query": "string — user query",
    "files": ["fixtures/path/to/input.md"],
    "expected_behavior": "string — natural language description of correct behavior"
  }
]
```

| Field | Required | Type | Purpose |
|---|---|---|---|
| `query` | yes | string | The query that triggers the skill and asks for the output |
| `files` | yes | array | Paths (relative to the eval run's cwd) to input fixtures; empty array `[]` if the query is self-contained |
| `expected_behavior` | yes | string | A grader-readable description of what the agent should have produced |

### Example

```json
[
  {
    "query": "validate this plugin and report all errors",
    "files": ["fixtures/broken-plugin/"],
    "expected_behavior": "Agent runs the validator, identifies (1) missing description field in plugin.json, (2) skill name mismatch in frontmatter, and (3) a references/X.md citation that points to a nonexistent file. All three errors must appear in the response with their exact field paths."
  },
  {
    "query": "my skill description is 250 chars — is that enough?",
    "files": [],
    "expected_behavior": "Agent explains that 250 chars is at the edge: the first 250 chars are the critical activation window, and trigger phrases must be front-loaded. A complete description should be 400-1024 chars with third-person phrasing and explicit trigger verbs."
  },
  {
    "query": "run my plugin's trigger evals",
    "files": ["fixtures/sample-plugin/"],
    "expected_behavior": "Agent invokes scripts/run_eval.py with --mode trigger, waits for completion, and reports pass rate broken down by positive/negative cases. On API key absence, agent falls back to --offline and loudly notes that offline scores are structural only."
  }
]
```

### Minimum size

**≥3 output cases per skill**. Output evals are expensive to run (each one is an agent session), so keep the set tight but representative: one happy path, one "partial success" (agent does most of it), one failure mode you want to test (edge case or regression).

### `expected_behavior` is grader input

The grader LLM reads the transcript AND `expected_behavior`, then decides pass/fail. Write `expected_behavior` the way you'd describe correct behavior to a colleague. Be specific:

- ❌ "Agent should validate the plugin" (too vague — grader can't score)
- ✅ "Agent runs validate_plugin.py, identifies the three errors (X, Y, Z), and reports the exact field path for each"

---

## How the harness consumes these files

### Live mode (`--mode trigger` or `--mode output`, requires `ANTHROPIC_API_KEY` + SDK)

1. Reads both eval files
2. For trigger mode: runs each `query` in a fresh session, checks whether the skill activated
3. For output mode: runs each `query` with attached `files`, captures transcript, sends transcript + `expected_behavior` to the grader
4. Writes `benchmark.json` (machine-readable) and `benchmark.md` (human-readable)

### Offline / smoke mode (`--offline`, always safe)

1. Reads both eval files
2. Validates JSON structure, required fields, minimum counts
3. Writes `benchmark.json` with `"mode": "offline"` and a synthetic-results warning banner
4. Writes `benchmark.md` with **OFFLINE MODE — STRUCTURAL SMOKE TEST ONLY** prefix

Offline mode is for CI and for fast iteration when you're editing eval files. It does **not** tell you whether the skill actually works.

---

## Provenance

This file format is adapted from Anthropic's skill-creator skill (bundled with Claude Code). Original reference: `skills/skill-creator/scripts/run_loop.py` and `skills/skill-creator/README.md`. See `iteration-methodology.md` for how Anthropic's run loop drives description iteration from eval results.
