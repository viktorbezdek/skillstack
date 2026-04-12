# Problem-Worthy Checklist

> The 7-criteria test for deciding whether a plugin idea is worth building. An idea must pass **at least 5 of 7** to justify the effort.

---

## The 7 criteria

### 1. Repeatable

**Test**: Can you state the trigger as "every time X, I want Y"? Can you point to ≥3 instances in the past month?

**Pass example**: "Every time I run a migration script, I forget to check the rollback plan. I want a hook that blocks `alembic upgrade` without first confirming the rollback file exists."

**Fail example**: "Sometimes I wish Claude would summarize long docs better."

- No specific trigger
- No measurable frequency
- No clear "every time X" pattern

### 2. Concrete

**Test**: Can you describe the desired behavior in 2-3 sentences with specific inputs and outputs?

**Pass example**: "When I paste a pytest traceback, I want a skill that parses the traceback, identifies the failing test's file and line, and suggests 3 likely causes based on the exception type and the surrounding context. Output is a markdown block with a section per cause."

**Fail example**: "I want a plugin that makes debugging easier."

- "Easier" has no definition
- No specific input
- No specific output

### 3. Shareable

**Test**: Would someone on your team — or someone outside your company — benefit from this same plugin?

**Pass example**: "A plugin that enforces our company's commit message format." — at least 10 people on your team have the same pain.

**Fail example**: "A plugin that opens my personal obsidian vault and appends a note." — only works for you, only you have an obsidian vault in that exact location.

**The gray zone**: personal workflow plugins are fine as ideation targets if you'd be comfortable explaining them in a README. If they'd require 3 paragraphs of "this only works if you use X and Y and Z exactly like I do", they're not shareable.

### 4. Not already solved

**Test**: Did you check the marketplace, the Anthropic bundled plugins, and ≥3 top community plugin collections?

**Pass example**: "I searched the skillstack marketplace, the Anthropic hub, and 3 community collections. No plugin covers this."

**Fail example**: "I haven't checked but I'm pretty sure there's nothing like this."

**Methodology**: this is `plugin-research` territory. Don't guess — actually survey. See the `plugin-research` skill for the full methodology.

### 5. Composable

**Test**: If another plugin installed alongside yours hooks the same event or defines a similar skill, does yours still work?

**Pass example**: A `PreToolUse` hook on `Bash` with a narrow matcher that blocks only `rm -rf /`. Two of these from different plugins is fine — they just both decline that specific pattern.

**Fail example**: A `PreToolUse` hook on `*` that rewrites all tool input through a proxy. This breaks any other hook on `*` that also wants to run.

**Composability red flags**:
- Matcher `*` or `Bash` (too broad)
- Modifies `updatedInput` in a way that overwrites fields other hooks care about
- Assumes exclusive write access to a shared file
- Overrides global settings

### 6. Maintainable

**Test**: If Claude Code ships a new version, will your plugin still work without changes? Or will it break because you relied on undocumented internals?

**Pass example**: Uses documented hook events, documented manifest fields, documented path substitution. Changes in Claude Code that could break it would be visible in release notes.

**Fail example**: Parses the transcript file format directly to extract tool results. That format is undocumented and changes between versions.

**Maintenance checklist**:
- Only references documented features
- Tests exist (trigger evals, output evals, unit tests for scripts)
- CI runs the tests on a recent Claude Code version
- README says "tested with Claude Code X.Y.Z" so users know when to re-verify

### 7. Testable

**Test**: Can you write eval queries that pass when the plugin works and fail when it doesn't?

**Pass example**: "I can write trigger evals: 10 queries that should activate my skill, 10 that shouldn't. I can write output evals: 3 cases with expected_behavior a grader can score."

**Fail example**: "I'll know it's working when users seem happier." — not testable, can't go in CI, can't detect regressions.

---

## The scoring template

Fill this out for each candidate idea:

