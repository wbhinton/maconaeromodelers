# Patterns

Implementation patterns and idioms for Macon Aero Modelers website.

## Naming Conventions

### Files
- PascalCase for components (.astro)
- kebab-case for pages/dirs
- snake_case for config files

### Functions
- camelCase
- Descriptive names (joinPath, fixPath, getCardinal)

### Imports
- Relative paths from src/ (../layouts/Layout.astro)
- Absolute for content

## Type Patterns

### Data Modeling
- Astro content collections with Zod schemas for docs and news

### Type Strictness
- TypeScript interfaces for component Props
- Zod for content validation

## Error Handling

### Strategy
- Client-side try/catch in fetch functions
- Graceful degradation (-- values)

### Propagation
- Console.error for client errors
- No server-side errors in static build

## Validation

### Location
- Zod schemas in content/config.ts for build-time validation

### Method
- Zod schema validation
- Optional fields with defaults

## Observability

### Logging
- Console.error/warn for client-side errors only

### Metrics
- Google Analytics via gtag.js script injection

### Tracing
- None detected

## Testing

- No test files in codebase

## IO Patterns

### Database
- None - static site with content collections

### HTTP Clients
- Fetch API in client-side scripts
- Cloudflare Worker proxy for weather data
