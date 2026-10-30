---
name: animation-creator
description: "Turns a plain-language animation request (scroll reveal, parallax, page transition, text reveal, SVG, hover, drag, 3D) into accessible web code with the lightest tool: CSS, GSAP, Motion, R3F, Lottie or Rive. Use when asked to animate web UI."
---

# Animation creator

Paths: `${CLAUDE_SKILL_DIR}` is this skill's folder (in Codex: the folder that contains this SKILL.md); `references/…` paths are relative to it. A skill named here: Skill tool (Claude) ↔ `$name` (Codex), or read its `SKILL.md`.

Turns a request such as "fade the sections in as I scroll" into complete, accessible, performant code with the lightest tool that fits.

Precedence: the project's own motion conventions win; then the motion rules and bans in [references/motion-rules.md](references/motion-rules.md) (read them first). Durations and easings: the project's animation tokens. Aesthetic direction: `frontend-design`. Expo / React Native (Reanimated) is out of scope.

## Workflow

Copy this checklist and tick it as you go:

```
- [ ] 1. Classify the request (category, complexity, target)
- [ ] 2. Pick one tool with the decision tree
- [ ] 3. Read the matching pattern reference; check version-sensitive APIs in the official docs
- [ ] 4. Build within the non-negotiables
- [ ] 5. Validation loop passes
- [ ] 6. Deliver
```

### 1. Classify

| Category | Typical words |
|---|---|
| Scroll | on scroll, as I scroll, parallax, scroll reveal, progress, pin |
| Trigger | on load, on click, when visible, stagger |
| Interaction | hover, drag, cursor follow, magnetic, gesture |
| Page transition | route change, navigate, shared element |
| Text | split text, typewriter, character by character, word reveal |
| SVG | draw, morph, path animation |
| Layout | reorder, expand, tab underline, grid to list |
| 3D | Three.js, WebGL, Spline, product viewer |
| Micro | feedback, toast, loading, skeleton |

Complexity: one property and one trigger is simple; several properties, timing control or stagger is medium; timelines, scrubbing, physics or 3D is complex.

Target: read `package.json` (`next`, `react`, neither = vanilla or Webflow) and reuse what the project already ships (GSAP, Motion, a house `useGSAP` hook) before adding a library. Ask one question only when the category or the target cannot be inferred.

### 2. Pick the tool

One default per branch:

```
CSS can do it (hover, focus, state change, entry with @starting-style)  → CSS
Scroll
  reveal, progress bar, light parallax         → CSS scroll-driven (animation-timeline) under @supports
  pin, scrub, snap, horizontal, timeline       → GSAP + ScrollTrigger
  scroll-linked value in a React app screen    → Motion useScroll
Page transition
  Next.js App Router                           → React <ViewTransition>
  multi-page site, Webflow                     → CSS @view-transition { navigation: auto; }
  React SPA without view transitions           → Motion AnimatePresence
Text split                                     → GSAP SplitText
SVG                                            → draw: CSS stroke-dashoffset (DrawSVG inside a GSAP timeline); morph: GSAP MorphSVG
Layout change, shared element                  → Motion layout / layoutId (React); GSAP Flip (vanilla)
Gesture, drag, spring                          → Motion (React); GSAP Draggable + Observer (vanilla)
3D                                             → React Three Fiber + drei (code) or Spline (design-led)
Designer-made animation                        → Lottie .lottie (After Effects); Rive (state machine)
Smooth scroll                                  → Lenis, desktop only (see references/motion-rules.md)
Number counter                                 → requestAnimationFrame on the server-rendered final value (see references/motion-rules.md)
```

Weight (gzip): CSS 0; Motion `motion` component about 34 KB, `m` + `LazyMotion` about 4.6 KB at first render; GSAP core about 27 KB plus each plugin; Lenis about 5.5 KB; dotLottie React about 34 KB plus its WASM renderer; three.js scenes are the heaviest.

### 3. Patterns

- CSS: scroll-driven animations, view transitions, `@starting-style`, motion path, visual effects (glass, grain, aurora, gradient border, glow), reduced motion: [css-patterns.md](references/css-patterns.md)
- GSAP: setup, `useGSAP`, timelines, ScrollTrigger, SplitText, Flip, SVG, magnetic, Lenis bridge: [gsap-patterns.md](references/gsap-patterns.md)
- React: Motion, React view transitions in Next.js, React Three Fiber, Spline, Lottie, Rive: [react-patterns.md](references/react-patterns.md)

For an API detail or a version not covered there, query the official docs rather than recalled snippets.

### 4. Non-negotiables

- Compositor-friendly properties only: `transform` or the individual `translate` / `rotate` / `scale`, `opacity`, `filter`. The full list of bans (layout properties, `transition: all`, `setTimeout`, CSS and GSAP on one property, `oklch` colours in GSAP) is in [references/motion-rules.md](references/motion-rules.md).
- Reduced motion ([WCAG 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)): under `prefers-reduced-motion: reduce` every element lands visible in its final state (CSS media query, `gsap.matchMedia()`, Motion `<MotionConfig reducedMotion="user">`). Never convey information by motion alone.
- Motion that starts automatically, lasts more than 5 seconds and runs beside other content gets a pause or stop control ([WCAG 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html), level A).
- Content never starts hidden unless its animation is guaranteed to run (the `@supports` + `no-preference` guard in references/motion-rules.md).
- Cleanup on unmount: `useGSAP` with a `scope`; Motion cleans up itself; never kill every ScrollTrigger globally.
- Heavy libraries (3D, Lottie, Rive, Spline) load through `next/dynamic` inside a Client Component, behind the heavy-effect guard of references/motion-rules.md (desktop width, fine pointer, no reduced motion, static fallback).
- One orchestrated sequence per page; durations and easings from the project's tokens.

### 5. Validation loop

Repeat until every check passes, then stop:

1. Typecheck and build: `tsc --noEmit`, then the project's lint and build scripts; zero errors.
2. Open the page at desktop width and at 375 px (Claude Code Browser pane or Codex browser plugin; otherwise ask the user to look): the animation plays as intended, no layout shift, nothing stays invisible, no console error.
3. Force reduced motion (Chrome DevTools Rendering panel, or Playwright `page.emulateMedia({ reducedMotion: 'reduce' })`): every element is visible in its final state.
4. Scroll-driven CSS: a browser without `animation-timeline` support (Firefox stable) still shows all content.
5. Fix what failed and go back to 1.

### 6. Deliver

One line `Category | Complexity | Tool`, then complete, copy-paste-ready code (no pseudocode, no placeholders), then the files touched and which checks passed.

## Example

Request: "Fade the sections in as I scroll" → `Scroll | Simple | CSS scroll-driven`

```css
@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .section {
      animation: reveal linear both;
      animation-timeline: view();
      animation-range: entry 0% cover 30%;
    }
  }
}

@keyframes reveal {
  from { opacity: 0; translate: 0 30px; }
  to { opacity: 1; translate: 0 0; }
}
```

Browsers without scroll-driven animations and reduced-motion users get the static, visible section; no JavaScript ships.
