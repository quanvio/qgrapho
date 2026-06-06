"""qgrapho index — index workspace into Graph Intelligence."""

from __future__ import annotations

from pathlib import Path


def run_index(path: str) -> int:
    target = Path(path).resolve()
    if not target.exists():
        print(f"Error: path not found: {target}")
        return 1

    print(f"Indexing {target} into QGrapho Graph Intelligence...")
    print("Status: Phase 1 — wire to index_repository MCP handler.")
    print("Track:  https://github.com/quanvio/qgrapho/blob/main/ROADMAP.md")
    return 0
