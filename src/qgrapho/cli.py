"""QGrapho command-line interface."""

from __future__ import annotations

import argparse
import sys

from qgrapho import __version__
from qgrapho.commands.doctor import run_doctor
from qgrapho.commands.init_cmd import run_init
from qgrapho.commands.index import run_index
from qgrapho.commands.start import run_start


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="qgrapho",
        description="QGrapho — graph-native autonomous engineering",
    )
    parser.add_argument("--version", action="version", version=f"qgrapho {__version__}")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init", help="First-time setup — provider and workspace")
    sub.add_parser("doctor", help="Verify installation and configuration")
    p_index = sub.add_parser("index", help="Index workspace into Graph Intelligence")
    p_index.add_argument("path", nargs="?", default=".", help="Path to index")
    sub.add_parser("start", help="Launch Console + Agent Engine (native profile)")
    sub.add_parser("upgrade", help="Upgrade QGrapho installation")
    sub.add_parser("uninstall", help="Remove CLI shim (keeps data)")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    cmd = args.command or "help"

    if cmd == "init":
        return run_init()
    if cmd == "doctor":
        return run_doctor()
    if cmd == "index":
        return run_index(args.path)
    if cmd == "start":
        return run_start()
    if cmd == "upgrade":
        print("Re-run scripts/install.sh or scripts/install.ps1 to upgrade.")
        return 0
    if cmd == "uninstall":
        print("Remove ~/.qgrapho/bin from PATH and delete the qgrapho entry point.")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
