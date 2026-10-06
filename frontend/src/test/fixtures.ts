import type { QuoteView } from "../types";

export function quoteFixture(reviewState: QuoteView["review_state"] = "awaiting_review"): QuoteView {
  return {
    quote_id: "draft-c20-demo",
    request_id: "c20-demo-request",
    status: "success",
    review_state: reviewState,
    message: "Validated historical risk evidence is linked to this draft for human review.",
    similar_quotes: [
      { quote_id: "synthetic-c03-quote-001", similarity_score: "0.88", matching_features: ["project category", "work mix"] },
    ],
    comparisons: [
      {
        quote_id: "synthetic-c03-quote-001",
        source_id: "synthetic-c03-source-001",
        hour_variance: { metric: "hours", unit: "hours", estimated: "43", actual: "54", variance: "11", percentage: "25.58" },
        cost_variance: null,
      },
    ],
    risk_evidence: [
      {
        metric: "hours",
        unit: "hours",
        comparable_project_count: 40,
        overrun_count: 30,
        overrun_rate: "0.75",
        average_variance: "11.8",
        median_variance: "10",
        source_quote_ids: ["synthetic-c03-quote-001"],
        evidence: [
          {
            evidence_id: "risk-hours-overrun-rate",
            metric: "overrun_rate",
            observed_value: "0.75",
            unit: "ratio",
            source_quote_ids: ["synthetic-c03-quote-001"],
            data_origin: "synthetic",
          },
        ],
      },
    ],
    draft_quote: {
      status: "draft",
      evidence_ids: ["risk-hours-overrun-rate"],
      risk_suggestions: [
        {
          suggestion_id: "risk-suggestion-1",
          severity: "medium",
          message: "Historical overrun evidence warrants human review.",
          evidence_ids: ["risk-hours-overrun-rate"],
          confidence: null,
        },
      ],
      quote: {
        quote_id: "draft-c20-demo",
        project_name: "Synthetic platform modernisation demo",
        currency: "SEK",
        items: [
          {
            item_id: "demo-discovery",
            description: "Platform discovery and solution design",
            estimated_hours: { value: "12", unit: "hours" },
            hourly_rate: { amount: "110", currency: "SEK" },
            actual_hours: null,
            actual_cost: null,
          },
        ],
        estimated_total_cost: { amount: "4620", currency: "SEK" },
        actual_total_cost: null,
        status: "draft",
        created_at: "2026-10-06T09:00:00Z",
        data_origin: "synthetic",
      },
    },
  };
}
