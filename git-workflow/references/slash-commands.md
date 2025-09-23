# Slash Commands Reference

Detailed workflows for each slash command.

## /commit - Smart Commit Helper

**Trigger:** User types `/commit` or says "help me commit"

**Smart Workflow (Adaptive):**

### Stage 1: Detection
Check for staged changes:
```bash
git diff --staged --name-only
```

### Stage 2: Path Selection

**If staged changes exist → Smart Analysis Path**

1. **Run analysis:**
   ```bash
   python scripts/analyze-diff.py --json
   ```

2. **Present suggestion:**
   ```
   📊 Analyzed your staged changes:
   
   Files changed: 3
    auth/oauth.py   | 45 +++++++++++++++
    auth/tokens.py  | 23 ++++++++
    tests/auth.py   | 67 ++++++++++++++++++++++
   
   Detected:
   • Type: feat (new functions found)
   • Scope: auth (from file paths)
   • Description: add OAuth2 authentication
   • Confidence: High (85%)
   
   Suggested commit:
   git commit -m"feat(auth): add OAuth2 authentication"
   
   Does this look good? (y/n/edit/help)
   ```

3. **Handle response:**
   - **`y` or "yes" or "looks good"** → Provide final command or execute
   - **`n` or "no"** → Ask "What should I change?" then rebuild
   - **`edit`** → Let them modify specific parts (type, scope, description)
   - **`help`** → Explain why each part was suggested
   - **Low confidence (<50%)** → Add warning: "⚠️ Low confidence. Would you like to build it step-by-step instead?"

**If no staged changes → Interactive Builder Path**

1. **Inform user:**
   ```
   No staged changes found.
   
   Tip: Stage your changes first with:
     git add <files>
   
   Or I can help you build the message. What did you change?
   ```

2. **Get description:**
   - Wait for user to describe their change
   - If they want to stage first, guide them

3. **Build interactively:**
   - Suggest type based on description
   - Ask for scope (optional)
   - Check breaking change
   - Refine description
   - Add body if needed
   - Add footer if needed

4. **Present final:**
   ```
   Your commit message:
   
   feat(auth): add OAuth2 login
   
   Git command:
   git commit -m"feat(auth): add OAuth2 login"
   ```

**If user provided description in request → Manual Path**

Example: "help me commit - I added OAuth login"

1. **Extract information:**
   - What they did: "added OAuth login"
   - Infer type: feat (adding something new)
   - Suggest scope: auth (OAuth is authentication)

2. **Build message:**
   ```
   Based on your description:
   
   git commit -m"feat(auth): add OAuth login"
   
   Want me to add more details? (y/n)
   ```

3. **Offer refinement:**
   - If yes: ask about body, footer
   - If no: done

### Key Principles

1. **Be smart:** Use automation when possible
2. **Be flexible:** Fall back to interactive when needed
3. **Be clear:** Always show what was detected and why
4. **Be helpful:** Offer next steps at each stage

## /analyze - REMOVED

**Note:** This command has been merged into `/commit`. The smart analysis is now the default first step when using `/commit` with staged changes.

Users can still trigger it by:
- Typing `/commit`
- Saying "help me commit"
- Saying "analyze my changes"

## /validate - Message Validation

**Trigger:** User types `/validate <message>` or "Is this valid: ..."

**Workflow:**
1. Extract message (after `/validate` or from context)
2. Run validation checks:
   - Format: matches `type(scope): description` pattern
   - Type: in approved list
   - Scope: valid format if present
   - Description: lowercase, no period, under 100 chars
   - Breaking change: indicator matches footer
3. Present results:
   
   **If valid:**
   ```
   ✅ Valid commit message!
   
   Type: feat
   Scope: auth
   Description: add OAuth login
   ```
   
   **If invalid:**
   ```
   ❌ Invalid commit message
   
   Issues:
   • Description starts with uppercase (should be lowercase)
   • Description ends with period (should not)
   
   Suggested fix:
   feat(auth): add OAuth login
   
   Original:
   feat(auth): Add OAuth login.
   ```

## /types - Show Commit Types

**Trigger:** User types `/types` or asks "what commit types..."

**Response:**
```
📝 Conventional Commit Types:

🆕 feat - New feature for users/API
   Example: feat(auth): add OAuth login

🐛 fix - Bug fix for users/API  
   Example: fix(api): prevent null pointer

♻️  refactor - Code change without behavior change
   Example: refactor(auth): extract validation logic

⚡ perf - Performance improvement
   Example: perf(db): add index to user queries

💄 style - Code formatting only
   Example: style: apply prettier formatting

✅ test - Add or fix tests
   Example: test(auth): add OAuth flow tests

📚 docs - Documentation changes
   Example: docs: update API reference

📦 build - Build system or dependencies
   Example: build: upgrade to React 18

🔧 ops - Infrastructure or deployment
   Example: ops(k8s): increase replica count

🏗️  chore - Miscellaneous maintenance
   Example: chore: update .gitignore

Need help choosing? Describe your change and I'll suggest the right type.
```

## /scopes - Scope Guide

**Trigger:** User types `/scopes` or asks about scopes

