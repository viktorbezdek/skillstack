---
name: systems-thinking
description: >-
  Analyze complex problems through feedback loops, system dynamics, causal relationships,
  and leverage points to understand WHY a system behaves the way it does. Use when the
  user asks to map feedback loops, trace causal chains, identify why a problem keeps
  recurring, find leverage points for change, analyze emergent behavior, or understand
  a complex system before intervening. NOT for generating creative solutions (use
  creative-problem-solving). NOT for stress-testing specific assumptions (use
  critical-intuition). NOT for structured risk registers or mitigation plans (use
  risk-management).
---

# Systems Thinking

Analyze complex systems through feedback loops, leverage points, and system dynamics.

## When to use this skill

- A problem keeps recurring despite repeated fixes — suspect a feedback loop
- You need to understand WHY a system behaves the way it does before intervening
- Intervening in one area might cause unintended consequences elsewhere
- You're trying to find the highest-leverage point to change a system
- Multiple stakeholders see the same problem differently and you need to reconcile views

## When NOT to use this skill

- **Generating novel solutions** → use `creative-problem-solving`
- **Stress-testing assumptions** → use `critical-intuition`
- **Building risk registers and mitigation plans** → use `risk-management`
- **Prioritizing which problem to solve first** → use `prioritization`
- **Simple cause-and-effect problems** → straightforward analysis suffices; systems thinking adds overhead without value when there are <3 interacting variables

---

## Decision tree

```
How many interacting variables are involved?
  1-2 → Systems thinking is overkill; use direct analysis
  3+ → Continue

Is the problem recurring (keeps coming back)?
  YES → Feedback loop likely; map the loop → identify leverage points
  NO  → Is the problem about unintended consequences of an intervention?
    YES → "Fixes that Fail" archetype; trace side effects
    NO  → Is the system hitting limits despite initial success?
      YES → "Limits to Growth" archetype; identify the constraining factor
      NO  → Use general causal loop analysis

What's your goal?
  Understand WHY → Map feedback loops, identify dominant loops
  Find where to intervene → Apply Meadows' leverage points (start at 12, work down)
  Predict behavior → Identify delays, stocks, and flows; trace system dynamics
```

### Leverage Point Selection

```
What type of change are you considering?
│
├─ Changing a number (budget, headcount, threshold)
│   └─ Level 1 (Parameters) — least effective; ask first: "what rule change would make this number irrelevant?"
│
├─ Changing physical structure (org chart, technology, node layout)
│   └─ Level 2 (Structure) — modest; good for removing bottlenecks
│
├─ Adding/removing buffers (inventory, slack time, reserves)
│   └─ Level 3 (Buffer sizes) — stabilizing but doesn't change dynamics
│
├─ Changing delays (feedback speed, reporting cadence)
│   └─ Level 5 (Delays) — powerful when the system oscillates from lag
│
├─ Strengthening/weakening feedback loops
│   └─ Level 6-7 (Balancing/Reinforcing loops) — changes system dynamics directly
│
├─ Changing information flows (who sees what data)
│   └─ Level 8 (Information flows) — often the cheapest high-leverage intervention
│
├─ Changing rules (incentives, constraints, permissions)
│   └─ Level 9 (Rules) — high leverage; rules determine who can do what
│
├─ Enabling self-organization (letting the system evolve its own structure)
│   └─ Level 10 (Self-organization) — very high leverage but requires trust
│
├─ Changing the system goal
│   └─ Level 11 (Goals) — transforms what the system optimizes for
│
└─ Changing the paradigm (mental model underlying the system)
    └─ Level 12 (Paradigms) — most powerful, rarest; reframes everything
```

---

## Core Concepts

### Feedback Loops

**Reinforcing (Positive) Loops**: Amplify change in one direction
```
Growth → Success → More Resources → More Growth
```

**Balancing (Negative) Loops**: Seek equilibrium
```
Temperature ↑ → Thermostat → Cooling → Temperature ↓
```

### Meadows' 12 Leverage Points

Intervention points ranked by effectiveness (most to least powerful):

| Level | Leverage Point | Example |
|-------|----------------|---------|
| 12 | Paradigms | Mental models underlying the system |
| 11 | Goals | System purpose and direction |
| 10 | Self-organization | Ability to evolve structure |
| 9 | Rules | Incentives, constraints, permissions |
| 8 | Information flows | Who has access to what data |
| 7 | Reinforcing loops | Amplifying feedback |
| 6 | Balancing loops | Stabilizing feedback |
| 5 | Delays | Time between action and response |
| 4 | Material stocks/flows | Physical resources |
| 3 | Buffer sizes | Stabilizing capacity |
| 2 | Structure | Physical connections |
| 1 | Parameters | Numbers and constants |

**Rule**: Changing parameters (level 1) is the most common intervention and the least effective. Changing paradigms (level 12) is the rarest intervention and the most effective.

### System Archetypes

| Archetype | Pattern | Intervention |
|-----------|---------|--------------|
| **Fixes that Fail** | Quick fix creates side effects that worsen the original problem | Address the fundamental cause instead of the symptom |
| **Shifting the Burden** | Symptomatic solution undermines the fundamental solution | Invest in the fundamental solution; use symptomatic relief only as a bridge |
| **Limits to Growth** | Initial success hits a constraining factor | Identify and remove the limit before growth stalls |
| **Tragedy of the Commons** | Individual benefit depletes shared resource | Add feedback (information, rules, or allocation) that makes the shared cost visible |

## Analysis Workflow

1. **Boundary Definition**: Scope, internal vs external, timescale
2. **Element Mapping**: Variables, stocks, flows
3. **Relationship Identification**: Causal connections, +/- classification
4. **Loop Detection**: Feedback paths, dominant loops
5. **Leverage Point Analysis**: High-impact intervention points
6. **Archetype Check**: Does the system match a known pattern?

## Causal Loop Notation

```
A --[+]--> B   (same direction)
A --[-]--> B   (opposite direction)
R = Reinforcing, B = Balancing
```

## Anti-Patterns with Solutions

1. **Linear thinking** — treating a system as a one-way chain when B→A feedback exists.
   - **Solution**: always check for reverse causality after mapping a forward link. Ask: "does the effect loop back to influence the cause?"

2. **Event focus** — reacting to events (symptoms) instead of addressing the underlying structure.
   - **Solution**: ask "why did this happen?" at least three times before proposing a fix. If the answer at level 3 is different from level 1, you have a structural problem.

3. **Boundary errors** — drawing the system boundary too narrow (misses key interactions) or too wide (loses focus).
   - **Solution**: start narrow, expand only when the model fails to explain observed behavior. A good model has 6-10 variables and 2-3 dominant loops.

4. **Delay blindness** — ignoring the time lag between action and response, leading to overcorrection.
   - **Solution**: explicitly label delays in every causal loop diagram. Ask: "how long between this action and its effect?"

5. **Parameter obsession** — tweaking numbers (level 1 leverage) instead of changing goals, rules, or information flows.
   - **Solution**: before adjusting a parameter, ask "what rule or goal change would make this parameter irrelevant?" If the answer exists, the parameter change is low-leverage.

6. **Intervening without understanding** — "something must be done" without first mapping the feedback loops.
   - **Solution**: always complete the analysis workflow (boundary → elements → relationships → loops → leverage) before proposing interventions. The map must exist before you navigate.
