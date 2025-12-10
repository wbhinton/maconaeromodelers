# Macon Aero Modelers Website

Official website for Macon Aero Modelers - a model airplane flying club.

## 🚀 Live Site

The website is deployed at: [https://wbhinton.github.io/maconaeromodelers/](https://wbhinton.github.io/maconaeromodelers/)

## 📋 Pages

- **Home** - Welcome page with club information
- **Gallery** - Photo gallery of aircraft and events
- **Videos** - Video library and tutorials
- **Events** - Upcoming events and activities calendar
- **Contact** - Contact form and information
- **Resources** - Downloadable documents and helpful links
- **New Members** - Membership information and sign-up details

## 🛠️ Development

This site is built with [Astro](https://astro.build/), a modern static site generator.

### Prerequisites

- Node.js 18+ 
- npm or pnpm

### Installation

```bash
npm install
```

### Local Development

```bash
npm run dev
```

Visit `http://localhost:4321/maconaeromodelers/` to view the site.

### Build

```bash
npm run build
```

The built site will be in the `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

## 📦 Project Structure

```
/
├── public/
│   ├── favicon.svg
│   └── resources/          # Downloadable PDF files
├── src/
│   ├── layouts/
│   │   └── Layout.astro   # Base layout with navigation and footer
│   └── pages/             # All website pages
│       ├── index.astro
│       ├── gallery.astro
│       ├── videos.astro
│       ├── events.astro
│       ├── contact.astro
│       ├── resources.astro
│       └── new-members.astro
├── astro.config.mjs       # Astro configuration
└── package.json
```

## 🚢 Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch via GitHub Actions.

### Setup GitHub Pages

1. Go to repository Settings → Pages
2. Set Source to "GitHub Actions"
3. Push to main branch to trigger deployment

The deployment workflow is defined in `.github/workflows/deploy.yml`.

## 🎨 Customization

### Theme Colors

Edit the CSS variables in `src/layouts/Layout.astro`:

```css
:root {
  --primary-color: #0066cc;
  --secondary-color: #004499;
  --accent-color: #ff6600;
  /* ... */
}
```

### Adding Resources

1. Place PDF files in `public/resources/`
2. Update links in `src/pages/resources.astro`

### Adding Images

Place images in `public/images/` and reference them in your pages.

## 📝 License

ISC
