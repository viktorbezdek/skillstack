# User Journey Design

> **v1.0.10** | Map the full user experience from first contact to mastery -- so you fix where the pain actually is, not where it is easiest to fix.
> Single skill, no references | 13 trigger evals + 3 output evals

## The Problem

Product teams optimize individual screens and never see the friction that accumulates between them. A signup page might test well in isolation. The email verification flow might be fine on its own. The onboarding wizard might score well in usability testing. But the journey from discovering the product to successfully using it for the first time can be full of dead ends, confusing hand-offs, and emotional low points that never surface in screen-level reviews.

Without a journey map, improvement efforts go where engineers happen to look or where the loudest user complaint lands -- not where reducing friction would have the biggest impact. A team might spend two weeks polishing the dashboard while the real drop-off happens during API credential setup, where users get stuck for 40 minutes, give up, and never come back. That credential setup pain is invisible because no single team owns it and no single screen shows it.

The deeper problem is that nobody documents what users think and feel between touchpoints. The moment after a user submits a form and waits for a confirmation email is invisible to analytics. The frustration of being redirected from docs to a support article that assumes knowledge the user does not have is invisible to screen-level testing. Journey maps make these invisible moments visible.

## The Solution

This plugin provides a structured approach to user journey mapping with three journey formats (current-state, future-state, and service blueprint), a seven-element template for each stage, and pre-built journey outlines for common flows. Every stage captures what users do, where they interact, what they think, how they feel (on a confidence-to-frustration scale), what causes friction, and where opportunities exist.

Current-state maps document the experience as it exists today, making friction visible so it can be prioritized. Future-state maps design the improved experience before building it, so the team can evaluate trade-offs before committing development time. Service blueprints show both the front-stage user actions and the back-stage organizational processes, revealing where internal handoffs create external friction.

The skill also provides pre-built journey templates for technical documentation flows -- Getting Started, Troubleshooting, and API Integration -- so documentation teams can map where users drop off without starting from scratch.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Teams optimize individual screens and miss cross-stage friction | Stage-by-stage mapping reveals where friction accumulates between touchpoints |
| Improvement priorities based on loudest complaint, not biggest impact | Emotion scores and pain points per stage show where to invest for maximum user impact |
| No documentation of what users think and feel between interactions | Seven elements per stage capture thoughts, emotions, and pain points at invisible moments |
| Redesigns introduce new friction that nobody anticipated | Side-by-side current-state vs future-state comparison catches new problems before building |
| Documentation improvements are guesswork about where users struggle | Pre-built documentation journey templates reveal drop-off points in Getting Started, API Integration, and Troubleshooting flows |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install user-journey-design@skillstack
```

### Prerequisites

No additional dependencies. Works with any Claude Code session.

### Verify installation

After installing, test with:

```
Map the user journey from discovering our product to completing their first task
```

## Quick Start

1. Install the plugin with the commands above
2. Type: `Map the onboarding journey for a developer integrating our API for the first time`
3. The skill produces a stage-by-stage map (Discover, Credentials, Read Reference, Test, Production) with goals, actions, touchpoints, emotions, pain points, and opportunities at each stage
4. Review the emotion scores -- stages scoring 1-2 (frustrated) are your highest-priority improvement targets
5. Next, try: `Now create a future-state version that fixes the two worst pain points`

---

## System Overview

```
User prompt (journey mapping, touchpoint analysis, service blueprint request)
        |
        v
+-----------------------------+
|   user-journey-design       |
|        (SKILL.md)           |
+-----------------------------+
        |
        |-- Journey type selection
        |     Current-state: as-is experience mapping
        |     Future-state: to-be design
        |     Service blueprint: user + org combined view
        |
        |-- 7-element template per stage
        |     Stages -> Touchpoints -> Actions
        |     Thoughts -> Emotions (1-5) -> Pain Points -> Opportunities
        |
        |-- Pre-built journey outlines
              Getting Started: Land -> Quickstart -> Setup -> Run -> Success
              Troubleshooting: Error -> Search -> Find -> Try -> Resolve
              API Integration: Discover -> Credentials -> Read -> Test -> Production
