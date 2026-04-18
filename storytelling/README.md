# Storytelling

> **v1.0.1** | Design & UX | 2 iterations

> Expert guidance for writing, editing, and teaching stories across fiction, business, data, speech, UX, and interactive narrative -- from structural frameworks through craft technique to anti-pattern diagnosis.
> Single skill + 12 references (progressive disclosure by domain)

## Context to Provide

The storytelling skill is most powerful when it has actual material to work with, not just a topic. The more you share, the more specific and actionable the guidance becomes.

**What information to include in your prompt:**

- **Your draft or raw material** -- paste the actual pitch deck bullets, chapter excerpt, data slides, or speech outline you are working with. The skill diagnoses real content, not hypothetical scenarios.
- **Domain and format** -- specify whether this is a fiction piece, investor pitch, quarterly business review, keynote, UX scenario, or game narrative. This drives reference selection.
- **Audience** -- who will read or hear this? Series B investors, technical conference attendees, new employees, executive leadership, or fiction readers. Audience determines structure and tone.
- **The specific problem** -- "the middle sags," "the dialogue is flat," "investors glaze over at slide 3," "the data doesn't tell a story." A named problem is diagnosable; a vague one is not.
- **What you have already tried** -- if you have already restructured the pitch or tried a different framework, say so. This prevents circular advice.

**What makes results better vs worse:**

- Better: paste the actual text with a specific diagnosis request ("why does this fall flat?")
- Better: name the domain and audience upfront ("investor pitch, Series B, technical audience")
- Better: describe the desired emotional outcome ("I want them to feel urgency, not just understand the product")
- Worse: asking for generic "storytelling advice" without any material to work with
- Worse: describing the topic without sharing the draft ("I need help with my keynote about our pivot")
- Worse: asking to "add storytelling" to existing content -- the skill restructures, it doesn't decorate

**Template prompt:**

```
I'm writing a [genre/format: investor pitch / keynote / short story / data presentation] for [audience].
Here's what I have:

[paste your draft, outline, or bullet points]

The specific problem: [what feels flat, stuck, or missing].
The desired outcome: [what you want the audience to feel or do].
```

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

---

## System Overview

