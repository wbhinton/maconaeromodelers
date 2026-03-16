# Modules

Module structure and dependencies for Macon Aero Modelers website.

## Modules

### pages
- **Type**: directory_module
- **Purpose**: Main Astro page routes for the website
- **Key Files**: index.astro, gallery.astro, events.astro, contact.astro, field-info.astro, resources.astro, new-members.astro, videos.astro, 404.astro

### pages/news
- **Type**: directory_module
- **Purpose**: News section with list and article pages using Astro content collections
- **Key Files**: index.astro, [...slug].astro

### pages/gallery
- **Type**: directory_module
- **Purpose**: Gallery section with year archives and album pages
- **Key Files**: [year]/index.astro, [year]/[slug].astro

### pages/docs
- **Type**: directory_module
- **Purpose**: Documentation section using Astro content collections with search
- **Key Files**: [...slug].astro

### components
- **Type**: directory_module
- **Purpose**: Reusable UI components
- **Key Files**: FieldWeather.astro, HeroSlider.astro, GalleryNav.astro

### components/docs
- **Type**: directory_module
- **Purpose**: Documentation-specific components
- **Key Files**: Search.astro, Card.astro

### layouts
- **Type**: directory_module
- **Purpose**: Astro layouts providing consistent page structure
- **Key Files**: Layout.astro

### content/news
- **Type**: directory_module
- **Purpose**: Markdown-based news articles
- **Key Files**: first-update.md

### styles
- **Type**: directory_module
- **Purpose**: Global CSS with Tailwind configuration
- **Key Files**: global.css

## Components

### Pages

| Component | File | Purpose |
|-----------|------|---------|
| index | src/pages/index.astro | Home page with hero slider and club information |
| gallery | src/pages/gallery.astro | Main gallery page with photo albums and YouTube videos |
| events | src/pages/events.astro | Events page displaying calendar events |
| contact | src/pages/contact.astro | Contact page with club info and contact form |
| field-info | src/pages/field-info.astro | Field information page with weather and location |
| resources | src/pages/resources.astro | Pilot resources page with documents and tools |
| new-members | src/pages/new-members.astro | New member onboarding page |
| videos | src/pages/videos.astro | Video gallery page with YouTube playlist |
| news-index | src/pages/news/index.astro | News listing page |
| news-article | src/pages/news/[...slug].astro | Individual news article page |
| gallery-year | src/pages/gallery/[year]/index.astro | Gallery archive page for specific year |
| gallery-album | src/pages/gallery/[year]/[slug].astro | Individual gallery album page with lightbox |
| docs | src/pages/docs/[...slug].astro | Documentation pages with sidebar navigation |
| not-found | src/pages/404.astro | 404 error page |

### Shared Components

| Component | File | Purpose |
|-----------|------|---------|
| FieldWeather | src/components/FieldWeather.astro | Weather dashboard showing field conditions and METAR data |
| HeroSlider | src/components/HeroSlider.astro | Rotating hero image slider with text overlay |
| GalleryNav | src/components/GalleryNav.astro | Dynamic gallery year navigation |
| Search | src/components/docs/Search.astro | Documentation search using Pagefind |
| Card | src/components/docs/Card.astro | Reusable card component |

## Dependencies

### Internal Dependencies

- **pages → components**: All pages import reusable components (Layout, FieldWeather, HeroSlider, etc.)
- **pages/gallery → pages/gallery/[year]**: Gallery year pages linked via GalleryNav
- **pages/news → content/news**: News pages use Astro content collections
- **pages/docs → components/docs**: Docs pages import Search component

### External Dependencies

| Dependency | Purpose | Used By |
|------------|---------|---------|
| astro | Astro web framework | all pages and components |
| ical | Parse iCal/ICS calendar data | events page |
| pagefind | Static search indexing | docs search component |
| tailwindcss | Utility-first CSS framework | global styles and all components |
| ambientweather.net | Field weather station data | FieldWeather component |
| METAR | Aviation weather data | FieldWeather component |
| web3forms | Contact form submission | contact page |
| youtube | Video embedding | gallery, videos pages |

## Cross-Module Patterns

### Content Collection Driven Pages
- **Description**: News and docs pages use Astro content collections to generate static pages from Markdown files
- **Modules**: pages/news, pages/docs, content/news
- **Benefits**: Type-safe content access, automatic static path generation

### Filesystem-Based Gallery
- **Description**: Gallery pages dynamically scan filesystem to discover albums
- **Modules**: pages/gallery, components/GalleryNav
- **Benefits**: No CMS required, simple album creation via folder structure

### Weather Data Integration
- **Description**: FieldWeather component fetches from multiple external APIs
- **Modules**: components/FieldWeather
- **Benefits**: Real-time field conditions, VFR/MVFR decision support
