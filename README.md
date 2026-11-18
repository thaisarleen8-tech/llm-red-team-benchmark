# Llm Red Team Benchmark

Authorized adversarial LLM test cases, risk classification, and reproducible safety reports.

## Engineering scope

This is an independent portfolio project demonstrating typed domain logic,
deterministic behavior, automated tests, CI, explicit limitations, and reproducible
examples. It uses synthetic examples and does not claim employer sponsorship.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
ruff check .
```

## Quality and limitations

See `docs/architecture.md`, `CONTRIBUTING.md`, and `SECURITY.md`.
The current implementation is a focused foundation, not a production deployment.
Extend it with documented interfaces, integration tests, benchmarks, and operational
controls before describing it as production-ready.
