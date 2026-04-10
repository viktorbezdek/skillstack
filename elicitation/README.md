# Elicitation

> **v1.0.0** | Design & UX | 0 iterations

Psychological profiling through natural conversation using narrative identity, self-defining memory elicitation, Motivational Interviewing (OARS), values elicitation, and schema detection.

## What Problem Does This Solve

User interviews and research conversations routinely produce surface-level responses — stated preferences rather than underlying motivations, polished narratives rather than the formative experiences that actually shape behavior. Direct questioning triggers defensiveness; questionnaires capture what people think they should say. This skill applies three evidence-based psychological frameworks (McAdams narrative identity, Singer self-defining memory elicitation, Miller & Rollnick Motivational Interviewing) to design conversations that create the conditions for authentic self-disclosure, revealing values, schemas, and motivations that standard interviews miss.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "I want to understand what really drives my users, not just what they tell me they want" | Values elicitation techniques (role model, opposite day, decision archaeology, anger-as-signal) grounded in Schwartz's 10 Universal Values framework |
| "Design a user interview script that goes beyond surface answers" | OARS framework (Open questions, Affirmations, Reflections, Summaries) with the 2:1 reflection-to-question ratio and conversational adaptation patterns |
| "Help me discover the formative experiences that shape a user's mental model" | Self-defining memory elicitation frames (the "keeps coming back" frame, "explains who I am" frame, "turning point" frame) targeting the reminiscence bump |
| "I'm building a conversational AI that needs to understand user personality over time" | Linguistic markers for personality (LIWC patterns), schema detection via Downward Arrow technique, and narrative theme analysis (agency vs. communion) |
| "Write a life review interview guide for a personal history product" | Barbara Haight's structured question sequences by life stage (childhood, adolescence, early adulthood, middle, later life) |
| "How do I build rapport in a conversation before asking personal questions?" | Anti-patterns to avoid (interrogation trap, premature depth, therapy cosplay) and graduated disclosure strategies using McAdams' 8-scene life story structure |

## Installation

```bash
claude install-plugin github:viktorbezdek/skillstack/elicitation
```

## How to Use

**Direct invocation:**

```
Use the elicitation skill to ...
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `elicitation`
- `user-research`
- `motivational-interviewing`
- `narrative-identity`
- `psychological-profiling`

## What's Inside

- **Goal** -- The scoring framework: evaluate all elicitation work on a 0-10 scale with specific feedback, iterating until the work embodies the core principle of depth through patience.
- **Core Principle** -- The foundational insight that depth comes from creating safety for self-disclosure, not from probing — with the key finding that people want to tell their stories.
- **Three Research Traditions** -- Synthesis of the three complementary frameworks: Autobiographical Memory Research (Singer), Narrative Identity Theory (McAdams), and Motivational Interviewing (Miller & Rollnick).
- **Self-Defining Memories** -- Singer's five criteria for memory salience, three conversational frames for eliciting them, and a table mapping memory features to personality insights.
- **Life Story Interview: 8 Key Scenes** -- McAdams' eight scene types (high point, low point, turning point, earliest memory, etc.) with conversational adaptations and narrative theme patterns to listen for.
- **OARS Framework** -- The four MI skills (Open questions, Affirmations, Reflections, Summaries) with examples of all four reflection types and the 2:1 reflection-to-question ratio guideline.
- **Values Elicitation** -- Schwartz's 10 Universal Values taxonomy plus four indirect elicitation techniques that surface values through behavior rather than self-report.
- **Schema Detection** -- Young's 18 Early Maladaptive Schemas organized by domain, the Downward Arrow technique for surfacing beliefs beneath surface concerns, and linguistic markers for each schema.

## Related Skills

- **[Content Modelling](../content-modelling/)** -- Design content models with types, fields, relationships, and governance rules for structured content systems.
- **[Navigation Design](../navigation-design/)** -- Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns for documentation and applicat...
- **[Ontology Design](../ontology-design/)** -- Design knowledge models with classes, properties, relationships, and taxonomies for structured data representation.
- **[Persona Definition](../persona-definition/)** -- Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps.
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 49 production-grade plugins for Claude Code.
