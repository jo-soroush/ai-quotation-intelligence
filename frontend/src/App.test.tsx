import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import App from "./App";
import { ApiError, quotationApi } from "./api";
import { quoteFixture } from "./test/fixtures";

describe("C20 quotation workflow", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    vi.spyOn(quotationApi, "createDraft").mockResolvedValue({
      request_id: "c20-demo-request", status: "success", quote_id: "draft-c20-demo", message: "Draft for human review.",
    });
    vi.spyOn(quotationApi, "getQuote").mockResolvedValue(quoteFixture());
    vi.spyOn(quotationApi, "decide").mockResolvedValue({
      quote_id: "draft-c20-demo", review_state: "approved", reviewer_id: "synthetic-demo-reviewer",
    });
    vi.spyOn(quotationApi, "exportQuote").mockResolvedValue(new Blob(["xlsx"], {
      type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    }));
  });

  afterEach(() => vi.restoreAllMocks());

  async function createDraft(user = userEvent.setup()) {
    render(<App />);
    await user.click(screen.getByRole("button", { name: /load synthetic example/i }));
    await user.click(screen.getByRole("button", { name: /analyze & create draft/i }));
    await screen.findByRole("heading", { name: /draft intelligence/i });
    return user;
  }

  it("discloses synthetic scope and constructs multiple explicit-unit work items", async () => {
    const user = userEvent.setup();
    render(<App />);
    expect(screen.getAllByText(/synthetic demo/i).length).toBeGreaterThan(0);
    expect(screen.getByText(/one process/i)).toBeInTheDocument();

    await user.click(screen.getByRole("button", { name: /load synthetic example/i }));
    expect(screen.getAllByRole("group")).toHaveLength(3);
    await user.click(screen.getByRole("button", { name: /analyze & create draft/i }));

    const sent = vi.mocked(quotationApi.createDraft).mock.calls[0][0];
    expect(sent.quotation_request.items).toHaveLength(3);
    expect(sent.quotation_request.items.every((item) => item.estimated_hours.unit === "hours")).toBe(true);
    expect(sent.quotation_request.items.every((item) => item.hourly_rate.currency === "SEK")).toBe(true);
  });

  it("keeps primary controls keyboard reachable and exposes semantic status", async () => {
    const user = userEvent.setup();
    render(<App />);
    expect(screen.getByRole("status")).toHaveTextContent(/ready for a synthetic quotation request/i);
    await user.tab();
    expect(screen.getByRole("link", { name: /quotation intelligence home/i })).toHaveFocus();
    await user.tab();
    const preset = screen.getByRole("button", { name: /load synthetic example/i });
    expect(preset).toHaveFocus();
    await user.keyboard("{Enter}");
    expect(screen.getByLabelText(/project name/i)).toHaveValue("Synthetic platform modernisation demo");
  });

  it("renders backend totals, comparisons, provenance, and AI interpretation as separate authorities", async () => {
    await createDraft();
    expect(screen.getByLabelText(/backend-calculated quotation total/i)).toHaveTextContent("4620 SEK");
    expect(screen.getByRole("heading", { name: /comparable quotations/i })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /estimate vs actual/i })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: /risk evidence/i })).toBeInTheDocument();
    expect(screen.getByText("risk-hours-overrun-rate")).toBeInTheDocument();
    expect(screen.getByText(/AI-selected interpretation/i)).toBeInTheDocument();
    expect(screen.getByText(/unapproved.*deterministic evidence.*human review/i)).toBeInTheDocument();
  });

  it("keeps export disabled until explicit backend approval and downloads backend bytes", async () => {
    const user = await createDraft();
    const download = screen.getByRole("button", { name: /download excel quotation/i });
    expect(download).toBeDisabled();

    vi.mocked(quotationApi.getQuote).mockResolvedValueOnce(quoteFixture("approved"));
    await user.click(screen.getByRole("button", { name: /approve quotation/i }));
    const confirm = screen.getByRole("button", { name: /confirm approval/i });
    expect(confirm).toHaveFocus();
    await user.click(confirm);
    await waitFor(() => expect(quotationApi.decide).toHaveBeenCalledWith(
      "draft-c20-demo",
      expect.objectContaining({ status: "approved", reviewer_id: "synthetic-demo-reviewer" }),
    ));
    await waitFor(() => expect(download).toBeEnabled());
    await user.click(download);
    await waitFor(() => expect(quotationApi.exportQuote).toHaveBeenCalledWith("draft-c20-demo"));
    expect(URL.createObjectURL).toHaveBeenCalled();
    expect(screen.getByText(/genuine backend-generated Excel quotation was downloaded/i)).toBeInTheDocument();
  });

  it("preserves backend rejection and never enables export", async () => {
    const user = await createDraft();
    vi.mocked(quotationApi.getQuote).mockResolvedValueOnce(quoteFixture("rejected"));
    await user.click(screen.getByRole("button", { name: /reject quotation/i }));
    await user.click(screen.getByRole("button", { name: /confirm rejection/i }));
    await screen.findByText(/backend recorded rejection/i);
    expect(screen.getByRole("button", { name: /download excel quotation/i })).toBeDisabled();
    expect(quotationApi.exportQuote).not.toHaveBeenCalled();
  });

  it("shows sanitized provider failure and no fabricated success content", async () => {
    vi.mocked(quotationApi.createDraft).mockRejectedValueOnce(
      new ApiError("backend", 503, "agent_unavailable"),
    );
    const user = userEvent.setup();
    render(<App />);
    await user.click(screen.getByRole("button", { name: /load synthetic example/i }));
    await user.click(screen.getByRole("button", { name: /analyze & create draft/i }));
    expect(await screen.findByText(/AI provider is unavailable/i)).toBeInTheDocument();
    expect(screen.getByText(/No successful draft was created/i)).toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /draft intelligence/i })).not.toBeInTheDocument();
  });

  it.each([
    ["agent_invalid", /did not pass the system's validation boundary/i],
    ["insufficient_evidence", /could not find enough validated evidence/i],
    ["network_unavailable", /local API is not reachable/i],
  ])("presents %s without a false successful draft", async (code, expected) => {
    vi.mocked(quotationApi.createDraft).mockRejectedValueOnce(
      new ApiError(code === "network_unavailable" ? "transport" : "backend", code === "network_unavailable" ? null : 422, code),
    );
    const user = userEvent.setup();
    render(<App />);
    await user.click(screen.getByRole("button", { name: /load synthetic example/i }));
    await user.click(screen.getByRole("button", { name: /analyze & create draft/i }));
    expect(await screen.findByText(expected)).toBeInTheDocument();
    expect(screen.getByText(/No successful draft was created/i)).toBeInTheDocument();
    expect(screen.queryByRole("heading", { name: /draft intelligence/i })).not.toBeInTheDocument();
  });

  it("keeps backend decision denial authoritative", async () => {
    const user = await createDraft();
    vi.mocked(quotationApi.decide).mockRejectedValueOnce(
      new ApiError("backend", 409, "invalid_transition"),
    );
    await user.click(screen.getByRole("button", { name: /approve quotation/i }));
    await user.click(screen.getByRole("button", { name: /confirm approval/i }));
    expect(await screen.findByText(/review transition is not allowed/i)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /download excel quotation/i })).toBeDisabled();
  });

  it("reports export failure without fabricating a download", async () => {
    vi.mocked(quotationApi.getQuote).mockResolvedValue(quoteFixture("approved"));
    vi.mocked(quotationApi.exportQuote).mockRejectedValueOnce(new ApiError("backend", 500, "export_failed"));
    const user = await createDraft();
    await user.click(screen.getByRole("button", { name: /download excel quotation/i }));
    expect(await screen.findByText(/could not generate a valid Excel workbook/i)).toBeInTheDocument();
    expect(screen.getByText(/No workbook was downloaded/i)).toBeInTheDocument();
    expect(URL.createObjectURL).not.toHaveBeenCalled();
  });

  it("shows honest empty evidence states", async () => {
    vi.mocked(quotationApi.getQuote).mockResolvedValueOnce({
      ...quoteFixture(), similar_quotes: [], comparisons: [], risk_evidence: [],
    });
    await createDraft();
    expect(screen.getByText(/no comparable quotations/i)).toBeInTheDocument();
    expect(screen.getByText(/no estimate\/actual comparisons/i)).toBeInTheDocument();
    expect(screen.getByText(/no structured RiskEvidence/i)).toBeInTheDocument();
  });

  it("prevents double submission while the current request is in flight", async () => {
    let resolveDraft: ((value: Awaited<ReturnType<typeof quotationApi.createDraft>>) => void) | undefined;
    vi.mocked(quotationApi.createDraft).mockImplementationOnce(() => new Promise((resolve) => { resolveDraft = resolve; }));
    const user = userEvent.setup();
    render(<App />);
    await user.click(screen.getByRole("button", { name: /load synthetic example/i }));
    const submit = screen.getByRole("button", { name: /analyze & create draft/i });
    await user.click(submit);
    expect(screen.getByRole("button", { name: /analyzing request/i })).toBeDisabled();
    expect(quotationApi.createDraft).toHaveBeenCalledTimes(1);
    resolveDraft?.({ request_id: "c20-demo-request", status: "success", quote_id: "draft-c20-demo", message: null });
    await screen.findByRole("heading", { name: /draft intelligence/i });
  });
});
