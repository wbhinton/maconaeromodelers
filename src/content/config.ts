import { defineCollection } from 'astro:content';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
  // This connects the 'docs' folder to Starlight
  docs: defineCollection({ schema: docsSchema() }),
};