```
Idea: ________________________________________________

1. Repeatable      [  /3]   (0=never, 1=once, 2=occasional, 3=frequent)
2. Concrete        [  /3]   (0=vague, 1=fuzzy, 2=mostly, 3=crisp)
3. Shareable       [  /3]   (0=just me, 1=team, 2=company, 3=industry)
4. Not already solved [  /3] (0=many alternatives, 1=few, 2=niche, 3=new)
5. Composable      [  /3]   (0=conflicts, 1=risky, 2=fine, 3=excellent)
6. Maintainable    [  /3]   (0=fragile, 1=brittle, 2=stable, 3=rock-solid)
7. Testable        [  /3]   (0=vibes only, 1=hard, 2=doable, 3=easy)

TOTAL:             [  /21]
```

**≥15 → strong idea, build it**
**10-14 → promising but needs work — iterate on the weak dimensions**
**<10 → skip it, or downgrade to a personal prompt/snippet**

---

## Worked example 1: pass

**Idea**: "Auto-format Python files after every edit with ruff."

| Criterion | Score | Why |
|---|---|---|
| Repeatable | 3 | Every edit is a trigger, fires 20+ times per session |
| Concrete | 3 | Clear: run `ruff format` on the edited file after Edit/Write |
| Shareable | 3 | Every Python developer wants this |
| Not already solved | 2 | A few hooks do this but none are polished as a plugin |
| Composable | 3 | Narrow matcher (Edit\|Write), small blast radius |
| Maintainable | 3 | Uses documented `PostToolUse` event |
| Testable | 2 | Trigger evals are N/A (hooks aren't skills), but can test with `test_hook.sh` |

**Total: 19/21 → BUILD**

---

## Worked example 2: fail

**Idea**: "A skill that makes Claude more creative."

| Criterion | Score | Why |
|---|---|---|
| Repeatable | 1 | "When creativity is needed" — vague trigger |
| Concrete | 0 | What does "more creative" mean? |
| Shareable | 2 | Many people want it, but they'd want it in different ways |
| Not already solved | 1 | Many "creativity"-themed skills already exist |
| Composable | 1 | Overlaps with any skill that injects reasoning style |
| Maintainable | 2 | No undocumented internals, but hard to know when it's broken |
| Testable | 0 | "I'll know it's creative when I see it" |

**Total: 7/21 → SKIP**

---

## Worked example 3: borderline

**Idea**: "A skill that migrates Redux code to Zustand."

| Criterion | Score | Why |
|---|---|---|
| Repeatable | 1 | Migration is typically a one-off per project |
| Concrete | 3 | Clear transformation: Redux patterns → Zustand equivalents |
| Shareable | 3 | Many projects do this migration |
| Not already solved | 2 | Some codemods exist but nothing plugin-shaped |
| Composable | 3 | Skill is narrow-domain, no conflicts |
| Maintainable | 2 | Redux/Zustand APIs evolve; needs periodic updates |
| Testable | 3 | Can write trigger evals (migration questions) and output evals (expected transformed code) |

**Total: 17/21 → BUILD, but note that the "repeatable" dimension suggests packaging as an installable reference rather than a daily-use skill**

---

## When an idea scores 10-14

Iterate rather than abandon:

| Weak dimension | Fix |
|---|---|
| Repeatable | Find the more general version of the problem that fires more often |
| Concrete | Write the one-sentence problem statement before scoring again |
| Shareable | Generalize the specific parts; make paths and tools configurable |
| Not already solved | Do the `plugin-research` pass; maybe fork instead of building |
| Composable | Narrow the matcher / scope / hook surface |
| Maintainable | Refactor to use documented APIs only; add tests |
| Testable | Break the behavior into measurable sub-behaviors |

Re-score after iterating. If the score doesn't move above 15, the idea probably isn't plugin-shaped — it may be a CLAUDE.md entry, a personal prompt, or a one-off.
