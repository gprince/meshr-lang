# Guide de développement du LSP Meshr-Lang

## 🚀 Démarrage rapide

### Prérequis
- Python 3.10+
- Node.js 18+
- ANTLR parser généré (`make grammar`)

### Installation

#### Serveur LSP (Python)
```bash
cd lsp/server
pip install -r requirements.txt
```

#### Client VSCode (TypeScript)
```bash
cd lsp/client
npm install
npm run compile
```

### Test du serveur LSP
```bash
# Test direct
python lsp/server/main.py

# Test avec les tests unitaires
python -m pytest lsp/tests/test_lsp.py -v
```

### Test de l'extension VSCode
```bash
cd lsp/client
npm run compile
# Ouvrir VSCode dans ce dossier et appuyer sur F5
```

## 🏗️ Architecture

### Serveur LSP (Python)
- **`main.py`** : Point d'entrée du serveur
- **`language_server.py`** : Implémentation du serveur LSP
- **`parser.py`** : Intégration avec le parser ANTLR
- **`diagnostics.py`** : Validation et diagnostics
- **`completion.py`** : Autocomplétion
- **`symbols.py`** : Navigation et symboles

### Client VSCode (TypeScript)
- **`extension.ts`** : Extension VSCode/Cursor
- **`syntaxes/meshr.tmLanguage.json`** : Coloration syntaxique
- **`snippets/meshr.json`** : Snippets de code
- **`language-configuration.json`** : Configuration du langage

## 🔧 Développement

### Ajouter une nouvelle fonctionnalité

1. **Serveur LSP** : Modifier les composants Python
2. **Client** : Mettre à jour l'extension TypeScript si nécessaire
3. **Tests** : Ajouter des tests dans `lsp/tests/`
4. **Documentation** : Mettre à jour ce guide

### Debugging

#### Serveur LSP
```bash
# Activer les logs détaillés
export PYTHONPATH=.
python lsp/server/main.py --log-level DEBUG
```

#### Extension VSCode
1. Ouvrir `lsp/client` dans VSCode
2. Appuyer sur F5 pour lancer l'extension en mode debug
3. Ouvrir un fichier `.meshr` pour tester

### Intégration avec ANTLR

Le serveur LSP utilise le parser ANTLR généré. Assurez-vous que :

1. La grammaire est générée : `make grammar`
2. Le chemin Python est correct dans `parser.py`
3. Les imports ANTLR fonctionnent

## 📚 Ressources

- [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)
- [VSCode Extension API](https://code.visualstudio.com/api)
- [pygls Documentation](https://pygls.readthedocs.io/)
- [ANTLR Python Runtime](https://github.com/antlr/antlr4/tree/master/runtime/Python3)

## 🐛 Dépannage

### Erreurs communes

1. **"Module not found"** : Vérifier PYTHONPATH et la génération de la grammaire
2. **"Server not starting"** : Vérifier les logs et la configuration
3. **"No completions"** : Vérifier que le serveur LSP est actif

### Logs

Les logs du serveur LSP sont disponibles dans :
- Console de l'extension VSCode
- Sortie du serveur LSP
- Fichiers de log (si configurés)
