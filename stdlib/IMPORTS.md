# 📥 Guide des Imports dans Meshr-Lang StdLib

Ce guide explique comment utiliser les imports dans la bibliothèque standard Meshr-Lang.

## 🎯 Types d'imports supportés

### 1. Import simple
```meshr
import Status from meshr.types
```
Importe un seul élément (enum, aspect, trait, etc.) d'un module.

### 2. Import groupé (recommandé)
```meshr
import { DataClassification, WithSecurity } from meshr.security
```
Importe plusieurs éléments spécifiques d'un module. C'est la méthode recommandée car elle est explicite et évite les conflits de noms.

### 3. Import wildcard
```meshr
import * from meshr.types
```
Importe tous les éléments exportés d'un module. Utilisez avec précaution pour éviter les conflits de noms.

## 📋 Ordre des déclarations

L'ordre correct dans un module Meshr-Lang est :

```meshr
module mon.module

// 1. Imports (après la déclaration du module)
import { Item1, Item2 } from autre.module

// 2. Exports (après les imports)
export { MonItem }

// 3. Déclarations (enums, aspects, traits, entités, etc.)
enum MonEnum is ("value1", "value2")
end
```

## 🚀 Exemples pratiques

### Exemple 1 : Import simple
```meshr
module examples.simple

import Status from meshr.types

export { Product }

entity Product is
  product_id : String
  status : Status
end
```

### Exemple 2 : Import groupé
```meshr
module examples.grouped

import { DataClassification, WithSecurity } from meshr.security
import { DataStewardship, WithStewardship } from meshr.governance

export { Customer }

entity Customer with WithSecurity, WithStewardship is
  customer_id : String
  
  aspects {
    DataClassification {
      level: "confidential",
      encryption_required: true,
      access_control: "role-based",
      data_retention: Interval 7 year,
      steward: "privacy@company.com"
    }
  }
end
```

### Exemple 3 : Import wildcard
```meshr
module examples.wildcard

import * from meshr.types

export { Company }

entity Company is
  company_id : String
  status : Status
  priority : Priority
end
```

## ⚠️ Bonnes pratiques

### ✅ Recommandé
- **Import groupé** : `import { Item1, Item2 } from module`
- **Noms explicites** : Utilisez des noms de modules clairs
- **Organisation** : Groupez les imports par module

### ❌ À éviter
- **Conflits de noms** : Évitez les imports wildcard si possible
- **Imports multiples** : Ne mélangez pas import simple et wildcard du même module
- **Ordre incorrect** : Respectez l'ordre module → imports → exports → déclarations

## 🔧 Résolution des erreurs courantes

### Erreur : "extraneous input 'import'"
**Cause** : L'import est placé après les exports ou déclarations.
**Solution** : Placez les imports juste après la déclaration du module.

### Erreur : "mismatched input '}' expecting ','"
**Cause** : Import groupé avec un seul élément.
**Solution** : Utilisez l'import simple ou ajoutez d'autres éléments.

### Erreur : "cannot resolve reference"
**Cause** : L'élément importé n'existe pas dans le module source.
**Solution** : Vérifiez que l'élément est bien exporté dans le module source.

## 📚 Modules disponibles

### `meshr.security`
- **Aspects** : `DataClassification`, `GDPRCompliance`, `SecurityControls`
- **Traits** : `WithSecurity`, `WithGDPR`
- **Types de relations** : `ACCESS_CONTROL`, `DATA_SHARING`
- **Enums** : `DataClassificationLevel`, `AccessControlType`

### `meshr.governance`
- **Aspects** : `DataStewardship`, `DataQuality`, `DataLineage`
- **Traits** : `WithStewardship`, `WithQuality`
- **Types de relations** : `DATA_OWNERSHIP`, `QUALITY_REVIEW`
- **Enums** : `DataQualityLevel`, `StewardshipRole`

### `meshr.lifecycle`
- **Aspects** : `DataLifecycle`, `VersionControl`
- **Traits** : `WithLifecycle`, `WithVersioning`
- **Types de relations** : `VERSION_TRANSITION`, `STATUS_CHANGE`
- **Enums** : `DataStatus`, `LifecycleStage`

### `meshr.types`
- **Aspects** : `ContactInfo`, `Address`
- **Traits** : `WithContactInfo`
- **Enums** : `Status`, `Priority`

## 🧪 Tests

Pour tester vos imports, utilisez :

```bash
# Test d'un fichier spécifique
.venv/bin/python tests/parse_module.py votre_fichier.meshr

# Test de toute la stdlib
make test-stdlib
```

## 📖 Exemples complets

Consultez les fichiers dans `stdlib/examples/` pour des exemples complets :
- `simple-imports.meshr` : Import simple et groupé
- `imports-demo.meshr` : Tous les types d'imports
- `customer-entity.meshr` : Exemple complet avec gouvernance
