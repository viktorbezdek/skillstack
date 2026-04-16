> **v1.0.15** | Strategic Thinking | 16 iterations

# Critical Intuition

> Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with intuition-level depth -- pattern recognition, bias detection, Bayesian reasoning, red flag identification, and reading between the lines.
> Single skill + 5 reference documents | 13 trigger evals, 3 output evals

## The Problem

Important decisions fail not because the analysis was wrong, but because critical information was hiding in plain sight. A proposal passes review because nobody asked what was conspicuously absent. A partnership agreement looks favorable until someone notices the incentive structure guarantees misalignment. A technical architecture gets approved because the team evaluated what was presented without questioning what was not.

The gap is not intelligence -- it is analytical depth. Surface-level analysis catches obvious problems. But the most dangerous failures come from subtext (what is implied but not stated), anomalies (what does not fit the pattern), and hidden dynamics (power structures, incentive misalignments, unstated constraints). These require a different kind of analysis: multi-level reading that examines surface, subtext, and meta layers simultaneously. Most people default to surface-level evaluation because deeper reading is cognitively expensive and there is no systematic process for it.

The cost compounds silently. A team that misses one red flag makes a decision that creates three more hidden problems. By the time the failure is visible, the root cause is buried under layers of subsequent decisions. Retroactively, everyone says "we should have seen that coming" -- and they are right, because the signals were there. They just were not reading at the right level.

## The Solution

This plugin provides a seven-step analytical process that moves from surface reading through deep signal detection, critical reasoning, probabilistic assessment, intuitive synthesis, early warning detection, to judgment formation. It is backed by five comprehensive reference documents covering pattern recognition, critical thinking frameworks, sixth sense and early warning signals, synthesis frameworks, and extended patterns for advanced techniques.

The skill teaches multi-level reading (surface, subtext, meta), signal detection (patterns, anomalies, micro-signals, gaps), critical reasoning (argument analysis, fallacy detection, evidence evaluation), probabilistic assessment (Bayesian thinking, multiple hypotheses, confidence calibration), and intuitive synthesis (gestalt perception, cross-domain connections, tacit knowledge). It provides red and green flag catalogs, output format templates, and validation checks to ensure analysis is thorough before forming judgments.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Evaluate proposals at face value; miss what is conspicuously absent or implied | Multi-level reading at surface, subtext, and meta layers; gap analysis catches what was not said |
| Accept evidence without evaluating source credibility or confounding factors | Critical reasoning framework evaluates argument structure, detects fallacies, and assesses evidence quality |
| Form opinions based on initial impressions without calibrating confidence | Bayesian reasoning updates beliefs with evidence, generates alternative hypotheses, and calibrates confidence |
| Discover problems only after they become visible failures | Early warning detection identifies leading indicators, stress accumulation, and red flag clusters before tipping points |
| Analysis stays within a single domain; miss cross-domain patterns | Intuitive synthesis connects analogical reasoning, structural similarities, and principle transfer across domains |
| Cognitive biases go unchecked; confirmation bias reinforces initial readings | Explicit metacognitive checks for biases, blind spots, and what would change the conclusion |

## Context to Provide

Critical analysis works at the subtext and meta levels -- which requires actual content to analyze. "What do you think about this?" with no document produces surface-level observations. Sharing the actual artifact (term sheet, proposal, architecture doc, competitor announcement, conversation transcript) enables the multi-level reading that surfaces what is hidden.

**What to include in your prompt:**
- **The artifact itself** -- paste the actual document, proposal, email, announcement, or conversation transcript; the skill reads between the lines, which requires actual lines to read
- **What you are trying to understand** -- the real question behind the surface question (not "is this deal good?" but "what does their urgency signal about their position?")
- **Your gut feeling if you have one** -- the skill is designed to articulate what intuition is detecting but cannot express; sharing "something feels off" is useful input, not noise
- **The relevant context** (who the parties are, what their incentives are, what has happened recently)
- **Your current interpretation** -- what you currently believe, so the skill can stress-test it rather than confirm it

