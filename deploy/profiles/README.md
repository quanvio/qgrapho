# Deploy profiles

QGrapho deployment profiles — native by default.

| Profile | File | Use case |
|---------|------|----------|
| **native** | [`dev-native.yaml`](dev-native.yaml) | Laptop, trusted repos — **default** |
| **isolated** | [`dev-isolated.yaml`](dev-isolated.yaml) | Optional container for Agent Engine only |
| **scale** | `prod-k8s/` *(Phase 5)* | Enterprise worker pool |

See [docs/installation.md](../../docs/installation.md).
