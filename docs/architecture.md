# Architecture

The project keeps deterministic domain logic inside `src/llm_redteam` and tests
behavior under `tests/`. External services, storage systems, and model providers are
intentionally not required by the initial implementation.

## Design principles

- Validate inputs at system boundaries.
- Keep core behavior deterministic and testable.
- Preserve evidence and provenance for evaluation outputs.
- Document assumptions and known limitations.
- Add integrations behind explicit interfaces rather than coupling them to core logic.
