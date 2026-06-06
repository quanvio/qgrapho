"""Load and validate QGrapho config.toml."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def load_config(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    with path.open("rb") as fh:
        return tomllib.load(fh)


def has_provider_key() -> bool:
    keys = (
        "OPENAI_API_KEY",
        "DEEPSEEK_API_KEY",
        "MOONSHOT_API_KEY",
        "XAI_API_KEY",
        "OPENROUTER_API_KEY",
        "ANTHROPIC_API_KEY",
        "AZURE_OPENAI_API_KEY",
        "QGRAPHO_CLOUD_API_KEY",
    )
    return any(os.environ.get(k) for k in keys)


def config_exists() -> bool:
    from qgrapho.paths import config_path

    return config_path().is_file()
