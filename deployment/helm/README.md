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

To find the address of the webapp and virtuoso:

```sh
minikube service virtuoso --url
minikube service web --url
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

### Changes for Local Development

To install the helm chart for a local deployment,

1. Set the correct virtuoso pvc `storageClassName` (removing it from the file should also work)
2. Install minikube
3. Run `helm install slinky . --namespace slinky --create-namespace`
4. Use the slinky namespace with `kubectl config set-context --current --namespace=slinky`
5. View the pods with `kubectl get po`
