# Iteration Methodology

> The loop for fixing a skill that fails its evals. Adapted from Anthropic's skill-creator `run_loop.py`. The core idea: change one thing at a time, measure, repeat — never batch changes.

---

## The loop

```
┌──────────────────────┐
│ 1. Run trigger-evals │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────────────┐
│ 2. Categorize failing cases  │
└─────────┬────────────────────┘
          │
          ▼
┌──────────────────────────────────────┐
│ 3. Pick ONE category, make ONE edit  │
└─────────┬────────────────────────────┘
          │
          ▼
┌──────────────────┐
│ 4. Re-run evals  │
└─────────┬────────┘
          │
          ▼
┌────────────────────────────┐
│ 5. Did the category clear? │
└─────────┬──────────────────┘
          │
  yes ─┴─ no
   │       │
   ▼       ▼
 next   revert and try a different edit
category
```

Stop when: positive rate ≥90%, negative rate ≥95%, and no single category has >1 remaining failure.

---

## Step 1: Run trigger-evals

```bash
python3 plugin-dev/scripts/run_eval.py \
  --plugin-dir plugin-dev \
  --skill <your-skill> \
  --mode trigger
```

Read `workspace/benchmark.md`. Look at the per-case results, not just the pass rate.

---

## Step 2: Categorize failing cases

Every failure falls into one of these buckets:

### A. Description too narrow (positive cases failing)

A realistic query uses a synonym or phrasing that your description doesn't mention.

**Example**: Description says "validate Claude Code plugins". Query says "check my SKILL.md for issues". "Check" isn't in the description — model doesn't pick the skill.

**Fix**: Add the synonym to the description. Front-load it in the first 250 chars.

### B. Description too generic (negative cases firing)

A negative case triggers the skill because the description overlaps with another skill's domain, or because it's so broad it grabs unrelated queries.

**Example**: Description says "handles all plugin work". A query asking "how do I scaffold a new plugin" triggers plugin-evaluation when it should have gone to plugin-ideation.

**Fix**: Tighten the description with "NOT for X" language and more specific verbs.

### C. Trigger verbs not front-loaded

Description mentions the right phrases but buries them past the 250-char mark where the first-pass matcher ignores them.

**Example**: Description starts "A comprehensive framework for evaluating…" — the word "evaluating" only appears at char 40. Good. But the actual trigger phrases ("eval harness", "trigger rate", "run evals") are at char 380 where the attention is weaker.

**Fix**: Rewrite the first 250 chars to include the 3-4 strongest trigger verbs.

### D. Eval query is unrealistic (you're wrong, not the skill)

The query doesn't match how real users would phrase it. Cheated positive cases (uses skill name literally) or artificial negatives (phrased in a way no human would type) both belong here.

**Fix**: Edit the eval, not the skill. Make the query realistic.

### E. Collision with another skill

Two skills both legitimately apply, and the model picks the other one. This is not a fixable-via-description problem — you need to either merge the skills, move the query to `should_trigger: false`, or accept that the query is ambiguous and count it as "pass" when either skill activates.

**Fix**: Architectural change or reframe the eval.

---

## Step 3: Make ONE edit

**This is the most important rule.** Changing description + query + adding a reference in the same iteration means you cannot tell which change fixed what. You lose the ability to measure cause and effect.

