# Roadmap

Public development plan for [QGrapho](https://github.com/quanvio/qgrapho).

**Current release:** `v0.0.1` — **Early preview** (documentation + CLI scaffold + project layout).  
Console, Agent Engine, and graph indexing ship in upcoming milestones.

---

## Status today

| Area | Status |
|------|--------|
| Public docs & config | ✅ Available |
| Python CLI (`qgrapho doctor`, `init`, …) | ✅ Scaffold — honest Phase 0 checks |
| Console + Agent Engine | 🔲 Phase 0 |
| Graph indexing | 🔲 Phase 1 |
| QGrapho Cloud (`qgrapho.quanvio.com`) | 🔲 Enable when endpoint is live |

---

## Phase 0 — Working spine

**Goal:** Console talks to your model provider; Graph MCP answers queries.

- [ ] Pin `vendor/` submodules (`vendor.lock`)
- [ ] Wire Console + Model Router (native install)
- [ ] Wire Quanvio MCP in developer config
- [ ] `qgrapho doctor` checks real binaries (not placeholders)
- [ ] GitHub Release with install script + wheel

**Exit criteria:** indexed repo returns symbols via `query_graph`; `qgrapho start` launches native stack.

---

## Phase 1 — Code Graph

- [ ] Embedded FalkorDB or LadybugDB
- [ ] `qgrapho index .` runs real indexer
- [ ] SCIP indexer in CI for supported languages

**Exit criteria:** “Who calls X?” answered via graph.

---

## Phase 2 — Schema Graph

- [ ] DB introspection → graph
- [ ] Migration / ORM parsers
- [ ] Optional DataHub on server

---

## Phase 3 — Runtime + Business graphs

- [ ] OpenTelemetry → Runtime Graph
- [ ] Business Knowledge Graph ingestion
- [ ] MCP: Jira, Confluence, Slack

---

## Phase 4 — Events + verification

- [ ] QGrapho Event Bus handlers
- [ ] Verification layer in CI
- [ ] Optional audit replay

---

## Phase 5 — Estate scale

- [ ] Federation across shards
- [ ] Optional Kubernetes worker pool
- [ ] GitOps deploy profiles

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Pick an unchecked Phase 0 item and open a PR.

Track requests: [github.com/quanvio/qgrapho/issues](https://github.com/quanvio/qgrapho/issues)
