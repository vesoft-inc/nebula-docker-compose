# Nebula Helm Chart

Nebula Graph Helm chart for Kubernetes

### Requirements

* Kubernetes >= 1.14
* [CoreDNS][] >= 1.6.0
* [Helm][] >= 3.2.0


### Helm installation
```sh
# NOTE: If installed under a different chart name and namespace, please specify as appropriate
$ helm install nebula charts/nebula
```

### Uninstalling the Chart
```sh
helm uninstall nebula
```


[helm]: https://helm.sh
[coredns]: https://github.com/coredns/coredns