# Knowledge Base

Macon Aero Modelers website - Astro-based static site for RC model aircraft club.

## Quick Facts

- **Repository Type**: Single-project
- **Framework**: Astro 5.x with React, Tailwind CSS 4.x, MDX
- **Total Files Analyzed**: 92
- **Languages**: TypeScript, JavaScript, MDX, CSS

## KB Sections

| Section | File | Lines | Description |
|---------|------|-------|-------------|
| Concepts | concept_map.md | 91 | Domain concepts, terminology, relationships |
| Architecture | architecture.md | 101 | System patterns, layers, integrations |
| Modules | modules.md | 120 | Components, pages, dependencies |
| Patterns | patterns.md | 70 | Implementation idioms and conventions |

## Key Files

| Category | Key Files |
|----------|-----------|
| Config | astro.config.mjs, tailwind.config.mjs, package.json |
| Pages | index.astro, gallery.astro, events.astro, contact.astro, field-info.astro |
| Components | FieldWeather.astro, HeroSlider.astro, GalleryNav.astro, Search.astro |
| Content | src/content/config.ts, src/layouts/Layout.astro |

## Architecture Overview

Static site generator (Astro) with:
- Component-based UI (React islands)
- Utility-first CSS (Tailwind)
- Content collections (MDX for docs/news)
- CI/CD to GitHub Pages

## Dependencies

- **Build**: Astro, Vite, Tailwind CSS, MDX
- **Runtime**: React, ical.js, Pagefind
- **External APIs**: Ambient Weather, METAR, Google Analytics 4, Web3Forms, YouTube

## Generated

- **Strategy**: Parallel map-reduce
- **Generated At**: 2026-03-09
- **Git Commit**: d5bd48cb3d838499dd01d0965acd15d0478a8958
