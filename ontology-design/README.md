# Ontology Design

> **v1.0.11** | Design & UX | 11 iterations

---

## The Problem

Every software system embeds a model of the world -- classes, properties, relationships, taxonomies -- whether the team designs it intentionally or not. When the model is implicit, problems emerge gradually and painfully. A "User" entity means different things in billing, authentication, and analytics. A "Product" class accumulates 40 properties because nobody defined whether accessories, subscriptions, and physical goods are distinct types. Relationships between entities are expressed as foreign keys with no semantics -- you know two things are connected but not why or how.

The consequences cascade through the entire stack. Database schemas encode an incoherent world model, requiring application-layer hacks to compensate. APIs expose inconsistent naming -- `userId` in one endpoint, `accountId` in another, both meaning the same thing. Search and recommendation systems fail because the taxonomy conflates unrelated concepts. New team members spend weeks understanding the implicit model buried across code, schemas, and tribal knowledge.

Domain experts and engineers speak different languages about the same system. The business says "customers" while the code says "users" and the database says "accounts." Without a shared formal model -- an ontology -- these gaps persist indefinitely, creating friction at every integration point and every new feature.

## The Solution

The Ontology Design plugin gives Claude expertise in formal knowledge modeling with classes, properties, relationships, and taxonomies. It provides a structured approach to designing domain models that are explicit, consistent, and shared across technical and business stakeholders.

The plugin covers the four core components (classes, properties, relationships, instances), four relationship types (is-a, has-a, uses, instance-of), taxonomy design from flat to deep hierarchies, a reusable class design template, and design principles grounded in MECE (mutually exclusive, collectively exhaustive) thinking. It identifies anti-patterns that cause long-term modeling problems: god classes, orphan classes, circular dependencies, and over-abstraction.

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Entity definitions are implicit, scattered across code and schemas | Explicit class definitions with properties, relationships, and cardinality documented in one place |
| "User" means different things in different parts of the system | MECE taxonomy ensures each concept has exactly one definition with clear boundaries |
| Relationships between entities are just foreign keys with no semantics | Typed relationships (is-a, has-a, uses, instance-of) with cardinality and directionality |
| God classes accumulate dozens of unrelated properties | Single responsibility classes with inheritance for shared properties and composition for parts |
| New team members reverse-engineer the domain model from code | Shareable ontology documents that both engineers and domain experts can read |
| Taxonomy design is ad hoc -- categories overlap and miss edge cases | MECE principle applied: mutually exclusive categories that collectively cover the domain |

## Context to Provide

Ontology design works best when you bring the domain knowledge and let the skill apply the modeling discipline. The more concrete your entity descriptions, the more precise the class hierarchy and relationship types.

**What information to include in your prompt:**
- **The domain and its key entities** -- list all the "things" the system tracks (products, users, orders, events, locations) and a one-sentence description of each
- **Business rules and cardinality constraints** -- which entities can have many-to-many relationships, which have one-to-many, and which are one-to-one; examples: "a user can belong to multiple organizations" or "an order has exactly one shipping address"
- **The problem you are solving** -- whether you are designing a new system, decomposing an existing god class, creating a taxonomy, or normalizing inconsistent definitions across services
- **Edge cases that cause problems** -- the cases where your current model breaks down or where your team argues about categorization ("can a user be both a customer and an employee?", "where does a subscription product differ from a one-time purchase product?")

**What makes results better:**
- Listing the actual properties of your existing classes (all 40 of them if it is a god class) -- the skill sorts them into cohesive groups by responsibility
- Describing the ambiguous cases where the same concept means different things in different parts of the system ("User in billing vs User in auth")
- Specifying what queries or operations the model must support ("the system must answer: who are all the users in organization X?", "find all orders that contain product Y")
- Mentioning the downstream implementation target (relational DB schema, document store, knowledge graph, API resource model) so the ontology is designed with the right constraints

**What makes results worse:**
- Describing the UI or database schema instead of the domain model -- "I need a table with columns name, email, address" is a schema; describe the entities and their relationships instead
- Asking the skill to design a schema without first validating the ontology -- conceptual modeling before physical modeling prevents months of schema refactoring
- Omitting cardinality -- "User has Projects" without "one user has many projects, a project has exactly one owner" leaves the most important design decision implicit

