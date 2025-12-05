# UI Anti-Patterns

Common UI and UX mistakes to avoid when creating user interfaces, with examples and better alternatives.

## Accessibility Anti-Patterns

### 1. Using Color Alone to Convey Information

**Problem:**
Color-blind users cannot distinguish information conveyed only through color.

**Bad:**
```html
<span style="color: red;">Error</span>
<span style="color: green;">Success</span>
```

**Good:**
```html
<span class="error">
  <svg aria-hidden="true"><path d="..."/></svg> <!-- X icon -->
  Error
</span>
<span class="success">
  <svg aria-hidden="true"><path d="..."/></svg> <!-- Check icon -->
  Success
</span>
```

### 2. Missing Alt Text on Images

**Problem:**
Screen readers cannot describe images without alt text.

**Bad:**
```html
<img src="product.jpg">
<img src="chart.png" alt="chart">
```

**Good:**
```html
<!-- Informative image -->
<img src="product.jpg" alt="Blue wireless headphones with noise cancellation">

<!-- Complex image -->
<img src="chart.png" alt="Sales chart showing 25% increase in Q4">

<!-- Decorative image -->
<img src="decorative-pattern.jpg" alt="">
```

### 3. Insufficient Color Contrast

**Problem:**
Low contrast text is difficult to read, especially for visually impaired users.

**Bad:**
```css
/* Contrast ratio: 2.3:1 (fails WCAG AA) */
.text {
  color: #999999;
  background: #ffffff;
}
```

**Good:**
```css
/* Contrast ratio: 7.0:1 (passes WCAG AAA) */
.text {
  color: #333333;
  background: #ffffff;
}
```

### 4. Non-Keyboard Accessible Interactions

**Problem:**
Keyboard-only users cannot access functionality.

**Bad:**
```html
<div onclick="handleClick()">Click me</div>
```

**Good:**
```html
<button onclick="handleClick()">Click me</button>

<!-- Or if div is necessary -->
<div
  role="button"
  tabindex="0"
  onclick="handleClick()"
  onkeydown="(e) => e.key === 'Enter' && handleClick()"
>
  Click me
</div>
```

### 5. Removing Focus Indicators

**Problem:**
Keyboard users cannot see where focus is.

**Bad:**
```css
button:focus {
  outline: none; /* Never do this without alternative */
}
```

**Good:**
```css
button:focus-visible {
  outline: 2px solid #3B82F6;
  outline-offset: 2px;
}
```

## UX Anti-Patterns

### 6. Unclear Call-to-Action Buttons

**Problem:**
Generic button labels don't communicate what will happen.

**Bad:**
```html
<button>Click here</button>
<button>Submit</button>
<button>OK</button>
```

**Good:**
```html
<button>Download pricing guide</button>
<button>Create account</button>
<button>Save changes</button>
```

### 7. Hidden Navigation (Hamburger Menu on Desktop)

**Problem:**
Hiding primary navigation behind a menu icon on desktop reduces discoverability.

**Bad:**
```html
<!-- Desktop with hamburger menu -->
<header>
  <button class="hamburger">☰</button>
</header>
```

**Good:**
```html
<!-- Desktop with visible navigation -->
<header>
  <nav>
    <a href="/products">Products</a>
    <a href="/pricing">Pricing</a>
    <a href="/about">About</a>
  </nav>
  <!-- Hamburger only on mobile -->
</header>
```

### 8. Modal Dialogs That Can't Be Closed

**Problem:**
Users feel trapped when modals lack obvious close mechanisms.

**Bad:**
```html
<div class="modal">
  <h2>Subscribe to newsletter</h2>
  <form>
    <input type="email">
    <button>Subscribe</button>
    <!-- No way to close -->
  </form>
</div>
```

**Good:**
```html
<div class="modal">
  <button class="close" aria-label="Close dialog">×</button>
  <h2>Subscribe to newsletter</h2>
  <form>
    <input type="email">
    <button>Subscribe</button>
    <button type="button">No thanks</button>
  </form>
</div>
<!-- Also close on Escape key and backdrop click -->
```

