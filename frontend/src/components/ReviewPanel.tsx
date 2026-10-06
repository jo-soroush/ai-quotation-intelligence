import { useEffect, useRef, useState } from "react";
import type { DecisionStatus, QuoteView } from "../types";

interface ReviewPanelProps {
  quote: QuoteView;
  busy: boolean;
  exporting: boolean;
  onDecision: (status: DecisionStatus, reviewerId: string, reason: string) => Promise<void>;
  onExport: () => Promise<void>;
}

export function ReviewPanel({ quote, busy, exporting, onDecision, onExport }: ReviewPanelProps) {
  const [reviewerId, setReviewerId] = useState("synthetic-demo-reviewer");
  const [reason, setReason] = useState("");
  const [pending, setPending] = useState<DecisionStatus | null>(null);
  const confirmationButton = useRef<HTMLButtonElement>(null);
  const awaiting = quote.review_state === "awaiting_review";
  const approved = quote.review_state === "approved";

  useEffect(() => {
    if (pending) confirmationButton.current?.focus();
  }, [pending]);

  async function confirm() {
    if (!pending || !reviewerId.trim()) return;
    const status = pending;
    setPending(null);
    await onDecision(status, reviewerId.trim(), reason.trim());
  }

  return (
    <section className="panel review-panel" aria-labelledby="review-heading">
      <div className="panel-heading review-heading-row">
        <div>
          <p className="eyebrow">03 · Human authority</p>
          <h2 id="review-heading">Review and decide</h2>
          <p>The backend review state—not this screen—controls approval and export eligibility.</p>
        </div>
        <span className={`state-pill state-${quote.review_state}`}>{quote.review_state.replaceAll("_", " ")}</span>
      </div>

      <div className="review-layout">
        <div className="review-form">
          <label>
            <span>Reviewer reference</span>
            <input value={reviewerId} onChange={(event) => setReviewerId(event.target.value)} disabled={!awaiting || busy} />
            <small>This local synthetic actor demonstrates the human-owned review boundary; it is not a claim of real manual review.</small>
          </label>
          <label>
            <span>Decision note (optional)</span>
            <textarea value={reason} onChange={(event) => setReason(event.target.value)} disabled={!awaiting || busy} rows={3} placeholder="Synthetic portfolio review" />
          </label>
          {awaiting ? (
            <div className="decision-actions">
              <button className="button button-primary" type="button" onClick={() => setPending("approved")} disabled={busy || !reviewerId.trim()}>Approve quotation</button>
              <button className="button button-danger" type="button" onClick={() => setPending("rejected")} disabled={busy || !reviewerId.trim()}>Reject quotation</button>
            </div>
          ) : (
            <p className="decision-complete">Decision recorded by the backend: <strong>{quote.review_state}</strong>.</p>
          )}
        </div>

        <div className="export-card">
          <p className="eyebrow">04 · Excel output</p>
          <h3>Approved workbook</h3>
          <p>The workbook is generated and reconciled by the existing backend export path.</p>
          <button className="button button-export" type="button" onClick={onExport} disabled={!approved || busy || exporting}>
            {exporting ? <><span className="spinner dark" aria-hidden="true" /> Preparing workbook…</> : "Download Excel quotation"}
          </button>
          {!approved && <small>Export remains locked until the backend reports an approved state.</small>}
        </div>
      </div>

      {pending && (
        <div
          className="confirmation"
          role="alertdialog"
          aria-modal="true"
          aria-labelledby="confirm-title"
          onKeyDown={(event) => { if (event.key === "Escape") setPending(null); }}
        >
          <div>
            <p className="eyebrow">Confirm explicit decision</p>
            <h3 id="confirm-title">{pending === "approved" ? "Approve this draft?" : "Reject this draft?"}</h3>
            <p>This sends a one-time <strong>{pending}</strong> decision to the existing backend review boundary.</p>
            <div className="decision-actions">
              <button ref={confirmationButton} className={pending === "approved" ? "button button-primary" : "button button-danger"} type="button" onClick={confirm}>Confirm {pending === "approved" ? "approval" : "rejection"}</button>
              <button className="button button-secondary" type="button" onClick={() => setPending(null)}>Cancel</button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
