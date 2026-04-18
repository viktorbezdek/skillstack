# UX Writing

> **v1.0.11** | Turn "Submit", "Error 404", and "Click here" into interface text that actually helps users succeed.
> Single skill, no references | 13 trigger evals + 3 output evals

## Context to Provide

UX writing works best when you show the current copy and describe where it appears. The skill rewrites specific text, not abstract intentions.

**What information to include in your prompt:**

- **The current copy** -- paste exactly what the button, error, dialog, or label says right now. Seeing "Are you sure?" is the starting point; hearing "our dialog is bad" is not.
- **Where it appears** -- name the feature area (signup form, payment step, settings page, empty dashboard). Context determines tone and verb choice.
- **What the action does or what went wrong** -- for buttons, describe the consequence of clicking. For errors, describe what actually failed. "Save" on a form that immediately publishes to 10,000 subscribers needs different copy than "Save" on a local draft.
- **What the user needs to do next** -- the Useful principle requires a next step. If you know what that step is, include it. If you do not, the skill will ask.
- **Brand voice, if you have one** -- formal/casual, playful/serious, technical audience or general public. Without this, the skill defaults to clear and neutral.

**What makes results better vs worse:**

- Better: paste multiple related pieces of copy together (all the errors on a form, all buttons on a checkout flow) -- the skill can ensure consistency across them
- Better: mention which copy generates the most support tickets or confusion -- this focuses effort on the highest-impact rewrites
- Better: include the surrounding context (what does the page title say? what does the preceding instruction say?) -- copy cannot be evaluated in isolation
- Worse: asking to "improve the copy" without showing the current text
- Worse: requesting marketing or landing page copy -- this skill is for in-product microcopy only
- Worse: asking to fix one word without context ("should it say Save or Submit?") -- the verb depends entirely on what the action does and what surrounds it

**Template prompt:**

```
Rewrite [copy type: error message / button label / empty state / confirmation dialog / form labels] for
[feature area: signup form / payment step / settings page / etc.].

Current copy: [paste exact text]

Context:
- What action does the button do / what went wrong for the error: [describe]
- What should the user do next: [next step]
- Audience: [technical / general / enterprise / consumer]
- Tone: [formal / casual / motivating / neutral]
```

## The Problem

Interface text is the last thing that gets written and the first thing users read. Engineers fill in placeholder copy -- "Submit", "Error: Invalid input", "Click here to learn more" -- and that placeholder ships to production because nobody goes back to improve it. The result: users stare at a "Submit" button and do not know what they are submitting. They see "Error 404" and have no idea what to do about it. They encounter an empty screen with "No items found" and do not know how to create their first item.

Every label, error message, button, tooltip, and empty state is a micro-decision point for the user. Bad copy creates a moment of confusion. A moment of confusion creates hesitation. Hesitation creates form abandonment, support tickets, and the slow erosion of trust that shows up as churn but never gets attributed to the actual cause: the interface said "Submit" instead of "Save changes" and the user was not sure what would happen.

The problem is not that teams do not care about copy. It is that there is no framework for writing it. Engineers default to technical accuracy ("Error: Connection refused at port 443") when users need helpful guidance ("Can't connect to the server. Check your internet connection and try again."). Designers focus on layout and leave the words for later. Product managers write feature specs, not button labels. Nobody owns the words, so the words stay bad.

## The Solution

This plugin treats interface copy as a UX discipline with its own principles, patterns, and quality bar. The Clear-Concise-Useful-Human framework gives every piece of interface text four concrete criteria to meet: use simple words and active voice (Clear), front-load the key information and cut filler (Concise), always provide a next step the user can take (Useful), and sound empathetic and conversational rather than robotic (Human).

