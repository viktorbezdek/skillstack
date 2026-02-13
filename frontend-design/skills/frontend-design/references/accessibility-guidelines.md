# Accessibility Guidelines

Comprehensive guide to creating accessible user interfaces following WCAG 2.2 standards and modern best practices (2025).

## Understanding Web Accessibility

Web accessibility ensures people with disabilities can perceive, understand, navigate, and interact with digital content.

**Who benefits from accessibility:**
- Visual impairments (blindness, low vision, color blindness)
- Auditory impairments (deafness, hard of hearing)
- Motor impairments (limited dexterity, tremors, paralysis)
- Cognitive impairments (dyslexia, ADHD, memory issues)
- Situational limitations (bright sunlight, noisy environments, broken mouse)
- Everyone (clear interfaces benefit all users)

**Legal requirements:**
- ADA (Americans with Disabilities Act)
- Section 508 (US federal websites)
- EN 301 549 (European standard)
- AODA (Ontario, Canada)

## WCAG 2.2 Principles (POUR)

Web Content Accessibility Guidelines organize requirements around four principles.

### Perceivable

Information and UI components must be presentable to users in ways they can perceive.

**Key guidelines:**
- Provide text alternatives for non-text content
- Provide captions and alternatives for multimedia
- Create content that can be presented in different ways
- Make it easier to see and hear content

### Operable

UI components and navigation must be operable.

**Key guidelines:**
- Make all functionality keyboard accessible
- Give users enough time to read and use content
- Don't design content that causes seizures
- Help users navigate and find content
- Make it easier to use inputs other than keyboard

### Understandable

Information and UI operation must be understandable.

**Key guidelines:**
- Make text readable and understandable
- Make content appear and operate in predictable ways
- Help users avoid and correct mistakes

### Robust

Content must be robust enough to be interpreted by a wide variety of user agents, including assistive technologies.

**Key guidelines:**
- Maximize compatibility with current and future user agents
- Support assistive technologies
- Use semantic HTML

## WCAG Conformance Levels

**Level A (Minimum):**
- Essential accessibility features
- Bare minimum legal compliance
- Not sufficient for most organizations

**Level AA (Target):**
- Industry standard (2025)
- Required by most laws and policies
- Addresses major accessibility barriers

**Level AAA (Enhanced):**
- Highest level of accessibility
- Not required for entire sites
- May not be achievable for all content

**Recommendation:** Target Level AA compliance for all public-facing UIs.

## Semantic HTML

Use HTML elements for their intended purpose.

### Proper Heading Structure

Headings create document outline for screen readers.

**Good heading hierarchy:**
```html
<h1>Page Title</h1>
  <h2>Main Section</h2>
    <h3>Subsection</h3>
    <h3>Another Subsection</h3>
  <h2>Another Section</h2>
    <h3>Subsection</h3>
```

**Anti-pattern:**
```html
<!-- Don't skip levels or use headings for styling -->
<h1>Page Title</h1>
<h3>Skipped h2 - breaks outline</h3>
<h2 class="small-text">Using h2 just for size</h2>
```

### Landmark Regions

Landmarks help screen reader users navigate.

**Essential landmarks:**
```html
<header> <!-- Site/page header -->
<nav> <!-- Navigation -->
<main> <!-- Primary content (one per page) -->
<aside> <!-- Complementary content -->
<footer> <!-- Site/page footer -->
<section> <!-- Thematic content grouping -->
<article> <!-- Self-contained content -->
```

**Example page structure:**
```html
<header>
  <nav aria-label="Main navigation">
    <!-- Primary navigation -->
  </nav>
</header>

<main>
  <h1>Page Title</h1>
  <article>
    <h2>Article Title</h2>
    <!-- Content -->
  </article>
  <aside>
    <h2>Related Links</h2>
    <!-- Sidebar content -->
  </aside>
</main>

<footer>
  <!-- Footer content -->
</footer>
```

### Semantic Form Elements

Forms require special attention for accessibility.

**Accessible form example:**
```html
<form>
  <!-- Always associate labels with inputs -->
  <label for="email">Email address</label>
  <input
    type="email"
    id="email"
    name="email"
    required
    aria-describedby="email-help"
  />
  <span id="email-help">We'll never share your email.</span>

  <!-- Group related inputs -->
  <fieldset>
    <legend>Shipping address</legend>
    <label for="street">Street</label>
    <input type="text" id="street" name="street" />

    <label for="city">City</label>
    <input type="text" id="city" name="city" />
  </fieldset>

  <!-- Clear error messages -->
  <div role="alert" aria-live="polite">
    <p id="email-error" class="error">
      Please enter a valid email address.
    </p>
  </div>

  <button type="submit">Submit</button>
</form>
```

## ARIA (Accessible Rich Internet Applications)

ARIA attributes enhance accessibility when semantic HTML isn't sufficient.

### ARIA Principles

**First Rule of ARIA:**
Don't use ARIA if you can use native HTML instead.

**Good (semantic HTML):**
```html
<button>Click me</button>
```

