# Elicitation

> **v2.0.0** | Design & UX | 2 iterations

Psychological elicitation and deep-interview design using narrative identity (McAdams), self-defining memories (Singer), Motivational Interviewing OARS (Miller & Rollnick), values elicitation (Schwartz), schema detection (Young), life review (Haight/Birren), and linguistic analysis (Pennebaker/LIWC). Curated by [Viktor Bezdek](https://github.com/viktorbezdek) from the original [tasteray/skills](https://github.com/tasteray/skills) content and restructured into 8 progressive-disclosure references.

## What Problem Does This Solve

User interviews and research conversations routinely produce surface-level responses — stated preferences rather than underlying motivations, polished narratives rather than the formative experiences that actually shape behavior. Direct questioning triggers defensiveness; questionnaires capture what people think they should say. This skill applies seven evidence-based psychological frameworks to design conversations that create the conditions for authentic self-disclosure — revealing values, schemas, formative memories, and motivations that standard interviews miss.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "I want to understand what really drives my users, not just what they tell me they want" | Values elicitation techniques (role model, opposite day, decision archaeology, anger-as-signal) grounded in Schwartz's 10 Universal Values framework |
| "Design a user interview script that goes beyond surface answers" | OARS framework with four reflection types (simple/complex/amplified/double-sided) and the 2:1 reflection-to-question ratio that governs all elicitation |
| "Help me discover the formative experiences that shape a user's mental model" | Self-defining memory elicitation frames ("keeps coming back", "explains who I am", "turning point") targeting the reminiscence bump (ages 10-30) |
| "I'm building a conversational AI that needs to understand user personality over time" | Linguistic markers for personality (LIWC pronoun patterns, cognitive complexity, emotional tone), schema detection via Downward Arrow, narrative theme analysis |
| "Write a life review interview guide for a personal history product" | Barbara Haight's stage-by-stage sequences (childhood → later life) combined with Birren's thematic approach (family, work, money, health, death, meaning) |
| "How do I build rapport in a conversation before asking personal questions?" | Seven anti-patterns to avoid (interrogation trap, interpretation leap, agenda push, premature depth, therapy cosplay, monologue response, validation trap) with concrete fixes |
| "Critique this interview transcript for missed depth opportunities" | Self-audit protocol scanning for all seven anti-patterns with specific signal-to-watch-for markers |

## When NOT to Use This Skill

- **Clinical diagnosis or treatment** — this skill is research/design-oriented, not therapeutic. Use a licensed professional.
- **Structured survey design** — if you only need facts (age, job title, stated preferences), use standard survey methodology. This skill is for depth.
- **Persona creation from scratch** — use the [persona-definition](../persona-definition/) skill to build personas from research data, then use this skill to design the research conversations that feed it.
- **Stakeholder mapping** — use the [persona-mapping](../persona-mapping/) skill for Power-Interest matrices and influence analysis.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install elicitation@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

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

**Natural language triggers** — Claude activates this skill automatically when you mention:

`elicitation` · `deep interview` · `user research` · `motivational interviewing` · `narrative identity` · `OARS` · `life review` · `values elicitation` · `schema detection` · `psychological profiling`

## What's Inside

**Lean SKILL.md** with core principle, when-to-use / when-not-to-use, domain routing table, and reasoning sequence. Loads one or more of these references progressively based on the query:

### 8 reference files

- **`self-defining-memories.md`** — Singer's five criteria for memory salience, three conversational frames that elicit memories without interrogation, and the reminiscence bump (ages 10-30) where identity forms
- **`narrative-identity.md`** — McAdams' 8-scene life story interview with conversational adaptations, and the four narrative themes (agency, communion, redemption, contamination) that predict well-being better than the events themselves
- **`motivational-interviewing.md`** — The OARS framework with all four reflection types (simple/complex/amplified/double-sided), the 2:1 reflection-to-question ratio as operational target, and the hierarchy of question types when questions are necessary
- **`values-elicitation.md`** — Schwartz's 10 universal values with four indirect elicitation techniques (role model, opposite day, decision archaeology, anger-as-signal) that surface values through behavior rather than self-report
- **`schema-detection.md`** — Young's 18 Early Maladaptive Schemas organized into five domains, the Downward Arrow technique for safely surfacing beliefs, and linguistic markers for each schema — with clear boundaries on clinical vs research use
- **`life-review-questions.md`** — Barbara Haight's stage-specific question sequences (childhood → later life) and James Birren's thematic approach (family, work, money, health, death, meaning), with guidance on combining both methods and pacing multi-session engagements
- **`linguistic-markers.md`** — Pennebaker/LIWC patterns (pronoun usage, cognitive complexity, emotional tone, temporal focus) with critical caveats about individual variation, cross-cultural limits, and the group-level-only validity of the findings
- **`anti-patterns.md`** — Seven anti-patterns (interrogation trap, interpretation leap, agenda push, premature depth, therapy cosplay, monologue response, validation trap) with mechanisms, concrete fixes, and a quick-audit table for self-review

## Version History

- `2.0.0` Major restructure: split 437-line SKILL.md into lean 150-line SKILL.md + 8 progressive-disclosure references, added "When NOT to Use" discrimination section, added domain routing table, added ethical guardrails section, added anti-patterns as auditable reference, attributed Viktor Bezdek as curator alongside the original tasteray content
- `1.0.0` Initial import from tasteray/skills

## Attribution

Research foundations by Singer, McAdams, Miller & Rollnick, Schwartz, Young, Haight, Birren, and Pennebaker. Original skill content from [tasteray/skills](https://github.com/tasteray/skills). Curated, restructured into progressive-disclosure form, and extended with anti-patterns reference and ethical guardrails by [Viktor Bezdek](https://github.com/viktorbezdek).

## Related Skills

- **[Content Modelling](../content-modelling/)** — Design content models with types, fields, relationships, and governance rules for structured content systems.
- **[Navigation Design](../navigation-design/)** — Design information architecture, wayfinding systems, breadcrumbs, and navigation patterns.
- **[Persona Definition](../persona-definition/)** — Create detailed user personas with demographics, goals, pain points, behaviors, and empathy maps from research data.
- **[Persona Mapping](../persona-mapping/)** — Map stakeholders and personas using Power-Interest matrices, RACI charts, and influence analysis.
- **[User Journey Design](../user-journey-design/)** — Map user journeys with touchpoints, emotional states, pain points, and opportunities.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — 50 production-grade plugins for Claude Code.
