---
name: brand-identity
description: "Derives a brand identity system from a logo (palette, typography, component tokens, voice, guidelines doc) or audits existing branding against it. Use for “branding from this logo”, a brand style guide or brand tokens."
argument-hint: "<logo file or URL> [--audit]"
---

# Meta Branding Creator

Paths: `${CLAUDE_SKILL_DIR}` = this skill's folder (Codex: the folder that contains this SKILL.md). Asking the user: `AskUserQuestion` (Claude) ↔ a question in the chat (Codex). Progress: `TodoWrite` (Claude) ↔ `update_plan` (Codex).

Derives a production-ready identity system from one logo: every color, font, radius and voice trait traces back to the logo. This skill writes the system and its spec, not the asset files (logo variants, favicons, app icons). No logo yet → `ui-ux-pro-max` proposes a starting design system. Next in the chain: `site-architect` (site structure), then `frontend-design` (visual direction of pages).

Contents: Before starting · Checklist · Phases 1–7 · Audit mode · Final validation.

## Before starting

- **Existing charter.** When the brand already has a charter or style guide, read it first. Charter values (HEX, fonts, logo rules, voice) win over anything derived here: derive only what the charter lacks and flag each divergence instead of overriding it. Brand or register unclear → ask. One deliverable = one brand.
- **Output location.** Deliverables go to the target project (tokens in its global CSS, guidelines in its docs). A change to an existing charter is proposed to its owner, never applied silently.
- **Logo quality.** Unreadable or low-resolution logo → ask for a better file (SVG preferred) before Phase 1.

## Checklist

Copy it into the plan and tick as you go:

```
- [ ] 1. Logo analysis validated by the user (gate)
- [ ] 2. Color system — contrast report: 0 FAIL, light and dark
- [ ] 3. Typography system (licenses noted)
- [ ] 4. Component tokens
- [ ] 5. Brand applications
- [ ] 6. Brand voice
- [ ] 7. Guidelines doc + token files written
- [ ] 8. Final validation passed
```

## Phase 1 — Logo analysis

Read the logo image and extract:

- **Shape language**: geometry — circles (community, protection), squares (stability, trust), triangles (innovation, power), organic (growth, creativity); corners — rounded (friendly), sharp (precise), mixed (sophisticated); line weight — thin (elegant) vs thick (bold); symmetry — symmetric (balanced) vs asymmetric (dynamic).
- **Colors**: every HEX value; primary (largest area or most prominent); secondaries; warmth; saturation.
- **Typography** (wordmark): serif / sans / script / display / custom; weight; geometric vs humanist vs grotesque; spacing.
- **Personality** on five spectrums: Playful ↔ Serious, Modern ↔ Classic, Minimal ↔ Complex, Warm ↔ Cool, Bold ↔ Subtle.

**Gate:** present the findings and get the personality assessment validated before generating anything else.

## Phase 2 — Color system

Derive the palette from the logo colors ([references/color-system.md](references/color-system.md)):

| Role | Count | Derivation |
|------|-------|-----------|
| Primary | 10 shades (50–900) | Logo's dominant color, kept unchanged at its step |
| Secondary | 10 shades | ±15–30° hue shift from primary, or the logo's second color |
| Accent | 10 shades | Complementary or high-contrast pick |
| Neutral | 10 shades | Primary hue, very low chroma |
| Semantic | 4 | Success, warning, error, info, tuned to the palette |

Distribution 60-30-10: 60% neutral surfaces, 30% primary structure, 10% accent (CTAs, highlights).

