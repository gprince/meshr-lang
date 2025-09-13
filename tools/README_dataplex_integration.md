# 🔗 Intégration Meshr -> Dataplex Universal Catalog

Cette intégration permet de traduire les aspects Meshr en types d'aspects Dataplex Universal Catalog et de les pousser via l'API Google Cloud.

## 📋 Vue d'ensemble

L'intégration comprend trois composants principaux :

1. **Déclaration d'aspects Meshr** : Syntaxe Meshr pour définir des types d'aspects
2. **Traducteur** : Conversion Meshr -> JSON compatible Dataplex
3. **Client API** : Poussée vers l'API Dataplex Universal Catalog

## 🚀 Utilisation rapide

### 1. Déclarer un aspect Meshr

```meshr
@DataplexAspect(
    aspect_type_id="data-governance",
    display_name="Data Governance",
    description="Aspect pour la gouvernance des données",
    project_id="my-project",
    location="us-central1"
)
aspect DataGovernance is
    data_governor : String = "Nom du gouverneur des données"
    business_owner : String = "Propriétaire métier"
    data_classification : DataClassification = DataClassification.PUBLIC
    approved_by_governance : Boolean = false
    date_of_governance_approval : Datetime = Datetime"2025-01-01T00:00:00Z"
end

enum DataClassification is (
    PUBLIC,
    SENSITIVE,
    CONFIDENTIAL
)
```

### 2. Traduire vers JSON

```bash
python tools/meshr_to_dataplex.py
```

### 3. Pousser vers Dataplex

```bash
# Configuration de l'authentification
gcloud auth application-default login

# Poussée vers Dataplex
python tools/push_to_dataplex.py dataplex-data-governance.json \
    --project-id YOUR_PROJECT_ID \
    --location us-central1
```

## 📁 Fichiers de l'intégration

### Fichiers principaux

- **`examples/dataplex-data-governance.meshr`** : Exemple d'aspect Data Governance
- **`tools/meshr_to_dataplex.py`** : Traducteur Meshr -> JSON
- **`tools/push_to_dataplex.py`** : Client API Dataplex
- **`tools/demo_dataplex_integration.py`** : Démonstration complète

### Fichiers générés

- **`dataplex-data-governance.json`** : Aspects traduits en JSON
- **`dataplex-data-governance.json`** : Appels API générés

## 🔧 Configuration

### Prérequis

1. **Python 3.7+** avec les packages :
   ```bash
   pip install requests google-auth google-auth-oauthlib
   ```

2. **Google Cloud SDK** :
   ```bash
   gcloud auth application-default login
   ```

3. **Permissions Dataplex** :
   - `dataplex.aspectTypes.create`
   - `dataplex.aspectTypes.update`
   - `dataplex.aspectTypes.get`

### Variables d'environnement

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

## 📚 API Reference

### Annotations Meshr

#### `@DataplexAspect`

Configuration pour la création d'un aspect type dans Dataplex.

```meshr
@DataplexAspect(
    aspect_type_id="string",           // ID unique de l'aspect
    display_name="string",             // Nom d'affichage
    description="string",              // Description
    project_id="string",               // ID du projet GCP
    location="string",                 // Localisation (us-central1, etc.)
    labels=Map{"key": "value"}         // Labels optionnels
)
```

#### `@DataplexEnum`

Configuration pour la création d'un enum dans Dataplex.

```meshr
@DataplexEnum(
    enum_type="string",                // Type de l'enum
    description="string"               // Description
)
```

### Types supportés

| Type Meshr | Type Dataplex | Description |
|------------|---------------|-------------|
| `String` | `string` | Chaîne de caractères |
| `Integer` | `int` | Nombre entier |
| `Float` | `double` | Nombre décimal |
| `Boolean` | `bool` | Booléen |
| `Datetime` | `datetime` | Date et heure (RFC3339) |
| `Date` | `datetime` | Date (RFC3339) |
| `Time` | `datetime` | Heure (RFC3339) |
| `Timestamp` | `datetime` | Timestamp (RFC3339) |
| `Json` | `string` | JSON sérialisé |
| `Bytes` | `string` | Données binaires (base64) |
| `Geography` | `string` | Géographie (WKT/GeoJSON) |
| `Sql` | `string` | Requête SQL |
| `Interval` | `string` | Intervalle temporel |

## 🛠️ Scripts disponibles

### `meshr_to_dataplex.py`

Traduit les fichiers Meshr en JSON compatible Dataplex.

```bash
python tools/meshr_to_dataplex.py
```

