# Site architecture — deliverable template

## Contents
1. Brand DNA Summary · 2. Information Architecture · 3. Design Token System · 4. Component Architecture · 5. Responsive Strategy · 6. Naming Conventions · 7. SEO & Accessibility Structure

Fill every section; write `N/A — <reason>` rather than dropping one. Copy placeholders stay in brackets (`[H1: main value proposition]`); real copy is written later.

```markdown
# Site Architecture — [Project name]

## 1. Brand DNA Summary
- Visual style: [minimal | rich | bold | elegant | playful | corporate]
- Color temperature: [warm | cool | neutral]
- Design density: [airy | balanced | dense]
- Shape language: [geometric | organic | mixed] — [sharp | rounded | mixed] corners
- Typography character: [modern | classic | technical | friendly | luxury]
- Border radius: [0-2px sharp | 4-8px subtle | 12-16px rounded | 24px+ pill]
- Elevation: [flat | subtle | prominent]
- Spacing feel: [compact | comfortable | spacious]
- Sources: [charter page, logo, brand guidelines used]

## 2. Information Architecture
### 2.1 Sitemap
[Tree of every page, max 3 URL levels]
### 2.2 Navigation Map
[Primary (≤ 7) | Secondary | Footer | Contextual | Breadcrumbs]
### 2.3 Page Blueprints
[Per page: ordered sections, each with the brand goal or user need it serves]

## 3. Design Token System
### 3.1 Primitives
[Raw color, type, spacing, radius, shadow values — traced to the brand]
### 3.2 Semantic Tokens
[Usage tokens referencing primitives, light and dark]
### 3.3 Component Tokens
[Only where a component needs its own token]

## 4. Component Architecture
### 4.1 Atoms
[Name — purpose — variants]
### 4.2 Molecules
[Name — atoms it combines]
### 4.3 Organisms
[Tree per section: organism → molecules → atoms, marked REUSE or NEW when a codebase exists]

## 5. Responsive Strategy
### 5.1 Breakpoints
[Stack table]
### 5.2 Grid System
[Container widths, columns, gutters]
### 5.3 Fluid Typography Scale
[clamp() per text level, rem + vw]
### 5.4 Responsive Behaviors
| Organism | Desktop | Tablet | Mobile |
|---|---|---|---|

## 6. Naming Conventions
[Stack convention with 3-5 real examples from this site]

## 7. SEO & Accessibility Structure
### 7.1 Heading Hierarchy
[H1-H3 plan per template]
### 7.2 Landmark Map
[header, nav, main, sections, aside, footer per template]
### 7.3 Meta & Structured Data
[Title and description pattern, OG image, JSON-LD type per page type]
### 7.4 Accessibility Checklist
[Skip link, focus order, focus visibility, contrast pairs checked, target sizes]
```
