"""QGrapho filesystem paths."""

from __future__ import annotations

import os
from pathlib import Path


def qgrapho_home() -> Path:
    raw = os.environ.get("QGRAPHO_HOME", "")
    if raw:
        return Path(raw).expanduser()
    return Path.home() / ".qgrapho"


def config_path() -> Path:
    return qgrapho_home() / "config.toml"


def data_dir() -> Path:
    return qgrapho_home() / "data"


def graphs_dir() -> Path:
    return data_dir() / "graphs"


def repo_config_example() -> Path | None:
    """Example config shipped with a source checkout."""
    src = os.environ.get("QGRAPHO_SRC")
    if src:
        candidate = Path(src) / "config" / "qgrapho.example.toml"
        if candidate.is_file():
            return candidate
    return None
