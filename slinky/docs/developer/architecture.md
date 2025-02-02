# Architecture


`slinky` is made of a few key classes, the most important of which is `SlinkyClient`:

- `SlinkyClient`: Entrypoint class that manages a connection to DataONE, a triple store, and Redis for short-term persistence and delayed jobs
- `FilteredCoordinatingNodeClient`: A view into a Coordinating Node that can limit what content appears to be available based on a Solr query. e.g., a CN client that can only see datasets that are part of a specific EML project or in a particular region
- `SparqlTripleStore`: Handles inserting into and querying a generic SPARQL-compliant RDF triplestore via SPARQL queries. Designed to be used with multiple triple stores.
- `Processor`: Set of classes that convert documents of various formats (e.g., XML, JSON-LD) into a set of RDF statements
- `jobs`: Set of routines for use in a background job scheduling system. Currently `rq`.

The `SlinkyClient` is the main entrypoint for everything the package does and handles connections to require services.
See the following diagram to get a sense of the interaction between the classes:

![slinky package architecture](images/slinky-client-architecture.png)
