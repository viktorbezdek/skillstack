---
name: deslop-ui
description: >-
  Audit and rewrite UI copy to remove AI slop — overlong button labels, hedging error
  messages, corporate filler, and passive voice in interface text. Use when asked to
  clean up UI text, deslop interface copy, fix AI-sounding buttons or error messages,
  audit microcopy for AI patterns, or humanize product UI. Trigger phrases: "deslop",
  "anti-slop", "remove AI slop from UI", "clean up button labels", "fix error messages",
  "humanize interface text", "UI copy review". NOT for writing new UI copy from scratch
  (use ux-writing). NOT for marketing or editorial prose (use deslop-copy). NOT for
  code quality cleanup (use ai-slop-cleaner).
allowed-tools:
  - Read
  - Write
  - Edit
---

# UI Copy Deslop

AI-generated UI text has a fingerprint. It over-explains, hedges, and defaults to corporate register. Human-written UI text is abrupt, direct, and treats the user as an adult. This skill removes the fingerprint.

## When to Use

✅ Use for:
- Button labels, CTA text, navigation items
- Error messages, validation messages, form hints
- Empty states, zero-data states, placeholder text
- Success and confirmation messages
- Onboarding tooltips, walkthroughs, and modals
- Any interface text that sounds like it was written by an AI assistant

## When NOT to Use

❌ NOT for:
- Writing new UI copy from scratch — use `ux-writing` for that
- Marketing landing pages, email copy, blog posts — use `deslop-copy`
- Code cleanup — use `ai-slop-cleaner`
- Brand voice guidelines or tone-of-voice documents

## The AI UI Copy Fingerprint

Patterns that mark UI text as AI-generated, ordered by frequency:

### Overlong button labels
- "Click here to submit your form" → **Submit**
- "Proceed to the next step" → **Next** or **Continue**
- "Save your changes and continue editing" → **Save**
- "Add a new item to your list" → **Add item**

### Hedging error messages
- "There seems to have been an issue processing your request" → **Couldn't process request**
- "It appears that something may have gone wrong" → **Something went wrong**
- "We were unable to complete this action at this time" → **Action failed**
- "An unexpected error has occurred" → **Error — [specific error]**

### Gratuitous politeness
- "Thank you for your patience while we process your data" → *(delete)*
- "We appreciate your understanding" → *(delete)*
- "Please ensure that you have completed all required fields" → **Fill in the required fields**

