---
name: design-handoff
description: "Generates a developer handoff spec from a design (Figma URL, screenshot or description): layout, tokens, component props, states, responsive, edge cases, motion, accessibility. Use for design handoff or a spec sheet for engineering."
argument-hint: "<Figma URL | screenshot | design description>"
---

# Design handoff

Path convention: `${CLAUDE_SKILL_DIR}` = this skill's folder (in Codex: the folder containing this SKILL.md). Figma tool names vary by runtime: find the Figma service (Claude Code: ToolSearch "figma"; Codex: `/mcp`), never a hardcoded tool name. Asking the user: AskUserQuestion (Claude Code) or a chat question (Codex).

Produces a spec a developer can implement without guessing. Opposite direction (implementing a design in code): `frontend-design`.

## Source

- Figma URL with a connected Figma service: read the targeted node (measurements, variables, components, states). No `node-id` in the URL: ask for the frame link.
- Screenshot or description: specify only what is visible or stated; list missing values under "To confirm" instead of inventing them.
- Tech stack unknown (e.g. React + Tailwind): ask, it shapes the implementation notes.

## What the spec covers

- **Visual**: exact measurements, token references (colors, type, spacing), component variants and states.
- **Interaction**: click/tap, hover, focus, transitions (duration, easing), gestures.
- **Content**: character limits, truncation, empty / loading / error states.
- **Edge cases**: min/max content, long or international text, slow connection, missing data.
- **Responsive**: what changes at each breakpoint.
- **Accessibility**: focus order, ARIA roles and labels, keyboard, screen-reader announcements.

## Principles

1. Nothing implicit: what is not specified will be guessed.
2. Tokens, not values: `spacing-md`, not `16px`.
3. Every state: default, hover, active, disabled, loading, error, empty.
4. Give the why when it drives a decision ("collapses on mobile: one-handed use").

## Output format

```markdown
## Handoff Spec: [Feature / screen]

### Overview
[What the screen does, user context]

### Layout
[Grid, breakpoints, responsive behavior]

### Design tokens used
| Token | Value | Usage |
|-------|-------|-------|

### Components
| Component | Variant | Props | Notes |
|-----------|---------|-------|-------|

### States and interactions
| Element | State | Behavior |
|---------|-------|----------|

### Responsive behavior
| Breakpoint | Changes |
|------------|---------|

### Edge cases
- Empty / long text / loading / error: [rendering]

### Animation / motion
| Element | Trigger | Animation | Duration | Easing |
|---------|---------|-----------|----------|--------|

### Accessibility notes
- Focus order, ARIA, keyboard

### To confirm
- [values absent from the source]
```

## Validation

Re-read the spec: every component has its states, no raw value where a token exists, every value comes from Figma or the user. Link the spec to a ticket in a connected issue tracker only if the user asks.
