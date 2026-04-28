# Source Tiering

Not every source carries equal weight. A strict tier hierarchy lets you choose between competing sources fast, defend choices in editing, and signal credibility to careful readers.

## The six tiers

| Tier | Source type | Authority signal | Examples |
|---|---|---|---|
| **0 — Primary** | The thing itself | Direct observation | Source code, RFCs, ISO/W3C/IETF specifications, raw datasets, the API/system you're benchmarking, your own reproducible experiment |
| **1 — Peer-reviewed** | Published research with external review | Methodology survived scrutiny | ACM, IEEE, USENIX, Nature, peer-reviewed journals, well-reviewed conference proceedings |
| **2 — Authoritative practitioner** | Named expert with reputation at stake | Track record, accountability | Engineering blogs from companies (with named authors), individual experts with public track records, conference talks with archived video and Q&A |
| **3 — Quality popular** | Reputable publication, no peer review | Editorial standards, named editor | NYT/FT/The Atlantic/Wired technology coverage, well-known tech publications with editorial standards, books from major publishers |
| **4 — Anonymous popular** | No accountability | Low; aggregate signal at best | Reddit comments, anonymous blog posts, "I heard from someone…" |
| **5 — Vendor / advocacy** | Selling something | Negative — assume motivated reasoning | Vendor whitepapers, product blogs, sponsored content, influencer posts with disclosed/undisclosed sponsorship |

## Tier rules

### 1. Cite the highest tier available

If a Tier 4 blog post and a Tier 1 paper both make the same claim, cite the paper. The blog post may be how *you* learned the claim; the paper is how the *reader* will verify it.

### 2. Translate down

When citing Tier 0 or Tier 1, also link to a Tier 2/3 explainer if one exists. The reader can choose their depth.

```
[As specified in RFC 9110 § 7.3.2][rfc-9110-7-3-2] (or see [Adam Roach's
explainer of method-specific cacheability][roach-cache] for the practical
implications)…
```

The primary citation establishes authority; the secondary citation establishes accessibility. Together they serve both the careful reader and the casual reader.

### 3. Tier 5 is a last resort

Vendor sources can be cited as **"X claims Y"** but never as the sole source for a load-bearing claim. The asymmetry is built in: the vendor is the source *and* the subject. They have an interest in the claim being true.

Acceptable Tier 5 use:

