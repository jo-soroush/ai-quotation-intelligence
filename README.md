# AI Quotation Intelligence

This repository currently contains the V1-C01 repository and application baseline for a local-first AI Quotation Intelligence system.

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

The package baseline provides an environment-backed configuration boundary and standard-library logging setup. No quotation domain logic, AI provider integration, AWS integration, API behavior, or other future-Card implementation exists yet.

Copy `.env.example` to `.env` for optional local settings. Never commit `.env` or credentials.
