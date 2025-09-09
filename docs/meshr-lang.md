# Meshr-Lang — Documentation du langage

> **Version :** 0.1.0  
> **Statut :** En conception active  
> **Mainteneur :** G. Prince - Architecte Principal
> **Dernière mise à jour :** YYYY-MM-DD

---

## 🧭 Objectif du langage

Meshr-Lang est un langage déclaratif dédié à la description des artefacts d’une architecture **Data-as-a-Product**, tels que les domaines, produits de données, contrats, aspects (métadonnées), équipes et politiques.

Il vise à offrir une syntaxe lisible, formelle et exécutable pour :
- Structurer la documentation vivante du data mesh
- Générer automatiquement les représentations techniques (YAML, Rego, Terraform, etc.)
- Alimenter les registres, catalogues et plateformes self-service

---

## 🔤 Syntaxe de base

- Fichiers : `.meshr`
- Style : déclaratif à blocs (inspiré de HCL, Kotlin DSL, GraphQL SDL)
- Commentaires : `// commentaire ligne` ou `/* commentaire bloc */`
- Valeurs :
  - Chaînes : `"texte"`
  - Références : `contract:domain:name:1.0.0`

### 💬 Commentaires

- Les commentaires sur une seule ligne commencent par `//`
- Les commentaires multi-lignes sont délimités par `/*` et `*/`
- Ils sont ignorés par l’analyse syntaxique (non représentés dans l’AST)

#### Exemples :

```meshr
// Ceci est un commentaire simple

/*
  Ceci est un commentaire
  sur plusieurs lignes
*/

---

## 📦 Déclaration des modules et imports

La première unité structurante de Meshr est le **module**. Il représente un espace de noms versionné, à partir duquel les autres artefacts sont déclarés ou importés.

### 📐 Syntaxe

```meshr
module marketing.analytics

import Customer from marketing.shared         // ✅ forme simple
import { Customer } from marketing.shared     // ✅ forme équivalente
import { * } from core.types                  // ✅ importation complète
import * from core.types                      // ✅ forme équivalente

import Customer, Producer from marketing.shared // ❌ interdit : nécessite des accolades

// autres déclarations

```

### 📚 Sémantique

- **Un fichier `.meshr` = un module unique**.
- Le `module` définit le **namespace** des artefacts qu’il contient.
- Les `import` permettent d'accéder à des symboles publics d'autres modules.
- Les annotations `@module_*` sont optionnelles mais encouragées pour documenter les modules.
- Les `import` permettent d'accéder à des symboles **explicitement exportés** d'autres modules.
- Les éléments d’un module **ne sont pas visibles depuis l’extérieur** s’ils ne sont pas précédés du mot-clé `export`.
- L’import de `{ * }` signifie **importer tous les symboles exportés** du module cible.
- L’import de `{ A, B }` permet une **importation sélective**.
- Les accolades `{}` sont **optionnelles uniquement si un seul identifiant** est importé.
- Si plusieurs identifiants sont importés d’un même module, l’usage des accolades est **obligatoire**.

### 📤 Export des déclarations

Deux formes d'export sont possibles dans un module :

#### ✅ Export inline (immédiat)

```meshr
export enum SensitivityLevel is (public, internal, restricted)
```

- La déclaration est rendue publique immédiatement.
- Facile à lire mais répétitif si plusieurs artefacts sont à exporter.

#### ✅ Export groupé (centralisé)

```meshr
export { PIICategory, SensitivityLevel }

