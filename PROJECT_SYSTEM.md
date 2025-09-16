# 🎯 Système de Projet Meshr-Lang

## 📋 Vue d'ensemble

Le système de projet Meshr-Lang permet de gérer les dépendances, résoudre les imports et fournir des fonctionnalités LSP avancées pour les projets Meshr-Lang.

## 🏗️ Architecture

### Composants principaux

1. **`meshr.toml`** - Configuration de projet
2. **`meshr_project.py`** - Gestionnaire de projet Python
3. **`lsp/server/project_manager.py`** - Intégration LSP
4. **StdLib** - Bibliothèque standard avec modules

## 📁 Structure de projet

```
mon-projet-meshr/
├── meshr.toml              # Configuration du projet
├── src/                    # Code source
│   └── mon-module.meshr    # Module principal
├── docs/                   # Documentation générée
└── dist/                   # Artifacts de build
```

## ⚙️ Configuration (`meshr.toml`)

```toml
[project]
name = "mon-projet"
version = "1.0.0"
description = "Description du projet"
authors = ["Auteur <email@example.com>"]
license = "MIT"

[project.module]
name = "mon.module"
path = "src/mon-module.meshr"

[dependencies]
meshr-stdlib = { version = "1.0.0", path = "../stdlib" }

[build]
target = "data-mesh"
output = "dist/"

[lsp]
enable_diagnostics = true
enable_completion = true
enable_hover = true
```

## 🔗 Gestion des dépendances

### Dépendances locales
```toml
[dependencies]
ma-bibliotheque = { version = "1.0.0", path = "../ma-bibliotheque" }
```

### Dépendances externes (futures)
```toml
[dependencies]
meshr-analytics = { version = "2.1.0", registry = "https://registry.meshr-lang.org" }
company-security = { version = "1.5.0", git = "https://github.com/company/security" }
```

## 📦 StdLib

La bibliothèque standard fournit des modules essentiels :

- **`meshr.security`** - Classification des données, GDPR, contrôle d'accès
- **`meshr.governance`** - Stewardship, qualité des données
- **`meshr.lifecycle`** - Gestion du cycle de vie des données
- **`meshr.types`** - Types de base
- **`meshr.annotations`** - Annotations et métadonnées

## 🚀 Utilisation

### 1. Créer un projet

```bash
mkdir mon-projet
cd mon-projet
```

Créer `meshr.toml` :
```toml
[project]
name = "mon-projet"
version = "1.0.0"

[project.module]
name = "mon.module"
path = "src/mon-module.meshr"

[dependencies]
meshr-stdlib = { version = "1.0.0", path = "../stdlib" }
```

### 2. Écrire le code

`src/mon-module.meshr` :
```meshr
module mon.module

import { DataClassification, WithSecurity } from meshr.security
import { DataStewardship, WithStewardship } from meshr.governance

export { MonEntite }

entity MonEntite with WithSecurity, WithStewardship is
  id : String
  name : String
  
  aspects {
    DataClassification {
      level: "internal",
      encryption_required: false,
      access_control: "role-based",
      data_retention: Interval 5 year,
      steward: "admin@company.com"
    }
  }
end
```

### 3. Tester le projet

```bash
python meshr_project.py .
```

## 🔧 API Python

### Gestionnaire de projet

```python
from meshr_project import MeshrProjectManager

# Charger un projet
manager = MeshrProjectManager("mon-projet")
config = manager.load_config()
modules = manager.resolve_dependencies()

# Résoudre un symbole
symbol_info = manager.resolve_import("mon.module", "DataClassification")

# Valider les imports
errors = manager.validate_imports("mon.module")
```

### Gestionnaire LSP

```python
from lsp.server.project_manager import LSPProjectManager

# Créer le gestionnaire
manager = LSPProjectManager()
manager.add_workspace_root("mon-projet")

# Résoudre un symbole
symbol_info = manager.resolve_symbol("file://mon-projet/src/module.meshr", "DataClassification")

# Obtenir les complétions
completions = manager.get_completion_items("file://mon-projet/src/module.meshr", "mon.module")
```

## 🎯 Fonctionnalités LSP

### Résolution de symboles
- **Go to Definition** - Navigation vers la définition
- **Hover** - Informations au survol
- **Find References** - Recherche de références

### Complétion intelligente
- Symboles exportés des modules
- Symboles des dépendances
- Contexte basé sur les imports

### Diagnostics avancés
- Validation des imports
- Vérification des dépendances
- Détection des symboles non résolus

## 📊 Exemple complet

Voir `examples/hr-employees-project/` pour un exemple complet :

```bash
cd examples/hr-employees-project
python ../../meshr_project.py .
```

Résultat :
```
Project: hr-employees v1.0.0
Module: hr.employees
Dependencies: ['meshr-stdlib']

Loaded modules: ['meshr.security', 'meshr.governance', 'meshr.lifecycle', 'meshr.types', 'meshr.annotations', 'hr.employees']

Module: meshr.security
  Exports: ['DataClassificationLevel', 'AccessControlType', 'DataClassification', 'GDPRCompliance', 'SecurityControls', 'WithSecurity', 'WithGDPR', 'ACCESS_CONTROL', 'DATA_SHARING']
  Imports: []

Module: hr.employees
  Exports: ['Employee', 'Department', 'Position', 'EmployeeSkill']
  Imports: ['meshr.security', 'meshr.governance', 'meshr.lifecycle']
```

## 🔮 Roadmap

### Fonctionnalités futures
- [ ] Registry de packages
- [ ] Gestion des versions sémantiques
- [ ] Build system intégré
- [ ] Tests automatisés
- [ ] Documentation générée automatiquement
- [ ] Support des workspaces multi-projets

### Améliorations LSP
- [ ] Refactoring (rename, extract)
- [ ] Code actions
- [ ] Formatage automatique
- [ ] IntelliSense avancé

## 🐛 Dépannage

### Problèmes courants

1. **Module non trouvé**
   - Vérifier le chemin dans `meshr.toml`
   - S'assurer que le module existe et est exporté

2. **Symbole non résolu**
   - Vérifier que le symbole est exporté
   - Vérifier l'import dans le module

3. **Dépendance circulaire**
   - Réorganiser les imports
   - Utiliser des interfaces communes

## 📚 Ressources

- [Documentation Meshr-Lang](docs/meshr-lang.md)
- [Grammaire EBNF](grammar/meshr_module.ebnf)
- [Exemples](examples/)
- [StdLib](stdlib/)
