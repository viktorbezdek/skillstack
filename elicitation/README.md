# Elicitation

> **v2.0.0** | Design & UX | 2 iterations

> Design conversations that reveal what people actually think, feel, and value -- using evidence-based psychological frameworks instead of standard interview questions.

## The Problem

Standard user interviews produce standard answers. When you ask someone "What do you value?" they recite socially acceptable answers. When you ask "Why did you choose this product?" they construct a rational narrative that may have little to do with their actual decision process. The gap between stated preferences and real motivations is one of the most well-documented phenomena in psychology, yet most interview guides ignore it entirely.

The consequences are expensive. Product teams build features based on what users *said* they wanted, only to discover low adoption because the stated needs were aspirational, not real. UX researchers run 20 interviews and produce findings that any team member could have guessed, because the questions never went deeper than surface-level preferences. Conversational AI products feel hollow because their question-and-answer structure signals interrogation, not genuine curiosity -- and people respond to interrogation by closing down, not opening up.

The underlying problem is structural: most interviewers rely on questions as their primary tool. But decades of research in Motivational Interviewing (Miller & Rollnick), narrative identity (McAdams), and autobiographical memory (Singer) show that questions are the least effective instrument for eliciting authentic disclosure. Reflections -- statements that mirror and extend what someone has said -- consistently outperform questions at producing depth. Without this knowledge, even skilled interviewers default to interrogation patterns that suppress the very disclosure they are trying to produce.

## The Solution

This plugin gives Claude access to seven evidence-based psychological frameworks for designing conversations that create the conditions for authentic self-disclosure. Instead of generating generic interview questions, Claude applies specific methodologies: the OARS framework from Motivational Interviewing (with the 2:1 reflection-to-question ratio), McAdams' 8-scene narrative identity interview, Singer's self-defining memory elicitation, Schwartz's indirect values discovery techniques, Young's schema detection through the Downward Arrow method, Haight and Birren's life review question sequences, and Pennebaker's LIWC linguistic markers.

The skill provides a single SKILL.md with progressive-disclosure routing -- Claude loads only the reference files relevant to the specific query, preventing context bloat from the 8 domain-specific reference documents. Each reference contains the full research framework with concrete techniques, example dialogue, and anti-pattern identification. An ethics guardrail layer ensures that all elicitation designs respect consent boundaries, withdrawal rights, and the line between research and therapy.

The plugin ships 8 reference files covering the complete depth of each framework, 13 trigger eval cases, and 3 output quality eval cases.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Interviews produce socially desirable answers because questions signal what the interviewer wants to hear | Reflection-first design (2:1 ratio) creates space for authentic disclosure instead of performed answers |
| Interview scripts are question lists that feel like interrogation to the participant | Conversation designs alternate reflections, open questions, affirmations, and summaries (OARS) for natural flow |
| Values discovery asks "What do you value?" and gets rehearsed answers | Indirect techniques (role-model, opposite-day, decision-archaeology) surface operational values, not aspirational ones |
| Researchers miss depth because they follow their agenda instead of the participant's energy | Domain routing teaches Claude to follow the participant's lead and go deeper where they show engagement |
| Conversational AI asks questions and waits for answers, creating a robotic interview feel | Framework-driven design builds agents that reflect, summarize, and earn depth incrementally |
| No systematic way to detect when an interview script has anti-patterns | Anti-pattern reference identifies 7 specific failure modes (interrogation trap, premature depth, therapy cosplay) with concrete fixes |

## Context to Provide

Interview design depends on who you are interviewing, what you want to learn, and how much trust has been established. The same topic requires a completely different conversation structure for a first-time contact versus an ongoing relationship, for a 20-minute user research call versus a 90-minute life story interview, for in-person versus async written format.

