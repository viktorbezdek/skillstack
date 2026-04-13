# Storytelling

> **v1.0.0** | Design & UX | 1 iteration

> Expert guidance for writing, editing, and teaching stories across fiction, business, data, speech, UX, and interactive narrative -- from structural frameworks through craft technique to anti-pattern diagnosis.

## The Problem

Everyone says "tell a story" -- at the investor pitch, the all-hands presentation, the product demo, the case study, the keynote. But most people have no structural vocabulary for what makes a story actually work. They start with a chronological sequence of events ("first we did X, then we did Y, then we did Z") and wonder why the audience is not engaged. The sequence has no causality, no conflict, no transformation, and no stakes. It is a timeline, not a narrative.

Fiction writers face a different version of the same problem. They have instinct but no diagnostic framework. A chapter "feels wrong" but they cannot name why. The dialogue is "flat" but they do not know what subtext is or how to construct it. The plot "sags in the middle" but they have never heard of scene/sequel structure or motivation-reaction units. Without craft vocabulary, revision is guesswork -- changing words without changing structure.

The gap between knowing a story is weak and knowing how to fix it is vast. Story structures exist (the Hero's Journey, Save the Cat, the Story Circle) but most people either learn one and apply it everywhere, or learn them all and cannot choose between them. Business storytelling has its own frameworks (StoryBrand, Pixar Spine, Before-After-Bridge) but practitioners rarely connect them to the underlying narrative principles that make them work. Data storytelling is treated as chart decoration rather than narrative architecture. The result is that storytelling remains an art practiced by instinct rather than a craft practiced by principle -- even though the principles have been documented for decades.

## The Solution

This plugin provides a complete storytelling craft system across six domains: fiction, business narrative, data storytelling, speeches and presentations, UX scenarios, and interactive narrative. It is built on five non-negotiable core principles (story = causality + change + stakes, specificity is power, conflict is the engine, show vs. tell as a deliberate choice, the ending earns everything) and uses progressive disclosure to load domain-specific guidance only when relevant.

The skill covers nine canonical story structures (3-Act, Freytag's Pyramid, Fichtean Curve, Hero's Journey, Story Circle, Save the Cat, Kishotenketsu, StoryBrand, Pixar Spine) with a decision framework for choosing the right one. It includes deep craft references for character design (want vs. need, arcs, flaws), scene construction and pacing (scene/sequel, MRUs, tension curves), dialogue (subtext, voice differentiation, the "as you know Bob" problem), and point of view (psychic distance, unreliable narrators, head-hopping).

Seven documented anti-patterns (info dump, Mary Sue, deus ex machina, "as you know Bob", telling not showing, moral misalignment, manufactured conflict) provide diagnostic tools for identifying why a story is not working and concrete fixes for each failure mode. Theoretical grounding from Propp, Polti, Booker, Tobias, Campbell, Genette, and Greimas provides the intellectual framework behind the practical techniques.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| "Tell a story" advice with no structural vocabulary -- timelines instead of narratives | Nine canonical structures with a decision framework for choosing the right one for your domain and purpose |
| Fiction drafts that "feel wrong" but the writer cannot diagnose why | Seven anti-pattern diagnostics (info dump, Mary Sue, deus ex machina, etc.) with recognition signals and concrete fixes |
| Business pitches that are chronological summaries of what happened | StoryBrand, Pixar Spine, and Before-After-Bridge frameworks that structure the pitch as a narrative with conflict and transformation |
| Data presentations that decorate charts instead of telling a story | Knaflic patterns and situation-complication-resolution framework that turn data into narrative arguments |
| Flat dialogue where every character sounds the same | Subtext technique, voice differentiation patterns, and the "on the nose" diagnosis |
| Speeches that list points instead of moving audiences | Duarte SparkLines, Monroe's Motivated Sequence, and TED structure for presentations that create emotional resonance |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install storytelling@skillstack
```

### Verify installation

After installing, test with:

```
I'm writing a pitch for investors and it feels flat -- it's just a list of what our product does. Help me turn it into a story.
```

The skill should activate and apply business storytelling frameworks to restructure your pitch with conflict, transformation, and stakes.

## Quick Start

1. **Install** the plugin using the commands above
2. **Describe your storytelling challenge** naturally: `I need to write a keynote about our company's pivot -- we went from B2C to B2B and it changed everything`
3. The skill **identifies the domain** (speech/presentation + business narrative) and loads the matching references
4. It **applies the right structure** (Duarte SparkLine for the keynote, Before-After-Bridge for the pivot story) and grounds every technique in your actual material
5. Before concluding, it **audits against anti-patterns** to catch info dumps, telling-not-showing in key emotional beats, and manufactured conflict

## What's Inside

This is a single-skill plugin with 12 progressive-disclosure reference files covering every storytelling domain.

| Component | Purpose |
|---|---|
| `SKILL.md` | Core principles, domain routing table, reasoning sequence (7 steps applied to every response) |
| 12 reference files | Domain-specific deep guidance loaded on demand |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

**Key references:**

| Reference | Topic |
|---|---|
| `narrative-fundamentals.md` | What a story is: character, desire, obstacle, transformation, the causality test, the "so what?" question |
| `story-structures.md` | 9 canonical structures (3-Act, Freytag, Fichtean, Hero's Journey, Story Circle, Save the Cat, Kishotenketsu, StoryBrand, Pixar Spine) with decision framework |
| `character-design.md` | Want vs. need, flaws, arcs (positive/flat/negative), dimensionality, internal/external conflict, supporting cast roles |
| `scene-and-pacing.md` | Scene/sequel model, motivation-reaction units, beat structure, pacing techniques, tension curves, chapter endings |
| `dialogue.md` | Subtext vs. text, voice differentiation, interiority, "as you know Bob", on-the-nose diagnosis, attribution |
| `point-of-view.md` | POV selection (1st, 3rd limited, 3rd omniscient, 2nd), psychic distance, head-hopping, unreliable narrators |
| `business-storytelling.md` | StoryBrand 7-part framework, Pixar Spine, Before-After-Bridge, founder stories, 12 brand archetypes, case study structure |
| `data-storytelling.md` | Knaflic 6 lessons, situation-complication-resolution, charts as narrative devices, executive briefing structure |
| `speech-and-presentation.md` | Duarte SparkLine, TED 18-minute structure, Monroe's Motivated Sequence, Aristotelian rhetoric, opening/closing patterns |
| `interactive-narrative.md` | Branching vs. state-based, environmental storytelling, ludonarrative dissonance, player agency, quest design |
| `anti-patterns.md` | 7 anti-patterns with diagnosis signals and concrete fixes: info dump, Mary Sue, deus ex machina, "as you know Bob", telling not showing, moral misalignment, manufactured conflict |
| `narrative-theory.md` | Propp's 31 functions, Polti's 36 situations, Booker's 7 plots, Tobias's 20 master plots, Campbell's monomyth, Genette, Greimas |

### storytelling

**What it does:** Activates when you are writing, editing, critiquing, or teaching stories in any domain -- fiction, business narrative, data presentations, speeches, UX scenarios, or interactive media. The skill identifies your domain, loads the matching references, and applies narrative craft principles grounded in your actual material. Every response ends with an anti-pattern audit.

**Try these prompts:**

```
I'm writing a short story about a programmer who discovers their AI can feel emotions -- help me structure the plot
```

```
My investor pitch is a chronological list of milestones. Turn it into a narrative that makes investors care about our mission.
```

```
I have a quarterly business review with 15 charts. Help me turn the data into a story that executives will act on.
```

```
This chapter feels flat -- the dialogue is just characters exchanging information. How do I add subtext?
```

```
I'm giving a 20-minute keynote at a tech conference. Help me structure it so the audience actually remembers the key point.
```

```
Which story structure should I use for a customer case study -- Hero's Journey, StoryBrand, or something else?
```

## Real-World Walkthrough

You are the CTO of a mid-stage startup preparing for a Series B fundraise. Your CEO asks you to write the "technical vision" section of the investor deck -- three slides that explain why your technology is defensible. You have a draft that lists your technical advantages: proprietary data pipeline, ML models trained on 3 years of customer data, and a patent-pending optimization algorithm. It is accurate but lifeless. Investors glaze over when they see it.

You open Claude Code and say:

```
I need to turn our technical vision slides into a story. Right now it's a list of technical advantages. Here's what I have: [paste draft]
```

The skill identifies this as a **business storytelling** challenge with a specific audience (Series B investors). It loads `business-storytelling.md` and asks one clarifying question: "What is the customer problem your technology solves, and what were your customers doing before your product existed?"

You explain: before your product, e-commerce companies manually optimized their search results. A merchandising team of 3-5 people would spend 15 hours per week manually reordering product listings. Your ML model automates this, reducing the work to 2 hours per week and improving conversion rates by 23%.

The skill applies the **Before-After-Bridge** framework. Instead of listing technical features, the slides now tell a story:

**Before:** "A team of four merchandisers at a mid-size retailer spends 60 person-hours per week manually reordering 12,000 product listings. They make decisions based on last week's sales data -- by the time they finish, the data is stale. Conversion suffers. Merchandising talent burns out and turns over every 18 months."

**After:** "The same team now spends 8 hours per week reviewing AI-generated optimizations. The model processes real-time behavioral data -- not last week's sales -- and reorders listings continuously. Conversion is up 23%. The team focuses on creative merchandising decisions instead of repetitive reordering."

**Bridge (your technology):** "This is possible because of three engineering decisions we made in 2022..." -- and now the technical advantages are motivated. Investors understand WHY the proprietary data pipeline matters (it enables real-time behavioral data), WHY the ML models are defensible (3 years of customer data creates a moat), and WHY the patent matters (the optimization algorithm is the bridge between data and action).

You notice the third slide is still a feature list. You say:

```
The third slide about our patent is still a list of technical specs. How do I make investors feel why this matters?
```

The skill applies the **specificity** principle. Instead of "Patent-pending optimization algorithm with O(n log n) complexity," the slide now reads: "When a customer searches for 'red running shoes,' our algorithm evaluates 847 products in 12 milliseconds, weighing 14 behavioral signals. The closest competitor processes 200 products in 300 milliseconds using 3 signals. This is why our conversion rates are 4x higher on tail queries."

The skill then runs the **anti-pattern audit**. It flags one issue: the first slide has an "info dump" in the form of a parenthetical explanation of how the ML model works. The technical detail is correct but interrupts the narrative flow. The skill recommends moving it to the appendix: "Investors who want technical depth will ask during Q&A. The deck slide should create the *desire* to ask, not answer the question before it's asked."

After two iterations, you have three slides that tell a coherent story: a painful before, a transformative after, and a technology bridge that makes the transformation proprietary. The CEO reads the revised slides and says: "Now I actually understand what our tech does."

The skill reminds you of principle five: "The ending earns everything." The last slide should not end with technical specs -- it should end with what comes next. You close with: "Every day this model runs, it learns. In 12 months, our data advantage will be 4x what it is today. The companies who join now get the compounding benefit. The companies who wait are training our model for their competitors."

## Usage Scenarios

### Scenario 1: Structuring a novel's plot

**Context:** You have a novel idea about a journalist uncovering corporate corruption, but you cannot figure out the right structure. You have 80,000 words in mind and a strong protagonist but no clear act breaks.

**You say:** `I'm writing a thriller about a journalist investigating corporate corruption. I have a strong protagonist but the plot structure isn't working. Which structure should I use?`

**The skill provides:**
- Decision framework comparing Hero's Journey (protagonist transformation focus), Fichtean Curve (crisis-driven escalation for thrillers), and 3-Act (traditional dramatic structure)
- Recommendation for Fichtean Curve (rising action through escalating crises fits the thriller/investigation genre)
- Character design guidance: want (get the story published) vs. need (confront their own complicity in the system)
- Scene/sequel pacing for investigation chapters alternating with personal-cost chapters

**You end up with:** A complete plot outline with crisis escalation points, a protagonist arc driven by want vs. need tension, and pacing guidance for alternating action and reflection.

### Scenario 2: Turning a quarterly review into a narrative

**Context:** You are a data analyst presenting quarterly results to the executive team. You have 15 charts showing mixed results -- revenue is up but customer churn increased.

**You say:** `I have 15 charts for our quarterly review. Revenue is up 12% but churn increased from 4% to 7%. Help me tell the story in these numbers.`

**The skill provides:**
- Situation-complication-resolution framework: situation (growth), complication (churn threatens sustainability), resolution (proposed retention initiatives)
- Knaflic pattern for selecting the 5 charts that tell the story and cutting the 10 that are noise
- Executive briefing structure: lead with the headline, support with data, close with a decision to make
- Anti-pattern check: no info dump of all 15 charts

**You end up with:** A 5-slide narrative that frames the mixed results as a strategic decision point -- not a reporting exercise -- with the data supporting a specific recommendation.

### Scenario 3: Writing a keynote speech

**Context:** You are giving a 20-minute keynote at a developer conference about why your team rewrote their microservices in a monolith. It is a contrarian take and you want it to be memorable.

**You say:** `I'm giving a 20-minute talk about why we moved from microservices back to a monolith. Help me structure it so it's memorable and not just a technical post-mortem.`

**The skill provides:**
- Duarte SparkLine structure: alternating between "what is" (microservices complexity, team pain) and "what could be" (simplicity, speed, joy of shipping)
- Monroe's Motivated Sequence for the contrarian angle: Attention (shocking admission), Need (microservices pain), Satisfaction (the monolith solution), Visualization (what the team looks like now), Action (how to evaluate for yourself)
- Opening pattern: start with the moment the CTO said "we're going back" and the room went silent
- Anti-pattern audit: avoiding info dump of technical details that belong in a blog post, not a talk

**You end up with:** A structured keynote that moves the audience emotionally (from skepticism to curiosity to conviction) rather than just informing them technically.

### Scenario 4: Diagnosing why a short story is not working

**Context:** You wrote a short story for a literary magazine submission. You have been revising it for weeks but something is off. The feedback you got was "technically proficient but emotionally distant."

**You say:** `My short story keeps getting rejected with feedback like "technically proficient but emotionally distant." What's wrong and how do I fix it?`

**The skill provides:**
- Anti-pattern diagnosis: likely "telling not showing" at emotional beats and/or excessive psychic distance in the POV
- Point-of-view analysis: is the narrator too detached? Could reducing psychic distance (moving from "he felt angry" to showing anger through action) create intimacy?
- Scene audit: are the key emotional moments happening in scene (real-time, with dialogue and action) or in summary (narrated past tense)?
- Dialogue check: is there subtext in the conversations, or are characters saying exactly what they mean?

**You end up with:** A specific revision plan targeting the 3-5 passages where emotional distance is the problem, with before/after examples showing how to rewrite each for greater intimacy.

## Ideal For

- **Founders and product leaders building pitch narratives** -- frameworks like StoryBrand and Before-After-Bridge transform feature lists into stories that investors, customers, and employees care about
- **Fiction writers developing craft** -- structural frameworks, character design with want vs. need, dialogue subtext, and seven anti-pattern diagnostics provide the vocabulary to diagnose and fix narrative problems
- **Anyone presenting data to decision-makers** -- data storytelling turns chart decks into narrative arguments with situation-complication-resolution structure
- **Conference speakers and keynote presenters** -- Duarte SparkLine and Monroe's Motivated Sequence create talks that audiences remember and act on
- **Game designers and interactive narrative creators** -- branching vs. state-based architecture, environmental storytelling, and ludonarrative dissonance analysis for narrative-driven game design

## Not For

- **Technical documentation** -- use [documentation-generator](../documentation-generator/) for API references, changelogs, and configuration guides; narrative structure does not apply
- **UX microcopy** -- use [ux-writing](../ux-writing/) for button labels, error messages, and form instructions; storytelling principles inform tone but microcopy has its own constraints
- **Persona creation** -- use [persona-definition](../persona-definition/) for user personas and customer archetypes; storytelling helps animate personas but does not replace the research process

## How It Works Under the Hood

The plugin is a single skill with progressive disclosure through 12 reference files. The SKILL.md body contains five core principles (causality + change + stakes, specificity, conflict, show vs. tell, the ending earns everything), a domain routing table, and a 7-step reasoning sequence applied to every response. This core is domain-agnostic -- the principles apply whether you are writing fiction, a business pitch, or a data presentation.

Domain-specific expertise lives in the reference files, organized into three tiers:

- **Foundations (2 files):** `narrative-fundamentals.md` (what a story is) and `story-structures.md` (9 structures with decision framework)
- **Craft for long-form narrative (4 files):** character design, scene/pacing, dialogue, point of view
- **Applied storytelling (4 files):** business, data, speech/presentation, interactive narrative

Two diagnostic references (`anti-patterns.md` and `narrative-theory.md`) support the audit phase of every interaction. The skill loads only the references that match the query -- typically 1-3 per interaction -- keeping context lean and responses focused.

## Related Plugins

- **[UX Writing](../ux-writing/)** -- Microcopy, error messages, and interface text -- the word-level craft that complements narrative-level storytelling
- **[Persona Definition](../persona-definition/)** -- Create user personas that storytelling can then animate into compelling narratives
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough ideas and approaches when narrative conventions are not producing the desired effect
- **[Prompt Engineering](../prompt-engineering/)** -- Optimize prompts that use storytelling principles (role assignment, context layering) for LLM interactions
- **[Content Modelling](../content-modelling/)** -- Structure content types and editorial workflows for the stories you produce

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
