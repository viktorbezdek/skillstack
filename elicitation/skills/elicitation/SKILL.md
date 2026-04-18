---
name: elicitation
description: Psychological elicitation and deep-interview design using narrative identity (McAdams), self-defining memories (Singer), Motivational Interviewing (Miller & Rollnick OARS), values elicitation (Schwartz), schema detection (Young), and life review (Haight/Birren). Use when designing user interviews that need to reveal motivations rather than stated preferences, writing conversation flows for personal discovery, auditing interview scripts for interrogation anti-patterns, building conversational AI that understands users over time, drafting life story or personal history products, or critiquing a conversation transcript for missed depth. NOT for clinical diagnosis, therapy, or treatment planning. NOT for structured data capture or survey design (use standard survey tools). NOT for persona creation from scratch (use persona-definition). NOT for stakeholder mapping (use persona-mapping).
---

# Elicitation

> Depth comes from patience, not probing. The most revealing information emerges when people feel safe to share, not when they are questioned.

This skill applies evidence-based psychological frameworks to design conversations that create the conditions for authentic self-disclosure — revealing values, schemas, formative memories, and motivations that standard interviews miss.

---

## When to use this skill

- **Interview design** — writing question sequences for user research, life review, personal history, or narrative discovery
- **Conversation critique** — auditing a transcript, script, or flow for interrogation anti-patterns and missed depth opportunities
- **Values discovery** — surfacing what actually drives a person vs. what they say drives them
- **Schema detection** — identifying stable belief patterns that shape behavior across contexts
- **Conversational AI design** — building agents that elicit psychological depth ethically over long sessions
- **Narrative analysis** — interpreting stories people tell for themes of agency, communion, redemption, contamination

## When NOT to use this skill

- **Clinical diagnosis or treatment** — this skill is research/design-oriented, not therapeutic. Use a licensed professional.
- **Structured data capture** — if you only need facts (age, job title, preferences), use standard survey design. This skill is for depth, not breadth.
- **Persona creation from scratch** — use the `persona-definition` skill for building individual user personas from research data, then use this skill to design the research conversations that feed it.
- **Stakeholder mapping** — use the `persona-mapping` skill for Power-Interest matrices and RACI charts across an organization.

---

## How to use this skill

On every query, first read the core principle below, then load ONLY the references relevant to the specific query. Do not pre-load all references — progressive disclosure prevents context bloat.

### Core principle (always apply)

**Depth through patience, not probing.** People want to tell their stories — they rarely get the chance. Your role is to create conversational space where disclosure feels natural, not extracted. Three non-negotiables:

1. **Reflections outperform questions.** Target a 2:1 reflection-to-question ratio. Questions gather; reflections invite elaboration. See `references/motivational-interviewing.md`.
2. **Earn depth incrementally.** Never ask deeply personal questions before trust is established. Start with easier territory and let the person's energy guide where to go deeper.
3. **Follow their lead, not your agenda.** Their emphasis is data. Steering toward topics you consider important signals you are not actually listening.

### Domain routing

| Query topic | Load reference |
|---|---|
| Interview structure across life stages, sequences for childhood/adolescence/adult periods, guided autobiography themes | `references/life-review-questions.md` |
| Eliciting formative memories, conversational frames for "memories that keep coming back", what vivid memories reveal about personality | `references/self-defining-memories.md` |
| McAdams life story interview, 8 key scenes, narrative theme analysis (agency/communion/redemption/contamination), narrative identity assessment | `references/narrative-identity.md` |
| OARS framework, reflection types (simple/complex/amplified/double-sided), 2:1 ratio mechanics, summary structure, reducing resistance | `references/motivational-interviewing.md` |
| Surfacing underlying values, Schwartz 10 universal values, role-model/opposite-day/decision-archaeology/anger techniques | `references/values-elicitation.md` |
| Detecting stable belief patterns (Young's 18 Early Maladaptive Schemas), Downward Arrow technique, schema domains, linguistic markers of schemas | `references/schema-detection.md` |
| LIWC language analysis, pronoun patterns, cognitive complexity markers, caveats about individual variation and cultural differences | `references/linguistic-markers.md` |
| Interrogation trap, interpretation leap, agenda push, premature depth, therapy cosplay, monologue response, validation trap | `references/anti-patterns.md` |
| Conversation critique / self-audit of a draft script | Load `references/anti-patterns.md` first, then the specific framework references for the techniques in the script |
| Multi-domain query | Load relevant references and synthesize — typically `motivational-interviewing.md` is always relevant |

### Reasoning sequence (apply to every response)

1. **Understand the use context.** Research interview? Life history? Conversational AI? Script critique? The use context determines which frameworks apply.
2. **Check trust stage.** Is this a first-contact or an established relationship? Early-stage conversations need graduated disclosure; late-stage can go deeper earlier.
3. **Load the matching reference(s).** Do not dump all techniques into the response — pick the ones that fit the specific situation.
4. **Design for reflections, not questions.** Every proposed question should come with one or two matching reflection moves for when the answer arrives.
5. **Flag anti-patterns explicitly** when reviewing existing content. Name which anti-pattern is present and show the concrete fix, not just "avoid this".
6. **Respect the ethical boundary.** Elicitation creates intimacy; that intimacy can be abused. Flag consent, withdrawal rights, and psychological safety whenever designing a real-world application.

---

## Three research traditions (one-paragraph summary)

| Tradition | Key researcher | Key finding | When it applies |
|---|---|---|---|
| **Autobiographical memory** | Jefferson Singer | Self-defining memories (vivid, emotionally intense, rehearsed, linked to enduring concerns) are the building blocks of personality | When you want to understand what shapes someone, not just what they currently think |
| **Narrative identity** | Dan McAdams | The *themes* people use in their stories (redemption vs. contamination, agency vs. communion) predict well-being better than the events themselves | When you want to interpret what a person's stories mean about how they see themselves |
| **Motivational interviewing** | Miller & Rollnick | Reflections outperform questions at eliciting disclosure; the 2:1 reflection-to-question ratio is the operational target | Always — this is the *how* for all other traditions |

---

## Ethical guardrails (always apply)

Elicitation is powerful because it creates the conditions for people to reveal what they normally keep private. That power carries responsibility. When designing real-world applications:

- **Consent must be specific, not general.** "I agree to a user interview" is not consent to discuss childhood trauma. Re-consent as depth increases.
- **Withdrawal must be friction-free.** People should be able to stop, skip, or retract without having to justify themselves.
- **This is not therapy.** If someone discloses something that needs professional support, name that clearly and redirect — do not improvise.
- **Stored disclosures are sensitive.** Any system that persists elicited data must treat it with the care you would want for your own most private memories.
- **Cross-cultural validity is limited.** The frameworks here are primarily derived from WEIRD (Western, Educated, Industrialized, Rich, Democratic) research. Adapt carefully to other contexts.

---

> *Elicitation Skill — built on research by Singer, McAdams, Miller & Rollnick, Schwartz, Young, Haight, Birren, and Pennebaker. Curated and restructured by [Viktor Bezdek](https://github.com/viktorbezdek) from the original [tasteray/skills](https://github.com/tasteray/skills) content. Licensed under MIT.*
