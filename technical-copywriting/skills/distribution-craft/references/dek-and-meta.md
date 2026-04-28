# Dek and Meta Description

The title earns the click; the dek and meta description determine *how confident* the click feels. Get them right and the reader commits to the body; get them wrong and the reader bounces before paragraph two.

## The dek

The dek (also called the standfirst, deck, subtitle, or hairline) is the second sentence the reader reads, immediately under the title. Its job:

- Confirm the title's promise.
- Add specificity the title couldn't carry.
- Earn the read.

### Dek formulas

#### Restate + specify

The dek restates the title's claim and specifies what the article will deliver.

```
Title: "Why TDD doesn't work for the median team"
Dek:   "TDD pays off at scale; for teams of 5-15 it usually adds cost without proportional
        benefit. A look at why, and what works instead."
```

The title makes a claim; the dek scopes the claim and previews the alternative.

#### Promise + scope

The dek details what the article covers.

```
Title: "The Postgres setting that's eating 30% of your disk"
Dek:   "How dead tuples accumulate, why VACUUM can't always clean them up, and the 6-line
        alert that catches the problem before you run out of space."
```

Three concrete previews of what's inside. Reader commits because they see the substance.

#### Story setup

For narrative-driven pieces, the dek extends the in-medias-res into a hook.

```
Title: "How we deleted 47 microservices in one quarter"
Dek:   "We had a distributed monolith pretending to be microservices. Here's how we noticed,
        what we cut, and what we kept."
```

#### Expectation set

For tutorials and reference-shape pieces, the dek tells the reader what they're signing up for.

```
Title: "The 5-minute Postgres health check"
Dek:   "A six-query script you can run on any database to find the most common operational
        problems. Designed for teams without a dedicated DBA."
```

Sets time investment, audience, and concrete output.

#### Counter-position preview

For opinion pieces, the dek often signals the contrarian move and the steel-manned alternative.

```
Title: "Microservices were a mistake for most teams"
Dek:   "Independent deployments, polyglot, scale-to-team-size — the case is real for the
        right context. For median teams (under 50 engineers), the distributed-systems cost
        dominates. The case for the modular monolith."
```

### Dek length

| Length | Effect |
|---|---|
| 15-25 words | Tight; works for direct titles |
| **25-50 words** | The safe band |
| 50-80 words | Acceptable for deep-dives or whitepapers; risks competing with body |
| 80+ words | Too long; reads as introduction, not dek |

### Dek anti-patterns

#### The repeat

```
Title: "Why TDD doesn't work for the median team"
Dek:   "Test-driven development doesn't work for the median team because…"
```

Wastes the dek. The reader who clicked the title is reading the same content again.

**Fix:** the dek extends, doesn't repeat.

#### The hype

```
Dek: "An incredible deep dive into the world of database performance optimization that will
      transform how you think about Postgres forever."
```

Adjective inflation tells the reader to discount.

**Fix:** specifics over adjectives. "Why VACUUM can't run during long transactions, and the alert that catches it" beats "incredible deep dive."

#### The over-promise

```
Dek: "Everything you need to know about Postgres MVCC, VACUUM, autovacuum, dead tuples, page
      visibility, and the entire heap storage engine."
```

Over-promises in the dek erode trust. If the article is actually scoped to one thing, scope the dek to that thing.

**Fix:** match the dek to what the article actually delivers. "How dead tuples accumulate and what VACUUM can't always clean up" beats "everything about MVCC."

#### The vague gesture

```
Dek: "Some thoughts on database performance, with a focus on common issues and best practices."
```

Tells the reader nothing specific. They have no reason to commit.

**Fix:** name a specific finding, scope, or claim. "How dead tuples accumulate to 30%+ in healthy-looking databases" tells them what they'll learn.

#### The dek-as-author-bio

```
Dek: "I've been a DBA for 15 years and I've seen a lot of databases."
```

Self-introduction is for the about page, not the dek. The dek's job is to extend the article's promise.

**Fix:** tell the reader what *the article* offers; save bio for elsewhere.

## Meta description (and SEO snippets)

The meta description appears in search results and most social previews. Often 150-160 characters.

### Meta description formula

```
[Article promise in one sentence], [specific differentiator or detail].
```

### Worked examples

```
Article: "How we deleted 47 microservices in one quarter"
Meta:    "We had a distributed monolith pretending to be microservices. How we identified
          which services to merge, what failed, and what we'd do differently."

(159 characters)
```

```
Article: "The Postgres setting that's eating 30% of your disk"
Meta:    "How dead tuples accumulate in Postgres, why VACUUM can't always clean them up, and
          the 6-line alert that catches it before you run out of disk space."

(158 characters)
```

```
Article: "Why TDD doesn't work for the median team"
Meta:    "TDD pays off at scale; for teams of 5-15 it usually adds cost without proportional
          benefit. The case, and what works instead."

(140 characters)
```

### Meta description rules

- **Around 150-160 characters.** Google truncates at varying widths; under 160 is safe.
- **Include the article's promise.** Don't waste characters on filler.
- **Front-load specifics.** First 100 characters do most of the work.
- **Don't repeat the title verbatim.** SERPs show both; repetition wastes the snippet.
- **Avoid ALL CAPS or hype.** Reads as marketing; lowers click-through.

### Meta vs dek

The meta description and dek serve similar purposes but for different surfaces:

| Element | Surface | Length |
|---|---|---|
| Dek | On the article page | 25-50 words (~150-300 chars) |
| Meta description | SERP, social preview | 150-160 chars |

Often the dek is a longer version of the meta description. Both should carry the article's promise; the dek can elaborate where the meta must be tight.

