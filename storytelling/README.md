# Storytelling

> **v1.0.0** | Design & UX | 1 iteration

Storytelling craft and application across fiction, business, data, speech, UX, and interactive narrative. Covers 9 canonical story structures, character design, scene construction, dialogue, POV, business storytelling frameworks (StoryBrand, Pixar Spine, Before-After-Bridge), data storytelling, speech writing, interactive narrative, and narrative theory — organized for progressive disclosure across 12 references.

## What Problem Does This Solve

Most practitioners who need to tell stories — writers, founders, presenters, designers, data analysts — either lack a systematic framework or have been taught exactly one (usually Hollywood 3-act) and try to force every situation into it. The result is weak pitches that treat the company as the hero, fiction drafts that collapse in act two, data presentations that list findings instead of arguing a point, and speeches that never give the audience a reason to remember anything. This skill provides the right framework for each context, not a one-size-fits-all answer.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My story is flat in the middle — I don't know what's wrong" | Scene/sequel diagnosis, midpoint reversal patterns, tension curve analysis, and anti-pattern audit for manufactured conflict or info dump |
| "Help me write a pitch that actually works for investors" | StoryBrand 7-part framework with "company as guide, not hero" principle, three-box pitch structure, and founder story template with crucible moment |
| "How do I turn this dashboard into a story an executive will act on?" | Situation-Complication-Resolution (Minto pyramid), Knaflic's 6 lessons, answer-first executive briefing structure, single-sentence chart headlines |
| "Which story structure should I use — Hero's Journey, 3-act, Kishōtenketsu?" | Side-by-side comparison of 9 canonical structures with decision framework matched to domain, length, and conflict requirements |
| "My main character feels hollow" | Want vs. need framework, the flaw-as-arc-engine principle, three arc types (positive/flat/negative), and supporting cast archetype roles |
| "My dialogue is on the nose — every character sounds like me" | Text-vs-subtext diagnosis, voice differentiation test, interiority balance, the three-beat rule, and fixes for "as you know, Bob" exposition |
| "Write me a TED-style talk opening" | Duarte SparkLine (current/ideal contrast), Monroe's Motivated Sequence, Aristotelian rhetoric balance, and working opening/closing patterns |
| "Critique this draft for narrative anti-patterns" | Self-audit against 7 anti-patterns (info dump, Mary Sue, deus ex machina, "as you know Bob", telling-not-showing, moral misalignment, manufactured conflict) |
| "I'm designing a branching game — how do I handle player agency?" | Branching vs state-based tradeoffs, ludonarrative dissonance, cheap-branching trap, environmental storytelling patterns |
| "I need the theoretical grounding — Propp, Booker, Campbell" | Side-by-side coverage of narrative theory (Propp's 31 functions, Polti's 36 situations, Booker's 7 plots, Tobias's 20, Campbell's monomyth, Genette, Greimas) |

## When NOT to Use This Skill

- **Plain technical documentation** — API references and config guides. Use the [documentation-generator](../documentation-generator/) skill.
- **UX microcopy** — button labels, error messages, form copy. Use the [ux-writing](../ux-writing/) skill.
- **Hard news journalism** — storytelling informs the form but news has its own ethical constraints.
- **Clinical or therapeutic narrative** — therapy uses narrative but requires licensed professional context.
- **Persona definition from scratch** — use [persona-definition](../persona-definition/), then use this skill to animate the persona in stories.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install storytelling@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

## How to Use

**Direct invocation:**

```
Use the storytelling skill to critique this short story draft for anti-patterns
```

```
Use the storytelling skill to help me structure a founder story for a 5-minute investor pitch
```

```
Use the storytelling skill to turn this quarterly data report into an executive briefing
```

**Natural language triggers** — Claude activates this skill automatically when you mention:

`story structure` · `narrative` · `hero's journey` · `story circle` · `save the cat` · `storybrand` · `pixar spine` · `pitch narrative` · `data storytelling` · `speech writing` · `dialogue craft` · `character arc` · `scene pacing` · `interactive narrative`

## What's Inside

**Lean SKILL.md** with core principles (causality, specificity, conflict, show-vs-tell, earned ending), when-to-use / when-not-to-use, domain routing table, and reasoning sequence. Loads ONE or MORE of these 12 references based on query:

### Foundations (2 files)
- **`narrative-fundamentals.md`** — The causality test (chronology vs. narrative), four core elements (character, want, obstacle, transformation), three stakes layers (Harmon), specificity principle, the "so what?" test
- **`story-structures.md`** — 9 canonical structures side-by-side: Freytag, 3-Act, Fichtean, Hero's Journey (Campbell/Vogler), Story Circle (Harmon), Save the Cat (Snyder), Kishōtenketsu, StoryBrand (Miller), Pixar Spine — with decision framework matching structure to domain

### Craft for long-form narrative (4 files)
- **`character-design.md`** — Want vs. need, flaw-arc linkage, three arc types (positive/flat/negative), internal/external conflict, Forster's round characters, supporting cast archetypes (Vogler), antagonist as shadow
- **`scene-and-pacing.md`** — Dwight Swain's scene/sequel model, Motivation-Reaction Units, beats, tension curve management, chapter endings, act breaks, middle-sag diagnosis and fixes
- **`dialogue.md`** — Text vs. subtext, voice differentiation, on-the-nose fixes, interiority balance, attribution, dialect handling, silence as dialogue, the three-beat rule
- **`point-of-view.md`** — POV selection, psychic distance (Gardner), head-hopping, unreliable narrator types, POV character selection (who has most to lose), filter words to delete in deep POV

### Applied storytelling (4 files)
- **`business-storytelling.md`** — StoryBrand 7-part framework (with "company as guide" principle), Pixar Spine, Before-After-Bridge, founder story structure (crucible → search → insight → bet), 12 brand archetypes (Mark & Pearson), customer case study template, three-box pitch
- **`data-storytelling.md`** — Exploratory vs. explanatory modes, Situation-Complication-Resolution (Minto), Knaflic's 6 lessons, chart-as-narrative matching, Z-pattern executive briefings, pyramid principle, single-sentence chart headlines
- **`speech-and-presentation.md`** — Duarte SparkLine (what-is / what-could-be oscillation), TED 18-minute structure, Monroe's Motivated Sequence, Aristotelian ethos/pathos/logos balance, working opening and closing patterns, rule of three
- **`interactive-narrative.md`** — Branching vs. state-based, cheap-branching trap, environmental storytelling, ludonarrative dissonance, player agency vs. authored story tension, quest patterns, blank-slate vs. authored protagonists

### Diagnostics (2 files)
- **`anti-patterns.md`** — 7 anti-patterns with diagnostic signals and concrete fixes: info dump, Mary Sue, deus ex machina, "as you know, Bob", telling not showing, moral misalignment, manufactured conflict — plus a quick audit checklist
- **`narrative-theory.md`** — Theoretical grounding: Propp's 31 functions, Polti's 36 situations, Booker's 7 plots, Tobias's 20 master plots, Campbell's monomyth (with the universality caveat), Genette's narratology, Greimas's actantial model — for teaching and close analysis

## Version History

- `1.0.0` Initial release — 12 progressive-disclosure references covering fiction craft, business storytelling, data storytelling, speech writing, interactive narrative, anti-patterns, and narrative theory

## Related Skills

- **[UX Writing](../ux-writing/)** — Interface copy, microcopy, error messages (the tactical side of product language storytelling covers).
- **[Persona Definition](../persona-definition/)** — Define user personas before writing stories about them.
- **[User Journey Design](../user-journey-design/)** — Map user journeys with touchpoints and emotional states; storytelling turns journeys into persuasive narratives.
- **[Prompt Engineering](../prompt-engineering/)** — When the story needs to be told by an AI system.
- **[Example Design](../example-design/)** — Design effective code examples and tutorials; example design is a form of technical storytelling.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — 50 production-grade plugins for Claude Code.
