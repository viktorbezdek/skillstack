> **v1.0.15** | Strategic Thinking | 16 iterations

# Critical Intuition

> Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis that reads between the lines -- the analytical complement to creative problem-solving.

## The Problem

When someone presents a plan, a proposal, or a decision, the natural response is to engage with what is explicitly stated. Teams evaluate the arguments on the surface, check the numbers that are presented, and assess the logic of the stated reasoning. But the most important information is often what is not said: the assumptions embedded so deeply they are invisible, the data conspicuously absent from the analysis, the incentive structures driving the framing, and the subtle signals that something does not fit.

This is how bad decisions get made by smart people. A vendor proposal looks compelling because the comparison omits the criteria where the vendor is weakest. A technical plan seems sound because it addresses the obvious risks while ignoring the systemic ones. A quarterly report reads as positive because the narrative emphasizes growth metrics while burying the retention numbers. The surface-level analysis says "yes" but the deeper reading says "wait."

Most teams lack a systematic process for this kind of critical analysis. They rely on individual experience and gut feelings, which are inconsistent and hard to communicate. When someone says "something feels off about this proposal" they cannot articulate what specifically is wrong, which means the concern gets dismissed. And when nobody in the room has the pattern recognition to spot the issue, the concern never gets raised at all. Teams ship products with unexamined assumptions, sign contracts with hidden downsides, and commit to strategies with undetected contradictions -- not because they are careless, but because they have no structured approach to reading below the surface.

## The Solution

This plugin provides a seven-step analytical methodology that moves from surface-level reading through deep analysis, pattern detection, critical reasoning, probabilistic assessment, intuitive synthesis, and judgment formation. At each step, it draws on specific techniques from five reference libraries covering pattern recognition, critical thinking frameworks, early warning detection, synthesis methods, and extended analysis patterns.

The skill teaches multi-level reading: surface level (what is explicitly stated), subtext level (what is implied, what assumptions are embedded, what is conspicuously absent), and meta level (why is this being communicated this way, what are the incentives and constraints). It applies formal reasoning analysis (argument structure, fallacy detection, evidence evaluation), Bayesian probability assessment (prior beliefs updated with evidence strength), and gestalt synthesis (combining disparate signals into a coherent picture).

