---
name: deslop-copy
description: >-
  Remove AI slop from marketing copy, blog posts, product descriptions, emails, and
  editorial content — and humanize the result. Use when asked to deslop, humanize,
  or anti-slop marketing copy, landing pages, product descriptions, email campaigns,
  blog posts, or any AI-generated prose. Trigger phrases: "deslop", "anti-slop",
  "remove AI slop", "humanize this copy", "this sounds AI-generated", "make this
  sound human", "clean up marketing copy", "remove AI clichés". NOT for UI microcopy
  or interface text (use deslop-ui). NOT for code cleanup (use ai-slop-cleaner). NOT
  for creating brand-new copy from scratch (use storytelling or prompt-engineering).
  NOT for preventing AI detector flags specifically (use deslop-detect).
allowed-tools:
  - Read
  - Write
  - Edit
---

# Marketing and Editorial Copy Deslop

AI models write the same copy. Every LLM-written landing page delves into your unique value proposition, leverages cutting-edge technology, and empowers teams to achieve unprecedented results. Every AI-generated email ends with "Don't hesitate to reach out." Every blog post opens with "In today's fast-paced world."

Human writers don't write like this. They're specific. They use contractions. They interrupt themselves. They vary sentence length. This skill removes the AI fingerprint from prose.

## When to Use

✅ Use for:
- Landing page copy and product descriptions
- Email campaigns, newsletters, cold outreach
- Blog posts, articles, and editorial content
- Social media copy and ad copy
- About pages, team bios, company descriptions
- Any prose that sounds like a generic AI assistant wrote it

## When NOT to Use

❌ NOT for:
- UI microcopy, buttons, and error messages — use `deslop-ui`
- Code and technical artifact cleanup — use `ai-slop-cleaner`
- Creating copy from scratch — use `storytelling` or `prompt-engineering`
- Evading AI content detectors specifically — use `deslop-detect`
- Technical documentation — not slop territory; accuracy > voice

## The AI Prose Fingerprint

### The blacklist

These words and phrases mark AI-generated text. Flag every instance and replace or delete:

**Verbs (AI favorites)**
- delve, delves, delving
- leverage (as a verb meaning "use")
- empower, empowers, empowering
- unlock (abstract sense: "unlock your potential")
- harness (abstract: "harness the power of")
- utilize (→ use)
- streamline (overused)
- facilitate (→ help, enable, make possible)

**Adjectives (filler superlatives)**
- comprehensive
- robust
- cutting-edge
- state-of-the-art
- innovative (unless something is actually new)
- groundbreaking, revolutionary
- seamless, frictionless
- intuitive
- holistic
- transformative
- unprecedented

**Opener phrases (throat-clearing)**
- "In today's fast-paced world..."
- "In an era where..."
- "As we navigate the complexities of..."
- "It's no secret that..."
- "Now more than ever..."
- "At the end of the day..."
- "In conclusion..." / "To summarize..."
- "It's important to note that..."
- "It's worth mentioning that..."
- "First and foremost..."

**Closing clichés**
- "Don't hesitate to reach out"
- "Feel free to contact us"
- "We look forward to hearing from you"
- "Thank you for considering us"
- "We're excited to connect"

**Filler connectives (at sentence/paragraph start)**
- "Furthermore" / "Moreover" / "Additionally" (→ specific connector or delete)
- "Therefore" / "Thus" / "Hence" (→ "So" or show the connection)
- "Nevertheless" (→ "But", "Still", or restructure)
- "In addition to the above" (→ delete, just say the thing)

