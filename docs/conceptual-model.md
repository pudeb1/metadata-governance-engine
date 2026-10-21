# Conceptual model

This describes business semantics, not finalized classes or database tables. Target names may differ from starter classes.

## Entities

| Entity | Meaning |
| --- | --- |
| Subdomain | Governance boundary owning a canonical glossary. |
| DataProduct | Identifiable product/source grouping within the demonstration subdomain. |
| DataConcept | Business meaning associated with one or more objects. |
| BusinessEntity | Possible concept classification; separate-entity design remains open. |
| DataObject | Table/view or dbt model belonging to a product. |
| PhysicalAttribute | Observed column occurrence belonging to an object. |
| CanonicalAttribute | Subdomain-owned business attribute with identity independent of its name and definition. |
| MetadataRelationship | Typed assertion or candidate with evidence and explicit governance state. |
| EquivalenceCandidate | Advisory equivalence proposal with method, rationale, and evidence; storage representation remains open. |
| GovernanceDecision | Human action with reviewer, time, rationale, and evidence about a governed subject. |
| TargetModelRequirement | Required canonical attribute in a conceptual to-be model and its relevant context. |
| SourceAvailabilityEvidence | Source evidence supporting a requirement assessment, including uncertainty. |

## Relationships and identity

- A subdomain owns many canonical attributes. Domain hierarchy does not imply enterprise glossary ownership.
- Products contain objects; objects contain physical occurrences.
- Objects and concepts have a many-to-many association. Concepts may span products.
- Multiple physical occurrences may map to one canonical attribute. Whether one occurrence may map to multiple canonical attributes remains open and must reflect business semantics.
- Canonical-attribute–concept many-to-many association is proposed, not finalized.
- Target requirements reference canonical attributes in target-model context; evidence relates requirements to source observations and governed mappings.
- Stable identities are separate from mutable names, definitions, and fingerprints. Source identity resolution must make repeat ingestion idempotent.

## Evidence and approval

Observed definitions report what a source says; they are not automatically approved canonical definitions. Deterministic and AI candidates remain advisory. Approving a canonical definition does not approve every physical mapping to it.

Preserve evidence origin, observation/source revision context, recommendation method, and the subject/version reviewed by a human. Exact persistence fields and lifecycle rules need later design. Source changes must preserve approvals while exposing changed evidence for review.

Availability categories are required, but their exact rules remain open. Absent metadata must not automatically mean absent data. Grain, scope, and relationships matter for equivalence and coverage.

## Recommendation semantics

Structured Pydantic outputs must contain a recommendation, explanation, evidence references, uncertainty, next action, and one assessment category:

- `equivalent`: evidence supports the same meaning, scope, and grain.
- `related`: meanings are connected but interchangeability is not supported.
- `distinct`: evidence supports different meanings, scopes, or grains.
- `insufficient_evidence`: available context cannot support a reliable assessment; identify the clarification needed.

These categories describe an advisory semantic assessment, not a human approval/rejection action. Missing evidence should lead to clarification rather than invented facts. Schema validation proves response shape, not semantic correctness; model-reported uncertainty is not automatically a calibrated probability.

Record provider/model identifiers, embedding model, prompt/schema versions, settings, source observations, retrieved glossary/standards versions, and validated response for traceability. Evidence references must identify supplied context. Keep human-reviewed evaluation labels separate from model predictions. Exact storage fields and Python contracts remain future implementation decisions.

## Starter alignment backlog

- `Domain` and configuration emphasize enterprise/domain structure; explicit subdomain glossary ownership is absent.
- Mandatory singular `CanonicalAttribute.concept_id` prematurely fixes an open cardinality.
- `MetadataObject.project` is a string rather than an explicit product identity.
- `MetadataOccurrence.canonical_attribute_id` lacks a separate mapping decision/provenance lifecycle; the existing test links it to a proposed attribute.
- Relationship status/score do not capture structured evidence origin or approval authority.
- UUID defaults alone do not resolve stable source identities on repeat ingestion.
- Target requirements, availability evidence, overlap justification, and structured observation history are absent.

These are future modeling tasks, not implementation authorized by this documentation step.