### Corporate superlatives in UI
- "Comprehensive analytics dashboard" → **Analytics**
- "Seamless integration experience" → **Integrations**
- "Powerful and intuitive" → *(delete — show, don't describe)*
- "Leverage our advanced AI" → *(delete from UI — belongs in marketing)*

### Passive voice in status messages
- "Your account has been successfully created" → **Account created** or **You're in**
- "The file has been uploaded" → **File uploaded**
- "Your changes have been saved" → **Saved**
- "An email has been sent to you" → **Check your email**

### Empty state verbosity
- Four-paragraph explanation of why the list is empty → **No items yet. [CTA]**
- Motivational text in empty states → cut it, keep the CTA
- "It looks like you haven't added anything yet!" → **Nothing here yet.**

### AI-specific onboarding patterns
- Tooltip with three paragraphs → one sentence or cut
- "Don't worry, you can always change this later" → *(delete)*
- "This is where you will [long explanation]" → **[Name of thing]** + tooltip if needed

## Component Word Budget

Apply these hard ceilings. Count words in every replacement before delivering it.

| Component type | Max words | Notes |
|---|---|---|
| Button / CTA | 3 | Action verb + object. Drop "click here", "proceed to". |
| Error message | 10 | State condition + recovery. No hedging, no gratitude. |
| Success message | 5 | Drop "successfully". State the outcome. |
| Empty state headline | 8 | State the condition only. No motivation. |
| Empty state body | 15 | One sentence max. CTA follows separately. |
| Tooltip | 10 | Name the thing + one action. No benefit lists. |
| Section header | 2 | Noun only. No adjectives. |
| Form hint | 8 | Imperative voice. No "please ensure". |

## Slop Type Taxonomy

Use EXACTLY these labels when classifying UI copy. Do not invent synonyms — these specific words are the vocabulary:

| Label | What it means | Example |
|---|---|---|
| `overlong` | Label is too many words for its function | "Click here to proceed to checkout" |
| `hedging` | Weasel words that avoid commitment | "There seems to have been an issue" |
| `passive` | Auxiliary verb construction hides the subject | "Your file has been uploaded" |
| `superlative` | Hollow adjective that adds no information | "Comprehensive Analytics Dashboard" |
| `verbose` | Over-explains what the user already understands | Four-sentence empty state |
| `reassurance` | Unnecessary comfort text ("don't worry", "easy") | "Creating an account is easy!" |
| `parallelism` | Contrastive "It's not X; it's Y" frame | "It's not about storage; it's about collaboration" |
| `em-dash` | Em-dash as emphasis machinery (more than 1 per message) | "We're here — always — for you" |

## Mandatory Output Format

Every deslop-ui response MUST follow this format. Include the slop type label for every item:

```
## Slop Audit

| # | Original | Type | Replacement |
|---|---|---|---|
| 1 | [original text] | overlong | [replacement] |
| 2 | [original text] | hedging | [replacement] |

**Types used:** [list only the labels found from the taxonomy above]

## Word Count Check
[For each item: "Item N: X words ✓" or "Item N: X words — cut to Y"]
```

After the table, produce a **Slop Score** for the original and the rewrite:

```
## Slop Score

| Dimension | Original (1-10) | Rewrite (1-10) | Notes |
|---|---|---|---|
| Directness | N | N | Statements, not announcements |
| Concision | N | N | Nothing cuttable? |
| Trust | N | N | Respects user intelligence |
| Authenticity | N | N | Sounds like a person |
| Clarity | N | N | Understood in one pass |
| **Total** | **/50** | **/50** | |

Threshold: original <35 = needed work; rewrite ≥40 = passing.
```

## Workflow

1. **Count originals** — note word count for each item before touching anything
2. **Audit** — classify every item into the table using the slop types above
3. **Apply word budgets** — replacements must meet the Component Word Budget ceiling
4. **Fill the table** — complete the Slop Audit format above; no skipping items
5. **Word Count Check** — explicitly state whether each replacement meets its budget
6. **Verify** — read the result aloud; if it sounds like something a human would type in Slack, it passes

## Decision Tree

```
Is it a button/CTA?
  → Is it longer than 2–3 words? → Cut to the action verb + object
  → Does it contain "click here" or "proceed to"? → Delete those, keep the action

Is it an error message?
  → Does it hedge? ("seems", "appears", "may have") → Replace with direct statement
  → Does it thank the user? → Delete gratitude
  → Does it use passive voice? → Convert to active or drop the auxiliary

Is it a success message?
  → Does it say "successfully"? → Delete — success is implied by the message appearing
  → Is it longer than 5 words? → Cut it

Is it an empty state?
  → Is it longer than one sentence + one CTA? → Cut to one sentence + CTA
  → Does it use "it looks like" or "it seems"? → Delete opener, state the condition directly

Is it onboarding/tooltip text?
  → Is it longer than 15 words? → Cut to under 10
  → Does it contain reassurance ("don't worry")? → Delete
```

## Anti-Pattern: The "Friendly" Hedge

**Symptom**
Error messages and status text read like a customer service apology: "We're sorry, but it seems there may have been a small issue with processing your request. Please try again later."

**Problem**
AI models trained on customer service data default to apologetic, hedging registers. The result is verbose, passive, and treats the user as fragile. It obscures what actually happened and what the user should do. Users in error states want information, not reassurance.

**Solution**
State the condition directly, within 10 words. If there's a recovery action, state it on the same line. "Couldn't save — check your connection." is better than five sentences of empathy.

## Anti-Pattern: The Superlative Decoration

**Symptom**
UI labels and section headers contain adjectives that describe the feature rather than naming it: "Comprehensive Reporting Dashboard", "Powerful Automation Tools", "Intuitive Project Management".

**Problem**
These adjectives exist because AI generates them by default — they're statistically likely after feature names in its training data. They add zero information, inflate labels beyond comfortable scan length, and sound like marketing copy inside a product interface. Users navigate by nouns, not superlatives.

**Solution**
Name the thing. "Reports", "Automation", "Projects". If a qualifier is genuinely needed to disambiguate, use a specific one: "Custom Reports" vs "Standard Reports", not "Powerful Reports".

## Anti-Pattern: The Verbose Empty State

**Symptom**
An empty state has two paragraphs: one explaining what the section is for, one reassuring the user that creating their first item is easy and they'll love the experience.

**Problem**
Empty states get read once — at the moment the user lands with no data. After that, they never see it again. Two paragraphs of explanation are wasted pixels. The motivational close ("You'll love it!") is the most cringeworthy genre of AI-generated copy.

**Solution**
One line stating the condition + one CTA button. If context truly helps, add a single short sentence. "No saved items. [Save your first item]" covers everything.

## Reference: Word-Level Replacements

| AI default | Human alternative |
|---|---|
| leverage (verb) | use |
| utilize | use |
| comprehensive | (delete) |
| robust | (delete or be specific) |
| seamless | (delete) |
| powerful | (delete or show it) |
| intuitive | (delete) |
| innovative | (delete) |
| cutting-edge | (delete or name the thing) |
| ensure | make sure / check |
| please ensure | check |
| successfully | (delete) |
| currently | now / (delete) |
| at this time | now / (delete) |
| in order to | to |
| please be aware | (delete opener) |
| it is important to note | (delete opener) |
| feel free to | (delete) |
