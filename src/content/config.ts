import { defineCollection, z } from 'astro:content';
import { docsSchema } from '@astrojs/starlight/schema';

// export const collections = {
//   // This connects the 'docs' folder to Starlight
//   docs: defineCollection({ schema: docsSchema() }),
// };

// 1. Define the schema for your news posts
const newsCollection = defineCollection({
  type: 'content', // v2.5+ uses 'content' for markdown
  schema: z.object({
    title: z.string(),
    date: z.date(),
    author: z.string().default('Club Secretary'),
    description: z.string(),
    // Optional image for the card
    image: z.string().optional(),
  }),
});

export const collections = {
  docs: defineCollection({ schema: docsSchema() }),
  // 2. Export the new collection
  news: newsCollection, 
};