**What to include in your prompt:**
- **Who you are interviewing** (enterprise buyers, end users, team members, potential customers, research participants) -- different populations need different frameworks and vocabulary
- **What you actually want to learn** -- go one level deeper than the surface goal; "why users abandon onboarding" is better than "user feedback"; "what values drive prioritization decisions" is better than "what the team wants"
- **The trust level** (first contact / one prior interaction / established relationship) -- premature depth in low-trust contexts suppresses disclosure
- **The format** (30-minute video call, async chat, in-person, written journaling prompt) -- pacing and reflection types differ
- **What you already know** -- existing data, prior interviews, hypotheses you want to stress-test
- **For conversation critique**: paste the actual transcript or script -- the skill reads the specific questions and reflections to flag anti-patterns

**What makes results better:**
- Stating what you have already tried and why it did not produce depth (e.g., "we ran 15 interviews that all produced 'it was confusing' with no specifics")
- Describing any sensitive topics that might come up (career failures, financial stress, relationship dynamics) so the skill can add consent checkpoints
- Specifying whether you want a conversation design, a critique of existing work, or a framework explanation

**What makes results worse:**
- Asking for "a list of questions" -- the skill's core methodology uses reflections, not questions; asking for questions gets questions but misses the depth-producing techniques
- Requesting clinical or therapeutic conversation design -- the skill flags this as outside its ethical boundary and redirects
- Omitting the trust stage -- asking for a deep-values discovery session for a first-contact interview produces an inappropriately invasive design

**Template prompt:**
```
Design a [format: 30-minute video call / async written / 90-minute in-person] interview guide for [audience]. The goal is to understand [specific depth target -- what you really want to know, not just the surface topic]. Trust level: [first contact / one prior meeting / established relationship]. I already know: [existing data or hypotheses]. The stated reason I keep getting surface answers is [why current approach is not working].
```

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install elicitation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention interview design, elicitation, deep interviews, values discovery, narrative identity, motivational interviewing, or conversation critique.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session
3. Type: `Design an interview script that reveals what actually motivates our users to switch from a competitor product`
4. Claude applies the OARS framework and values elicitation techniques to produce a conversation flow with reflections, open questions, and indirect value-surfacing techniques -- not a list of direct questions
5. Next, try: `Critique this interview transcript for depth I missed` and paste a real or draft conversation

---

## System Overview

```
User prompt (interview design / conversation critique / values discovery)
        |
        v
+------------------+     +---------------------------+
|  elicitation     |---->| Domain routing table      |
|  skill (SKILL.md)|     | (loads relevant refs only)|
+------------------+     +---------------------------+
        |                         |
        v                         v
  Core principle            Reference files (8)
  (always applied):         loaded on demand:
  - 2:1 reflection ratio    - motivational-interviewing.md
  - Earn depth gradually    - narrative-identity.md
  - Follow their lead       - self-defining-memories.md
        |                   - values-elicitation.md
        v                   - schema-detection.md
  Reasoning sequence:       - life-review-questions.md
  1. Understand context     - linguistic-markers.md
  2. Check trust stage      - anti-patterns.md
  3. Load matching refs
  4. Design reflections
  5. Flag anti-patterns
  6. Respect ethics
```

Single-skill plugin with 8 progressive-disclosure reference files. References are loaded selectively based on the query topic -- Claude never loads all 8 simultaneously.

## What's Inside

| Component | Type | What It Provides |
|---|---|---|
| **elicitation** | Skill | Core methodology, domain routing table, reasoning sequence, ethical guardrails |
| **motivational-interviewing.md** | Reference | OARS framework, reflection types (simple/complex/amplified/double-sided), 2:1 ratio mechanics |
| **narrative-identity.md** | Reference | McAdams' 8-scene life story interview, narrative themes (agency/communion/redemption/contamination) |
| **self-defining-memories.md** | Reference | Singer's framework for identifying and eliciting formative memories |
| **values-elicitation.md** | Reference | Schwartz's 10 universal values, 4 indirect elicitation techniques |
| **schema-detection.md** | Reference | Young's 18 Early Maladaptive Schemas, Downward Arrow technique |
| **life-review-questions.md** | Reference | Haight/Birren structured question sequences across life stages |
| **linguistic-markers.md** | Reference | Pennebaker/LIWC language analysis patterns with validity caveats |
| **anti-patterns.md** | Reference | 7 specific failure modes with concrete fixes |
| **trigger-evals** | Eval | 13 trigger eval cases (8 positive, 5 negative) |
| **output-evals** | Eval | 3 output quality eval cases |

