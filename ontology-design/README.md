# Ontology Design

> **v1.0.10** | Design & UX | 11 iterations

> Design formal knowledge models with classes, properties, relationships, and taxonomies that give your domain a shared, unambiguous vocabulary.

## The Problem

Every software project implicitly defines a domain model, but most teams never make it explicit. The database has a `users` table, the API returns `customer` objects, the frontend calls them `accounts`, and the documentation says `clients`. These are the same concept with four names, and no one notices until the billing team's "customer" does not map to the support team's "account" during an integration.

Without a deliberate ontology, teams reinvent entity relationships in every new feature. One developer models a product with a flat category field. Another adds a hierarchical category system in a different service. A third creates a tagging system that partially overlaps with both. The data becomes inconsistent, migrations become painful, and answering cross-domain questions ("Which products in category X were purchased by users who also bought from category Y?") requires heroic data engineering because the relationships were never formally defined.

The deeper problem is communication. When business stakeholders say "order" and engineers hear "order," they often mean different things -- the business includes draft orders, the engineering model starts at checkout. Ontology design makes these distinctions visible before they become production bugs.

## The Solution

This plugin provides a systematic approach to designing formal knowledge models using classes, properties, relationships, and taxonomies. It gives you a vocabulary of relationship types (is-a, has-a, uses, instance-of), a design template for documenting classes with their properties and cardinalities, design principles (MECE, single inheritance, normalization, domain-driven), and a catalog of anti-patterns to avoid.

The skill produces concrete ontology artifacts: class hierarchies with inheritance, property tables with types and constraints, relationship maps with cardinality, and taxonomy structures. These are not abstract diagrams -- they translate directly into database schemas, API contracts, and type definitions. The output bridges the gap between domain experts who think in business concepts and developers who think in data structures.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Same concept has different names across services (user, customer, account, client) | Single authoritative class definition with explicit synonyms and scope |
| Entity relationships reinvented differently in each feature | Formal relationship map with cardinality and direction, reused across features |
| Flat category fields that cannot express hierarchy or cross-cutting concerns | Taxonomy structures with inheritance and MECE classification |
| God classes with 30+ properties because no one modeled subclasses | Proper class hierarchy with single inheritance and focused responsibilities |
| Domain discussions between business and engineering produce different interpretations | Shared ontology artifact that makes distinctions explicit before implementation |
| Circular dependencies between entities discovered during implementation | Anti-pattern detection catches circular dependencies, orphan classes, and over-abstraction at design time |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install ontology-design@skillstack
```

Run the commands above from inside a Claude Code session. After installation, the skill activates automatically when you mention relevant topics.

## Quick Start

1. Install the plugin using the commands above.
2. Describe the domain you need to model:
   ```
   Design the ontology for an e-commerce platform -- I need to model products, categories, orders, customers, and inventory
   ```
3. The skill produces a class hierarchy with properties, relationships, cardinalities, and taxonomy structure.
4. Drill into specific modeling questions:
   ```
   Should product variants be subclasses of Product or a separate class with a relationship?
   ```
5. Get a decision with trade-off analysis based on MECE principles and your specific cardinality requirements.

## What's Inside

Compact single-skill plugin focused on knowledge modeling and taxonomy design.

| Component | Description |
|---|---|
| **SKILL.md** | Core skill covering ontology components (classes, properties, relationships, instances), relationship types, taxonomy levels, class design template, design principles (MECE, single inheritance, normalization), and anti-patterns |
| **evals/** | 13 trigger evaluation cases + 3 output quality evaluation cases |

### ontology-design

**What it does:** Activates when you need to design formal knowledge models, class hierarchies, taxonomies, entity-relationship structures, or semantic models for any domain. It provides a structured methodology for defining classes with properties and constraints, mapping relationships with cardinality, building classification taxonomies, and avoiding common modeling mistakes.

**Try these prompts:**

```
Design the domain model for a healthcare system with patients, providers, appointments, prescriptions, and insurance claims
```

```
I have a Product class with 25 properties -- help me decompose it into a proper class hierarchy
```

```
Build a taxonomy for categorizing support tickets by type, severity, and product area
```

```
What's the right way to model a many-to-many relationship between students and courses with enrollment metadata?
```

```
Review my entity model -- I think I have circular dependencies between Order, Invoice, and Payment
```

```
Design an ontology for a knowledge management system that needs to represent articles, topics, authors, and cross-references
```

## Real-World Walkthrough

You are building a learning management system (LMS) for a corporate training company. The system needs to handle courses, modules, lessons, quizzes, instructors, learners, enrollments, certifications, and learning paths. The business has been using spreadsheets with inconsistent terminology -- "course" and "program" mean different things to different departments, and no one agrees on how certifications relate to course completions.

**Step 1: Identify the core classes.**

You start by describing the domain:

```
Design the ontology for a corporate LMS. We have courses that contain modules and lessons, quizzes for assessment, instructors who teach and learners who take courses, enrollments tracking progress, certifications awarded on completion, and learning paths that group courses into sequences.
```

The skill produces the initial class inventory, immediately flagging the business terminology issue: "course" and "program" need disambiguation. It proposes `Course` as the atomic unit of instruction (containing modules and lessons), and `LearningPath` as the sequence of courses -- what some departments call a "program." This distinction, made explicit in the ontology, prevents the confusion that has been plaguing the spreadsheets.

**Step 2: Define the class hierarchy.**

The skill maps out inheritance relationships:

```
LearningContent (abstract)
├── Course
│   ├── SelfPacedCourse
│   └── InstructorLedCourse
├── Module
├── Lesson
│   ├── VideoLesson
│   ├── TextLesson
│   └── InteractiveLesson
└── Assessment
    ├── Quiz
    └── FinalExam
