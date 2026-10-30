# Motion rules for web UI

Defaults this skill applies unless the project's own conventions say otherwise.

## Which tool

- **CSS first**: hover, focus, toasts, skeletons, marquees, scroll reveals with `animation-timeline: view()` under `@supports` (zero JS, works in Server Components).
- **GSAP + ScrollTrigger**: timelines, orchestrated staggers, pinning, scrub, SplitText. Brand and marketing sites.
- **Motion (`motion/react`)**: gestures, layout animations and exit animations inside a React app. A project still on `framer-motion` keeps its imports.
- **Lenis**: desktop only, dynamically imported, off below 768 px and under reduced motion.
- **3D**: React Three Fiber + drei (code) or Spline (design), loaded client-only (`next/dynamic` in Next.js).
- **Number counter**: `requestAnimationFrame` on a final value already rendered on the server; no animation library needed.

## Do

- Before a signature animation (hero, scroll story, carousel, text effect, shader), study one or two references with the same mechanic and carry over values (easing, durations, triggers), not code.
- GSAP in React: `useGSAP(() => …, { scope: ref, dependencies })` from `@gsap/react` in a `'use client'` file; `gsap.registerPlugin(useGSAP, ScrollTrigger)` once in a shared module; tweens fired from handlers wrapped in `contextSafe`.
- Reduced motion: `gsap.matchMedia()` with `(prefers-reduced-motion: reduce)`, or an early return; content stays visible in its final state.
- Animate only `transform`, `opacity`, `filter`; set `will-change` at the start and remove it after.
- Heavy effect (canvas, 3D, particle text) behind a guard: width ≥ 768 px, fine pointer, no reduced motion, static fallback rendered on the server, mounted after first paint and an idle period.
- Split text: keep a `sr-only` copy of the text plus an `aria-hidden` split version, because SEO and LLM extractors ignore `aria-label` and drop `aria-hidden` subtrees.
- Durations and easings come from animation tokens; easing matches the brand's personality.
- One orchestrated sequence per page.

## Never

- A scroll interceptor (Lenis or custom smooth scroll) without a bridge to ScrollTrigger (`lenis.on('scroll', ScrollTrigger.update)` + `gsap.ticker`): sections silently stay stuck at `opacity: 0`.
- JS smooth scroll on mobile: a permanent ticker on the main thread for no gain; native mobile scrolling is enough.
- Initial `opacity: 0` on content whose animation might not run: hide only under `@supports (animation-timeline: view())` and `prefers-reduced-motion: no-preference`.
- Hand-written `useEffect` + `gsap.context()` in a new component: use `useGSAP`.
- One `IntersectionObserver` client component per section when CSS can do it.
- Animating `width`, `height`, `top`, `left`, `margin`, `padding`; `transition: all`; timing with `setTimeout`; CSS and GSAP on the same property.
- GSAP colour tweens in `oklch`: use HEX, RGB or HSL.
- A 3D library in a public page bundle without measuring mobile LCP.
