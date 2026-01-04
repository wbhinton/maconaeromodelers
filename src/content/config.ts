import { defineCollection, z } from 'astro:content';

// 1. Define the Docs Schema (Manual version, no Starlight)
const docsCollection = defineCollection({
  type: 'content', 
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    order: z.number().default(99), // Sort order for sidebar
  }),
});

// 2. Your News Schema
const newsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.date(),
    author: z.string().default('Club Secretary'),
    description: z.string(),
    image: z.string().optional(),
  }),
});

// 3. Export collections using the correct variable names
export const collections = {
  docs: docsCollection,
  news: newsCollection, 
};