## Open-graph metadata

Open Graph (OG) tags control how the article appears when shared on social platforms. The four that matter most:

```html
<meta property="og:title" content="The Postgres setting that's eating 30% of your disk" />
<meta property="og:description" content="How dead tuples accumulate, why VACUUM can't always..." />
<meta property="og:image" content="https://example.com/article-image.png" />
<meta property="og:url" content="https://example.com/post-url" />
```

### og:title

Usually the article title. Sometimes shortened or rewritten if the original title is too long for social previews.

### og:description

Usually the meta description or a slight variant. Same rules apply.

### og:image

The image shown in the social preview. Two patterns:

1. **The title rendered well.** Clean typography, brand-consistent color. Works when the title carries the substance.
2. **A graphic or chart from the article.** Works when the article has a memorable visual.

Avoid:
- Stock photos. They tell the reader the content is generic before they read.
- Logos alone. Tells the reader who published, not what the article is.
- Text-heavy designs. Can become unreadable in small previews.

### og:image dimensions

Most platforms render OG images at 1200×630 pixels. Below that, images get scaled up and look fuzzy. Above, they get cropped.

### og:image as the dek

A common pattern: the OG image *is* the dek, rendered as an image. The reader scanning a feed sees the image (which carries the promise) and the title (which carries the hook). Clicking is a synthesis of both.

This works especially well for X/Twitter and LinkedIn previews.

## Schema.org / JSON-LD

For SEO, articles often include structured data:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Postgres setting that's eating 30% of your disk",
  "description": "How dead tuples accumulate, why VACUUM can't always...",
  "datePublished": "2024-03-15",
  "author": {
    "@type": "Person",
    "name": "Jane Doe"
  }
}
</script>
```

Most platforms generate this automatically; manual editing is rarely needed. The fields that matter most: `headline`, `description`, `datePublished`, `author`.

## The dek + title + meta package

These three elements work together. Test them as a unit.

### Audit checklist

- [ ] Does the title hook with curiosity?
- [ ] Does the dek confirm the title and add specifics?
- [ ] Does the meta description carry the promise into search?
- [ ] Are the three consistent? (Same article, same promise.)
- [ ] Are they each appropriate for their surface?
- [ ] Does the OG image extend or replace the visual hook?

### Worked package

```
Title:           "The Postgres setting that's eating 30% of your disk"
Dek:             "How dead tuples accumulate in Postgres, why VACUUM can't always clean them
                  up, and the 6-line alert that catches the problem before you run out of disk
                  space."
Meta:            "How dead tuples accumulate in Postgres, why VACUUM can't always clean them
                  up, and the 6-line alert that catches it before you run out of disk."
OG image:        Title rendered with a Postgres-themed background graphic; dek as a smaller
                 line beneath.
```

The four elements together: title hooks, dek extends, meta carries to search, OG image carries to social. Each surface gets the right slice.

## Common failure modes

### The title is honest, the dek over-promises

```
Title: "Why VACUUM blocks during long transactions"
Dek:   "Discover the SECRETS of database performance that THE EXPERTS don't want you to know!"
```

Title is tight; dek undermines it. Reader trust drops.

**Fix:** dek matches title's energy and honesty.

### The title and dek are inconsistent

```
Title: "Why TDD doesn't work for the median team"
Dek:   "A look at the benefits and tradeoffs of test-driven development across team sizes."
```

Title commits; dek backs off. Reader senses the writer hedged after writing the title.

**Fix:** commit consistently. If the title's claim isn't defensible, change the title.

### Meta description is auto-generated and weak

Many platforms auto-generate the meta description from the article's first paragraph. If your first paragraph is hook-style ("In today's fast-paced…"), your meta description is throw-away.

**Fix:** explicitly set the meta description. Don't rely on auto-extraction for high-stakes pieces.

### OG image is missing or generic

The article shows up on social with no preview image, or with the site's default logo. Social engagement drops dramatically (preview-image presence boosts click-through 2-3x).

**Fix:** every published article gets a custom or template-rendered OG image.

### Multiple OG images for the same article

The OG cache on different platforms (Twitter, Facebook, LinkedIn) cache differently. If you change the OG image after publishing, some viewers see the old image.

**Fix:** set OG metadata correctly *before* the first share. If you must update, use platform-specific cache-bust tools (Twitter Card Validator, Facebook Sharing Debugger).

## Channel-specific tweaks

| Channel | Surface | Optimize for |
|---|---|---|
| Search results | Title + meta | Specific keywords + clear promise |
| X / Twitter | OG title + image | Curiosity-led title; image carries the promise |
| LinkedIn | OG title + dek | Professional framing; dek does heavy lifting |
| Hacker News | Title only (no preview image) | Honest, specific title |
| RSS readers | Title + dek | Both visible; dek confirms |
| Email newsletters | Subject + preview text | Subject = title compressed; preview = dek compressed |

The same article can have different OG metadata for different channels (some platforms support per-channel overrides), but most use the same OG tags everywhere.

## When the dek is the title

Some platforms (notably some newsletters and email-first publications) treat the subject line as both title and meta. In that case, the title-craft work has to do double duty.

Example: a newsletter's subject line is the article's title and the inbox preview is the article's dek. Both have to work in tight space.

## The compounding pattern

Like every other element of distribution craft, dek and meta improvement compounds:

- Articles with strong deks get more reads.
- Articles with strong meta descriptions get more search clicks.
- Search clicks compound (Google rewards higher CTR with higher rankings).
- Social clicks compound (each share generates more shares).

Spending 15 minutes on title + dek + meta package per article is one of the highest-ROI moves in technical content.