**What makes results better:**
- Pasting the full document rather than paraphrasing it -- paraphrasing already filters out the signals
- Describing the stakes clearly (reversible/low-cost vs. irreversible/high-stakes changes the depth of analysis)
- Asking "what am I missing?" or "what could go wrong?" rather than "confirm this is good" -- the latter biases toward validation
- Specifying whose perspective to take (buyer, seller, employee, board member) for multi-stakeholder situations

**What makes results worse:**
- Asking for creative solutions -- this skill evaluates existing situations; use `creative-problem-solving` to generate alternatives
- Providing no artifact to analyze -- "what do you think about acquisitions generally?" is theory, not analysis
- Asking for validation instead of analysis ("tell me this is a good plan") -- confirmation bias corrupts the output

**Template prompt:**
```
Analyze [this document / proposal / announcement / situation] at multiple levels. I want to understand: what is explicitly stated, what is implied but not said, and what incentives or dynamics explain why it is being communicated this way. My current interpretation is [your read]. What am I missing, and what are the early warning signs I should watch for if I proceed?

[Paste the actual content here]
```

## Installation

Add the SkillStack marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install critical-intuition@skillstack
```

### Prerequisites

No additional dependencies. Pairs naturally with `creative-problem-solving` (generating ideas to analyze), `risk-management` (systematic risk assessment), and `systems-thinking` (understanding feedback loops in complex situations).

### Verify installation

After installing, test with:

```
Read between the lines on this vendor proposal -- what are they not telling us, and what incentives are driving their recommended approach?
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `"What am I missing in this architecture decision? The team is confident but something feels off."`
3. The skill activates and performs multi-level reading, identifying hidden assumptions and potential failure modes
4. Follow up with: `"What are the early warning signs I should watch for if we proceed?"`
5. The skill provides leading indicators and red flag clusters to monitor

---

## System Overview

```
critical-intuition (plugin)
└── critical-intuition (skill)
    ├── 7-step analysis process
    │   ├── Step 1: Multi-level reading (surface, subtext, meta)
    │   ├── Step 2: Signal detection (patterns, anomalies, micro-signals)
    │   ├── Step 3: Critical reasoning (arguments, fallacies, evidence)
    │   ├── Step 4: Probabilistic assessment (Bayesian, hypotheses)
    │   ├── Step 5: Intuitive synthesis (gestalt, cross-domain)
    │   ├── Step 6: Early warning detection (leading indicators, red flags)
    │   └── Step 7: Judgment formation (integration, metacognitive check)
    └── references/
        ├── pattern-recognition.md (advanced pattern detection, signal vs noise)
        ├── critical-thinking.md (argument analysis, logical structure, fallacies)
        ├── sixth-sense.md (subtle signal detection, micro-signals, early warnings)
        ├── synthesis-frameworks.md (multi-source synthesis, decision under uncertainty)
        └── extended-patterns.md (advanced techniques, red/green flag catalogs)
```

## What's Inside

| Component | Type | Description |
|---|---|---|
| `critical-intuition` | Skill | Seven-step analysis from surface reading to judgment formation |
| `pattern-recognition.md` | Reference | Advanced pattern detection, signal vs. noise discrimination, anomaly detection |
| `critical-thinking.md` | Reference | Argument analysis, logical structure, formal and informal fallacy detection |
| `sixth-sense.md` | Reference | Subtle signal detection, micro-signals, early warning systems, tipping points |
| `synthesis-frameworks.md` | Reference | Multi-source synthesis, information integration, decision under uncertainty |
| `extended-patterns.md` | Reference | Advanced reading-between-lines techniques, red/green flag catalogs, output templates |
| Trigger evals | Test suite | 13 trigger evaluation cases |
| Output evals | Test suite | 3 output quality evaluation cases |

### Component Spotlights

#### critical-intuition (skill)

**What it does:** Activates when users need rigorous analytical depth -- detecting hidden patterns, exposing blind spots, evaluating proposals, or reading between the lines. Provides a seven-step process from multi-level reading through signal detection, critical reasoning, probabilistic assessment, intuitive synthesis, early warning detection, to judgment formation.

