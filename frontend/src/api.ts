import type { AgentInput, AgentView, DecisionInput, DecisionView, QuoteView } from "./types";

export type ApiErrorKind = "backend" | "transport" | "invalid_response";

export class ApiError extends Error {
  constructor(
    public readonly kind: ApiErrorKind,
    public readonly status: number | null,
    public readonly code: string,
  ) {
    super(code);
    this.name = "ApiError";
  }
}

async function readError(response: Response): Promise<ApiError> {
  let code = "request_failed";
  try {
    const payload: unknown = await response.json();
    if (
      typeof payload === "object" &&
      payload !== null &&
      "code" in payload &&
      typeof payload.code === "string" &&
      /^[a-z_]{1,64}$/.test(payload.code)
    ) {
      code = payload.code;
    }
  } catch {
    // The bounded public code is the only backend detail shown to the UI.
  }
  return new ApiError("backend", response.status, code);
}

async function requestJson<T>(path: string, init: RequestInit, signal?: AbortSignal): Promise<T> {
  let response: Response;
  try {
    response = await fetch(`/api${path}`, {
      ...init,
      signal,
      headers: { "Content-Type": "application/json", Accept: "application/json", ...init.headers },
    });
  } catch (error) {
    if (error instanceof DOMException && error.name === "AbortError") throw error;
    throw new ApiError("transport", null, "network_unavailable");
  }
  if (!response.ok) throw await readError(response);
  try {
    return (await response.json()) as T;
  } catch {
    throw new ApiError("invalid_response", response.status, "invalid_response");
  }
}

export const quotationApi = {
  createDraft(payload: AgentInput, signal?: AbortSignal): Promise<AgentView> {
    return requestJson<AgentView>("/quotes/draft", { method: "POST", body: JSON.stringify(payload) }, signal);
  },

  getQuote(quoteId: string, signal?: AbortSignal): Promise<QuoteView> {
    return requestJson<QuoteView>(`/quotes/${encodeURIComponent(quoteId)}`, { method: "GET" }, signal);
  },

  decide(quoteId: string, payload: DecisionInput, signal?: AbortSignal): Promise<DecisionView> {
    return requestJson<DecisionView>(`/quotes/${encodeURIComponent(quoteId)}/approve`, {
      method: "POST",
      body: JSON.stringify(payload),
    }, signal);
  },

  async exportQuote(quoteId: string): Promise<Blob> {
    let response: Response;
    try {
      response = await fetch(`/api/quotes/${encodeURIComponent(quoteId)}/export`, {
        method: "POST",
        headers: { Accept: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" },
      });
    } catch {
      throw new ApiError("transport", null, "network_unavailable");
    }
    if (!response.ok) throw await readError(response);
    const contentType = response.headers.get("content-type")?.split(";", 1)[0];
    if (contentType !== "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") {
      throw new ApiError("invalid_response", response.status, "invalid_export_response");
    }
    return response.blob();
  },
};
