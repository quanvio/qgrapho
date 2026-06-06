# Getting started

Get QGrapho running in about 10 minutes. No Podman, Docker, or Kubernetes required.

---

## 1. Install

**Windows**

```powershell
irm https://raw.githubusercontent.com/quanvio/qgrapho/main/scripts/install.ps1 | iex
```

**macOS / Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/quanvio/qgrapho/main/scripts/install.sh | bash
```

Restart your terminal, then verify:

```bash
qgrapho doctor
```

You should see: Console, Agent Engine, Graph Intelligence OK. Models OK once you add a provider.

---

## 2. Add a model provider (30 seconds)

QGrapho uses **your** LLM — any OpenAI-compatible API. You are not locked to any vendor.

```bash
qgrapho init
```

The wizard suggests smart defaults:

| Choice | Models | Key |
|--------|--------|-----|
| **OpenAI** | gpt-4o, gpt-4o-mini | `OPENAI_API_KEY` |
| **DeepSeek** | v4-flash, v4-pro | `DEEPSEEK_API_KEY` |
| **Moonshot (Kimi)** | kimi-k2.6, k2.5, turbo, thinking | `MOONSHOT_API_KEY` |
| **Grok (xAI)** | grok-4.3, grok-build | `XAI_API_KEY` |
| **Ollama (local)** | your local models | no key |
| **OpenRouter** | DeepSeek + Kimi + Grok via one key | `OPENROUTER_API_KEY` |
| **Custom URL** | any gateway | your env var |
| **QGrapho Cloud** *(optional)* | hosted preset | `QGRAPHO_CLOUD_API_KEY` |

Example — OpenAI only:

```bash
export OPENAI_API_KEY="sk-..."
qgrapho provider add openai
qgrapho provider use openai
```

Add more providers anytime:

```bash
qgrapho provider add ollama
qgrapho provider add custom
qgrapho model suggest    # see smart routing table
```

Full guide: **[Models & providers](models.md)**

Config: `~/.qgrapho/config.toml` — never commit API keys.

---

## 3. Index your codebase

```bash
cd /path/to/your/project
qgrapho index .
```

Builds **Code Graph** — symbols, callers, routes, dependencies.

---

## 4. Start QGrapho

```bash
qgrapho start
```

| Component | What you get |
|-----------|--------------|
| **QGrapho Console** | Interactive terminal |
| **QGrapho Agent Engine** | Native process mode — no containers |

Example prompts:

```text
Explain the architecture of this service.
Who calls the payment handler?
Fix the failing test in auth module and open a PR.
```

Switch model in session: `/model openai/gpt-4o`

---

## 5. First autonomous task

```text
Run a small fix: update the README typo and verify tests pass.
```

1. Query Code Graph  
2. Route to best model (`code` route)  
3. Agent Engine executes  
4. Graph refreshes  

---

## What you do not need

| Not required | Notes |
|--------------|-------|
| QGrapho Cloud | Optional hosted preset — enable when endpoint is live |
| Docker / Podman | Default is native |
| Kubernetes | Later, optional |
| Local GPU | Only if **you** choose Ollama/local models |
| Many config files | One `config.toml` |

---

## Next steps

- [Models & providers](models.md) — unlimited providers, smart routing  
- [Capabilities & modalities](capabilities.md) — vision, image, video, audio, docs, embed  
- [Installation](installation.md) — profiles, upgrades  
- [Architecture](architecture.md) — platform design & four graphs  
- [Concepts](concepts.md) — glossary & agent loops  
- [Configuration](configuration.md) — all settings  

---

## Help

- Issues: [github.com/quanvio/qgrapho/issues](https://github.com/quanvio/qgrapho/issues)  
- Email: [founder@quanvio.com](mailto:founder@quanvio.com)