The skill provides tone calibration by context -- success messages are celebratory ("You're all set!"), error messages are helpful without blaming ("Let's fix this"), warnings are direct ("This can't be undone"), and empty states are encouraging ("Create your first project"). It includes concrete before/after rewrites for the four most common UI text patterns: buttons (Verb + Object formula), error messages (what happened + what to do), confirmation dialogs (action-specific title + irreversibility warning + labeled buttons), and form labels (plain language label + example placeholder + helper text).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Button says "Submit" -- user does not know what will happen | Button says "Save changes" -- Verb + Object formula makes every action clear |
| Error says "Error 404" -- user has no recovery path | Error says "Page not found -- try searching or go to homepage" -- every error includes a next step |
| Empty state is blank or says "No items found" | Empty state says "Create your first project to start organizing your work" with a visible action button |
| Confirmation dialog says "Are you sure?" with OK/Cancel | Confirmation says "Delete 'Report'? This can't be undone." with [Delete]/[Cancel] buttons |
| Error messages use technical jargon: "Connection refused at port 443" | Error messages use human language: "Can't connect to the server. Check your internet connection and try again." |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install ux-writing@skillstack
```

### Prerequisites

No additional dependencies. Works with any Claude Code session.

### Verify installation

After installing, test with:

```
Rewrite these error messages to be more helpful -- "Error 404", "Invalid input", "Server error"
```

## Quick Start

1. Install the plugin with the commands above
2. Type: `My form buttons all say "Submit" -- rewrite them for each form type: signup, payment, and settings`
3. The skill applies the Verb + Object formula and produces context-specific labels: "Create account", "Complete payment", "Save settings"
4. Review the before/after comparison to see how each new label tells the user exactly what happens next
5. Next, try: `Write empty state copy for a dashboard that has no projects yet`

---

## System Overview

```
User prompt (microcopy request, error message rewrite, button label, empty state)
        |
        v
+------------------------+
|     ux-writing         |
|      (SKILL.md)        |
+------------------------+
        |
        |-- 4 Principles
        |     Clear: simple words, active voice
        |     Concise: front-load key info, cut filler
        |     Useful: always provide a next step
        |     Human: empathetic, conversational
        |
        |-- 4 Tone Contexts
        |     Success -> celebratory ("You're all set!")
        |     Error -> helpful ("Let's fix this")
        |     Warning -> direct ("This can't be undone")
        |     Empty -> encouraging ("Create your first...")
        |
        |-- 4 UI Pattern Templates
              Buttons: Verb + Object formula
              Errors: what happened + what to do
              Confirmations: action title + consequence + labeled buttons
              Form labels: plain label + example + helper text
```

This is a compact single-skill plugin with no reference documents. All methodology -- principles, tone guidance, and pattern templates -- fits directly in the core `SKILL.md`. The skill identifies which UI pattern applies to your request, selects the appropriate tone context, and produces specific rewrites with explanations.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `skills/ux-writing/SKILL.md` | Skill | Core principles (Clear, Concise, Useful, Human), tone-by-context guidance, four UI pattern rewrites (buttons, errors, confirmation dialogs, form labels) |
| `evals/trigger-evals.json` | Eval | 13 trigger scenarios for activation boundary testing |
| `evals/evals.json` | Eval | 3 output quality scenarios for copy improvement |

### Component Spotlight

#### ux-writing (skill)

**What it does:** Activates when you need to write or improve microcopy, error messages, button labels, empty states, confirmation dialogs, form labels, or any interface text. Applies the Clear-Concise-Useful-Human framework, calibrates tone by context (success, error, warning, empty state), and provides before/after rewrites using proven UI text patterns.

**Input -> Output:** You describe your current interface text, the context it appears in, and optionally what is going wrong -> You get rewritten copy following the four principles, with before/after comparison and explanation of why each change improves the experience.

**When to use:**
- Replacing placeholder "Submit", "OK", "Cancel" buttons with meaningful labels
- Rewriting generic error messages so users know what went wrong and what to do
- Writing empty state copy that explains the feature and encourages the first action
- Creating confirmation dialogs for destructive actions with clear consequences
- Building a tone guide for consistent voice across an application
- Writing microcopy for onboarding flows, tooltips, or password reset flows

**When NOT to use:**
- Generating long-form documentation or help articles -> use [documentation-generator](../documentation-generator/)
- Designing visual layout or navigation patterns -> use [frontend-design](../frontend-design/) or [navigation-design](../navigation-design/)
- Creating content models for a CMS -> use [content-modelling](../content-modelling/)

**Try these prompts:**

```
Rewrite the error messages for our registration form. Every field shows "Invalid input" on validation
failure. The fields are: email address, password (min 8 chars, one uppercase, one number), username
(3-20 chars, alphanumeric only), and company name (optional). Users are signing up for a B2B SaaS tool --
technical audience, expect precision.
```

```
My checkout has five steps and every primary button says "Continue". Rewrite them with specific labels.
Here is what each button actually does:
1. Cart review page: proceeds to shipping address entry
2. Shipping page: saves address and moves to delivery options
3. Delivery options: confirms selection and goes to payment
4. Payment page: charges the card and creates the order
5. Order confirmation: returns to the product catalog
```

```
Write empty state copy for the Saved Reports screen in our analytics tool. A new user lands here with
no reports yet. The feature lets users save custom query results as named reports they can revisit and
share. The first action is "Create report" which opens a query builder. Tone: helpful but not overly
enthusiastic -- our users are data analysts.
```

```
Rewrite this confirmation dialog for permanently deleting a workspace in our project management tool.
A workspace contains all the user's projects, tasks, and files.

