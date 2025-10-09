# Decision-Making Frameworks

## Multi-Criteria Analysis

### Weighted Scoring
Quantify qualitative factors.
1. List decision criteria
2. Assign weights (sum to 100%)
3. Score each option (1-10) per criterion
4. Calculate weighted scores
5. Compare totals

Watch for: Hidden assumptions in weights, non-linear relationships

### Decision Matrix
Compare options across criteria.
- Rows: Options
- Columns: Criteria
- Cells: Ratings
- Visual pattern recognition
- Identify dominance (option better on all criteria)

### Pugh Matrix
Compare to baseline/reference.
- Choose reference option
- Rate others as +, 0, - relative to reference
- Sum positives and negatives
- Iterative refinement

## Optimization Approaches

### Pareto Optimization
Find non-dominated solutions.
- Can't improve one objective without worsening another
- Pareto frontier = all non-dominated options
- Choose based on preferences along frontier

### Satisficing
Good enough > optimal.
- Define minimum acceptable thresholds
- First option meeting all thresholds wins
- Saves analysis time
- When: Cost of optimization > benefit of marginal improvement

### Local vs. Global Optima
Avoid local peaks.
- Hill climbing finds local peak
- May need to go down to go higher
- Random restarts, simulated annealing
- Question: "Could a very different approach work better?"

### Multi-Objective Optimization
Handle trade-offs explicitly.
- No single "best" - depends on priorities
- Scalarization: Combine into single score
- Epsilon-constraint: Optimize one subject to others
- Interactive: Explore trade-off space

## Risk Analysis

### Expected Value Calculation
Probabilistic cost-benefit.
- EV = Σ(probability × payoff)
- Include all possible outcomes
- Discount for time value
- Sensitivity analysis on probabilities

### Decision Trees
Map choices and chance events.
- Square nodes: Decisions
- Circle nodes: Chance events
- Branches: Options/outcomes with probabilities
- Fold back from end to find optimal path
- Calculate expected values at each node

### Monte Carlo Simulation
Model uncertainty distribution.
- Define probability distributions for variables
- Run thousands of simulations
- Analyze result distribution (mean, variance, tails)
- Identify key risk drivers

### Scenario Planning
Prepare for multiple futures.
- Define key uncertainties
- Create 3-4 distinct scenarios
- Strategy robust across scenarios
- Signposts: Early indicators of which scenario emerging

## Timing & Optionality

### Real Options Analysis
Value of flexibility.
- Option to expand, contract, abandon, defer
- Uncertainty has value (not just cost)
- Don't commit prematurely
- Invest to keep options open

### Reversibility Test
Distinguish one-way from two-way doors.
- **Two-way**: Easy to reverse → Decide fast, test
- **One-way**: Hard to reverse → Analyze deeply
- Most decisions are two-way (vs. our bias)

### Timing Value
When to decide?
- **Value of waiting**: Information, flexibility
- **Cost of waiting**: Missed opportunities, competition
- Optimal timing: When VoW = CoW

### Sequential Decision Making
Break into stages.
- Don't decide everything now
- Commit to next step only
- Gather information
- Reassess at each stage
- Avoid sunk cost fallacy

## Heuristics & Mental Models

### Regret Minimization
10-10-10 rule: How will I feel about this in 10 minutes, 10 months, 10 years?
- Short-term pain, long-term gain decisions
- Overcome present bias
- "Will I regret not trying?"

### Opportunity Cost
What are you giving up?
- Not just money: Time, attention, alternatives
- Real cost = next best alternative
- "By doing X, I cannot do Y"
- Make trade-offs explicit

### Outside View
Base rates over inside view.
- How long do projects like this usually take?
- What's the success rate for similar endeavors?
- Am I special? (Usually no)
- Combat planning fallacy

### Pre-commitment
Remove future temptation.
- Ulysses contracts: Tie yourself to mast
- Change defaults
- Automate correct behavior
- Reduce activation energy for good, increase for bad

### Kill Criteria
Conditions for stopping/pivoting.
- Define failure conditions upfront
- If X happens, we stop/change
- Prevents sunk cost fallacy
- Psychological permission to quit

## Bias Mitigation

### Red Team / Blue Team
Adversarial analysis.
- Blue: Propose plan
- Red: Attack it
- Uncover vulnerabilities
- Strengthen before execution

### Steel Man
Argue strongest version of alternative.
- Opposite of straw man
- Find legitimate counterarguments
- Identify genuine weaknesses
- Build mutual understanding

### Devil's Advocate
Formal disagreement role.
- Assign someone to argue against
- Legitimizes dissent
- Surfaces groupthink
- Must be genuine, not pro forma

### Consider the Opposite
Force contrary perspective.
- "What if I'm wrong?"
- "What would prove this false?"
- "Why might the opposite be true?"
- Confirmation bias antidote

### Prospective Hindsight
"Looking back, we failed because..."
- Easier to generate reasons than predict
- Uncovers hidden assumptions
- 30% more problems identified vs. prospective analysis

## Group Decision-Making

### Diverge Then Converge
Separate ideation from evaluation.
1. Individual generation (parallel)
2. Share all ideas (no judgment)
3. Discuss and build
4. Evaluate and decide
- Prevents groupthink and premature convergence

### Nominal Group Technique
Structured group process.
1. Silent individual ideation
2. Round-robin sharing
3. Discussion for clarity
4. Silent individual voting
5. Aggregate votes
- Balances participation

### Delphi Method
Expert consensus without meeting.
1. Questionnaire to experts
2. Summarize responses
3. Send summary to experts
4. Experts revise estimates
5. Iterate until convergence
- Avoids groupthink and authority bias

### Consent vs. Consensus
Different agreement levels.
- **Consensus**: Everyone agrees it's best
- **Consent**: No one has paramount objection
- Consent faster, often sufficient
- "Can you live with this?"