**Bad (unnecessary ARIA):**
```html
<div role="button" tabindex="0">Click me</div>
```

### Common ARIA Roles

Use roles when semantic HTML doesn't exist.

**Landmark roles:**
```html
<div role="banner"> <!-- Header -->
<div role="navigation"> <!-- Nav -->
<div role="main"> <!-- Main -->
<div role="complementary"> <!-- Aside -->
<div role="contentinfo"> <!-- Footer -->
<div role="search"> <!-- Search region -->
```

**Widget roles:**
```html
<div role="button"> <!-- Interactive button -->
<div role="tab"> <!-- Tab in tablist -->
<div role="dialog"> <!-- Modal dialog -->
<div role="alert"> <!-- Important message -->
<div role="status"> <!-- Status message -->
<div role="progressbar"> <!-- Progress indicator -->
```

### ARIA States and Properties

**aria-label** - Provides accessible name:
```html
<button aria-label="Close dialog">
  <svg><!-- X icon --></svg>
</button>
```

**aria-labelledby** - References another element for name:
```html
<h2 id="dialog-title">Delete Account</h2>
<div role="dialog" aria-labelledby="dialog-title">
  <!-- Dialog content -->
</div>
```

**aria-describedby** - Provides description:
```html
<input
  type="password"
  aria-describedby="password-requirements"
/>
<div id="password-requirements">
  Must be at least 8 characters with one number.
</div>
```

**aria-expanded** - Indicates disclosure state:
```html
<button aria-expanded="false" aria-controls="menu">
  Menu
</button>
<div id="menu" hidden>
  <!-- Menu items -->
</div>
```

**aria-live** - Announces dynamic changes:
```html
<!-- Polite: Announces when user is idle -->
<div aria-live="polite" role="status">
  Item added to cart
</div>

<!-- Assertive: Announces immediately -->
<div aria-live="assertive" role="alert">
  Error: Payment failed
</div>
```

**aria-hidden** - Hides decorative elements:
```html
<span aria-hidden="true">🎉</span>
<span>Celebration!</span>
```

## Keyboard Accessibility

All functionality must be keyboard accessible.

### Focus Management

**Focus indicators:**
Must be visible and meet 3:1 contrast ratio (WCAG 2.2).

```css
/* Ensure visible focus */
:focus {
  outline: 2px solid #3B82F6;
  outline-offset: 2px;
}

/* Never remove focus without replacement */
:focus:not(:focus-visible) {
  outline: none; /* Only when focus-visible supported */
}

:focus-visible {
  outline: 2px solid #3B82F6;
  outline-offset: 2px;
}
```

**Tab order:**
Should follow visual order (left-to-right, top-to-bottom).

```html
<!-- Control tab order when necessary -->
<button tabindex="0">First (natural tab order)</button>
<button tabindex="-1">Not in tab order</button>
<button tabindex="1">Last (avoid positive tabindex)</button>
```

### Keyboard Patterns

**Common keyboard shortcuts:**
- **Tab**: Move focus forward
- **Shift + Tab**: Move focus backward
- **Enter/Space**: Activate buttons and links
- **Escape**: Close modals/dialogs
- **Arrow keys**: Navigate menus, tabs, lists
- **Home/End**: Jump to start/end

**Modal dialog keyboard pattern:**
```javascript
// Trap focus within modal
function trapFocus(modal) {
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    } else if (e.key === 'Escape') {
      closeModal();
    }
  });

  // Focus first element when modal opens
  firstElement.focus();
}
```

## Color and Contrast

### Contrast Ratios

**WCAG 2.2 requirements:**

| Content Type | Level AA | Level AAA |
|--------------|----------|-----------|
| Normal text (< 18px) | 4.5:1 | 7:1 |
| Large text (≥ 18px or ≥ 14px bold) | 3:1 | 4.5:1 |
| UI components | 3:1 | N/A |
| Graphics | 3:1 | N/A |

**Testing tools:**
- Chrome DevTools (built-in contrast checker)
- WebAIM Contrast Checker
- Stark (Figma plugin)

### Color Blindness

**Types of color blindness:**
- Protanopia (red-blind, ~1% of males)
- Deuteranopia (green-blind, ~1% of males)
- Tritanopia (blue-blind, <0.01%)
- Achromatopsia (total color blindness, rare)

**Design guidelines:**
- Don't rely on color alone to convey information
- Use patterns, icons, or text labels alongside color
- Test designs with color blindness simulators

**Example - accessible status indicators:**
```html
<!-- Bad: Color only -->
<span style="color: red">●</span> Error
<span style="color: green">●</span> Success

<!-- Good: Color + icon + text -->
<span style="color: red">
  <svg aria-hidden="true"><!-- X icon --></svg>
</span>
<span>Error</span>

<span style="color: green">
  <svg aria-hidden="true"><!-- Check icon --></svg>
</span>
<span>Success</span>
```

## Screen Reader Support

### Text Alternatives