For early warnings and red flags, the skill identifies leading indicators (upstream signals, stress accumulation, resilience degradation), trajectory sensing (momentum shifts, inflection point detection, tipping point proximity), and red flag clusters (multiple small concerns that individually seem minor but collectively signal a problem). The result is not just "something feels off" but a precise articulation of what specifically is wrong and why it matters.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Evaluate proposals based on what is explicitly stated | Multi-level reading catches what is implied, hidden, or conspicuously absent |
| Accept reasoning at face value if the logic seems sound | Critical reasoning analysis detects hidden assumptions, informal fallacies, and motivated reasoning |
| "Something feels off" but cannot articulate what | Pattern detection and signal analysis produce specific, communicable concerns |
| Miss early warning signs until problems become crises | Leading indicators, trajectory sensing, and red flag clusters catch issues upstream |
| Gut feelings are inconsistent and get dismissed | Structured intuitive synthesis produces calibrated confidence judgments backed by evidence |
| No process for distinguishing signal from noise in complex situations | Bayesian assessment with multiple hypothesis testing and discriminating evidence identification |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install critical-intuition@skillstack
```

### Verify installation

After installing, test with:

```
Read between the lines on this vendor proposal -- something feels off but I can't put my finger on it
```

## Quick Start

1. Install the plugin using the commands above
2. Share something you want analyzed critically: `Analyze this product strategy -- what am I missing?`
3. The skill reads at multiple levels (surface facts, implied assumptions, meta-level framing) and identifies what is conspicuously absent
4. It detects patterns, anomalies, and red flag clusters that signal potential problems
5. You get a calibrated judgment with specific findings, confidence levels, and what would change the assessment

## What's Inside

| Component | Description |
|---|---|
| `critical-intuition` skill | Core skill with the seven-step analytical methodology: multi-level reading, signal detection, critical reasoning, probabilistic assessment, intuitive synthesis, early warning detection, and judgment formation |
| 5 reference libraries | Pattern recognition, critical thinking, sixth sense and early warnings, synthesis frameworks, and extended patterns with advanced techniques |
| 13 trigger eval cases | Validates correct skill activation and near-miss rejection |
| 3 output eval cases | Tests pattern detection, critical analysis depth, and judgment quality |

### critical-intuition

**What it does:** Activates when you need to analyze something critically, detect what is hidden or implied, identify red flags and early warnings, evaluate reasoning rigor, or form judgments under uncertainty. Provides structured analytical depth that goes beyond surface-level evaluation.

**Try these prompts:**

```
Read between the lines on this email from our biggest client -- they say everything is fine but I sense a problem
```

```
What am I missing in this technical design? It looks sound but my gut says we're overlooking something
```

```
Analyze this competitor's strategy announcement critically -- what are they really saying and what aren't they saying?
```

```
I have a feeling our project timeline is at risk despite all green status reports -- help me identify the early warning signs
```

```
We're about to make a major hiring decision between two candidates -- help me detect the subtle signals I might be missing in their interview feedback
```

**Key references:**

| Reference | Topic |
|---|---|
| `pattern-recognition.md` | Advanced pattern detection, multi-level reading techniques, anomaly identification, and signal-to-noise separation |
| `critical-thinking.md` | Argument analysis, fallacy detection, evidence evaluation frameworks, and reasoning rigor assessment |
| `sixth-sense.md` | Subtle signal detection, leading indicators, trajectory sensing, tipping point proximity, and red flag clusters |
| `synthesis-frameworks.md` | Information integration, Bayesian synthesis, decision under uncertainty, and metacognitive calibration |
| `extended-patterns.md` | Advanced techniques for reading between lines, sixth sense development, critical questioning, bias mitigation, and output format templates |

## Real-World Walkthrough

You are a VP of Engineering evaluating a proposal from your infrastructure team to migrate from AWS to Google Cloud. The proposal is 15 pages long, well-structured, with cost comparisons, timeline estimates, risk assessments, and a detailed migration plan. On the surface, it looks thorough and compelling -- the projected savings are 30% annually, the timeline is 9 months, and the risk section identifies and addresses the major concerns. Your CTO is enthusiastic. But something nags at you.

You open Claude Code and share the key sections:

```
Analyze this cloud migration proposal critically. The numbers look good and the plan seems thorough but something feels off and I can't articulate what. Read between the lines for me.
```

The critical-intuition skill activates and begins with multi-level reading.

**Surface level:** The proposal states a 30% cost reduction, 9-month timeline, 3-person dedicated team, and low risk of service disruption. The comparison shows GCP winning on 8 of 12 evaluation criteria.

**Subtext level:** The skill identifies several conspicuous absences. The cost comparison includes compute and storage but does not mention egress costs, which are notoriously high during migration. The 9-month timeline assumes no feature development freeze, but the proposal does not address how the migration team will handle ongoing production changes to the systems being migrated. The risk section covers technical risks (data loss, downtime) but omits organizational risks (team ramp-up on GCP, loss of AWS-specific institutional knowledge, impact on hiring pipeline for AWS-experienced candidates).

**Meta level:** The skill examines why this proposal is being made now. It notes that the infrastructure team's annual review is in two months, and a major migration project would significantly strengthen their visibility and headcount justification. This does not mean the proposal is wrong, but it means the framing is optimistic by default -- the team has strong incentives to present the most favorable case.

**Pattern detection:** The skill identifies a pattern in the cost projections: they assume current usage levels grow linearly. But your company grew 3x last year. At 3x scale, the GCP pricing tiers shift significantly. The skill calculates that at 3x current usage, the savings drop from 30% to 11%. At 5x, GCP is actually more expensive because of their pricing structure for high-volume compute.

**Anomaly detection:** The 12-criteria comparison rates GCP higher on "managed services ecosystem." But the proposal's own migration plan lists 4 critical AWS-specific managed services (Aurora, SQS, CloudFront, Lambda@Edge) that have no direct GCP equivalents and would need to be replaced with different architectural patterns. The comparison criterion and the migration plan contradict each other.

**Red flag cluster:** Individually, each finding is minor. But clustered together -- omitted egress costs, unaddressed feature development conflicts, organizational incentive bias, growth-blind cost projections, and self-contradicting evaluation criteria -- they form a pattern suggesting the proposal was built backward from the conclusion rather than forward from the evidence.

**Bayesian assessment:** The skill's prior for "cloud migration saves 30% annually" given industry data is about 15% (most migrations save less than projected due to unforeseen costs). The evidence in this proposal does not update that prior upward because the cost analysis has significant gaps. Updated probability of achieving 30% savings: roughly 10-15%.

**Judgment formation:** The migration may still be worthwhile for non-cost reasons (technical capabilities, team preference, strategic alignment), but the financial case is substantially weaker than presented. The skill recommends requesting: a cost analysis including egress fees and growth projections at 3x and 5x, a parallel-development plan for the 9-month migration window, and an independent review by someone outside the infrastructure team.

You present these specific, evidenced concerns to the CTO. The infrastructure team revises the proposal. The updated cost analysis shows 14% savings (not 30%), the timeline extends to 14 months with parallel development, and the team acknowledges two GCP service gaps requiring architectural changes. The project proceeds, but with realistic expectations and proper planning. Your "gut feeling" was right -- the skill just helped you articulate exactly what was wrong.

## Usage Scenarios

### Scenario 1: Evaluating a vendor proposal

**Context:** You received a detailed proposal from a SaaS vendor. The sales team is pushing for a quick decision. The proposal looks good but you want to ensure you are not missing hidden downsides.

**You say:** `Read between the lines on this vendor proposal -- I want to know what they're not telling me`

**The skill provides:**
- Multi-level reading: surface claims, implied limitations, conspicuous absences
- Incentive analysis: what the vendor is motivated to emphasize vs downplay
- Gap detection: what information is missing that you should request before deciding
- Red flag identification: pricing structures, lock-in clauses, SLA ambiguities

**You end up with:** A specific list of concerns to investigate and questions to ask the vendor before proceeding.

