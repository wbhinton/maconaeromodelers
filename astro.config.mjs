import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwindcss from '@tailwindcss/vite';

import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://maconaeromodelers.com',
  base: '/',
  output: 'static',
  redirects: {
    '/airfield-&-map': '/location',
    '/faa-notice-to-flyers': '/rules',
    '/safety.php': '/',
    '/techtalk.php': '/',
    '/safetynews.php': '/',
    '/remotemem.php': '/',
    '/prposts.php': '/',
    '/propspinners.php': '/',
    '/commodore7_24.php': '/',
    '/commodore8_14.php': '/',
    '/safetynews020511.php': '/',
    '/safety_checklist2018.php': '/',
    '/safetynews030412.php': '/',
    '/safetynews071411.php': '/',
    '/safetynews081306.php': '/',
    '/safetynews081812.php': '/',
    '/safetynews082809.php': '/',
    '/safetynews091708.php': '/',
    '/techtalk020106.php': '/',
    '/techtalk030306.php': '/',
  },

  vite: {
    plugins: [tailwindcss()],
  },

  build: {
    inlineStylesheets: 'always',
  },

  integrations: [react(), mdx()],
});