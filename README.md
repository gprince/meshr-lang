# Meshr-Lang

> A DSL to describe the components of a modern Data-as-a-Product architecture (domains, products, contracts, aspects, policies, teams…).

## Structure

- `grammar/` → ANTLR v4 grammar files (.g4)
- `cli/`     → CLI tool (Python or Kotlin)
- `lsp/`     → Language Server (VSCode/Cursor)
- `docs/`    → Markdown documentation
- `examples/`→ DSL examples (.ms)
- `tests/`   → Parser and CLI unit tests

---

## 🧰 Getting Started (Python + ANTLR)

```bash
# 1. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate parser (ANTLR → Python)
make grammar

# 4. Run test parser
python tests/parse_module.py
```

---

## 🛠 Toolchain

- **Language**: Python 3.10+
- **Parser Generator**: [ANTLR 4.13.2](https://www.antlr.org/)
- **Runtime**: `antlr4-python3-runtime`
- **Grammar file**: [`grammar/MeshrModule.g4`](grammar/MeshrModule.g4)
- **Generated code**: `grammar/generated/`

---

## 📁 Notes

- The `grammar/generated/` folder is not committed (see `.gitignore`)
- The Makefile ensures grammar generation and module structure
- DSL file extension: `.meshr`

📚 See full spec in [docs/meshr-lang.md](docs/meshr-lang.md)

---