Current dialog:
Title: "Warning"
Body: "Are you sure you want to delete this workspace? This action cannot be undone."
Buttons: [OK] [Cancel]

The user must understand exactly what they will lose and that it is permanent. They should feel
like they made an active, informed choice, not like they clicked through an obstacle.
```

```
Our B2B SaaS tool uses inconsistent tone across contexts: success messages sound robotic ("Operation
completed successfully"), errors sound alarming ("CRITICAL ERROR: Request failed"), warnings are
passive ("Please note that..."). Create a tone guide for all four contexts (success, error, warning,
empty state) for a business productivity tool used by operations teams. Not playful, but not corporate.
```

```
Write all the microcopy for our password reset flow. The flow has three screens:
1. Enter email screen (user requests reset link)
2. Confirmation screen (link sent, user should check email)
3. Success screen (password has been changed, user is now logged in)

One complication: if the email is not in our system, we still show the "link sent" screen (security
best practice). The copy needs to handle this without being dishonest.
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, may not activate) | Good (specific, activates reliably) |
|---|---|
| "Help with copy" | "Rewrite our form error messages -- right now they all say 'Invalid input'" |
| "Fix my text" | "My checkout has five buttons that all say 'Submit' -- write specific labels for each step" |
| "Write something for the empty page" | "Write empty state copy for a dashboard with no projects -- explain the feature and encourage the first action" |
| "Make the dialog better" | "Rewrite this confirmation dialog for file deletion: title 'Warning', body 'Are you sure?', buttons 'OK'/'Cancel'" |
| "Our copy is bad" | "Our errors sound angry and success messages sound robotic -- help me create a consistent tone guide" |

### Structured Prompt Templates

**For error message rewrites:**
```
Rewrite these error messages so users know what's wrong and what to do: [list current error messages]. Context: they appear in [form type / feature area].
```

**For button label improvements:**
```
My [feature area] has these buttons that all say [current generic label]. Write specific labels for each: [list the actions each button performs].
```

**For empty state copy:**
```
Write empty state copy for [screen name] when [what's missing, e.g., "the user has no projects yet"]. It should explain [what the feature does] and encourage [the first action].
```

**For confirmation dialogs:**
```
Rewrite the confirmation dialog for [destructive action, e.g., "deleting a project"]. Current dialog: title "[current title]", body "[current body]", buttons [current buttons]. The user needs to understand [what happens / consequence].
```

**For tone guides:**
```
Create a tone guide for our [type of app]. We want to sound [desired voice, e.g., "motivating but not annoying"]. Cover success, error, warning, and empty state contexts with examples.
```

### Prompt Anti-Patterns

- **Asking for "good copy" without providing context:** "Write better copy" does not tell the skill what UI pattern to apply or what tone context to use. Provide the current copy, where it appears, and what the user is trying to do.
- **Requesting marketing copy instead of interface text:** "Write copy for our landing page headline" is marketing, not UX writing. This skill is for in-product microcopy -- buttons, errors, empty states, dialogs, form labels.
- **Asking to fix just one word:** "Should my button say 'Save' or 'Submit'?" is too narrow. Provide the full context -- what form it is on, what happens when clicked, what other buttons are nearby -- so the skill can apply the Verb + Object formula properly.
- **Dumping all app copy for review without indicating problems:** "Here's all our copy, make it better" is too broad. Start with the worst offenders -- the screens that generate support tickets or have the highest drop-off rates.

## Real-World Walkthrough

You are a frontend engineer working on a project management app. The app shipped three months ago with placeholder copy that was never replaced. Your support team reports that 30% of tickets are "I don't understand what this button does" or "I got an error and don't know what to do." Your PM asks you to do a "copy pass" across the app, but you have no framework for what good copy looks like.

**Step 1 -- Fix the error messages.** You start with the worst offender:

```
Our app shows these errors and users always contact support. Rewrite them: "Error: Invalid input", "Operation failed", "Error 500", "Timeout", "Not authorized"
```

The skill applies the error message pattern (what happened + what to do):

- "Error: Invalid input" becomes "This email address needs an @ symbol" (field-specific, not form-level)
- "Operation failed" becomes "Could not save your changes. Check your connection and try again."
- "Error 500" becomes "Something went wrong on our end. We're looking into it -- try again in a few minutes."
- "Timeout" becomes "This is taking longer than usual. Check your connection or try again."
- "Not authorized" becomes "You don't have access to this page. Contact your team admin to request access."

