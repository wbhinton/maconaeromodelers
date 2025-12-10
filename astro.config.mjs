import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import starlight from '@astrojs/starlight';
import react from '@astrojs/react';

// https://astro.build/config
export default defineConfig({
  site: 'https://wbhinton.github.io',
  base: '/maconaeromodelers/',
  output: 'static',
  // REMOVED the 'plugins' block from here
  integrations: [
    tailwind(), // This will automatically look for tailwind.config.mjs
    react(),
    starlight({
      title: 'Macon Aero Modelers Docs',
      disable404Route: true,
      customCss: ['./src/styles/starlight.css'],
      sidebar: [
        {
          label: 'Start Here',
          items: [
            { label: 'Overview', slug: 'docs' },
          ],
        },
      ],
    }),
  ],
});