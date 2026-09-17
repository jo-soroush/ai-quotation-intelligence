# AI Quotation Intelligence

This repository contains the implemented V1-C01–V1-C07 foundation and the V1-C08
provider-isolated Amazon Bedrock integration for an AI Quotation Intelligence system.

## Development setup

The project targets Python 3.13 or newer. Use the local virtual environment when available:

```bash
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Run the baseline tests with:

```bash
pytest
```

The current foundation provides:

- environment-backed configuration and standard-library logging;
- typed quotation domain models with explicit Decimal, hours, currency, and provenance boundaries;
- deterministic synthetic historical quotation data;
- deterministic quotation calculation and total reconciliation;
- historical estimate-versus-actual comparison; and
- deterministic, explainable similar-quotation retrieval; and
- deterministic, traceable risk-evidence statistics with explicit insufficient-evidence handling; and
- configurable Amazon Bedrock Converse integration using Amazon Nova Micro, with
  validated responses and controlled provider failures. Deterministic Core logic
  remains authoritative for commercial calculations and evidence.

V1-C09 and later capabilities are not implemented. This includes agent tools and
quotation-agent orchestration, human review workflow, Excel generation, FastAPI,
S3, AWS deployment, CloudWatch, evaluation/failure handling, and the demo UI.

For current Card lifecycle and authorization state, see [PROJECT_CONTROL.md](PROJECT_CONTROL.md). This README is project-facing documentation, not live-state authority.

Copy `.env.example` to `.env` for optional local settings. Never commit `.env` or credentials.
