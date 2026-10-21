# Architecture decisions

**Accepted** means agreed; **Proposed** remains unresolved; **Superseded** preserves an earlier choice with a replacement reference. These records capture the user's confirmed target, not completed implementation.

## ADR-001 — Subdomain glossary ownership

- **Status:** Accepted
- **Context:** Harmonize attributes across products in one subdomain.
- **Decision:** Subdomains own canonical definitions, whose stable identities are independent of names and descriptions.
- **Alternatives:** Enterprise-owned or product-local canonical glossaries.
- **Consequences:** Ownership must be explicit. Prior enterprise-glossary wording is superseded; code/configuration still need alignment. Physical renaming is unnecessary.

## ADR-002 — SQLite and derived NetworkX graphs

- **Status:** Accepted
- **Context:** Auditable persistence and graph learning without production graph infrastructure.
- **Decision:** SQLite is the persistent governance system of record; reconstruct NetworkX graphs from governed records.
- **Alternatives:** Graph-only persistence, Neo4j now, independently maintained graph state.
- **Consequences:** Analytics never become another source of truth. Preserve boundaries allowing future Neo4j evaluation without requiring it for the MVP.

## ADR-003 — Human approval and evidence origins

- **Status:** Accepted
- **Context:** Similarity and AI reasoning cannot prove semantic equivalence alone.
- **Decision:** Separate source assertions, inferred candidates, and approved facts. Humans approve governance decisions; retain provenance and decision history.
- **Alternatives:** Automatic score-based approval; treating source observations as governed truth.
- **Consequences:** Definition approval does not approve mappings. Source changes expose review needs without overwriting approvals. Object similarity does not establish redundancy; metadata availability does not establish data quality.

## ADR-004 — Small CLI-first MVP

- **Status:** Accepted for stack, CLI, and scope; original AI deferral superseded by ADR-007
- **Context:** Deliver a working, teachable engine incrementally.
- **Decision:** Python 3.12, Poetry, Pydantic v2, pytest, dbt YAML/SQL first, deterministic matching first, useful JSON/YAML exports. Defer Unity Catalog, UI, and production infrastructure.
- **Alternatives:** UI-first delivery, multiple initial adapters, embeddings/LLMs from the outset.
- **Consequences:** Originally deferred AI pending measurable value; ADR-007 replaces that condition with mandatory hybrid intelligence and evaluation. Add appropriate tests with capabilities; preserve repeatable ingestion. Implementation and installation require scoped user approval.

## ADR-005 — Canonical attributes and concepts

- **Status:** Proposed
- **Context:** Attributes may be meaningful in multiple concepts; starter code requires exactly one.
- **Proposal:** Consider many-to-many association, separate from subdomain ownership.
- **Alternatives:** Mandatory or optional single-concept ownership.
- **Consequences:** Validate examples before deciding cardinality or changing models. Documentation approval does not finalize this proposal.

## ADR-006 — Business entity classification

- **Status:** Proposed
- **Context:** The conceptual inventory includes concepts and business entities.
- **Proposal:** Consider `BusinessEntity` as a classification of `DataConcept`.
- **Alternatives:** Separate entities with an explicit association.
- **Consequences:** Choose based on concrete semantics before creating classes/tables.

## ADR-007 — Mandatory hybrid LLM recommendations

- **Status:** Accepted
- **Context:** The user requires operational semantic intelligence in the MVP, superseding the AI-deferral portion of ADR-004.
- **Decision:** Combine lexical discovery, embedding retrieval, and LLM reasoning grounded in approved glossary entries and applicable standards. Separate provider-independent embedding and recommendation contracts, initially implemented through OpenAI APIs. Require structured Pydantic outputs covering recommendation, explanation, evidence, uncertainty, next action, and `equivalent`, `related`, `distinct`, or `insufficient_evidence` categories.
- **Alternatives:** Deterministic-only MVP; lexical-only retrieval; provider-coupled business logic; unstructured LLM responses.
- **Consequences:** Embeddings and actual LLM calls are mandatory MVP deliverables. Record provider/model information, prompt/schema versions, settings, source evidence, retrieved context versions, and validated responses. Maintain a small human-reviewed evaluation dataset and compare quality with a lexical baseline. Distinguish mocked application tests from live model evaluation. Traceability does not guarantee identical replay.
- **Authority boundary:** LLM recommendations cannot directly modify approved glossary records. Humans separately approve authoritative mappings; incomplete evidence should prompt clarification.
- **Learning:** Teach embeddings, retrieval, structured outputs, prompting, evaluation, and provider abstraction incrementally. Implementation, model selection, dependencies, and evaluation thresholds remain separately scoped work.

## Deferred questions

Physical-to-canonical mapping cardinality, source identity keys, observation/version history, approval review rules, availability scoring, and graph weights/algorithms need future decisions. A dedicated skill is deferred until a stable reusable procedure emerges; current agent guidance belongs in `AGENTS.md`.