The skill points out that "Not authorized" is particularly bad because it does not tell the user who can fix it.

**Step 2 -- Fix the buttons.** You tackle every "Submit" button:

```
Here are all the buttons in our app that say "Submit": signup form, settings page, project creation, task assignment, and invoice generation. Rewrite each one.
```

The skill applies Verb + Object: "Create account", "Save settings", "Create project", "Assign task", "Generate invoice." Each button now tells the user exactly what clicking it will do.

**Step 3 -- Fix the confirmation dialogs.** Your single reusable dialog ("Warning" / "Are you sure?" / OK / Cancel) gets three context-specific versions:

```
Rewrite our confirmation dialog for deleting a project, removing a team member, and canceling a subscription
```

**Delete project:** "Delete 'Q4 Report'? This will permanently delete the project and all its tasks. This can't be undone." [Delete project] [Keep project]

**Remove member:** "Remove Sarah from this project? Sarah will lose access to all project files and conversations." [Remove member] [Cancel]

**Cancel subscription:** "Cancel your Pro plan? You'll keep access until March 15, then your account switches to the free plan." [Cancel subscription] [Keep Pro plan]

**Step 4 -- Fix the empty states.** "No items" on every empty screen becomes feature-specific copy:

```
Write empty state copy for: projects list (new user), team members (solo user), and reports (no data yet)
```

"No items" on projects becomes "Organize your work into projects. Create your first project to get started." with a [Create project] button.

**Step 5 -- Result.** Support tickets about confusing interface copy drop by half within the first month. The copy pass took a single day using the framework. The Clear-Concise-Useful-Human framework becomes your team's standard.

**Gotchas discovered:** The biggest impact came from making buttons action-specific (Verb + Object), not from rewriting errors. Users who understand what a button does make fewer errors in the first place.

## Usage Scenarios

### Scenario 1: Rewriting form error messages

**Context:** You are a developer and your registration form shows "Invalid input" for every validation error. Users cannot figure out what is wrong with their submission.

**You say:** `Rewrite the error messages for our registration form -- right now every field just shows "Invalid input" when validation fails`

**The skill provides:**
- Field-specific error messages: "Email address needs an @ symbol", "Password must be at least 8 characters", "This username is already taken -- try another"
- Placement guidance: show errors inline below the field, not in a banner at the top
- Tone calibration: helpful without blaming ("needs an @ symbol" not "you entered an invalid email")

**You end up with:** Error messages that tell users exactly what is wrong and how to fix it, reducing form abandonment and support tickets.

### Scenario 2: Creating a tone guide for a new product

**Context:** You are a product designer launching a new app and want consistent voice across all interface text from day one.

**You say:** `Help me create a tone guide for our fitness app -- we want to sound motivating but not annoying`

**The skill provides:**
- Tone calibration across four contexts: success (celebratory but not over-the-top), error (supportive, not blaming), warning (honest, not scary), empty state (motivating, not pushy)
- Example copy for each context tailored to a fitness domain
- Anti-patterns to avoid: overly casual ("Oopsie!"), corporate ("An error has occurred"), or patronizing ("Great job clicking that button!")

**You end up with:** A documented tone guide with examples that your entire team can follow for consistent interface copy.

### Scenario 3: Writing onboarding microcopy

**Context:** Your SaaS app has a five-step onboarding wizard but users drop off at step 3. The copy in each step is generic ("Step 3 of 5") and does not explain why each step matters.

**You say:** `Write microcopy for each step of our onboarding wizard -- users drop off at step 3 (connecting their data source) and we think the copy isn't motivating enough`

**The skill provides:**
- Progress indicators that show value, not just position ("Almost there -- connect your data to see your first dashboard")
- Step descriptions that explain why each step matters ("Connect your data source so we can show you real insights, not sample data")
- Encouragement copy at friction points ("This usually takes about 2 minutes. We'll walk you through it.")

**You end up with:** Onboarding copy that motivates users through the hard steps and reduces drop-off by connecting each step to the value they will get.

### Scenario 4: Improving an existing confirmation dialog

**Context:** Your e-commerce app uses a generic "Are you sure?" dialog for removing items from the cart, and users accidentally confirm removals because the buttons say "OK" and "Cancel."

**You say:** `Users keep accidentally removing items from their cart because the confirmation dialog is too generic -- rewrite it`

