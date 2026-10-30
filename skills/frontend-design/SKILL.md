---
name: frontend-design
description: Designs new or restyled web UI (pages, landing pages, dashboards, components, posters) with a distinctive direction in type, color, layout and copy that avoids templated AI defaults. Not for non-visual code or polishing existing UI.
license: Complete terms in LICENSE.txt
---

# Frontend Design

Paths: `${CLAUDE_SKILL_DIR}` = this skill's folder (Codex: the folder that contains this SKILL.md); it bundles only `LICENSE.txt` and `NOTICE`. The last section, House rules, applies on top of the upstream guidance.

Approach this as the design lead at a design studio known for giving every client a distinct visual identity that is not mistaken for anyone else's. This client has already rejected proposals that felt cliché or templated, and is paying for a distinctive point of view: make deliberate, opinionated choices about palette, typography, and layout that are specific to this brief, and take aesthetic risk if justified.

## Ground your designs in the subject matter

If the brief does not identify what the product or subject matter is, identify it yourself before designing, and confirm with the client. You can come up with one concrete subject, the design's audience, and the design's primary job, as a proposal. If there's any information in your memory about the client's preferences or context about what they're building, use that as a hint. The subject's industry, subject matter, materials, and vernacular are where distinctive visual choices come from — a design for a toy for girls aged 8–11 will be very aesthetically different from a dashboard for financial analysts. Build with the brief's real content and subject matter throughout.

## Read the brief, pick the foundation

State one line before designing: "Reading this as: <page kind> for <audience>, <vibe>, leaning toward <system or aesthetic>." Audience, quiet constraints (public sector, regulated, kids, accessibility-first) and existing brand assets outrank taste. Ask one question, only when the read genuinely forks; otherwise proceed.

When the brief names a real design system, install its official package and do not rewrite its CSS or override most of its tokens. One system per project; the project's own system (for example shadcn/ui already installed) wins over any row below.

Packages: Fluent (`@fluentui/react-components`), Material (`@material/web`), Carbon (`@carbon/react`), Primer (`@primer/react-brand`), Atlaskit (`@atlaskit/tokens`), GOV.UK (`govuk-frontend`), USWDS (`@uswds/uswds`), Radix (`@radix-ui/themes`).

An aesthetic (glass, bento, brutalist, editorial, aurora) has no official package: build it with native CSS and say it is an approximation. There is no official web Liquid Glass.

## Design principles

For web designs, the hero is the first thing viewers will see. Open with the most characteristic thing in the subject's world, in the form that is most appropriate: a headline, an image, an animation, a live demo, an interactive moment, or other treatments. A big number with a small label, stats and a gradient accent is the default treatment: use it only if truly best.

Hero discipline: headline on 2 lines at most, short subtext, one primary CTA (plus at most one secondary) visible without scrolling. Trust logos, pricing teasers and feature lists go in the section below, not in the hero. One intent = one CTA label across the page ("Get in touch" and "Let's talk" together is a duplicate).

Consistency locks: one accent color used the same way everywhere, one corner-radius system, one theme per page (no section flipping to inverted mode).

Typography carries the personality of the page. You don't need a different typeface for display or headline text and body content: use one family or two, and if two, make them clearly distinct.

Choose typefaces deliberately, not the families you reach for on every project, and set a clear type scale following the default guidance of The Elements of Typographic Style with intentional weights, widths, and spacing. When type is used as a headline or visual element, use the type treatment itself as an active part of the design, not a neutral delivery vehicle for the content.

Default to line lengths of less than 80 characters. Serif typefaces can have slightly longer line lengths; give serif body text slightly more line-height than a sans-serif.

Avoid these default typographic treatments; they are the commonest tells of a generated page:
- Accenting just a single word or phrase in a headline, like putting one word in italic/bold or a different color.
- Using all caps for labels.
- Adding unnecessary typographic labels above content.

Visual structure is information. Structural devices like outlines, borders, numbering, eyebrows, dividers, labels, etc., encode useful information about the content rather than decorate it. Many generic designs use numbered markers (01 / 02 / 03), but that's only appropriate if the content actually is a sequence — like a stepped process or a timeline. Before adding numbered markers, check the content really is a sequence.

Use non-user-triggered motion sparingly and deliberately, only to draw attention. A single orchestrated moment — one page-load sequence or one reveal — lands better than scattered effects; fade-and-slide-up entrances on each section and hover transitions on every card are the generic default and read as AI-generated. Motion that answers a person's action (opening, expanding, confirming) is welcome when it shows what changed.

Placeholder content must be credible: realistic locale-appropriate names, non-round figures (47.2%, not 50%), brand names that sound real (not Acme or Nexus), varied dates; no generic avatars. Consider written content carefully. Copy can make a design feel as templated as the layout: see the writing section below.

## Process: plan, review against the brief, build, critique