**Response:**
```
📍 Scopes in Conventional Commits

A scope provides context about what part of the codebase changed.

**Format:**
- Optional (can omit)
- Lowercase
- Alphanumeric + hyphens
- 1-20 characters
- Based on your project structure

**Common patterns:**

By module/component:
  feat(auth): ...
  fix(api): ...
  refactor(database): ...
  
By feature area:
  feat(payments): ...
  fix(checkout): ...
  
By technical layer:
  refactor(ui): ...
  perf(backend): ...

**Examples:**
  ✅ feat(auth): add login
  ✅ fix(shopping-cart): prevent empty checkout
  ✅ refactor(api-v2): restructure endpoints
  
  ❌ feat(#123): add feature  (don't use issue numbers)
  ❌ feat(AUTHENTICATION): ... (not uppercase)
  ❌ feat(this-is-way-too-long-scope): ... (max 20 chars)

**Your project:**
Based on your file structure, consider scopes like:
[analyze their repo structure and suggest relevant scopes]
```

## /breaking - Breaking Change Guide

**Trigger:** User types `/breaking` or mentions breaking changes

**Response:**
```
⚠️  Breaking Changes Guide

A breaking change is any modification that requires users to change their code.

**When to mark as breaking:**
• Removed public API endpoints
• Changed function signatures
• Modified response formats
• Removed configuration options
• Changed database schema
• Updated minimum version requirements

**How to mark breaking changes:**

1. Add `!` before the colon:
   feat(api)!: remove deprecated endpoints

2. Add BREAKING CHANGE in footer:
   
   feat(api)!: remove deprecated v1 endpoints
   
   BREAKING CHANGE:
   
   All v1 API endpoints have been removed. Clients must
   migrate to v2 API with updated authentication.
   
   Migration guide: docs/v1-to-v2-migration.md

**Template:**
```
<type>(<scope>)!: <description>

<optional body explaining the change>

BREAKING CHANGE:

What broke: <explain what no longer works>
Why: <reason for the breaking change>
Migration: <how to update code>
```

**Example:**
```
refactor(auth)!: change token format to JWT

Replace custom token format with industry-standard JWT
for better security and third-party integration.

BREAKING CHANGE:

Auth tokens are now JWT format instead of custom base64.

Migration steps:
1. Update token parsing: use jwt.decode() instead of base64
2. Update token validation: verify JWT signature
3. Existing tokens will be invalidated - users must re-login

See: docs/jwt-migration.md
```

**Version impact:**
Breaking changes trigger a MAJOR version bump (1.x.x → 2.0.0)
```

## /changelog - Generate Changelog

**Trigger:** User types `/changelog` or asks to generate changelog

**Workflow:**
1. Get version info: "From which version/tag? (default: last tag)"
2. Run git log: `git log <version>..HEAD --format=%s`
3. Parse conventional commits
4. Group by type:
   - Breaking Changes (top priority)
   - Features
   - Bug Fixes
   - Other (refactor, perf, docs, etc.)
5. Format as markdown:
   ```markdown
   ## [2.0.0] - 2025-11-15
   
   ### ⚠️ BREAKING CHANGES
   
   - **auth**: change token format to JWT (#234)
     Migration required. See docs/jwt-migration.md
   
   ### ✨ Features
   
   - **auth**: add OAuth2 login (#123)
   - **api**: add user search endpoint (#145)
   - **ui**: add dark mode toggle (#167)
   
   ### 🐛 Bug Fixes
   
   - **api**: prevent null pointer in user lookup (#156)
   - **ui**: fix date picker timezone issue (#178)
   
   ### ⚡ Performance
   
   - **database**: add index to user queries (#189)
   
   ### 📚 Documentation
   
   - update API reference (#190)
   - add authentication guide (#191)
   ```

## /version - Semantic Versioning

**Trigger:** User types `/version` or asks "what should the next version be"

**Workflow:**
1. Get current version: `git describe --tags --abbrev=0` or ask user
2. Analyze commits since that version
3. Apply semantic versioning rules:
   - **Major** (X.0.0): Has breaking changes
   - **Minor** (0.X.0): Has features or fixes, no breaking changes
   - **Patch** (0.0.X): Only other changes
4. Present analysis:
   ```
   📊 Version Analysis
   
   Current version: 1.2.3
   Analyzing commits since v1.2.3...
   
   Found:
   • 1 breaking change
   • 5 features
   • 3 bug fixes
   • 7 other commits
   
   Recommended: 2.0.0 (Major)
   Reason: Breaking change detected
   
   Breaking commits:
   • feat(api)!: remove deprecated v1 endpoints
   
   Create this version?
   git tag -a v2.0.0 -m "Release 2.0.0"
   git push origin v2.0.0
   ```

## /examples - Show Examples

**Trigger:** User types `/examples` or asks for examples

**Response:**
Load and display relevant examples from references/examples.md based on context:
- If discussing features → show feature examples
- If discussing fixes → show fix examples
- If discussing breaking changes → show breaking change examples
- Default → show variety of examples

## /fix - Amend Last Commit

**Trigger:** User types `/fix` or "I need to fix my last commit"

**Workflow:**
1. Get last commit: `git log -1 --format=%s`
2. Show current message: "Your last commit: `feat: add login`"
3. Ask: "What needs fixing?"
4. Common scenarios:
   
   **Wrong message:**
   ```
   Current: feat: add login
   New message: feat(auth): add OAuth login
   
   Command:
   git commit --amend -m"feat(auth): add OAuth login"
   ```
   
   **Forgot files:**
   ```
   Stage missing files:
   git add forgotten-file.py
   git commit --amend --no-edit
   ```
   
   **Older commit:**
   ```
   To fix an older commit, use interactive rebase:
   git rebase -i HEAD~3
   
   Then mark the commit as 'edit' or 'reword'
   ```

## General Response Pattern

For all slash commands:
1. Acknowledge the command
2. Execute the workflow
3. Present clear, actionable output
4. Offer next steps
5. Be concise but complete
