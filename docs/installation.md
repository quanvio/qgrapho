# Installation

One-click install for QGrapho on Windows, macOS, and Linux.

---

## One-click install

### Windows

Open PowerShell and run:

```powershell
irm https://raw.githubusercontent.com/quanvio/qgrapho/main/scripts/install.ps1 | iex
```

### macOS / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/quanvio/qgrapho/main/scripts/install.sh | bash
```

The installer:

1. Creates `~/.qgrapho/` config directory  
2. Installs QGrapho CLI (`qgrapho` command)  
3. Installs **QGrapho Console** and **QGrapho Agent Engine** (native binaries)  
4. Writes default config with **OpenAI preset** (change any time)  
5. Runs `qgrapho doctor` smoke test  

---

## Manual install (from clone)

For contributors or air-gapped environments:

```bash
git clone https://github.com/quanvio/qgrapho.git
cd qgrapho
./scripts/install.sh --from-source
```

---

## Deployment profiles

QGrapho ships three profiles. **Native is the default.**

| Profile | Containers | K8s | Use when |
|---------|------------|-----|----------|
| **`native`** (default) | None | No | Daily dev, trusted repos, minimal RAM |
| **`isolated`** | One (optional) | No | Untrusted code, shared machines |
| **`scale`** | Optional | Yes | Many parallel workers, HA |

Set in `~/.qgrapho/config.toml`:

```toml
[deploy]
profile = "native"   # native | isolated | scale
```

### Native profile (recommended)

- **QGrapho Console** — native process  
- **QGrapho Agent Engine** — `RUNTIME=process` (native, no isolation overhead)  
- **QGrapho Graph Intelligence** — embedded graph store  
- **Your model provider** — OpenAI, Ollama, custom gateway, or optional Quanvio preset  

**RAM:** typically 500 MB – 2 GB for a single session.

### Isolated profile (optional)

Same as native, but Agent Engine runs inside **one** Podman or Docker container when you need host isolation.

```toml
[deploy]
profile = "isolated"
[agent_engine]
runtime = "docker"
```

You still do **not** need Kubernetes.

### Scale profile (optional, later)

Worker pool on Kubernetes, GitOps deploy, event bus at estate scale. Enable only when a single server is not enough.

---

## QGrapho Agent Engine — why containers are optional

The Agent Engine executes shell commands, edits files, and runs git on your behalf.

| Mode | Containers | Weight | Isolation |
|------|------------|--------|-----------|
| **Process** (default) | None | Lightest | Same as your user — trusted dev only |
| **Docker / Podman** | One | Medium | Host protected |
| **Remote / K8s** | Many | Heavy | Enterprise scale |

QGrapho defaults to **process mode** so public installs stay lightweight. Switch to **isolated** only when security policy requires it.

---

## Verify installation

```bash
qgrapho doctor
```

Expected output:

```text
QGrapho Doctor
  Console .............. OK
  Agent Engine ......... OK (native)
  Graph Intelligence ... OK
  Model Router ......... OK (≥1 provider)
  Event Bus ............ optional
  Insights ............. optional
```

---

## Upgrade

```bash
qgrapho upgrade
```

Upgrades the QGrapho release bundle. Vendor engines are pinned inside the release — you always get a tested combination.

---

## Uninstall

```bash
qgrapho uninstall
```

Removes `~/.qgrapho/bin` and CLI shim. Your workspace and graph data under `~/.qgrapho/data` are preserved unless you pass `--purge`.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `qgrapho: command not found` | Restart terminal; ensure `~/.qgrapho/bin` is on PATH |
| Model auth failed | `qgrapho provider add openai` or set your provider's API key env var |
| Want QGrapho Cloud | Optional: `qgrapho provider add qgrapho-cloud` — enable when live |
| Agent Engine won't start | Run `qgrapho doctor --verbose` |
| Need isolation | Set `profile = "isolated"` in config |

---

## System requirements

| | Minimum | Recommended |
|---|---------|-------------|
| RAM | 4 GB | 8 GB |
| Disk | 2 GB | 10 GB (large repo indexes) |
| OS | Win 10+, macOS 12+, Linux x64/arm64 | — |
| Containers | Not required | Optional for isolated profile |