**Input -> Output:** A situation, proposal, document, or decision to analyze -> Multi-level analysis revealing hidden dynamics, bias assessment, probabilistic judgment with confidence calibration, early warning indicators, and actionable implications.

**When to use:**
- Reading between the lines on proposals, communications, or situations
- Identifying what is missing, hidden, or unstated
- Critically evaluating arguments, evidence, or reasoning
- Detecting early warning signs or red flags
- Synthesizing complex information under uncertainty
- Risk assessment requiring deep pattern analysis

**When NOT to use:**
- Generating new creative solutions (use `creative-problem-solving`)
- Brainstorming or strategic reframing (use `creative-problem-solving`)
- First-principles reasoning about what to build (use `creative-problem-solving`)

**Try these prompts:**

```
Read between the lines on this vendor proposal. They're recommending a 3-year enterprise contract with $50K early termination penalties and a "technology roadmap alignment" clause I don't fully understand. What incentives are driving this structure and what does the alignment clause actually mean for us?

[paste the proposal text]
```

```
Our main competitor just open-sourced their core product -- the same product they've charged $200/seat for over three years. On the surface it looks like a strategic gift to us. What's the strategic game being played? What does this move signal about their position, and how should we respond?
```

```
My team presented this microservices migration plan with a 6-month timeline. The presentation was polished and they are confident, but something feels off -- the timeline has no contingency, and the data migration section was skipped in the presentation. What are the hidden risks and what questions should I ask?

[paste the architecture proposal]
```

```
I interviewed a senior engineer candidate. Technical interview was strong, resume checks out, but I have a persistent gut feeling something is wrong and I can't articulate it. Help me identify what my intuition might be detecting. Here's my interview notes.

[paste interview notes]
```

**Key references:**

| Reference | Topic |
|---|---|
| `pattern-recognition.md` | Advanced pattern detection, signal vs. noise, meta-patterns, anomaly detection |
| `critical-thinking.md` | Argument structure analysis, fallacy detection (formal, informal, statistical) |
| `sixth-sense.md` | Micro-signals, subtle energy shifts, timing variations, early warning systems |
| `synthesis-frameworks.md` | Multi-source synthesis, information integration, decision making under uncertainty |
| `extended-patterns.md` | Reading between lines, sixth sense development, red/green flag catalogs, output templates |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate) | Good (specific, activates reliably) |
|---|---|
| "What do you think?" | "Read between the lines on this email from our VP -- what's the real message behind the reorganization announcement?" |
| "Is this a good idea?" | "Analyze this acquisition target critically. The financials look clean but three board members just sold shares. What patterns do you see?" |
| "Help me decide" | "I have two conflicting data sources about market size. How should I weight them using Bayesian reasoning?" |
| "Find problems" | "What early warning signs should I watch for if we proceed with this migration? What are the leading indicators of failure?" |

### Structured Prompt Templates

**For reading between the lines:**
```
Analyze [this communication/proposal/document] at three levels: what is explicitly stated, what is implied but not said, and what incentives or power dynamics explain why it is being communicated this way.
```

**For detecting hidden risks:**
```
Our team is [confident/excited] about [decision]. Play devil's advocate: what are we not seeing? What assumptions are we making that could be wrong? What would need to be true for this to fail?
```

**For early warning monitoring:**
```
We're proceeding with [initiative]. What leading indicators should I monitor to detect problems early? What red flag clusters would signal we need to change course?
```

### Prompt Anti-Patterns

- **Asking for creative solutions:** "How should we solve this?" is a generation question. This skill analyzes existing situations and ideas. Use `creative-problem-solving` to generate, then this skill to evaluate.
- **Requesting validation instead of analysis:** "Confirm this is a good plan" biases the analysis toward agreement. Instead ask "What am I missing?" or "What could go wrong?"
- **Providing too little context:** "What do you think about our strategy?" gives the skill nothing to analyze at the subtext and meta levels. Share the actual document, proposal, or situation details.

## Real-World Walkthrough

**Starting situation:** You are CTO of a mid-stage startup. Your company is in acquisition talks with a larger company. The term sheet looks favorable -- premium valuation, retention packages, technical autonomy for 2 years. Your board is enthusiastic. Your CEO has scheduled the signing for next week. But something feels off and you cannot articulate what.

