# Client-First (Finsweet) — référence

## Sommaire
1. Philosophie · 2. Nommage des classes · 3. Système de dossiers · 4. Core structure · 5. Spacing · 6. Typographie · 7. Couleurs et variables · 8. Utilities · 9. Interactions · 10. Unités

Source : [Client-First docs](https://finsweet.com/client-first/docs). Vérifier sur la doc avant d'affirmer un détail absent d'ici.

## 1. Philosophie

Conventions pour Webflow : nommage clair et descriptif, sans abréviation, du général au spécifique, sans empilement profond (*deep stacking*).

## 2. Nommage des classes

| Type | Identifiant | Exemple | Rôle |
|------|-------------|---------|------|
| **Custom class** | Contient `_` | `header-primary_content` | Style propre à un composant |
| **Utility class** | Tirets seulement | `text-color-primary` | Propriété CSS réutilisable |

### Combo classes — préfixe `is-`

Variante posée sur une classe de base, dont elle hérite.

```
Classe de base : button
Variantes : is-primary, is-secondary, is-alternative, is-inactive, is-dark
```

| Classes empilées | Évaluation |
|---------------|-----------|
| 1-2 | Idéal |
| 3 | Acceptable |
| 4 | Limite |
| 5+ | Créer une custom class |

## 3. Système de dossiers

Le `_` crée des dossiers virtuels dans le panneau Styles de Webflow.

```
[dossier]_[element]
nav_logo              → dossier nav/, élément logo
blog_header_graphic   → dossier blog/header/, élément graphic
```

- Dossier général : `slider_arrow`, `subscribe_form-input`
- Dossier page : `home-hero_heading`, `about-team_photo`
- Mot-clé component : `client-slider_component` (wrapper parent copiable-collable)

## 4. Core structure (6 classes)

```
page-wrapper
  └── main-wrapper                          (<main>)
        └── section_[identifiant]           (<section>)
              └── padding-global + padding-section-[size]   (même div)
                    └── container-[size]
                          └── [contenu]
```

| Classe | Tag | Rôle |
|--------|-----|------|
| `page-wrapper` | `<div>` | Enveloppe toute la page |
| `main-wrapper` | `<main>` | Contenu principal ; nav et footer restent dehors |
| `section_[id]` | `<section>` | Organisation, ancres |
| `padding-global` | `<div>` | Padding horizontal global |
| `padding-section-[size]` | sur la div `padding-global` | Padding vertical, posé sur la même div pour réduire l'imbrication |
| `container-[size]` | `<div>` | Centrage et largeur max |

Tailles : `container-small|medium|large`, `padding-section-small|medium|large`.

## 5. Spacing

| Taille | Valeur |
|--------|--------|
| `tiny` | 0.125rem |
| `xxsmall` | 0.25rem |
| `xsmall` | 0.5rem |
| `small` | 1rem |
| `medium` | 2rem |
| `large` | 3rem |
| `xlarge` | 4rem |
| `xxlarge` | 5rem |
| `huge` | 6rem |
| `xhuge` | 8rem |
| `xxhuge` | 12rem |

Stratégies : spacing block (div vide `padding-bottom padding-medium`), spacing wrapper (`margin-bottom margin-large`), `row-gap`/`column-gap` sur le parent en CSS Grid, ou margin/padding directement sur la custom class.

## 6. Typographie

Basée sur les tags HTML par défaut (H1-H6, Body) ; classes seulement pour les variations.

- `heading-style-h1` à `heading-style-h6` : découple le style visuel du tag sémantique.
- `text-size-tiny|small|regular|medium|large`
- `text-weight-light|normal|semibold|bold|xbold`
- `text-color-primary|secondary|alternate`
- `text-align-left|center|right`
- `text-style-allcaps|italic|link|muted|nowrap|quote|strikethrough|2lines|3lines`

## 7. Couleurs et variables

Deux niveaux : primitives (couleurs brutes) puis sémantiques (fonction : `background-color--background-primary`). Classes `background-color-primary|secondary|tertiary|alternate`, `text-color-primary|secondary|alternate`. Toujours nommer par fonction, jamais par couleur.

## 8. Utilities

- `max-width-xxsmall` à `max-width-xxlarge`, `max-width-full`
- `hide`, `hide-tablet`, `hide-mobile-landscape`, `hide-mobile-portrait`
- `icon-height-small|medium|large`, `icon-1x1-small|medium|large`
- `aspect-ratio-square|portrait|landscape|widescreen`
- `z-index-1|2`, `overflow-hidden|scroll|auto`
- `spacing-clean` : remet marges et paddings à zéro
- Section sombre : combo class propre au projet sur `section_[id]` (ex. `is-dark`)

## 9. Interactions

Format : `Element [Action + State]`, ex. `Nav Menu [Open/Close]`, `Button Arrow [Move In/Out]`.

## 10. Unités

`rem` pour la plupart des tailles (base 16px) ; les bordures de 1px restent en `px`.