Pick the single category with the most failures. Make the smallest possible edit that addresses it. Commit the intermediate state (even if it's ugly) so you can revert.

### Description surgery rules

Things it is safe to edit:
- Add synonyms to the `description` field
- Reorder phrases in the first 250 chars
- Add "NOT for X" disjunctions
- Tighten verbs (e.g. "handles" → "validates")

Things that are NOT safe to edit during iteration:
- The `name` field (breaks activation cache, invalidates all prior runs)
- The body structure (irrelevant to triggering — the model only sees the frontmatter during trigger matching)
- The `references/` content (same — not read during triggering)

### Eval surgery rules

Things it is safe to edit:
- Rephrase a query to be more realistic
- Add `note` fields explaining *why* a case matters
- Add new cases (growing the set)
- Move a case from positive to negative (or vice versa) if your understanding of the skill's scope changed

Things that are NOT safe:
- Deleting failing cases without noting why (that's erasing signal)
- Adding cases that are tautological (theater — see eval-quality-criteria.md)

---

## Step 4: Re-run evals

Run the trigger evals again. Compare pass rates per category:

```
Before:  category A = 4/8 fail, category B = 2/5 fail
After:   category A = 1/8 fail, category B = 2/5 fail
```

If category A improved (as intended), good — proceed. If category B got worse, investigate whether your edit broke a negative case (e.g. you added a synonym that was also used in an out-of-scope query).

---

## Step 5: Repeat or stop

**Stop** when:
- Positive rate ≥90% (at least 8/10 or 9/10)
- Negative rate ≥95% (at least 5/5 or 9/10)
- No single category has >1 remaining failure
- Re-running the evals twice gives stable results (not a flaky 80%/95% oscillation)

**Keep going** otherwise. Each iteration is one edit + one re-run. Budget: 5-10 iterations for a new skill, 1-3 for a mature skill.

---

## Anti-patterns in the iteration loop

### Batch editing

"I noticed 4 issues, let me fix all of them." → now you can't tell which fix worked. Revert and do them one at a time.

### Keyword stuffing

"My description needs more keywords" → adding every synonym you can think of. Result: description becomes a word salad, trigger rate plateaus because the model can't identify the core domain. Aim for 3-4 strong trigger phrases, not 15 weak ones.

### Chasing the long tail

Iteration 10 fixed the last 2 edge cases. Iteration 11 hurts average case. This is overfitting to the eval. Stop and call it done — the eval is a proxy, not the goal.

### Editing evals to pass

A case fails → you delete or rephrase the case until it passes. This is theater. The only valid reason to edit a failing query is that the query itself was unrealistic (category D). If the query is realistic and failing, the **skill** needs the change.

### Ignoring negatives

Focusing only on positive pass rate. A skill that triggers on everything has 100% positive but 0% negative — useless. Always check both rates.

---

## Example iteration log

```
Iteration 1:
  Trigger evals: pos 5/8 (62.5%), neg 5/5 (100%)
  Failing positive cases: (2, 4, 7)
  Category A (too narrow): cases 2, 4 use "check" not "validate"
  Edit: added "check, verify, inspect" to description first line
  Result: pos 7/8 (87.5%), neg 4/5 (80%)
  Regression: case 9 (neg) now fires — "check this code for issues"

Iteration 2:
  Edit: added "NOT for general code review" to description
  Result: pos 7/8 (87.5%), neg 5/5 (100%)
  Remaining positive failure: case 7 — "why doesn't my plugin work"
  Category B-adjacent — query is too generic to map to plugin-validation
  Decision: move case 7 to plugin-ideation's eval set instead
  Result (after eval file edit): pos 7/7 (100%), neg 5/5 (100%)

DONE.
```

---

## When the loop stalls

If you've done 5+ iterations and rates haven't moved, stop and ask:

1. **Is the skill's scope well-defined?** If you can't write a one-sentence "this skill handles X" without contradictions, the scope is the problem, not the description.
2. **Is there collision with another skill?** Run the same evals against the colliding skill — if both fire, you have a domain overlap to resolve.
3. **Is the description < 400 chars?** Anthropic's guidance targets 400-1024 chars. Below 400 and you don't have room for proper trigger coverage.
4. **Is the query set too small?** 8 positive + 5 negative is the floor. 16 + 10 is better. More cases = lower flake, clearer signal.

If all four are fine and the loop still stalls, the problem may not be solvable with description surgery — it may be an architecture issue (should be a hook, not a skill; should be merged with another skill; belongs in a different plugin). See `plugin-architecture` skill.
