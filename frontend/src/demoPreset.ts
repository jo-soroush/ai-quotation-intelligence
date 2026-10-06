import type { AgentInput } from "./types";

export const SYNTHETIC_PRESET_NAME = "Synthetic platform modernisation demo";

export function syntheticPreset(): AgentInput["quotation_request"] {
  return {
    project_name: SYNTHETIC_PRESET_NAME,
    currency: "SEK",
    requested_at: "2026-10-06T09:00:00.000Z",
    items: [
      {
        item_id: "demo-discovery",
        description: "Platform discovery and solution design",
        estimated_hours: { value: "12", unit: "hours" },
        hourly_rate: { amount: "110", currency: "SEK" },
      },
      {
        item_id: "demo-delivery",
        description: "Synthetic platform implementation",
        estimated_hours: { value: "20", unit: "hours" },
        hourly_rate: { amount: "125", currency: "SEK" },
      },
      {
        item_id: "demo-validation",
        description: "Integration and quality validation",
        estimated_hours: { value: "8", unit: "hours" },
        hourly_rate: { amount: "100", currency: "SEK" },
      },
    ],
  };
}
