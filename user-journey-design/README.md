# User Journey Design

> **v1.0.10** | Design & UX | 11 iterations

Design user journey maps with touchpoints, emotional states, pain points, and opportunities.

## What Problem Does This Solve

Product teams often optimize individual screens while missing the friction that accumulates across the full experience. A signup page might test well in isolation, but the journey from discovering a product to successfully using it for the first time could be full of dead ends, confusing hand-offs, and emotional low points that never surface in screen-level reviews. User journey mapping makes that cross-stage friction visible by documenting what users do, think, feel, and struggle with at every touchpoint -- so improvements can be prioritized where they reduce the most pain rather than where they are easiest to implement.

This skill provides three journey formats (current-state, future-state, service blueprint), a structured template with seven elements per stage, and pre-built journey outlines for common technical documentation flows.

## Installation

Add the SkillStack marketplace, then install this plugin:

```bash
/plugin marketplace add viktorbezdek/skillstack
/plugin install user-journey-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention the triggers below, or you can invoke it explicitly.

**Direct invocation:**

```
Use the user-journey-design skill to map the onboarding experience
```

**Natural language triggers** -- Claude activates this skill automatically when you mention:

- `user-journey`
- `touchpoints`
- `experience-mapping`

## What's Inside

This is a **single-skill plugin** with no reference documents and two eval suites.

| Component | Path | Purpose |
|---|---|---|
| Skill | `skills/user-journey-design/SKILL.md` | Journey types, core elements, structured template, and documentation journey outlines |
| Evals | `evals/trigger-evals.json` | Trigger scenarios for activation boundary testing |
| Evals | `evals/evals.json` | Output quality scenarios for journey map generation |

**Journey types covered:**

| Type | Focus | Use when... |
|---|---|---|
| Current-state | As-is experience | Mapping what users experience today to find friction |
| Future-state | To-be design | Designing the improved experience before building it |
| Service blueprint | Combined user + org view | You need to see both front-stage user actions and back-stage organizational processes |

**Seven elements per stage:** Stages, Touchpoints, Actions, Thoughts, Emotions (confidence-to-frustration scale), Pain Points, Opportunities.

## Usage Scenarios

**1. "Map the new user experience from first hearing about the product to being a power user"**
The skill provides a stage-by-stage journey (Awareness, Evaluation, Onboarding, Usage, Mastery) with the structured template for goals, actions, touchpoints, emotion scores, and opportunities at each stage. Fill in the template per stage to see where the emotional low points cluster.

**2. "Where are users getting frustrated during API integration?"**
Use the pre-built API Integration journey (Discover, Credentials, Read Reference, Test, Production) as a starting framework. Each stage gets its own pain point and opportunity analysis. Common findings: credentials setup is confusing, reference docs lack runnable examples, error messages during testing are opaque.

**3. "I need to compare the current experience with the redesign"**
Create two journey maps -- current-state and future-state -- using the same stage structure. Side-by-side comparison reveals which stages improve, which get worse, and where the redesign introduces new friction the team did not anticipate.

**4. "What questions should I ask in user research to fill in a journey map?"**
The seven elements (touchpoints, actions, thoughts, emotions, pain points, opportunities) directly map to interview and observation questions. For each stage, ask: "What did you do?", "Where did you interact with us?", "What were you thinking?", "How confident or frustrated did you feel?", "What was painful?", "What would have helped?"

**5. "Help me find where to invest in documentation improvements"**
Use the Getting Started and Troubleshooting journey templates. They reveal where documentation gaps create user drop-off -- for example, if users land on the quickstart but cannot find the setup prerequisites, or if the troubleshooting flow assumes knowledge the user does not have.

## When to Use / When NOT to Use

**Use when:**
- Mapping end-to-end user experiences across multiple touchpoints
- Identifying where friction accumulates across stages (not just individual screens)
- Designing before/after comparisons for a product redesign
- Planning documentation improvements based on where users drop off
- Creating service blueprints that show both user and organizational processes

**Do NOT use when:**
- Creating individual user personas -- use [persona-definition](../persona-definition/) instead
- Designing navigation patterns or information architecture -- use [navigation-design](../navigation-design/) instead
- Writing the actual interface copy for touchpoints -- use [ux-writing](../ux-writing/) instead

## Related Plugins in SkillStack

- **[Persona Definition](../persona-definition/)** -- Create the personas whose journeys you map
- **[Navigation Design](../navigation-design/)** -- Design the navigation systems users encounter at each touchpoint
- **[UX Writing](../ux-writing/)** -- Write the microcopy for error states, empty states, and confirmation dialogs along the journey
- **[Content Modelling](../content-modelling/)** -- Design the content structures that back your documentation journeys
- **[Ontology Design](../ontology-design/)** -- Model the knowledge relationships that inform your journey stages

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