**Images:**
```html
<!-- Informative image -->
<img src="chart.png" alt="Sales increased 25% in Q4" />

<!-- Decorative image -->
<img src="decorative.png" alt="" />

<!-- Complex image -->
<img src="infographic.png" alt="Summary description" longdesc="details.html" />
<a href="details.html">Full description</a>
```

**Icons:**
```html
<!-- Icon with visible text -->
<button>
  <svg aria-hidden="true"><!-- Icon --></svg>
  Delete
</button>

<!-- Icon without visible text -->
<button aria-label="Delete">
  <svg aria-hidden="true"><!-- Icon --></svg>
</button>
```

### Skip Links

Allow keyboard users to skip repetitive content.

```html
<a href="#main-content" class="skip-link">
  Skip to main content
</a>

<!-- Visually hidden until focused -->
<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
</style>
```

### Accessible Names

Every interactive element needs an accessible name.

**Naming hierarchy:**
1. `aria-labelledby` (references visible text)
2. `aria-label` (programmatic label)
3. Element content (button text)
4. `alt` attribute (images)
5. `title` attribute (last resort, not reliable)

## Common Component Patterns

### Modal Dialogs

**Accessibility requirements:**
- Focus trap (Tab cycles within modal)
- Escape key closes modal
- Focus returns to trigger element on close
- Backdrop click closes modal
- Proper ARIA attributes

```html
<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
>
  <h2 id="dialog-title">Confirm Delete</h2>
  <p id="dialog-desc">
    Are you sure you want to delete this item?
  </p>
  <button>Cancel</button>
  <button>Delete</button>
</div>
```

### Dropdown Menus

**Accessibility requirements:**
- Arrow keys navigate menu items
- Home/End jump to first/last item
- Typing filters/selects items
- Escape closes menu
- Proper ARIA attributes

```html
<button
  aria-haspopup="true"
  aria-expanded="false"
  aria-controls="menu-1"
>
  Options
</button>

<ul role="menu" id="menu-1" hidden>
  <li role="menuitem">
    <a href="/profile">Profile</a>
  </li>
  <li role="menuitem">
    <a href="/settings">Settings</a>
  </li>
  <li role="menuitem">
    <a href="/logout">Logout</a>
  </li>
</ul>
```

### Tabs

**Accessibility requirements:**
- Arrow keys navigate tabs
- Tab moves focus to active panel
- Proper ARIA attributes

```html
<div role="tablist" aria-label="Account settings">
  <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">
    Profile
  </button>
  <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2">
    Security
  </button>
</div>

<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  <!-- Profile content -->
</div>

<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  <!-- Security content -->
</div>
```

## Automated Testing

### Tools

**Browser extensions:**
- axe DevTools (most comprehensive)
- WAVE (WebAIM)
- Lighthouse (Chrome DevTools)

**Testing libraries:**
- jest-axe (unit tests)
- axe-playwright (E2E tests)
- pa11y (CI integration)

### Example: Playwright + axe

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('homepage should be accessible', async ({ page }) => {
  await page.goto('/');

  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'])
    .analyze();

  expect(accessibilityScanResults.violations).toEqual([]);
});
```

## Manual Testing Checklist

Automated tools catch ~30-40% of issues. Manual testing is essential.

**Keyboard testing:**
- [ ] Can reach all interactive elements with Tab
- [ ] Focus indicator is visible
- [ ] Tab order is logical
- [ ] No keyboard traps
- [ ] Can operate all functionality with keyboard only

**Screen reader testing:**
- [ ] All images have appropriate alt text
- [ ] Headings create logical outline
- [ ] Form inputs have labels
- [ ] Error messages are announced
- [ ] Dynamic content updates are announced

**Visual testing:**
- [ ] Text meets contrast requirements
- [ ] UI is usable at 200% zoom
- [ ] Information isn't conveyed by color alone
- [ ] Animations can be paused or disabled

**Screen reader recommendations:**
- NVDA (Windows, free)
- JAWS (Windows, commercial)
- VoiceOver (macOS/iOS, built-in)
- TalkBack (Android, built-in)

## Best Practices Summary

1. **Use semantic HTML** - Native elements have built-in accessibility
2. **Keyboard first** - Ensure full keyboard operability
3. **Provide text alternatives** - All non-text content needs text equivalents
4. **Sufficient contrast** - Meet WCAG 2.2 contrast requirements
5. **Clear focus indicators** - Visible and high contrast
6. **Logical tab order** - Follows visual layout
7. **Descriptive links** - "Learn more about pricing" not "Click here"
8. **Error prevention and recovery** - Clear errors with solutions
9. **Test with real users** - Include people with disabilities
10. **Automate testing** - Integrate axe into CI/CD pipeline

## Resources

**Guidelines and standards:**
- WCAG 2.2 (W3C)
- ARIA Authoring Practices Guide (W3C)
- Inclusive Design Principles

**Testing tools:**
- axe DevTools
- WAVE
- Lighthouse
- Color Contrast Analyzer

**Learning resources:**
- WebAIM
- A11y Project
- Deque University
