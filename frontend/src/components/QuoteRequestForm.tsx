import { useMemo, useState } from "react";
import { syntheticPreset } from "../demoPreset";
import type { AgentInput } from "../types";

interface EditableItem {
  key: number;
  itemId: string;
  description: string;
  hours: string;
  rate: string;
}

interface FormState {
  projectName: string;
  currency: string;
  items: EditableItem[];
}

interface QuoteRequestFormProps {
  busy: boolean;
  onSubmit: (payload: AgentInput) => Promise<void>;
}

let requestSequence = 0;

function blankItem(key: number): EditableItem {
  return { key, itemId: `work-${key}`, description: "", hours: "", rate: "" };
}

function initialForm(): FormState {
  return { projectName: "", currency: "SEK", items: [blankItem(1)] };
}

function nextRequestId(): string {
  requestSequence += 1;
  return `c20-demo-${Date.now().toString(36)}-${requestSequence}`;
}

export function QuoteRequestForm({ busy, onSubmit }: QuoteRequestFormProps) {
  const [form, setForm] = useState<FormState>(initialForm);
  const [formError, setFormError] = useState<string | null>(null);
  const nextKey = useMemo(() => Math.max(0, ...form.items.map((item) => item.key)) + 1, [form.items]);

  function updateItem(key: number, field: keyof Omit<EditableItem, "key">, value: string) {
    setForm((current) => ({
      ...current,
      items: current.items.map((item) => item.key === key ? { ...item, [field]: value } : item),
    }));
  }

  function loadPreset() {
    const preset = syntheticPreset();
    setForm({
      projectName: preset.project_name,
      currency: preset.currency,
      items: preset.items.map((item, index) => ({
        key: index + 1,
        itemId: item.item_id,
        description: item.description,
        hours: item.estimated_hours.value,
        rate: item.hourly_rate.amount,
      })),
    });
    setFormError(null);
  }

  async function submit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const currency = form.currency.trim().toUpperCase();
    const invalid = !form.projectName.trim() || !/^[A-Z]{3}$/.test(currency) || form.items.some(
      (item) => !item.itemId.trim() || !item.description.trim() || item.hours === "" || item.rate === ""
        || !Number.isFinite(Number(item.hours)) || Number(item.hours) < 0
        || !Number.isFinite(Number(item.rate)) || Number(item.rate) < 0,
    );
    if (invalid) {
      setFormError("Complete every work item with a description, non-negative hours, rate, and a three-letter currency.");
      return;
    }
    setFormError(null);
    await onSubmit({
      request_id: nextRequestId(),
      quotation_request: {
        project_name: form.projectName.trim(),
        currency,
        requested_at: new Date().toISOString(),
        items: form.items.map((item) => ({
          item_id: item.itemId.trim(),
          description: item.description.trim(),
          estimated_hours: { value: item.hours, unit: "hours" },
          hourly_rate: { amount: item.rate, currency },
        })),
      },
    });
  }

  return (
    <section className="panel request-panel" aria-labelledby="request-heading">
      <div className="panel-heading request-heading-row">
        <div>
          <p className="eyebrow">01 · Quotation request</p>
          <h2 id="request-heading">Define the work</h2>
          <p>Commercial inputs are sent to the backend exactly as entered. The browser never calculates the quote total.</p>
        </div>
        <button className="button button-secondary" type="button" onClick={loadPreset} disabled={busy}>
          Load synthetic example
        </button>
      </div>

      <form onSubmit={submit} noValidate>
        <div className="form-grid form-grid-top">
          <label>
            <span>Project name</span>
            <input
              name="projectName"
              value={form.projectName}
              onChange={(event) => setForm({ ...form, projectName: event.target.value })}
              placeholder="Synthetic platform discovery"
              required
              disabled={busy}
            />
          </label>
          <label>
            <span>Currency</span>
            <input
              name="currency"
              value={form.currency}
              onChange={(event) => setForm({ ...form, currency: event.target.value })}
              maxLength={3}
              required
              disabled={busy}
            />
          </label>
        </div>

        <div className="items-header">
          <div>
            <h3>Work items</h3>
            <p>Hours use the explicit API unit <strong>hours</strong>.</p>
          </div>
          <button
            className="text-button"
            type="button"
            onClick={() => setForm({ ...form, items: [...form.items, blankItem(nextKey)] })}
            disabled={busy || form.items.length >= 40}
          >
            + Add work item
          </button>
        </div>

        <div className="work-items">
          {form.items.map((item, index) => (
            <fieldset className="work-item" key={item.key}>
              <legend>Item {index + 1}</legend>
              <label className="item-id">
                <span>Item ID</span>
                <input value={item.itemId} onChange={(event) => updateItem(item.key, "itemId", event.target.value)} disabled={busy} required />
              </label>
              <label className="item-description">
                <span>Description</span>
                <input value={item.description} onChange={(event) => updateItem(item.key, "description", event.target.value)} disabled={busy} required />
              </label>
              <label>
                <span>Estimated hours</span>
                <div className="input-with-suffix">
                  <input aria-label={`Item ${index + 1} estimated hours`} inputMode="decimal" value={item.hours} onChange={(event) => updateItem(item.key, "hours", event.target.value)} disabled={busy} required />
                  <span>hours</span>
                </div>
              </label>
              <label>
                <span>Hourly rate</span>
                <div className="input-with-suffix">
                  <input aria-label={`Item ${index + 1} hourly rate`} inputMode="decimal" value={item.rate} onChange={(event) => updateItem(item.key, "rate", event.target.value)} disabled={busy} required />
                  <span>{form.currency.toUpperCase() || "currency"}</span>
                </div>
              </label>
              {form.items.length > 1 && (
                <button className="remove-button" type="button" onClick={() => setForm({ ...form, items: form.items.filter((candidate) => candidate.key !== item.key) })} disabled={busy} aria-label={`Remove item ${index + 1}`}>
                  Remove
                </button>
              )}
            </fieldset>
          ))}
        </div>

        {formError && <p className="inline-error" role="alert">{formError}</p>}
        <div className="form-actions">
          <p className="authority-note"><span aria-hidden="true">◆</span> Backend validation and arithmetic remain authoritative.</p>
          <button className="button button-primary" type="submit" disabled={busy}>
            {busy ? <><span className="spinner" aria-hidden="true" /> Analyzing request…</> : "Analyze & create draft"}
          </button>
        </div>
      </form>
    </section>
  );
}
