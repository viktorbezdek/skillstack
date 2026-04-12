# Eval Quality Criteria

> What separates a useful eval from theater. Applies to both `trigger-evals.json` and `evals.json`. Source: Anthropic's skill-creator + experience iterating on the skillstack plugins.

---

## The three failure modes of bad evals

1. **Theater** — eval passes because it's tautological (asks for the exact description text back), not because the skill works.
2. **Noise** — eval is so flaky the pass rate changes run to run regardless of skill changes.
3. **Narrow** — eval only tests the happy path, so the skill passes with 100% but fails every real user query.

All three look like "our evals pass" on paper. None of them tell you the skill works.

---

## Criteria for a good trigger eval query

A query is good if it satisfies **all** of:

### 1. Realistic

Phrased like a real user would phrase it — the way they'd type into a fresh Claude Code session with no context.

| Bad | Good |
|---|---|
| "execute plugin-validation on file X" | "my plugin isn't loading — can you check it for issues?" |
| "trigger the hooks skill" | "how do I write a hook that blocks rm -rf?" |
| "invoke the storytelling framework" | "help me restructure this story — the middle is flat" |

If the query names the skill or uses imperative CLI-speak, it's cheating. The whole point of the trigger eval is to measure whether the model picks the skill **without being told to**.

### 2. Varied

Mix across at least three axes:

- **Length**: short ("fix my plugin") and long ("I've been working on a plugin with three skills for weeks and the validation is now failing because…")
- **Explicitness**: direct ("validate this plugin") and implicit ("I'm getting weird errors on install")
- **Tone**: formal and casual

A set of 8 positive cases that are all 10-word imperatives is actually 1 eval repeated 8 times. It won't catch a description that works only for formal queries and fails on casual ones.

### 3. Grounded in the description

Every positive case should map to at least one trigger phrase from the SKILL.md frontmatter. If the query uses a phrase your description doesn't mention, that's either:

- A description gap (add the phrase if it's a real user pattern), or
- An out-of-scope query (move it to negatives)

**Exception**: include 1-2 "stretch" positive cases per skill — queries that use reasonable synonyms your description doesn't explicitly list — as a canary for description surgery. If those pass, your description is generalizing well.

### 4. Near-miss negatives

Boring negatives don't teach you anything:

```json
{"query": "write a python script", "should_trigger": false}   // useless — obviously unrelated
```

Good negatives sound like they might trigger:

```json
{"query": "test my hook before I ship", "should_trigger": false, "note": "Near-miss — sounds like plugin-evaluation, belongs to plugin-hooks"}
```

Aim for **≥3 of your ≥5 negatives to be near-miss** (topic-adjacent or phrase-overlapping). The remaining 2 can be "clearly off-topic" as a sanity check.

---

## Criteria for a good output eval case

### 1. `expected_behavior` is specific and gradable

A grader LLM reads your `expected_behavior` and scores the agent's transcript against it. If the description is fuzzy, the grading is fuzzy.

| Bad | Good |
|---|---|
| "Agent should validate the plugin" | "Agent invokes validate_plugin.py with --plugin-dir path, identifies the three errors (missing description, name mismatch, dead reference), and reports the exact field path for each error." |
| "Agent writes a good SKILL.md" | "Agent produces a SKILL.md with YAML frontmatter containing `name` and `description` fields, the description is 400-1024 chars in third person, contains ≥2 trigger verbs from the domain, and the body references at least one file under `references/`." |

The test: can you run two different agents, show their transcripts to a third person along with `expected_behavior`, and have that person reliably agree on which one passed?

### 2. `files` is minimal and self-contained

Attached fixtures should be as small as possible and live inside the test fixture directory. Do NOT reference the plugin's own source — that couples the eval to implementation details and breaks when you refactor.

### 3. At least one "partial credit" case

Pure pass/fail evals hide regressions where a skill degrades from "excellent" to "mostly works". Include at least one case whose `expected_behavior` has 2-3 distinct requirements so the grader can report "2 of 3 met" and you can notice the regression.

---

## Triage checklist before shipping an eval set

Run through this before committing the files:

- [ ] ≥8 positive + ≥5 negative trigger cases
- [ ] ≥3 of the negatives are near-miss
- [ ] No positive case uses skill-name or CLI-speak
- [ ] Queries vary in length (shortest < 8 words, longest > 20 words)
- [ ] ≥1 stretch positive (synonym not in the description)
- [ ] ≥3 output cases
- [ ] Every `expected_behavior` contains ≥2 testable assertions
- [ ] All fixtures under `fixtures/` are < 50 lines or justified

---

## Counter-examples

### A positive case that is actually theater

```json
{
  "query": "use the plugin-validation skill to validate my plugin",
  "should_trigger": true
}
```

This passes because the query literally says the skill name. It measures nothing — any skill with a matching `name` field would pass. Rephrase:

```json
{
  "query": "my plugin throws weird errors on install — can you check if the structure is correct?",
  "should_trigger": true
}
```

### A negative case that is noise

```json
{
  "query": "hello",
  "should_trigger": false
}
```

Obviously won't trigger anything. It adds 1 to your negative count without stressing the description.

### An `expected_behavior` that can't be graded

```json
{
  "query": "validate this plugin",
  "files": ["fixtures/broken-plugin/"],
  "expected_behavior": "Agent does a good job."
}
```

A grader cannot score this. What counts as "good"? What should the agent have caught? Rewrite with specific, checkable requirements.

---

## When to update vs throw out an eval

**Update** when the query is still realistic but the correct expected_behavior changed (e.g. the validator now reports one more error).

**Throw out** when the query is unrealistic in hindsight (nobody would actually ask that), or when it's measuring the wrong skill's territory.

**Never** edit an eval to make it pass. That is the definition of theater. If a case fails, either the skill is wrong (fix the skill) or the eval is wrong (fix the eval **because the query was unrealistic**, not **because it failed**).
