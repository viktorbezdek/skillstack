---
name: plugin-evaluation
description: Measures whether a Claude Code plugin actually works by running triggering evals (does the model pick the skill?) and output evals (does it produce correct results?). Use when you need to evaluate a plugin, run skill activation testing, set up an eval harness, measure plugin quality, write trigger rate tests, check output quality, compare plugin iterations, or iterate on a SKILL description based on eval results. Covers the two eval file formats (trigger-evals.json and evals.json), the grader/analyzer/comparator pattern from Anthropic's skill-creator, quality criteria for eval queries (realistic, varied, near-miss negatives), and the iteration methodology for fixing a skill that fails activation. NOT for writing the plugin's code itself — use plugin-architecture, plugin-hooks, or plugin-validation.
---

# Plugin Evaluation

> **If you haven't measured the activation rate and the output pass rate, you have not evaluated your plugin.** Shipping a skill without evals is shipping an untested function. This skill teaches the two eval types, the harness, and the iteration loop.

Primary source: Anthropic's skill-creator (`/Users/vbezdek/Work/skillstack/skill-foundry` — skills/skill-foundry/scripts/run_loop.py and README). This skill adapts that pattern and adds an offline smoke mode so you can validate eval *structure* without burning API calls.

---

## When to use this skill

- Preparing to ship a new skill and need to know if it will actually activate
- A skill is in production but sometimes Claude "forgets" to use it — debugging why
- Iterating on a SKILL description to improve trigger rate
- Comparing two versions of a skill to measure which is better
- Setting up CI to prevent activation regressions
- Writing the first eval files for an existing plugin that shipped without any

## When NOT to use this skill

- **Structural validation** (frontmatter, file layout) → use `plugin-validation`
- **Deciding what the skill should do** → use `plugin-architecture`
- **Writing hook scripts** → use `plugin-hooks`

---

## The two eval types

Every plugin needs **both**:

### 1. Trigger evals — does the model pick the skill?

Stored in `skills/<skill>/evals/trigger-evals.json`. Each case is a query + a `should_trigger` boolean.

```json
[
  {"query": "validate my claude code plugin structure", "should_trigger": true},
  {"query": "write a react component", "should_trigger": false}
]
```

The harness runs each query in a fresh session and checks whether the skill was invoked. Pass rate = (correct_triggers + correct_non_triggers) / total.

**Target**: ≥90% trigger rate on positive cases, ≥95% correct-no-trigger on negative cases. Below that, your description is too vague, too narrow, or collides with another skill.

### 2. Output evals — does the skill produce the right result?

Stored in `skills/<skill>/evals/evals.json`. Each case has a `query`, optional `files`, and `expected_behavior` (natural language description of what a correct run looks like).

```json
[
  {
    "query": "validate this plugin and report any errors",
    "files": ["fixtures/broken-plugin/"],
    "expected_behavior": "Agent runs the validator, identifies the missing description field in plugin.json, and reports it with the exact field path."
  }
]
```

The harness runs each case with a grader LLM that reads the agent's transcript and scores whether `expected_behavior` was met. This is the **grader pattern** from Anthropic's skill-creator — see `references/eval-file-formats.md` for the full schema.

---

## The harness: `scripts/run_eval.py`

Run in smoke (offline) mode — always safe, no API calls, structural checks only:

```bash
python3 plugin-dev/scripts/run_eval.py --plugin-dir plugin-dev --skill plugin-evaluation --offline
```

Or in live mode when you have `ANTHROPIC_API_KEY` and the SDK installed:

```bash
python3 plugin-dev/scripts/run_eval.py --plugin-dir plugin-dev --skill plugin-evaluation --mode trigger
python3 plugin-dev/scripts/run_eval.py --plugin-dir plugin-dev --skill plugin-evaluation --mode output
```

**⚠️ Offline mode is structural only.** It validates the eval files exist, parse, and have the required fields. It does NOT run the model. The benchmark report is prefixed with `OFFLINE MODE — SMOKE TEST ONLY` and the JSON has `"mode": "offline"`. Never ship an offline score as "the skill works".

---

## Quality criteria for eval queries

A good eval query is:

1. **Realistic** — phrased like a real user would phrase it. Not "execute plugin-validation skill for file X" (that's a skill invocation, not a query).
2. **Varied** — mix short and long, explicit and implicit, formal and casual.
3. **Including near-miss negatives** — negative cases should sound close to the skill's domain without actually requiring it. "How do I test a hook?" (near-miss: sounds like plugin-evaluation, belongs to plugin-hooks).
4. **Grounded in the description triggers** — every positive case should hit at least one trigger phrase from the frontmatter.

See `references/eval-quality-criteria.md` for counter-examples and a triage checklist.

---

## Iteration methodology

When a skill fails its triggering eval, DO NOT start adding keywords randomly. Follow this loop (adapted from Anthropic's `run_loop.py`):

```
1. Run trigger-evals → record which queries failed
2. Read the failing queries → categorize the misses
   - "description too narrow" → query uses valid synonym the description doesn't mention
   - "description too generic" → negative case triggered because description overlaps with another skill
   - "eval query unrealistic" → the query is the bug, not the skill
3. Update ONE thing at a time (description OR queries, not both)
4. Re-run evals → measure delta
5. Repeat until ≥90% positive and ≥95% negative
```

See `references/iteration-methodology.md` for the full loop including the "description surgery" rules (what to edit, what to leave alone) and common patterns (synonym gaps, domain collisions, trigger-phrase front-loading).

---

## The grader/analyzer/comparator pattern

Anthropic's skill-creator decomposes output evaluation into three roles:

| Role | Responsibility |
|---|---|
| **Grader** | Reads agent transcript + `expected_behavior`, scores pass/fail with reasoning |
| **Analyzer** | Reads all grader outputs, identifies patterns in failures (common confusion, missing capability) |
| **Comparator** | Runs two skill versions on the same evals, reports which produced better results and why |

This skill's harness ships with the grader and a basic analyzer. For full comparator mode, reference the run_loop.py in Anthropic's skill-creator.

---

## Self-test

This skill's own evals (`evals/trigger-evals.json`, `evals/evals.json`) are both exemplars and a self-test. Run the harness against this skill to see the pattern in action:

```bash
python3 plugin-dev/scripts/run_eval.py --plugin-dir plugin-dev --skill plugin-evaluation --offline
```

You should see a benchmark report with `mode: offline`, the case count from the eval files, and zero errors.

---

## References

| File | Contents |
|---|---|
| `references/eval-file-formats.md` | Full JSON schema for `trigger-evals.json` and `evals.json` with annotated examples |
| `references/eval-quality-criteria.md` | What makes a realistic query, counter-examples, the near-miss negative pattern, triage checklist |
| `references/iteration-methodology.md` | The failure-categorize-edit-remeasure loop, description surgery rules, common patterns |

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
