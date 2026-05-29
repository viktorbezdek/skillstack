---
name: deslop-detect
description: >-
  Rewrite AI-generated content to evade AI content detectors by increasing perplexity,
  burstiness, and lexical entropy. Use when asked to make content pass GPTZero,
  Originality.ai, Turnitin AI detection, Copyleaks, or any AI content detector; when
  asked to make writing "undetectable"; or when existing deslop passes fail detection
  checks. Trigger phrases: "pass AI detector", "evade AI detection", "make this
  undetectable", "GPTZero", "Originality.ai", "Turnitin", "AI detection score",
  "reduce AI score", "beat the detector", "bypass AI checker". NOT for general copy
  quality improvement (use deslop-copy). NOT for UI copy cleanup (use deslop-ui).
  NOT for code (use ai-slop-cleaner). NOT for academic fraud — this skill is for
  legitimate content creators reclaiming work that was partially AI-assisted.
allowed-tools:
  - Read
  - Write
  - Edit
---

# AI Detection Prevention

AI content detectors measure statistical properties of text — not meaning. They look for patterns that distinguish machine-generated sequences from human-written ones. Understanding what they measure tells you exactly where to intervene.

## When to Use

✅ Use for:
- Content that was partially AI-assisted and needs to pass detection for legitimate publishing
- Marketing copy that AI detection is flagging incorrectly (false positive remediation)
- Testing whether desloped content will clear detection thresholds before publication
- Understanding why a piece is flagging and how to fix it
- Ensuring compliance with platforms or clients that require human-written content

## When NOT to Use

❌ NOT for:
- General copy quality improvement without a detection concern — use `deslop-copy`
- UI microcopy — use `deslop-ui`
- Academic fraud, plagiarism detection evasion, or submitting AI work as human in academic contexts
- Deceiving audiences about the fundamental origin of content in ways that harm trust
- Code cleanup — use `ai-slop-cleaner`

## How AI Detectors Work

The three metrics that most detectors measure, and what they actually check:

### 1. Perplexity
How predictable each token is given its context. Language models predict the most statistically likely next token. When a model writes, it produces low-perplexity text — everything that follows is what you'd expect. Human writers make less predictable choices: unusual word order, unexpected transitions, idiosyncratic vocabulary.

**What to measure against**: GPTZero uses perplexity as its primary signal. Low perplexity = high AI probability.

**How to increase it**: Use unexpected but correct word choices. Start sentences mid-thought. Make structural choices that violate conventions deliberately. Reference specific things that require real knowledge.

### 2. Burstiness
How much sentence length varies throughout the piece. AI produces uniformly medium-length sentences (15–25 words each). Human writers burst: three-word sentences followed by compound sentences that run for fifty words across two independent clauses before landing.

**What to measure against**: GPTZero's burstiness score. Low variance = high AI probability.

**How to increase it**: Deliberately alternate between very short sentences (3–6 words) and long ones (35+ words). The contrast is the signal.

### 3. Lexical Entropy / Homogeneity
How varied the vocabulary is, and how homogeneous the sentence structure is. AI models have preferred token patterns — they write the same transitional phrases, the same sentence frames, the same closing structures.

**What to measure against**: Originality.ai trains on content features. Turnitin's AI detection looks at these structural patterns.

**How to increase it**: Vary sentence structure at the grammatical level. Open sentences differently: with a noun, a verb, a preposition, a conjunction, an interjection. Break the pattern.

## The Major Detectors and Their Blind Spots

| Detector | Primary signal | Threshold approach | Notes |
|---|---|---|---|
| **GPTZero** | Perplexity + burstiness | Burstiness is the easier lever | Most deployed in education |
| **Originality.ai** | Trained classifier | Structural patterns matter more than vocabulary | Aggressive; many false positives |
| **Turnitin AI** | Sentence structure + statistical patterns | Sentence opening variety helps | Education market |
| **Copyleaks** | Multiple signals | Specific vocabulary and transitions matter | Also checks plagiarism |
| **ZeroGPT** | Simpler heuristics | Easier to clear | Less reliable in general |
| **Sapling** | Perplexity-based | Similar to GPTZero approach | Often used in writing platforms |

## Rewriting Strategy

Apply in order. Each pass targets a different detector signal.

### Pass 1: Burstiness injection (highest ROI)

**Mandatory targets — verify these before finishing:**
- At least one sentence of **≤5 words** (short, punchy, emphatic)
- At least one sentence of **≥35 words** (long, flowing, subordinate-clause-heavy)
- No more than 3 consecutive sentences within the 12–28 word range

Go through the text and identify runs of similar-length sentences. After every 2–3 medium sentences, add a short one (3–5 words). Then let one sentence run long. The pattern: medium, medium, **short**, medium, long, medium, **short**.

Before: "AI detectors measure statistical properties of text. They use perplexity and burstiness to identify machine-generated content. Both metrics are well-documented in the research literature."

After: "AI detectors measure statistics, not meaning. They care about two things: how predictable your word choices are, and how much your sentence lengths vary. That's it. Once you understand those two levers, the rest follows."

