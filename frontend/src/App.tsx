import { useEffect, useRef, useState } from "react";
import { ApiError, quotationApi } from "./api";
import { EvidencePanel } from "./components/EvidencePanel";
import { QuoteRequestForm } from "./components/QuoteRequestForm";
import { ReviewPanel } from "./components/ReviewPanel";
import type { AgentInput, DecisionStatus, QuoteView } from "./types";
import "./styles.css";

type WorkflowStatus = "idle" | "submitting" | "ready" | "reviewing" | "exporting" | "failed";

const FRIENDLY_ERRORS: Readonly<Record<string, string>> = {
  invalid_request: "The backend rejected the request. Check every required commercial value and explicit unit.",
  agent_invalid: "The provider response did not pass the system's validation boundary.",
  agent_unavailable: "The AI provider is unavailable. No quotation was created.",
  insufficient_evidence: "The backend could not find enough validated evidence to create this draft.",
  invalid_decision: "The backend rejected the review decision.",
  invalid_transition: "That review transition is not allowed by the backend.",
  approval_required: "Backend approval is required before Excel export.",
  export_reconciliation_failed: "The workbook did not reconcile with authoritative quotation data.",
  export_failed: "The backend could not generate a valid Excel workbook.",
  quote_not_found: "The process-local quote is no longer available. Create a new draft in this session.",
  network_unavailable: "The local API is not reachable. Confirm that the demo backend is running.",
  invalid_export_response: "The backend did not return a valid Excel response.",
  invalid_response: "The local API returned an unreadable response.",
  request_failed: "The request failed without a recognized public error code.",
};

function safeError(error: unknown): string {
  if (error instanceof ApiError) return FRIENDLY_ERRORS[error.code] ?? FRIENDLY_ERRORS.request_failed;
  return FRIENDLY_ERRORS.request_failed;
}

function WorkflowRail({ quote, status }: { quote: QuoteView | null; status: WorkflowStatus }) {
  const steps = [
    { label: "Request", active: true, done: quote !== null },
    { label: "Evidence", active: quote !== null, done: quote !== null },
    { label: "Review", active: quote !== null, done: quote?.review_state !== "awaiting_review" && quote !== null },
    { label: "Export", active: quote?.review_state === "approved", done: status === "ready" && quote?.review_state === "approved" },
  ];
  return (
    <nav className="workflow-rail" aria-label="Quotation workflow">
      {steps.map((step, index) => (
        <div className={`workflow-step ${step.active ? "is-active" : ""} ${step.done ? "is-done" : ""}`} key={step.label}>
          <span>{step.done ? "✓" : index + 1}</span><strong>{step.label}</strong>
        </div>
      ))}
    </nav>
  );
}

