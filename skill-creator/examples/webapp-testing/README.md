# Web App Testing Skill Example

This example demonstrates a skill for automated web application testing using Python and Playwright.

## Skill Structure

- **SKILL.md** - Main skill file with instructions
- **LICENSE.txt** - MIT License

## Removed Resources (Described Below)

### examples/ (3 example test scripts)

Example test implementations demonstrating different testing patterns:

#### console_logging.py
Testing console output and JavaScript errors:
- Capture console.log, console.error, console.warn messages
- Assert expected console outputs
- Detect JavaScript runtime errors
- Monitor network errors
- Validate client-side logging

**Key patterns:**
- Page.on('console') event listener
- Message type filtering
- Error detection and reporting

#### element_discovery.py
Finding and interacting with page elements:
- Multiple selector strategies (CSS, XPath, text)
- Waiting for elements to appear
- Handling dynamic content
- Shadow DOM navigation
- Frame and iframe handling

**Key patterns:**
- page.wait_for_selector()
- page.locator() for modern selectors
- Retry logic for flaky elements
- Explicit waits vs implicit waits

#### static_html_automation.py
Testing static HTML pages without server:
- Loading local HTML files
- Testing without backend server
- Validating DOM structure
- Form interaction testing
- Client-side validation tests

**Key patterns:**
- file:// URL loading
- Pure frontend testing
- No network dependencies
- Fast test execution

### scripts/

Utility scripts for test execution:

#### with_server.py
Test harness that manages test server lifecycle:
- Starts local development server
- Runs tests against live server
- Cleans up server after tests
- Handles port conflicts
- Captures server logs

**Usage pattern:**
```python
with TestServer(port=8000) as server:
    # Run tests against server.url
    page.goto(f"{server.url}/index.html")
    # Tests run here
# Server automatically cleaned up
```

## Use Cases

This skill helps with:
- Writing Playwright tests for web apps
- Testing without a running server
- Capturing console output and errors
- Finding elements reliably
- Managing test server lifecycle
- Handling dynamic content

## Skill Patterns Demonstrated

- **Example tests** - Realistic test scenarios
- **Test patterns** - Common testing approaches
- **Utility scripts** - Test infrastructure helpers
- **Multiple strategies** - Different ways to solve same problem
- **Production patterns** - Real-world test code

## Dependencies

Tests require:
```
playwright>=1.40.0
pytest>=7.4.0
pytest-playwright>=0.4.0
```

## Restoration

To recreate the test examples:
1. Create `examples/console_logging.py` with console capture examples
2. Create `examples/element_discovery.py` with selector pattern examples
3. Create `examples/static_html_automation.py` with file:// URL examples
4. Create `scripts/with_server.py` with test server context manager
5. Add pytest fixtures and configuration
6. Test with: `pytest examples/`

See SKILL.md for the complete skill implementation with inline examples.

