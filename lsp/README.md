# Meshr-Lang Language Server Protocol (LSP)

Ce dossier contient l'implémentation du Language Server Protocol pour Meshr-Lang, permettant l'intégration avec VSCode, Cursor et autres éditeurs supportant LSP.

## 🏗️ Architecture

```
lsp/
├── server/                 # Serveur LSP (Python)
│   ├── __init__.py
│   ├── main.py            # Point d'entrée du serveur
│   ├── language_server.py # Implémentation du serveur LSP
│   ├── parser.py          # Intégration avec le parser ANTLR
│   ├── diagnostics.py     # Validation et diagnostics
│   ├── completion.py      # Autocomplétion
│   └── symbols.py         # Navigation et symboles
├── client/                # Client LSP (TypeScript)
│   ├── package.json
│   ├── src/
│   │   ├── extension.ts   # Extension VSCode/Cursor
│   │   └── client.ts      # Client LSP
│   └── syntaxes/
│       └── meshr.tmLanguage.json # Coloration syntaxique
├── tests/                 # Tests du LSP
└── docs/                  # Documentation LSP
```

## 🚀 Fonctionnalités

### Phase 1 - Base
- [x] Structure du projet
- [ ] Serveur LSP Python
- [ ] Client TypeScript
- [ ] Coloration syntaxique
- [ ] Validation basique

### Phase 2 - Avancé
- [ ] Autocomplétion intelligente
- [ ] Navigation dans le code
- [ ] Refactoring
- [ ] Hover information
- [ ] Formatage automatique

### Phase 3 - Expert
- [ ] Intégration avec la stdlib
- [ ] Suggestions contextuelles
- [ ] Debugging support
- [ ] Multi-workspace

## 🛠️ Développement

### Prérequis
- Python 3.10+
- Node.js 18+
- ANTLR parser généré

### Installation
```bash
# Serveur LSP
cd lsp/server
pip install -r requirements.txt

# Rebuilder le binaire standalone (PyInstaller)
python build_server.py

# Client VSCode
cd lsp/client
npm install
```

Le script `build_server.py` encapsule désormais la configuration de PyInstaller :
- il force PyInstaller à utiliser des caches locaux au dépôt (utile dans les environnements sandboxés) ;
- il collecte automatiquement tous les sous-modules `pygls`/`lsprotocol` pour éviter les erreurs `ImportError` lors du lancement du serveur embarqué.


### Test
```bash
# Test du serveur LSP
python lsp/server/main.py

# Test de l'extension
cd lsp/client
npm run compile
```

## 🆕 Nouvelles fonctionnalités (v0.2.0)

### 📊 Support des métriques
- ✅ **Coloration syntaxique** : `metric`, `source`, `calculation`, `aggregation`, etc.
- ✅ **Snippets** : Templates pour métriques simples et complexes
- ✅ **Pattern matching** : Support de `match...is...end` avec `or`
- ✅ **Validation** : Détection des erreurs de syntaxe métrique

### 📝 Exports annotés
- ✅ **Export inline** : `@annotation export enum MyEnum`
- ✅ **Validation** : Rejet des annotations sur exports groupés

## 📚 Ressources

- [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)
- [VSCode Extension API](https://code.visualstudio.com/api)
- [ANTLR Python Runtime](https://github.com/antlr/antlr4/tree/master/runtime/Python3)
