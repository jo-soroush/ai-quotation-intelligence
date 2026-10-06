# V1-C20 Local Demo UI

This is a local, synthetic-only React/TypeScript presentation of the existing
FastAPI quotation workflow. The backend remains authoritative for commercial
values, evidence, review state, and Excel export.

## Run locally

From `frontend/`, use two terminals:

```text
npm run backend
npm run dev
```

Open `http://127.0.0.1:5173`. Vite proxies `/api` to the demo backend on
`127.0.0.1:8765`; no backend CORS change is required. The backend process uses
the existing FastAPI application factory, deterministic synthetic history,
real agent/tools/review/Excel paths, and a local scripted client injected at the
existing Bedrock adapter boundary. It makes no live AWS or Bedrock call.

The process-local quotation store is intentionally non-durable. Restarting the
backend clears review state. This demo does not claim production persistence,
multi-user safety, authentication, or public deployment readiness.

## Verify

```text
npm run typecheck
npm run build
npm test
PLAYWRIGHT_BROWSERS_PATH=.playwright-browsers npx playwright install chromium
npm run test:e2e
```

Generated `dist/`, browser binaries, Playwright reports, downloads, and
`node_modules/` are ignored and must not be committed.
