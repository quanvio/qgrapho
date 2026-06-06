# Vendor upstream sources

Pinned OSS engines live here as **git submodules**. Commit hashes are recorded in [`vendor.lock`](../vendor.lock).

Maintainers add submodules during Phase 0. **Public docs never name upstream projects.**

See internal engineering docs (`.qgrapho.md`, not in this repository) for the vendor map.

```bash
# After submodule is added:
git submodule update --init --recursive
```
