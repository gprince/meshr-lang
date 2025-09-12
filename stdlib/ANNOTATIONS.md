# 🏷️ Guide des Annotations dans Meshr-Lang StdLib

Ce guide explique comment utiliser les annotations standard et créer des annotations personnalisées dans Meshr-Lang.

## 🎯 Vue d'ensemble

Les annotations permettent d'ajouter des métadonnées structurées sur n'importe quelle déclaration Meshr-Lang. Elles sont inspirées des annotations Java/Kotlin et des directives GraphQL.

## 📦 Module `meshr.annotations`

Le module `meshr.annotations` fournit :
- **Méta-annotations** : `@Target`, `@Retention`, `@Repeatable`
- **Annotations communes** : `@Experimental`, `@Deprecated`, `@Version`, etc.
- **Enums de support** : `RetentionPolicy`, `AnnotationTarget`, `ScopeLevel`, etc.

## 🔧 Méta-annotations

### `@Target`
Spécifie sur quels types d'éléments l'annotation peut être utilisée.

```meshr
@Target("all")           // Tous les éléments
@Target("annotation")    // Seulement les annotations
@Target("entity")        // Seulement les entités
@Target("module")        // Seulement les modules
```

**Valeurs possibles :**
- `"all"` : Tous les éléments
- `"annotation"` : Annotations
- `"enum"` : Énumérations
- `"module"` : Modules
- `"record"` : Records
- `"trait"` : Traits
- `"aspect"` : Aspects
- `"entity"` : Entités
- `"type_relation"` : Types de relations
- `"relation"` : Relations

### `@Retention`
Spécifie la durée de vie de l'annotation.

```meshr
@Retention(compile)  // Supprimée à la compilation
@Retention(model)    // Conservée dans le modèle
@Retention(export)   // Exportée avec l'artefact
```

### `@Repeatable`
Indique si l'annotation peut être utilisée plusieurs fois sur le même élément.

```meshr
@Repeatable(true)   // Peut être répétée
@Repeatable(false)  // Ne peut pas être répétée
```

## 🏷️ Annotations communes

### `@Experimental`
Marque un élément comme expérimental.

```meshr
@Experimental(reason="Feature is experimental and may change")
```

### `@Deprecated`
Marque un élément comme déprécié.

```meshr
@Deprecated(
  reason="Use new OrderV2 entity instead",
  since="2024-01-01",
  replacement="OrderV2"
)
```

### `@Version`
Spécifie la version d'un élément.

```meshr
@Version("1.2.0")
```

### `@Author`
Spécifie l'auteur d'un élément.

```meshr
@Author(
  name="Data Team",
  email="data@company.com",
  organization="ACME Corp"
)
```

### `@Scope`
Spécifie la portée d'un élément.

```meshr
@Scope(level="internal", description="Internal use only")
```

**Niveaux possibles :**
- `"public"` : Public
- `"internal"` : Interne
- `"private"` : Privé

### `@Confidentiality`
Spécifie le niveau de confidentialité.

```meshr
@Confidentiality(
  level="confidential",
  classification="PII",
  handling_instructions="Encrypt at rest"
)
```

**Niveaux possibles :**
- `"public"` : Public
- `"internal"` : Interne
- `"confidential"` : Confidentiel
- `"restricted"` : Restreint

### `@Documented`
Ajoute de la documentation structurée.

```meshr
@Documented(
  summary="Customer entity with personal information",
  description="Core entity for customer data management",
  examples="See examples/ directory",
  see_also="CustomerV2 entity"
)
```

## 🛠️ Création d'annotations personnalisées

### Syntaxe de base

```meshr
@Target("all")
@Retention(model)
annotation MonAnnotation is
  required nom : String
  optional valeur : String = "défaut"
  optional actif : Boolean = true
end
```

### Champs `required` vs `optional`

- **`required`** : Champ obligatoire, sans valeur par défaut
- **`optional`** : Champ optionnel, avec ou sans valeur par défaut

### Types supportés

- **Types de base** : `String`, `Boolean`, `Integer`, `Float`, `Date`, `Timestamp`
- **Enums** : `MonEnum`
- **Collections** : `List of String`, `Map of String to Integer`

### Exemple complet

```meshr
@Target("entity")
@Retention(model)
@Repeatable(true)
annotation Tag is
  required name : String
  optional priority : Integer = 1
  optional category : String = "general"
end

// Utilisation
@Tag(name="important", priority=5)
@Tag(name="reviewed", category="quality")
entity Customer is
  id : String
  name : String
end
```

## 📋 Bonnes pratiques

### ✅ Recommandé
- **Utilisez des noms clairs** : `@Version` plutôt que `@V`
- **Documentez vos annotations** : Utilisez `@Documented`
- **Spécifiez la portée** : Utilisez `@Target` approprié
- **Groupez les annotations** : Placez-les ensemble au-dessus de l'élément

### ❌ À éviter
- **Annotations sans `@Target`** : Spécifiez toujours la portée
- **Champs `required` avec valeurs par défaut** : Utilisez `optional`
- **Annotations trop complexes** : Gardez-les simples et focalisées
- **Noms ambigus** : Évitez les noms génériques comme `@Info`

## 🎯 Exemples d'utilisation

### Module annoté
```meshr
@Version("1.0.0")
@Author(name="Data Team", email="data@company.com")
@Scope(level="internal")
@Confidentiality(level="confidential")
module mon.module
```

### Entité annotée
```meshr
@Version("1.2.0")
@Author(name="Product Team")
@Documented(summary="Customer entity with personal information")
@Experimental(reason="New customer model, API may change")
entity Customer is
  id : String
  name : String
end
```

### Annotation personnalisée
```meshr
@Target("all")
@Retention(model)
annotation QualityGate is
  required level : String
  optional automated : Boolean = true
  optional reviewer : String = ""
end

@QualityGate(level="high", reviewer="senior-dev")
entity CriticalEntity is
  id : String
end
```

## 🧪 Tests

Pour tester vos annotations :

```bash
# Test d'un fichier spécifique
.venv/bin/python tests/parse_module.py votre_fichier.meshr

# Test de toute la stdlib
make test-stdlib
```

## 📖 Exemples complets

Consultez les fichiers dans `stdlib/examples/` :
- `annotations-usage.meshr` : Utilisation des annotations communes
- `meta-annotations.meshr` : Création d'annotations personnalisées

## 🔗 Intégration avec la stdlib

Les annotations s'intègrent parfaitement avec les autres modules de la stdlib :

```meshr
import { DataClassification, WithSecurity } from meshr.security
import { Version, Author, Documented } from meshr.annotations

@Version("1.0.0")
@Author(name="Security Team")
@Documented(summary="Secure customer entity")
entity SecureCustomer with WithSecurity is
  id : String
  
  aspects {
    DataClassification {
      level: "confidential",
      encryption_required: true
    }
  }
end
```
