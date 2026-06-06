"""qgrapho init — first-time setup."""

from __future__ import annotations

import shutil
from pathlib import Path

from qgrapho.paths import config_path, qgrapho_home, repo_config_example


PROVIDERS = (
    ("1", "OpenAI", "OPENAI_API_KEY", "openai"),
    ("2", "DeepSeek (v4-flash / v4-pro)", "DEEPSEEK_API_KEY", "deepseek"),
    ("3", "Moonshot / Kimi", "MOONSHOT_API_KEY", "moonshot"),
    ("4", "Grok / xAI", "XAI_API_KEY", "grok"),
    ("5", "Ollama (local, no key)", None, "ollama"),
    ("6", "OpenRouter", "OPENROUTER_API_KEY", "openrouter"),
    ("7", "Custom URL", None, "custom"),
    ("8", "QGrapho Cloud (optional)", "QGRAPHO_CLOUD_API_KEY", "qgrapho-cloud"),
)


def _ensure_config_template() -> None:
    home = qgrapho_home()
    home.mkdir(parents=True, exist_ok=True)
    (home / "data" / "graphs").mkdir(parents=True, exist_ok=True)
    (home / "config").mkdir(parents=True, exist_ok=True)

    dest = config_path()
    if dest.is_file():
        return

    example = repo_config_example()
    if example:
        shutil.copy(example, dest)
        shutil.copy(example, home / "config" / "qgrapho.example.toml")
        return

    dest.write_text('[product]\nname = "QGrapho"\n', encoding="utf-8")


def run_init() -> int:
    _ensure_config_template()
    print("QGrapho setup — pick a model provider\n")
    for num, label, _, _ in PROVIDERS:
        print(f"  {num}) {label}")
    choice = input("\nChoice [1-8]: ").strip() or "1"

    selected = next((p for p in PROVIDERS if p[0] == choice), PROVIDERS[0])
    _, label, env_key, preset = selected
    print(f"\nSelected: {label}")

    if preset == "ollama":
        print("Enable ollama in config.toml and run: ollama serve")
    elif preset == "custom":
        print(f"Edit {config_path()} — add [[providers]] with your base_url")
    elif preset == "qgrapho-cloud":
        print("Enable when https://qgrapho.quanvio.com/v1 is live.")
        print(f"Run: qgrapho provider add {preset}  (coming soon)")
        if env_key:
            import os

            if not os.environ.get(env_key):
                key = input(f"{env_key}: ").strip()
                if key:
                    print(f"Set {env_key} in your shell profile (not stored by qgrapho init).")
    elif env_key:
        import os

        if not os.environ.get(env_key):
            key = input(f"{env_key}: ").strip()
            if key:
                print(f"Set {env_key} in your shell profile (not stored by qgrapho init).")
        print(f"Next: qgrapho provider add {preset}  (coming soon)")

    print(f"\nConfig: {config_path()}")
    print("Docs:  https://github.com/quanvio/qgrapho/blob/main/docs/models.md")
    print("Run:   qgrapho doctor")
    return 0
