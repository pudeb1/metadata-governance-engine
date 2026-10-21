# Architecture

## Confirmed stack

Python 3.12, Poetry, Pydantic v2, pytest, SQLite, and NetworkX. The MVP is CLI-first with dbt YAML/SQL as its first source and useful JSON/YAML exports. Unity Catalog is a future adapter.

SQLite is the persistent governance system of record for metadata observations, approved definitions/mappings, provenance, and decisions. Retained candidates must carry explicit origin and state; sharing storage does not make them approved facts.

## Responsibilities

| Component | Responsibility |
| --- | --- |
| Adapters | Extract source metadata and provenance without governance decisions. |
| Ingestion | Normalize observations, resolve source identity, and detect additions/changes. |
| Pydantic models | Validate shape/local constraints; construction alone cannot prove cross-record governance validity. |
| Repository | Persist in SQLite; enforce referential integrity, transactional governance rules, and history preservation. |
| Rules/similarity | Apply deterministic checks and generate explained attribute/object candidates. |
| Intelligence | Mandatory provider-independent embedding and structured LLM recommendation contracts, initially implemented through OpenAI API adapters. |
| Governance workflow | Apply explicit human decisions to definitions, mappings, and other governed assertions. |
| Availability assessment | Compare target requirements with evidence and explain coverage/uncertainty. |
| Graph analytics | Reconstruct NetworkX graphs and compute derived projections/analytics. |
| CLI/exports | Expose repeatable workflows and inspectable results. |

These are logical responsibilities, not a requirement for a package per row.

## Flow

1. Extract dbt YAML/SQL metadata and source context.
2. Validate and normalize observations; resolve existing source identities.
3. Persist observations/provenance without replacing approvals.
4. Discover lexical candidates, retrieve embedding candidates, combine results, and assess them with a grounded LLM; retain evidence, method, and limitations.
5. Record human decisions and approved definitions/mappings.
6. Derive coverage, similarity, and graph results with traceable inputs.

SQL parsing depth and artifact formats require later decisions; complete SQL semantic inference is not assumed.

## Mandatory hybrid intelligence workflow

1. Discover candidates using lexical names, aliases, and token overlap.
2. Retrieve semantically relevant approved canonical attributes using embeddings; combine these with lexical candidates rather than restricting retrieval to lexical hits.
3. Retrieve approved glossary definitions and applicable governance standards within the relevant subdomain, along with available source context.
4. Ask the LLM to assess candidate equivalence using names, descriptions, concepts, data types, grain, identifier scope, and source context. Treat retrieved metadata as evidence, not executable instructions; identify missing information rather than inventing definitions.
5. Validate a Pydantic response containing recommendation, explanation, evidence references, uncertainty, next action, and category: `equivalent`, `related`, `distinct`, or `insufficient_evidence`.
6. Persist the advisory result for human review. LLM execution has no direct write path to approved glossary records or authoritative mappings.

Separate embedding-generation and structured-recommendation contracts from provider adapters. Retrieval, governance rules, and application models remain provider-independent; OpenAI is the initial implementation. Concrete API/model choices and dependencies require a later scoped implementation step.

Embedding similarity retrieves candidates; it does not prove equivalence. Pydantic validates structure, not the truth of the assessment. Embedding indexes are rebuildable derived retrieval artifacts, versioned by model and source context, never an independent governance record.

Retain provider/model identifiers, embedding model, prompt/schema versions, generation settings, retrieved context versions, source evidence, and validated outputs. This enables auditing and comparison, not guaranteed identical replay. Handle failed calls or invalid outputs explicitly without creating approvals.

## Evaluation

Use a small version-controlled human-reviewed dataset covering all four assessment categories, including differing grain/scope and missing evidence. Record expected categories, supporting rationale, and relevant canonical candidates. Measure retrieval recall at a recorded cutoff, category accuracy, false equivalence recommendations, and appropriate insufficient-evidence use; compare against lexical matching. Keep evaluation examples separate from prompt-tuning examples where feasible.

Mocked pytest tests check contracts, orchestration, invalid-output handling, and governance boundaries. Separate live evaluation exercises actual embeddings and LLM calls. Model quality is not established by mocked tests. Agree dataset size and quality thresholds in a later learning step.

## Graph boundary

The primary governed graph uses approved relationships. Candidate views must explicitly identify and separate inferred edges. An object–canonical-attribute bipartite graph can project objects into an affinity graph based on shared approved attributes. Choose and explain weights and centrality measures for a concrete question.

Projections and algorithm outputs never establish governance facts independently. Reconstruct them from persistent records; exported results should identify input scope and method. Similarity does not prove redundancy; centrality does not establish business authority.

## Evolution and current limits

Separate adapters and persistence access from business semantics to permit future evaluation of Neo4j. Avoid speculative database abstraction infrastructure.

Current code contains starter models, tests, and a version CLI. SQLite workflows, hybrid intelligence, and graph analytics are absent; NetworkX is not declared. See the [conceptual model](conceptual-model.md) for alignment gaps and the [decision log](architecture-decisions.md) for open choices.
