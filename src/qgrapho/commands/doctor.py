"""qgrapho doctor — verify installation."""

from __future__ import annotations

from qgrapho import __version__
from qgrapho.config import config_exists, has_provider_key, load_config
from qgrapho.paths import config_path, graphs_dir, qgrapho_home


def _status(ok: bool) -> str:
    return "OK" if ok else "run qgrapho init"


def run_doctor() -> int:
    home = qgrapho_home()
    home.mkdir(parents=True, exist_ok=True)
    graphs_dir().mkdir(parents=True, exist_ok=True)

    cfg_ok = config_exists()
    cfg = load_config(config_path()) if cfg_ok else {}
    product = cfg.get("product", {}).get("name", "QGrapho")

    print(f"QGrapho Doctor v{__version__}\n")
    print(f"  Home ................. {home}")
    print(f"  Product .............. {product}")
    print(f"  Config ............... {_status(cfg_ok)}")
    print("  Console .............. pending (Phase 0)")
    print("  Agent Engine ......... pending (Phase 0, RUNTIME=process)")
    print("  Graph Intelligence ... pending (Phase 1)")
    print(f"  Model Router ......... {_status(has_provider_key())}")
    print("  Event Bus ............ optional")
    print("  Insights ............. optional")
    print()
    print("Phase 0 in progress — see ROADMAP.md")

    if not cfg_ok or not has_provider_key():
        return 1
    return 0