For calibration, AI-generated design right now clusters around some traits:
1. a warm cream background (near #F4F1EA) with a high-contrast serif display and a terracotta or warm-clay accent (often near #D97757 — Anthropic's own Claude-interaction accent, so on a user's brief it reads as a tell);
2. a near-black background with a single bright acid-green or vermilion accent;
3. a broadsheet-style layout with hairline rules, zero border-radius, and dense newspaper-like columns;
4. the SaaS-card kit: content chopped into identical rounded cards, one border-radius on everything regardless of hierarchy, the same soft grey shadow (rgba(0,0,0,.1)) under each, and gradient washes as decoration;
5. template chrome that appears whatever the subject: a tracked-out ALL-CAPS eyebrow label above every heading; meta strings joined with middle dots ('A · B · C'); labels built as 'WORD — fragment' with a spaced em dash; tinted near-black (#0B0B0B, #111) standing in for black; a monospace face for small data labels; a '→' appended to link and button text.

All traits are legitimate for some briefs, but they are defaults rather than choices, and they appear regardless of subject. Where the brief pins down a visual direction, follow it exactly — the brief's own words always win, including when it asks for one of these looks. Where it leaves an axis free, don't spend that freedom on one of these defaults.

Work in two passes. First, brainstorm a short design plan based on the client's design brief: create a compact token system with color, type, layout, and principles.
- Color: describe the core base palette as 4–6 named hex values.
- Type: the typefaces and their roles.
- Layout: a layout concept, using one-sentence prose descriptions and ASCII wireframes to ideate and compare. Include alignment guidance; should the content be left aligned, center aligned, justified?
- Principles: the high-level guidance for what makes this page unique.

Then review that plan against the brief before building: if any part of it reads like the generic default you would produce for any similar page (work through a similar prompt to see if you arrive somewhere similar) rather than a choice made for this specific brief — revise that part, say what you changed and why. Only after you've confirmed the relative uniqueness of your design plan should you start to write the code, following the revised plan.

Watch CSS specificity: a `.section` rule and a `.cta` rule often cancel each other's padding or margin.

## Restraint and self-critique

Spend your boldness in one place. Let one element be the memorable thing, keep everything around it quiet and disciplined, and cut any decoration that does not serve the brief. Quality floor, unannounced: responsive down to mobile, visible keyboard focus, reduced motion respected, visually accessible, harmonious color palettes. Critique your own work as you build, taking screenshots to review if your environment supports it — a picture is worth 1000 tokens. Before finishing, remove one decorative element.

## Before delivering

- The one-line read, the plan and the build agree; the memorable element is one and visible.
- Hero fits the first viewport; CTAs unique by intent; locks respected.
- Every visible string re-read; no invented claims.
- Rendered and checked (see House rules, Look at the render).

## More on writing in design

Words are design content, not decoration: before writing, ask what the design needs to say.

Write from the end user's perspective. Name things by what users will understand in simple language, not by how the system is built. A user manages notifications, not webhook config. Describe what something is or does in plain terms rather than selling it. Being specific and legible to new users is always better than being clever.

Use active voice as default. A CTA says exactly what happens when it is used: "Save changes," not "Submit." An action keeps the same name through the whole flow, so the button that says "Publish" produces a toast that says "Published." The vocabulary of an interface is the signposting for someone navigating the product. Cohesion and consistency are how people learn their way around.

Errors and empty states give direction, not mood: say what went wrong and how to fix it, without apologizing; an empty screen invites an action. Plain verbs, sentence case, no filler, tone matched to the brand; each written element does one job.

## House rules

- **References first.** Before a signature section (hero, scroll story, carousel, text effect), look at 2 to 4 real references with the same mechanic (award galleries, component libraries the user trusts) and carry the decisions over as values (easing, durations, spacing, type scale), never as copied code. Respect each source's license.
- **Brand work.** When the project has a brand charter (exact HEX, typefaces, tone), the charter is the brief: follow it and spend the design freedom only where it leaves an axis open. Unknown brand or tone: ask before designing.
- **Code.** In a Tailwind v4 project the plan's palette becomes CSS tokens: primitives in `@theme`, semantic tokens (`--primary`, `--background`, `--muted`, `--border`…) in `:root`, consumed as `bg-primary`, never arbitrary classes like `bg-[#1a2b3c]` nor a `tailwind.config` for web tokens. Components: named exports, typed props, `cva` variants plus `cn()` over semantic tokens. Reuse the project's components before creating new ones; every route gets a loading state that mirrors the real layout.
- **Motion.** CSS first (hover, focus, reveals with `animation-timeline: view()` under `@supports`); GSAP + ScrollTrigger through `useGSAP` for orchestrated timelines; Motion (`motion/react`) for gestures and layout in app UI. Animate only `transform`, `opacity`, `filter`; honor `prefers-reduced-motion` with content left visible in its final state; one orchestrated sequence per page. For a specific animation request, use the `animation-creator` skill.
- **Look at the render.** Check it at 320, 768, 1024 and 1440 px, with keyboard and reduced motion, in a real browser (browser pane, Playwright or any preview tool you have).
- **Elsewhere.** Accessibility audit: `audit-accessibility`. Interface guidelines review: `web-design-guidelines`. Site structure before design: `site-architect`. Brand system from a logo: `brand-identity`. Microcopy: `ux-copy`.
