"""Platform-independent metadata contracts (Milestone 1)."""
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator, model_validator


class GovernanceStatus(str, Enum):
    OBSERVED = "observed"
    PROPOSED = "proposed"
    APPROVED = "approved"
    REJECTED = "rejected"
    DEPRECATED = "deprecated"


class Domain(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    key: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str = ""
    parent_domain_id: UUID | None = None
    owner: str | None = None
    is_enterprise: bool = False


class BusinessConcept(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    domain_id: UUID
    name: str = Field(min_length=1)
    definition: str = ""
    status: GovernanceStatus = GovernanceStatus.PROPOSED


class CanonicalAttribute(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    concept_id: UUID
    name: str = Field(min_length=1)
    description: str = ""
    data_type: str | None = None
    status: GovernanceStatus = GovernanceStatus.PROPOSED
    aliases: list[str] = Field(default_factory=list)


class MetadataObject(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    domain_id: UUID
    source_system: str = Field(min_length=1)  # dbt, unity_catalog, etc.
    project: str = Field(min_length=1)
    object_name: str = Field(min_length=1)
    object_type: str = "model"
    qualified_name: str | None = None
    source_path: str | None = None
    description: str = ""


class MetadataOccurrence(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    object_id: UUID
    column_name: str = Field(min_length=1)
    description: str = ""
    data_type: str | None = None
    canonical_attribute_id: UUID | None = None
    definition_fingerprint: str | None = None
    status: GovernanceStatus = GovernanceStatus.OBSERVED
    source_path: str | None = None


class RelationshipType(str, Enum):
    EQUIVALENT = "equivalent"
    RELATED = "related"
    BROADER = "broader"
    NARROWER = "narrower"
    CONFLICTS_WITH = "conflicts_with"


class MetadataRelationship(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    source_entity_id: UUID
    target_entity_id: UUID
    relationship_type: RelationshipType
    similarity_score: float | None = Field(default=None, ge=0, le=1)
    rationale: str = ""
    status: GovernanceStatus = GovernanceStatus.PROPOSED

    @model_validator(mode="after")
    def distinct_entities(self) -> "MetadataRelationship":
        if self.source_entity_id == self.target_entity_id:
            raise ValueError("A relationship must link two distinct entities")
        return self


class DecisionAction(str, Enum):
    APPROVE = "approve"
    REJECT = "reject"
    DEPRECATE = "deprecate"
    REQUEST_CHANGES = "request_changes"


class GovernanceDecision(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    entity_id: UUID
    action: DecisionAction
    reviewer: str = Field(min_length=1)
    rationale: str = ""
    evidence: list[str] = Field(default_factory=list)
    decided_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
