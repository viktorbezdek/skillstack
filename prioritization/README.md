# Prioritization

> **v1.0.10** | Strategic Thinking | 11 iterations

Apply prioritization frameworks including RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making.

## What Problem Does This Solve

Teams routinely work on the wrong things — building features that affect few users, pursuing initiatives driven by the loudest voice rather than evidence, or treating all backlog items as equally important. Without structured scoring, prioritization defaults to gut feel, seniority, or whoever pushed hardest last sprint. This skill provides quantitative frameworks that replace opinion-based debates with calculated scores grounded in reach, impact, confidence, and effort.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "Help me score and rank these feature ideas" | RICE scoring (Reach x Impact x Confidence / Effort) with a structured template to calculate and compare numeric scores |
| "What must we ship vs. what can we cut from this release?" | MoSCoW categorization (Must/Should/Could/Won't) with the 60% rule to prevent Must items from consuming the entire effort budget |
| "I need a quick way to rank initiatives without much data" | ICE scoring averaging Impact, Confidence, and Ease on a 1-10 scale for fast relative ranking |
| "Which items give us the best return for the least work?" | Effort-Impact matrix plotting Quick Wins, Big Bets, Fill Ins, and Money Pits for visual prioritization |
| "Someone keeps pushing for this pet project — how do I push back?" | Anti-patterns catalog covering HiPPO, recency bias, squeaky wheel, and sunk cost to name and defuse common traps |
| "Help me document the rationale for why we chose this priority" | Prioritization template with RICE factors, calculated score, priority level, and written rationale |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/prioritization
```

## How to Use

**Direct invocation:**

```
Use the prioritization skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `rice`
- `moscow`
- `ice`
- `prioritization`

## What's Inside

- **RICE Scoring** -- Formula-based scoring using Reach, Impact (0.25-3 scale), Confidence percentage, and Effort in person-months to produce a comparable numeric priority score.
- **MoSCoW Method** -- Four-tier classification (Must/Should/Could/Won't) with the guideline that Must items cannot exceed 60% of total effort.
- **ICE Scoring** -- Lightweight three-factor scoring (Impact + Confidence + Ease / 3) for rapid ranking when full RICE data isn't available.
- **Effort-Impact Matrix** -- Visual 2x2 matrix sorting items into Quick Wins, Big Bets, Fill Ins, and Money Pits with a recommended priority order.
- **Prioritization Template** -- Structured Markdown template capturing RICE factors, calculated score, decision, and written rationale for each item.
- **Anti-Patterns** -- Named traps to recognize and counter: HiPPO (highest-paid person's opinion), recency bias, squeaky wheel, and sunk cost reasoning.

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
- **[Risk Management](../risk-management/)** -- Apply risk assessment frameworks, mitigation strategies, risk registers, and monitoring practices.
- **[Systems Thinking](../systems-thinking/)** -- Apply systems thinking principles including feedback loops, leverage points, and system dynamics to analyze complex prob...

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