After completing the rewrite, **explicitly state**: "Shortest sentence: [sentence] ([N] words). Longest sentence: [sentence] ([N] words)." This confirms the burstiness targets were met.

### Pass 2: Sentence structure diversification

**Mandatory for every rewrite: the first sentence of the rewrite must NOT open with a noun phrase as the subject.** Use one of these openers instead:
- Conjunction: "And that's the key distinction."
- Verb: "Consider what happens when..."
- Adverb: "Surprisingly, this rarely matters."
- Preposition: "For most writers, the issue is..."
- Fragment: "Not always."
- Question: "Why does this work?"

Then continue varying. No two consecutive sentences may open the same grammatical way.

Detectors pattern-match sentence openings. Variety disrupts that.

### Pass 3: Perplexity injection
Replace predictable phrases with unexpected-but-correct equivalents:
- Don't use the most obvious word — use the second-most-accurate one
- Use a specific reference where a general term would be expected: "Salesforce" instead of "CRM platforms"
- Use a concrete number where a vague claim would be expected: "six months" instead of "over time"
- Add a detail that requires actual knowledge: a person's name, a specific place, a real date

### Pass 4: Voice injection
Add first-person perspective, hedging (genuine, not AI-hedging), and self-correction:
- "I've seen this go wrong in exactly this way."
- "This is the part that trips most people up — including me, the first time."
- "Actually, scratch that. The better framing is..."
- Parenthetical asides: "(and I mean this literally)"
- Honest qualifications: "This works most of the time. It doesn't work when..."

### Pass 5: Structural disruption
- Remove all lists and convert to prose (lists are an AI signal)
- Break one long paragraph into one-sentence paragraphs
- Add a paragraph that tangentially relates before returning to the point
- End a paragraph mid-thought, then start the next one by completing it

### Mandatory Output Structure

Every deslop-detect response MUST end with this verification block after the rewrite:

```
## Detector Signal Verification

**Burstiness**
- Shortest sentence: "[sentence]" (N words) ✓/✗ target ≤5
- Longest sentence: "[sentence]" (N words) ✓/✗ target ≥35

**Sentence openings (first 3)**
1. [grammatical type: conjunction / verb / adverb / preposition / fragment / question / noun-SVO]
2. [grammatical type]
3. [grammatical type]
Variety: ✓ no two consecutive same type / ✗ [fix needed]

**Perplexity**
- Specific references injected: [list names/numbers/examples added]
- First sentence opener type: [type] — ✓ not SVO / ✗ still SVO

**Passes applied**: [list: burstiness / structure / perplexity / voice / structural-disruption]
```

Do not deliver the rewrite without this block.

## Anti-Pattern: Synonym Spinning

**Symptom**
Running the content through a paraphrasing tool or manually replacing words with synonyms. GPTZero score improves slightly; Originality.ai doesn't move.

**Problem**
Synonym swapping changes vocabulary but preserves sentence structure and token-sequence patterns. Detectors that look at structural features or trained classifiers (Originality.ai, Turnitin) see through this immediately. The statistical fingerprint of AI generation lives in the sentence frames and transitions, not the nouns and verbs.

**Solution**
Rewrite at the sentence level, not the word level. Change how sentences are constructed, not just what words appear in them.

## Anti-Pattern: AI-Generated "Humanization"

**Symptom**
Asking another AI model to "make this sound more human" or "rewrite this to evade AI detection."

**Problem**
AI models asked to humanize text tend to add AI-humanization patterns — they introduce the same phrases they've seen in training data labeled "human-sounding": "In my opinion," "I've been thinking about this a lot," "Let me be honest with you." These are now in detectors' training data too, and some detectors actively flag them as AI-humanization signals.

**Solution**
Human-written humanization only. The techniques in Pass 1–5 above must be applied by a human writer (or a human reviewing LLM suggestions one at a time). Batch AI humanization is self-defeating.

## Anti-Pattern: Single-Pass Fix

**Symptom**
Running the rewrite once, checking the detector, getting a passing score, publishing.

**Problem**
AI detectors update their models. A piece that passes GPTZero today may flag on Originality.ai tomorrow or on Turnitin's next model update. Detection is an arms race.

**Solution**
Run the content through at least two detectors with different underlying approaches (e.g., GPTZero + Originality.ai). If it passes both, it's structurally humanized, not just threshold-gaming. The techniques in this skill target structural signals, not thresholds, so they degrade more gracefully against model updates.

## Quick Checklist Before Publication

- [ ] Sentence length variance is high — runs of short and long sentences visible
- [ ] At least one sentence starts with And, But, or So
- [ ] At least one fragment or very short sentence (under 6 words)
- [ ] At least one sentence is 35+ words
- [ ] No two consecutive sentences open the same grammatical way
- [ ] No list-heavy sections (convert to prose where possible)
- [ ] At least one specific reference (name, number, date) per major claim
- [ ] At least one moment of first-person voice or direct opinion
- [ ] Checked on GPTZero and one classifier-based detector (Originality.ai or Turnitin)
