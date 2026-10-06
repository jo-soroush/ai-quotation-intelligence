import { afterEach, describe, expect, it, vi } from "vitest";
import { ApiError, quotationApi } from "./api";
import type { AgentInput } from "./types";
import { quoteFixture } from "./test/fixtures";

const payload: AgentInput = {
  request_id: "c20-contract",
  quotation_request: {
    project_name: "Synthetic contract case",
    currency: "SEK",
    requested_at: "2026-10-06T09:00:00Z",
    items: [{
      item_id: "contract-item",
      description: "Contract verification",
      estimated_hours: { value: "8", unit: "hours" },
      hourly_rate: { amount: "120", currency: "SEK" },
    }],
  },
};

afterEach(() => vi.unstubAllGlobals());

describe("typed API boundary", () => {
  it("constructs the exact current draft request including explicit hours unit", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({
      request_id: "c20-contract", status: "success", quote_id: "draft-c20-contract", message: "Draft for human review.",
    }), { status: 200, headers: { "content-type": "application/json" } }));
    vi.stubGlobal("fetch", fetchMock);

    await quotationApi.createDraft(payload);

    expect(fetchMock).toHaveBeenCalledWith("/api/quotes/draft", expect.objectContaining({ method: "POST" }));
    const body = JSON.parse(fetchMock.mock.calls[0][1].body as string) as AgentInput;
    expect(body).toEqual(payload);
    expect(body.quotation_request.items[0].estimated_hours.unit).toBe("hours");
  });

  it("maps the delivered GET presentation contract without recalculation", async () => {
    const quote = quoteFixture();
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(JSON.stringify(quote), {
      status: 200, headers: { "content-type": "application/json" },
    })));
    await expect(quotationApi.getQuote(quote.quote_id)).resolves.toEqual(quote);
  });

  it("preserves bounded backend error codes and hides arbitrary bodies", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(
      JSON.stringify({ code: "agent_unavailable", raw_error: "SECRET provider payload" }),
      { status: 503, headers: { "content-type": "application/json" } },
    )));
    const error = await quotationApi.createDraft(payload).catch((caught: unknown) => caught);
    expect(error).toEqual(expect.objectContaining({ kind: "backend", status: 503, code: "agent_unavailable" }));
    expect(String(error)).not.toContain("SECRET");
  });

  it("uses the existing approval shape and preserves HTTP denial", async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ code: "invalid_transition" }), {
      status: 409, headers: { "content-type": "application/json" },
    }));
    vi.stubGlobal("fetch", fetchMock);
    await expect(quotationApi.decide("draft-c20-contract", {
      status: "approved", reviewer_id: "synthetic-demo-reviewer", reason: "Synthetic review",
    })).rejects.toMatchObject({ status: 409, code: "invalid_transition" });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body as string)).toEqual({
      status: "approved", reviewer_id: "synthetic-demo-reviewer", reason: "Synthetic review",
    });
  });

  it("accepts only the real XLSX response contract", async () => {
    const blob = new Blob(["xlsx"], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response(blob, {
      status: 200,
      headers: { "content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" },
    })));
    await expect(quotationApi.exportQuote("draft-c20-contract")).resolves.toBeInstanceOf(Blob);

    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(new Response("not a workbook", {
      status: 200, headers: { "content-type": "text/plain" },
    })));
    await expect(quotationApi.exportQuote("draft-c20-contract")).rejects.toMatchObject({ code: "invalid_export_response" });
  });

  it("distinguishes a transport failure from a bounded backend error", async () => {
    vi.stubGlobal("fetch", vi.fn().mockRejectedValue(new TypeError("connection details must stay private")));
    const error = await quotationApi.createDraft(payload).catch((caught: unknown) => caught);
    expect(error).toEqual(expect.objectContaining({ kind: "transport", status: null, code: "network_unavailable" }));
    expect(String(error)).not.toContain("connection details");
  });
});
