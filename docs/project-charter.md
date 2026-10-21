# Project charter

## Purpose

Establish semantic uniformity at attribute level across products within one subdomain. The subdomain owns the canonical glossary; physical occurrences retain source names and provenance.

For example, `sales_order_no` and `isell_order_id` may be equivalent, but names alone cannot prove this. Definitions, context, identifier scope, grain, and relationships must support a human decision.

## Scope

Govern domains/subdomains, products, concepts, tables/views, physical and canonical attributes, relationships, provenance, and decisions. Capture descriptions, types, keys, and cardinalities where available; preserve uncertainty when metadata is absent.

Support initial consolidation and incremental developer guidance, object similarity with intentional-overlap justification, conceptual target modeling, metadata availability assessment, and graph analytics.

The MVP includes an operational hybrid recommendation workflow: lexical candidate discovery, embedding-based retrieval, and LLM reasoning grounded in the approved glossary and applicable standards. Use provider-independent interfaces with an initial OpenAI API implementation, structured recommendations, recorded evidence, and human-reviewed evaluation.

## Learning objectives

Develop practical understanding of Python architecture, Pydantic, pytest, persistence, metadata modeling, graph theory, embeddings, retrieval, structured outputs, prompting, evaluation, and model-provider abstraction. Work in small explained steps, preferably implemented by the learner and reviewed together.

## Principles and demonstration boundary

Humans approve governance decisions. Separate source assertions, candidates, and approved facts. Preserve evidence and decision history.

Target one subdomain, approximately three products, 6–10 objects, and 50–100 physical attribute occurrences. These are sizing targets, not hard limits. See [requirements](mvp-requirements.md).

## Non-goals

Enterprise glossary ownership, mandatory physical renaming, automatic AI approval, production infrastructure, and UI development are outside the MVP. Metadata availability does not measure actual data quality. Unity Catalog and Neo4j are future options.
