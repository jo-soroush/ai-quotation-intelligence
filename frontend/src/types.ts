export type AgentResultStatus = "success" | "invalid" | "unavailable" | "insufficient_evidence";
export type ReviewState = "awaiting_review" | "approved" | "rejected";
export type DecisionStatus = "approved" | "rejected";

export interface HoursInput {
  value: string;
  unit: "hours";
}

export interface MoneyInput {
  amount: string;
  currency: string;
}

export interface QuoteItemInput {
  item_id: string;
  description: string;
  estimated_hours: HoursInput;
  hourly_rate: MoneyInput;
}

export interface AgentInput {
  request_id: string;
  quotation_request: {
    project_name: string;
    currency: string;
    items: QuoteItemInput[];
    requested_at: string;
  };
  instructions?: string;
}

export interface AgentView {
  request_id: string;
  status: AgentResultStatus;
  quote_id: string | null;
  message: string | null;
}

export interface Money {
  amount: string;
  currency: string;
}

export interface Hours {
  value: string;
  unit: "hours";
}

export interface QuoteItem {
  item_id: string;
  description: string;
  estimated_hours: Hours;
  hourly_rate: Money;
  actual_hours: Hours | null;
  actual_cost: Money | null;
}

export interface RiskSuggestion {
  suggestion_id: string;
  severity: "low" | "medium" | "high" | "unknown";
  message: string;
  evidence_ids: string[];
  confidence: string | null;
}

export interface DraftQuote {
  status: "draft" | "validated" | "awaiting_review" | "approved" | "rejected";
  quote: {
    quote_id: string;
    project_name: string;
    currency: string;
    items: QuoteItem[];
    estimated_total_cost: Money | null;
    actual_total_cost: Money | null;
    status: "draft" | "validated" | "awaiting_review" | "approved" | "rejected";
    created_at: string;
    data_origin: "synthetic" | "real" | "unknown";
  };
  risk_suggestions: RiskSuggestion[];
  evidence_ids: string[];
}

export interface SimilarQuoteView {
  quote_id: string;
  similarity_score: string;
  matching_features: string[];
}

export interface VarianceResult {
  metric: string;
  unit: string;
  estimated: string | null;
  actual: string | null;
  variance: string | null;
  percentage: string | null;
}

export interface ComparisonView {
  quote_id: string;
  source_id: string;
  hour_variance: VarianceResult | null;
  cost_variance: VarianceResult | null;
}

export interface RiskEvidenceView {
  evidence_id: string;
  metric: string;
  observed_value: string;
  unit: string;
  source_quote_ids: string[];
  data_origin: "synthetic" | "real" | "unknown";
}

export interface RiskEvidenceReportView {
  metric: string;
  unit: string;
  comparable_project_count: number;
  overrun_count: number;
  overrun_rate: string;
  average_variance: string;
  median_variance: string;
  evidence: RiskEvidenceView[];
  source_quote_ids: string[];
}

export interface QuoteView {
  quote_id: string;
  request_id: string;
  status: AgentResultStatus;
  review_state: ReviewState;
  draft_quote: DraftQuote;
  message: string | null;
  similar_quotes: SimilarQuoteView[];
  comparisons: ComparisonView[];
  risk_evidence: RiskEvidenceReportView[];
}

export interface DecisionInput {
  status: DecisionStatus;
  reviewer_id: string;
  reason?: string;
}

export interface DecisionView {
  quote_id: string;
  review_state: ReviewState;
  reviewer_id: string;
}
