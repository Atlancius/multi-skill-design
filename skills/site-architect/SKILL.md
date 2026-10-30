---
name: site-architect
description: "Plans a website's architecture from a brand identity: sitemap, page blueprints, design tokens, Atomic Design components, responsive and SEO/a11y structure for Next.js, Astro/HTML or Webflow. Use for “site architecture” or planning a new site."
argument-hint: "[brand guidelines or project path] [nextjs|tanstack|astro|webflow|html]"
---

# Site Architect

Paths: `${CLAUDE_SKILL_DIR}` = this skill's folder (Codex: the folder that contains this SKILL.md). Asking the user: `AskUserQuestion` (Claude) ↔ a question in the chat (Codex). Progress: `TodoWrite` (Claude) ↔ `update_plan` (Codex).

Produces the structural blueprint (information architecture, tokens, components, responsive, SEO/a11y) that designers and developers build from, derived from the brand's visual DNA. Chain: `brand-identity` (identity) → **site-architect** (structure) → `frontend-design` (visual direction) → implementation. No copy (placeholders only), no code files. Product framing of a new SaaS or app (problem, MVP, data, stack) is out of scope.

Contents: Before starting · Checklist · Phases 1–7 · Validation · Calibration examples.

## Before starting

- **Brand facts.** When the brand has a charter, its values win. Otherwise use the guidelines from `brand-identity`.
- **Missing inputs.** Ask for what is missing before Phase 1; minimum: colors, fonts, logo, site purpose, audience.
- **Stack.** Not given → ask before naming anything. Sensible default for a new project: brand or marketing site → Next.js; fully static showcase → Astro. Webflow only when the client works in Webflow.
- **Language.** Ask which languages the site ships in; multilingual changes the URL structure and the sitemap.

## Checklist

```
- [ ] 1. Brand DNA summary
- [ ] 2. Information architecture (sitemap, navigation, page blueprints)
- [ ] 3. Design token system
- [ ] 4. Component architecture
- [ ] 5. Responsive strategy
- [ ] 6. Stack naming conventions
- [ ] 7. Deliverable assembled from the template
- [ ] 8. Validation passed
```

## Phase 1 — Brand DNA

Extract from every input: logo (shapes, proportions, complexity), palette (exact HEX for primary, secondary, accent, neutrals), typography (families, weights, classification), tone, values, positioning, audience (demographics, devices), industry (B2B/B2C, competitor patterns). Summarize as the Brand DNA block of [references/output-template.md](references/output-template.md): style, temperature, density, shape language, type character, radius, elevation, spacing feel, and the sources used.

## Phase 2 — Information architecture

