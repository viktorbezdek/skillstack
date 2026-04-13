---
name: plugin-ideation
description: Turns a vague "I want to build a Claude plugin" into a concrete, problem-first plugin idea — or tells you to not build it. Use when you want to build a Claude plugin, have an idea for a plugin and don't know if it's worth pursuing, are asking "should I build this as a plugin or is there already one", are exploring plugin ideas for your team, or are mining your workflow for repeatable pain points that could become plugins. Covers pain-point mining (what workflow pains become plugins), the problem-worthy checklist (seven criteria a plugin idea must pass), the "build for a problem, not for yourself" discipline, and ideation anti-patterns (scope creep, engineering-exercise plugins, one-off tasks, already-solved). NOT for validating an idea against existing plugins — use plugin-research for marketplace surveys.
---

# Plugin Ideation

> **Problem-first framing. Do not build a plugin for a one-off task.** The best plugin ideas come from watching yourself suffer the same friction repeatedly, not from "wouldn't it be cool if Claude could…". This skill teaches the discipline of mining pain, checking whether it's worth solving, and filtering out ideas that should remain as one-off prompts.

---

## When to use this skill

- You want to build a plugin but don't have a specific idea yet
- You have an idea and wonder if it's worth the build effort
- You're reviewing several ideas and need a way to rank them
- You just shipped a plugin and want to find the next one to build
- You're on a team brainstorming plugins and need a framework

## When NOT to use this skill

- **Validating an idea against existing plugins** → `plugin-research` (marketplace survey, build-vs-fork)
- **Designing the plugin's components** → `plugin-architecture`
- **Writing the plugin content** → `skill-foundry`, `plugin-hooks`, `plugin-composition`
- **Evaluating a shipped plugin** → `plugin-evaluation`

---

## The core discipline: problem-first framing

A plugin is worth building if and only if it solves a **repeatable problem**. Two words matter:

- **Problem**: something that's causing friction now, not a theoretical pain
- **Repeatable**: happens often enough that a reusable solution pays back the build cost

If either word is missing, you don't have a plugin idea yet — you have an engineering hobby project.

### Three kinds of ideas that are NOT plugin-worthy

1. **"Wouldn't it be cool if…"** — no real user pain driving it
2. **"I did this once last quarter"** — not repeatable, just a one-off
3. **"I want to play with hooks"** — engineering exercise, not problem-driven

Every one of these will produce a plugin nobody uses, including you.

---

## Pain-point mining

The best source of plugin ideas is watching yourself work. Spend a week noticing:

### Repetitive prompts

Are you typing the same kind of prompt week after week? "Review this PR", "summarize this meeting", "debug this test"? If the pattern is stable, it's a skill candidate.

### Repeated context setup

Are you pasting the same 5 files into Claude every time you start a task? That's a `SessionStart` hook candidate — it can inject that context automatically.

### Pre- and post-action automation

Are you running the same commands before or after every edit / commit / test? That's a hook candidate. Lint on save, format on save, test on commit.

### External system bridges

Are you pasting data from your CRM / monitoring / ticket tracker into Claude? That's an MCP candidate.

### Workflow gates

Are you manually checking "did I remember to X before shipping Y"? That's a guardrail hook.

### Pick one from the list

The *best* pain point is:
- Something that wasted >30 minutes this week
- Happens ≥3 times per week
- You can describe the desired behavior in one sentence
- It's not already covered by an existing plugin (check `plugin-research`)

---

## The problem-worthy checklist

Once you have a candidate, test it against these 7 criteria. A worthy plugin idea passes **at least 5 out of 7**. Full discussion: `references/problem-worthy-checklist.md`.

### 1. Repeatable

You can state the trigger with confidence: "Every time I do X, I want Y to happen". Not "sometimes I wish…".

### 2. Concrete

You can describe the desired behavior in 2-3 sentences. If you need a paragraph, the scope is too vague.

### 3. Shareable

Someone else would want the same behavior. If it's so specific to you that nobody else has the same pain, it's a CLAUDE.md entry, not a plugin.

### 4. Not already solved

You checked the marketplace and no existing plugin does the thing. (Cross-reference: `plugin-research`.)

### 5. Composable

Your plugin works alongside others without conflicts. A hook that blocks every Bash call is not composable.

### 6. Maintainable

You (or the team) can keep it working as Claude Code evolves. A plugin relying on undocumented internals is not maintainable.

### 7. Testable

You can measure whether it works — with trigger evals, output evals, or automated scripts. "I'll know it's working when it feels right" is not testable.

**5/7 or better → ship it. 4/7 → iterate on the idea. <4/7 → skip it.**

---

## Ideation anti-patterns

Covered in full in `references/ideation-anti-patterns.md`. Summary:

### 1. Building for yourself only

The plugin works for your specific workflow and nobody else's. Symptoms: hardcoded paths, assumed tools, no configuration.

### 2. Tool vs problem confusion

"I want to build a plugin that uses hooks" — you picked a tool before you identified the problem. Start with the pain, not the tech.

### 3. Scope creep at ideation time

Your one-sentence idea grew into seven sentences of features. Trim back to the core pain before building.

### 4. Engineering-exercise plugins

You're building it to learn hooks / MCP / subagents, not to solve a problem. Fine as a learning project, but don't publish it as a plugin.

### 5. Already-solved

Someone shipped this 6 months ago. You didn't check. You're duplicating work.

### 6. One-off dressed as repeatable

"I need to migrate this codebase from React 17 to 18" is a one-off. A plugin is the wrong container — use a detailed prompt or a subagent for a single run.

### 7. Shiny technology

"New Claude Code feature X just dropped, let me make a plugin using it" — backwards. Start with the problem, then see if feature X fits.

---

## From idea to hand-off

Once an idea passes the checklist:

1. **Write the one-sentence problem statement.** "When I [trigger], I want [behavior], so that [outcome]."
2. **Hand off to `plugin-research`** to confirm nothing already solves it and to gather authoritative references.
3. **Hand off to `plugin-architecture`** to decide the component decomposition.
4. **Hand off to `skill-foundry` / `plugin-hooks` / `plugin-composition`** to build.
5. **Hand off to `plugin-evaluation`** to measure whether it works.
6. **Hand off to `plugin-validation`** to ensure it ships valid.

The lifecycle: ideate → research → architect → build → evaluate → validate. This skill is step 1 of 6.

---

## References

| File | Contents |
|---|---|
| `references/problem-worthy-checklist.md` | The 7 criteria with examples, counter-examples, and a scoring template |
| `references/ideation-anti-patterns.md` | The 7 anti-patterns above, expanded with case studies and "fix by" instructions |

---

> *Plugin-Dev Authoring Toolkit by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
