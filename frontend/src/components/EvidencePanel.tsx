import type { QuoteView, VarianceResult } from "../types";

function displayDecimal(value: string, maximumFractionDigits = 2): string {
  const numeric = Number(value);
  return Number.isFinite(numeric)
    ? new Intl.NumberFormat("en-US", { maximumFractionDigits }).format(numeric)
    : value;
}

function Value({ value, unit, maximumFractionDigits }: {
  value: string | null;
  unit: string;
  maximumFractionDigits?: number;
}) {
  return <span>{value === null ? "Not available" : `${displayDecimal(value, maximumFractionDigits)} ${unit}`}</span>;
}

function VarianceRow({ value }: { value: VarianceResult }) {
  return (
    <div className="variance-row">
      <div><span>Estimated</span><Value value={value.estimated} unit={value.unit} /></div>
      <div><span>Actual</span><Value value={value.actual} unit={value.unit} /></div>
      <div><span>Variance</span><Value value={value.variance} unit={value.unit} /></div>
      <div><span>Percentage</span><Value value={value.percentage} unit="%" maximumFractionDigits={1} /></div>
    </div>
  );
}

export function EvidencePanel({ quote }: { quote: QuoteView }) {
  const total = quote.draft_quote.quote.estimated_total_cost;
  return (
    <section className="results-stack" aria-labelledby="results-heading">
      <div className="panel result-summary">
        <div>
          <p className="eyebrow">02 · Backend result</p>
          <h2 id="results-heading">Draft intelligence</h2>
          <p className="quote-reference">Quote {quote.quote_id}</p>
        </div>
        <div className="total-card" aria-label="Backend-calculated quotation total">
          <span>Backend-calculated total</span>
          <strong>{total ? `${total.amount} ${total.currency}` : "Not available"}</strong>
          <small>Deterministic Core result</small>
        </div>
      </div>

      <div className="evidence-grid">
        <section className="panel evidence-panel deterministic-panel" aria-labelledby="similar-heading">
          <div className="evidence-label"><span aria-hidden="true">D</span> Deterministic evidence</div>
          <h3 id="similar-heading">Comparable quotations</h3>
          {quote.similar_quotes.length ? (
            <div className="table-scroll">
              <table>
                <thead><tr><th>Quotation</th><th>Similarity</th><th>Matching signals</th></tr></thead>
                <tbody>{quote.similar_quotes.map((item) => (
                  <tr key={item.quote_id}>
                    <td><code>{item.quote_id}</code></td>
                    <td>{displayDecimal(item.similarity_score, 3)}</td>
                    <td>{item.matching_features.join(", ") || "No matching feature label"}</td>
                  </tr>
                ))}</tbody>
              </table>
            </div>
          ) : <p className="empty-state">The backend returned no comparable quotations.</p>}
        </section>

        <section className="panel evidence-panel deterministic-panel" aria-labelledby="comparison-heading">
          <div className="evidence-label"><span aria-hidden="true">D</span> Deterministic evidence</div>
          <h3 id="comparison-heading">Estimate vs actual</h3>
          {quote.comparisons.length ? quote.comparisons.slice(0, 5).map((item) => (
            <article className="comparison-card" key={`${item.quote_id}-${item.source_id}`}>
              <div className="comparison-title"><code>{item.quote_id}</code><span>Source {item.source_id}</span></div>
              {item.hour_variance ? <VarianceRow value={item.hour_variance} /> : <p className="empty-state">No hour outcome was available.</p>}
            </article>
          )) : <p className="empty-state">The backend returned no estimate/actual comparisons.</p>}
        </section>

        <section className="panel evidence-panel deterministic-panel risk-panel" aria-labelledby="risk-heading">
          <div className="evidence-label"><span aria-hidden="true">D</span> Deterministic evidence</div>
          <h3 id="risk-heading">Risk evidence</h3>
          {quote.risk_evidence.length ? quote.risk_evidence.map((report) => (
            <article className="risk-report" key={`${report.metric}-${report.unit}`}>
              <div className="metric-strip">
                <div><span>Comparable projects</span><strong>{report.comparable_project_count}</strong></div>
                <div><span>Overrun observations</span><strong>{report.overrun_count}</strong></div>
                <div><span>Overrun rate</span><strong>{displayDecimal(report.overrun_rate, 2)}</strong></div>
                <div><span>Average variance</span><strong>{displayDecimal(report.average_variance, 2)} {report.unit}</strong></div>
                <div><span>Median variance</span><strong>{displayDecimal(report.median_variance, 2)} {report.unit}</strong></div>
              </div>
              <div className="provenance-list">
                {report.evidence.map((item) => (
                  <div key={item.evidence_id}>
                    <div><strong>{item.metric.replaceAll("_", " ")}</strong><code>{item.evidence_id}</code></div>
                    <p>{displayDecimal(item.observed_value, 2)} {item.unit} · {item.data_origin} · {item.source_quote_ids.length} source quotation(s)</p>
                  </div>
                ))}
              </div>
            </article>
          )) : <p className="empty-state">No structured RiskEvidence was returned.</p>}
        </section>

        <section className="panel evidence-panel ai-panel" aria-labelledby="ai-heading">
          <div className="evidence-label ai-label"><span aria-hidden="true">AI</span> AI-selected interpretation</div>
          <h3 id="ai-heading">Draft interpretation</h3>
          <p className="ai-message">{quote.message ?? "No permitted agent message was returned."}</p>
          {quote.draft_quote.risk_suggestions.length ? (
            <div className="suggestion-list">{quote.draft_quote.risk_suggestions.map((suggestion) => (
              <article key={suggestion.suggestion_id}>
                <span className={`severity severity-${suggestion.severity}`}>{suggestion.severity}</span>
                <p>{suggestion.message}</p>
                <small>References: {suggestion.evidence_ids.join(", ")}</small>
              </article>
            ))}</div>
          ) : <p className="empty-state">No AI-selected risk suggestion was included.</p>}
          <p className="ai-disclaimer">Interpretation is constrained and unapproved. Deterministic evidence and human review remain authoritative.</p>
        </section>
      </div>
    </section>
  );
}