**Step 1: Multi-level reading.** You share the term sheet and ask: "Read between the lines on this acquisition offer. The terms look great but something feels wrong. Help me identify what."

The skill performs three-level analysis. Surface: generous premium, strong retention packages, autonomy guarantees. Subtext: the autonomy clause has a "consistent with parent company strategy" qualifier that could nullify it. The retention packages vest over 4 years but the autonomy guarantee is only 2 years -- meaning years 3-4 of retention have no autonomy protection. Meta: the acquiring company just lost a major product bet and needs your technology to fill the gap. The favorable terms are not generosity -- they are urgency. This affects negotiating position.

**Step 2: Signal detection.** The skill identifies anomalies: (1) the acquiring company's VP of Engineering was not in the meetings -- unusual for a technical acquisition, suggesting the deal is being driven by business strategy, not technical alignment. (2) The due diligence questions focused on customer list and revenue metrics, not technical architecture -- suggesting they value the business more than the technology. (3) The "consistent with parent company strategy" clause appeared in version 3 of the term sheet, not version 1 -- something changed internally.

**Step 3: Critical reasoning.** The skill examines the argument structure of the term sheet: "We value your technical autonomy" paired with a clause that allows overriding it. This is a formal contradiction. The retention packages assume continued autonomy (engineers stay because they have independence), but the term sheet allows removing the condition that makes retention work. The logical conclusion: the retention packages are structured to be exercised, not necessarily honored in spirit.

**Step 4: Probabilistic assessment.** Using Bayesian reasoning: the prior probability that post-acquisition autonomy survives 2+ years is approximately 25% based on industry data. The evidence (VP of Engineering absent, business-focused diligence, strategy-qualifier clause) updates this downward to approximately 10-15%. The tail risk is that your team leaves in years 3-4 when autonomy evaporates but before packages vest, leaving you with neither autonomy nor talent.

**Step 5: Early warning detection.** The skill provides red flag clusters to watch for if you proceed: (1) "alignment meetings" appearing on calendars within 3 months, (2) hiring freezes "until integration planning completes," (3) requests to use the parent company's development tools or processes, (4) your roadmap items being reprioritized to "support the broader platform." Any two of these in the first 6 months indicates autonomy erosion is accelerating.

**Step 6: Judgment formation.** The skill synthesizes: this is not a bad deal, but the real deal is different from the presented deal. The terms are buying your customer base and team, not your technology's independence. The negotiating leverage is that they need this deal more urgently than the premium suggests. The recommendation: renegotiate the autonomy clause to remove the strategy qualifier, extend autonomy to match retention vesting (4 years), and add objective criteria for what constitutes autonomy. If they refuse, that is the clearest signal of what post-acquisition life will look like.

**Gotchas discovered:** The "gut feeling" was real -- it was pattern-matching the contradiction between generous financial terms and a clause that undermined their intent. The skill articulated what intuition was detecting but could not express: the term sheet was internally inconsistent.

## Usage Scenarios

### Scenario 1: Evaluating a technical architecture proposal

**Context:** Your team proposes a microservices migration. The presentation is polished and the team is confident.

**You say:** "Critically analyze this microservices proposal. The team is enthusiastic but the 6-month timeline concerns me. What are we not seeing?"

**The skill provides:**
- Gap analysis: what was not addressed (data migration, service discovery, distributed tracing)
- Assumption testing: "our services are already loosely coupled" -- verify against actual code dependencies
- Red flags: confident timelines without contingency buffers; no mention of rollback strategy
- Probabilistic assessment of timeline risk based on industry data

**You end up with:** A list of hidden risks, specific questions to ask the team, and early warning indicators for timeline slippage.

### Scenario 2: Reading a competitor's strategic move

**Context:** Your main competitor just announced a free tier for their product -- previously entirely paid.

**You say:** "Our competitor just launched a free tier. What's the strategic game being played? What does this signal about their position?"

