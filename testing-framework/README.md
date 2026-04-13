# Testing Framework

> **v1.1.23** | Quality & Testing | 25 iterations

> Multi-language test infrastructure setup, framework selection, and test suite authoring -- covering unit testing (Rust, TypeScript, PHP, Shell), E2E testing (Playwright), component testing (React Testing Library), accessibility testing (axe-core), mutation testing, fuzz testing, and CI/CD integration.

## The Problem

Setting up testing infrastructure is one of those tasks that takes half a day and nobody documents. You need to pick the right framework (Vitest vs. Jest for TypeScript? ShellSpec vs. BATS for shell scripts?), configure it for your project structure, set up CI/CD integration, add coverage reporting, and make sure the whole thing runs fast enough that developers actually use it. Get any of these decisions wrong and you either have slow tests nobody runs, flaky tests nobody trusts, or no tests at all.

The problem multiplies in polyglot projects. A team with a Rust backend, a Next.js frontend, and shell scripts for deployment needs three different testing setups, each with its own configuration, naming conventions, and CI integration patterns. The Rust developer writes excellent unit tests but has no idea how to set up Playwright for the frontend. The frontend developer uses React Testing Library but has never configured PHPUnit. The DevOps engineer writes shell scripts with no tests at all because "who tests bash scripts?"

Beyond setup, teams struggle with testing concerns that cross language boundaries: accessibility testing (how to integrate axe-core with component tests and E2E tests), mutation testing (how to verify your tests actually catch bugs, not just cover lines), fuzz testing (how to find edge cases you did not think of), and CI/CD integration (how to make tests run fast in parallel with proper artifact collection). Each of these is a specialized skill that requires different tools and patterns, and most teams learn them through painful trial and error.

## The Solution

This plugin provides a complete testing infrastructure toolkit covering six testing modules: Rust unit testing with cargo test and tokio, E2E testing with Playwright including visual analysis and screenshot capture, Next.js testing with Vitest, React Testing Library, and Playwright, TYPO3/PHP testing with PHPUnit, shell script testing with ShellSpec and BATS, and skill validation testing. It includes specialized coverage for accessibility testing (axe-core), mutation testing, fuzz testing, and CI/CD integration.

The skill operates as a decision matrix: describe what you need to test and in what language, and it routes you to the right framework, configuration, and patterns. Thirty reference files provide deep guidance on every testing topic from the AAA pattern and naming conventions through async testing and CI/CD integration. Eleven utility scripts handle infrastructure setup, test generation, quality analysis, and validation. Templates for Rust, E2E/Playwright, TYPO3/PHP, and Next.js provide ready-to-use configurations and test file starters.

The core philosophy is "deployment confidence, not coverage theater." Tests should catch real bugs, not boost metrics. Every recommendation is grounded in that principle -- from which assertions to use (specific over generic) to how to organize tests (by feature, not by type) to what to mock (external dependencies) and what not to mock (pure functions).

## Before vs After

| Without this plugin | With this plugin |
|---|---|
| Half a day setting up test infrastructure by trial and error | Decision matrix routes to the right framework, provides config templates, and generates test starters in minutes |
| Shell scripts with zero tests -- "who tests bash?" | ShellSpec (BDD-style) and BATS (TAP-compliant) with setup scripts, templates, and CI integration |
| Accessibility testing is a manual audit done once before launch | axe-core integrated into component tests and E2E tests, running automatically on every PR |
| 90% line coverage but tests do not catch real bugs | Mutation testing verifies test quality by checking whether tests fail when code is deliberately broken |
| Flaky E2E tests that fail randomly in CI | Playwright best practices: proper waits, retry strategies, artifact collection, and screenshot comparison |
| CI/CD test integration configured differently across projects | Reusable GitHub Actions and GitLab CI templates with parallel execution, coverage reporting, and artifact management |

## Installation

Add the SkillStack marketplace, then install this plugin:

