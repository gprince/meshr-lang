# Meshr-Lang

> A DSL to describe the components of a modern Data-as-a-Product architecture (domains, products, contracts, aspects, policies, teams…).

## Structure

- `grammar/` → ANTLR v4 grammar files (.g4)
- `cli/`     → CLI tool (Python or Kotlin)
- `lsp/`     → Language Server (VSCode/Cursor)
- `docs/`    → Markdown documentation
- `examples/`→ DSL examples (.ms)
- `stdlib/`  → Standard library modules (.meshr)
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

# 5. Run all tests
make test

# 6. Check for test failures only
make test-failures
```

---

## 🛠 Toolchain

- **Language**: Python 3.10+
- **Parser Generator**: [ANTLR 4.13.2](https://www.antlr.org/)
- **Runtime**: `antlr4-python3-runtime`
- **Grammar file**: [`grammar/MeshrModule.g4`](grammar/MeshrModule.g4)
- **Generated code**: `grammar/generated/`

## 📋 Commandes disponibles

### 🔧 Développement
- `make grammar` : Génère le parser ANTLR
- `make test` : Exécute tous les tests
- `make test-failures` : Affiche uniquement les tests qui échouent
- `make test-stdlib` : Teste les modules de la bibliothèque standard
- `make clean` : Nettoie les fichiers générés
- `make all` : Exécute grammar + test + test-stdlib

### 📚 Documentation
- `make docs` : Génère la documentation PDF et HTML
- `make docs-pdf` : Génère uniquement la documentation PDF
- `make docs-html` : Génère uniquement la documentation HTML
- `make docs-clean` : Supprime les fichiers de documentation générés

---

## 📁 Notes

- The `grammar/generated/` folder is not committed (see `.gitignore`)
- The Makefile ensures grammar generation and module structure
- DSL file extension: `.meshr`

📚 See full spec in [docs/meshr-lang.md](docs/meshr-lang.md)

---