### 9. Pagination Without Load More Option

**Problem:**
Users have to click through many pages for long content.

**Bad:**
```html
<!-- Only pagination -->
<div class="pagination">
  <button>1</button>
  <button>2</button>
  <button>3</button>
  <!-- ... -->
  <button>50</button>
</div>
```

**Good:**
```html
<!-- Infinite scroll or load more -->
<div class="content">
  <!-- Items -->
</div>
<button>Load more items</button>

<!-- Or hybrid approach -->
<div class="content">
  <!-- Items -->
</div>
<button>Load 20 more</button>
<div class="pagination">
  <button>Previous</button>
  <span>Page 1 of 50</span>
  <button>Next</button>
</div>
```

### 10. Auto-Playing Videos with Sound

**Problem:**
Unexpected sound is disruptive and accessibility issue.

**Bad:**
```html
<video autoplay>
  <source src="video.mp4">
</video>
```

**Good:**
```html
<video controls muted>
  <source src="video.mp4">
  <track kind="captions" src="captions.vtt">
</video>
```

## Form Anti-Patterns

### 11. Vague Error Messages

**Problem:**
Generic errors don't help users fix issues.

**Bad:**
```html
<span class="error">Invalid input</span>
<span class="error">Error</span>
```

**Good:**
```html
<span class="error">Email must include @ symbol</span>
<span class="error">Password must be at least 8 characters</span>
<span class="error">This username is already taken. Try username123</span>
```

### 12. Inputs Without Labels

**Problem:**
Users don't know what to enter; screen readers can't announce purpose.

**Bad:**
```html
<input type="text" placeholder="Enter email">
```

**Good:**
```html
<label for="email">Email address</label>
<input
  type="email"
  id="email"
  placeholder="you@example.com"
>
```

### 13. Clearing Form on Error

**Problem:**
Users have to re-enter all data after a single mistake.

**Bad:**
```javascript
function handleSubmit(formData) {
  if (hasErrors(formData)) {
    form.reset(); // Don't do this
    showError('Please fix errors');
  }
}
```

**Good:**
```javascript
function handleSubmit(formData) {
  if (hasErrors(formData)) {
    // Preserve user input
    showErrorsInline(errors);
    // Focus on first error
    firstErrorField.focus();
  }
}
```

### 14. Disabled Submit Button Before Validation

**Problem:**
Users don't know why they can't submit.

**Bad:**
```html
<form>
  <input type="email">
  <button disabled>Submit</button> <!-- Always disabled -->
</form>
```

**Good:**
```html
<form>
  <input type="email" required>
  <!-- Let them click, then show errors -->
  <button>Submit</button>
</form>

<!-- Or provide clear indication -->
<form>
  <input type="email" required>
  <button disabled>
    Submit (fill required fields first)
  </button>
</form>
```

## Design Anti-Patterns

### 15. Inconsistent Spacing

**Problem:**
Random spacing creates visual chaos.

**Bad:**
```css
.section-1 { margin-bottom: 17px; }
.section-2 { margin-bottom: 23px; }
.section-3 { margin-bottom: 31px; }
```

**Good:**
```css
/* Use spacing scale (8-point grid) */
.section-1 { margin-bottom: 16px; }
.section-2 { margin-bottom: 24px; }
.section-3 { margin-bottom: 32px; }
```

### 16. Too Many Font Styles

**Problem:**
Multiple fonts create inconsistent, unprofessional appearance.

**Bad:**
```css
h1 { font-family: 'Playfair', serif; }
h2 { font-family: 'Roboto', sans-serif; }
h3 { font-family: 'Courier', monospace; }
body { font-family: 'Comic Sans', cursive; }
```

**Good:**
```css
/* Limit to 1-2 font families */
h1, h2, h3 { font-family: 'Inter', sans-serif; }
body { font-family: 'Inter', sans-serif; }
```

### 17. No Visual Hierarchy

