/** @type {import('tailwindcss').Config} */
import typography from '@tailwindcss/typography';

export default {
  // This tells Tailwind where to look for class names
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // We can re-define your club colors here so 'text-primary' works in your docs
        primary: '#1e40af', 
        secondary: '#475569',
        alert: '#f59e0b',
        'text-dark': '#1e293b',
        background: '#ffffff',
      },
    },
  },
  plugins: [
    typography,
  ],
}