**The skill provides:**
- Action-specific title: "Remove 'Blue Running Shoes' from your cart?"
- Consequence description: "You can always add it back later."
- Labeled buttons: [Remove item] [Keep in cart] instead of [OK] [Cancel]
- Optional: undo toast as an alternative to the confirmation dialog for low-stakes actions

**You end up with:** A confirmation dialog where users understand exactly what will happen, and accidental removals drop significantly.

---

## Decision Logic

**Which UI pattern template applies?**

The skill selects from four templates based on what you describe: buttons (any call-to-action or form submission), error messages (any failure or validation state), confirmation dialogs (any action with consequences the user should understand before proceeding), and form labels (any input field needing a label, placeholder, and helper text). If your request spans multiple patterns -- "rewrite all the copy on our checkout page" -- the skill applies each pattern to the relevant elements.

**How does tone context get selected?**

Tone comes from the situation, not the preference. Success messages (user completed an action) get celebratory tone. Error messages (something failed) get helpful tone. Warnings (action has irreversible consequences) get direct tone. Empty states (nothing to show yet) get encouraging tone. You do not pick the tone -- the context determines it. The only customization is brand voice (formal vs casual, playful vs serious), which adjusts the intensity within each context.

**When to use this skill vs the frontend-design or navigation-design skill?**

This skill handles the words inside the interface. If you are deciding what a button should say, what an error message should communicate, or what copy goes in an empty state -- use this skill. If you are deciding where the button goes, how it looks, or how the page is laid out -- use frontend-design. If you are deciding what navigation labels to use or how to structure the information architecture -- use navigation-design.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| Applying the same tone to every context | Success messages sound as serious as errors; error messages sound as casual as success messages -- the app feels emotionally flat | Map each piece of copy to one of the four tone contexts (success, error, warning, empty state). Each context has a different register. Celebratory success + helpful error + direct warning creates emotional range. |
| Error messages that are too vague even after rewriting | "Something went wrong" is still not actionable when the user could have fixed it with specific information like "Your file exceeds the 10 MB limit" | Push for specificity: every error should include what the user can do next. If the error comes from a validation rule, include the rule. If it requires support, include how to contact them. |
| Button labels that are action-specific but too long | "Save your updated notification preferences and return to the settings page" does not fit in a button | Keep buttons to 2-4 words maximum. The Verb + Object formula produces "Save preferences" -- the rest of the context comes from the page heading and surrounding UI, not the button label. |
| Empty state copy that only explains but does not provide a call-to-action | "Reports show your project's progress over time." describes the feature but the user still does not know what to do next | Every empty state needs a visible action element -- a button or link that starts the process. Explanation + call-to-action ("Track your project's progress. Create your first report.") is the pattern. |
| Over-optimizing microcopy for personality at the expense of clarity | "Oopsie-daisy, something borked!" might sound on-brand but tells the user nothing about what happened or what to do | The Clear principle always outranks the Human principle. Be human and empathetic, but never at the expense of clear communication. Users in error states need help, not personality. |

## Ideal For

- **Frontend engineers writing interface text** -- the framework replaces guesswork with concrete patterns for buttons, errors, empty states, and dialogs
- **Product teams doing a "copy pass" before launch** -- the four principles and tone guide provide a systematic approach instead of ad-hoc rewrites
- **Designers creating prototypes with realistic copy** -- placeholder text creates false usability signals; realistic copy reveals real friction
- **Teams with no dedicated UX writer** -- the patterns are simple enough for any team member to apply consistently

## Not For

- **Generating long-form documentation or help articles** -- use [documentation-generator](../documentation-generator/) for technical docs, tutorials, and API references
- **Designing visual layout or navigation patterns** -- use [frontend-design](../frontend-design/) for component design or [navigation-design](../navigation-design/) for information architecture
- **Creating content models for a CMS** -- use [content-modelling](../content-modelling/) for structured content types and editorial workflows
- **Writing marketing copy for landing pages** -- this skill is for in-product microcopy, not acquisition-stage content

## Related Plugins

- **[User Journey Design](../user-journey-design/)** -- Map the journeys where your microcopy appears at each touchpoint
- **[Persona Definition](../persona-definition/)** -- Understand who reads your copy so tone and vocabulary match their expectations
- **[Navigation Design](../navigation-design/)** -- Design the navigation labels and wayfinding text
- **[Content Modelling](../content-modelling/)** -- Structure the content types that contain your copy
- **[Frontend Design](../frontend-design/)** -- Design the visual components where your copy lives

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
