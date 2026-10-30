---
name: ux-copy
description: "Writes or reviews interface microcopy: button and CTA labels, error messages, empty states, confirmation dialogs, tooltips, onboarding text. Not marketing copy (copywriting). Use on \"what should this button say?\", \"review this error message\"."
argument-hint: "<context or copy to review>"
---

# UX copy

Path convention: `${CLAUDE_SKILL_DIR}` = this skill's folder (in Codex: the folder containing this SKILL.md). This skill uses no runtime-specific tool. Questions to the user: AskUserQuestion (Claude Code) or a question in chat (Codex).

Microcopy inside the product. Conversion copy (landing pages, emails, ads, headlines) is out of scope.

## Inputs

Take them from the request or the screen; ask only for what is missing and changes the wording:

- Context: which screen, flow or feature.
- User state: what the user is trying to do, how they feel (blocked, anxious, done).
- Tone and constraints: character limits, platform guidelines, target language.
- Voice: when the product has a brand voice or style guide, follow it. Otherwise reuse the product's existing terms and tone.
- Design context: a Figma service (find it by description, never by a hardcoded tool name) can show the surrounding flow and layout limits.

## Principles

1. Clear: say exactly what happens; no jargon.
2. Concise: fewest words that keep the full meaning.
3. Consistent: one term per concept across the product.
4. Useful: every word helps the user finish their task.
5. Human: write as a helpful person, not as a system.

## Patterns

- **CTA**: start with a verb and name the outcome ("Start free trial", "Save changes"); "Create account", not "Submit".
- **Error**: what happened + why + how to fix. Example: "Payment declined. Your bank refused the card. Try another card or contact your bank." Never blame the user; never show codes or stack traces as the message.
- **Empty state**: what this place is + why it is empty + how to start. Example: "No projects yet. Create your first project to start collaborating."
- **Confirmation dialog**: state the action and its consequence ("Delete 3 files? This can't be undone."); label buttons with the actions ("Delete files" / "Keep files"), not "OK" / "Cancel".
- **Tooltip**: short, adds what the label does not say, never states the obvious.
- **Loading**: set expectations (what is happening, how long) to reduce anxiety.
- **Onboarding**: one concept per step, progressive disclosure.

Tone by moment: success celebratory but restrained; error empathetic and actionable; warning clear and actionable; neutral informative.

## Process

1. Fix context, user state, tone and limits.
2. Draft the recommended copy plus 2 alternatives that differ in tone.
3. Check: same term as elsewhere in the product, within the character limit, no ambiguous verb, every action button self-explanatory out of context.
4. When reviewing existing copy, quote each line, name the problem, give the rewrite.

## Output

```markdown
## UX copy: [context]

### Recommended copy
**[Element]**: [copy]

### Alternatives
| Option | Copy | Tone | Best for |
|--------|------|------|----------|
| A | | | |
| B | | | |

### Rationale
[Why it works: user state, clarity, action orientation]

### Localization notes
[Idioms to avoid, text expansion, cultural context]
```
