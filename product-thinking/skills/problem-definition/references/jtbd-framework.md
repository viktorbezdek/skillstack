# Jobs-To-Be-Done Framework

Jobs-To-Be-Done (JTBD) reframes products as tools users "hire" to get a job done in a specific context. The framework separates the job from the solution so teams stop building features for wants and start building for the underlying job.

## The core claim

A customer is not buying a drill — they are hiring a drill to make a quarter-inch hole. If a better way to make the hole arrives (a laser, a hydraulic press, a pre-drilled board), the drill loses the job. Competitors are not whoever makes similar products — they are whoever else can do the job.

## The three job dimensions

Every job has three dimensions. Most teams elicit the first and miss the other two.

### Functional

What the user is literally trying to get done. Observable, measurable.

| Context | Functional job |
|---|---|
| Deploying a service | Push a new version to production without breaking running traffic |
| Onboarding a new hire | Give them a working environment by end of day one |
| Reviewing a PR | Decide whether the change is safe to merge |

### Emotional

How the user wants to feel — or avoid feeling — while doing the job.

| Functional job | Emotional job |
|---|---|
| Deploy a service | Not feel like I am about to cause an outage |
| Submit expense report | Not feel surveilled or distrusted |
| Ask for help in Slack | Not feel stupid for not knowing |

Emotional jobs explain why two tools with identical feature sets have radically different adoption.

### Social

How the user wants to be perceived by others while doing the job.

| Context | Social job |
|---|---|
| Choose an IDE | Signal that I take my craft seriously |
| File a bug | Not look like the person who broke it |
| Post a status update | Appear to be adding value to my manager |

Social jobs drive purchase decisions in organizations far more than teams admit — especially for tools with visible outputs (IDEs, design tools, dashboards).

## Job hierarchy

Jobs exist at multiple altitudes. Confusing altitudes produces a problem statement that feels off.

| Altitude | Example (for an engineer) |
|---|---|
| Big job | Ship reliable software |
| Little job | Deploy a service |
| Micro-job | Rollback if deploy fails |

A product that solves a micro-job but ignores the little job is useful but not loved. A product that claims to solve a big job but only solves one little job is overclaiming.

Pick the altitude that matches your product's scope. Solving the big job is ambitious; solving a specific little job well is often more valuable.

## Job interview prompts

Questions that elicit jobs, not solutions:

- "Walk me through the last time you [did the task]. What triggered it?"
- "What were you trying to accomplish?"
- "What did you do before you used any product for this?"
- "If the product disappeared tomorrow, what would you do instead?"
- "What would 'success' look like for this task?"
- "What would you want to feel while doing this task? What would you want to avoid feeling?"
- "Who sees you doing this? Does that change how you do it?"

Avoid:

- "Would you like a feature that…?" (invites speculation)
- "Do you like our product?" (invites validation theater)
- "What would make our product better?" (invites feature requests disguised as needs)

## The job-to-product map

Once jobs are elicited, map them to product surface area.

```
JOB                                      | PRODUCT SURFACE        | EVIDENCE
-----------------------------------------+------------------------+---------
Know at a glance that production is OK   | Status dashboard       | Session replay
Verify no one burned things down last    | Overnight alert digest | Login times
  night
Triage issues before standup             | Priority-sorted queue  | Task frequency
```

Each job should map to at least one surface area, and each surface area should serve at least one job. Orphans on either side are opportunities to cut scope.

## Common JTBD mistakes

- **Conflating a feature with a job** — "users want notifications" is a feature. The job is "know when X happens without having to check."
- **Collecting only functional jobs** — the interview surfaces functional jobs easily; the team stops there and misses the emotional and social drivers.
- **Job-as-demographic** — "the job is to be a mid-market sales rep" confuses who the user is with what they are trying to do.
- **Ignoring the trigger** — a job without a context/trigger cannot be designed for. The trigger is when the job arises; without it, you can't design for the moment of need.
- **Timeless jobs** — a job without a frequency is hard to prioritize. If the job arises once a quarter, the solution doesn't need to be central to the product.

## When to use JTBD vs personas

Personas describe who the user is (demographics, role, goals). JTBD describes what they are trying to get done. Use both:

- Persona answers: **who** is the user?
- JTBD answers: **what** job are they hiring the product for, and **in what context**?

The two are complementary. A good product discovery has both.