**Template prompt -- new domain model:**
```
Design an ontology for [domain].

Key entities (list all, with one-sentence description each):
- [Entity A]: [what it represents]
- [Entity B]: [what it represents]

Key relationships I know about:
- [Entity A] [relationship to] [Entity B]: [cardinality -- one-to-many, many-to-many, etc.]

Business rules / constraints:
- [Rule 1: e.g., "a user can belong to multiple organizations but has one primary org"]
- [Rule 2]

Edge cases to handle:
- [Ambiguous case: e.g., "users can be both customers and employees"]

Queries the model must support:
- [Query 1: e.g., "find all orders for customer X in the last 30 days"]
```

**Template prompt -- god class decomposition:**
```
Decompose my [class name] class. It has these [N] properties:
[list all properties with their types]

The class is used for these operations:
- [Operation 1: e.g., "display user profile in the UI"]
- [Operation 2: e.g., "calculate billing for the subscription"]
- [Operation 3: e.g., "check auth permissions"]

My concern: [what breaks or feels wrong about it -- too many reasons to change, slow queries because of unrelated fields, etc.]
```

## Installation

Add the marketplace and install:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install ontology-design@skillstack
```

### Prerequisites

None. For CMS content types and editorial workflows built on top of ontologies, also install `content-modelling`. For consistency in naming conventions, also install `consistency-standards`.

### Verify installation

After installing, test with:

```
Help me design the domain model for an e-commerce platform -- products, categories, orders, customers, and inventory
```

## Quick Start

1. Install the plugin using the commands above
2. Ask: `Design an ontology for a project management system with users, projects, tasks, and permissions`
3. The skill generates class definitions with properties, relationship types, and cardinality
4. You receive a formal domain model with MECE taxonomy and anti-pattern checks
5. Next, try: `Review my existing data model -- I think my User class has too many responsibilities`

---

## System Overview

```
ontology-design/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
└── skills/
    └── ontology-design/
        ├── SKILL.md         # Core skill (classes, properties, relationships, taxonomy, templates)
        └── evals/
            ├── trigger-evals.json   # 13 trigger evaluation cases
            └── evals.json           # 3 output evaluation cases
