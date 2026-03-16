# Architecture

System architecture for Macon Aero Modelers website.

## Patterns

### Static Site Generator
- **Evidence**: Astro configured with output: 'static', builds to static HTML/CSS/JS
- **Description**: Pre-rendered static pages deployed to CDN

### Component-Based UI
- **Evidence**: @astrojs/react integration, React components in static pages
- **Description**: React used for interactive islands within static Astro pages

### Utility-First CSS
- **Evidence**: Tailwind CSS with custom color palette in tailwind.config.mjs
- **Description**: Atomic CSS classes for styling with custom club colors

## Layers

### Presentation Layer
- **Purpose**: User-facing pages and components
- **Components**: Astro pages (.astro files), React components, MDX content

### Build Layer
- **Purpose**: Static site generation and asset processing
- **Components**: Astro build engine, Vite bundler with Tailwind plugin, MDX processor

### Deployment Layer
- **Purpose**: CI/CD to GitHub Pages
- **Components**: .github/workflows/deploy.yml
- **Dependencies**: Build Layer

## Interactions

### Content Authoring
1. Author writes MDX content
2. Astro processes MDX with React components
3. Tailwind scans and generates atomic CSS

### Deployment
1. Developer pushes to main branch
2. GitHub Actions triggers deploy workflow
3. Astro action builds and uploads artifact
4. GitHub Pages deploys static site

## Integrations

| Service | Purpose | Type |
|---------|---------|------|
| GitHub Pages | Static site hosting | hosting |
| Google Analytics 4 | Website analytics tracking | analytics |
| Tailwind Typography | Beautiful prose styling for MDX | styling plugin |

## Data Flow

### State Management
- **Strategy**: Static generation - no runtime state
- **Location**: Build-time generated files
- **Lifecycle**: Content → Build → Static HTML → Deploy → CDN

### Data Flows

**Site Generation**
- Input: MDX files, React components, assets
- Processing: Astro compiles MDX + React → Vite bundles → Tailwind purges unused CSS
- Output: Static HTML/CSS/JS in dist/

**Analytics Injection**
- Input: PUBLIC_GA_MEASUREMENT_ID from .env
- Processing: Injected at build time via import.meta.env
- Output: GA script tag in HTML head

## Deployment

- **Type**: Static Site
- **Environment**: GitHub Pages
- **Distribution**: CDN via GitHub Pages with custom domain

## Diagram

```mermaid
graph TB
    subgraph Content
      MDX[MDX Content] ←→ React[React Components]
    end
    
    subgraph Build
      Astro[Astro SSG] → Vite[Vite Bundler]
      Vite → Tailwind[Tailwind CSS]
    end
    
    subgraph Deploy
      GitHub[GitHub Actions] → Pages[GitHub Pages]
    end
    
    Content → Build
    Build → Deploy
    
    Analytics[Google Analytics 4] → Pages
```