export default function App() {
  const [quote, setQuote] = useState<QuoteView | null>(null);
  const [status, setStatus] = useState<WorkflowStatus>("idle");
  const [message, setMessage] = useState<string>("Ready for a synthetic quotation request.");
  const [error, setError] = useState<string | null>(null);
  const requestVersion = useRef(0);
  const activeRequest = useRef<AbortController | null>(null);

  useEffect(() => () => activeRequest.current?.abort(), []);

  async function submit(payload: AgentInput) {
    activeRequest.current?.abort();
    const controller = new AbortController();
    activeRequest.current = controller;
    const version = ++requestVersion.current;
    setStatus("submitting");
    setQuote(null);
    setError(null);
    setMessage("The backend agent is validating inputs and collecting evidence.");
    try {
      const draft = await quotationApi.createDraft(payload, controller.signal);
      if (!draft.quote_id) throw new ApiError("invalid_response", 200, "invalid_response");
      const current = await quotationApi.getQuote(draft.quote_id, controller.signal);
      if (version !== requestVersion.current) return;
      setQuote(current);
      setStatus("ready");
      setMessage("Draft and deterministic evidence returned by the backend. Human review is required.");
    } catch (caught) {
      if (caught instanceof DOMException && caught.name === "AbortError") return;
      if (version !== requestVersion.current) return;
      setStatus("failed");
      setError(safeError(caught));
      setMessage("No successful draft was created.");
    }
  }

  async function decide(decision: DecisionStatus, reviewerId: string, reason: string) {
    if (!quote) return;
    setStatus("reviewing");
    setError(null);
    setMessage(`Submitting the explicit ${decision} decision to the backend.`);
    try {
      await quotationApi.decide(quote.quote_id, {
        status: decision,
        reviewer_id: reviewerId,
        ...(reason ? { reason } : {}),
      });
      const current = await quotationApi.getQuote(quote.quote_id);
      setQuote(current);
      setStatus("ready");
      setMessage(decision === "approved"
        ? "The backend recorded approval. Excel export is now available."
        : "The backend recorded rejection. Export remains unavailable.");
    } catch (caught) {
      setStatus("failed");
      setError(safeError(caught));
      setMessage("The backend did not accept the review decision.");
    }
  }

  async function exportWorkbook() {
    if (!quote || quote.review_state !== "approved") return;
    setStatus("exporting");
    setError(null);
    setMessage("The backend is generating and reconciling the Excel workbook.");
    try {
      const blob = await quotationApi.exportQuote(quote.quote_id);
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = "Draft_Quote.xlsx";
      document.body.append(anchor);
      anchor.click();
      anchor.remove();
      URL.revokeObjectURL(url);
      setStatus("ready");
      setMessage("The genuine backend-generated Excel quotation was downloaded.");
    } catch (caught) {
      setStatus("failed");
      setError(safeError(caught));
      setMessage("No workbook was downloaded.");
    }
  }

  const busy = ["submitting", "reviewing"].includes(status);
  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href="#main" aria-label="Quotation Intelligence home">
          <span className="brand-mark" aria-hidden="true"><i /><i /><i /></span>
          <span><strong>Quotation Intelligence</strong><small>Evidence-led commercial drafting</small></span>
        </a>
        <div className="demo-badge"><span aria-hidden="true" /> Local synthetic demo</div>
      </header>

      <main id="main">
        <section className="hero">
          <div>
            <p className="eyebrow">AI-assisted · Human-approved</p>
            <h1>Turn quotation inputs into <em>evidence-backed</em> decisions.</h1>
            <p className="hero-copy">A professional local demonstration of deterministic commercial calculations, synthetic historical evidence, bounded AI interpretation, and explicit human review.</p>
          </div>
          <aside className="scope-card">
            <span>Demo boundary</span>
            <strong>Synthetic data only</strong>
            <p>No customer data, live Bedrock, cloud call, authentication, or production persistence.</p>
          </aside>
        </section>

        <WorkflowRail quote={quote} status={status} />

        <div className={`status-banner status-${error ? "error" : "info"}`} role="status" aria-live="polite">
          <span aria-hidden="true">{error ? "!" : "i"}</span>
          <div>
            <strong>{error ? "Action needed" : "Workflow status"}</strong>
            <p>{error ?? message}</p>
            {error && <p className="status-outcome">{message}</p>}
          </div>
        </div>

        <QuoteRequestForm busy={busy} onSubmit={submit} />
        {quote && <EvidencePanel quote={quote} />}
        {quote && <ReviewPanel quote={quote} busy={busy} exporting={status === "exporting"} onDecision={decide} onExport={exportWorkbook} />}

        <section className="limitation-note" aria-label="Local demo limitation">
          <strong>Local session boundary</strong>
          <p>Quotation review state is held in one process. Restarting the backend clears the demo session; this interface does not claim durable or multi-user persistence.</p>
        </section>
      </main>

      <footer><span>AI Quotation Intelligence · V1 portfolio demonstration</span><span>Backend truth · Evidence before claims · Human approval</span></footer>
    </div>
  );
}
