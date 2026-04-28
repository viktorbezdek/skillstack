# Citation Discipline

A citation is a contract: *I claim X, here is where you can check.* Citation discipline is the set of habits that makes the contract enforceable a year after publication.

## When to cite

Cite when:

- The claim is **load-bearing** — your argument depends on it.
- The claim is **comparative** — X is better/worse/faster/cheaper than Y.
- The claim is **statistical** — most/many/typically/N%.
- The claim is **causal** — X causes Y, or X led to Y.
- The claim is **non-obvious** — a careful reader would ask "is that true?"
- You're using someone else's framing, terminology, or chart.
- You're quoting directly.

Don't cite when:

- The claim is trivially true ("HTTP is a stateless protocol").
- The claim is your own experience ("we migrated to Postgres in 2023").
- The claim is established craft knowledge for the audience.
- You'd be decorating with citations to look authoritative — readers smell it.

## Inline vs footnote vs hybrid

Three approaches; pick by venue and reader:

### Inline links (most blogs, modern web articles)

```
The TypeScript team [introduced strict mode in 2.3](https://devblogs.microsoft.com/typescript/2017/04/27/announcing-typescript-2-3/),
making the strict family of flags opt-in via a single tsconfig setting.
```

**Pros:** Casual reader can ignore; deep reader can click; reads naturally.
**Cons:** No standalone reference list; broken links scatter through the article.

### Footnotes (long-form essays, academic-leaning publications)

```
The TypeScript team introduced strict mode in 2.3¹, making the strict family of flags opt-in
via a single tsconfig setting.

---
¹ Microsoft TypeScript Blog, "Announcing TypeScript 2.3," 27 April 2017,
   https://devblogs.microsoft.com/typescript/2017/04/27/announcing-typescript-2-3/
```

**Pros:** Centralized reference list; visually clean prose; allows extended notes.
**Cons:** More effort; overkill for casual articles.

### Hybrid (recommended for technical deep-dives)

Inline link for the casual reader; footnote for the careful reader; both for load-bearing claims.

```
The TypeScript team [introduced strict mode in 2.3][ts-2-3], making the strict family of flags
opt-in via a single tsconfig setting.[^1]

[ts-2-3]: https://devblogs.microsoft.com/typescript/2017/04/27/announcing-typescript-2-3/

[^1]: This conflicts with some early documentation that suggests strict mode was added later;
      see TypeScript GitHub issue #18643 for the timeline.
```

The footnote here adds nuance without breaking the prose. The inline link serves the click-and-go reader.

## Citation formats

### Web articles / blog posts

```
[Author Name. "Title." Publication, Date. URL]
```

Example:
```
Adam Wathan. "Why I'm Skeptical of Atomic CSS." Adam Wathan's blog, 18 March 2017.
https://adamwathan.me/css-utility-classes-and-separation-of-concerns/
```

### Specifications

```
[RFC NNNN, Section X.Y, "Title."]
```

Example:
```
RFC 9110, Section 9.3.2, "Method Definitions: GET."
https://www.rfc-editor.org/rfc/rfc9110#section-9.3.2
```

Cite the specific section, not the whole RFC. "See RFC 9110" is too broad.

### Academic papers

```
[Author1, Author2, et al. "Title." Venue, Year. DOI/URL]
```

Example:
```
Smith, J., Liu, K., et al. "Concurrency Control Mechanisms in Modern OLTP Systems."
Proceedings of VLDB 2022. https://doi.org/10.14778/example
```

Always prefer the DOI when available — DOIs are stable identifiers, URLs change.

### Source code

```
[project/file.ext at commit-hash, line range]
```

Example:
```
postgres/src/backend/access/heap/heapam.c at commit a1b2c3d, lines 1234-1289.
https://github.com/postgres/postgres/blob/a1b2c3d/src/backend/access/heap/heapam.c#L1234-L1289
```

The commit hash matters. Linking to `master`/`main` is fine for "current state" but the file may not exist or may have changed when the reader clicks.

### Versioned software docs

```
[Project Name documentation, Version X.Y, "Section." URL]
```

Example:
```
PostgreSQL 16 documentation, "Row Security Policies."
https://www.postgresql.org/docs/16/ddl-rowsecurity.html
```

Always include the version number — docs change between versions, and a "/current/" link will silently update.

### Personal communications

```
[Person, role/affiliation, communication type, date]
```

Example:
```
Conversation with Jane Doe, Staff Engineer at Acme Corp, March 2024.
```

If quoting: get explicit permission to quote and cite by name. Otherwise, paraphrase as "an engineer at Acme Corp confirmed…" with a note about your verification process.

## Link-rot mitigation

Link rot is a research problem and a credibility problem. Two-thirds of links in academic papers break within ten years; tech blog posts decay faster. Citations that no longer resolve undermine the article's authority *years after publication*, when the author is no longer paying attention.

### Capture everything to archive.org while researching

When you find a useful source, save it immediately:

