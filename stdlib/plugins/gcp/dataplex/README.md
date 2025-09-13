# 🔗 Plugin GCP Dataplex

Plugin officiel pour l'intégration avec Google Cloud Dataplex Universal Catalog.

## 📋 Vue d'ensemble

Ce plugin fournit les annotations, types et aspects nécessaires pour déclarer des métadonnées compatibles avec Dataplex Universal Catalog.

## 📁 Structure

```
stdlib/plugins/gcp/dataplex/
├── annotations.meshr    # Annotations Dataplex
├── types.meshr         # Types et enums
├── aspects.meshr       # Aspects prédéfinis
└── README.md          # Documentation
```

## 🚀 Utilisation

### Import du plugin

```meshr
import { DataplexAspect, DataGovernance } from stdlib.plugins.gcp.dataplex
```

### Déclaration d'un aspect

```meshr
@DataplexAspect(
    aspect_type_id="my-custom-aspect",
    display_name="My Custom Aspect",
    description="Description of my custom aspect"
)
aspect MyCustomAspect is
    field1 : String = "Description of field1"
    field2 : Integer = 42
    field3 : DataClassification = DataClassification.PUBLIC
end
```

### Utilisation dans une entité

```meshr
entity MyTable is
    table_name : String
    
    aspects {
        DataGovernance {
            data_governor: "John Smith",
            business_owner: "Jane Doe",
            data_classification: DataClassification.SENSITIVE,
            approved_by_governance: true,
            date_of_governance_approval: Datetime"2025-01-15T10:30:00Z",
            data_lifecycle: DataLifecycle.PRODUCTION,
            retention_date: Datetime"2030-12-31T23:59:59Z",
            delete_by_date: Datetime"2030-12-31T23:59:59Z",
            is_encrypted: true,
            has_pii: true
        }
    }
end
```

## 📚 Annotations disponibles

### `@DataplexAspect`

Déclare un type d'aspect compatible avec Dataplex.

**Paramètres :**
- `aspect_type_id` (requis) : Identifiant unique de l'aspect
- `display_name` (optionnel) : Nom d'affichage
- `description` (optionnel) : Description
- `labels` (optionnel) : Labels associés

### `@DataplexEnum`

Déclare un enum compatible avec Dataplex.

**Paramètres :**
- `enum_type` (requis) : Type de l'enum
- `description` (optionnel) : Description

### `@DataplexEntry`

Déclare une entrée compatible avec Dataplex.

**Paramètres :**
- `entry_id` (requis) : Identifiant de l'entrée
- `entry_type` (requis) : Type d'entrée
- `display_name` (optionnel) : Nom d'affichage
- `description` (optionnel) : Description
- `labels` (optionnel) : Labels associés

## 🎯 Types disponibles

### Enums prédéfinis

- **`DataClassification`** : PUBLIC, SENSITIVE, CONFIDENTIAL
- **`DataLifecycle`** : TEST, DEV, QA, PRODUCTION, OTHER, DEPRECATED
- **`DataQualityStatus`** : EXCELLENT, GOOD, FAIR, POOR, UNKNOWN
- **`EntryType`** : TABLE, VIEW, DATABASE, SCHEMA, COLUMN, FILE, DIRECTORY, DATASET, MODEL, JOB, PIPELINE
- **`GovernanceLevel`** : ENTERPRISE, DEPARTMENTAL, PROJECT, INDIVIDUAL

## 🏗️ Aspects prédéfinis

### `DataGovernance`

Aspect pour la gouvernance des données.

**Champs :**
- `data_governor` : Gouverneur des données
- `business_owner` : Propriétaire métier
- `data_classification` : Classification des données
- `approved_by_governance` : Approbation par la gouvernance
- `date_of_governance_approval` : Date d'approbation
- `data_lifecycle` : Cycle de vie des données
- `retention_date` : Date de rétention
- `delete_by_date` : Date de suppression
- `is_encrypted` : Chiffrement
- `has_pii` : Données personnelles

### `DataQuality`

Aspect pour la qualité des données.

**Champs :**
- `completeness_score` : Score de complétude
- `accuracy_score` : Score de précision
- `consistency_score` : Score de cohérence
- `freshness_score` : Score de fraîcheur
- `validity_score` : Score de validité
- `quality_status` : Statut de qualité
- `last_validation_date` : Dernière validation
- `next_validation_date` : Prochaine validation
- `validation_rules` : Règles de validation
- `validation_tool` : Outil de validation
- `validation_frequency` : Fréquence de validation

### `DataLineage`

Aspect pour la généalogie des données.

**Champs :**
- `source_systems` : Systèmes sources
- `source_tables` : Tables sources
- `transformation_logic` : Logique de transformation
- `transformation_tools` : Outils de transformation
- `target_systems` : Systèmes cibles
- `target_tables` : Tables cibles
- `lineage_last_updated` : Dernière mise à jour
- `lineage_tool` : Outil de généalogie
- `upstream_dependencies` : Dépendances amont
- `downstream_dependencies` : Dépendances aval

### `DataSecurity`

Aspect pour la sécurité des données.

**Champs :**
- `security_classification` : Classification de sécurité
- `access_control_policy` : Politique de contrôle d'accès
- `authorized_users` : Utilisateurs autorisés
- `authorized_roles` : Rôles autorisés
- `encryption_at_rest` : Chiffrement au repos
- `encryption_in_transit` : Chiffrement en transit
- `encryption_algorithm` : Algorithme de chiffrement
- `audit_enabled` : Audit activé
- `audit_retention_days` : Rétention d'audit
- `compliance_frameworks` : Cadres de conformité
- `data_retention_policy` : Politique de rétention
- `contains_pii` : Contient des données personnelles
- `contains_phi` : Contient des données de santé
- `contains_financial_data` : Contient des données financières

## 🔧 Intégration avec les outils

Ce plugin est conçu pour fonctionner avec les outils de traduction vers Dataplex :

- **`meshr_to_dataplex.py`** : Traduction vers JSON
- **`push_to_dataplex.py`** : Poussée vers l'API Dataplex

## 📝 Versioning

Toutes les déclarations utilisent l'annotation `@since` pour indiquer leur version :

```meshr
@since("1.0.0")
@id("data-governance-aspect")
@display_name("Data Governance")
aspect DataGovernance is
    // ...
end
```

## 🚀 Prochaines versions

### Version 1.1.0 (planifiée)
- Ajout d'aspects pour la conformité (GDPR, CCPA, etc.)
- Support des métadonnées techniques avancées
- Intégration avec Data Catalog

### Version 1.2.0 (planifiée)
- Support des workflows de gouvernance
- Intégration avec Cloud Data Loss Prevention
- Métadonnées de coût et d'utilisation

## 📞 Support

Pour toute question ou problème :

1. **Documentation** : Consulter ce README
2. **Issues** : Créer une issue sur le repository
3. **Discussions** : Utiliser les discussions GitHub

---

*Plugin développé pour Meshr-lang - Version 1.0.0*
