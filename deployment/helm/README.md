# Slinky Helm Chart

## Installation

### Pre-requisites

- A Kubernetes cluster
- Helm

### Quick-Start

To make installing Slinky straightforward, we provide a [Helm](https://helm.sh) chart in this repository.

Install the Chart by running:

```sh
cd helm
helm install $YOUR_NAME .
```

### Ingress

The Slinky chart supports setting up an Ingress, provided your cluster is set up to create and set up Ingress resources.

To install the chart with Ingress, you must provide the following values in your `helm install` command:

- `ingress.enabled`
- `ingress.host`
- `ingress.tls.secretName`
- `ingress.clusterIssuer`

As an example,

```sh
helm install \
    --set ingress.enabled=true \
    --set ingress.host=api.example.org \
    --set ingress.tls.secretName=my-tls-secret-name \
    --set ingress.clusterIssuer=my-cluster-issuer \
    slinky .
```

### Scaling Workers

To scale the number of workers processing datasets beyond the default, run:

```sh
kubectl scale --replicas=3 deployments/{dataset-pod-name}
```
