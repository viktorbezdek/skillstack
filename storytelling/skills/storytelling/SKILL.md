---
name: storytelling
description: Expert guidance for writing, editing, and teaching stories across fiction, business, data, speech, UX, and interactive narrative. Covers canonical story structures (3-act, Hero's Journey, Story Circle, Save the Cat, Kishōtenketsu, Freytag, Fichtean), business narrative frameworks (StoryBrand, Pixar Spine, Before-After-Bridge, founder story, brand archetypes), data storytelling (Knaflic patterns, situation-complication-resolution), speech writing (Duarte SparkLines, TED structure, Monroe's Motivated Sequence), narrative craft (character design with want/need, scene/sequel, dialogue subtext, POV, pacing), interactive narrative (branching, environmental storytelling, ludonarrative), narrative theory (Propp 31 functions, Polti 36 situations, Booker 7 plots, Campbell monomyth, Greimas), and seven craft anti-patterns (info dump, Mary Sue, deus ex machina, "as you know Bob", telling not showing, moral misalignment, manufactured conflict). Use when writing or editing stories, designing pitches or presentations, structuring case studies, drafting speeches, planning interactive narratives, critiquing existing narrative work, or teaching storytelling principles.
---

# Storytelling

> A story is not a sequence of events. It is a sequence of *caused* events that changes a character in a way the audience cares about. Everything in this skill flows from that definition.

This skill covers story craft across every domain where narrative is a tool: fiction, business pitches, data presentations, speeches, UX scenarios, and interactive media. It loads focused references on demand rather than front-loading everything, because the right structure for a product pitch is not the right structure for a memoir.

---

## When to use this skill

- **Writing fiction or creative nonfiction** — short stories, novels, memoir, screenplays
- **Business pitches and founder stories** — investor decks, sales narratives, customer case studies
- **Data presentations** — turning a dashboard into a story, executive briefings, report structure
- **Speeches and keynotes** — TED-style talks, all-hands presentations, ceremonies
- **UX scenarios and design fiction** — user journey narratives, speculative design storytelling
- **Interactive narrative** — game writing, branching story systems, environmental storytelling
- **Editing and critique** — diagnosing why a story isn't working and giving concrete fixes
- **Teaching narrative** — explaining story principles to writers, designers, or founders

## When NOT to use this skill

- **Plain technical documentation** — API references, changelogs, configuration guides. Use the `documentation-generator` skill.
- **UX writing microcopy** — button labels, error messages, form instructions. Use the `ux-writing` skill.
- **Literal journalism** — hard news, fact reporting. Storytelling principles inform the form but journalism has its own ethics and constraints.
- **Clinical/therapeutic narrative work** — therapy uses narrative but requires licensed professional context. Use [elicitation](../elicitation/) for research-oriented conversation design only.
- **Persona creation** — use `persona-definition` (though storytelling helps you animate personas once defined).

---

## Core principles (always apply)

Before loading any reference, hold these five principles. They are non-negotiable regardless of domain:

1. **Story = causality + change + stakes.** A sequence of events is not a story. A story is events where *because* this happened, *that* happened, and the change matters to a character the audience is invested in. If you cannot say "because", you have chronology, not narrative.

2. **Specificity is power.** Abstractions disappear; concrete details stick. "She was nervous" does nothing. "Her coffee shook in the cup" does everything. Apply this to business stories too — not "our customers struggled with onboarding" but "on day three, 47% of new users had not yet completed their first action".

3. **Conflict is the engine.** No conflict, no story. Conflict does not have to mean fighting — it can be a decision under pressure, a reconciliation of opposing values, an external obstacle, or an internal contradiction. But there must be friction between what the protagonist wants and what the situation allows.

4. **Show, don't tell — when possible.** Show when you want the audience to *feel* something. Tell when you need to move past information efficiently. Most narrative failures come from telling where showing is needed (emotional beats, revelations, climaxes) and showing where telling is needed (basic context, time jumps, logistics). See `anti-patterns.md`.

5. **The ending earns everything.** Audiences tolerate weak openings if the ending rewards them. A weak ending poisons even the best opening. Work backward from how the story ends and what it means — not forward from a clever premise.

---

## Domain routing

Load ONLY the references that match the query. Do not pre-load everything — this skill is designed for progressive disclosure.

### Foundations (usually load one of these first)

| Query | Load |
|---|---|
| "What makes something a story? What are the basic elements?" | `references/narrative-fundamentals.md` |
| "Which story structure should I use?" — 3-act, Hero's Journey, Story Circle, Save the Cat, Kishōtenketsu, Freytag, Fichtean, StoryBrand, Pixar Spine, with a decision framework | `references/story-structures.md` |

### Craft for long-form narrative

| Query | Load |
|---|---|
| Character design: want vs. need, arcs, flaws, dimensionality, internal conflict | `references/character-design.md` |
| Scene construction, pacing, MRUs (motivation-reaction units), scene/sequel, beat structure, tension curves | `references/scene-and-pacing.md` |
| Writing dialogue: subtext, voice differentiation, "on the nose" problems, interiority, attribution | `references/dialogue.md` |
| Point of view: choosing POV, psychic distance, unreliable narrators, head-hopping | `references/point-of-view.md` |

