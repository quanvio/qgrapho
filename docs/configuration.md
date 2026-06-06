# Configuration

All settings live in **`~/.qgrapho/config.toml`**. Run `qgrapho init` for the interactive wizard.

**Models:** any provider you choose — see **[Models & providers](models.md)** for the full guide.

---

## Minimal example (bring your own OpenAI key)

```toml
[models]
default_provider = "openai"
default_model = "gpt-4o-mini"

[routing]
chat = "openai/gpt-4o-mini"
code = "openai/gpt-4o"
plan = "openai/gpt-4o"
fast = "openai/gpt-4o-mini"

[[providers]]
id = "openai"
label = "OpenAI"
base_url = "https://api.openai.com/v1"
api_key_env = "OPENAI_API_KEY"
enabled = true

  [[providers.models]]
  id = "gpt-4o"
  tags = ["code", "plan"]

  [[providers.models]]
  id = "gpt-4o-mini"
  tags = ["chat", "fast"]

[workspace]
path = "D:/projects/my-app"
mount_in_engine = "/workspace"

[deploy]
profile = "native"

[console]
enabled = true

[agent_engine]
enabled = true
runtime = "process"

[graph_intelligence]
backend = "embedded"
data_dir = "~/.qgrapho/data/graphs"
```

---

## Models section

| Key | Purpose |
|-----|---------|
| `[models] default_provider` | Active provider id |
| `[models] default_model` | Fallback model id |
| `[routing]` | Smart map: task/modality → `provider/model` |
| `[[providers]]` | Add unlimited providers |
| `[[providers.models]]` | Models per provider with `tags` + `modalities` |

### Routing keys (text + multimodal)

| Route | Use |
|-------|-----|
| `chat`, `fast` | Quick text |
| `code`, `plan`, `agent`, `reason` | Agents & architecture |
| `vision`, `diagram`, `ocr` | Image **input** |
| `doc` | PDF, Confluence, long docs |
| `image_out` | Generate images |
| `video_in`, `video_out` | Video understand / generate |
| `audio_in`, `audio_out` | Transcribe / TTS |
| `embed`, `search` | Vectors & semantic search |

Full guide: **[Capabilities & modalities](capabilities.md)**

### Model modalities (per `[[providers.models]]`)

```toml
[[providers.models]]
id = "gpt-4o"
tags = ["vision", "doc", "code"]

[providers.models.modalities]
input  = ["text", "image", "file"]
output = ["text"]

[providers.models.modalities.features]
tools     = true
streaming = true
thinking  = false
```

| `input` value | Meaning |
|---------------|---------|
| `text` | Prompts, code |
| `image` | PNG, JPG, screenshots |
| `video` | MP4, demos |
| `audio` | WAV, MP3, voice |
| `file` | PDF, attachments |

| `output` value | Meaning |
|----------------|---------|
| `text` | Chat, code patches |
| `image` | Generated assets |
| `video` | Generated clips |
| `audio` | Speech |
| `embed` | Embedding vectors |

Provider fields:

| Field | Description |
|-------|-------------|
| `endpoints.image` | Image generation path (default `/v1/images/generations`) |
| `endpoints.embed` | Embeddings path |
| `endpoints.audio_in` / `endpoints.audio_out` | Transcription / TTS paths |

---

## Environment variables

| Variable | When |
|----------|------|
| `OPENAI_API_KEY` | OpenAI preset |
| `DEEPSEEK_API_KEY` | DeepSeek V4 Flash / Pro |
| `MOONSHOT_API_KEY` | Kimi K2.6, K2.5, Turbo, Thinking |
| `XAI_API_KEY` | Grok 4.3, Grok Build |
| `OPENROUTER_API_KEY` | OpenRouter (many models, one key) |
| `ANTHROPIC_API_KEY` | Anthropic preset |
| `QGRAPHO_CLOUD_API_KEY` | **Optional** QGrapho Cloud only |
| `QGRAPHO_HOME` | Config root (default `~/.qgrapho`) |
| `QGRAPHO_WORKSPACE` | Override workspace path |
| `QGRAPHO_PROFILE` | Override deploy profile |

Never commit API keys. Use env vars or OS secret store.

---

## Agent Engine runtime

| Value | Meaning |
|-------|---------|
| `process` | Native, lightweight — **default** |
| `docker` | One container — isolated profile |
| `remote` | Remote sandbox — scale profile |

```toml
[agent_engine]
runtime = "process"

[workspace]
path = "/home/you/project"
mount_in_engine = "/workspace"
```

---

## MCP tools

`~/.qgrapho/mcp.json`:

```json
{
  "servers": {
    "qgrapho": {
      "command": "qgrapho-mcp",
      "args": ["serve"]
    }
  }
}
```

---

## Deploy profiles

| Profile | `[deploy] profile` | `[agent_engine] runtime` |
|---------|-------------------|--------------------------|
| Native | `native` | `process` |
| Isolated | `isolated` | `docker` |
| Scale | `scale` | `remote` |

See [Installation](installation.md#deployment-profiles).

---

## Full example

See [config/qgrapho.example.toml](../config/qgrapho.example.toml) in the repo.
