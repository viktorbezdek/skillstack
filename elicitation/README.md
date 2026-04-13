# Elicitation

> **v2.0.0** | Design & UX | 2 iterations

> Design conversations that reveal what people actually think, feel, and value -- not just what they say when asked directly.

## The Problem

Standard user interviews produce surface-level responses. When you ask someone "Why do you use this product?" you get a rationalization, not the real answer. When you ask "What matters to you?" you get a socially acceptable list, not the beliefs that actually drive behavior. This is not because people are dishonest -- it is because direct questions trigger self-presentation rather than self-reflection. The interviewer and the interviewee are both stuck in the same loop: ask, answer, move on.

The consequences are expensive. Product teams build features based on what users say they want, then watch adoption flatline because the stated preferences do not match the underlying motivations. Research teams conduct 20 interviews and extract insights that any stakeholder could have guessed, because the conversation never got below the surface. Conversational AI products feel hollow after the first session because they react to words rather than understanding the person behind them.

The root cause is methodological. Most interview guides are lists of questions -- and questions are the weakest tool for eliciting depth. Psychological research across multiple traditions (Singer's self-defining memories, McAdams' narrative identity, Miller & Rollnick's motivational interviewing) converges on the same finding: reflections outperform questions, patience outperforms probing, and the most revealing information emerges when people feel safe to share rather than pressured to answer. But translating these research frameworks into practical conversation design is a specialized skill that few product teams have access to.

## The Solution

This plugin gives Claude access to seven evidence-based psychological frameworks for designing conversations that create the conditions for authentic self-disclosure. Instead of generating a list of questions, the skill teaches Claude to design conversations where reflections outnumber questions 2:1, where depth is earned incrementally through trust, and where the interviewer follows the participant's energy rather than pushing their own agenda.

The core SKILL.md contains the reasoning sequence Claude applies to every query: understand the use context, check the trust stage, load the relevant frameworks, design for reflections, flag anti-patterns, and respect ethical boundaries. Behind it, eight progressive-disclosure reference files provide deep methodology for specific techniques -- from Singer's five criteria for memory salience to Young's 18 Early Maladaptive Schemas to Pennebaker's LIWC linguistic markers.

The practical outputs are interview scripts with reflection moves pre-designed for each question, conversation flow diagrams with trust-appropriate depth progression, transcript critiques that name specific anti-patterns (interrogation trap, interpretation leap, premature depth) and show concrete fixes, and design specs for conversational AI products that build understanding across sessions.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Interview scripts are lists of questions with no reflection strategy -- responses stay surface-level | Every question comes with 1-2 matching reflection moves, targeting a 2:1 reflection-to-question ratio |
| Interviewers ask about values directly ("What matters to you?") and get performative answers | Four indirect elicitation techniques (role model, opposite day, decision archaeology, anger-as-signal) surface values through behavior |
| Conversation depth depends entirely on the interviewer's intuition and experience | Structured progression from safe territory to deeper disclosure, calibrated to trust stage |
| Transcript reviews check for "good questions" but miss structural anti-patterns | Seven named anti-patterns (interrogation trap, interpretation leap, agenda push, premature depth, therapy cosplay, monologue response, validation trap) with specific detection criteria and fixes |
| Conversational AI products react to keywords rather than building a model of the person | Linguistic markers, narrative themes, and schema patterns provide structured signals for personality modeling across sessions |
| Research conversations produce insights that stakeholders could have guessed without the interview | Formative memories, narrative themes (agency/communion/redemption/contamination), and schema detection surface non-obvious drivers |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install elicitation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when your prompts mention elicitation, deep interviews, user research methodology, motivational interviewing, OARS, narrative identity, life review, values elicitation, or schema detection.

## Quick Start

1. Install the plugin using the commands above
2. Open a Claude Code session
3. Type: `Design a user research interview that reveals why people abandon our fitness app after week 2`
4. Claude produces an interview script with reflection-first structure, graduated depth progression, self-defining memory frames, and anti-pattern warnings
5. Next, try: `Critique this interview transcript for anti-patterns` and paste a real or draft transcript

## What's Inside

Single-skill plugin with one SKILL.md, 8 progressive-disclosure reference files, 13 trigger eval cases, and 3 output eval cases. Claude loads only the references relevant to each query -- no context bloat.

| Component | What It Provides |
|---|---|
| **Core Skill** | Reasoning sequence, domain routing table, ethical guardrails, and the "depth through patience" principle |
| **8 Reference Files** | Deep methodology for each psychological framework, loaded progressively based on query topic |

### elicitation

**What it does:** Activates when you ask about designing interviews, critiquing conversations, surfacing values or motivations, building conversational AI, or creating life story products. Routes to the appropriate psychological framework(s), applies the core reasoning sequence (understand context, check trust stage, design for reflections, flag anti-patterns), and produces conversation designs grounded in research.

**Try these prompts:**

```
Design an interview script that reveals what actually drives our power users -- not just what they say they like about the product
```

```
Critique this user research transcript -- I think the interviewer was leading the participant but I can't pinpoint where
```

```
I'm building a journaling app that helps people reflect on their life story. Design the conversation flow for the first three sessions
```

```
How do I surface someone's core values without just asking "what are your values?" -- I need indirect techniques for a stakeholder interview
```

```
Design a conversational AI persona that builds understanding of the user across multiple sessions using linguistic and narrative patterns
```

**Key references:**

| Reference | Topic |
|---|---|
| `self-defining-memories.md` | Singer's five criteria for memory salience, three conversational frames, and the reminiscence bump (ages 10-30) |
| `narrative-identity.md` | McAdams' 8-scene life story interview and four narrative themes (agency, communion, redemption, contamination) |
| `motivational-interviewing.md` | OARS framework, four reflection types, 2:1 ratio mechanics, and resistance reduction |
| `values-elicitation.md` | Schwartz's 10 universal values and four indirect elicitation techniques |
| `schema-detection.md` | Young's 18 Early Maladaptive Schemas, Downward Arrow technique, and clinical vs. research boundaries |
| `life-review-questions.md` | Haight's stage-specific sequences and Birren's thematic approach |
| `linguistic-markers.md` | Pennebaker/LIWC patterns with cross-cultural and individual-variation caveats |
| `anti-patterns.md` | Seven anti-patterns with mechanisms, examples, and concrete fixes |

## Real-World Walkthrough

You are the lead researcher at a health-tech startup building a chronic pain management app. After three months of user interviews, your team has a stack of transcripts that all say the same thing: "I want to track my pain better" and "I wish my doctor understood my situation." These are true statements, but they are not actionable insights. You suspect there are deeper motivations and fears driving app adoption (and abandonment) that your interview guide is not reaching.

You start by asking Claude: **"Critique our current interview guide for a chronic pain management app -- here are the first 10 questions"** and paste the guide, which includes questions like "How would you rate your pain today?", "What features would be most useful?", and "How often do you use health apps?"

Claude activates the elicitation skill and loads the anti-patterns reference. It identifies three structural problems. First, the **interrogation trap**: the guide has 10 questions and zero reflection moves, creating a rapid-fire pattern that signals "I need your data" rather than "I want to understand your experience." Second, **premature depth**: question 4 asks "How has chronic pain changed your relationships?" -- a deeply personal topic positioned before any trust has been established. Third, **agenda push**: every question steers toward app features rather than following the participant's emphasis.

You ask Claude: **"Redesign this interview using the OARS framework and self-defining memory techniques."**

Claude loads the motivational-interviewing and self-defining-memories references. It produces a redesigned interview with three phases:

**Phase 1 -- Establishing Safety (10 minutes).** Open-ended questions about daily routines, not pain. "Walk me through a typical Tuesday" -- followed by a reflection template: "So your mornings are structured around [their words], and the afternoons are more variable." This builds trust and gives the participant control over when pain enters the conversation (it always does -- you just have to be patient).

**Phase 2 -- Memory Elicitation (15 minutes).** Instead of "How has pain changed your life?", Claude designs a self-defining memory frame: "If you think back over the past year, is there a specific moment -- maybe a few minutes, maybe an hour -- where you felt like your relationship with pain changed? Not the worst moment, just one that keeps coming back to you." This follows Singer's five criteria for memory salience: vivid, emotionally intense, frequently rehearsed, linked to enduring concerns, and associated with other similar memories. The memory frame invites narrative rather than evaluation.

For each memory prompt, Claude includes two reflection moves. If the participant describes a moment of helplessness, the simple reflection is: "That moment left you feeling like the pain was making the decisions, not you." The complex reflection adds a theme: "It sounds like what made that moment significant was not the pain level itself, but the loss of control -- like the pain was writing the script for your day." These reflections use McAdams' agency theme (control vs. helplessness) to deepen the conversation without adding a question.

**Phase 3 -- Values Surfacing (10 minutes).** Claude applies the decision archaeology technique from the values-elicitation reference: "Think about the last time you decided to push through pain to do something -- what was the activity, and what made it worth pushing through?" This surfaces the value (connection, achievement, independence) through a concrete behavior rather than abstract self-report. The follow-up is a reflection, not a question: "So being at your daughter's recital was worth three days of recovery -- that tells me something about what this app needs to protect."

The redesigned interview has a 2:1 reflection-to-question ratio, graduates from safe territory to emotional territory over 35 minutes, and surfaces values through behavior rather than self-report. Claude also flags two ethical considerations: re-consent is needed before Phase 2 ("We're going to talk about some more personal experiences -- you can skip anything that doesn't feel right"), and any disclosure that suggests the participant needs professional support should be acknowledged and redirected, not explored further.

You run three interviews with the redesigned guide. The difference is immediate. Instead of "I want to track my pain," participants share: "I stopped going to book club because I was afraid of being the person who always cancels" (loss of social identity), "My husband started making decisions for me and I couldn't explain why that felt worse than the pain" (autonomy as a core value), and "I downloaded four apps, deleted them all -- if I admit I need an app, I'm admitting this is permanent" (schema: defectiveness/shame around chronic illness). These are actionable insights that reshape your product strategy from pain tracking (a feature) to identity preservation (a mission).

## Usage Scenarios

### Scenario 1: Designing a user research interview that goes deeper

**Context:** You are a product researcher at a fintech company and your last round of interviews about savings behavior produced only stated preferences ("I want to save more").

**You say:** "Design an interview that reveals the emotional and psychological drivers behind why people fail to save -- not just the practical barriers"

**The skill provides:**
- An OARS-based interview structure with reflections designed for each question
- Self-defining memory frames ("Tell me about a moment with money that sticks with you")
- Decision archaeology prompts to surface values through past behavior
- Anti-pattern warnings specific to financial topics (avoiding the agenda push toward your product)

**You end up with:** A 30-minute interview script with graduated depth, pre-designed reflection moves, and ethical guardrails for discussing financial stress.

### Scenario 2: Auditing a research transcript for anti-patterns

**Context:** Your junior researcher conducted 8 interviews and the insights feel shallow. You suspect the interviewing technique is the problem but do not have time to listen to all recordings.

**You say:** "Critique this interview transcript for elicitation anti-patterns" and paste the transcript.

**The skill provides:**
- Named anti-patterns identified at specific points in the transcript (e.g., "Lines 12-15: interrogation trap -- three questions in succession with no reflection")
- The mechanism explaining why each anti-pattern suppresses depth
- Concrete rewrites showing how each moment could have been handled differently
- An overall score of the reflection-to-question ratio

**You end up with:** A coaching document you can use in a 1:1 with the researcher, with specific before/after examples from their own transcript.

### Scenario 3: Building a conversational AI that understands users over time

**Context:** You are designing an AI journaling product that converses with users across daily sessions. You want it to build a model of the user's personality, values, and narrative themes over time.

**You say:** "Design a multi-session conversation architecture for a journaling AI that builds psychological depth incrementally"

**The skill provides:**
- Session-by-session depth progression using the life review framework
- Linguistic markers (pronoun patterns, cognitive complexity) as signals for personality modeling
- Narrative theme tracking (agency, communion, redemption, contamination) across entries
- Schema detection triggers for identifying recurring belief patterns
- Ethical guardrails for storing and acting on elicited psychological data

**You end up with:** A conversation architecture spec with session templates, signal extraction logic, and a data sensitivity classification.

### Scenario 4: Creating a guided autobiography product

**Context:** You are building an app that helps older adults record their life story for their families.

**You say:** "Design the conversation flow for a life story recording app -- it should cover childhood through present day without feeling like a questionnaire"

**The skill provides:**
- Haight's stage-by-stage question sequences adapted for a product context
- Birren's thematic approach (family, work, money, health, meaning) as an alternative organization
- Self-defining memory frames for each life stage
- Anti-pattern audit ensuring prompts create reflective space rather than extraction pressure
- Consent and withdrawal design for sensitive disclosures

**You end up with:** A complete conversation flow with 6-8 sessions, each covering a life stage with reflection-first prompts and natural transitions.

### Scenario 5: Running a stakeholder interview for enterprise software

**Context:** The VP of Sales says they need "better reporting" but you suspect the real issue is trust in the underlying data. You need an interview approach that gets past the feature request to the actual problem.

**You say:** "How do I interview a VP of Sales to find out what's really wrong with their reporting -- they keep asking for dashboards but I think the problem is data trust"

**The skill provides:**
- Decision archaeology technique: "Walk me through the last time you made a pricing decision using a report"
- Reflection moves calibrated for executive conversations (no therapeutic language)
- Values surfacing through behavior: what they actually check vs. what they say they check
- The anger-as-signal technique for identifying where current tools fail emotionally, not just functionally

**You end up with:** A 20-minute interview guide that uncovers the real friction points behind the feature request, with specific probing sequences for data trust issues.

## Ideal For

- **Product researchers who need depth, not volume** -- the frameworks produce insights that reshape product direction rather than confirming existing assumptions
- **Conversational AI designers** -- the psychological frameworks provide structured signals (narrative themes, linguistic markers, schema patterns) for building understanding across sessions
- **Teams building personal history or life review products** -- Haight and Birren's methods are the gold standard for guided autobiography, adapted here for product contexts
- **Research team leads coaching junior researchers** -- the anti-patterns reference provides named, specific feedback on interviewing technique with concrete before/after examples
- **Enterprise product managers running stakeholder interviews** -- indirect elicitation techniques (decision archaeology, anger-as-signal) get past feature requests to real problems

## Not For

- **Clinical diagnosis or treatment planning** -- this skill is research/design-oriented. Schema detection and life review methods are used here for understanding, not therapy. Use a licensed professional for clinical applications
- **Structured survey design** -- if you need quantitative data (demographics, stated preferences, Likert scales), use standard survey methodology. This plugin is for depth, not breadth
- **Creating user personas from scratch** -- use [persona-definition](../persona-definition/) to build personas from research data. Use this plugin to design the research conversations that produce the data

## How It Works Under the Hood

The plugin uses a progressive-disclosure architecture with a lean SKILL.md and 8 reference files. The SKILL.md contains:

1. **Core principle** -- "depth through patience, not probing" -- applied to every response
2. **Domain routing table** -- maps query topics to the relevant reference file(s)
3. **Reasoning sequence** -- six steps applied to every query: understand context, check trust stage, load references, design for reflections, flag anti-patterns, respect ethical boundary
4. **Ethical guardrails** -- consent, withdrawal, clinical boundaries, data sensitivity, cross-cultural caveats

When a query arrives, Claude reads the routing table and loads only the relevant references. A question about interview design might load `motivational-interviewing.md` + `self-defining-memories.md`. A transcript critique loads `anti-patterns.md` first, then the framework references for the techniques in the script. A conversational AI design question might load `linguistic-markers.md` + `narrative-identity.md` + `schema-detection.md`. This keeps context lean while providing research-grade depth on demand.

## Attribution

Research foundations by Singer, McAdams, Miller & Rollnick, Schwartz, Young, Haight, Birren, and Pennebaker. Original skill content from [tasteray/skills](https://github.com/tasteray/skills). Curated, restructured into progressive-disclosure form, and extended with anti-patterns reference and ethical guardrails by [Viktor Bezdek](https://github.com/viktorbezdek).

## Related Plugins

- **[Persona Definition](../persona-definition/)** -- Build detailed user personas from research data -- pairs naturally with this plugin (design the interviews here, build the personas there)
- **[Persona Mapping](../persona-mapping/)** -- Stakeholder mapping with Power-Interest matrices and RACI charts
- **[User Journey Design](../user-journey-design/)** -- Map user journeys with touchpoints, emotional states, and pain points
- **[Content Modelling](../content-modelling/)** -- Design content models for the data structures that store elicited information
- **[Navigation Design](../navigation-design/)** -- Information architecture for products built around elicited content

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