```
User asks about writing / editing / teaching stories
    │
    ▼
┌────────────────────────────────────────────────────────┐
│              storytelling (skill)                        │
│                                                         │
│  5 Core Principles (always active):                     │
│  1. Story = causality + change + stakes                 │
│  2. Specificity is power                                │
│  3. Conflict is the engine                              │
│  4. Show vs tell (deliberate choice)                    │
│  5. The ending earns everything                         │
│                                                         │
│  7-Step Reasoning Sequence (every response):            │
│  Identify context → Ask about audience → Load refs →    │
│  Structure before surface → Ground abstractions →       │
│  Audit anti-patterns → Connect to meaning               │
│                                                         │
│  Domain Routing (progressive disclosure):               │
│  ┌────────────────────────────────────────────────┐     │
│  │ Foundations                                     │     │
│  │  narrative-fundamentals | story-structures      │     │
│  ├────────────────────────────────────────────────┤     │
│  │ Craft (fiction / long-form)                     │     │
│  │  character-design | scene-and-pacing |          │     │
│  │  dialogue | point-of-view                       │     │
│  ├────────────────────────────────────────────────┤     │
│  │ Applied (business / data / speech / interactive)│     │
│  │  business-storytelling | data-storytelling |    │     │
│  │  speech-and-presentation | interactive-narrative│     │
│  ├────────────────────────────────────────────────┤     │
│  │ Diagnostics                                     │     │
│  │  anti-patterns | narrative-theory               │     │
│  └────────────────────────────────────────────────┘     │
│                                                         │
│  Typically loads 1-3 references per interaction          │
└────────────────────────────────────────────────────────┘
```

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `storytelling` | skill | Core principles, domain routing table, 7-step reasoning sequence applied to every response |
| `narrative-fundamentals.md` | reference | What a story is: character, desire, obstacle, transformation, the causality test, the "so what?" question |
| `story-structures.md` | reference | 9 canonical structures (3-Act, Freytag, Fichtean, Hero's Journey, Story Circle, Save the Cat, Kishotenketsu, StoryBrand, Pixar Spine) with decision framework |
| `character-design.md` | reference | Want vs. need, flaws, arcs (positive/flat/negative), dimensionality, supporting cast roles |
| `scene-and-pacing.md` | reference | Scene/sequel model, motivation-reaction units, beat structure, tension curves, chapter endings |
| `dialogue.md` | reference | Subtext vs. text, voice differentiation, interiority, "as you know Bob", on-the-nose diagnosis |
| `point-of-view.md` | reference | POV selection, psychic distance, head-hopping, unreliable narrators |
| `business-storytelling.md` | reference | StoryBrand 7-part framework, Pixar Spine, Before-After-Bridge, founder stories, 12 brand archetypes, case study structure |
| `data-storytelling.md` | reference | Knaflic 6 lessons, situation-complication-resolution, charts as narrative devices, executive briefing structure |
| `speech-and-presentation.md` | reference | Duarte SparkLine, TED 18-minute structure, Monroe's Motivated Sequence, Aristotelian rhetoric |
| `interactive-narrative.md` | reference | Branching vs. state-based, environmental storytelling, ludonarrative dissonance, player agency, quest design |
| `anti-patterns.md` | reference | 7 anti-patterns with diagnosis signals and fixes: info dump, Mary Sue, deus ex machina, "as you know Bob", telling not showing, moral misalignment, manufactured conflict |
| `narrative-theory.md` | reference | Propp's 31 functions, Polti's 36 situations, Booker's 7 plots, Tobias's 20 master plots, Campbell's monomyth, Genette, Greimas |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

### Component Spotlights

#### storytelling (skill)

**What it does:** Activates when you are writing, editing, critiquing, or teaching stories in any domain -- fiction, business narrative, data presentations, speeches, UX scenarios, or interactive media. Identifies your domain, loads the matching references, applies narrative craft principles grounded in your actual material, and audits every response against anti-patterns.

**Input -> Output:** A storytelling challenge (a draft, a pitch, a data deck, a speech outline, a stuck novel) -> Structural diagnosis, framework recommendation, concrete revision guidance grounded in the user's actual content, and an anti-pattern audit.

**When to use:** Writing fiction or creative nonfiction. Structuring business pitches and founder stories. Turning data into narrative presentations. Writing speeches and keynotes. Designing interactive narrative for games. Diagnosing why a story is not working. Teaching narrative principles to writers, designers, or founders.

**When NOT to use:** Plain technical documentation (use documentation-generator). UX microcopy like button labels and error messages (use ux-writing). Persona creation (use persona-definition). Clinical or therapeutic narrative work.

**Try these prompts:**

```
I'm writing a thriller about a journalist investigating corporate corruption -- she's uncovering a cover-up
that reaches into the government. The plot has a strong beginning and end but the middle third feels like
a sequence of events with no escalation. Here's my chapter outline: [paste outline]. Which structure should
I use and where are the act breaks?
```

```
My Series B investor pitch is currently a bullet list of milestones: "we built X in 2022, launched Y in 2023,
grew to Z customers." Here's the current slide: [paste slide text]. Turn this into a Before-After-Bridge
narrative. Our customer problem is: e-commerce teams spend 15 hours/week manually reordering product listings.
```

```
I have 15 charts for our Q3 business review. Revenue is up 12% but churn rose from 4% to 7%. Executives are
going to ask "so what should we do?" Help me select the 5 charts that tell the story and structure them
with situation-complication-resolution so the last slide is a clear decision point.
```

```
This dialogue scene feels flat -- here's the excerpt: [paste scene]. The two characters are arguing about
a promotion but every line is just stating positions. How do I add subtext so the real conflict (jealousy,
not the promotion) comes through without being stated directly?
```

```
I'm giving a 20-minute keynote at a technical conference about why we moved from microservices back to a
monolith. The audience is skeptical senior engineers. I want them to leave thinking "this is brave and right"
not "this is a cautionary tale." Structure it so the contrarian take lands as conviction, not failure.
```

```
I need to write a customer case study for our enterprise sales team. The customer is a logistics company
that reduced shipping errors by 34% using our software. Should I use Hero's Journey, StoryBrand, or
something else? The audience is VP-level buyers at similar companies.
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, gets generic advice) | Good (specific, gets grounded craft guidance) |
|---|---|
| "Help me with my story" | "I'm writing a thriller about a journalist investigating corporate corruption -- the middle third sags and I can't figure out the act 2 structure" |
| "Make my pitch better" | "My investor pitch is a chronological list of what we built. Turn it into a Before-After-Bridge narrative -- the customer problem is [describe]" |
| "How do I present data" | "I have 15 charts for our quarterly review but revenue is up while churn is also up. Help me frame the conflict in the data." |
| "Write me a speech" | "I'm giving a 20-minute keynote about why we moved from microservices back to a monolith -- it's a contrarian take and I want it to be memorable" |
| "Fix my dialogue" | "My characters sound the same -- here's a scene where two people argue about a promotion. How do I give each person a distinct voice and add subtext?" |

### Structured Prompt Templates

**For fiction writing:**
```
I'm writing a [genre] [form: short story / novel / screenplay] about [premise].
My protagonist wants [desire] but faces [obstacle]. I'm stuck on [specific problem:
structure, character arc, dialogue, pacing]. What structure and craft techniques
should I use?
```

**For business narrative:**
```
I need to [pitch investors / present a case study / write a founder story].
The audience is [who]. The key facts are [what happened]. Right now it reads
like [a list / a timeline / a feature dump]. Turn it into a narrative with
conflict, transformation, and stakes.
```

**For data storytelling:**
```
I have [N] charts showing [summary of data]. The headline is [what matters].
The complication is [what's surprising or concerning]. Help me structure this
as a narrative that leads to [specific decision or recommendation].
```

**For speech writing:**
```
I'm giving a [duration]-minute [talk type: keynote / internal presentation / ceremony]
about [topic]. The audience is [who]. The one thing I want them to remember is
[key point]. Structure it so the audience feels [desired emotional arc].
```

### Prompt Anti-Patterns

- **Asking for generic storytelling advice without a specific piece of material:** "How do I tell better stories?" produces theory. "Here's my pitch deck -- why doesn't it land?" produces actionable revision guidance. The skill is most powerful when it has your actual content to diagnose.
- **Requesting structure without specifying audience or domain:** "Which story structure should I use?" has no answer without knowing who the audience is and what domain you are working in. A thriller needs Fichtean Curve; a founder pitch needs Before-After-Bridge; a keynote needs Duarte SparkLine. Specify the context.
- **Treating storytelling as decoration on top of existing content:** Asking to "add storytelling" to a data deck or pitch does not work. The narrative IS the structure -- you do not layer it on top. The skill needs to restructure the content, not decorate it.
- **Asking to "make it more engaging" without identifying the specific problem:** The skill diagnoses with anti-patterns (info dump, telling not showing, flat dialogue). Point to what feels wrong -- "the middle is boring," "the dialogue is flat," "the ending falls flat" -- and the skill can diagnose the specific failure.

## Real-World Walkthrough

You are the CTO of a mid-stage startup preparing for a Series B fundraise. Your CEO asks you to write the "technical vision" section of the investor deck -- three slides that explain why your technology is defensible. You have a draft that lists your technical advantages: proprietary data pipeline, ML models trained on 3 years of customer data, and a patent-pending optimization algorithm. It is accurate but lifeless. Investors glaze over when they see it.

You open Claude Code and say:

```
I need to turn our technical vision slides into a story. Right now it's a list of technical advantages. Here's what I have: [paste draft]
```

The skill identifies this as a **business storytelling** challenge with a specific audience (Series B investors). It loads `business-storytelling.md` and asks one clarifying question: "What is the customer problem your technology solves, and what were your customers doing before your product existed?"

You explain: before your product, e-commerce companies manually optimized their search results. A merchandising team of 3-5 people would spend 15 hours per week manually reordering product listings. Your ML model automates this, reducing the work to 2 hours per week and improving conversion rates by 23%.

The skill applies the **Before-After-Bridge** framework. Instead of listing technical features, the slides now tell a story:

**Before:** "A team of four merchandisers at a mid-size retailer spends 60 person-hours per week manually reordering 12,000 product listings. They make decisions based on last week's sales data -- by the time they finish, the data is stale."

**After:** "The same team now spends 8 hours per week reviewing AI-generated optimizations. The model processes real-time behavioral data. Conversion is up 23%."

**Bridge (your technology):** "This is possible because of three engineering decisions we made in 2022..." -- and now the technical advantages are motivated. Investors understand WHY each piece of technology matters because they have felt the problem it solves.

You notice the third slide is still a feature list. You ask for help making investors feel why the patent matters. The skill applies the **specificity** principle: instead of "patent-pending optimization algorithm with O(n log n) complexity," it becomes "when a customer searches for 'red running shoes,' our algorithm evaluates 847 products in 12 milliseconds, weighing 14 behavioral signals. The closest competitor processes 200 products in 300 milliseconds using 3 signals."

The skill then runs the **anti-pattern audit**. It flags one issue: the first slide has an info dump -- a parenthetical explanation of how the ML model works that interrupts narrative flow. The skill recommends moving it to the appendix: "Investors who want technical depth will ask during Q&A. The deck slide should create the desire to ask, not answer the question before it is asked."

After two iterations, you have three slides that tell a coherent story: a painful before, a transformative after, and a technology bridge that makes the transformation proprietary. The skill reminds you of principle five: "The ending earns everything." The last slide closes with: "Every day this model runs, it learns. In 12 months, our data advantage will be 4x what it is today."

## Usage Scenarios

### Scenario 1: Structuring a novel's plot

**Context:** You have a novel idea about a journalist uncovering corporate corruption, but you cannot figure out the right structure. You have a strong protagonist but no clear act breaks.

**You say:** `I'm writing a thriller about a journalist investigating corporate corruption. I have a strong protagonist but the plot structure isn't working. Which structure should I use?`

**The skill provides:**
- Decision framework comparing Hero's Journey, Fichtean Curve, and 3-Act for this genre
- Recommendation for Fichtean Curve (crisis-driven escalation fits thriller/investigation)
- Character design: want (get the story published) vs. need (confront their own complicity)
- Scene/sequel pacing for alternating investigation and personal-cost chapters

**You end up with:** A complete plot outline with crisis escalation points, a protagonist arc, and pacing guidance.

### Scenario 2: Turning a quarterly review into a narrative

**Context:** You have 15 charts for the quarterly review. Revenue is up but customer churn increased.

**You say:** `I have 15 charts for our quarterly review. Revenue is up 12% but churn increased from 4% to 7%. Help me tell the story in these numbers.`

**The skill provides:**
- Situation-complication-resolution framework for the mixed data
- Knaflic pattern: select the 5 charts that tell the story, cut the 10 that are noise
- Executive briefing structure: headline, supporting data, decision to make

**You end up with:** A 5-slide narrative that frames mixed results as a strategic decision point with a specific recommendation.

### Scenario 3: Writing a keynote speech

**Context:** You are giving a 20-minute keynote about why your team rewrote microservices as a monolith.

**You say:** `I'm giving a 20-minute talk about why we moved from microservices back to a monolith. Help me structure it so it's memorable.`

**The skill provides:**
- Duarte SparkLine alternating "what is" (microservices pain) and "what could be" (simplicity)
- Monroe's Motivated Sequence for the contrarian angle
- Opening pattern: start with the moment the CTO said "we're going back"

**You end up with:** A structured keynote that moves the audience emotionally from skepticism to conviction.

### Scenario 4: Diagnosing why a short story is not working

**Context:** Your short story keeps getting rejected with feedback like "technically proficient but emotionally distant."

**You say:** `My short story keeps getting rejected with feedback like "technically proficient but emotionally distant." What's wrong?`

**The skill provides:**
- Anti-pattern diagnosis: likely telling-not-showing at emotional beats and/or excessive psychic distance
- POV analysis and psychic distance adjustment recommendations
- Scene audit identifying where key moments happen in summary instead of scene
- Dialogue subtext check

**You end up with:** A revision plan targeting the specific passages where emotional distance is the problem, with before/after examples.

---

## Decision Logic

**How does the skill choose which references to load?**

The skill uses a domain routing table. It examines your request and loads only the matching references:
- Fiction/creative writing -> `story-structures.md` + the relevant craft reference (character, scene/pacing, dialogue, or POV)
- Business pitch or founder story -> `business-storytelling.md`
- Data presentation -> `data-storytelling.md`
- Speech or keynote -> `speech-and-presentation.md`
- Interactive/game narrative -> `interactive-narrative.md`
- "Something feels wrong" / critique request -> `anti-patterns.md`
- Multi-domain queries load 2-3 references. Loading more than 4 indicates the query is not focused enough.

**How does the skill choose between 9 story structures?**

The `story-structures.md` reference includes a decision framework:
- **3-Act Structure**: general-purpose, works for most narratives
- **Hero's Journey**: protagonist transformation with external adventure
- **Story Circle (Harmon)**: simplified Hero's Journey for TV/series
- **Save the Cat (Snyder)**: beat-by-beat for screenplays and commercial fiction
- **Fichtean Curve**: crisis-driven escalation for thrillers and investigations
- **Freytag's Pyramid**: traditional dramatic arc (tragedies, literary fiction)
- **Kishotenketsu**: twist-based structure without conflict (East Asian narrative)
- **StoryBrand (Miller)**: customer-as-hero for business narrative
- **Pixar Spine**: "Once upon a time... Until one day..." for pitches and presentations

**Why does every response end with an anti-pattern audit?**

Most narrative failures are anti-patterns, not missing principles. A draft can follow the Hero's Journey perfectly and still fail if it has an info dump in act one, flat dialogue in act two, or a deus ex machina ending. The audit catches failures that structural advice alone misses.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| User wants "storytelling" but really needs documentation | They ask to "tell the story of our API" -- they need documentation structure, not narrative structure | Clarify the intent. If they need people to understand how the API works, that is documentation (use documentation-generator). If they need people to care about why the API exists, that is storytelling. |
| Framework imposed on content that does not fit | Before-After-Bridge applied to a topic where there is no meaningful "before" state | Not every communication is a story. Status updates, reference documents, and process descriptions are not narratives. The skill should tell you when storytelling is the wrong tool. |
| Anti-pattern diagnosed incorrectly because context is missing | The skill flags "telling not showing" in a passage that is intentionally summary | Some telling is correct -- time jumps, logistics, transitional passages. The principle is "show when you want the audience to feel, tell when you need to move past information efficiently." If the flagged passage is logistical, the anti-pattern does not apply. |
| Multiple structures recommended with no clear winner | The user's project could plausibly use Hero's Journey, 3-Act, or Story Circle | Ask about the audience and medium. The answer usually collapses the options: screenwriters lean Save the Cat, novelists lean 3-Act or Fichtean, presenters lean StoryBrand or SparkLine. |
| User expects the skill to write the story, not teach the craft | They paste a topic and expect a finished draft | The skill provides structure, technique, and revision guidance. It can produce drafts, but its primary value is the diagnostic and structural framework. For pure content generation, the skill's output is a structured outline and revision plan. |

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

## Related Plugins

- **[UX Writing](../ux-writing/)** -- Microcopy, error messages, and interface text -- the word-level craft that complements narrative-level storytelling
- **[Persona Definition](../persona-definition/)** -- Create user personas that storytelling can then animate into compelling narratives
- **[Creative Problem Solving](../creative-problem-solving/)** -- Generate breakthrough ideas when narrative conventions are not producing the desired effect
- **[Prompt Engineering](../prompt-engineering/)** -- Optimize prompts that use storytelling principles for LLM interactions
- **[Content Modelling](../content-modelling/)** -- Structure content types and editorial workflows for the stories you produce

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