### Scenario 2: Sensing project risk despite green status

**Context:** Your project status reports show green across all workstreams, but you have a nagging sense that the team is behind. You cannot point to any specific data point.

**You say:** `All our status reports are green but I feel like we're heading for trouble -- help me identify the early warning signs I might be sensing`

**The skill provides:**
- Leading indicator analysis: what signals appear before status turns yellow?
- Stress accumulation detection: increased overtime, declining code review quality, growing tech debt
- Trajectory sensing: is velocity stable, increasing, or subtly declining?
- Red flag cluster mapping: which "minor" issues might collectively indicate a systemic problem?

**You end up with:** Specific metrics to check and questions to ask that will either confirm or dispel your concern with evidence.

### Scenario 3: Analyzing a competitor's public statements

**Context:** Your main competitor announced a "strategic pivot" in their latest earnings call. You need to understand what they are really doing and what it means for your market position.

**You say:** `Our competitor just announced a 'strategic pivot to enterprise' -- analyze what they're really saying and what it means for us`

**The skill provides:**
- Meta-level reading: why announce this publicly? What is the intended audience?
- Gap analysis: what did they not say? Which products or markets went unmentioned?
- Pattern matching: does this match known patterns of companies in similar situations (growth stall, market retreat, repositioning)?
- Probability assessment: likelihood of different interpretations with discriminating evidence

**You end up with:** A range of interpretations with calibrated probabilities and specific signals to watch that would confirm which interpretation is correct.

### Scenario 4: Evaluating team member signals

**Context:** A key engineer's behavior has changed subtly over the past month. Their work quality is still good but something seems different. You want to understand what you are sensing before it becomes a problem.

**You say:** `My senior engineer seems different lately -- work is still good but something's off. Help me articulate what I might be picking up on`

**The skill provides:**
- Micro-signal analysis: what behavioral changes are significant vs noise?
- Pattern matching: common patterns that precede disengagement, burnout, or departure
- Gap analysis: what interactions or behaviors have stopped or changed?
- Action framework: how to investigate without being intrusive, and when to have a direct conversation

**You end up with:** A structured assessment of what the behavioral changes might mean and a concrete approach for addressing it.

## Ideal For

- **Leaders making high-stakes decisions** who need to see past well-crafted presentations to the reality underneath
- **Engineers evaluating technical proposals** where the surface analysis looks sound but experience says something is missing
- **Product managers assessing market signals** from competitors, customers, or usage data where the important information is in what is not said
- **Anyone with a "gut feeling" about a situation** who needs help transforming intuition into specific, communicable analysis
- **Teams building a culture of critical thinking** who want a structured methodology for questioning assumptions and detecting blind spots

## Not For

- **Generating new creative solutions** or brainstorming from scratch -- use [creative-problem-solving](../creative-problem-solving/) instead
- **Systematic risk assessment** with probability matrices and mitigation planning -- use [risk-management](../risk-management/) instead
- **Prioritizing work items** or deciding what to build -- use [prioritization](../prioritization/) instead

## How It Works Under the Hood

The plugin is a single-skill architecture with five reference libraries providing analytical depth.

The **core skill** (`SKILL.md`) defines a seven-step analytical methodology: multi-level reading (surface, subtext, and meta levels), signal detection (pattern recognition, anomaly detection, micro-signals, gap analysis), critical reasoning (argument structure, fallacy detection, evidence evaluation), probabilistic assessment (Bayesian updating, multiple hypotheses, confidence calibration), intuitive synthesis (gestalt perception, cross-domain connections, tacit knowledge integration), early warning detection (leading indicators, trajectory sensing, red flag clusters), and judgment formation (information integration, decision under uncertainty, metacognitive calibration). It includes validation checks to ensure analytical rigor before finalizing any judgment.

The five **reference libraries** provide technique depth on demand:
- **Pattern recognition** -- advanced detection techniques, multi-level reading methods, anomaly identification, and signal-to-noise separation for complex analytical situations
- **Critical thinking** -- argument analysis, formal and informal fallacy detection, evidence evaluation frameworks, and statistical reasoning assessment
- **Sixth sense** -- subtle signal detection, leading indicator identification, trajectory sensing, tipping point proximity assessment, and red flag cluster analysis for early warning
- **Synthesis frameworks** -- information integration methods, Bayesian synthesis, decision under uncertainty, and metacognitive calibration techniques
- **Extended patterns** -- advanced reading-between-lines techniques, sixth sense development, critical questioning frameworks, bias mitigation strategies, and structured output format templates

The skill explicitly routes to creative-problem-solving when the user needs to generate new ideas rather than analyze existing ones.

## Related Plugins

- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough solutions through lateral thinking, first principles, game theory, and strategic reframing
- **[Risk Management](../risk-management/)** -- Systematic risk assessment with probability matrices, mitigation strategies, and monitoring
- **[Systems Thinking](../systems-thinking/)** -- Analyze complex problems through feedback loops, leverage points, and system dynamics
- **[Prioritization](../prioritization/)** -- Apply RICE, MoSCoW, ICE, and effort-impact matrices for decision-making

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