### Applied storytelling

| Query | Load |
|---|---|
| Business pitch, founder story, StoryBrand (Miller), Pixar Spine, Before-After-Bridge, brand archetypes (Mark & Pearson), customer case studies | `references/business-storytelling.md` |
| Data storytelling, turning charts into narrative, situation-complication-resolution, Knaflic patterns, executive briefings | `references/data-storytelling.md` |
| Speech and presentation writing, Duarte SparkLines, TED structure, Monroe's Motivated Sequence, Aristotelian rhetoric, keynote planning | `references/speech-and-presentation.md` |
| Interactive narrative, game writing, branching vs. state-based, environmental storytelling, ludonarrative dissonance, emergent narrative | `references/interactive-narrative.md` |

### Diagnostics

| Query | Load |
|---|---|
| Why isn't this story working? — auditing for info dump, Mary Sue, deus ex machina, "as you know Bob", telling-not-showing, moral misalignment, manufactured conflict | `references/anti-patterns.md` |
| Theoretical grounding: Propp's 31 functions, Polti's 36 situations, Booker's 7 plots, Tobias's 20 master plots, Campbell's monomyth, Genette's narratology, Greimas' actantial model | `references/narrative-theory.md` |

### Multi-domain queries

If a query spans multiple areas (e.g., "write a data-driven pitch that tells our customer's story"), load:
- One structure reference (`story-structures.md` or `business-storytelling.md`)
- One craft reference (`character-design.md` for the customer as protagonist)
- `anti-patterns.md` for the self-audit pass

Three is usually the right number. Loading more than four references indicates the query is not focused enough — consider asking the user to narrow it.

---

## Reasoning sequence (apply to every response)

1. **Identify the use context.** Fiction? Pitch? Speech? Interactive? This determines which references to load and which principles dominate.
2. **Ask about the audience** if not stated. Story decisions collapse without an audience in mind. A founder story for investors is different from the same founder story for employees.
3. **Load the matching reference(s).** Progressive disclosure, not everything-at-once.
4. **Work structure before surface.** Fix the skeleton before polishing the prose. A beautifully written story with no structure fails; an ugly draft with strong structure is editable into something great.
5. **Ground abstractions.** Any time you use a craft term (arc, stakes, subtext, beat), give a concrete example from the user's actual material. Never leave a craft concept hanging as vocabulary.
6. **Audit against anti-patterns.** Before concluding, check the draft against `anti-patterns.md`. Most narrative failures are anti-patterns, not missing principles.
7. **Connect to meaning.** Every story answers the implicit question "so what?" Make sure the draft has an answer — not as a moral, but as a felt point.

---

## Reference files

| File | Contents | Typical size |
|---|---|---|
| `narrative-fundamentals.md` | What a story is, four core elements (character, desire, obstacle, transformation), causality test, specificity, the so-what question | ~160 lines |
| `story-structures.md` | 9 canonical structures side-by-side (3-act, Freytag, Fichtean, Hero's Journey, Story Circle, Save the Cat, Kishōtenketsu, StoryBrand, Pixar Spine), decision framework for choosing | ~260 lines |
| `character-design.md` | Want vs. need, flaws, arcs (positive/flat/negative), dimensionality, internal/external conflict, supporting cast roles, the "Save the Cat" beat | ~220 lines |
| `scene-and-pacing.md` | Scene/sequel model, motivation-reaction units, beat structure, pacing techniques, tension curves, chapter endings, act breaks | ~220 lines |
| `dialogue.md` | Subtext vs. text, voice differentiation, interiority, "as you know Bob" problem, on-the-nose dialogue, attribution, dialect | ~180 lines |
| `point-of-view.md` | POV selection (1st, 3rd limited, 3rd omniscient, 2nd), psychic distance, head-hopping, unreliable narrators, POV character selection | ~170 lines |
| `business-storytelling.md` | StoryBrand 7-part framework, Pixar Spine, Before-After-Bridge, founder stories, brand archetypes (12), customer case structure, pitch narrative | ~260 lines |
| `data-storytelling.md` | Knaflic 6 lessons, situation-complication-resolution, charts as narrative devices, executive briefing structure, story-of-the-data vs. story-in-the-data | ~200 lines |
| `speech-and-presentation.md` | Duarte SparkLine (current/ideal contrast), TED 18-minute structure, Monroe's Motivated Sequence, Aristotelian rhetoric (ethos/pathos/logos), opening and closing patterns | ~220 lines |
| `interactive-narrative.md` | Branching vs. state-based, environmental storytelling, ludonarrative dissonance, player agency, emergent narrative, quest design patterns | ~200 lines |
| `anti-patterns.md` | 7 anti-patterns (info dump, Mary Sue, deus ex machina, "as you know Bob", telling not showing, moral misalignment, manufactured conflict) with diagnosis signals and concrete fixes | ~220 lines |
| `narrative-theory.md` | Propp's 31 functions, Polti's 36 dramatic situations, Booker's 7 basic plots, Tobias's 20 master plots, Campbell's monomyth stages, Genette's narratology terms, Greimas actantial model | ~240 lines |

---

> *Storytelling skill by [Viktor Bezdek](https://github.com/viktorbezdek) — licensed under MIT.*