**Contrastive parallelism (AI's rhetorical reflex)**
- "It's not about X; it's about Y" — flag every instance
- "It's not just sales; it's relationships"
- "Not working harder, but working smarter"
- "The question isn't what AI can do — it's what should we do with AI"
These frames feel deep but are empty. Replace with a direct statement of the actual position.

**Em-dash overuse**
AI uses em-dashes as emphasis machinery — constantly. One per paragraph is fine. More than two in a piece is a tell. Delete or restructure; don't replace every em-dash with another form of the same pause.

**New AI tell phrases (2025–2026 vintage)**
- "Picture this" / "Imagine this" (story-setup cliché)
- "The implications are clear" (vague conclusory statement)
- "The takeaway?" (fake-Socratic transition)
- "Here's the thing:" (overused pivoting device)
- "At its core," / "At the heart of," (nesting abstraction opener)
- "Game-changer" / "paradigm shift"
- "In the age of AI," / "In this AI-driven era,"

**Vague outcome claims**
- "achieve unprecedented results"
- "drive growth and success"
- "take your business to the next level"
- "make informed decisions"
- "gain valuable insights"
- "deliver exceptional value"

### AI structural patterns

Beyond individual words, AI prose has structural tells:

- **Uniform sentence length** — every sentence is 15–25 words
- **Three-item lists everywhere** — "fast, reliable, and secure"; "plan, execute, and deliver"
- **Every paragraph the same length** — 2–3 sentences, then a transition
- **Benefits listed as abstract nouns** — "efficiency", "clarity", "performance"
- **Problem-agitate-solution every time** — used correctly occasionally, formulaic at scale
- **No examples, no numbers, no names** — abstract claims without evidence
- **No personality or opinion** — AI never takes a controversial position

## Humanization Techniques

Apply these after clearing the blacklist:

### 1. Vary sentence length deliberately
After a long sentence, write a short one. Stop. Then go long again when it serves the point. Rhythm matters more than rules.

### 2. Use contractions
"You're", "it's", "don't", "we'll", "they've". Formal register doesn't mean avoiding contractions — it means being precise. Contractions make copy sound like a person wrote it.

### 3. Start sentences with And, But, So
"And that's where we come in." "But here's the thing." "So we built something different." Trained-on-formal-text AI avoids this. Humans do it constantly.

### 4. Be specific instead of general
"Reduces onboarding time" → "Cut onboarding from 3 weeks to 4 days for Acme's 200-person team." Specificity signals real experience. Vague claims signal fabrication.

### 5. Use questions as transitions
"So why does this matter?" "What does that look like in practice?" Questions break up the rhythm and create a conversational forward pull.

### 6. Add asides and qualifications
Use em dashes and parenthetical asides: "We spent two years — longer than we'd like to admit — figuring out the right architecture." AI rarely second-guesses itself mid-sentence.

### 7. Acknowledge the obvious
"Yes, this is basic stuff." "You've probably heard this before." "This isn't a new insight." Acknowledging the mundane signals honesty. AI writes as though everything it says is novel.

### 8. Take a position
"We think most X tools get this wrong." "The conventional wisdom on Y is backwards." "This approach is slower, and that's a feature, not a bug." Opinions signal a human author.

### 9. Use imperfect transitions
"Anyway." "Right." "Here's the thing." These short pivots feel colloquial. AI transitions are elaborate bridging sentences.

### 10. Let short paragraphs stand alone

Like this one. A single sentence is fine. It creates emphasis.

## Workflow

1. **Scan and flag** — list every blacklist hit and structural pattern before touching anything
2. **Rewrite in passes**:
   - Pass 1: Delete or replace every blacklist item
   - Pass 2: Break up uniform sentence length — add a short punchy sentence (≤8 words) and one long flowing one (≥25 words)
   - Pass 3: Inject one specific example or number per major abstract claim
   - Pass 4: Add contractions where natural (you're, it's, don't, we'll)
   - Pass 5: Replace abstract outcome claims with concrete alternatives; take a clear position where the original is vague
3. **Word budget** — the rewrite must not exceed the original word count; trim if it does
4. **Explain your changes** — name which humanization techniques you applied (e.g., "shortened opener, added contraction, varied sentence length, replaced 'leverage' with 'use'")
5. **Read aloud** — if a sentence sounds like you'd say it in a meeting, keep it; if it sounds like a press release, cut it

## Anti-Pattern: Synonym Swapping

**Symptom**
"Leverage" gets replaced with "harness", "utilize" becomes "employ", "comprehensive" becomes "extensive". The text now fails the blacklist check but reads identically flat.

**Problem**
AI slop is a register problem, not a vocabulary problem. The AI wrote in corporate marketing voice — an entire mode of expression characterized by abstract claims, passive sentiment, and inflated language. Swapping words within that register doesn't change the register.

**Solution**
Rewrite at the sentence level, not the word level. "Our comprehensive platform leverages AI to empower teams" → "We built this so small teams can do what used to take an enterprise department." Completely different construction, same fact.

## Anti-Pattern: Over-Humanization

**Symptom**
Every sentence now starts with "And" or "But". Every paragraph is one sentence. The copy reads like a stream-of-consciousness Twitter thread, not a product description.

**Problem**
Humanization techniques exist to vary rhythm and register — not to be applied maximally to every sentence. Human writers use contractions, questions, and short sentences selectively. Applying every technique everywhere creates a different kind of uniform prose.

**Solution**
Use humanization techniques as punctuation, not as the base register. The default is clear, direct prose. Contractions, asides, and short punchy sentences appear when they serve emphasis or rhythm — not on autopilot.

## Anti-Pattern: Specificity Theater

**Symptom**
Generic claims get replaced with made-up numbers: "Reduces costs" → "Reduces costs by 47%". The text passes the "be specific" check but the numbers are invented.

**Problem**
Fabricated specificity is worse than honest vagueness. Readers notice when numbers are too round (50%) or too precise to be credible without a source. Invented statistics erode trust.

**Solution**
Specificity must be real. Use actual customer data, real timelines, actual names. If you don't have real data, use qualitative specificity instead: "Our customers typically see results in the first week, not the first quarter."

## Reference: Sentence Patterns Before and After

| AI default | Human alternative |
|---|---|
| "Leverage our comprehensive suite of tools" | "Use the tools we built for this exact problem" |
| "Empower your team to achieve unprecedented results" | "Give your team what they need to close deals faster" |
| "In today's fast-paced world, businesses must adapt" | "Things move fast. Here's how to keep up." |
| "Don't hesitate to reach out if you have any questions" | "Questions? Reply to this email." |
| "Furthermore, it's worth noting that our platform..." | "Also:" / "One more thing:" / (just say it) |
| "Deliver exceptional value to your customers" | "Make your customers happy" / (specific outcome) |
| "Gain valuable insights from your data" | "See which pages convert, which drop" / (specific insight) |
| "Our innovative solution transforms the way you work" | "We changed how [specific process] works" |