```

This is a compact single-skill plugin with no reference documents -- all methodology fits directly in `SKILL.md`. The skill selects the appropriate journey type based on your request context and produces a structured stage-by-stage map using the seven-element template.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `skills/user-journey-design/SKILL.md` | Skill | Journey types, seven core elements, structured template, documentation journey outlines |
| `evals/trigger-evals.json` | Eval | 13 trigger scenarios for activation boundary testing |
| `evals/evals.json` | Eval | 3 output quality scenarios for journey map generation |

**Journey types covered:**

| Type | Focus | Use when... |
|---|---|---|
| Current-state | As-is experience | Mapping what users experience today to find friction |
| Future-state | To-be design | Designing the improved experience before building it |
| Service blueprint | Combined user + org view | You need to see both front-stage user actions and back-stage organizational processes |

### Component Spotlight

#### user-journey-design (skill)

**What it does:** Activates when you need to map user journeys, customer journeys, experience maps, or service blueprints. Produces structured stage-by-stage maps with seven elements per stage: stages, touchpoints, actions, thoughts, emotions (confidence-to-frustration scale), pain points, and opportunities. Supports current-state mapping (what exists today), future-state design (the improved version), and service blueprints (user actions + organizational processes together).

**Input -> Output:** You describe a user flow, product experience, or service interaction -> You get a structured journey map with stages, touchpoints, emotions, pain points, and improvement opportunities.

**When to use:**
- Mapping where users drop off in onboarding or activation flows
- Comparing current vs future experience for a redesign
- Designing documentation improvement plans based on real user paths
- Creating service blueprints to reveal internal handoff friction
- Planning user research questions tied to specific journey stages

**When NOT to use:**
- Creating individual user personas -> use [persona-definition](../persona-definition/)
- Designing navigation patterns or information architecture -> use [navigation-design](../navigation-design/)
- Writing interface copy for the touchpoints themselves -> use [ux-writing](../ux-writing/)

**Try these prompts:**

```
Map the complete new user journey from first hearing about our product to becoming a power user
```

```
Where are users getting frustrated during our API integration flow? Map the journey from discovering our API docs to running in production
```

```
I need to compare our current checkout experience with the redesigned version -- create both journey maps so we can see what improves and what gets worse
```

```
Create a service blueprint for our support ticket flow -- I need to see what happens both on the user side and inside our organization
```

```
Help me design user research questions for each stage of our onboarding journey
```

```
Map the developer journey through our documentation -- from landing on the docs site to successfully deploying their first integration
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, may not activate) | Good (specific, activates reliably) |
|---|---|
| "Help me with UX" | "Map the onboarding journey for a developer integrating our API for the first time" |
| "Improve our product" | "Where are users dropping off between signup and first successful task? Map the current-state journey" |
| "Make a user flow" | "Create current-state and future-state journey maps for our checkout flow so we can compare them" |
| "Customer experience" | "Create a service blueprint for our support ticket flow showing both user-facing and internal processes" |
| "What's wrong with onboarding?" | "Map the journey from account creation to first API call -- I need emotion scores at each stage to find the worst friction" |

### Structured Prompt Templates

**For current-state mapping:**
```
Map the current-state journey for a [user type] who [starting action] and tries to [end goal] in our [product/service]. I need to see where the friction is.
```

**For future-state design:**
```
Create a future-state journey that fixes [specific pain points] in our [flow name]. The goal is [target metric, e.g., "get from signup to first API call in under 5 minutes"].
```

**For side-by-side comparison:**
```
Create current-state and future-state journey maps for our [flow name] so we can compare what improves, what stays the same, and what might get worse with the redesign.
```

**For service blueprints:**
```
Create a service blueprint for our [process, e.g., support ticket flow] -- I need to see the user-facing experience and the internal organizational processes together, including where handoffs happen.
```

**For documentation journey mapping:**
```
Map the developer journey through our documentation -- from [starting point, e.g., arriving at the docs site] to [end goal, e.g., successfully deploying their first integration].
```

### Prompt Anti-Patterns

- **Asking for a journey map without specifying the user or goal:** "Create a journey map" is too vague. The skill needs to know who the user is and what they are trying to accomplish to produce meaningful stages and emotions.
- **Asking for wireframes or screen designs:** Journey maps are about the experience between and across screens, not the screens themselves. If you need screen-level design, use frontend-design.
- **Requesting a journey map for an internal technical process:** Journey maps center on user experience with emotions and pain points. If you need to document an internal workflow (CI/CD pipeline, deploy process), that is a process diagram, not a journey map.
- **Combining persona creation with journey mapping in one prompt:** "Create a persona and their journey" splits attention between two different skills. Create the persona first with persona-definition, then map their journey with this skill.

## Real-World Walkthrough

You are the product lead for a developer tools startup. Your API product has healthy signup numbers but terrible activation -- only 18% of developers who create an account ever make a successful API call. You suspect the problem is somewhere in the onboarding flow, but you have five teams (marketing, docs, platform, developer experience, and support) each optimizing their piece independently. Nobody has mapped the end-to-end experience.

**Step 1 -- Map the current state.** You ask:

```
Map the current-state journey for a developer who discovers our API product through a blog post and tries to make their first successful API call
```

The skill produces a five-stage journey: Discovery, Signup, Credential Setup, First API Call, and Integration. For each stage, you populate the seven elements with your team:

