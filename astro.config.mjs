import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://wbhinton.github.io',
  base: '/maconaeromodelers/',
  output: 'static',

  vite: {
    plugins: [tailwindcss()],
  },

  integrations: [
    react(),
    starlight({
      title: 'Macon Aero Modelers Docs',
      disable404Route: true,
      // defaultTheme: 'light',
      customCss: ['./src/styles/starlight.css'],
      // Note: We removed the 'integrations' block from inside Starlight

      sidebar: [
        {
          label: 'Start Here',
          items: [
            { label: 'Overview', slug: 'docs' },
          ],
        },
        {
          label: 'Club Info',
          items: [
            { label: 'Constitution & Bylaws', slug: 'docs/governance/constitution' },
          ],
        },
        {
          label: 'Safety & Operations',
          items: [
             { label: 'Field Rules', slug: 'docs/safety/field-rules' },
          ],
        },
        {
          label: 'Membership',
          items: [
            { label: 'How to Join', slug: 'docs/membership/joining' },
          ],
        },
      ],
    }),
  ],
});