### Component Spotlights

#### elicitation (skill)

**What it does:** Activates when you ask about designing interviews, critiquing conversation scripts, surfacing user motivations, building conversational AI, or analyzing narratives for psychological depth. Applies a domain routing table to load only the relevant reference frameworks, then produces conversation designs using the OARS methodology with a 2:1 reflection-to-question ratio.

**Input -> Output:** You provide a conversation design goal, interview context, or transcript to critique -> The skill produces a conversation flow with reflections and questions, a framework-specific methodology, anti-pattern flags, and ethical guardrails.

**When to use:**
- Designing user research interview scripts that go beyond surface preferences
- Critiquing or auditing an existing conversation flow for depth opportunities
- Building conversational AI that earns trust incrementally
- Discovering what actually drives a person (values, schemas, formative experiences)
- Analyzing narrative transcripts for themes of agency, communion, redemption, contamination

**When NOT to use:**
- Clinical diagnosis or treatment planning -> consult a licensed professional
- Structured data capture (age, job title, preferences) -> use standard survey design
- Building user personas from existing research data -> use [persona-definition](../persona-definition/)
- Stakeholder mapping across an organization -> use [persona-mapping](../persona-mapping/)

**Try these prompts:**

```
Design a 45-minute video call interview guide for enterprise IT buyers (directors and VPs) who are evaluating switching from their current project management platform. I want to understand what actually drives their switching decision -- not the vendor comparison criteria they recite in sales calls. These are first contacts introduced through a partner. What's really behind phrases like "we need better reporting"?
```

```
Critique this user research transcript for missed depth opportunities. We were trying to understand why users abandon our onboarding flow, but every answer was "it was confusing" with no actionable specifics. Flag where a reflection would have gone deeper than the question asked.

[paste transcript]
```

```
I'm building a weekly reflection journaling app. Users answer 3 prompts each Friday. Design the prompt sequence so it builds depth over time -- first session feels welcoming, later sessions surface what users actually value about their work (not just what they did). Format: async written, 5-10 minutes per session.
```

```
Our users keep requesting "more customization" in our project management tool -- we've shipped 4 customization features and adoption is low. Help me design a 30-minute interview that surfaces what customization actually means to them. I have two prior interviews on this topic that produced the same "more control" answers. Trust level: one prior interaction each.
```

```
Audit this career coaching chatbot script for anti-patterns. It's supposed to help users explore a career pivot but user feedback says it "feels like a job application form." I suspect the reflection-to-question ratio is wrong.

[paste chatbot conversation flow]
```

**Key references by topic:**

| Reference | Topic |
|---|---|
| `motivational-interviewing.md` | OARS framework, reflection types, 2:1 ratio mechanics |
| `narrative-identity.md` | McAdams' 8-scene interview, narrative theme analysis |
| `self-defining-memories.md` | Eliciting formative memories that shape personality |
| `values-elicitation.md` | Schwartz's 10 values, indirect discovery techniques |
| `schema-detection.md` | Young's schemas, Downward Arrow technique |
| `life-review-questions.md` | Structured question sequences across life stages |
| `linguistic-markers.md` | LIWC language patterns with validity caveats |
| `anti-patterns.md` | 7 failure modes: interrogation trap, premature depth, therapy cosplay, etc. |

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Write interview questions" | "Design an interview that reveals why users abandon our onboarding flow -- go deeper than 'it was confusing'" |
| "Help me understand users" | "I have a transcript from a user interview about remote work preferences. Critique it for missed depth opportunities." |
| "Make a chatbot" | "Build a conversational flow for a career coaching bot that earns trust before asking about fears and regrets" |
| "What questions should I ask?" | "Design a values discovery session for a product team -- I need to understand what actually drives their prioritization decisions" |
| "Analyze this conversation" | "Analyze this life story interview for themes of agency vs communion and identify where the interviewer steered instead of following" |