**Problem:**
Users can't scan content or identify importance.

**Bad:**
```html
<div>
  <p style="font-size: 14px">Heading</p>
  <p style="font-size: 14px">Subheading</p>
  <p style="font-size: 14px">Body text</p>
  <p style="font-size: 14px">Caption</p>
</div>
```

**Good:**
```html
<div>
  <h1 style="font-size: 32px; font-weight: 700">Heading</h1>
  <h2 style="font-size: 24px; font-weight: 600">Subheading</h2>
  <p style="font-size: 16px">Body text</p>
  <small style="font-size: 14px; color: #666">Caption</small>
</div>
```

### 18. Overusing Colors

**Problem:**
Rainbow interfaces are overwhelming and lack hierarchy.

**Bad:**
```css
.primary { background: #FF0000; }
.secondary { background: #00FF00; }
.tertiary { background: #0000FF; }
.quaternary { background: #FFFF00; }
.quinary { background: #FF00FF; }
```

**Good:**
```css
/* Limited, purposeful palette */
.primary { background: #3B82F6; } /* Blue */
.neutral { background: #6B7280; } /* Gray */
.success { background: #10B981; } /* Green */
.error { background: #EF4444; } /* Red */
```

### 19. Fixed Pixel Widths

**Problem:**
Breaks on different screen sizes.

**Bad:**
```css
.container {
  width: 1200px; /* Breaks on mobile */
}
```

**Good:**
```css
.container {
  width: 100%;
  max-width: 1200px;
  padding: 0 1rem;
  margin: 0 auto;
}
```

## Performance Anti-Patterns

### 20. Unoptimized Images

**Problem:**
Large images slow page load and waste bandwidth.

**Bad:**
```html
<img src="photo-5mb.jpg" width="300">
```

**Good:**
```html
<picture>
  <source
    srcset="photo-300.webp 300w, photo-600.webp 600w"
    type="image/webp"
  >
  <img
    src="photo-300.jpg"
    srcset="photo-300.jpg 300w, photo-600.jpg 600w"
    sizes="(max-width: 600px) 300px, 600px"
    alt="Description"
    loading="lazy"
  >
</picture>
```

### 21. Blocking JavaScript in Head

**Problem:**
Blocks page rendering while scripts download.

**Bad:**
```html
<head>
  <script src="large-bundle.js"></script>
</head>
```

**Good:**
```html
<head>
  <!-- Critical CSS only -->
  <style>/* Critical styles */</style>
</head>
<body>
  <!-- Content -->

  <!-- Scripts at end of body or with defer -->
  <script src="bundle.js" defer></script>
</body>
```

### 22. Not Using Lazy Loading

**Problem:**
Loading all content at once slows initial page load.

**Bad:**
```html
<img src="image1.jpg">
<img src="image2.jpg">
<!-- 50 more images -->
<img src="image50.jpg">
```

**Good:**
```html
<img src="image1.jpg"> <!-- Above fold, load immediately -->
<img src="image2.jpg" loading="lazy">
<img src="image3.jpg" loading="lazy">
<!-- More images with lazy loading -->
```

## Mobile Anti-Patterns

### 23. Tiny Touch Targets

**Problem:**
Small buttons are hard to tap accurately.

**Bad:**
```css
.button {
  padding: 2px 4px; /* Too small */
  font-size: 10px;
}
```

**Good:**
```css
.button {
  /* Minimum 44x44px touch target (iOS), 48x48px (Android) */
  min-height: 48px;
  min-width: 48px;
  padding: 12px 16px;
}
```

### 24. Horizontal Scrolling

**Problem:**
Users expect vertical scrolling; horizontal is unexpected and awkward.

**Bad:**
```css
.content {
  width: 2000px; /* Forces horizontal scroll on mobile */
  overflow-x: scroll;
}
```

**Good:**
```css
.content {
  width: 100%;
  /* Stack items vertically on mobile */
  display: flex;
  flex-direction: column;
}

@media (min-width: 768px) {
  .content {
    flex-direction: row; /* Horizontal on desktop */
  }
}
```

