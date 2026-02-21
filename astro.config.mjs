import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';

import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://maconaeromodelers.com',
  base: '/',
  output: 'static',

  vite: {
    plugins: [tailwindcss()],
  },

  integrations: [react(), mdx()],
});