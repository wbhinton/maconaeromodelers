# Macon Aero Modelers Website

This is the official website for the **Macon Aero Modelers** RC Club (OTX AeroDrome), built using [Astro](https://astro.build) and [Tailwind CSS](https://tailwindcss.com).

The site is designed to be **static**, fast, and easy to maintain. It is deployed automatically via GitHub Pages.

## 🚀 Quick Start

To run this project locally on your machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/wbhinton/maconaeromodelers.git](https://github.com/wbhinton/maconaeromodelers.git)
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
    Open your browser to `http://localhost:4321/maconaeromodelers/`.

## 📂 Project Structure

Here are the key files and folders you need to know about:

```text
/
├── public/
│   └── assets/
│       ├── gallery/           <-- PHOTO UPLOADS GO HERE (See "Updating Gallery")
│       └── images/            <-- Static site images (Hero banners, logos)
├── src/
│   ├── components/            <-- Reusable UI (Navbar, Footer, WeatherWidget)
│   ├── content/
│   │   └── docs/              <-- STARLIGHT CONTENT (Member Handbook)
│   │       └── docs/
│   │           ├── governance/
│   │           ├── membership/
│   │           └── safety/
│   ├── layouts/               <-- Main HTML wrapper (Layout.astro)
│   └── pages/                 <-- Site Pages (Routes)
│       ├── index.astro        <-- Homepage
│       ├── events.astro       <-- Events (Google Calendar logic)
│       ├── gallery.astro      <-- Gallery Index (Automated)
│       ├── contact.astro      <-- Contact Form
│       ├── field-info.astro   <-- Maps & Weather
│       ├── new-members.astro  <-- Join Info & Dues
│       └── resources.astro    <-- Pilot Documents & Links
├── astro.config.mjs           <-- Astro Config (Starlight Sidebar & Integrations)
└── tailwind.config.mjs        <-- Styling & Color Palette

## 🛠️ How to Update Content

We have designed the site to be "Low Code" for common updates.

### 1. Updating the Member Handbook (Starlight)
The "Member Handbook" section (`/docs/`) uses the **Starlight** theme. Content is stored as Markdown (`.md`) files.

**To edit existing rules:**
1.  Navigate to `src/content/docs/docs/`.
2.  Open the relevant folder (`governance`, `safety`, or `membership`).
3.  Edit the `.md` file directly.

**To add a NEW page:**
1.  Create a new `.md` file in the appropriate subfolder.
2.  Add the required "frontmatter" at the top of the file:
    ```markdown
    ---
    title: My New Page Title
    description: A short description of this section.
    ---
    Your content goes here...
    ```
3.  **Crucial Step:** Open `astro.config.mjs` in the root folder.
4.  Scroll down to the `starlight` configuration and add your new page to the `sidebar` array so it appears in the menu.

### 2. Updating the Photo Gallery
The gallery is **fully automated**. You do not need to write code to add new albums.

1.  Navigate to `public/assets/gallery/`.
2.  Open the folder for the current year (e.g., `2025`). If it's a new year, create a new folder (e.g., `2026`).
3.  **Create a folder** for your event (e.g., `spring-fly-in`).
4.  **Drag and drop** your photos (`.jpg`, `.png`, `.webp`) into that folder.
5.  **(Optional)** Add a file named `info.json` inside the event folder to set the title and cover image:
    ```json
    {
      "title": "Spring Fly-In",
      "date": "May 15, 2025",
      "description": "Great turnout with over 30 pilots.",
      "cover": "my-favorite-pic.jpg"
    }
    ```

### 3. Updating Events
The Events page (`src/pages/events.astro`) automatically fetches data from the club's **Google Calendar**.
* **To add an event:** Simply add it to the Google Calendar associated with the club.
* **To change the Calendar Source:** Open `src/pages/events.astro` and update the `GOOGLE_ICAL_URL` constant.

## 🎨 Theme & Color Palette

The site uses a specific color scheme defined in `tailwind.config.mjs`. Use these utility classes to keep the design consistent.

| Semantic Name | Tailwind Class | Hex Code (Approx) | Usage |
| :--- | :--- | :--- | :--- |
| **Primary Blue** | `text-primary` / `bg-primary` | `#1e40af` (Blue-800) | Main buttons, headers, links |
| **Secondary** | `text-secondary` / `bg-secondary` | `#1e3a8a` (Blue-900) | Footer backgrounds, hero overlays |
| **Accent/Alert** | `text-alert` / `bg-alert` | `#dc2626` (Red-600) | Safety warnings, important notices |
| **Background** | `bg-background` | `#ffffff` | Main page background |
| **Alt Background** | `bg-background-alt` | `#f3f4f6` (Gray-100) | Section alternates, cards |

## 🔌 Third-Party Integrations & Tech Stack

This site relies on specific external services to function without a backend server.

### 1. Weather System (Custom Build)
We built a custom weather widget (`src/components/FieldWeather.astro`) that combines data from two sources:
* **On-Site Data:** Real-time wind/gusts from the club's Ambient Weather Station (OTX).
    * *Implementation:* Data is fetched via a **Cloudflare Worker** acting as a proxy to fetch data securely from the Ambient Weather API without exposing keys.
* **Aviation Data:** Cloud ceiling and visibility (METAR) fetched from the nearest airport (`K1A5`) via the NOAA/NWS text service.

### 2. Contact Form
* **Service:** [Web3Forms](https://web3forms.com/).
* **Function:** Handles form submissions and delivers emails to club officers without requiring a backend server.
* **Configuration:** Access Key is stored in `src/pages/contact.astro`.

### 3. Google Calendar
* **Function:** Powers the "Upcoming Events" section.
* **Implementation:** Fetches the public `.ics` feed at build time and parses it to generate event cards.

## 🔮 Future Plans & Roadmap

### Discord & SMS Bridge
We have established a Discord server for member communication.
* **Goal:** Build a "Bridge Bot" that connects Discord announcements to an SMS gateway.
* **Use Case:** When a "Field Open/Closed" announcement is made in Discord, it will automatically text members who have opted-in (useful for members without smartphones or data at the field).

## 🔐 Security & Privacy

* **Email Obfuscation:** Club officer emails on the Contact page are encoded using HTML Entities to prevent scraping by spam bots.
* **Contact Form:** Uses Web3Forms with Honeypot spam protection (`botcheck`).
* **No Database:** This is a static site; there is no database to hack.

## 🚀 Deployment

The site is hosted on **GitHub Pages**.

**To deploy updates:**
1.  Commit your changes (including new photos in `public/` or docs in `src/content/`).
2.  Push to the `main` branch.
3.  GitHub Actions will automatically build the site and deploy it. This usually takes 1-2 minutes.