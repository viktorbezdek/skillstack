# User Journey Design

> **v1.0.10** | Design & UX | 11 iterations

> Map the full user experience from first contact to mastery -- so you fix where the pain actually is, not where it is easiest to fix.

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

## What's Inside

This is a **single-skill plugin** with pre-built journey templates and eval coverage.

| Component | Purpose |
|---|---|
| `skills/user-journey-design/SKILL.md` | Journey types, seven core elements, structured template, documentation journey outlines (Getting Started, Troubleshooting, API Integration) |
| `evals/trigger-evals.json` | 13 trigger scenarios for activation boundary testing |
| `evals/evals.json` | 3 output quality scenarios for journey map generation |

**Journey types covered:**

| Type | Focus | Use when... |
|---|---|---|
| Current-state | As-is experience | Mapping what users experience today to find friction |
| Future-state | To-be design | Designing the improved experience before building it |
| Service blueprint | Combined user + org view | You need to see both front-stage user actions and back-stage organizational processes |

### user-journey-design

**What it does:** Activates when you need to map user journeys, customer journeys, experience maps, or service blueprints. Produces structured stage-by-stage maps with seven elements per stage: stages, touchpoints, actions, thoughts, emotions (confidence-to-frustration scale), pain points, and opportunities. Supports current-state mapping (what exists today), future-state design (the improved version), and service blueprints (user actions + organizational processes together).

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
Help me design user research questions for each stage of our onboarding journey
```

```
Create a service blueprint for our support ticket flow -- I need to see what happens both on the user side and inside our organization
```

```
Map the developer journey through our documentation -- from landing on the docs site to successfully deploying their first integration
```

## Real-World Walkthrough

You are the product lead for a developer tools startup. Your API product has healthy signup numbers but terrible activation -- only 18% of developers who create an account ever make a successful API call. You suspect the problem is somewhere in the onboarding flow, but you have five teams (marketing, docs, platform, developer experience, and support) each optimizing their piece independently. Nobody has mapped the end-to-end experience.

You start by mapping the current state:

```
Map the current-state journey for a developer who discovers our API product through a blog post and tries to make their first successful API call
```

The skill produces a five-stage journey: Discovery, Signup, Credential Setup, First API Call, and Integration. For each stage, it prompts you to fill in the seven elements. Working with your team, you populate the map:

**Discovery** (emotion: 4/5 -- excited): Developer reads a compelling blog post, clicks through to the product page. Touchpoints: blog, landing page. Pain point: pricing is not visible without signing up.

**Signup** (emotion: 3/5 -- neutral): Standard email/password form, email verification. Touchpoints: signup page, verification email. Pain point: verification email takes 3-5 minutes to arrive, no indication of delay.

**Credential Setup** (emotion: 2/5 -- frustrated): Developer lands on a dashboard with six menu items and no clear "get started" path. Must navigate to Settings > API Keys > Create New Key, choose between "test" and "production" keys without explanation of the difference, and configure CORS origins before the key works. Touchpoints: dashboard, settings page, API key creation form. Pain point: 15-minute setup for something that should take 30 seconds.

**First API Call** (emotion: 1/5 -- very frustrated): Developer copies the API key, goes to documentation, finds a curl example that uses an endpoint format that changed two versions ago. Gets a 401 error. Tries the SDK, which requires a config file in a specific location that is mentioned in a different doc page. Touchpoints: docs, terminal, SDK. Pain point: outdated examples and scattered prerequisites create a 40-minute debugging session.

**Integration** (emotion: 2/5 -- frustrated): Developer finally gets a successful response but the data format does not match what the docs describe. Searches for "response format" and finds three different pages with conflicting information. Touchpoints: docs, API response, support forum. Pain point: documentation inconsistency erodes trust.

The map reveals the pattern immediately: the emotional low point is stages 3 and 4 (Credential Setup and First API Call), not the stages your teams have been optimizing. Marketing has been A/B testing the landing page (stage 1, already scoring 4/5). Platform has been adding dashboard features (stage 5). Nobody has been working on the 40-minute gap between "I have an account" and "I made a successful call."

You create a future-state map targeting stages 3 and 4:

```
Create a future-state journey that fixes credential setup and first API call -- I want to get developers from signup to successful API call in under 5 minutes
```

The future-state map eliminates the credential setup stage entirely by auto-generating a test API key on signup and presenting it on a post-signup "Get Started" page with a working curl command that the developer can copy and run immediately. The first API call stage becomes: copy command, paste in terminal, see response. Emotion goes from 1/5 to 4/5.

Side-by-side comparison with the current-state map reveals one risk the team did not anticipate: the auto-generated key needs scope limitations to prevent accidental production use, which means adding a "upgrade to production key" step later in the journey. You add this as a new stage in the future-state map and design it to be friction-free.

The result: your 18% activation rate has a clear diagnosis (stages 3-4), a concrete improvement plan (auto-generated keys, working examples on signup), and an awareness of a new risk (production key upgrade flow) -- all from a structured journey mapping exercise that took one session.

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

## Ideal For

- **Product managers mapping onboarding flows** -- the structured template reveals where users drop off and why, not just that they drop off
- **Developer experience teams improving API docs** -- pre-built documentation journey templates eliminate the blank-page problem
- **UX designers validating redesigns before building** -- side-by-side current vs future state catches new friction before it ships
- **Service design teams fixing cross-department handoffs** -- service blueprints connect front-stage user experience to back-stage organizational processes
- **Teams starting user research** -- the seven elements per stage map directly to interview questions

## Not For

- **Creating individual user personas** -- use [persona-definition](../persona-definition/) to build the personas whose journeys you then map with this plugin
- **Designing navigation patterns or information architecture** -- use [navigation-design](../navigation-design/) for site maps, menu structures, and wayfinding
- **Writing the actual interface copy for touchpoints** -- use [ux-writing](../ux-writing/) for microcopy, error messages, and button labels

## How It Works Under the Hood

The plugin is a single compact skill with no reference documents -- all methodology fits in the core `SKILL.md`. The skill defines three journey types (current-state, future-state, service blueprint), seven elements per stage (stages, touchpoints, actions, thoughts, emotions, pain points, opportunities), a structured markdown template for documenting each stage, and pre-built journey outlines for technical documentation flows.

The skill activates from natural language mentions of user journeys, customer journeys, experience maps, touchpoint analysis, or service blueprints. When activated, it applies the appropriate journey type based on context and produces a structured stage-by-stage map that teams can fill in, review, and act on.

## Related Plugins

- **[Persona Definition](../persona-definition/)** -- Create the personas whose journeys you map
- **[Navigation Design](../navigation-design/)** -- Design the navigation systems users encounter at each touchpoint
- **[UX Writing](../ux-writing/)** -- Write the microcopy for error states, empty states, and confirmation dialogs along the journey
- **[Content Modelling](../content-modelling/)** -- Design the content structures that back your documentation journeys
- **[Ontology Design](../ontology-design/)** -- Model the knowledge relationships that inform your journey stages

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) — production-grade plugins for Claude Code.
