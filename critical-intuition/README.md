> **v1.0.15** | Strategic Thinking | 16 iterations

# Critical Intuition

Detect hidden patterns, expose blind spots, and deliver rigorous critical analysis with intuition-level depth -- making the tacit analytical moves of domain experts explicit and repeatable.

## What Problem Does This Solve

Information is rarely presented at face value: a proposal leaves out its failure modes, a status update is technically accurate but strategically misleading, a decision looks reasonable until you notice what is conspicuously absent. Standard analysis takes content at face value and misses the subtext, meta-signals, and anomalies that experienced practitioners catch instinctively. This skill provides a structured seven-step process for multi-level reading (surface, subtext, meta), signal and anomaly detection, fallacy identification, Bayesian reasoning, intuitive synthesis, early warning detection, and judgment formation -- turning tacit expert analysis into an explicit, repeatable methodology.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install critical-intuition@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

This is a single-skill plugin with five reference documents:

| Component | Description |
|---|---|
| `skills/critical-intuition/SKILL.md` | Core skill covering the seven-step analysis process (multi-level reading, signal detection, critical reasoning, probabilistic assessment, intuitive synthesis, early warning detection, judgment formation), the six-phase workflow, and eight validation checks for pre-completion quality assurance |
| `references/pattern-recognition.md` | Advanced reading techniques for detecting patterns, anomalies, micro-signals, and gaps in information |
| `references/critical-thinking.md` | Argument structure analysis, formal and informal fallacy detection, evidence evaluation, and motivated reasoning identification |
| `references/sixth-sense.md` | Subtle signal detection, leading indicators, trajectory sensing, tipping point proximity, and red flag cluster identification |
| `references/synthesis-frameworks.md` | Gestalt perception, cross-domain analogical reasoning, tacit knowledge integration, and information triangulation |
| `references/extended-patterns.md` | Advanced techniques for reading between lines, sixth sense development, critical questioning, bias mitigation, red/green flag catalogs, and output format templates |

## Usage Scenarios

**1. Reviewing a proposal for what it does NOT say**

A vendor proposal looks comprehensive, but something feels off. Apply multi-level reading: surface level (what is explicitly stated), subtext level (what assumptions are embedded, what is conspicuously absent), meta level (why is it framed this way, what are the vendor's incentives, what power dynamics are at play). Gap analysis identifies what information would normally be present but is not -- and why that absence is meaningful.

**2. Detecting red flags in a project status report**

A status report says the project is "on track" but the report's language has shifted from specific metrics to vague reassurances. Apply red flag cluster detection: multiple small concerns (hedging language, absent metrics, timeline qualifications), coincidence accumulation (three "minor" delays in adjacent workstreams), pattern breaks (previously detailed reports now lack specifics), and trajectory sensing (the rate of reassurance is increasing while the rate of concrete deliverables is decreasing).

**3. Evaluating an argument with calibrated confidence**

Someone presents a business case with compelling data. Apply Bayesian reasoning: what is the prior probability (base rate for this type of initiative succeeding)? How strong is the presented evidence (source credibility, sample representativeness, confounding factors)? What is the updated probability after incorporating the evidence? What would change your mind? Explicitly identify whether you are being overconfident or underconfident, and what discriminating evidence would shift the probability significantly.

**4. Diagnosing a gut feeling that something is wrong**

You have a strong intuition that a technical architecture decision is flawed but cannot articulate why. Apply intuitive synthesis: gestalt perception (combine disparate cues into a whole-picture understanding), cross-domain analogical reasoning (have you seen a similar structural pattern fail in another context?), tacit pattern matching (gut feeling as compressed expertise from past experience). Then apply metacognitive bias checks to distinguish genuine pattern recognition from anchoring, availability bias, or motivated reasoning.

**5. Reading between the lines in stakeholder communication**

A senior stakeholder says "we fully support this initiative" but their calendar shows no time allocated to it. Apply the three-level reading framework: the surface statement is supportive. The subtext -- no resource allocation, no follow-up questions, delegation to a junior team member -- suggests passive resistance. The meta level examines incentives: does this initiative threaten the stakeholder's current priorities? Synthesize into actionable judgment with explicit confidence calibration.

## How to Use

**Direct invocation:**

```
Use the critical-intuition skill to analyze this proposal for hidden risks and blind spots
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `pattern-recognition`
- `bayesian-reasoning`
- `analysis`

## When to Use / When NOT to Use

**Use when:**
- You need to read between the lines or detect what is not being said
- Critical analysis of an argument, proposal, or plan
- Identifying red flags, early warning signals, or hidden patterns
- Judgment under uncertainty with explicit confidence calibration
- Detecting bias, motivated reasoning, or logical fallacies
- Synthesizing complex, contradictory information into a coherent assessment

**Do NOT use when:**
- Generating new creative solutions, brainstorming, or strategic reframing -- use [creative-problem-solving](../creative-problem-solving/) instead

## Related Plugins

- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough solutions through lateral thinking, first principles reasoning, game theory, and strategic reframing
- **[Outcome Orientation](../outcome-orientation/)** -- Focus on measurable outcomes using OKRs, results-driven thinking, and the outcome vs. output distinction
- **[Prioritization](../prioritization/)** -- Apply RICE, MoSCoW, ICE scoring, and effort-impact matrices for decision-making
- **[Risk Management](../risk-management/)** -- Risk assessment frameworks, mitigation strategies, risk registers, and monitoring
- **[Systems Thinking](../systems-thinking/)** -- Feedback loops, leverage points, and system dynamics for analyzing complex problems

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
