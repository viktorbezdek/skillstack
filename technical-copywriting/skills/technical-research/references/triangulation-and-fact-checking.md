# Triangulation & Fact-Checking

A load-bearing claim — one your argument depends on — needs three independent sources before you cite it with confidence. The discipline costs time. The alternative is publishing things that turn out to be wrong.

## What "triangulation" means

Triangulation is finding three *independent* confirmations of a claim. The three sources should:

1. Have arrived at the claim through different paths (different methods, different data, different reasoning).
2. Have something at stake if they're wrong (named author, institutional reputation, peer-reviewed publication).
3. Not derive the claim from each other.

When all three agree, the claim is robust. When they disagree, you've discovered a controversy worth surfacing — not a fact worth asserting.

## What counts as a "load-bearing claim"

Not every sentence needs three sources. Triangulate the claims your argument *depends on*. If a claim were wrong, would the article still hold up?

| Claim | Load-bearing? | Why |
|---|---|---|
| "Postgres uses MVCC for concurrency control" | No | Trivially true, well-documented in primary source |
| "Postgres MVCC has lower contention than MySQL InnoDB for workload X" | **Yes** | Comparative performance claim; one source could be wrong |
| "Most production Rails apps use Postgres" | **Yes** | Statistical claim about a population |
| "We migrated to Postgres in 2023" | No | Author's own experience; cite it as such |
| "Migration took 4 months" | No (for author's own migration) | Personal experience |
| "Migrations of similar scale typically take 3-6 months" | **Yes** | Generalization across cases |

Rule of thumb: if the claim is **comparative** (X is better than Y), **statistical** (most/many/typically), or **causal** (X causes Y), it's load-bearing.

## The independence test

Apparent multiple sources frequently collapse to a single source on inspection. Run this test:

1. **Trace each source's origin.** Where did the source learn this claim?
2. **Map the citation graph.** Do the sources cite each other? Cite the same upstream source?
3. **Check for shared methodology.** If three benchmarks use the same dataset, they have one data source.

| Apparent | Real | Why |
|---|---|---|
| Five blog posts citing the same StackOverflow answer | 1 | The SO answer is the actual source |
| Two papers, both reanalyzing the same dataset | 1 (data) + 2 (interpretations) | Data is the single point of failure |
| Vendor's docs + vendor's blog + vendor's CEO tweet | 1 (the vendor) | All three reflect the vendor's view |
| Three independent benchmarks of the same library on different hardware | 3 | Different methodology, different results |
| Original paper + three independent reproductions | 4 | Each reproduction is independent confirmation |
| Original paper + three citing papers that don't reproduce | 1 (with secondary support) | Citing isn't reproducing |

## The triangulation worksheet

For each load-bearing claim, fill out:

```
Claim: [exact wording]
Source 1: [tier, citation, what it says, methodology]
Source 2: [tier, citation, what it says, methodology]
Source 3: [tier, citation, what it says, methodology]

Independence check:
- Different methodologies? [Y/N — explain]
- Different data sources? [Y/N — explain]
- No citation chains between them? [Y/N — explain]

Disagreement?
- All three agree? → cite confidently
- Two agree, one disagrees? → cite with caveat ("most evidence suggests… though [source 3] disputes this")
- All three disagree? → reframe as controversy, don't pick a side
```

## Worked example: triangulating a performance claim

**Claim:** "TypeScript strict mode adds 15-25% to compilation time on large codebases."

### Triangulation attempt 1 (fails)

- Source 1: A blog post citing "around 20%" with no methodology
- Source 2: A Hacker News comment from someone who "saw 25% on our codebase"
- Source 3: A tweet from a TS contributor mentioning "noticeable but worth it"

**Independence:** All three are anecdotal. None publish a methodology. Independence is high (different authors), but quality is uniformly low.

**Verdict:** This is one tier of evidence (anecdote) repeated three times. Not robust enough for a load-bearing claim. Either cut, weaken, or run your own benchmark.

### Triangulation attempt 2 (succeeds)

- Source 1: A reproducible benchmark on a 500k-line codebase published by an engineering team, with `tsc --diagnostics` output and methodology
- Source 2: A `tsc --extendedDiagnostics` comparison on the TypeScript repo's own benchmark suite (Tier 0 — the project's own measurement)
- Source 3: Your own measurement on a 200k-line codebase you have access to

**Independence:** Three different codebases, three different measurement methods, no shared data. All measure the same dimension.

