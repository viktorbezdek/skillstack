# Systems Thinking

> **v1.0.10** | Strategic Thinking | 11 iterations

Apply systems thinking principles including feedback loops, leverage points, and system dynamics to analyze complex problems.

## What Problem Does This Solve

Complex problems — declining user engagement, runaway costs, team burnout cycles — resist simple fixes because their causes are circular, not linear. Organizations apply solutions to visible symptoms without understanding the feedback loops sustaining the problem, causing fixes that fail or shift the burden elsewhere. This skill provides the causal loop notation, system archetypes, and leverage point analysis needed to identify where intervention actually changes system behavior rather than just treating symptoms.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "We keep solving this problem but it keeps coming back" | System archetype identification: Fixes that Fail (side effects undermine fix) or Shifting the Burden (symptomatic solution crowds out fundamental solution) |
| "Map the feedback loops driving this growth/decline pattern" | Causal loop notation (A--[+]-->B, A--[-]-->B) with Reinforcing and Balancing loop identification |
| "Where should we intervene to change this system?" | Meadows' 12 Leverage Points ranked by effectiveness, from Parameters (least powerful) up to Paradigms (most powerful) |
| "Why is our quick fix making things worse?" | Analysis workflow: Boundary Definition, Element Mapping, Relationship Identification, Loop Detection, and Leverage Point Analysis |
| "We're growing fast but hitting walls we didn't expect" | Limits to Growth archetype analysis identifying the constraining feedback loop that caps the reinforcing growth loop |
| "How do I avoid making the wrong diagnosis of a system?" | Common pitfalls: linear thinking, event focus (symptoms vs. structures), boundary errors (too narrow/wide), and delay blindness |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/systems-thinking
```

## How to Use

**Direct invocation:**

```
Use the systems-thinking skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `systems`
- `feedback-loops`
- `leverage-points`

## What's Inside

- **Core Concepts** -- Reinforcing (positive) and Balancing (negative) feedback loop definitions with examples, plus Meadows' 12 Leverage Points ranked from Parameters (least powerful) to Paradigms (most powerful).
- **Analysis Workflow** -- Five-step process: Boundary Definition, Element Mapping, Relationship Identification, Loop Detection, and Leverage Point Analysis.
- **Causal Loop Notation** -- Standard notation for representing same-direction (+) and opposite-direction (-) causal links, with R (Reinforcing) and B (Balancing) loop labels.
- **Common Pitfalls** -- Four diagnostic errors to avoid: linear thinking (ignoring feedback), event focus (symptoms vs. structures), boundary errors (scope too narrow or wide), and delay blindness.

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
- **[Outcome Orientation](../outcome-orientation/)** -- Focus on measurable outcomes using OKRs, results-driven thinking, and outcome vs output distinction.
- **[Prioritization](../prioritization/)** -- Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making.
- **[Risk Management](../risk-management/)** -- Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 50 production-grade plugins for Claude Code.