```
/plugin marketplace add viktorbezdek/skillstack
/plugin install testing-framework@skillstack
```

### Verify installation

After installing, test with:

```
Set up a complete testing stack for my Next.js project -- I need unit tests, component tests, and E2E tests
```

The skill should activate and provide a configured Vitest + React Testing Library + Playwright setup with example tests and CI/CD integration.

## Quick Start

1. **Install** the plugin using the commands above
2. **Describe your testing need**: `I need to set up Playwright E2E tests for my React application`
3. The skill **configures the framework**: Playwright config, page object templates, global setup/teardown, and a first test spec
4. **Write your first test** with guidance: the skill shows the Playwright pattern for your specific page and walks through assertions
5. **Add CI integration**: the skill provides a GitHub Actions workflow that runs Playwright tests in parallel with screenshot artifact collection

## What's Inside

This is a single-skill plugin with an extensive ecosystem of references, scripts, templates, assets, and examples.

| Component | Purpose |
|---|---|
| `SKILL.md` | Decision matrix, six testing modules with quick starts, available scripts and references, best practices, troubleshooting |
| 30 reference files | Deep guidance on testing patterns, frameworks, CI/CD, accessibility, mutation, fuzz testing |
| 11 utility scripts | Infrastructure setup, test generation, quality analysis, validation |
| Templates for 4 platforms | Rust, E2E/Playwright, TYPO3/PHP, Next.js |
| Examples | E2E with React Vite, Next.js unit/component/E2E, analysis reports |
| Assets | Config files, checklists, workflow phases, best practices data |

**Eval coverage:** 13 trigger evaluation cases, 3 output evaluation cases.

**Key references:**

| Reference | Topic |
|---|---|
| `aaa-pattern.md` | Arrange-Act-Assert pattern with detailed examples |
| `naming-conventions.md` | Test naming best practices across languages |
| `anti-patterns.md` | Common testing anti-patterns to avoid |
| `test-builders.md` | Test builder and object mother patterns |
| `unit-testing.md` | PHP/TYPO3 unit testing patterns |
| `functional-testing.md` | Functional testing with database access |
| `e2e-testing.md` | End-to-end testing guide |
| `javascript-testing.md` | JavaScript/TypeScript testing patterns |
| `async-testing.md` | Async test patterns for concurrent code |
| `accessibility-testing.md` | axe-core WCAG compliance testing |
| `a11y-testing.md` | Accessibility testing guidelines |
| `fuzz-testing.md` | Security fuzz testing methodologies |
| `mutation-testing.md` | Test quality verification via code mutation |
| `ci-cd.md` | GitHub Actions and GitLab CI workflows |
| `ci-integration.md` | CI/CD integration patterns |
| `gotchas.md` | BATS common pitfalls and solutions |
| `advanced-patterns.md` | ShellSpec advanced testing patterns |
| `troubleshooting.md` | Debugging test failures across frameworks |
| `sonarcloud.md` | SonarCloud integration for quality gates |

**Key scripts:**

| Script | Purpose |
|---|---|
| `analyze-test-quality.py` | Analyze test file quality and patterns |
| `setup-testing.sh` | Set up TYPO3 testing infrastructure |
| `generate-test.sh` | Generate test class templates (unit, functional, E2E) |
| `validate-setup.sh` | Validate testing infrastructure configuration |
| `run_tests.py` | Run skill test suites |
| `generate_test_template.py` | Generate test templates from skill definitions |
| `validate_test_results.py` | Validate test outputs against expected results |
| `diagnose_test.sh` | Diagnose ShellSpec test failures |
| `init_bats_project.sh` | Initialize BATS project structure |
| `generate_test_deps.py` | Generate Next.js test dependencies |

### testing-framework

**What it does:** Activates when you need to set up testing infrastructure, choose a test framework, write tests, configure test automation, or integrate tests into CI/CD. Routes you to the right framework and patterns based on your language, platform, and testing needs. Covers unit, integration, E2E, component, accessibility, mutation, and fuzz testing.