### Structured Prompt Templates

**For interview design:**
```
Design an interview guide for [context: user research / life review / product discovery] targeting [audience]. The goal is to understand [specific depth target, e.g., "why they chose competitor X" or "what values drive their career decisions"]. The interview will be [format: 30-min call / async chat / in-person]. Trust level: [first contact / established relationship].
```

**For conversation critique:**
```
Critique this [transcript / script / conversation flow] for elicitation anti-patterns and missed depth. The goal was [what the interviewer was trying to learn]. Flag specific moments where a reflection would have worked better than the question asked.
```

**For conversational AI design:**
```
Design a conversational flow for [product type, e.g., journaling app / coaching bot / onboarding sequence] that builds trust incrementally. Users will interact [frequency]. The depth target is [what you want to eventually surface, e.g., career values / life goals / pain points].
```

### Prompt Anti-Patterns

- **Asking for a list of questions:** "Give me 20 interview questions about user satisfaction" -- the skill's core insight is that questions are the least effective elicitation tool. It will produce conversation designs with reflections, not question lists.
- **Skipping the context:** "Design an interview" without specifying who you are interviewing, what you want to learn, or what trust level exists -- the skill needs context to calibrate depth and choose frameworks.
- **Requesting clinical/therapeutic applications:** "Help me design a therapy session for processing trauma" -- the skill explicitly flags this as outside its ethical boundary. It is for research and design, not treatment.
- **Expecting instant depth:** "Design a 5-minute conversation that reveals someone's deepest values" -- the skill will push back because depth requires trust, and trust requires time. It will suggest graduated disclosure strategies instead.

## Real-World Walkthrough

You are a product manager at a B2B SaaS company. Your team is building a new feature based on user feedback: "We need better reporting." But after three quarters of building reporting features, adoption remains flat. You suspect the stated need ("better reporting") is masking the real need. You decide to design a user research session that goes deeper.

**Step 1: Framing the goal.** You ask Claude: **"Design an interview guide that reveals what our enterprise users actually need when they say 'better reporting' -- I think the stated need is masking something deeper."**

Claude activates the elicitation skill and loads two references: `motivational-interviewing.md` (because all elicitation conversations need the OARS framework) and `values-elicitation.md` (because you are trying to surface the real need behind a stated preference).

**Step 2: The conversation design.** Claude produces a 45-minute interview flow structured in three phases:

*Phase 1 (Trust building, 10 min):* Open with a narrative prompt -- "Walk me through a typical day when you use our product" -- followed by simple reflections ("So you start by checking the dashboard before your standup"). No direct questions about reporting yet. The goal is to understand the user's workflow context before narrowing.

*Phase 2 (Decision archaeology, 20 min):* Use the decision-archaeology technique from values elicitation. "Think of a recent time you made a decision that required data from our product. Walk me through what happened." Follow with complex reflections: "It sounds like the frustration wasn't about the data being missing -- it was about not being able to get it in time for the meeting." This surfaces whether "better reporting" actually means "faster access," "more trust in the numbers," or "something I can show my VP without explanation."

*Phase 3 (Depth, 15 min):* Based on where the user's energy went in Phase 2, go deeper with the opposite-day technique: "Imagine a world where reporting didn't exist at all in our product. What would change about your day?" This surfaces the underlying job-to-be-done rather than the feature request.

**Step 3: Anti-pattern audit.** Claude flags that your original draft had an interrogation pattern: five consecutive questions about reporting satisfaction with no reflections between them. It shows you how to replace three of the five with reflections that invite elaboration without adding cognitive load.