```bash
# CLI tool, install via pip install internetarchive
ia upload --metadata=collection:web https://example.com/page

# Or use the web form: https://web.archive.org/save
```

Or use a headless workflow during research:

```bash
# Save URL to wayback machine
curl -X POST "https://web.archive.org/save/https://example.com/page"
```

The cost is seconds. The benefit is that your citation survives the source disappearing.

### Provide both URLs in the citation

```
[Adam Roach. "HTTP Method Cacheability." Mnot's Blog, 2018.
 https://www.mnot.net/blog/2018/05/30/http-method-cacheability
 (archived: https://web.archive.org/web/20240101000000/https://www.mnot.net/blog/2018/05/30/http-method-cacheability)]
```

The original link first; the archive link as fallback. When the original 404s, the archive resolves.

### Prefer stable identifiers

In order of preference:

1. **DOI** — designed to outlive the URL.
2. **Permalinks** — `/permalink/abc123` rather than `/blog/2024/01/05/title-with-slug-that-may-change`.
3. **Archive.org URLs** — point to a fixed snapshot.
4. **Hash-pinned source code** — `github.com/.../blob/<commit>/...`, not `.../blob/main/...`.
5. **Versioned docs** — `/v1.5/...`, not `/latest/...`.

Mutable URLs (`/main/`, `/latest/`, `/current/`) silently break citations as content evolves. Pin everything.

## Quote discipline

Quoting introduces extra obligations:

### 1. Quote with surrounding context

A quote that says X in your article and Y in the original is research malpractice.

```
✗ Bad:
"The author concedes that 'strict mode adds compilation time.'"

✓ Better:
"The author writes: 'Yes, strict mode adds compilation time — typically 5-10% on our codebase —
but the type-error catches paid back the time within two weeks of running the migration.'"
```

The "bad" version inverts the meaning. The "better" version preserves the author's actual position.

### 2. Use ellipsis sparingly and honestly

```
✓ "X led to performance gains... eventually."
```

If the omitted text contains a qualification that changes the meaning, restore it. Ellipsis is not a tool for fixing inconvenient phrasing.

### 3. Mark added emphasis

```
"The migration was painful but worth it" (emphasis added).
```

Don't bold parts of someone else's quote without disclosing.

### 4. Mark edits

```
"[The migration] was painful but worth it."
```

Square brackets disclose your edits to the quoted material. Use them to clarify references; don't use them to change meaning.

### 5. Get permission for personal communications

Quoting an email, DM, or private conversation requires permission unless the source is a public figure speaking in their public capacity. Default to asking.

## Dating sources

Software claims age. A 2018 article about Kubernetes networking may not describe 2024 Kubernetes networking. A 2020 benchmark may not reflect 2024 hardware.

### Always include the date

```
✓ "As of PostgreSQL 16 (2023)..."
✓ "In 2022, GitHub reported..."

✗ "PostgreSQL supports..."  (which version?)
✗ "GitHub reports..."        (when?)
```

### Note staleness explicitly

If you're citing a source older than ~2 years for a fast-moving topic, either:

- Spot-check that the claim is still true.
- Note the staleness ("This data is from 2021; the landscape has shifted with the introduction of X").
- Cut and find a current source.

### Update before republishing

When refreshing or republishing an article, re-check date-sensitive citations. The article is your name, even when the underlying world changes.

## Citation as voice

Citation patterns signal voice. A piece with dense Tier 0–1 citations reads as academic; a piece with mostly inline blog-post citations reads as conversational; a piece with no citations reads as opinion (and should be framed as such).

Match citation density to the genre:

| Genre | Citation density | Format |
|---|---|---|
| Personal essay / opinion | Sparse | Inline links |
| Tutorial | Light | Inline links to docs |
| Deep-dive / explainer | Medium-heavy | Inline + occasional footnotes |
| Investigation / report | Heavy | Footnotes, methodology section |
| Whitepaper / academic | Very heavy | Footnotes + reference list |

A tutorial cluttered with academic footnotes feels heavy. A whitepaper with only inline blog-post links feels weak. The format is part of the genre signal.

## The audit pass

Before publishing, do a citation audit:

1. **Every link resolves.** Click each one.
2. **Every citation is captured to archive.org.**
3. **Every load-bearing claim has a Tier 0–2 citation.**
4. **Every direct quote matches the original** (open the original, search for the quoted text).
5. **Every date is included** for time-sensitive claims.
6. **Every version number is current** for software-version-sensitive claims.

This pass takes 15–30 minutes. It catches the embarrassments before publication.

## When you can't find a citation

If you've exhausted triangulation and a load-bearing claim has no Tier 0–2 source:

1. **Run an experiment** — become the source.
2. **Weaken the claim** — "anecdotally," "in some cases," "limited evidence suggests."
3. **Reframe as an open question** — "It's not clear whether…" can be honest and interesting.
4. **Cut the claim.**

Don't bluff. The cost of a confident sentence backed by nothing is the entire article's credibility.
