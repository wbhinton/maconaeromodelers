import typography from '@tailwindcss/typography';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // Your Custom Palette
        primary: {
          DEFAULT: '#0369a1', // Sky-700
          hover: '#0284c7',   // Sky-600 (A bit lighter for hover states)
        },
        secondary: '#475569', // Slate-600
        background: {
          DEFAULT: '#ffffff', // White
          alt: '#f8fafc',     // Slate-50
        },
        alert: '#f59e0b',     // Amber-500
        success: '#059669',   // Emerald-600
        error: '#dc2626',     // Red-600
        
        // Text colors (derived from Slate for softer contrast than pure black)
        text: {
            dark: '#1e293b',  // Slate-800
            light: '#64748b', // Slate-500
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [
    typography, // <--- CHANGED: Uses the imported variable instead of require()
  ],
}