- **Discovery** (emotion: 4/5 -- excited): Developer reads a compelling blog post, clicks to the product page. Pain point: pricing not visible without signing up.
- **Signup** (emotion: 3/5 -- neutral): Standard email/password form, email verification. Pain point: verification email takes 3-5 minutes, no indication of delay.
- **Credential Setup** (emotion: 2/5 -- frustrated): Dashboard with six menu items, no "get started" path. Must navigate Settings > API Keys > Create New Key, choose "test" vs "production" with no explanation, configure CORS. Pain point: 15-minute setup for something that should take 30 seconds.
- **First API Call** (emotion: 1/5 -- very frustrated): Documentation has a curl example using an endpoint format from two versions ago. 401 error. SDK needs a config file mentioned on a different page. Pain point: 40-minute debugging session.
- **Integration** (emotion: 2/5 -- frustrated): Successful response but data format doesn't match docs. Three pages with conflicting information. Pain point: documentation inconsistency erodes trust.

**Step 2 -- Identify the real problem.** The map reveals the pattern immediately: the emotional low point is stages 3 and 4 (Credential Setup and First API Call), not the stages your teams have been optimizing. Marketing has been A/B testing the landing page (already scoring 4/5). Platform has been adding dashboard features. Nobody has been working on the 40-minute gap between "I have an account" and "I made a successful call."

**Step 3 -- Design the future state.** You ask:

```
Create a future-state journey that fixes credential setup and first API call -- I want developers from signup to successful API call in under 5 minutes
```

The future-state map eliminates the credential setup stage by auto-generating a test API key on signup and presenting it on a "Get Started" page with a working curl command. First API Call becomes: copy command, paste in terminal, see response. Emotion goes from 1/5 to 4/5.

**Step 4 -- Catch new risks.** Side-by-side comparison reveals one risk: the auto-generated key needs scope limitations to prevent accidental production use, which means adding a "upgrade to production key" step later. You add this as a new stage and design it friction-free.

**Step 5 -- Result.** Your 18% activation rate has a clear diagnosis (stages 3-4), a concrete improvement plan (auto-generated keys, working examples on signup), and awareness of a new risk (production key upgrade flow) -- all from one structured journey mapping session.

**Gotchas discovered:** Emotion scoring is the most valuable element. Without it, every stage looks equally important in a bulleted list. With scores, the 1/5 and 2/5 stages stand out immediately as priorities.

## Usage Scenarios

### Scenario 1: Mapping onboarding drop-off

**Context:** You are a product manager and your SaaS product has a 60% drop-off between signup and first meaningful action. You do not know where users are getting stuck.

**You say:** `Map the current-state journey from signup to completing the first meaningful task in our project management tool`

**The skill provides:**
- Five-stage journey template (Signup, Setup, First Project, First Task, First Collaboration)
- Seven elements per stage including emotion scores to identify the worst friction points
- Pain point analysis revealing where drop-off is most likely
- Opportunity identification for each stage

**You end up with:** A visual map showing exactly which stages cause the 60% drop-off, with prioritized opportunities for improvement.

### Scenario 2: Designing a documentation improvement plan

**Context:** Your developer documentation gets complaints but you do not know which part to fix first. The docs span getting started guides, API references, tutorials, and troubleshooting.

**You say:** `Map the developer journey through our documentation -- from arriving at the docs site to successfully resolving a production issue`

**The skill provides:**
- Pre-built documentation journey stages (Land, Find Quickstart, Setup, Run Example, Success) plus Troubleshooting stages (Error, Search, Find Article, Try Fix, Resolve)
- Pain point templates for common documentation failures (missing prerequisites, outdated examples, assumed knowledge)
- Opportunities tied to specific documentation improvements

**You end up with:** A prioritized list of documentation improvements based on where developers actually get stuck, not where the team guesses they get stuck.

### Scenario 3: Before/after comparison for a redesign

**Context:** Your team is redesigning the checkout flow and wants to validate that the new design actually improves the experience before committing to building it.

**You say:** `Create current-state and future-state journey maps for our checkout flow so we can compare them side by side`

**The skill provides:**
- Current-state map documenting today's friction (Cart, Shipping, Payment, Confirmation)
- Future-state map with the redesigned flow and projected emotion improvements
- Side-by-side comparison highlighting stages that improve, stay the same, or introduce new friction
- Risk identification for new friction the redesign creates

**You end up with:** Evidence-based validation that the redesign improves the overall experience, with early warning about stages where the redesign might make things worse.

### Scenario 4: Creating a service blueprint

**Context:** Your customer support flow involves the user submitting a ticket, an automated triage system, a support agent, and possibly an engineering escalation. Users complain about slow resolution times but you cannot see where the delay happens.

**You say:** `Create a service blueprint for our support ticket flow -- I need to see the user-facing experience and the internal organizational processes together`

