# Storytelling

> **v1.0.0** | Design & UX | 1 iteration

Storytelling craft and application across fiction, business, data, speech, UX, and interactive narrative. Covers 9 canonical story structures, character design, scene construction, dialogue, POV, business storytelling frameworks (StoryBrand, Pixar Spine, Before-After-Bridge), data storytelling, speech writing, interactive narrative, and narrative theory -- organized for progressive disclosure across 12 references.

## What Problem Does This Solve

Most people who need to tell stories -- writers, founders, presenters, designers, data analysts -- either lack a systematic framework or have been taught exactly one (usually Hollywood 3-act) and try to force every situation into it. The result is pitches that cast the company as the hero instead of the guide, fiction drafts that collapse in act two, data presentations that list findings without arguing a point, and speeches that give the audience no reason to remember anything. Different contexts require different structures, and the craft elements (character, scene, dialogue, pacing) work differently in a founder story than in a novel chapter. This skill provides the right framework for each context rather than a one-size-fits-all answer, with progressive disclosure that loads only the references you actually need.

## When to Use This Skill

| You say... | The skill provides... |
|---|---|
| "My story is flat in the middle -- I don't know what's wrong" | Scene/sequel diagnosis, midpoint reversal patterns, tension curve analysis, and anti-pattern audit for manufactured conflict or info dump |
| "Help me write a pitch that actually works for investors" | StoryBrand 7-part framework ("company as guide, not hero"), three-box pitch structure, and founder story template with crucible moment |
| "How do I turn this dashboard into a story an exec will act on?" | Situation-Complication-Resolution (Minto pyramid), Knaflic's 6 lessons, answer-first executive briefing, single-sentence chart headlines |
| "Which story structure should I use?" | Side-by-side comparison of 9 canonical structures (3-act, Freytag, Fichtean, Hero's Journey, Story Circle, Save the Cat, Kishotenketsu, StoryBrand, Pixar Spine) with a decision framework |
| "My dialogue is on the nose -- every character sounds like me" | Text-vs-subtext diagnosis, voice differentiation test, interiority balance, three-beat rule, and fixes for "as you know, Bob" exposition |

## When NOT to Use This Skill

- Plain technical documentation (API references, config guides) -- use [documentation-generator](../documentation-generator/) instead
- UX microcopy (button labels, error messages, form copy) -- use [ux-writing](../ux-writing/) instead
- Persona definition from scratch -- use [persona-definition](../persona-definition/), then use storytelling to animate personas in narratives
- Hard news journalism -- storytelling informs the form but journalism has its own ethical constraints

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
Use the storytelling skill to structure a founder story for a 5-minute investor pitch
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `story structure`
- `narrative`
- `hero's journey`
- `story circle`
- `save the cat`
- `storybrand`
- `pixar spine`
- `pitch narrative`
- `data storytelling`
- `dialogue craft`
- `character arc`

## What's Inside

This plugin uses a lean SKILL.md with five non-negotiable core principles and a domain routing table that loads references on demand. The SKILL.md never front-loads all 12 references -- it loads only the ones matching the query.

### Core Skill

| Component | Purpose |
|---|---|
| `SKILL.md` | Five core principles (causality, specificity, conflict, show-vs-tell, earned ending), domain routing table, reasoning sequence, and reference index |

### Foundations (2 references)

| Reference | Contents |
|---|---|
| `narrative-fundamentals.md` | What a story is, four core elements (character, want, obstacle, transformation), the causality test, specificity principle, the "so what?" question |
| `story-structures.md` | 9 canonical structures side-by-side with a decision framework for matching structure to domain, length, and conflict requirements |

### Craft for Long-Form Narrative (4 references)

| Reference | Contents |
|---|---|
| `character-design.md` | Want vs. need, flaw-arc linkage, three arc types (positive/flat/negative), Forster's round characters, Vogler's supporting cast archetypes |
| `scene-and-pacing.md` | Swain's scene/sequel model, Motivation-Reaction Units, beat structure, tension curves, chapter endings, middle-sag diagnosis |
| `dialogue.md` | Text vs. subtext, voice differentiation, on-the-nose fixes, interiority balance, attribution, dialect, silence as dialogue |
| `point-of-view.md` | POV selection, Gardner's psychic distance, head-hopping, unreliable narrator types, filter words to delete in deep POV |

### Applied Storytelling (4 references)

| Reference | Contents |
|---|---|
| `business-storytelling.md` | StoryBrand 7-part framework, Pixar Spine, Before-After-Bridge, founder story structure, 12 brand archetypes (Mark & Pearson), customer case study template |
| `data-storytelling.md` | Exploratory vs. explanatory modes, Situation-Complication-Resolution (Minto), Knaflic's 6 lessons, Z-pattern executive briefings, single-sentence chart headlines |
| `speech-and-presentation.md` | Duarte SparkLine (what-is / what-could-be), TED 18-minute structure, Monroe's Motivated Sequence, Aristotelian rhetoric, opening and closing patterns |
| `interactive-narrative.md` | Branching vs. state-based, cheap-branching trap, environmental storytelling, ludonarrative dissonance, player agency, quest patterns |

### Diagnostics (2 references)

| Reference | Contents |
|---|---|
| `anti-patterns.md` | 7 anti-patterns with diagnostic signals and fixes: info dump, Mary Sue, deus ex machina, "as you know Bob", telling not showing, moral misalignment, manufactured conflict |
| `narrative-theory.md` | Propp's 31 functions, Polti's 36 situations, Booker's 7 plots, Tobias's 20 master plots, Campbell's monomyth, Genette's narratology, Greimas's actantial model |

## Usage Scenarios

**Scenario 1 -- Structuring a founder pitch.** You need a 5-minute investor pitch. The skill loads `business-storytelling.md`, applies the StoryBrand framework (your company is the guide, the customer is the hero), structures the narrative as crucible -> search -> insight -> bet, and audits against the "company as hero" anti-pattern.

**Scenario 2 -- Diagnosing a saggy middle.** Your novel's second act drags. The skill loads `scene-and-pacing.md`, runs a scene/sequel analysis, identifies missing midpoint reversals and tension curve dips, checks for info-dump anti-patterns, and suggests structural fixes (stakes escalation, subplot intersection, ticking clock).

**Scenario 3 -- Turning data into an executive briefing.** You have quarterly metrics that need to convince a C-suite audience. The skill loads `data-storytelling.md`, applies Situation-Complication-Resolution structure, converts chart titles from labels ("Q3 Revenue") to single-sentence headlines ("Q3 revenue grew 12% driven by enterprise expansion"), and arranges the narrative answer-first.

**Scenario 4 -- Writing a TED-style talk.** You are preparing an 18-minute keynote. The skill loads `speech-and-presentation.md`, applies Duarte's SparkLine pattern (oscillating between "what is" and "what could be"), maps Monroe's Motivated Sequence (attention -> need -> satisfaction -> visualization -> action), and tests the opening for a specific, concrete hook.

**Scenario 5 -- Critiquing a short story.** A writer shares a draft that "doesn't land." The skill loads `anti-patterns.md` and `narrative-fundamentals.md`, runs the causality test (are events caused or just sequential?), identifies anti-patterns (telling where showing is needed, Mary Sue protagonist), and provides concrete rewrite suggestions grounded in the specific text.

## Related Skills

- **[UX Writing](../ux-writing/)** -- Interface copy, microcopy, and error messages -- the tactical side of product language.
- **[Persona Definition](../persona-definition/)** -- Define user personas before writing stories about them.
- **[User Journey Design](../user-journey-design/)** -- Map user journeys with touchpoints and emotional states; storytelling turns journeys into persuasive narratives.
- **[Prompt Engineering](../prompt-engineering/)** -- When the story needs to be told by an AI system, prompt engineering controls how.
- **[Example Design](../example-design/)** -- Effective examples are a form of technical storytelling with progressive complexity.

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- 52 production-grade plugins for Claude Code.