- Quoting a vendor's official position on a controversy: "AWS's response to the outage acknowledged the BGP misconfiguration ([AWS post-mortem](https://...))."
- Documenting product behavior: "According to the Stripe API docs, idempotency keys expire after 24 hours."

Unacceptable Tier 5 use:

- "AWS is the most reliable cloud provider, with 99.999% uptime ([AWS status page](https://status.aws.amazon.com))."
- "Postgres outperforms MySQL on workload X ([Postgres benchmarks page](https://...))."

When the vendor is the entire source for a comparative or competitive claim, the claim has zero independent backing.

### 4. The independence test

When triangulating across tiers, check that sources are *actually* independent:

| Apparent sources | Real source count |
|---|---|
| Three blog posts that cite the same StackOverflow answer | 1 |
| A primary paper, an independent benchmark, and your own experiment | 3 |
| A vendor's docs, the vendor's blog, and the vendor's CEO's tweet | 1 |
| The original paper, three citing papers that confirm the result | 4 (the citing papers are independent confirmations *if* they ran their own experiments) |
| Five engineering blog posts that all cite the same Hacker News thread | 1 |

If five sources collapse to one when you check their citations, you have one source.

## Edge cases

### "Primary" is harder than it looks

For a programming language: the spec is primary; the reference implementation is also primary; a popular alternative implementation is Tier 1 or 2. They can disagree.

For a benchmark: the methodology paper is primary; the dataset is primary; rerunning the benchmark yourself is primary. Citing "MLPerf" without specifying version, hardware, and methodology is not really primary.

For a system in production: the source code is primary for what it *does*; the operations team's incident reports are primary for what it *did*; the marketing site is Tier 5.

### Pre-prints and arxiv

Pre-prints (arxiv, biorxiv, ssrn) are useful but not yet peer-reviewed. Treat them as Tier 2 — accountable (named authors, public track record) but not yet vetted. Note "(pre-print)" in the citation.

If a pre-print is later published in a peer-reviewed venue, switch to citing the published version.

### Conference talks vs conference papers

A talk with a published paper: cite both, prefer the paper for specific claims. The paper survives editing; the talk surfaces nuance.

A talk without a paper: Tier 2 if archived video exists and the speaker has a track record. Cite the timestamp.

A talk without video: not citable. The audience can't verify it. (Exception: notes from a private conference, used as a secondary source with disclosure.)

### Books

Major publisher books (O'Reilly, Manning, MIT Press, Pragmatic) are Tier 3. Self-published books are Tier 2 if the author has a track record, Tier 4 otherwise.

Books age fast for technical topics. A 2018 book about Kubernetes is potentially obsolete; cite version-and-date for time-sensitive claims, or pair with a current Tier 2 source.

### Interviews and personal communications

A direct interview with an expert is a primary source for what that expert thinks, but Tier 2 for whether they're correct. Quote them; don't treat their opinion as established fact.

Personal communications ("X told me Y in a call last month") are Tier 2 for the fact that X said Y, Tier 4 for whether Y is true. Get permission to cite by name; otherwise paraphrase as "an engineer at [company]" with a note that you've verified the claim.

## Examples by domain

### Benchmarks

```
Tier 0 — Primary: TechEmpower benchmark methodology + raw results
Tier 1 — Peer-reviewed: VLDB / SIGMOD performance papers
Tier 2 — Authoritative: A team's published benchmark with methodology
Tier 5 — Vendor: "X is faster than Y" without methodology, on the vendor's site
```

When a vendor publishes a benchmark, it's Tier 5 — even if the methodology looks rigorous. The selection of what to benchmark and how is the editorial choice that makes it advocacy.

### Security claims

```
Tier 0 — Primary: CVE database, exploit code, advisory from the affected project
Tier 1 — Peer-reviewed: USENIX Security, CCS, IEEE S&P papers
Tier 2 — Authoritative: Project Zero blog, Trail of Bits research, named individual researchers
Tier 3 — Quality popular: Krebs on Security, Bruce Schneier's blog
Tier 5 — Vendor: "We take security seriously" press releases
```

### Performance / latency

```
Tier 0 — Primary: Production telemetry from a system you have access to
Tier 1 — Peer-reviewed: SIGMETRICS, EuroSys papers
Tier 2 — Authoritative: Engineering blog posts with methodology and reproducible results
Tier 3 — Quality popular: HighScalability case studies (older but well-edited)
Tier 5 — Vendor: Sales-oriented "10x faster" claims
```

## Tier signaling in prose

Strong technical writing makes the source tier visible to the reader without naming the framework:

- **Tier 0:** "The TLS 1.3 specification (RFC 8446) defines…"
- **Tier 1:** "In a 2022 USENIX paper, Smith et al. showed…"
- **Tier 2:** "Cloudflare's engineering blog reports…"
- **Tier 3:** "According to Wired's investigation…"
- **Tier 5 (used carefully):** "MongoDB's marketing materials claim — though independent benchmarks show otherwise…"

The verb signals the relationship: *defines*, *showed*, *reports*, *claims*. Don't use *proves* unless you're citing Tier 0–1 with high confidence.

## When to cut the claim

If you can't find a Tier 0–2 source for a load-bearing claim:

1. **Run your own experiment** and become a Tier 0 source.
2. **Weaken the claim** to "anecdotally" with attribution to where you encountered it.
3. **Cut the claim.** This is often the right answer. A confident sentence backed by one Tier 4 source is worse than a missing sentence.

A claim is only as strong as its weakest source. If the source is bad, the claim is bad — no amount of confident prose fixes it.
