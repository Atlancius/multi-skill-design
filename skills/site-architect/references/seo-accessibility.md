# Structure SEO et accessibilité — référence

## Sommaire
1. Règles qui priment · 2. Titres · 3. HTML sémantique et landmarks · 4. URLs · 5. Maillage interne · 6. Gabarits meta · 7. Données structurées par type de page · 8. Core Web Vitals · 9. Accessibilité dans l'architecture

## 1. Règles qui priment

Ce fichier ne garde que ce qui se décide au niveau de l'architecture. Les conventions du projet priment ; points de départ :

- SEO, AEO, GEO (HTML crawlable, JSON-LD éligible, robots, sitemap et `lastmod`, `llms.txt`, interdits) : Google Search Central et schema.org.
- Accessibilité (WCAG 2.2 AA, procédure de test) : skill `audit-accessibility` (référence WCAG intégrée).

## 2. Titres

- Un seul H1 par page (sujet principal, lisible).
- Ne pas sauter de niveau en descendant (H2 puis H4) ; remonter en fin de sous-section est permis.
- Les tags H ne servent pas au style visuel (Client-First : `heading-style-*`).
- Titres descriptifs du contenu (pas « Introduction »).

## 3. HTML sémantique et landmarks

| Élément | Rôle | Règle |
|---|---|---|
| `<header>` | En-tête de page ou de section | Plusieurs autorisés |
| `<nav>` | Navigation | `aria-label` s'il y en a plusieurs |
| `<main>` | Contenu principal | Un seul par page |
| `<article>` | Contenu autonome | Lisible hors contexte |
| `<section>` | Division thématique | Avec un titre |
| `<aside>` | Complémentaire | Sidebar, liens associés |
| `<footer>` | Pied de page ou de section | Copyright, liens légaux |

HTML sémantique avant les rôles ARIA ; landmarks du même type différenciés par `aria-label` sans répéter le type (« Principale », pas « Navigation principale »).

## 4. URLs

- Minuscules, tirets comme séparateurs, mots lisibles plutôt qu'identifiants ; pas d'ID de session, paramètres au minimum ; HTTPS.
- La structure reflète la hiérarchie du sitemap.
- Conventions internes (pas des exigences Google) : slug de 3-5 mots, 3 niveaux au plus, ni date ni caractère spécial.
- Une URL modifiée garde une redirection permanente côté serveur (301/308).

## 5. Maillage interne

- Hub & spoke (clusters thématiques) : le hub renvoie vers chaque spoke ; chaque spoke vers le hub et ses voisins.
- Fil d'Ariane balisé `BreadcrumbList`.
- Ancres descriptives (jamais « cliquez ici »), liens contextuels dans le corps, aucune page orpheline.

## 6. Gabarits meta

Google n'impose aucune longueur et tronque à la largeur d'affichage : les longueurs sont des repères.

- **Title** : unique, sujet en tête, marque en début ou en fin après un séparateur ; repère 50-60 caractères.
- **Description** : unique, résumé fidèle de la page ; repère 150-160 caractères.
- **Open Graph** : requis `og:title`, `og:type`, `og:image`, `og:url` ([ogp.me](https://ogp.me/)) ; recommandés `og:description`, `og:locale` ; image 1200×630px (1.91:1).
- **X / Twitter** : `twitter:card` (`summary_large_image`) ; titre, description et image retombent sur les `og:*` absents.
- **Canonical** auto-référent sur chaque page indexable.

## 7. Données structurées par type de page

| Type de page | JSON-LD |
|---|---|
| Accueil | Organization (ou LocalBusiness pour un commerce) + WebSite |
| Page locale / contact | LocalBusiness (adresse, `geo`, horaires) |
| Article de blog | Article + BreadcrumbList |
| Fiche produit | Product |
| Page profonde | BreadcrumbList |
| Vidéo | VideoObject |

Éligibilité aux résultats enrichis et types inutiles (FAQ, HowTo, avis sur soi-même) : règle SEO, AEO, GEO. Le JSON-LD décrit uniquement un contenu visible sur la page.

## 8. Core Web Vitals

Cibles « bon » au 75e percentile, mobile et desktop : LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1.

| Métrique | Décision d'architecture |
|---|---|
| LCP | Image LCP découvrable dans le HTML initial (sinon preload), `fetchpriority="high"`, jamais en lazy-load ; contenu indexable rendu au serveur |
| CLS | Dimensions ou `aspect-ratio` sur médias et embeds, espace réservé aux contenus dynamiques, polices auto-hébergées avec fallback ajusté |
| INP | Code-splitting par route, JS non critique différé, longues tâches découpées, SSR/SSG |

## 9. Accessibilité dans l'architecture

- Lien d'évitement (« Aller au contenu ») en premier élément focusable, visible au focus, ciblant `<main>`.
- Ordre du DOM = ordre visuel ; aucun `tabindex` > 0.
- Focus visible sur tout élément interactif (`:focus-visible`), jamais entièrement masqué par un header ou un footer sticky (WCAG 2.4.11).
- Modales : focus piégé, retour du focus à la fermeture, `Escape` ferme.
- Contrastes : texte 4.5:1, grand texte (≥ 24px, ou ≥ 18.66px gras) 3:1, composants d'UI 3:1 — vérifiés sur les paires de tokens.
- Alternatives textuelles : image informative → alt concis portant l'information ; décorative → `alt=""` ; image-lien → destination ; logo → nom de la marque ; icône seule → fonction. Jamais « Image de… ».
- Cibles tactiles ≥ 24×24px (WCAG 2.5.8), 44×44px visé.
