# 📚 Meshr-Lang Standard Library (StdLib)

La bibliothèque standard de Meshr-Lang fournit un ensemble d'artefacts prédéfinis, d'aspects et de types communs pour faciliter le développement d'architectures Data-as-a-Product.

## 🏗️ Structure

```
stdlib/
├── core/                    # Modules fondamentaux
│   ├── security.meshr      # Aspects et types de sécurité
│   ├── governance.meshr    # Gouvernance des données
│   ├── lifecycle.meshr     # Cycle de vie des données
│   ├── types.meshr         # Types de base et communs
│   └── annotations.meshr   # Annotations standard et méta-annotations
├── business/               # Modules métier
│   ├── domains.meshr       # Domaines métier communs
│   ├── entities.meshr      # Entités métier de base
│   └── processes.meshr     # Processus métier
├── analytics/              # Modules d'analytics
│   ├── metrics.meshr       # Types de métriques
│   ├── lineage.meshr       # Lignage des données
│   └── quality.meshr       # Qualité des données
└── integrations/           # Intégrations réglementaires
    ├── gdpr.meshr          # Conformité GDPR
    ├── sox.meshr           # Conformité SOX
    └── iso27001.meshr      # Conformité ISO 27001
```

## 🎯 Objectifs

- **Réutilisabilité** : Composants standards pour les cas d'usage courants
- **Cohérence** : Conventions et patterns établis
- **Productivité** : Réduction du temps de développement
- **Qualité** : Composants testés et validés

## 📋 Roadmap

- [ ] **Phase 1** : Modules `security` et `governance`
- [ ] **Phase 2** : Modules `business` et `lifecycle`  
- [ ] **Phase 3** : Module `analytics` et intégrations
- [ ] **Phase 4** : Outils de validation et génération
- [ ] **Phase 5** : Documentation et exemples

## 🚀 Utilisation

### Import des composants

```meshr
module mon.module

// Import groupé (recommandé)
import { DataClassification, GDPRCompliance } from meshr.security
import { DataStewardship, WithStewardship } from meshr.governance
import { WithLifecycle } from meshr.lifecycle

// Import simple
import Status from meshr.types

// Import wildcard
import * from meshr.types

export { Customer }

// Utilisation dans vos artefacts
entity Customer with WithStewardship, WithLifecycle is
  customer_id : String
  email : String
  status : Status
  
  aspects {
    DataClassification { 
      level: "confidential", 
      encryption_required: true 
    }
  }
end
```

### Types d'imports supportés

- **Import simple** : `import Item from module`
- **Import groupé** : `import { Item1, Item2 } from module`
- **Import wildcard** : `import * from module`

> 📖 Voir [IMPORTS.md](IMPORTS.md) pour un guide complet des imports.

## 🏷️ Annotations

### Import des annotations

```meshr
module mon.module

// Import des annotations standard
import { Version, Author, Documented, Experimental } from meshr.annotations

export { MonEntite }

// Utilisation des annotations
@Version("1.0.0")
@Author(name="Mon Équipe", email="team@company.com")
@Documented(summary="Mon entité de test")
@Experimental(reason="Nouvelle fonctionnalité")
entity MonEntite is
  id : String
  name : String
end
```

### Types d'annotations disponibles

- **Méta-annotations** : `@Target`, `@Retention`, `@Repeatable`
- **Annotations communes** : `@Experimental`, `@Deprecated`, `@Version`, `@Author`, `@Scope`, `@Confidentiality`, `@Documented`

> 📖 Voir [ANNOTATIONS.md](ANNOTATIONS.md) pour un guide complet des annotations.

## 📝 Conventions

- **Nommage** : Utiliser des noms descriptifs et cohérents
- **Documentation** : Chaque artefact doit être documenté
- **Tests** : Chaque module doit avoir ses tests de validation
- **Versioning** : Suivre le versioning sémantique
- **Compatibilité** : Maintenir la rétrocompatibilité

## 🔧 Développement

Pour contribuer à la stdlib :

1. Créer un nouveau module dans le dossier approprié
2. Suivre les conventions de nommage
3. Ajouter des tests de validation
4. Documenter les cas d'usage
5. Mettre à jour ce README

## 📚 Documentation

Voir la section "Bibliothèque Standard (StdLib)" dans la documentation principale (`docs/meshr-lang.md`) pour plus de détails sur les modules proposés et leurs cas d'usage.