**Try these prompts:**

```
Set up a complete testing stack for my Next.js app with Vitest, React Testing Library, and Playwright
```

```
I need to test my shell scripts -- what framework should I use and how do I set it up?
```

```
Add accessibility testing to my React components using axe-core
```

```
Configure GitHub Actions to run my Playwright E2E tests in parallel with screenshot artifacts
```

```
My tests have 85% coverage but I don't trust them -- how do I verify they actually catch bugs?
```

```
Write Rust unit tests for this async function using tokio and the AAA pattern
```

## Real-World Walkthrough

You are building a TYPO3 extension for a large enterprise client. The extension manages product catalogs with CRUD operations, search, and a REST API. It needs unit tests for business logic, functional tests for database operations, E2E tests for the backend module UI, and the entire test suite must run in GitHub Actions. You have never set up testing for a TYPO3 extension before.

You open Claude Code and say:

```
I need to set up a complete testing infrastructure for a TYPO3 extension -- unit tests, functional tests with database, and E2E tests for the backend module. It needs to run in GitHub Actions.
```

The skill activates and routes you to the **TYPO3/PHP testing module**. It starts with infrastructure setup:

```bash
scripts/setup-testing.sh --with-e2e
```

This generates the testing infrastructure: `phpunit.xml` configurations for unit and functional tests, the bootstrap file for functional tests (`FunctionalTestsBootstrap.php`), Playwright configuration for E2E tests, and the GitHub Actions workflow file. The skill explains each component:

- **Unit tests** (`Build/Tests/Unit/`): Fast tests for validators, services, and utility classes. No database, no TYPO3 framework -- pure PHP logic tested in isolation. PHPUnit runs these in milliseconds.
- **Functional tests** (`Build/Tests/Functional/`): Tests that need the TYPO3 database layer. Each test gets a fresh database state via fixtures. PHPUnit runs these with the functional test bootstrap.
- **E2E tests** (`Build/Tests/E2E/`): Playwright tests that automate the TYPO3 backend module browser. These verify the actual UI behavior after login.

You start with the product validator:

```
Generate a unit test for my ProductValidator class -- it should validate that product names are non-empty and prices are positive
```

The skill generates the test using the AAA pattern:

```php
class ProductValidatorTest extends UnitTestCase
{
    private ProductValidator $subject;

    protected function setUp(): void
    {
        parent::setUp();
        $this->subject = new ProductValidator();
    }

    /**
     * @test
     */
    public function validateRejectsEmptyProductName(): void
    {
        // Arrange
        $product = new Product('', 29.99);

        // Act
        $result = $this->subject->validate($product);

        // Assert
        self::assertFalse($result->isValid());
        self::assertContains('name', $result->getErrorFields());
    }
}
```

The naming follows the convention from `naming-conventions.md`: `validate_RejectsEmpty_ProductName` (method_Scenario_ExpectedBehavior). The skill generates four test methods covering: empty name, negative price, valid product, and boundary values (zero price, single-character name).

Next, you need functional tests for the repository:

```
Generate functional tests for ProductRepository -- it needs to test CRUD operations with the database
```

The skill generates a functional test with database fixtures:

```php
class ProductRepositoryTest extends FunctionalTestCase
{
    protected array $testExtensionsToLoad = ['my_extension'];

    protected function setUp(): void
    {
        parent::setUp();
        $this->importCSVDataSet(__DIR__ . '/Fixtures/Products.csv');
    }
}
```

It creates the CSV fixture file with test data and generates tests for `findByUid`, `findByCategory`, `add`, `update`, and `remove`. The skill references `functional-testing.md` for the container reset pattern -- ensuring each test starts with clean state.

For E2E testing, you say:

```
I need Playwright E2E tests for the backend product list module -- test that an admin can view, create, and delete products
```

The skill generates a Playwright test spec using the page object pattern:

```typescript
test('admin creates new product', async ({ page }) => {
  await page.goto('/typo3/module/products');
  await page.getByRole('button', { name: /create/i }).click();
  await page.getByLabel(/product name/i).fill('Test Product');
  await page.getByLabel(/price/i).fill('49.99');
  await page.getByRole('button', { name: /save/i }).click();
  await expect(page.getByText('Test Product')).toBeVisible();
});
```

The skill also adds accessibility testing using axe-core:

```typescript
test('product list has no accessibility violations', async ({ page }) => {
  await page.goto('/typo3/module/products');
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toHaveLength(0);
});
```

Finally, the GitHub Actions workflow. The skill generates a complete CI configuration from the `templates/typo3/github-actions-tests.yml` template:

```yaml
jobs:
  unit-tests:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        php-version: ['8.2', '8.3']
    steps:
      - uses: actions/checkout@v4
      - name: Run unit tests
        run: vendor/bin/phpunit -c Build/Tests/UnitTests.xml

  functional-tests:
    runs-on: ubuntu-latest
    services:
      mysql:
        image: mysql:8.0
    steps:
      - name: Run functional tests
        run: vendor/bin/phpunit -c Build/Tests/FunctionalTests.xml

  e2e-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Run Playwright tests
        run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-screenshots
          path: test-results/
```

After the setup, you run `scripts/validate-setup.sh` to verify everything is configured correctly. The validation checks PHPUnit configuration, database connectivity for functional tests, Playwright browser installation, and CI workflow syntax. All checks pass.

You now have a complete testing infrastructure: 8 unit tests, 6 functional tests, 4 E2E tests (including accessibility), and a CI pipeline that runs them all on every pull request -- set up in about an hour instead of half a day of trial and error.

## Usage Scenarios

### Scenario 1: Setting up testing for a new Next.js project

**Context:** You are starting a Next.js project and want to set up testing from day one -- unit tests for utilities, component tests with React Testing Library, and E2E tests with Playwright.

**You say:** `Set up the complete Next.js testing stack -- Vitest, React Testing Library, Playwright, and accessibility testing with axe-core`

**The skill provides:**
- Vitest config (`vitest.config.ts`) with path aliases and test setup
- React Testing Library setup with custom render utility
- Playwright config with projects for desktop and mobile viewports
- axe-core integration for component and E2E accessibility tests
- Example tests for each type (unit, component, E2E)

**You end up with:** A fully configured testing stack where you can write `bun test` for unit/component tests and `bunx playwright test` for E2E -- with accessibility checking built into both.

### Scenario 2: Adding tests to shell scripts

**Context:** Your deployment scripts are 500 lines of untested Bash. After a deployment failure caused by a subtle quoting bug, you want to add tests.

**You say:** `I need to test my deployment shell scripts. They parse config files, validate environments, and call APIs.`

**The skill provides:**
- Framework recommendation: ShellSpec for BDD-style tests (better for complex scripts) or BATS for TAP-compliant tests (better for CI integration)
- Project initialization with `scripts/init_bats_project.sh`
- Test templates for config parsing, environment validation, and API mocking
- Common gotchas from `references/gotchas.md` (quoting in assertions, temp file cleanup, subprocess mocking)

**You end up with:** A BATS test suite covering your critical deployment paths, running in CI, catching the class of bugs that caused the original failure.

### Scenario 3: Verifying test quality with mutation testing

**Context:** Your project has 88% test coverage, but you suspect many tests are testing implementation details rather than behavior. A recent bug shipped despite passing all tests.

**You say:** `My tests have high coverage but they didn't catch a real bug. How do I verify the tests actually work?`

**The skill provides:**
- Mutation testing setup from `references/mutation-testing.md` -- deliberately break the code and check if tests fail
- Analysis of which tests are testing behavior vs. implementation details
- Guidance on improving mutation score by writing tests that assert observable outcomes
- Anti-pattern identification from `references/anti-patterns.md` (testing mock calls instead of results)

**You end up with:** A mutation testing report showing which tests would fail to catch real bugs, plus revised tests that verify behavior instead of implementation.

