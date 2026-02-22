# Macon Aero Modelers Website (AMA Club #492)
Welcome to the official repository for the Macon Aero Modelers (OTX AeroDrome) website.

This site is built to be modern, fast, and extremely low-maintenance. It uses a **Static Site Generation (SSG)** architecture, meaning there is no traditional backend server or database to manage. Content is updated automatically via external integrations or simple file uploads.

## 🚀 Quick Start

### Prerequisites
*   **Node.js** (v18 or higher)
*   **npm**

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/wbhinton/maconaeromodelers.git
    cd maconaeromodelers
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Start the development server:**
    ```bash
    npm run dev
    ```
    The site will be available at `http://localhost:4321/`.

## 🛠 Tech Stack & Architecture

We chose this stack to minimize costs (free hosting) and maintenance effort.

*   **Framework**: [Astro](https://astro.build) - A modern web framework optimized for speed.
*   **Styling**: [Tailwind CSS](https://tailwindcss.com) - Utility-first CSS framework.
*   **Language**: TypeScript / JavaScript.
*   **Hosting**: GitHub Pages with custom domain [maconaeromodelers.com](https://maconaeromodelers.com).

## 🧩 Key Features & Integrations

### 1. 🌦️ Weather System (Serverless)
The weather widget on the homepage and "Field Info" page combines data from two sources to give pilots a complete picture:
*   **Field Data (Wind/Gusts)**: Fetched from our on-site Ambient Weather station. We use a **Cloudflare Worker** as a secure proxy to hide our API keys.
*   **Aviation Data (Ceiling/Vis)**: Fetched from the nearest airport (K1A5) using NOAA METAR text services.

### 2. 📅 Events (Automated)
*   **Source**: The club's Google Calendar.
*   **How it works**: The site fetches the public `.ics` calendar feed at build time.
*   **Update Process**: Simply add an event to the Google Calendar, and the site updates automatically on the next build. No code changes required.

### 3. 🖼️ Photo Gallery (File-Based)
*   **How it works**: The gallery is generated automatically from the file system.
*   **Update Process**:
    1.  Create a folder in `public/assets/gallery/{YEAR}/{EVENT_NAME}`.
    2.  Drop your photos in.
    3.  (Optional) Add a simple `info.json` for metadata.
    The site scans these folders and builds the gallery page for you.

### 4. 📬 Contact Form (Web3Forms)
*   **Service**: [Web3Forms](https://web3forms.com/).
*   **How it works**: Submissions are sent directly to club officers' emails. This allows us to have a working contact form without a backend server.

### 5. 📘 Member Handbook (Custom System)
*   **Implementation**: Custom integration using **Astro Content Collections** and **Tailwind Typography**.
*   **Why**: We built this custom system instead of using Starlight to ensure the documentation pages inherit the main site's styling perfectly.
*   **Content**: Documentation is written in standard Markdown files located in `src/content/docs`.

## 📂 Project Structure

```text
/
├── public/
│   └── assets/
│       ├── gallery/           # Gallery images (Year > Event > Photos)
│       └── images/            # Static site assets (Logos, hero banners)
├── src/
│   ├── components/            # Reusable UI (Navbar, WeatherWidget, Footer)
│   ├── content/
│   │   └── docs/              # Member Handbook content (Markdown)
│   ├── layouts/               # Main page wrappers
│   └── pages/                 # Website routes (index.astro, events.astro, etc.)
├── astro.config.mjs           # Configuration for Astro & Integrations
└── tailwind.config.mjs        # Design system tokens (colors, fonts)
```

## 🚢 Deployment

The site is deployed automatically to GitHub Pages.

1.  Push changes to the `main` branch.
2.  A **GitHub Action** triggers automatically.
3.  The action builds the site and deploys it to the `gh-pages` branch.
4.  Updates are live within minutes.

## 🤝 Contributing

We welcome contributions!
1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes.
4.  Open a Pull Request.