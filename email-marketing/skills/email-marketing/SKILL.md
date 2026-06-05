---
name: email-marketing
description: >-
  Email content writing for newsletters, drip sequences, onboarding flows, and transactional emails. Use for newsletter drafting, automated drip sequence copy, welcome email series, subject line and preview text optimisation, re-engagement emails, and plain-language transactional email (receipts, confirmations, alerts). Trigger phrases: "write a newsletter", "draft an onboarding email sequence", "write a subject line", "write a drip campaign", "create a welcome email". NOT for email infrastructure setup (ESP config, sending domains, DKIM/DMARC) — that is a technical ops concern. NOT for social media content — use the social-media-content skill for LinkedIn or Twitter. NOT for cold outreach / sales prospecting emails — those have compliance and conversion constraints beyond marketing content.
allowed-tools: Read,Write,Edit,Bash
---

# email-marketing

Email newsletters, drip sequences, subject line optimisation, onboarding emails, and plain-language transactional email copy.

## When to use

- Write a 5-email onboarding sequence for new SaaS trial users
- Write a monthly product newsletter for our developer tool
- Suggest 5 subject line variants for our product launch email
- Write a re-engagement email for users who haven't logged in for 30 days
- Draft the welcome email for new subscribers to our blog
- Write a plain-language payment failed email that doesn't alarm users
- Create a 3-email abandoned cart sequence for our e-commerce store
- Write preview text for 10 emails in our nurture sequence

## When NOT to use

- Configure SPF and DKIM for our SendGrid sending domain — Email infrastructure — not content
- Write a cold outreach sequence to VPs of Engineering at Series A companies — Sales prospecting — different constraints
- Write a Twitter thread about our email marketing strategy — Social content — use social-media-content skill
- Set up a Mailchimp automation workflow — ESP platform config — not copy

## Anti-patterns

### Symptom
Invoking this skill for tasks outside its scope — e.g., infrastructure concerns when the request is about application code, or vice versa.

### Problem
Scope mismatch wastes context and produces advice tuned for the wrong domain. A database schema skill answering a connection-pooling question gives schema advice when the real problem is operational configuration.

### Solution
Read the NOT for clauses carefully. If the request matches an exclusion, identify the correct skill (check SkillStack for the right domain) rather than stretching this skill to cover adjacent ground.
