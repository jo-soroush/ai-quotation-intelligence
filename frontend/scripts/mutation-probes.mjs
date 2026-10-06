import { spawnSync } from "node:child_process";
import { cpSync, mkdtempSync, readFileSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

const frontend = resolve(import.meta.dirname, "..");

const mutations = [
  {
    name: "client total substituted for backend total",
    file: "src/components/EvidencePanel.tsx",
    search: "total.amount",
    replacement: '"9999"',
    test: "src/App.test.tsx",
  },
  {
    name: "approval/export enabled after backend denial",
    file: "src/components/ReviewPanel.tsx",
    search: 'const approved = quote.review_state === "approved";',
    replacement: "const approved = true;",
    test: "src/App.test.tsx",
  },
  {
    name: "API failure rendered without failure state",
    file: "src/App.tsx",
    search: "setError(safeError(caught));",
    replacement: "setError(null);",
    test: "src/App.test.tsx",
  },
  {
    name: "AI interpretation relabeled as deterministic evidence",
    file: "src/components/EvidencePanel.tsx",
    search: "AI-selected interpretation",
    replacement: "Deterministic evidence",
    test: "src/App.test.tsx",
  },
  {
    name: "synthetic-data disclosure removed",
    file: "src/App.tsx",
    search: "Local synthetic demo",
    replacement: "Local portfolio demo",
    test: "src/App.test.tsx",
  },
  {
    name: "fabricated duplicate RiskEvidence displayed",
    file: "src/components/EvidencePanel.tsx",
    search: "quote.risk_evidence.length ? quote.risk_evidence.map((report) => (",
    replacement: "quote.risk_evidence.length ? [...quote.risk_evidence, quote.risk_evidence[0]].map((report) => (",
    test: "src/App.test.tsx",
  },
  {
    name: "unsafe model-text HTML rendering introduced",
    file: "src/components/EvidencePanel.tsx",
    search: '<p className="ai-message">{quote.message ?? "No permitted agent message was returned."}</p>',
    replacement: '<p className="ai-message" dangerouslySetInnerHTML={{ __html: quote.message ?? "No permitted agent message was returned." }} />',
    test: "src/security.test.ts",
  },
  {
    name: "raw backend error payload exposed",
    file: "src/api.ts",
    search: "code = payload.code;",
    replacement: "code = JSON.stringify(payload);",
    test: "src/api.test.ts",
  },
  {
    name: "frontend-generated fake workbook",
    file: "src/App.tsx",
    search: "const blob = await quotationApi.exportQuote(quote.quote_id);",
    replacement: 'const blob = new Blob(["fake workbook"]);',
    test: "src/App.test.tsx",
  },
  {
    name: "frontend bypasses HTTP boundary",
    file: "src/types.ts",
    search: "export type AgentResultStatus",
    replacement: "// ai_quotation_intelligence direct backend access\nexport type AgentResultStatus",
    test: "src/security.test.ts",
  },
  {
    name: "process-local limitation hidden",
    file: "src/App.tsx",
    search: "Quotation review state is held in one process.",
    replacement: "Quotation review state is reliable across processes.",
    test: "src/App.test.tsx",
  },
];

const results = [];
for (const mutation of mutations) {
  const directory = mkdtempSync(join(tmpdir(), "aqi-c20-mutant-"));
  try {
    cpSync(frontend, directory, {
      recursive: true,
      filter: (source) => !["node_modules", "dist", ".playwright-browsers", "test-results", "playwright-report"].includes(source.split("/").at(-1)),
    });
    symlinkSync(join(frontend, "node_modules"), join(directory, "node_modules"), "dir");
    const target = join(directory, mutation.file);
    const original = readFileSync(target, "utf8");
    if (!original.includes(mutation.search)) throw new Error(`mutation anchor missing: ${mutation.name}`);
    writeFileSync(target, original.replace(mutation.search, mutation.replacement));
    const run = spawnSync("npm", ["test", "--", "--run", mutation.test], {
      cwd: directory,
      encoding: "utf8",
      env: { ...process.env, NO_COLOR: "1" },
    });
    const result = run.status === 0 ? "NOT_CAUGHT" : "CAUGHT";
    results.push({ name: mutation.name, result });
    console.log(`${result}: ${mutation.name}`);
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
}

console.log("NOT_APPLICABLE: stale response overwrite (the UI serializes submissions and disables all request-changing controls while in flight)");
if (results.some(({ result }) => result === "NOT_CAUGHT")) process.exitCode = 1;