**The skill provides:**
- Multi-level reading: surface (growth strategy), subtext (possibly growth has stalled), meta (may be preparing for funding round needing user metrics)
- Pattern recognition: free tier launches often precede pricing changes for paid tiers
- Game theory implications: how this changes the competitive dynamics for your pricing
- Early warning: watch for their paid tier pricing changes within 6 months

**You end up with:** Strategic interpretation that goes beyond the press release, with actionable monitoring indicators.

### Scenario 3: Gut feeling about a hire

**Context:** You interviewed a senior engineering candidate. Resume is excellent, technical interview was strong, but something feels off.

**You say:** "I can't articulate why but I have a bad feeling about this candidate. Help me identify what my intuition is picking up on."

**The skill provides:**
- Micro-signal analysis: what specific moments triggered the feeling? (Language hedging, topic avoidance, emphasis patterns)
- Gap analysis: what questions did the candidate avoid or redirect? What would normally be mentioned but was not?
- Pattern matching: does the career trajectory have discontinuities that were not explained?
- Confidence calibration: how much weight should the gut feeling carry vs. the strong technical signals?

**You end up with:** Specific follow-up questions to resolve the ambiguity, and a framework for weighing intuitive signals against objective evidence.

---

## Decision Logic

**When does critical-intuition activate vs. creative-problem-solving?**

These skills are complementary opposites:
- **critical-intuition:** Analyzing what exists -- proposals, situations, evidence, patterns. Convergent, evaluative, backward-looking.
- **creative-problem-solving:** Generating what does not yet exist -- solutions, strategies, alternatives. Divergent, generative, forward-looking.

Rule of thumb: if the input is an existing thing to evaluate, use critical-intuition. If the input is a problem to solve, use creative-problem-solving. In practice, they alternate: generate options, critique them, refine, evaluate again.

**Which analysis depth is appropriate?**

The skill calibrates based on stakes:
- Low stakes (minor decision, reversible): surface + subtext reading, quick red flag scan
- Medium stakes (significant decision, partially reversible): full seven-step process, probabilistic assessment
- High stakes (irreversible decision, major consequences): full process with extended patterns, multiple hypothesis testing, explicit metacognitive checks

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Over-reading: finding signals that are not there | Analysis produces alarming conclusions from ambiguous data; every proposal looks suspicious | Calibrate confidence: distinguish high-confidence findings from speculation; require corroborating evidence for strong claims |
| Analysis paralysis: too many hypotheses, no judgment | Analysis identifies 10 possible interpretations but cannot recommend which is most likely | Force probabilistic ranking: assign relative likelihoods even if uncertain; identify the discriminating evidence that would resolve ambiguity |
| Confirmation bias in analysis direction | The "gut feeling" biases the analysis toward confirming the initial suspicion | Explicit metacognitive check: what would change my mind? Generate the strongest counter-argument to the conclusion |

## Ideal For

- **Technical leaders** evaluating proposals, architectures, or strategic decisions who need to see beyond the presented surface to hidden risks and dynamics
- **Negotiators** reading between the lines on term sheets, contracts, or partnership offers who need to understand the other party's actual position and incentives
- **Product managers** interpreting market signals, competitor moves, or customer feedback where what is not said is as important as what is said
- **Risk analysts** who need to identify early warning indicators and red flag clusters before problems become visible failures

## Not For

- **Generating new ideas or solutions** -- if you need creative alternatives or breakthrough thinking, use `creative-problem-solving`
- **Brainstorming or divergent thinking** -- if the problem requires expanding the solution space, use `creative-problem-solving`
- **Systematic risk frameworks** -- if you need structured risk registers and mitigation plans, use `risk-management` (which this skill complements with deeper pattern detection)

## Related Plugins

- **creative-problem-solving** -- The generative counterpart: create ideas with creative-problem-solving, then evaluate them with critical-intuition
- **risk-management** -- Structured risk assessment frameworks that critical-intuition's pattern detection feeds into
- **systems-thinking** -- Deeper systems dynamics for understanding the feedback loops that critical-intuition identifies
- **prioritization** -- For ranking the risks and opportunities that critical-intuition surfaces
- **outcome-orientation** -- Define measurable criteria for monitoring the early warning indicators identified here

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