```

It applies the MECE principle: every piece of learning content is exactly one type (mutually exclusive), and the subtypes cover all possibilities in the domain (collectively exhaustive). Single inheritance keeps the hierarchy clean -- a `VideoLesson` is a `Lesson` which is `LearningContent`, with no diamond problem.

**Step 3: Map relationships with cardinality.**

You ask for the relationship model:

```
Map the relationships between all the LMS classes, including cardinality and direction
```

The skill produces a relationship table:

| Relation | Source | Target | Cardinality | Description |
|----------|--------|--------|-------------|-------------|
| contains | Course | Module | one-to-many | Course contains ordered modules |
| contains | Module | Lesson | one-to-many | Module contains ordered lessons |
| teaches | Instructor | Course | many-to-many | Instructors can teach multiple courses |
| enrolledIn | Learner | Course | many-to-many | Via Enrollment join class |
| completedBy | Assessment | Learner | many-to-many | Via AttemptRecord join class |
| awards | Course | Certification | many-to-one | Completing a course may award a cert |
| sequences | LearningPath | Course | many-to-many | Ordered sequence via PathStep join class |

The skill flags that `enrolledIn` and `completedBy` need join classes (Enrollment and AttemptRecord) because the relationships carry metadata -- enrollment date, progress percentage, attempt score, completion timestamp.

**Step 4: Design property tables.**

For the core class `Course`, the skill produces:

```markdown
## Class: Course

**Description**: An atomic unit of instruction comprising modules and lessons
**Parent**: LearningContent

### Properties
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | UUID | yes | Unique identifier |
| title | string | yes | Display title |
| slug | string | yes | URL-friendly identifier |
| description | text | yes | Course overview |
| difficulty | enum | yes | beginner/intermediate/advanced |
| estimatedHours | number | yes | Expected completion time |
| status | enum | yes | draft/published/archived |
| prerequisites | Course[] | no | Required prior courses |

