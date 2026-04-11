# Critical Intuition

> **v1.0.15** | Strategic Thinking | 16 iterations

Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with intuition-level depth.

## What Problem Does This Solve

Information is rarely presented at face value: a proposal leaves out its failure modes, a status update is technically accurate but strategically misleading, a decision looks reasonable until you notice what's conspicuously absent. Standard analysis takes content at face value and misses the subtext, meta-signals, and anomalies that experienced practitioners catch instinctively. This skill provides a structured seven-step process for multi-level reading, signal detection, fallacy identification, Bayesian reasoning, and intuitive synthesis — making the tacit analytical moves of domain experts explicit and repeatable.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "What am I missing in this proposal / plan / argument?" | Gap analysis and anomaly detection: what information would normally be present but isn't, and why that absence is meaningful |
| "Read between the lines — what's really going on here?" | Three-level reading framework: surface (explicit facts), subtext (implied assumptions and omissions), and meta (incentives, power dynamics, why it's framed this way) |
| "Are there red flags in this?" | Red flag cluster detection: multiple small concerns, coincidence accumulation, pattern breaks, and trajectory sensing for early warning |
| "Analyze this argument critically" | Structured argument analysis: premise/conclusion mapping, formal and informal fallacy detection, evidence quality evaluation, motivated reasoning identification |
| "What's my confidence level on this? Am I being overconfident?" | Bayesian reasoning framework: prior probability, evidence strength assessment, updated probability, and confidence calibration with explicit "what would change my mind" checks |
| "I have a gut feeling something is wrong but can't articulate it" | Intuitive synthesis methodology: gestalt perception, cross-domain analogical reasoning, tacit pattern matching, and metacognitive bias checks |

## When NOT to Use This Skill

- generating new creative solutions, brainstorming, or strategic reframing -- use [creative-problem-solving](../creative-problem-solving/) instead

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install critical-intuition@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the critical-intuition skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `pattern-recognition`
- `bayesian-reasoning`
- `analysis`

## What's Inside

- **When to Use This Skill** -- Trigger phrases and analytical contexts: reading between lines, critical analysis requests, red flag detection, hidden pattern identification, and judgment under uncertainty.
- **Core Approach** -- Six-phase pattern: surface analysis, deep reading, pattern detection, critical evaluation, intuitive synthesis, and judgment formation.
- **Analysis Process** -- Seven detailed steps covering multi-level reading, signal and anomaly detection, critical reasoning with fallacy identification, probabilistic assessment, intuitive synthesis, early warning detection, and judgment formation.
- **Workflow** -- Six operational steps for executing critical intuition: initial understanding, reference loading, multi-level analysis, critical evaluation, intuitive synthesis, and judgment with actionable recommendations.
- **Validation Checks** -- Eight pre-completion checks ensuring full analytical coverage before finalizing judgment, including bias checks and confidence calibration.

## Version History

- `1.0.15` fix(thinking): disambiguate creative-problem-solving vs critical-intuition (6e73dfc)
- `1.0.14` fix: update plugin count and normalize footer in 31 original plugin READMEs (3ea7c00)
- `1.0.13` fix: change author field from string to object in all plugin.json files (bcfe7a9)
- `1.0.12` fix: rename all claude-skills references to skillstack (19ec8c4)
- `1.0.11` refactor: remove old file locations after plugin restructure (a26a802)
- `1.0.10` docs: update README and install commands to marketplace format (af9e39c)
- `1.0.9` refactor: restructure all 34 skills into proper Claude Code plugin format (7922579)
- `1.0.8` refactor: make each skill an independent plugin with own plugin.json (6de4313)
- `1.0.7` docs: add detailed README documentation for all 34 skills (7ba1274)
- `1.0.6` refactor: standardize frontmatter and split oversized SKILL.md files (4a21a62)

## Related Skills

- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough solutions through lateral thinking, first principles reasoning, game theory, and strategic reframi...
- **[Outcome Orientation](../outcome-orientation/)** -- Focus on measurable outcomes using OKRs, results-driven thinking, and outcome vs output distinction.
- **[Prioritization](../prioritization/)** -- Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making.
- **[Risk Management](../risk-management/)** -- Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices.
- **[Systems Thinking](../systems-thinking/)** -- Apply systems thinking principles including feedback loops, leverage points, and system dynamics to analyze complex prob...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