```

A single skill with no additional references. The SKILL.md contains the complete ontology design framework: core components, relationship types, taxonomy levels, the class design template, design principles, and anti-patterns.

## What's Inside

| Component | Type | Purpose |
|---|---|---|
| `ontology-design` | Skill | Class design, relationship typing, taxonomy structure, MECE principles, anti-pattern detection |

### Component Spotlight

#### ontology-design (skill)

**What it does:** Activates when you need to design or review formal knowledge models. Provides class/property/relationship definitions, four relationship types with cardinality, taxonomy design from flat to deep hierarchies, a reusable class design template, and anti-pattern detection for common modeling mistakes.

**Input -> Output:** A domain description or existing data model -> Formal ontology with class definitions, typed relationships, cardinality, taxonomy hierarchy, and anti-pattern audit.

**When to use:**
- Designing domain models for new systems
- Reviewing existing data models for structural problems
- Creating taxonomies for product catalogs, content systems, or knowledge bases
- Defining entity relationships with proper typing and cardinality
- Normalizing inconsistent class structures across services

**When NOT to use:**
- CMS content types, editorial workflows, or publishing pipelines (use `content-modelling`)
- Database schema design and SQL optimization (use a database-specific tool)
- API resource naming and endpoint design (use `api-design`)
- Visual entity-relationship diagrams (use a diagramming tool)

**Try these prompts:**

```
Design the domain model for a healthcare system. Key entities: Patient (person receiving care), Provider (doctor, nurse, or specialist), Appointment (scheduled visit), Prescription (medication order), InsuranceClaim (payment request to insurer), Facility (hospital or clinic). Key constraints: a patient can have many providers; a prescription belongs to one patient and is written by one provider; an insurance claim covers one appointment and is filed by one patient. The system must answer: "all upcoming appointments for patient X" and "all prescriptions written by provider Y in the last 90 days."
```

```
My User class has 30 properties. Please decompose it. Properties include: id, email, passwordHash, authToken, refreshToken, tokenExpiry, firstName, lastName, avatarUrl, bio, preferredLanguage, timezone, notificationPrefs (JSON), stripeCustomerId, subscriptionTier, subscriptionExpiry, billingAddress (JSON), organizationId, organizationRole, teamIds (array), lastLoginAt, loginCount, isEmailVerified, mfaEnabled, mfaSecret, createdAt, updatedAt, deletedAt, adminNotes, featureFlags (JSON).
```

```
Create a MECE product taxonomy for an electronics retailer. Products include: MacBook Pro, iPhone 15, AirPods Pro, AppleCare+ for MacBook, iCloud+ subscription, USB-C cable, MagSafe adapter, and in-store repair service. Current categories overlap: AirPods appears under both "Audio" and "iPhone Accessories." Design a taxonomy where each product has exactly one home, with no gaps or overlaps. Max 3 levels deep.
```

```
What relationship type and cardinality connects Organization and Employee? Constraints: an employee belongs to exactly one organization; an organization has many employees; an employee can hold multiple roles within the organization (engineer and team lead simultaneously). The organization existed before any employees and can exist with zero employees. Which pattern handles the multiple-roles case -- inheritance, composition, or a junction entity?
```

```
Review this class hierarchy and tell me if it is well-structured: Vehicle (abstract) > Car, Truck, Bicycle, Motorcycle. Car > ElectricCar, HybridCar, GasCar. Bicycle > ElectricBicycle, ManualBicycle. The system needs to track: fuel efficiency for gas/hybrid/electric cars, motor wattage for electric vehicles (including ElectricBicycle), and cargo capacity for trucks and cargo bicycles. ElectricBicycle needs both the Bicycle and ElectricVehicle properties. Is the hierarchy correct, or is there a diamond inheritance problem?
```

---

## Prompt Patterns

### Good Prompts vs Bad Prompts

| Bad (vague, won't activate well) | Good (specific, activates reliably) |
|---|---|
| "Help me with my data" | "Design an ontology for a multi-tenant SaaS with organizations, workspaces, projects, and role-based access" |
| "I need classes" | "Decompose my Order class -- it currently holds customer info, line items, shipping, payment, and fulfillment status" |
| "Make a taxonomy" | "Create a MECE product taxonomy for a grocery delivery platform covering fresh produce, packaged goods, household items, and prepared meals" |
| "What's a good model?" | "Review my class hierarchy: Content > Article, Content > Video, Content > Podcast -- should Newsletter be a subclass of Content or Article?" |

### Structured Prompt Templates

**For new domain models:**
```
Design an ontology for [domain]. Key entities: [list entities]. Key relationships: [describe how entities connect]. Constraints: [business rules, cardinality limits, invariants].
```

**For class decomposition:**
```
My [class name] class has these properties: [list all]. It's becoming a god class. Help me decompose it into focused classes with proper relationships.
```

**For taxonomy design:**
```
Create a taxonomy for [domain] that covers [list categories]. Requirements: MECE (no overlap, no gaps), max [N] levels deep, must accommodate [edge cases].
```

### Prompt Anti-Patterns

- **Describing the UI instead of the domain** -- "I need a form with fields for name, email, and address" is a UI question; describe the entities and their relationships instead
- **Asking for a database schema directly** -- ontology design produces a conceptual model; translate to physical schema after the model is validated
- **Ignoring cardinality** -- "User has Projects" is incomplete without specifying one-to-many, many-to-many, or the constraints on the relationship

## Real-World Walkthrough

**Starting situation:** You are building a learning management system (LMS) for a corporate training platform. The current data model evolved organically: a `Course` table with 25 columns including instructor info, a `User` table that conflates students, instructors, and admins, and a `Content` table that mixes video lessons, quizzes, and downloadable resources. The team wants to add certification tracking, but the existing model has no clean place for it.

**Step 1: Entity identification.** You ask: "Design the ontology for an LMS with courses, lessons, quizzes, users (students/instructors/admins), enrollments, progress tracking, and certifications."

The skill identifies the core classes: Course, Lesson, Quiz, User, Enrollment, Progress, Certification, and Content (abstract). It immediately flags the mixed-responsibility issues: User should be decomposed by role, Course should not contain instructor data directly, and Content needs a proper type hierarchy.

**Step 2: Class hierarchy design.** The skill designs the taxonomy. `User` becomes an abstract class with three subclasses: Student (has enrollments, progress), Instructor (has courses taught, credentials), and Admin (has permissions, audit trail). The skill applies single inheritance and notes that if a user can be both student and instructor, a role-based composition pattern is better than multiple inheritance.

**Step 3: Content type hierarchy.** The skill creates: `Content` (abstract: id, title, duration, format) with subclasses `VideoLesson`, `TextLesson`, `Quiz`, and `Resource`. Each subclass has type-specific properties: VideoLesson has `videoUrl` and `transcript`; Quiz has `questions` and `passingScore`; Resource has `fileType` and `downloadUrl`. This is an is-a (inheritance) relationship.

**Step 4: Relationship mapping.** The skill defines typed relationships:
- Course has-a Lesson (one-to-many, ordered by `sequence`)
- Lesson has-a Content (one-to-one)
- Student uses Course via Enrollment (many-to-many with junction entity)
- Enrollment has-a Progress (one-to-one per student-course pair)
- Course produces Certification (one-to-one template, many instances per student)

Each relationship gets cardinality and directionality. The skill notes that Enrollment is a first-class entity (not just a join table) because it carries its own properties: enrollment date, completion date, score.

**Step 5: Anti-pattern audit.** The skill checks the model against its anti-pattern list. No god classes (Course was decomposed, User was split). No orphan classes (every class has at least one relationship). No circular dependencies (the relationship graph is a directed acyclic graph with Enrollment as the hub). Slight over-abstraction risk flagged: the Content abstract class may be unnecessary if VideoLesson, TextLesson, Quiz, and Resource share fewer than 3 properties.

**Step 6: Certification integration.** With the clean model, certification fits naturally: `Certification` is a class with `template` (course-level definition of requirements) and `instance` (student-level issued certificate). The relationship: Course defines-a CertificationTemplate (one-to-one), Student earns-a CertificationInstance (one-to-many). Progress.completionPercentage >= CertificationTemplate.threshold triggers issuance.

**Final outcome:** A formal ontology with 10 classes, 4 relationship types, proper cardinality, a content type hierarchy, role-based user model, and clean certification integration. The model is documented using the class design template from the skill, readable by both engineers and the training operations team.

**Gotchas discovered:** The skill identified that the "student can also be an instructor" edge case requires composition (role assignment) rather than inheritance (User > Student, User > Instructor). This prevented a diamond inheritance problem that would have surfaced during implementation.

## Usage Scenarios

### Scenario 1: Decomposing a god class

**Context:** Your `Product` class has 45 properties covering physical attributes, pricing, inventory, shipping, reviews, and marketing metadata. Every query touches this one table.

**You say:** "My Product class has 45 properties including dimensions, weight, price, discount rules, stock levels, warehouse locations, reviews, ratings, SEO metadata, and category tags. Help me decompose it."

**The skill provides:**
- Decomposition into 6 focused classes: Product (core identity), PhysicalAttributes (dimensions, weight), Pricing (price, discounts, rules), Inventory (stock, warehouse), Reviews (ratings, comments), and MarketingMetadata (SEO, tags)
- Relationship types: Product has-a PhysicalAttributes (one-to-one), Product has-a Pricing (one-to-one, versioned), Product has-a Inventory (one-to-many per warehouse)
- MECE validation: each property belongs to exactly one class

**You end up with:** Six focused classes with clear responsibilities and typed relationships, replacing the 45-property monolith.

### Scenario 2: Designing a MECE taxonomy

**Context:** You are building a content platform and need to categorize articles, tutorials, case studies, news, and opinion pieces. Current categories overlap (a tutorial can also be a case study).

**You say:** "Create a MECE content taxonomy where articles, tutorials, case studies, news, and opinion pieces have clear boundaries without overlap."

**The skill provides:**
- MECE analysis showing the overlap: "tutorial" is a format, "case study" is a subject -- they are different classification dimensions
- Two-axis taxonomy: Format (article, tutorial, video, infographic) x Subject (case study, announcement, opinion, reference)
- Faceted classification: content tagged on both axes instead of shoehorned into one
- Decision rule for each category boundary

**You end up with:** A faceted taxonomy where content is classified along two orthogonal dimensions, eliminating the overlap problem.

### Scenario 3: Modeling complex relationships

**Context:** You are building a legal case management system where cases involve parties (plaintiffs, defendants, witnesses), documents (filings, exhibits, orders), and events (hearings, depositions, rulings). Relationships are many-to-many with role qualifiers.

**You say:** "Design the relationship model for a legal case system. Cases have parties with different roles, documents with different types, and events with participants. A person can be a plaintiff in one case and a witness in another."

**The skill provides:**
- Person as a role-independent entity, with CaseParty as a junction entity carrying the role (plaintiff, defendant, witness)
- Document with type hierarchy (Filing, Exhibit, Order) using is-a inheritance
- Event with participant junction entity carrying role (judge, attorney, witness)
- Cardinality: Case has-a CaseParty (many), CaseParty uses Person (many-to-one), Event has-a EventParticipant (many)

**You end up with:** A relationship model where people exist independently of cases, with role-qualified junction entities that allow the same person to hold different roles across cases.

---

## Decision Logic

**When is-a vs has-a vs uses?**

- **Is-a (inheritance)** -- when the child IS a specialized version of the parent and shares all parent properties. Test: "An ElectricCar IS a Car" -- true, use is-a. "An Engine IS a Car" -- false, don't use is-a.
- **Has-a (composition)** -- when the parent CONTAINS the child as a part. Test: "A Car HAS an Engine" -- true, use has-a. The child cannot exist independently of the parent.
- **Uses (association)** -- when two entities are related but neither contains the other. Test: "A Person USES a Tool" -- true, use uses. Both exist independently.
- **Instance-of** -- when relating a specific entity to its class definition. "Fido instance-of Dog."

**When to use a junction entity vs a simple foreign key?**

Use a junction entity (first-class relationship) when the relationship carries its own properties (enrollment date, role, status), when the relationship has its own lifecycle (created, active, expired), or when the same pair can be related multiple times with different qualifiers.

## Failure Modes & Edge Cases

| Failure | Symptom | Recovery |
|---|---|---|
| God class | One class has 20+ properties spanning multiple concerns | Decompose by responsibility; each class should have a single cohesive purpose |
| Orphan class | A class with no relationships to any other class | Either delete it (YAGNI) or identify its connections -- every entity should relate to at least one other |
| Circular dependency | A references B which references A, creating update cascades | Break the cycle with a junction entity or event-driven decoupling |
| Over-abstraction | Abstract base classes that add no shared properties or behavior | Eliminate abstractions that share fewer than 3 properties; prefer composition over deep hierarchies |
| Diamond inheritance | A class inherits from two classes that share a common ancestor | Switch to composition with roles or interfaces; single inheritance preferred |
| MECE violation | Categories overlap (item belongs to two) or have gaps (item belongs to none) | Audit taxonomy with concrete examples; faceted classification resolves overlap by splitting into orthogonal dimensions |

## Ideal For

- **Backend engineers** designing data models for new systems who want principled domain modeling before writing schemas
- **Architects** normalizing inconsistent entity definitions across microservices where "User" means different things
- **Product managers** defining domain vocabulary that both business and engineering teams share
- **Data engineers** building knowledge graphs, search taxonomies, or recommendation systems that need clean entity hierarchies
- **Teams refactoring** legacy systems where the implicit domain model has accumulated god classes and circular dependencies

## Not For

- **CMS content modeling** -- content types, editorial workflows, and publishing pipelines use `content-modelling`
- **Database schema optimization** -- index design, query optimization, and physical schema layout are implementation concerns, not conceptual modeling
- **API resource design** -- endpoint naming, versioning, and response formats use `api-design`

## Related Plugins

- **content-modelling** -- content type design built on top of ontological foundations
- **consistency-standards** -- naming conventions and taxonomy standards that complement ontology design
- **api-design** -- API resource naming and endpoint design informed by the domain model
- **edge-case-coverage** -- identifying boundary conditions that stress-test ontology completeness

---

*SkillStack plugin by [Viktor Bezdek](https://github.com/viktorbezdek) -- licensed under MIT.*
