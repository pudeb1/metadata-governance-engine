# Metadata Governance Engine

A Python project for subdomain-level metadata governance and attribute harmonization across data products. It will recommend semantic equivalences, support human approval of a canonical glossary, and map physical columns to approved definitions without requiring column renaming.

## Current status

The scaffold contains Pydantic models, three model-validation tests, and a minimal `mge --version` CLI. Adapter, ingestion, repository, similarity, rules, and intelligence packages are placeholders.

Ingestion, SQLite persistence, approval workflows, hybrid lexical/embedding/LLM recommendations, availability assessment, and graph analytics are not implemented. Existing models and configuration still contain enterprise/domain assumptions requiring separately approved alignment with subdomain glossary ownership. NetworkX is not yet declared as a dependency.

## Mandatory intelligence capability

The MVP must run a provider-independent hybrid recommendation workflow, initially through an OpenAI API implementation: lexical discovery, embedding retrieval, glossary/standards context retrieval, and LLM assessment with validated Pydantic outputs. Human approval is required before mappings become authoritative; the LLM cannot modify approved glossary records.

A small human-reviewed evaluation dataset will measure recommendation quality. This workflow is required but not implemented yet.

## Development setup

Use Python 3.12 with Poetry. For a local checkout using pyenv:

```bash
pyenv install -s 3.12.13
pyenv local 3.12.13
poetry env use 3.12
poetry install
poetry run pytest
poetry run mge --version
```

These are developer instructions; agents must follow [AGENTS.md](AGENTS.md) approval boundaries before installing dependencies or modifying files.

## Documentation

- [Project charter](docs/project-charter.md): purpose, learning goals, scope, non-goals.
- [MVP requirements](docs/mvp-requirements.md): workflows and acceptance outcomes.
- [Conceptual model](docs/conceptual-model.md): entities, relationships, unresolved questions.
- [Architecture](docs/architecture.md): implementation boundaries and metadata flow.
- [Architecture decisions](docs/architecture-decisions.md): status, reasoning, trade-offs.
- [Agent agreement](AGENTS.md): incremental teaching and implementation rules.

Documentation describes the agreed target; the scaffold does not yet implement it fully.
