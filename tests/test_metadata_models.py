from uuid import uuid4

import pytest
from pydantic import ValidationError

from metadata_governance.models import (
    BusinessConcept, CanonicalAttribute, Domain, GovernanceStatus,
    MetadataObject, MetadataOccurrence, MetadataRelationship, RelationshipType,
)


def test_federated_metadata_links():
    enterprise = Domain(key="enterprise", name="Enterprise", is_enterprise=True)
    domain = Domain(key="last_mile_delivery", name="Last-mile Delivery", parent_domain_id=enterprise.id)
    concept = BusinessConcept(domain_id=domain.id, name="Shipment Destination Country")
    attribute = CanonicalAttribute(concept_id=concept.id, name="shipping_destination_country_code")
    obj = MetadataObject(domain_id=domain.id, source_system="dbt", project="last-mile", object_name="dim_shipment")
    occurrence = MetadataOccurrence(object_id=obj.id, column_name="destination_country", canonical_attribute_id=attribute.id)
    assert concept.status == GovernanceStatus.PROPOSED
    assert occurrence.status == GovernanceStatus.OBSERVED
    assert occurrence.canonical_attribute_id == attribute.id


def test_similarity_score_bounds():
    with pytest.raises(ValidationError):
        MetadataRelationship(source_entity_id=uuid4(), target_entity_id=uuid4(), relationship_type=RelationshipType.RELATED, similarity_score=1.2)


def test_relationship_cannot_point_to_self():
    entity_id = uuid4()
    with pytest.raises(ValidationError):
        MetadataRelationship(source_entity_id=entity_id, target_entity_id=entity_id, relationship_type=RelationshipType.EQUIVALENT)
