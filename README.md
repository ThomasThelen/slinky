# Slinky, the DataONE Graph Store

[![pytest](https://github.com/dataoneorg/slinky/actions/workflows/pytest.yaml/badge.svg)](https://github.com/dataone/slinky/actions/workflows/pytest.yaml)

A Linked Open Data interface to [DataONE](https://dataone.org) designed to run on [Kubernetes](https://kubernetes.io).

## Overview

Slinky follows for representing its holdings in RDF, using the schema.org vocabulary. The project provides a SPARQL endpoint which supports federated querying. Slinky's URI's are also dereferenceable and support content negotiation, enabling agent driven data discovery. 

For more information about the project, visit slinky.dataone.org

This repository acts as the Slinky monorepo where all services, documentation, and deployment files are stored.

## Deployment

Slinky is primarily designed for deployment on the DataONE [Kubernetes](https://kubernetes.io/) cluster however, with minikube it can be deployed locally.

For deployment instructions, refer to the Helm chart Readme in the [helm](./deployment/helm/) folder.

## Contributing

Before making contributions, refer to the [contributing](./CONTRIBUTING.md) file.
