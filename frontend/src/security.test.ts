import { readFileSync, readdirSync } from "node:fs";
import { extname, join } from "node:path";
import { describe, expect, it } from "vitest";

function sourceFiles(directory: string): string[] {
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const path = join(directory, entry.name);
    return entry.isDirectory() ? sourceFiles(path) : [path];
  }).filter((path) => [".ts", ".tsx"].includes(extname(path)) && !path.endsWith(".test.ts") && !path.endsWith(".test.tsx"));
}

describe("frontend boundary invariants", () => {
  const sources = sourceFiles(join(process.cwd(), "src"))
    .map((path) => [path, readFileSync(path, "utf8")] as const);

  it("has no unsafe HTML, browser storage, secret, or backend-internal access path", () => {
    for (const [path, text] of sources) {
      expect(text, path).not.toContain("dangerouslySetInnerHTML");
      expect(text, path).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
      expect(text, path).not.toMatch(/AKIA[0-9A-Z]{16}/);
      expect(text, path).not.toContain("ai_quotation_intelligence");
      expect(text, path).not.toContain("evaluation/c19");
    }
  });

  it("contains no authoritative commercial calculation expression", () => {
    const production = sources.map(([, text]) => text).join("\n");
    expect(production).not.toMatch(/estimated_hours\s*\*\s*hourly_rate/);
    expect(production).not.toMatch(/reduce\([^\n]*(?:amount|rate|cost|hours)/i);
    expect(production).not.toContain("calculateQuote");
  });

  it("keeps visible keyboard focus styling in the presentation contract", () => {
    const styles = readFileSync(join(process.cwd(), "src", "styles.css"), "utf8");
    expect(styles).toContain(":focus-visible");
  });
});
