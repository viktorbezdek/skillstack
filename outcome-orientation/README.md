# Outcome Orientation

> **v1.0.10** | Strategic Thinking | 11 iterations

Focus on measurable outcomes using OKRs, results-driven thinking, and outcome vs output distinction.

## What Problem Does This Solve

Teams routinely confuse delivering outputs — features shipped, meetings held, documents written — with achieving outcomes that actually matter to users and the business. This disconnect means roadmaps fill with activity that looks productive but moves no meaningful metrics. This skill provides the frameworks (OKRs, results chains, leading/lagging metrics) and the "so what?" discipline needed to define goals in terms of measurable change rather than completed tasks.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Help me write OKRs for my team" | OKR structure template with Objective and Key Results table (baseline/target/current), plus good vs bad OKR examples |
| "How do I know if my goal is an output or an outcome?" | Outputs vs outcomes comparison table and the "so what?" chain to trace activities to real value |
| "What metrics should I track to measure product success?" | Outcome metrics table with lagging results (revenue, NPS, defect rate) paired with leading predictors (pipeline, activation rate, test coverage) |
| "My roadmap is full of features but leadership wants to see business impact" | Results chain model mapping Activities → Outputs → Outcomes → Impact |
| "How do I write a Key Result that's actually measurable?" | Outcome definition checklist: end-state description, measurability, time-bound scope, user/business value, and achievability |
| "We completed everything we planned but the metric didn't move — what went wrong?" | Outputs vs outcomes framing to diagnose whether the work was tied to the right leading indicators |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/outcome-orientation
```

## How to Use

**Direct invocation:**

```
Use the outcome-orientation skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `okrs`
- `outcomes`
- `metrics`

## What's Inside

- **Outcomes vs Outputs** -- Side-by-side table contrasting output activities with the outcomes they should drive, plus the "so what?" question chain
- **OKR Framework** -- OKR structural definition and a fill-in template with Objective, Key Results table, and Initiatives section; includes good vs bad OKR comparison
- **Outcome Metrics** -- Four metric categories (revenue, adoption, quality, satisfaction) each with a lagging result metric paired with its leading predictor
- **Results Chain** -- Four-stage model (Activities → Outputs → Outcomes → Impact) for tracing work to business change
- **Outcome Definition Checklist** -- Five criteria for validating that a goal qualifies as a genuine outcome rather than an activity

## Version History

- `1.0.10` fix(strategy+ux): optimize descriptions for outcome, prioritization, risk, systems, journey, ux-writing (9661735)
- `1.0.9` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.8` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.7` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.6` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.5` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.4` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.3` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.2` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)
- `1.0.1` docs: improve strategic skill descriptions (f59b24a)

## Related Skills

- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough solutions through lateral thinking, first principles reasoning, game theory, and strategic reframi...
- **[Critical Intuition](../critical-intuition/)** -- Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with intuition-level depth.
- **[Prioritization](../prioritization/)** -- Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making.
- **[Risk Management](../risk-management/)** -- Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices.
- **[Systems Thinking](../systems-thinking/)** -- Apply systems thinking principles including feedback loops, leverage points, and system dynamics to analyze complex prob...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