**The skill provides:**
- Front-stage map: user actions from submitting ticket to receiving resolution
- Back-stage map: automated triage, agent assignment, escalation rules, engineering handoff
- Line of visibility showing where user-facing actions connect to internal processes
- Pain points on both sides (user waits without updates; engineering gets incomplete context from agent)

**You end up with:** A blueprint showing that the 48-hour delay is not in engineering resolution (4 hours average) but in the agent-to-engineering handoff (36 hours average because of queue prioritization).

---

## Decision Logic

**When to use current-state vs future-state vs service blueprint?**

Use **current-state** when you need to understand where friction exists today. This is the diagnostic step -- do this first before proposing solutions. It answers "where is the pain?" Use **future-state** after you have a current-state map and want to design improvements. It answers "what would better look like?" Always compare against the current-state map to ensure the redesign does not introduce new friction. Use **service blueprint** when user-visible delays or frustrations are caused by internal organizational processes. If the pain is not in the product interface but in handoffs between teams, departments, or systems, a service blueprint connects front-stage to back-stage.

**When does this skill activate vs persona-definition or navigation-design?**

This skill activates when you describe a user's experience across multiple stages or touchpoints -- anything involving journeys, flows, or experience paths. persona-definition activates when you need to create the user profiles themselves (demographics, goals, behaviors) before mapping their journeys. navigation-design activates when you need to structure the information architecture or menu systems at individual touchpoints. The workflow: create personas first, map their journeys second, design the navigation at each touchpoint third.

**How to prioritize improvements from a journey map?**

The emotion scores drive prioritization. Stages scoring 1/5 or 2/5 are top priority because they represent the points where users are most likely to abandon. Among equally low-scoring stages, prioritize the one that comes earliest in the journey -- early friction prevents users from reaching later stages at all.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Journey map too granular -- every click is a stage | Map has 15+ stages and the team cannot identify which ones matter | Consolidate to 4-7 stages, each representing a meaningful user goal transition (not a UI interaction). A stage is "Get API credentials," not "Click Settings, Click API Keys, Click Create." |
| Emotion scores assigned by the team without user data | Scores reflect developer assumptions, not actual user experience; priorities are wrong | Use the journey map as a user research planning tool. The seven elements per stage map directly to interview questions. Validate scores with 5-8 user interviews before committing to priorities. |
| Future-state map designed without current-state baseline | Team designs the "ideal" experience but cannot measure improvement because there is no before to compare against | Always create the current-state map first, even if it feels redundant. The current-state map is the baseline that makes future-state improvements measurable. |
| Service blueprint missing the line of visibility | Front-stage and back-stage actions are listed but not connected; nobody can see which internal process causes which user-facing delay | Explicitly draw the line of visibility -- map each user-facing wait or frustration to the specific internal process that causes it. The connection is the insight, not the list. |
| Single journey map used for all user types | Different personas have different pain points at the same stages, but one map averages them out and hides the differences | Create separate journey maps for each key persona. A power user's journey through troubleshooting is very different from a beginner's. Use persona-definition first if needed. |

## Ideal For

- **Product managers mapping onboarding flows** -- the structured template reveals where users drop off and why, not just that they drop off
- **Developer experience teams improving API docs** -- pre-built documentation journey templates eliminate the blank-page problem
- **UX designers validating redesigns before building** -- side-by-side current vs future state catches new friction before it ships
- **Service design teams fixing cross-department handoffs** -- service blueprints connect front-stage user experience to back-stage organizational processes
- **Teams starting user research** -- the seven elements per stage map directly to interview questions for each part of the experience

## Not For

- **Creating individual user personas** -- use [persona-definition](../persona-definition/) to build the personas whose journeys you then map with this plugin
- **Designing navigation patterns or information architecture** -- use [navigation-design](../navigation-design/) for site maps, menu structures, and wayfinding
- **Writing the actual interface copy for touchpoints** -- use [ux-writing](../ux-writing/) for microcopy, error messages, and button labels
- **Mapping internal technical workflows** -- journey maps center on user emotions and experience; if you need to document a CI/CD pipeline or deploy process, use workflow-automation

## Related Plugins

- **[Persona Definition](../persona-definition/)** -- Create the personas whose journeys you map
- **[Persona Mapping](../persona-mapping/)** -- Map stakeholders across the organization to understand who owns each journey stage
- **[Navigation Design](../navigation-design/)** -- Design the navigation systems users encounter at each touchpoint
- **[UX Writing](../ux-writing/)** -- Write the microcopy for error states, empty states, and confirmation dialogs along the journey
- **[Content Modelling](../content-modelling/)** -- Design the content structures that back your documentation journeys
- **[Ontology Design](../ontology-design/)** -- Model the knowledge relationships that inform your journey stages

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