1. **Site type → sitemap template** ([references/component-architecture.md](references/component-architecture.md#5-architecture-de-linformation)):

| Site type | Template |
|-----------|----------|
| Showcase / corporate | Home, Services, Work, About, Blog, Contact, Legal |
| SaaS / product | Home, Product, Solutions, Pricing, Resources, Company, Login/Signup, Legal |
| Portfolio / freelance | Home, Projects, Services, About, Contact, Legal |
| Shop showcase | Home, Categories, Products, About, Blog, Contact, Legal |
| Landing page | One page: Hero, Problem, Solution, Features, Social proof, Pricing, CTA, FAQ |

2. **Navigation**: ≤ 7 primary items; main CTA as a distinct button; breadcrumbs beyond two levels; ≤ 3 URL levels; map primary, secondary, footer and contextual navigation.
3. **Page blueprints**: per page, ordered sections from the catalog (navigation, hero, content, social proof, conversion, specific), each justified by a brand goal or user need. Social proof only where real proof exists.

## Phase 3 — Design token system

Tokens are the bridge between brand and code; never skip them. Three levels: primitives (raw values) → semantic (usage) → component (only when needed). Categories: colors (bg, text, border, status), typography (families, sizes, weights, line heights), spacing (section, component, inline), elevation, radius (from the shape language), transitions (durations, easings), z-index (dropdown 1000, sticky 1100, overlay 1200, modal 1300, tooltip 1500). Implementation per stack: Tailwind v4 primitives in `@theme`, semantics in `:root`, `.dark` overrides; Webflow variables per Client-First. Every token traces to the brand palette, never to a framework default.

## Phase 4 — Component architecture

Atomic Design, listing only the components the sitemap needs:

- **Atoms**: buttons, inputs, icons, badges, tags, avatars, dividers, loaders actually used.
- **Molecules**: form field, search bar, nav item, media object, stat block, breadcrumb item.
- **Organisms**: the Phase 2 sections, each decomposed into molecules and atoms:

```
hero_component (organism)
├── hero_content
│   ├── Badge (atom) — optional label
│   ├── Heading (atom) — [H1: main value proposition]
│   ├── Paragraph (atom) — [P: supporting subheading]
│   └── Button Group (molecule) — primary + secondary CTA
└── hero_media
    └── Image / Video (atom)
```

- **Templates**: each page as an ordered sequence of organisms.

When a codebase already exists, mark each node REUSE (existing component) or NEW.

## Phase 5 — Responsive strategy

Breakpoints, grid, fluid scales and patterns: [references/responsive-design.md](references/responsive-design.md). Define breakpoints for the chosen stack (Tailwind mobile-first; Webflow desktop-first by construction), container widths, columns and gutters, a `clamp()` type scale with a `rem` term, then one behavior row per organism at desktop, tablet and mobile (layout change, visibility, navigation pattern, image art direction, type scaling). Visual checks run at 320, 768, 1024 and 1440px.

## Phase 6 — Stack conventions

- **Next.js or TanStack Start (React + Tailwind v4)**: `components/ui/`, `components/sections/`, `components/layouts/` (brand sites: `atoms/`, `molecules/`, `organisms/`); named exports, `cva` variants over semantic tokens.
- **Webflow**: Client-First ([references/client-first.md](references/client-first.md)): `_` folders for custom classes, core structure `page-wrapper → main-wrapper → section_[id] → padding-global + padding-section-[size] → container-[size]`, `is-` combo classes, utility classes for type, color and spacing, `rem` units.
- **HTML/CSS (Astro or static)**: BEM `.block__element--modifier`, tokens as custom properties on `:root`, one CSS file per component, mobile-first media queries; CUBE CSS (composition, utility, block, exception) when the project already uses it.

## Phase 7 — Deliverable

Fill [references/output-template.md](references/output-template.md) completely, with the SEO and accessibility structure from [references/seo-accessibility.md](references/seo-accessibility.md) (heading plan, landmark map, meta and JSON-LD per page type, a11y checklist). Write it to the project (default `docs/site-architecture.md`) or return it in the chat when there is no project; never into `ia/`.

## Validation

Check before delivering; fix and recheck any failing line:

- [ ] Brand alignment: every spacing, radius, elevation and color decision traces to the Brand DNA.
- [ ] Completeness: all seven template sections filled or marked `N/A — <reason>`.
- [ ] Token traceability: each semantic token references a primitive; each primitive comes from the brand.
- [ ] Contrast: text and UI token pairs meet WCAG AA (text 4.5:1, large text and UI 3:1), with computed ratios, never estimated.
- [ ] Responsive: every organism has a desktop, tablet and mobile behavior.
- [ ] SEO structure: one H1 per template, landmarks mapped, JSON-LD types eligible for rich results (schema.org).
- [ ] Stack accuracy: naming matches the chosen stack exactly.
- [ ] Actionability: a developer can start building without asking anything.
- [ ] No copy beyond bracketed placeholders, no code files, no invented proof.

## Calibration examples

- **Minimal SaaS** (Inter, deep blue on white, Next.js) → minimal, cool, airy, geometric, subtle shadows, 8px radius; SaaS template; blue scale + neutral grays; organisms around product previews, feature grids, pricing cards; Tailwind naming; LCP and code-splitting emphasized.
- **Bold local shop** (neon accent on dark, geometric sans headings, young audience, Webflow) → bold, dark, dense, energetic, 4–8px radius, prominent shadows; showcase template with one section per activity; dark primitives, neon accent kept for CTAs, high-contrast text; Client-First naming (`section_hero`, `hero_content`, `is-dark`); motion hooks noted per organism for `frontend-design`.