**Step 4: Ethical check.** Claude notes that Phase 3 could surface workplace frustrations or political dynamics (user might reveal that "better reporting" is really "ammunition for a budget fight with another department"). It recommends adding a consent checkpoint before Phase 3: "We're going to explore this a bit more deeply -- is that okay? You can skip anything that feels too specific to internal dynamics."

**Step 5: Pilot and iterate.** You run the interview with two users. The first reveals that "better reporting" actually means "I need something I can screenshot and paste into Slack in under 30 seconds." The second reveals it means "I need to prove ROI to my CFO every quarter." Neither maps to the reporting features your team has been building.

You now have a validated interview guide, two concrete insights that reframe the product direction, and a methodology you can reuse for the next discovery cycle. The total time from prompt to pilot was about 2 hours -- compared to the weeks you previously spent building features based on surface-level feedback.

## Usage Scenarios

### Scenario 1: Designing a user research interview that goes beyond stated preferences

**Context:** You are a UX researcher running a study on why users abandon your onboarding flow. Previous interviews produced "it was confusing" but no actionable detail.

**You say:** "Design an interview guide that reveals why users really abandon our onboarding -- 'it was confusing' isn't actionable. I have 30 minutes per session and these are first-time contacts."

**The skill provides:**
- A graduated three-phase conversation flow (trust, exploration, depth) calibrated for 30 minutes with strangers
- OARS-based reflections paired with each question so you know how to deepen any answer
- Two indirect value-surfacing techniques (opposite-day and decision-archaeology) tailored to onboarding
- Anti-pattern flags for your existing draft questions

**You end up with:** An interview guide that produces specific, actionable insights about the emotional and cognitive barriers in your onboarding -- not just "confusing."

### Scenario 2: Auditing a chatbot conversation flow for anti-patterns

**Context:** Your team built a career coaching chatbot, but user feedback says it feels "like talking to a survey." You suspect the conversation design is question-heavy.

**You say:** "Audit this chatbot script for elicitation anti-patterns. It's supposed to help users explore career direction but users say it feels robotic." And you paste the conversation flow.

**The skill provides:**
- Line-by-line anti-pattern identification (interrogation trap, premature depth, monologue response)
- Specific replacement dialogue for each flagged pattern
- Reflection-to-question ratio analysis (yours was 1:5; target is 2:1)
- Suggested graduated disclosure structure so the bot earns trust before asking about fears

**You end up with:** A revised conversation flow with a natural rhythm that users are more likely to engage with deeply.

### Scenario 3: Building a personal history product

**Context:** You are building a "life story" feature for a journaling app. Users answer prompts about their life and the app creates a narrative timeline.

**You say:** "Design the prompt sequence for our life story feature. It should cover childhood through present, feel natural, and produce rich narratives -- not one-sentence answers."

**The skill provides:**
- Haight/Birren life review question sequence adapted for async journaling (shorter prompts, more reflective follow-ups)
- McAdams' 8 key scenes structured as a progressive disclosure sequence across 8 sessions
- Singer's self-defining memory prompts for identifying the memories that carry disproportionate weight
- Ethical guardrails for handling disclosures about trauma or loss in a non-therapeutic product

**You end up with:** A multi-session prompt sequence that produces 2-3 paragraph responses per prompt instead of one-sentence answers, with built-in consent checkpoints for sensitive topics.

### Scenario 4: Discovering team values for a product prioritization workshop

**Context:** Your product team keeps having circular debates about what to build next. You suspect the real disagreement is about values (growth vs stability, speed vs quality), not about the features themselves.

**You say:** "Help me surface the underlying values driving our team's prioritization disagreements. I need a workshop exercise for 6 people, 90 minutes."

**The skill provides:**
- Schwartz values framework applied to product decisions (mapping the 10 universal values to tech team dynamics)
- Role-model technique adapted for teams: "Think of a product decision from another company you admire. What made it admirable?"
- Decision-archaeology exercise: walk through the last 3 contentious decisions and surface the value trade-offs that were implicit
- Anti-pattern warning: do not ask "What are your values?" directly -- it produces performative answers

