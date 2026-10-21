# MVP requirements

These are target outcomes, not claims about current implementation.

## Workflows

**Initial consolidation:** Ingest metadata from multiple dbt products, preserve provenance, identify possible equivalents, obtain human approval of canonical definitions, and approve physical-to-canonical mappings.

**Incremental governance:** Detect new or changed attributes. Recommend reuse, definition clarification, or a new canonical attribute. Preserve existing approvals and expose changed evidence for review.

## Acceptance outcomes

| ID | Capability | Observable outcome |
| --- | --- | --- |
| MVP-01 | Ingestion | Ingest multiple dbt products and trace each occurrence to its product, object, source artifact, and recorded observation. |
| MVP-02 | Equivalence | Combine lexical candidate discovery and embedding retrieval with LLM assessment of semantic context; expose missing evidence and never approve from similarity alone. |
| MVP-03 | Glossary | A human can create and approve a subdomain-owned canonical definition with stable identity and an auditable decision. |
| MVP-04 | Mapping | Record human-approved physical-to-canonical mappings separately from candidates, with evidence and decision history. |
| MVP-05 | Developer guidance | Explain a reuse, clarification, or new-definition recommendation for a new or changed attribute without automatic approval. |
| MVP-06 | Object overlap | Compare objects using approved canonical overlap and other metadata; record intentional overlap and human justification without equating similarity with redundancy. |
| MVP-07 | Target coverage | Assess a small target model as available, partially available, missing, or unknown; explain a metadata-based availability score. |
| MVP-08 | Graph analytics | Reconstruct a governed graph; demonstrate a meaningful bipartite affinity projection and centrality analysis with interpretations and limitations. |
| MVP-09 | Repeatability | Ingest unchanged inputs twice without duplicate source records; ingest changes without overwriting approvals or decision history. |

## Mandatory intelligence acceptance outcomes

| ID | Capability | Observable outcome |
| --- | --- | --- |
| MVP-10 | Operational hybrid workflow | Run lexical discovery, embedding retrieval, and actual LLM assessment through the CLI using an OpenAI API adapter behind provider-independent interfaces; mocked responses alone do not satisfy this outcome. |
| MVP-11 | Grounded structured recommendations | Retrieve approved glossary entries and applicable standards; assess names, descriptions, business concepts, source context, data types, grain, and identifier scope. Validate a Pydantic response with category, recommendation, explanation, evidence references, uncertainty, and next action. Categories are `equivalent`, `related`, `distinct`, and `insufficient_evidence`. |
| MVP-12 | Traceability and authority | Retain provider/model identifiers, embedding model, prompt/schema versions, generation settings, retrieved context versions, source evidence, and validated response. LLM execution cannot modify approved glossary records; mappings require human approval. |
| MVP-13 | Recommendation evaluation | Maintain a small version-controlled human-reviewed dataset covering all four categories. Report retrieval recall, category accuracy, false equivalence recommendations, and appropriate insufficient-evidence use; compare with a lexical baseline. |

## Validation and limits

Add appropriate pytest coverage as capabilities are implemented, especially for ownership, approval boundaries, stable source identity, preserved decisions, and graph reconstruction. Use the small demonstration scope in the [charter](project-charter.md).

Scoring rules, evidence thresholds, graph weights, and centrality measures require later approved design. Community detection is optional. Embeddings and LLM reasoning are required; evaluation measures their contribution rather than determining whether to include them. Dataset size, retrieval cutoffs, and quality targets need later agreement. Mocked pytest tests verify application behavior; separate live evaluation measures actual model quality. Exact replay of model responses is not guaranteed.