**Verdict:** Robust enough to claim. Add the citations, note the range and that it varies with codebase characteristics, and move on.

## When sources disagree

Disagreement is information. When two sources you trust contradict each other:

### 1. Surface the disagreement instead of picking

Don't suppress one source to keep the prose clean. The article that says "X is true" while the citations conflict invites a "well actually" in the comments. The article that says "X is true according to A and B; C reports otherwise, possibly due to [methodology difference]" earns trust.

### 2. Diagnose the disagreement

Sources disagree for predictable reasons:

| Reason | Diagnostic |
|---|---|
| Different methodology | Compare the methodologies; explain the discrepancy |
| Different time period | Note the dates; the world may have changed |
| Different scope (e.g., different languages, hardware) | Note the scope difference |
| Vendor vs independent measurement | Tier-5 vendor source likely overstates; weight independents |
| Newer source vs older | Default to newer unless newer is Tier 4-5 |

### 3. If you can't diagnose, weaken the claim

"The picture is mixed: X reports 20%, Y reports 5%, the difference may stem from [hypothesis]" is honest. Don't pretend the literature is clearer than it is.

## Fact-checking your draft

After drafting, do a fact-check pass on the load-bearing claims:

1. **Highlight every load-bearing claim** in the draft.
2. **For each, check the citation actually supports it.** Read the cited source. Does it say what you said it says, in context?
3. **Check the numbers.** Re-derive any computed numbers. Spot-check direct quotes against the original.
4. **Check the dates.** Is the cited source still current? (Software claims age; statistical claims may need refreshing.)
5. **Check the links.** Do they resolve? Capture them to archive.org if you haven't already.
6. **Check the names and affiliations.** Are people named correctly? Are titles current?

This pass takes 30–60 minutes per article. It catches the embarrassments before publication.

## Common fact-checking failures

### Quote-mining

A quote that says X in your article and Y in the original is a research failure. It's also a credibility failure that compounds: readers who notice one mined quote distrust every other quote in the article.

**Fix:** Always quote with surrounding context. Read the original; if your quote misrepresents the original's overall position, either include the surrounding context or don't quote.

### Outdated benchmarks

A 2019 benchmark of a 2024 system isn't a benchmark of the 2024 system. Software changes; the original measurement may not still hold.

**Fix:** Cite version-and-date. If the cited measurement is more than ~18 months old for software performance claims, run a current spot-check or note the staleness.

### Number drift

You said "80% of developers" because you read "most developers" and rounded confidently. Or you cited a study that surveyed 200 developers and presented the result as "developers" globally.

**Fix:** Cite the exact number when possible ("a 2023 Stack Overflow Developer Survey of 89,000 respondents reported 67% use…"). When generalizing, signal it ("among the engineers surveyed").

### Phantom sources

A claim citing "industry research" or "studies show" with no link is, functionally, no citation. The reader can't verify; you may have pulled it from memory or from another article that pulled it from another article.

**Fix:** Either link to a specific source or remove the claim. "Studies show" without a study is a verbal tic, not a citation.

### Stale links

Half of all links break within five years (search "link rot research"). A two-year-old article with broken citations reads as careless even if it was rigorous at the time.

**Fix:** Capture every cited URL to archive.org while researching. Use the archive URL as a backup citation.

## When you become the source

Sometimes the best response to "I can't find three sources for this claim" is to *become* one of the sources by running your own experiment.

This is the most authoritative move available — but it imposes new obligations:

- **Methodology.** Document the setup so someone else could reproduce.
- **Data.** Make the raw data available where possible.
- **Disclosure.** Note your stake in the outcome (your codebase, your hardware, your assumptions).
- **Limits.** Be explicit about what your experiment doesn't show.

A piece that runs its own benchmark with rigor becomes a citable source for future articles. That's a much stronger position than triangulating across three weak existing sources.

## The escalation ladder

When triangulation doesn't yield three solid sources, escalate in order:

1. **Search harder.** Add field-specific search terms; check primary literature; check non-English sources; check specialized databases (ACM DL, IEEE Xplore).
2. **Ask an expert.** A direct interview with a named expert is itself a primary source.
3. **Run your own experiment.** Become the third source.
4. **Weaken the claim.** "Anecdotally," "in some cases," "the limited evidence suggests."
5. **Cut the claim.** Sometimes the right answer.

Don't skip rungs. Going from "couldn't find a third source" to "stating it confidently anyway" is the most common research failure in technical articles.
