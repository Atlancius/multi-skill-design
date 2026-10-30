---
name: ui-ux-pro-max
description: "Picks a style, color palette, font pairing and landing pattern from a UI/UX database (Python CLI) and saves a design-system MASTER.md. Use when starting a site, landing page, dashboard or app that has no brand charter or design system yet."
---

# UI/UX Pro Max

`${CLAUDE_SKILL_DIR}` = this skill's directory (in Codex: the directory that contains this SKILL.md). Run every command from the project root.

## Precedence

Database results are suggestions; they never override the project:

1. Brand charter and project tokens. When the project has a brand charter, colors and fonts come from it: use this skill only for page pattern, layout and UX checks.
2. The project's own conventions (CLAUDE.md, AGENTS.md, rules files, existing components and tokens).
3. This database (snapshot of upstream v2.2.1). Some rows predate Tailwind v4 or modern stacks (the `Tailwind Config` column of `typography`, React Hook Form in `shadcn` rows): rules 1-2 win.

## Workflow

Copy and track:

```
- [ ] 1. Brief: product type, industry, style keywords, stack
- [ ] 2. Design system generated (and persisted for a multi-page project)
- [ ] 3. Gaps filled by domain and stack searches
- [ ] 4. Translated into project tokens
- [ ] 5. Implemented
- [ ] 6. Validation loop passed
```

**0. Prerequisite.** `python3 -I -c 'import sys; assert sys.version_info >= (3, 9)'`. If it fails, install Python 3 (macOS `brew install python3`, Debian/Ubuntu `sudo apt install python3`, Windows `winget install Python.Python.3.12`) and rerun. Standard library only, no pip package.

**1. Brief.** Extract product type (SaaS, e-commerce, portfolio, dashboard, landing...), industry (healthcare, fintech, gaming...), style keywords (minimal, playful, elegant, dark...) and stack. Specific keywords match better ("healthcare SaaS dashboard", not "app").

**2. Generate the design system (always first).**

```bash
python3 -I "${CLAUDE_SKILL_DIR}/scripts/search.py" "<product> <industry> <keywords>" --design-system -p "<Project Name>" [-f markdown]
```

Returns pattern, style, colors, typography, key effects and anti-patterns. No good match: retry with other keywords.

Multi-page project: persist it.

```bash
python3 -I "${CLAUDE_SKILL_DIR}/scripts/search.py" "<query>" --design-system --persist -p "<Project Name>" [--page "<page>"] [-o <dir>]
```

Writes `design-system/<project-slug>/MASTER.md` and, with `--page`, `pages/<page>.md`. Existing files are kept (they may hold manual edits); `--force` regenerates them. When building a page, read `MASTER.md`, then `pages/<page>.md` if it exists: page rules override Master.

**3. Fill gaps.**

```bash
python3 -I "${CLAUDE_SKILL_DIR}/scripts/search.py" "<keywords>" --domain <domain> [-n <max>]
python3 -I "${CLAUDE_SKILL_DIR}/scripts/search.py" "<keywords>" --stack <stack>
```

| Domain | Use for |
|---|---|
| `product` | Style and pattern by product type |
| `style` | UI styles, effects, implementation checklists |
| `typography` | Font pairings (Google Fonts) |
| `color` | Palettes by product type |
| `landing` | Section order, CTA placement |
| `chart` | Chart type and library by data shape |
| `ux` | Animation, z-index, accessibility, touch, forms (search it on every UI task) |
| `icons` | Icons with import code |

Stacks: `html-tailwind`, `react`, `nextjs`, `astro`, `vue`, `nuxtjs`, `nuxt-ui`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`, `jetpack-compose`. React and Next.js performance: Vercel's `react-best-practices` skill (github.com/vercel-labs/agent-skills); web interface guidelines: skill `audit-accessibility` (`--ui`).

**4. Translate into tokens.** Colors become primitive tokens in `@theme` and semantic tokens in `:root`, consumed as `bg-primary`, never as `bg-[#hex]`; fonts become `--font-*` loaded through `next/font` or self-hosted files, never `tailwind.config` nor the Google Fonts `@import` the CLI prints.

**5. Implement** with the project's components first.

**6. Validation loop.** Check, fix, check again; deliver only when everything passes:

- [ ] Every anti-pattern listed by the generated design system is absent.
- [ ] Same style, container width and icon set on every page; no emoji as icon.
- [ ] Hover feedback by color, opacity, shadow or border, without layout shift; `cursor-pointer` on clickable elements.
- [ ] Every mode the project ships (light, dark) checked: contrast, translucent surfaces, borders.
- [ ] Rendered at 320, 768, 1024 and 1440 px, then `audit-accessibility`.
- [ ] Charts: type matches the data shape, accessible palette, table alternative.

## Related skills

`frontend-design` (creative direction and implementation), `web-design-guidelines` (interface review), `animation-creator` (motion), `site-architect` (page structure), `brand-identity` (brand DNA before the design system).

Upstream: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT, [LICENSE](LICENSE)).