### 25. Fixed Positioning Covering Content

**Problem:**
Fixed headers/footers consume valuable mobile screen space.

**Bad:**
```css
.header {
  position: fixed;
  top: 0;
  height: 80px; /* Takes up 20% of small mobile screens */
}
```

**Good:**
```css
/* Smaller fixed header on mobile */
.header {
  position: fixed;
  top: 0;
  height: 56px;
}

@media (min-width: 768px) {
  .header {
    height: 80px; /* Larger on desktop */
  }
}

/* Or use sticky positioning */
.header {
  position: sticky;
  top: 0;
}
```

## Content Anti-Patterns

### 26. Lorem Ipsum in Production

**Problem:**
Placeholder text doesn't represent real content challenges.

**Bad:**
```html
<h1>Lorem ipsum dolor sit amet</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit...</p>
```

**Good:**
```html
<h1>Get started with our platform in minutes</h1>
<p>Sign up today and start building amazing products with our intuitive tools...</p>
```

### 27. Walls of Text

**Problem:**
Large text blocks are intimidating and hard to scan.

**Bad:**
```html
<p>
  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
  incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
  exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
  irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
  pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
  deserunt mollit anim id est laborum.
</p>
```

**Good:**
```html
<h2>Breaking content into sections</h2>

<p>Short, focused paragraphs are easier to read.</p>

<h3>Use headings to organize</h3>

<ul>
  <li>Bullet points for lists</li>
  <li>Improve scannability</li>
  <li>Make content digestible</li>
</ul>

<p>Add visual breaks between sections.</p>
```

### 28. CAPTCHA on Every Form

**Problem:**
CAPTCHAs frustrate users and create accessibility barriers.

**Bad:**
```html
<form>
  <input type="email">
  <div class="captcha">Solve: 7 + 3 = ?</div>
  <button>Sign up</button>
</form>
```

**Good:**
```html
<form>
  <input type="email">
  <!-- Use honeypot or invisible reCAPTCHA -->
  <input type="text" name="website" style="display:none" tabindex="-1" autocomplete="off">
  <button>Sign up</button>
</form>
```

## Animation Anti-Patterns

### 29. Excessive Animation

**Problem:**
Too much motion is distracting and can cause motion sickness.

**Bad:**
```css
.everything {
  transition: all 0.5s ease-in-out;
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}
```

**Good:**
```css
/* Subtle, purposeful animations */
.button {
  transition: background-color 0.2s ease;
}

.button:hover {
  background-color: #2563EB;
}

/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 30. Slow Animations

**Problem:**
Long animations make the UI feel sluggish.

**Bad:**
```css
.modal {
  transition: all 1.5s ease-in-out; /* Too slow */
}
```

**Good:**
```css
.modal {
  transition: all 0.2s ease-out; /* Snappy */
}
```

## Best Practices Summary

**Do:**
- Use semantic HTML
- Ensure keyboard accessibility
- Maintain sufficient color contrast
- Provide clear feedback
- Design mobile-first
- Optimize images and assets
- Use consistent spacing and typography
- Test with real users
- Include proper alt text and labels
- Make error messages helpful

**Don't:**
- Remove focus indicators
- Use color alone to convey information
- Auto-play videos with sound
- Create tiny touch targets
- Block page rendering with scripts
- Use vague button labels
- Disable submit buttons without explanation
- Create walls of text
- Overuse animations
- Ignore accessibility guidelines

## Testing for Anti-Patterns

**Automated checks:**
- Lighthouse (accessibility, performance)
- axe DevTools (accessibility)
- ESLint with a11y plugins
- Bundlesize (performance budgets)

**Manual checks:**
- Keyboard-only navigation
- Screen reader testing (NVDA, VoiceOver)
- Mobile device testing
- Color blindness simulator
- Slow network testing
- User testing sessions

By avoiding these anti-patterns, you'll create more accessible, performant, and user-friendly interfaces that serve all users effectively.