### Relationships
| Relation | Target | Cardinality |
|----------|--------|-------------|
| contains | Module | one-to-many |
| taughtBy | Instructor | many-to-many |
| awards | Certification | many-to-one |
```

**Step 5: Validate against anti-patterns.**

The skill reviews the complete ontology and catches two issues. First, `LearningPath` initially had both a `courses` property (direct list) and a `sequences` relationship through `PathStep` -- redundant and potentially inconsistent. The fix: remove the direct list, use only the `PathStep` join class which carries the sequence order. Second, `Certification` had no relationship back to the awarding authority -- an orphan class risk. The fix: add an `issuedBy` relationship to `Organization`.

The result: a complete LMS ontology with 12 classes, clear inheritance hierarchies, explicit relationships with cardinality, property tables for every class, and validated adherence to MECE, single inheritance, and normalization principles. The ontology document becomes the shared reference for the development team, resolving the "course vs. program" terminology debate and providing the blueprint for the database schema, API contracts, and TypeScript type definitions.

## Usage Scenarios

### Scenario 1: Designing a product catalog data model

**Context:** You are building an e-commerce platform and need to model products with variants, categories, pricing, and inventory across multiple warehouses.

**You say:** "Design the ontology for a product catalog. Products have variants (size, color), belong to hierarchical categories, have prices that vary by region, and inventory tracked per warehouse."

**The skill provides:**
- Class hierarchy: Product > ProductVariant with is-a and has-a relationship analysis
- Category taxonomy with hierarchical levels following MECE
- Price as a separate class with region and currency properties (not a flat field on Product)
- Inventory as a join class between ProductVariant and Warehouse with quantity and threshold properties
- Anti-pattern check: ensures no god class, no circular dependencies

**You end up with:** A normalized ontology that translates directly into a database schema, with clear cardinalities that prevent data inconsistencies.

### Scenario 2: Decomposing a god class

**Context:** Your `User` model has grown to 35 properties covering authentication, profile, preferences, billing, permissions, and activity tracking.

**You say:** "My User class has 35 properties and does everything. Help me decompose it into a proper class hierarchy."

**The skill provides:**
- Subclass analysis: which properties cluster into coherent groups
- Proposed hierarchy: User (core identity) with related classes Profile, Preferences, BillingInfo, Permissions, ActivityLog
- Relationship mapping: User has-a Profile (one-to-one), User has-a BillingInfo (one-to-one), etc.
- Property migration table showing which properties move to which class
- Single inheritance validation

**You end up with:** A clean class hierarchy where User has 6 properties (identity only) and related classes hold domain-specific attributes, each with clear boundaries.

### Scenario 3: Building a classification taxonomy

**Context:** Your content platform needs to classify articles into topics, but the current flat tag system has become unmanageable with 500+ tags and no hierarchy.

**You say:** "I have 500 tags with no structure. Help me design a hierarchical taxonomy for classifying articles by topic."

**The skill provides:**
- Taxonomy design with 3-4 levels following the biological taxonomy model
- MECE classification ensuring each article fits into exactly one primary category
- Faceted classification for cross-cutting concerns (topic + difficulty + format)
- Migration strategy from flat tags to hierarchical taxonomy

**You end up with:** A structured taxonomy with clear levels, MECE categories, and a migration path from the existing tag system.

### Scenario 4: Modeling complex relationships

**Context:** You are building a project management tool where users can belong to multiple organizations, each organization has projects, and users have different roles per project.

**You say:** "Users belong to multiple orgs, orgs have projects, and users have different roles per project. How do I model the three-way relationship between User, Organization, and Project?"

**The skill provides:**
- Join class analysis: Membership (User-Organization) and ProjectRole (User-Project) as separate classes
- Cardinality mapping for each relationship
- Role as an enum property on the join class, not on User or Project
- Anti-pattern check: avoids circular dependency between User > Organization > Project > User

**You end up with:** A clean relationship model with explicit join classes that carry the context-specific metadata (role, permissions, dates).

## Ideal For

- **Backend engineers designing database schemas** -- the ontology translates directly into normalized tables with foreign keys and join tables
- **API designers defining resource models** -- class hierarchies map to REST resources and GraphQL types
- **Domain modelers aligning business and engineering vocabulary** -- the shared ontology artifact makes terminology disagreements visible and resolvable
- **Data architects planning for cross-service integration** -- formal ontologies prevent the "same concept, four names" problem across microservices
- **Anyone decomposing a god class or untangling circular dependencies** -- the anti-pattern catalog identifies structural problems before they become production issues

## Not For

- **CMS content types, editorial workflows, or structured content for publishing** -- use [content-modelling](../content-modelling/) for COPE (Create Once, Publish Everywhere) patterns
- **Database performance tuning, indexing, or query optimization** -- the ontology defines the logical model, not the physical storage
- **API endpoint design, status codes, or pagination** -- use [api-design](../api-design/) for API-level concerns that build on top of the ontology

## How It Works Under the Hood

The skill is a compact, focused knowledge base covering the core discipline of ontology design. The SKILL.md provides the complete framework: four ontology components (classes, properties, relationships, instances), four relationship types (is-a, has-a, uses, instance-of), a full taxonomy hierarchy model, a reusable class design template with property and relationship tables, four design principles (MECE, single inheritance, normalization, domain-driven), and an anti-pattern catalog (god class, orphan classes, circular dependencies, over-abstraction).

There are no additional reference files -- the skill is deliberately compact so it loads fully into context and delivers immediate, actionable ontology design. This makes it fast to activate and directly productive.

The evaluation suite (13 trigger cases, 3 output quality cases) ensures the skill activates reliably on ontology and knowledge modeling queries.

## Related Plugins

- **[Content Modelling](../content-modelling/)** -- CMS-specific content types and editorial workflows built on top of domain ontologies
- **[Consistency Standards](../consistency-standards/)** -- Naming conventions and taxonomy standards for consistent terminology
- **[API Design](../api-design/)** -- API resource design that implements the ontology as endpoints
- **[Systems Thinking](../systems-thinking/)** -- Systems-level analysis of how ontology components interact and influence each other

## Version History

- `1.0.10` fix(design+docs): regenerate READMEs for design and documentation plugins
- `1.0.9` fix: add standard keywords and expand READMEs to full format
- `1.0.8` fix: change author field from string to object in all plugin.json files
- `1.0.7` fix: rename all claude-skills references to skillstack
- `1.0.0` Initial release

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
