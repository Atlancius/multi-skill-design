---
name: design-md
description: "Writes, lints, diffs and exports DESIGN.md files (Google's design-token spec: YAML tokens plus rationale) with the @google/design.md CLI, incl. Tailwind and DTCG export. Use on DESIGN.md, design tokens file, token lint, contrast check."
license: MIT
---

# DESIGN.md

`${CLAUDE_SKILL_DIR}` = ce dossier (Codex : le dossier qui contient ce SKILL.md).

Format ouvert de Google ([google-labs-code/design.md](https://github.com/google-labs-code/design.md), statut `alpha`, il peut changer) qui décrit une identité visuelle à des agents de code : un front matter YAML (jetons normatifs) puis un corps Markdown (le pourquoi). Ce skill couvre le fichier lui-même. Dériver une identité depuis un logo : `brand-identity`. Dessiner l'UI : `frontend-design`.

## Anatomie

Gabarit complet à copier : `${CLAUDE_SKILL_DIR}/templates/starter.md`.

Front matter : `name`, `version: alpha` (optionnel), `description`, puis `colors`, `typography`, `rounded`, `spacing`, `components`. Le champ optionnel `omitted` liste les sections volontairement absentes.

| Type | Format | Exemple |
|---|---|---|
| Couleur | toute couleur CSS (hex, `rgb()`, `oklch()`, nom) | `"#1A1C1E"` |
| Dimension | nombre + unité `px`, `em`, `rem` | `48px`, `"-0.02em"` |
| Référence | chemin pointé entre accolades | `{colors.primary}` |
| Typographie | objet : `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`, `fontFeature`, `fontVariation` | |

Composants : propriétés admises `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Une variante (hover, active) est une entrée sœur au nom proche (`button-primary-hover`), jamais imbriquée.

Sections `##`, facultatives, dans cet ordre quand elles sont présentes : Overview (alias Brand & Style), Colors, Typography, Layout (alias Layout & Spacing), Elevation & Depth (alias Elevation), Shapes, Components, Do's and Don'ts. Un titre en double fait rejeter le fichier ; une section inconnue est conservée.

## Écrire un DESIGN.md

Checklist :

```
- [ ] Ton de la marque, accent, direction typographique (demander ou déduire du site, de l'image ou du brief fourni)
- [ ] Fichier à la racine du projet, depuis le gabarit : name, colors (avec primary), typography, rounded, spacing, components
- [ ] Composants en références {colors.x}, jamais en hex recopié
- [ ] Corps Markdown dans l'ordre canonique, une phrase de rôle par couleur et par composant
- [ ] Lint à zéro erreur, avertissements traités ou justifiés
- [ ] Exports écrits à côté si le projet utilise Tailwind ou des jetons DTCG
```

Pièges YAML : citer les couleurs hex (`#` ouvre un commentaire) et les valeurs négatives (`"-0.02em"`).

## CLI

Node requis. Toutes les commandes lisent un fichier ou `-` (stdin) et sortent du JSON.

```bash
npx -y @google/design.md lint DESIGN.md                       # exit 1 si erreur
npx -y @google/design.md diff DESIGN.md DESIGN-v2.md          # exit 1 si plus d'erreurs ou d'avertissements après
npx -y @google/design.md export --format css-tailwind DESIGN.md > theme.css        # Tailwind v4 (@theme)
npx -y @google/design.md export --format json-tailwind DESIGN.md > tailwind.theme.json   # Tailwind v3 (alias : tailwind)
npx -y @google/design.md export --format dtcg DESIGN.md > tokens.json              # W3C Design Tokens
npx -y @google/design.md spec --rules-only --format json     # règles, pour un prompt d'agent
```

Windows : `npx -p @google/design.md designmd lint DESIGN.md` (le suffixe `.md` du binaire entre en collision avec l'association Markdown). `ENOVERSIONS` = le registre npm configuré n'est pas le public (`npm config get registry`).

`export` sort en 0 même si le lint échoue : lancer `lint` avant. Format Tailwind : `css-tailwind` pour un projet Tailwind v4 (web), `json-tailwind` pour un `tailwind.config.js` v3 (NativeWind 4 mobile inclus).

### Règles de lint

| Règle | Niveau | Vérifie |
|---|---|---|
| `broken-ref` | error | une référence `{...}` ne pointe sur aucun jeton |
| `missing-primary` | warning | couleurs définies sans `primary` |
| `contrast-ratio` | warning | paire `backgroundColor`/`textColor` d'un composant sous WCAG AA (4,5:1) |
| `orphaned-tokens` | warning | couleur jamais référencée par un composant |
| `missing-typography` | warning | couleurs définies sans typographie |
| `section-order` | warning | sections hors de l'ordre canonique |
| `unknown-key`, `token-like-ignored` | warning | clé de premier niveau qui ressemble à une faute de frappe, ou à des jetons ignorés |
| `token-summary`, `missing-sections`, `omitted-rules` | info | bilans et sections facultatives absentes |

Boucle de validation : lancer `lint`, corriger les erreurs, relancer jusqu'à zéro erreur. Annoncer chaque `contrast-ratio` à l'utilisateur : c'est le principal gain du format côté accessibilité.

## Sortie

Chemin du fichier, résultat du lint (erreurs et avertissements restants), exports écrits.