**Options :**
- `--input` : Fichier Meshr d'entrée (défaut: `examples/dataplex-data-governance.meshr`)
- `--output` : Fichier JSON de sortie (défaut: `dataplex-data-governance.json`)

### `push_to_dataplex.py`

Pousse les aspects vers l'API Dataplex Universal Catalog.

```bash
python tools/push_to_dataplex.py <json_file> --project-id <project_id>
```

**Options :**
- `--project-id` : ID du projet Google Cloud (requis)
- `--location` : Localisation (défaut: `us-central1`)
- `--credentials` : Chemin vers le fichier de credentials JSON
- `--dry-run` : Simulation sans exécution réelle
- `--update` : Mettre à jour les aspects existants
- `--list` : Lister les aspects existants

### `demo_dataplex_integration.py`

Démonstration complète de l'intégration.

```bash
python tools/demo_dataplex_integration.py
```

## 📊 Exemple complet

### 1. Fichier Meshr

```meshr
@DataplexAspect(
    aspect_type_id="data-quality",
    display_name="Data Quality",
    description="Métriques de qualité des données",
    project_id="my-project",
    location="us-central1"
)
aspect DataQuality is
    completeness_score : Float = 0.0
    accuracy_score : Float = 0.0
    consistency_score : Float = 0.0
    freshness_score : Float = 0.0
    last_validation_date : Datetime = Datetime"2025-01-01T00:00:00Z"
    validation_rules : List of String = List[]
    quality_status : QualityStatus = QualityStatus.UNKNOWN
end

enum QualityStatus is (
    EXCELLENT,
    GOOD,
    FAIR,
    POOR,
    UNKNOWN
)
```

### 2. JSON généré

```json
{
  "aspect_types": [
    {
      "aspect_type_id": "data-quality",
      "display_name": "Data Quality",
      "description": "Métriques de qualité des données",
      "project_id": "my-project",
      "location": "us-central1",
      "fields": [
        {
          "name": "completeness_score",
          "type": "double",
          "description": "Score de complétude",
          "required": false
        },
        {
          "name": "quality_status",
          "type": "enum",
          "description": "Statut de qualité",
          "required": false,
          "enum_values": ["EXCELLENT", "GOOD", "FAIR", "POOR", "UNKNOWN"]
        }
      ]
    }
  ]
}
```

### 3. Appel API Dataplex

```json
{
  "method": "POST",
  "url": "https://dataplex.googleapis.com/v1/projects/my-project/locations/us-central1/aspectTypes",
  "body": {
    "aspectTypeId": "data-quality",
    "displayName": "Data Quality",
    "description": "Métriques de qualité des données",
    "metadataTemplate": {
      "recordFields": [
        {
          "index": 1,
          "name": "completeness_score",
          "type": "double",
          "constraints": {"required": false}
        },
        {
          "index": 2,
          "name": "quality_status",
          "type": "enum",
          "constraints": {"required": false},
          "enumValues": [
            {"index": 1, "name": "EXCELLENT"},
            {"index": 2, "name": "GOOD"},
            {"index": 3, "name": "FAIR"},
            {"index": 4, "name": "POOR"},
            {"index": 5, "name": "UNKNOWN"}
          ]
        }
      ]
    }
  }
}
```

## 🔍 Dépannage

### Erreurs courantes

1. **Authentification échouée** :
   ```bash
   gcloud auth application-default login
   ```

2. **Permissions insuffisantes** :
   - Vérifier les rôles IAM Dataplex
   - Ajouter le rôle `Dataplex Admin`

3. **Aspect déjà existant** :
   ```bash
   python tools/push_to_dataplex.py file.json --project-id project --update
   ```

4. **Format JSON invalide** :
   - Vérifier la syntaxe Meshr
   - Valider avec le parser ANTLR

### Logs et débogage

```bash
# Mode verbose
python tools/push_to_dataplex.py file.json --project-id project --dry-run

# Vérifier les aspects existants
python tools/push_to_dataplex.py file.json --project-id project --list
```

## 🚀 Prochaines étapes

1. **Intégrations supplémentaires** :
   - DataHub
   - OpenMetadata
   - Apache Atlas

2. **Améliorations** :
   - Interface utilisateur web
   - Validation avancée
   - Gestion des erreurs
   - Tests automatisés

3. **Fonctionnalités** :
   - Synchronisation bidirectionnelle
   - Templates d'aspects
   - Gestion des versions
   - Métadonnées enrichies

## 📞 Support

Pour toute question ou problème :

1. **Documentation** : Consulter ce README
2. **Issues** : Créer une issue sur le repository
3. **Discussions** : Utiliser les discussions GitHub

---

*Intégration développée pour Meshr-lang - 2024*