**Validation loop (mandatory):** list every text/background, button label/button, icon/surface and focus-ring/surface pair, in light and dark, with the WCAG ratio of each: computed from relative luminance (a throwaway `node -e` or `python3 -c` calculation, or the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)), never estimated by eye. Thresholds: text 4.5:1, large text and UI 3:1, unrounded ([references/color-system.md](references/color-system.md#wcag-contrast)). A failing pair: move the token one or two steps along its scale (never change the logo color itself), recompute, and continue only at 0 FAIL. A logo color that cannot reach the threshold as text stays decorative and gets a darker sibling for text.

**Deliver:** HEX table (OKLCH too if the project uses it), CSS tokens (Tailwind v4: primitives in `@theme`, semantics in `:root`, `.dark` overrides), the contrast report.

## Phase 3 — Typography system

Match fonts to the logo personality ([references/typography-system.md](references/typography-system.md)). At most three: **Display** (headlines, carries the logo's character), **Body** (paragraphs and UI, highly legible), **Mono** (only for a technical brand).

| Element | Size | Weight | Line height | Letter spacing |
|---------|------|--------|-------------|----------------|
| H1 | `clamp(2rem, 1.25rem + 3vw, 3.5rem)` | 700 | 1.1 | −0.02em |
| H2 | `clamp(1.5rem, 1.1rem + 2vw, 2.5rem)` | 600 | 1.2 | −0.01em |
| H3 | `clamp(1.25rem, 1rem + 1.25vw, 1.75rem)` | 600 | 1.3 | 0 |
| Body | `clamp(1rem, 0.95rem + 0.25vw, 1.125rem)` | 400 | 1.5 | 0 |
| Small | `0.875rem` | 400 | 1.4 | 0.01em |
| Caption | `0.75rem` | 500 | 1.3 | 0.02em |

**Deliver:** families with license and self-hosted loading (`next/font` in Next.js), fallback stacks, the type scale as tokens. Flag any font that needs a paid license.

## Phase 4 — Component tokens

Derive from the logo shape language ([references/component-system.md](references/component-system.md)):

- **Radius** from the logo corners: rounded → base 12px; sharp → 4px; mixed → 8px; plus `full` for pills.
- **Spacing**: 4px-based scale `4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96`.
- **Elevation**: five levels, softer for friendly brands, crisper for professional ones.
- **Specs** for buttons (primary, secondary, ghost — every state), cards (standard, image, featured), inputs (text, select, checkbox, radio, error), icons (Lucide by default, stroke matched to the logo weight), motion personality (easing and durations; reduced motion always honored).

## Phase 5 — Brand applications

- **Website**: header and navigation, hero, card grid, footer, dark mode direction (the page design itself belongs to `site-architect` and `frontend-design`).
- **Social**: feed post, story, LinkedIn post, profile picture and banner ([references/component-system.md](references/component-system.md#social-media-templates)).
- **Photography**: lighting, temperature, saturation, composition, post-processing values ([references/brand-guidelines.md](references/brand-guidelines.md#photography-style-guide)).

## Phase 6 — Brand voice

Brand with an existing voice guide → reuse it, derive nothing. New brand → map the logo personality to 4–5 traits (playful shapes → conversational, witty; sharp geometry → precise, authoritative; organic forms → warm, empathetic; bold colors → confident, direct). **Deliver:** trait matrix (trait → do → don't), tone by context, vocabulary to use and avoid. Copy written in this voice: `copywriting`.

## Phase 7 — Guidelines document

Compile ([references/brand-guidelines.md](references/brand-guidelines.md)):

```
1. Brand story (logo meaning, personality)
2. Logo usage (clear space, minimum size, variations, do's & don'ts)
3. Color palette (HEX, RGB, HSL, OKLCH + usage rules + contrast report)
4. Typography (families, licenses, scale, CSS)
5. Component system (radius, shadows, spacing, buttons, cards, inputs, icons, motion)
6. Photography & imagery
7. Brand voice
8. Social media templates
9. Design tokens (CSS file + JSON in the W3C DTCG format)
```

Logo defaults when the logo has no rules: clear space ≥ 0.5 × logo height; minimum width 190px web, 38mm print; variations full color, monochrome black, monochrome white, greyscale.

## Audit mode (`--audit`)

Run Phase 1, then compare the existing site, components and assets with the extracted DNA: colors (exact values and computed contrast), fonts, radius, shadows, voice. Score each category ([references/brand-guidelines.md](references/brand-guidelines.md#brand-audit-method)) and deliver a gap report: file or URL, current value, expected value, exact fix, ranked by severity. Read-only unless the user asks for the fixes.

## Final validation

Before delivering, all must hold; otherwise fix and recheck:

- [ ] Every color traces to the logo or the charter; the logo color appears unchanged in its scale.
- [ ] The contrast report shows 0 FAIL for light and dark, with the computed ratio of each pair.
- [ ] Light and dark variants delivered.
- [ ] Every font has its license and loading method; paid fonts flagged.
- [ ] Token files parse (CSS loads, JSON valid) and use the same names as the guidelines.
- [ ] One brand, one register; no brand fact written into `ia/`.
