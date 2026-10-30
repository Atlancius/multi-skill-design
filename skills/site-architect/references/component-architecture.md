# Architecture de composants et design tokens — référence

## Sommaire
1. Atomic Design · 2. Design tokens · 3. Catalogue de sections · 4. Conventions de nommage par stack · 5. Architecture de l'information

## 1. Atomic Design (Brad Frost)

| Niveau | Description | Exemples |
|--------|-------------|----------|
| **Atomes** | Éléments indivisibles | Button, Input, Label, Icon, Avatar, Badge |
| **Molécules** | Groupe d'atomes, une fonction | Search Bar, Form Field, Nav Link, Media Object |
| **Organismes** | Section d'interface reconnaissable | Header, Hero, Feature Grid, Pricing, Footer |
| **Templates** | Agencement d'organismes (squelette) | Landing, Blog Listing, Dashboard |
| **Pages** | Template + contenu réel | Validation des cas limites |

Arbre de décision :

```
Élément HTML natif / wrapper minimal ?     → ATOME
Combine 2-3 atomes, une micro-fonction ?   → MOLÉCULE
Section d'interface autonome ?             → ORGANISME
Agencement d'organismes sans contenu ?     → TEMPLATE
Template + vrai contenu ?                  → PAGE
```

Emplacement conseillé dans un projet React : `components/ui/` (atomes, molécules), `components/sections/` (organismes), `components/layouts/` (templates) ; sites de marque : `atoms/`, `molecules/`, `organisms/`.

## 2. Design tokens

Trois niveaux :

1. **Primitives** (valeurs brutes) : `--color-blue-500`, `--font-size-16`, `--space-4`.
2. **Sémantiques** (usage) : `--color-bg-primary`, `--color-text-brand`, `--spacing-section-md`.
3. **Composants** (spécifiques, si nécessaire) : `--button-bg-primary`, `--card-border-radius`, `--input-border-focus`.

Tailwind v4 : primitives en `@theme`, sémantiques en `:root`, override `.dark` ; aucun `tailwind.config` pour les tokens web. Webflow : variables primitives puis sémantiques (Client-First). Format d'échange JSON : W3C Design Tokens (DTCG 2025.10).

| Catégorie | Exemples |
|-----------|----------|
| Couleurs | bg-primary, text-secondary, border-default, brand |
| Typographie | font-family, font-size, font-weight, line-height |
| Spacing | section-sm/md/lg, component-xs/sm/md/lg, inline-xs/sm/md |
| Élévation | shadow-xs à shadow-xl |
| Rayons | radius-sm, radius-md, radius-lg, radius-xl, radius-full |
| Transitions | duration-fast/normal/slow, easing-default/in/out |
| Z-index | dropdown 1000, sticky 1100, overlay 1200, modal 1300, tooltip 1500 |

Nommage : `--{catégorie}-{propriété}-{élément}-{variante}-{état}`, segments inutiles omis.

## 3. Catalogue de sections

- **Navigation et structure** : Announcement Bar, Header, Breadcrumbs, Sidebar, Footer.
- **Hero** : Centered, Split, With Form, Video, Animated, Slider, Minimal.
- **Contenu** : Features Grid, Features Alternating, Benefits, How it Works, Stats, Comparison, Content Block, Gallery, Timeline, Map.
- **Preuve sociale** : Testimonials, Logo Cloud, Case Studies, Reviews, Awards, Press Mentions — uniquement avec des preuves réelles, jamais inventées.
- **Conversion** : CTA Section, CTA Banner, Pricing, Newsletter, Contact Form, Lead Magnet, Booking.
- **Spécifiques** : Team, FAQ, Blog Grid, Portfolio, Integrations, Download/App, Job Openings.

## 4. Conventions de nommage par stack

| Stack | Convention | Syntaxe |
|-------|-----------|---------|
| Webflow | Client-First | `section_hero`, `hero_content`, `is-dark` |
| Next.js / TanStack Start (React) | Tailwind v4 + composants `cva` | utilitaires sur tokens sémantiques, export nommé |
| HTML/CSS (Astro, statique) | BEM | `.card__title--large` |
| CSS moderne sans framework | CUBE CSS | composition + utility + block + exception |

## 5. Architecture de l'information

| Structure | Pour |
|-----------|------|
| Hiérarchique | Sites d'entreprise, e-commerce |
| Séquentielle | Onboarding, checkout, tutoriels |
| Matricielle | Sites riches, documentation |
| Base de données | Annuaires, catalogues, blogs |
| Hub & spoke | Apps, dashboards |

Sitemap type — site vitrine B2B :

```
Accueil
├── Services (+ sous-pages par service)
├── Réalisations (+ études de cas)
├── À propos (histoire, équipe, valeurs)
├── Ressources (blog, guides)
├── Contact
├── Mentions légales
├── Politique de confidentialité
└── CGV (si vente)
```

Sitemap type — SaaS :

```
Accueil
├── Produit (fonctionnalités, intégrations, sécurité, changelog)
├── Solutions (par secteur ou cas d'usage)
├── Tarifs
├── Ressources (blog, docs, tutoriels)
├── Entreprise (à propos, carrières, presse)
├── Contact / Support
├── Connexion / Inscription
├── Mentions légales
└── Politique de confidentialité
```

Navigation : 7 entrées principales au plus ; logo → accueil ; CTA principal en bouton distinct ; page active visible ; fil d'Ariane au-delà de 2 niveaux.

Parcours : chaque page peut être une porte d'entrée (SEO) ; CTA visible au-dessus de la ligne de flottaison et répété sur les pages longues ; premier formulaire court (nom + email) ; preuve sociale près des points de conversion ; divulgation progressive.
