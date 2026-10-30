# Responsive design — référence

## Sommaire
1. Breakpoints · 2. Typographie fluide · 3. Spacing fluide · 4. Container queries · 5. Grilles fluides · 6. Mobile-first ou desktop-first · 7. Patterns · 8. Unités de viewport · 9. Propriétés logiques · 10. Performance

## 1. Breakpoints

| Stack | Breakpoints | Sens |
|---|---|---|
| Tailwind v4 | `sm` 40rem (640px), `md` 48rem (768px), `lg` 64rem (1024px), `xl` 80rem (1280px), `2xl` 96rem (1536px) ; personnalisables par `--breakpoint-*` dans `@theme` | Mobile-first (`min-width`) ; `max-*` pour borner une plage |
| Webflow | Desktop = base (≥ 992px) ; Tablet 768–991px (glossaire Webflow : 768–990 ; CSS exporté : `max-width: 991px`) ; Mobile landscape 480–767px ; Mobile portrait ≤ 479px ; optionnels 1280, 1440, 1920px | Desktop-first : la base cascade vers le bas et vers les grands breakpoints ; un style posé sur Tablet cascade vers les mobiles seulement |
| Bootstrap 5.3 | `sm` 576, `md` 768, `lg` 992, `xl` 1200, `xxl` 1400px | Mobile-first |

Sources : [Tailwind responsive design](https://tailwindcss.com/docs/responsive-design), [Webflow mobile portrait](https://university.webflow.com/glossary/mobile-portrait-breakpoint), [Webflow tablet](https://university.webflow.com/glossary/tablet-breakpoint), [Webflow mobile landscape](https://university.webflow.com/glossary/mobile-landscape-breakpoint), [Bootstrap breakpoints](https://getbootstrap.com/docs/5.3/layout/breakpoints/).

CSS sans framework, mobile-first :

```css
@media (width >= 40rem) { } /* 640px  */
@media (width >= 48rem) { } /* 768px  */
@media (width >= 64rem) { } /* 1024px */
@media (width >= 80rem) { } /* 1280px */
```

Contrôle visuel : 320, 768, 1024 et 1440px.

## 2. Typographie fluide

```css
:root {
  --step-0: clamp(1rem, 0.91rem + 0.46vw, 1.25rem);
  --step-1: clamp(1.25rem, 1.14rem + 0.57vw, 1.56rem);
  --step-2: clamp(1.56rem, 1.42rem + 0.71vw, 1.95rem);
  --step-3: clamp(1.95rem, 1.78rem + 0.89vw, 2.44rem);
  --step-4: clamp(2.44rem, 2.22rem + 1.11vw, 3.05rem);
  --step-5: clamp(3.05rem, 2.78rem + 1.39vw, 3.81rem);
}
```

Toujours un terme en `rem` dans la valeur préférée (un `vw` pur ignore le zoom, WCAG 1.4.4). Heuristique : max ≤ 2,5 × min pour que le zoom à 200 % agrandisse encore le texte. Longueur de ligne : `max-width: 65ch`.

## 3. Spacing fluide

```css
:root {
  --space-xs:  clamp(0.25rem, 0.2rem + 0.25vw, 0.5rem);
  --space-sm:  clamp(0.5rem, 0.4rem + 0.5vw, 0.75rem);
  --space-md:  clamp(1rem, 0.8rem + 1vw, 1.5rem);
  --space-lg:  clamp(1.5rem, 1rem + 2vw, 3rem);
  --space-xl:  clamp(2rem, 1.5rem + 2.5vw, 4rem);
  --space-2xl: clamp(3rem, 2rem + 4vw, 6rem);
}
```

## 4. Container queries

| Critère | Media queries | Container queries |
|---|---|---|
| Référence | Viewport | Conteneur parent |
| Réutilisabilité | Faible | Forte |
| Cas idéal | Layout global de la page | Composant posé dans des contextes de largeurs différentes |

Container size queries : Baseline « widely available » depuis août 2025 ([web.dev](https://web.dev/blog/baseline-digest-aug-2025)). Tailwind v4 : `@container` sur le parent, variantes `@md:` sur les enfants. Défaut : container queries pour les composants réutilisés (cartes, médias, widgets), media queries pour le layout global.

## 5. Grilles fluides

```css
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: var(--space-md);
}
```

## 6. Mobile-first ou desktop-first

- Mobile-first (`min-width`) : sites grand public, e-commerce, blogs, vitrines — défaut de Tailwind.
- Desktop-first : dashboards et outils B2B data-heavy ; Webflow l'impose par construction (desktop = base).
- Dans les deux cas, styles de base intrinsèquement responsives d'abord (flex-wrap, grid `minmax`, `clamp`, container queries), breakpoints ensuite.

## 7. Patterns

- **Navigation** : hamburger au-delà de ~6 liens ou contenu riche ; bottom nav pour une PWA/app (3-5 entrées) ; mega menu pour les catalogues.
- **Grille → pile** : grid `auto-fit` + `minmax()` (sans media query), flex `wrap` + `flex: 1 1 18rem`, ou media queries explicites.
- **Images** : `srcset` + `sizes` pour la résolution ; `<picture>` pour la direction artistique et les formats (AVIF > WebP > JPEG) ; `aspect-ratio` ou `width`/`height` contre le CLS ; `loading="lazy"` sous la ligne de flottaison ; `fetchpriority="high"` sur l'image LCP.
- Ne jamais masquer un contenu critique sur mobile : divulgation progressive.

## 8. Unités de viewport

| Unité | Comportement |
|---|---|
| `dvh` | Dynamique (suit la barre d'adresse) |
| `svh` | Petite (barre visible) |
| `lvh` | Grande (barre masquée) |

Hero plein écran : `min-height: 100svh` (pas de saut quand la barre se rétracte) ou `100dvh` si le hero doit suivre la barre.

## 9. Propriétés logiques

`margin-inline`, `margin-block`, `padding-inline`, `padding-block`, `inline-size`, `block-size`, `inset-inline-start`, `text-align: start` : prêtes pour le RTL sans réécriture.

## 10. Performance

- CSS critique inline dans le `<head>` (viser ~14 Ko compressés pour le premier aller-retour).
- `loading="lazy"` sous la ligne de flottaison, jamais sur l'image LCP.
- CSS inutilisé retiré au build (Tailwind v4 ne génère que les classes détectées).
- Polices auto-hébergées (`next/font` en Next.js).
