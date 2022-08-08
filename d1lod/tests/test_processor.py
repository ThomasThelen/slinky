import RDF

from d1lod.processors.processor import Processor
from d1lod.processors.util import model_has_statement
from d1lod.namespaces import NS_SPDX

from .conftest import load_metadata, load_sysmeta


def test_processor_sets_checksum_and_algorithm(client, model):
    metadata = load_metadata("eml/eml-attribute-gym.xml")
    sysmeta = load_sysmeta("eml-attribute-gym-sysmeta.xml")

    processor = Processor(client, model, sysmeta, metadata, [])
    processor.process()

    assert model_has_statement(
        processor.model,
        RDF.Statement(
            None,
            RDF.Node(RDF.Uri(NS_SPDX.algorithm)),
            None,
        ),
    )

    assert model_has_statement(
        processor.model,
        RDF.Statement(
            None,
            RDF.Node(RDF.Uri(NS_SPDX.checksumValue)),
            None,
        ),
    )