**You end up with:** A 90-minute workshop design that surfaces the actual value tensions driving disagreements, enabling the team to name and negotiate them explicitly.

---

## Decision Logic

The skill uses a domain routing table to decide which references to load for each query:

| Query topic | References loaded |
|---|---|
| Interview structure, life stages, guided autobiography | `life-review-questions.md` |
| Formative memories, vivid memories, personality shaping | `self-defining-memories.md` |
| Life story interview, narrative themes, 8 key scenes | `narrative-identity.md` |
| OARS, reflection types, 2:1 ratio, resistance | `motivational-interviewing.md` (loaded for almost every query) |
| Values discovery, Schwartz values, indirect techniques | `values-elicitation.md` |
| Belief patterns, schemas, Downward Arrow | `schema-detection.md` |
| Language analysis, pronoun patterns, cognitive markers | `linguistic-markers.md` |
| Conversation critique, script audit | `anti-patterns.md` first, then relevant framework references |
| Multi-domain query | Multiple references loaded and synthesized |

The `motivational-interviewing.md` reference is almost always loaded because the OARS framework and 2:1 reflection ratio apply to every elicitation context. Other references are loaded only when the query specifically requires their framework.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| User asks for a question list instead of a conversation design | Skill produces reflections and OARS structure but user wanted a simple numbered list | Explain that the skill's methodology uses reflections, not questions. If you truly need a question list, ask for "a structured interview guide with follow-up probes" and the skill will adapt while keeping reflection-first principles |
| Ethical boundary crossed (clinical/therapeutic request) | Skill flags the request and refuses to design a therapeutic intervention | Reframe the request as research or design: "I'm building a product that helps users reflect on X" rather than "design a therapy session for X" |
| Cross-cultural validity concern | Skill produces frameworks based on WEIRD research populations that may not transfer | Skill explicitly flags this limitation. Adapt by testing the conversation design with the target population before scaling |
| Context too vague to calibrate depth | Skill asks clarifying questions instead of producing a design | Provide: who you are interviewing, what you want to learn, the trust level (stranger vs established), the format (live/async), and the time available |
| Premature depth in low-trust context | Conversation design asks about values or schemas in a first-contact interview | Review the trust stage: the skill's reasoning sequence checks trust level at step 2 and calibrates depth accordingly. Specify "first contact" explicitly in your prompt |

## Ideal For

- **UX researchers** who need interview guides that produce actionable depth instead of surface-level preferences
- **Product managers** who suspect that stated feature requests mask deeper needs and want techniques to surface the real jobs-to-be-done
- **Conversational AI designers** building chatbots, journaling apps, or coaching products that need to feel human rather than robotic
- **Workshop facilitators** designing team exercises for values discovery, retrospectives, or strategic alignment
- **Content creators** building life story, memoir, or personal history products that need prompts capable of producing rich narratives

## Not For

- **Clinical diagnosis or therapy** -- the skill is explicitly research/design-oriented, not therapeutic. If someone discloses something requiring professional support, it will redirect.
- **Structured data capture** -- if you need facts (age, job title, preferences), use standard survey design. This skill is for depth, not breadth.
- **Persona creation from existing data** -- use [persona-definition](../persona-definition/) to build personas from research data. Use this skill to design the research conversations that produce that data.

## Related Plugins

- **[Persona Definition](../persona-definition/)** -- Build individual user personas from the research data this skill helps you collect
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholders across organizations using Power-Interest matrices and RACI charts
- **[Creative Problem Solving](../creative-problem-solving/)** -- When the insight from elicitation needs to be turned into actionable ideas
- **[UX Writing](../ux-writing/)** -- Write interface copy that reflects the language and values surfaced through elicitation
- **[Content Modelling](../content-modelling/)** -- Structure the content that elicitation-based research produces

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
