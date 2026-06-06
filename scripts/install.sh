#!/usr/bin/env bash
# QGrapho one-click installer (macOS / Linux)
set -euo pipefail

QGRAPHO_HOME="${QGRAPHO_HOME:-$HOME/.qgrapho}"
FROM_SOURCE=false

for arg in "$@"; do
  case "$arg" in
    --from-source) FROM_SOURCE=true ;;
  esac
done

info()  { echo "==> $*"; }
ok()    { echo " ok  $*"; }
warn()  { echo " !!  $*"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO_ROOT="$SCRIPT_DIR"

info "Installing QGrapho to $QGRAPHO_HOME"
mkdir -p "$QGRAPHO_HOME/data/graphs" "$QGRAPHO_HOME/config"

export QGRAPHO_HOME
export QGRAPHO_SRC="$REPO_ROOT"

# Config template
if [[ -f "$REPO_ROOT/config/qgrapho.example.toml" ]]; then
  cp "$REPO_ROOT/config/qgrapho.example.toml" "$QGRAPHO_HOME/config/qgrapho.example.toml"
  [[ -f "$QGRAPHO_HOME/config.toml" ]] || cp "$REPO_ROOT/config/qgrapho.example.toml" "$QGRAPHO_HOME/config.toml"
fi

# Python CLI (preferred)
if command -v python3 >/dev/null 2>&1; then
  info "Installing QGrapho CLI (Python 3.11+)"
  python3 -m pip install --upgrade pip >/dev/null 2>&1 || true
  if python3 -m pip install -e "$REPO_ROOT" --quiet; then
    ok "qgrapho CLI installed via pip"
  else
    warn "pip install failed — ensure Python 3.11+ and pip are available"
    warn "Try: cd $REPO_ROOT && python3 -m pip install -e ."
  fi
else
  warn "python3 not found — install Python 3.11+ then re-run this script"
fi

# PATH hint for user installs
if [[ -d "$HOME/.local/bin" ]] && ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
  SHELL_RC="$HOME/.bashrc"
  [[ -n "${ZSH_VERSION:-}" ]] && SHELL_RC="$HOME/.zshrc"
  if ! grep -q '.local/bin' "$SHELL_RC" 2>/dev/null; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
    ok "Added ~/.local/bin to PATH in $SHELL_RC"
  fi
fi

if $FROM_SOURCE; then
  ln -sfn "$REPO_ROOT" "$QGRAPHO_HOME/src" 2>/dev/null || true
  ok "Linked source: $QGRAPHO_HOME/src"
fi

ok "QGrapho installed"
echo ""
echo "Next steps:"
echo "  1. qgrapho --version"
echo "  2. qgrapho init"
echo "  3. qgrapho doctor"
echo "  4. qgrapho start"
echo ""
echo "Development: see ROADMAP.md · No Podman, Docker, or Kubernetes required."
