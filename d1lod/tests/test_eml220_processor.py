import pytest
import RDF

from d1lod.processors.eml.eml220_processor import EML220Processor

from .conftest import load_metadata, load_sysmeta


def test_processor_extracts_dataset_level_annotations(client, model):
    simple = load_metadata("eml/eml-annotation-gym.xml")
    sysmeta = load_sysmeta("eml-annotation-gym-sysmeta.xml")

    processor = EML220Processor(client, model, sysmeta, simple, [])
    processor.process()

    statement = RDF.Statement(
        RDF.Node(RDF.Uri("https://dataone.org/datasets/eml-annotation-gym#dataset01")),
        RDF.Node(RDF.Uri("http://purl.org/dc/elements/1.1/subject")),
        RDF.Node(RDF.Uri("http://purl.obolibrary.org/obo/ENVO_01000177")),
    )

    assert statement in processor.model


def test_processor_extracts_entity_level_annotations(client, model):
    metadata = load_metadata("eml/eml-annotation-gym.xml")
    sysmeta = load_sysmeta("eml-annotation-gym-sysmeta.xml")

    processor = EML220Processor(client, model, sysmeta, metadata, [])
    processor.process()
    statement = RDF.Statement(
        RDF.Node(
            RDF.Uri("https://dataone.org/datasets/eml-annotation-gym#my.data.table")
        ),
        RDF.Node(RDF.Uri("http://purl.obolibrary.org/obo/IAO_0000136")),
        RDF.Node(RDF.Uri("http://purl.obolibrary.org/obo/NCBITaxon_40674")),
    )

    assert statement in processor.model


def test_processor_extracts_attribute_level_annotations(client, model):
    metadata = load_metadata("eml/eml-annotation-gym.xml")
    sysmeta = load_sysmeta("eml-annotation-gym-sysmeta.xml")

    processor = EML220Processor(client, model, sysmeta, metadata, [])
    processor.process()
    statement = RDF.Statement(
        RDF.Node(
            RDF.Uri("https://dataone.org/datasets/eml-annotation-gym#my.attribute")
        ),
        RDF.Node(
            RDF.Uri(
                "http://ecoinformatics.org/oboe/oboe.1.2/oboe-core.owl#containsMeasurementsOfType"
            )
        ),
        RDF.Node(RDF.Uri("http://purl.dataone.org/odo/ECSO_00001197")),
    )

    assert statement in processor.model


def test_processor_extracts_top_level_annotations(client, model):
    metadata = load_metadata("eml/eml-annotation-gym.xml")
    sysmeta = load_sysmeta("eml-annotation-gym-sysmeta.xml")

    processor = EML220Processor(client, model, sysmeta, metadata, [])
    processor.process()

    first_statement = RDF.Statement(
        RDF.Node(RDF.Uri("https://dataone.org/datasets/eml-annotation-gym#dataset01")),
        RDF.Node(RDF.Uri("http://purl.obolibrary.org/obo/IAO_0000136")),
        RDF.Node(RDF.Uri("http://purl.obolibrary.org/obo/ENVO_01000177")),
    )

    second_statement = RDF.Statement(
        RDF.Node(RDF.Uri("https://dataone.org/datasets/eml-annotation-gym#test.user")),
        RDF.Node(RDF.Uri("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")),
        RDF.Node(RDF.Uri("https://schema.org/Person")),
    )

    assert first_statement in processor.model
    assert second_statement in processor.model


def test_processor_extracts_additional_metadata_annotations(client, model):
    metadata = load_metadata("eml/eml-annotation-gym.xml")
    sysmeta = load_sysmeta("eml-annotation-gym-sysmeta.xml")

    processor = EML220Processor(client, model, sysmeta, metadata, [])
    processor.process()

    statement = RDF.Statement(
        RDF.Node(RDF.Uri("https://dataone.org/datasets/eml-annotation-gym#test.user")),
        RDF.Node(RDF.Uri("https://schema.org/memberOf")),
        RDF.Node(RDF.Uri("https://ror.org/017zqws13")),
    )

    assert statement in processor.model


# TOOD: Award tests
# Test blank node and not-blank node for
# - award
# - funder


def test_award_uses_blank_nodes_when_appropriate(client, model):
    metadata = load_metadata("eml/eml-award-blanknodes.xml")
    sysmeta = load_sysmeta("eml-award-sysmeta.xml")

    processor = EML220Processor(client, model, sysmeta, metadata, [])
    processor.process()

    # Test award is a blank node
    statement = RDF.Statement(
        RDF.Node(RDF.Uri("https://dataone.org/datasets/eml-award")),
        RDF.Node(RDF.Uri("https://schema.org/award")),
        RDF.Node(blank="award"),
    )

    # Test funder is a blank node
    statement = RDF.Statement(
        RDF.Node(blank="award"),
        RDF.Node(RDF.Uri("https://schema.org/funder")),
        RDF.Node(blank="funder"),
    )

    assert statement in processor.model


def test_award_uses_named_nodes_when_appropriate(client, model):
    metadata = load_metadata("eml/eml-award-noblanknodes.xml")
    sysmeta = load_sysmeta("eml-award-sysmeta.xml")

    processor = EML220Processor(client, model, sysmeta, metadata, [])
    processor.process()

    # Test award is a URI
    statement = RDF.Statement(
        RDF.Node(RDF.Uri("https://dataone.org/datasets/eml-award")),
        RDF.Node(RDF.Uri("https://schema.org/award")),
        RDF.Node(RDF.Uri("https://www.nsf.gov/awardsearch/showAward?AWD_ID=12345")),
    )

    # Test funder is a URI
    statement = RDF.Statement(
        RDF.Node(RDF.Uri("https://www.nsf.gov/awardsearch/showAward?AWD_ID=12345")),
        RDF.Node(RDF.Uri("https://schema.org/funder")),
        RDF.Node(RDF.Uri("https://doi.org/10.13039/00000001")),
    )

    assert statement in processor.model


@pytest.mark.integration
def test_production_eml(client, model):
    """
    Tests that the EML processor works on a number of production EML documents without error.

    :param client: The slinky client
    :return: None
    """
    metadata = load_metadata(
        "eml/eml-Arctic_sea_ice_thermal_emission_measurements_from.xml"
    )
    sysmeta = load_sysmeta("eml-Arctic_sea_ice_thermal_emission_measurements_from.xml")

    processor = EML220Processor(client, model, sysmeta, metadata, [])
    processor.process()
