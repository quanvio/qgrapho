"""qgrapho start — launch Console + Agent Engine."""

from __future__ import annotations

import os


def run_start() -> int:
    os.environ.setdefault("RUNTIME", "process")
    print("Starting QGrapho (native profile)...")
    print(f"  RUNTIME={os.environ['RUNTIME']}  (no Docker / Podman / K8s required)")
    print("  Console + Agent Engine: Phase 0 — not yet wired to release bundle.")
    print("  See ROADMAP.md for Phase 0 exit criteria.")
    return 0
