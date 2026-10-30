# Multi Skill Design

13 skills de design web pour agents de code (Claude Code, Codex, ou tout agent qui lit des `SKILL.md`). Chaque dossier est autonome : aucune dépendance externe, aucun compte, aucune clé d'API.

## Installation

Claude Code : copier les dossiers voulus de `skills/` dans

- `~/.claude/skills/` (tous tes projets), ou
- `.claude/skills/` à la racine d'un projet (ce projet seulement).

Codex : copier dans `~/.codex/skills/` (ou `.agents/skills/` du projet). Les fichiers `agents/openai.yaml` servent à Codex et sont ignorés par Claude.

Ensuite, appeler un skill par son nom (`/frontend-design` dans Claude Code, `$frontend-design` dans Codex) ou le laisser se déclencher depuis sa description.

## Les skills

| Skill | Rôle | Langue |
|---|---|---|
| `frontend-design` | Direction visuelle distinctive pour une page, une landing, un dashboard ou un composant neuf, sans le look « template IA » | EN |
| `ui-ux-pro-max` | Base de données UI/UX (styles, palettes, paires de polices, patterns de landing) + script Python qui sort un design system | EN |
| `brand-identity` | Système d'identité complet depuis un logo : palette, typo, tokens, composants, ton de voix, guide | EN |
| `site-architect` | Architecture d'un site : sitemap, blueprints de pages, tokens, Atomic Design, responsive, SEO/a11y | EN/FR |
| `animation-creator` | Transforme une demande d'animation (scroll reveal, parallax, transition, texte, 3D) en code accessible avec l'outil le plus léger | EN |
| `apple-design` | Principes Apple (WWDC) d'interfaces fluides pour le web : springs, gestes, momentum, matières | EN |
| `mobile-native` | Fait qu'une web app se sente native sur téléphone : hover collé, 100vh, zoom des inputs, safe areas | EN |
| `pick-ui-library` | Choisit LA bonne librairie React pour un besoin (toasts, ⌘K, OTP, charts, drag and drop…) | EN |
| `web-design-guidelines` | Revue d'UI contre les Web Interface Guidelines de Vercel | FR |
| `audit-accessibility` | Audit WCAG 2.2 AA du code (statique + axe-core) et correction des points bloquants | FR |
| `ux-copy` | Microcopy : boutons, erreurs, états vides, confirmations, onboarding | EN |
| `design-handoff` | Spec de handoff développeur depuis une maquette (Figma, capture ou description) | EN |
| `design-md` | Écrit et vérifie un fichier `DESIGN.md` (spec de Google pour décrire un design aux agents) | FR |

## Enchaînement conseillé pour un nouveau site

`brand-identity` (depuis le logo) → `site-architect` (structure) → `frontend-design` (direction et build) → `animation-creator` (motion) → `audit-accessibility` + `web-design-guidelines` (contrôle).

Sans logo : commencer par `ui-ux-pro-max`.

## Prérequis optionnels

- `ui-ux-pro-max` : Python 3 pour son script de recherche.
- `audit-accessibility` : `@axe-core/playwright` dans le projet pour l'audit automatisé ; sinon analyse statique seule.
- `design-md` : `npx @google/design.md` pour lint et export.

## Licences

Chaque dossier garde sa licence et son `NOTICE` :

- MIT : `apple-design`, `mobile-native`, `pick-ui-library` (Emil Kowalski), `ui-ux-pro-max` (Next Level Builder), `web-design-guidelines` (Vercel Labs), `design-md` (Nous Research), `animation-creator`, `brand-identity`, `site-architect`, `audit-accessibility`.
- Apache-2.0 : `frontend-design` (Anthropic, avec ajouts MIT de Leonxlnx/taste-skill), `ux-copy`, `design-handoff` (Anthropic knowledge-work-plugins).

Pour aller plus loin sur l'animation, le skill `animate` d'Emil Kowalski est public : github.com/emilkowalski/skills.