enum PIICategory is (contact, identity, financial, health, biometric, location)
enum SensitivityLevel is (public, internal, restricted, confidential)
```

- Doit apparaître juste **après les imports**, jamais en fin de module.
- Permet de déclarer tous les artefacts exportés en un seul point.
- Aucune déclaration listée dans ce bloc n’a besoin du mot-clé `export` en ligne.

#### 🧠 Règles de priorité d’export

1. Une déclaration précédée de `export` est **immédiatement publique**.
2. Une déclaration listée dans `export { ... }` devient **publique à posteriori**.
3. Un même nom peut apparaître dans les deux formes (toléré).
4. Toute déclaration **non exportée explicitement** est **privée** au module.

- **Un fichier `.meshr` = un module unique**.
- Le `module` définit le **namespace** des artefacts qu’il contient.
- Les `import` permettent d'accéder à des symboles publics d'autres modules.
- Les annotations `@module_*` sont optionnelles mais encouragées pour documenter les modules.
- Les `import` permettent d'accéder à des symboles **explicitement exportés** d'autres modules.
- Les éléments d’un module **ne sont pas visibles depuis l’extérieur** s’ils ne sont pas précédés du mot-clé `export`.
- L’import de `{ * }` signifie **importer tous les symboles exportés** du module cible.
- L’import de `{ A, B }` permet une **importation sélective**.
- Les accolades `{}` sont **optionnelles uniquement si un seul identifiant** est importé.
- Si plusieurs identifiants sont importés d’un même module, l’usage des accolades est **obligatoire**.

### 📁 Convention d’arborescence

Par convention (non obligatoire), l’arborescence des fichiers reflète les noms qualifiés des modules :

| Module                    | Fichier                                    |
|---------------------------|---------------------------------------------|
| `core.types`             | `modules/core/types.meshr`                  |
| `marketing.analytics`    | `modules/marketing/analytics.meshr`         |

---

### 🧩 [2025-09-09] — Module = unité, namespace et fichier unique

- **Contexte :** Il fallait décider si l’on autorisait plusieurs modules par fichier, et s’il y avait un lien fort avec l’arborescence.
- **Décision :** Le langage impose qu’un fichier `.meshr` déclare **un seul module**. Le nom du module est un **namespace**. L’arborescence n’est **pas contrainte**, mais une convention est proposée.
- **Pourquoi :** Cela permet une résolution simple par les outils (CLI, LSP), évite les collisions de symboles, et reste lisible.

---

## 🧱 Artefacts définissables

### 1. `domain`

Déclaration d’un domaine hiérarchique.

```meshr
domain retail.marketing {
  description = "Marketing domain for the retail perimeter"
}
```

### 2. `product`

Déclaration d’un produit de données.

```meshr
product leads_b2c_import {
  domain = retail.marketing
  contracts = [
    contract:marketing:leads_b2c_import:1.0.0
  ]
}
```

### 3. `contract`

(Défini dans une autre couche ou généré via DCDL)

### 4. `aspect`

(TBD)

### 5. `team`

(TBD)

### 6. `policy`

(TBD)

---

## 📘 Décisions de conception

### 🧩 [2025-09-09] — Syntaxe déclarative avec blocs `{}`

- **Contexte :** Le langage doit rester simple, lisible pour les métiers, mais formalisable en grammaire ANTLR.
- **Décision :** Utiliser une syntaxe à blocs (`{}`), proche de HCL/Terraform.
- **Pourquoi :** Meilleure lisibilité et extensibilité que YAML/JSON, tout en étant facilement parsable.

### 🧩 [2025-09-10] — Visibilité par export explicite

- **Contexte :** Le langage devait gérer la visibilité entre modules pour encourager l'encapsulation.
- **Décision :** Un artefact déclaré dans un module n’est accessible depuis l’extérieur que s’il est précédé du mot-clé `export`.
- **Pourquoi :** Cette règle encourage une séparation claire entre API publique et éléments internes, facilite la documentation automatique et le linting.

### 🧩 [2025-09-10] — Deux formes d’export : inline ou groupé

- **Contexte :** Besoin de contrôler la visibilité des artefacts à l’extérieur du module.
- **Décision :** Deux formes sont supportées : inline (`export decl`) et groupée (`export { A, B }`).
- **Justification :** Favorise à la fois la lisibilité locale (inline) et la gestion explicite de l’API publique (groupé après les imports).

---

## 🚧 À venir

- Structuration des aspects (inline vs référence)
- Système de types
- Imports / Références croisées
- Mécanisme de validation
- Export YAML (DCDL, AML, Rego)
