# Elicitation

> **v2.0.0** | Design & UX | 2 iterations

Psychological elicitation and deep-interview design using narrative identity (McAdams), self-defining memories (Singer), Motivational Interviewing OARS (Miller & Rollnick), values elicitation (Schwartz), schema detection (Young), life review (Haight/Birren), and linguistic analysis (Pennebaker/LIWC). Curated by [Viktor Bezdek](https://github.com/viktorbezdek) from the original [tasteray/skills](https://github.com/tasteray/skills) content and restructured into 8 progressive-disclosure references.

## What Problem Does This Solve

User interviews and research conversations routinely produce surface-level responses -- stated preferences rather than underlying motivations, polished narratives rather than the formative experiences that actually shape behavior. Direct questioning triggers defensiveness; questionnaires capture what people think they should say. This skill applies seven evidence-based psychological frameworks to design conversations that create the conditions for authentic self-disclosure -- revealing values, schemas, formative memories, and motivations that standard interviews miss. The core principle: depth comes from patience, not probing.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install elicitation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## What's Inside

A lean SKILL.md with the core principle, when-to-use / when-not-to-use guidance, a domain routing table, reasoning sequence, and ethical guardrails. It loads one or more of the following 8 reference files progressively based on the query:

| Reference File | What It Covers |
|---|---|
| **`self-defining-memories.md`** | Singer's five criteria for memory salience, three conversational frames that elicit memories without interrogation, and the reminiscence bump (ages 10-30) where identity forms |
| **`narrative-identity.md`** | McAdams' 8-scene life story interview with conversational adaptations, and the four narrative themes (agency, communion, redemption, contamination) that predict well-being |
| **`motivational-interviewing.md`** | The OARS framework with all four reflection types (simple/complex/amplified/double-sided), the 2:1 reflection-to-question ratio, and question-type hierarchy |
| **`values-elicitation.md`** | Schwartz's 10 universal values with four indirect elicitation techniques (role model, opposite day, decision archaeology, anger-as-signal) that surface values through behavior |
| **`schema-detection.md`** | Young's 18 Early Maladaptive Schemas across five domains, the Downward Arrow technique, and linguistic markers -- with clinical vs research boundaries |
| **`life-review-questions.md`** | Barbara Haight's stage-specific question sequences (childhood through later life) and James Birren's thematic approach (family, work, money, health, death, meaning) |
| **`linguistic-markers.md`** | Pennebaker/LIWC patterns (pronoun usage, cognitive complexity, emotional tone, temporal focus) with caveats about individual variation and cross-cultural limits |
| **`anti-patterns.md`** | Seven anti-patterns (interrogation trap, interpretation leap, agenda push, premature depth, therapy cosplay, monologue response, validation trap) with mechanisms and fixes |

## How to Use

**Direct invocation:**

```
Use the elicitation skill to design an interview script that reveals what drives a product user
```

```
Use the elicitation skill to critique this transcript for interrogation anti-patterns
```

```
Use the elicitation skill to build a life review conversation flow for a personal history product
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

`elicitation` · `deep interview` · `user research` · `motivational interviewing` · `narrative identity` · `OARS` · `life review` · `values elicitation` · `schema detection` · `psychological profiling`

## Usage Scenarios

**1. Designing a user research interview for a health app.** You need to understand why people abandon fitness routines, not just that they do. Use the OARS framework to write an interview script where reflections outnumber questions 2:1, and layer in self-defining memory frames ("tell me about a time exercise felt effortless") to surface the emotional anchors that drive sustained behavior.

**2. Auditing a customer interview transcript.** Your research team conducted 10 interviews but the insights feel shallow. Load the anti-patterns reference and scan the transcripts for the interrogation trap (rapid-fire questions without reflection), the interpretation leap (jumping to conclusions mid-response), and premature depth (asking about childhood before trust is established).

**3. Building a conversational AI that understands personality over time.** You are designing an agent that converses with users across multiple sessions. Use the linguistic markers reference to identify pronoun patterns and cognitive complexity as signals of personality, combined with the values elicitation techniques to surface what drives someone through their own stories rather than self-report scales.

**4. Creating a guided autobiography product.** You are building an app that helps people record their life story. Use Haight's stage-by-stage sequences for chronological flow and Birren's thematic approach for depth, then apply the anti-patterns audit to ensure the prompts create space for reflection rather than feeling like a questionnaire.

**5. Running a stakeholder interview for enterprise software.** The CTO says they want "better analytics" but you suspect the real problem is trust in data quality. Use the decision archaeology technique from values elicitation ("walk me through the last time you made a decision using this dashboard") to surface the actual friction points.

## When to Use / When NOT to Use

**Use when:** You need conversations that go beyond surface answers -- user research interviews, persona discovery, conversational AI design, life review products, or any situation where understanding motivation matters more than collecting facts.

**Do NOT use for:**
- **Clinical diagnosis or treatment** -- this skill is research/design-oriented, not therapeutic. Use a licensed professional.
- **Structured survey design** -- if you only need facts (age, job title, stated preferences), use standard survey methodology.
- **Persona creation from scratch** -- use [persona-definition](../persona-definition/) to build personas from research data, then use this skill to design the conversations that feed it.
- **Stakeholder mapping** -- use [persona-mapping](../persona-mapping/) for Power-Interest matrices and RACI charts.

## Attribution

Research foundations by Singer, McAdams, Miller & Rollnick, Schwartz, Young, Haight, Birren, and Pennebaker. Original skill content from [tasteray/skills](https://github.com/tasteray/skills). Curated, restructured into progressive-disclosure form, and extended with anti-patterns reference and ethical guardrails by [Viktor Bezdek](https://github.com/viktorbezdek).

## Related Plugins in SkillStack

- **[Content Modelling](../content-modelling/)** -- Design content models with types, fields, relationships, and governance rules
- **[Navigation Design](../navigation-design/)** -- Information architecture, wayfinding systems, breadcrumbs, and navigation patterns
- **[Persona Definition](../persona-definition/)** -- Detailed user personas with demographics, goals, pain points, and empathy maps
- **[Persona Mapping](../persona-mapping/)** -- Stakeholder mapping using Power-Interest matrices, RACI charts, and influence analysis
- **[User Journey Design](../user-journey-design/)** -- User journey maps with touchpoints, emotional states, and pain points

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
