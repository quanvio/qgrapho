# Contributing to QGrapho

Thank you for helping build the graph-native future of software engineering.

---

## Before you start

1. Read the [README](../README.md) and [Architecture](architecture.md)  
2. Run `qgrapho doctor` after setup  
3. Open an issue for large changes before opening a PR  

---

## Development setup

```bash
git clone https://github.com/quanvio/qgrapho.git
cd qgrapho
python -m pip install -e ".[dev]"
export QGRAPHO_SRC="$(pwd)"
qgrapho init
qgrapho doctor
```

Or use the installer:

```bash
./scripts/install.sh --from-source   # macOS / Linux
# or
.\scripts\install.ps1 --from-source  # Windows
```

---

## Pull requests

1. Fork [quanvio/qgrapho](https://github.com/quanvio/qgrapho)  
2. Create a focused branch (`feat/`, `fix/`, `docs/`)  
3. Keep changes scoped — one concern per PR  
4. Update docs when behavior or config changes  
5. Ensure public docs use **QGrapho product names only** (no third-party engine names in user-facing markdown)  

---

## Documentation standards

Public docs should read like a product from a top-tier platform company:

- Clear headings and short paragraphs  
- Tables for comparisons  
- Diagrams for architecture (`docs/assets/*.svg`)  
- Copy-pasteable commands that work  
- No internal implementation vendor names in README or `docs/`  

**Quanvio maintainers:** internal vendor map lives in `.qgrapho.md` at repo root — **gitignored, never pushed**. Request a copy from the team if you need engine-level detail.

---

## Code of conduct

See [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md).

---

## Security

See [SECURITY.md](../SECURITY.md) for vulnerability reporting.

---

## License

By contributing, you agree your contributions are licensed under the [MIT License](../LICENSE).