### Scenario 4: CI/CD test integration with parallel execution

**Context:** Your test suite takes 20 minutes to run in CI, causing developer frustration and slow PR merges. You need to parallelize and optimize.

**You say:** `Our CI tests take 20 minutes. Help me parallelize them and set up proper artifact collection.`

**The skill provides:**
- GitHub Actions matrix strategy for parallel test execution by shard
- Test splitting by execution time (from `references/ci-cd.md`)
- Artifact configuration for screenshots, coverage reports, and JUnit XML
- SonarCloud integration for quality gate enforcement (from `references/sonarcloud.md`)

**You end up with:** A CI pipeline that runs in 5 minutes with 4 parallel shards, collects screenshots on failure, and enforces coverage thresholds through SonarCloud.

## Ideal For

- **Teams setting up testing infrastructure from scratch** -- the decision matrix and configuration templates eliminate the trial-and-error of framework selection and setup
- **Polyglot projects needing consistent testing across languages** -- unified methodology (AAA pattern, naming conventions, CI integration) across Rust, TypeScript, PHP, and Shell
- **Teams adding specialized testing** -- accessibility testing (axe-core), mutation testing, and fuzz testing are specialized skills that most teams learn through painful trial and error
- **DevOps engineers who need to test shell scripts** -- ShellSpec and BATS setup with templates, gotchas documentation, and CI integration patterns

## Not For

- **TDD methodology and red-green-refactor workflow** -- use [test-driven-development](../test-driven-development/) for the test-first development methodology; this plugin provides the frameworks and infrastructure that TDD uses
- **Diagnosing and fixing bugs** -- use [debugging](../debugging/) for root cause analysis; this plugin helps you write the tests that prevent bugs, not diagnose them
- **Reviewing existing code or PRs** -- use [code-review](../code-review/) for structured code reviews; this plugin focuses on test authoring and infrastructure

## How It Works Under the Hood

The plugin is a single skill with six testing modules organized by platform: Rust, E2E/Playwright, Next.js, TYPO3/PHP, Shell, and Skill Testing. The SKILL.md body contains the decision matrix that routes to the right module, quick starts for each platform with code examples, script and reference listings, universal best practices, and troubleshooting guides.

Thirty reference files provide deep guidance organized into five categories:

- **Core testing patterns (6 files):** AAA pattern, naming conventions, test builders, anti-patterns, writing tests, test patterns
- **Framework-specific (6 files):** Unit testing (PHP), functional testing, async testing, E2E testing, JavaScript testing, functional test patterns
- **Specialized testing (4 files):** Fuzz testing, mutation testing, accessibility testing (2 files)
- **CI/CD and tools (6 files):** GitHub Actions, GitLab CI, CI integration, test runners, quality tools, SonarCloud
- **Shell testing (5 files):** BATS gotchas, assertions, advanced patterns, troubleshooting, real-world examples

Templates cover four platforms (Rust, E2E/Playwright, TYPO3/PHP) with configuration files, test starters, and CI workflows. Eleven utility scripts handle setup, generation, validation, and analysis. Assets include config files, E2E workflow phase documentation, accessibility check data, and Rust development checklists.

## Related Plugins

- **[Test-Driven Development](../test-driven-development/)** -- The Red-Green-Refactor methodology that uses these frameworks (complementary: TDD is the methodology, this plugin is the infrastructure)
- **[Python Development](../python-development/)** -- Python-specific testing with pytest, fixtures, and parametrization
- **[React Development](../react-development/)** -- React component testing patterns with hooks and architecture
- **[CI/CD Pipelines](../cicd-pipelines/)** -- Pipeline configuration beyond testing -- deployment, infrastructure, and release automation
- **[Code Review](../code-review/)** -- Review test quality and coverage as part of PR reviews

---

Part of [SkillStack](https://github.com/viktorbezdek/skillstack) -- production-grade plugins for Claude Code.
