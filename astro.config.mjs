import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import starlight from '@astrojs/starlight';
import react from '@astrojs/react';

// https://astro.build/config
export default defineConfig({

  site: 'https://wbhinton.github.io',
  base: '/maconaeromodelers/',
  output: 'static',
  plugins: [
    require('@tailwindcss/typography'),
  ],
  integrations: [
    tailwind(),
    react(),
    
    starlight({
      title: 'Macon Aero Modelers Docs',
      disable404Route: true, // Let your main theme handle 404s

      customCss: ['./src/styles/starlight.css'],
      sidebar: [
        {
          label: 'Start Here',
          items: [
            // The slug 'docs' points to src/content/docs/docs/index.md
            { label: 'Overview', slug: 'docs' },
          ],
        },
      ],
    }),
  ],
});
