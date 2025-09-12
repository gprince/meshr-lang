# Changelog

Toutes les modifications notables de la bibliothèque standard Meshr-Lang seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-12

### Ajouté
- **Module `meshr.security`** : Aspects et types pour la sécurité des données
  - `DataClassification` : Classification des données (public, internal, confidential, restricted)
  - `GDPRCompliance` : Conformité GDPR avec droits des personnes et bases légales
  - `SecurityControls` : Contrôles de sécurité (chiffrement, audit, logging)
  - `WithSecurity` et `WithGDPR` : Traits pour l'injection de sécurité
  - `ACCESS_CONTROL` et `DATA_SHARING` : Types de relations de sécurité

- **Module `meshr.governance`** : Gouvernance et qualité des données
  - `DataStewardship` : Gestion des stewards et propriétaires de données
  - `DataQuality` : Métriques et règles de qualité des données
  - `DataLineage` : Traçabilité et lignage des données
  - `WithStewardship` et `WithQuality` : Traits pour la gouvernance
  - `DATA_OWNERSHIP` et `QUALITY_REVIEW` : Types de relations de gouvernance

- **Module `meshr.lifecycle`** : Cycle de vie et versioning des données
  - `DataLifecycle` : Gestion du cycle de vie des données
  - `VersionControl` : Contrôle de version et release notes
  - `WithLifecycle` et `WithVersioning` : Traits pour le cycle de vie
  - `VERSION_TRANSITION` et `STATUS_CHANGE` : Types de relations de cycle de vie

- **Exemples d'utilisation** : Fichiers de démonstration
  - `examples/simple-customer.meshr` : Entité Customer simple
  - `examples/customer-entity.meshr` : Entité Customer avec gouvernance complète
  - `examples/simple-imports.meshr` : Démonstration des imports simples et groupés
  - `examples/imports-demo.meshr` : Démonstration complète de tous les types d'imports
  - `examples/annotations-usage.meshr` : Utilisation des annotations communes
  - `examples/meta-annotations.meshr` : Création d'annotations personnalisées

- **Outils de test** : Scripts de validation
  - `test_stdlib.py` : Script de test automatisé pour tous les modules
  - Intégration avec le Makefile (`make test-stdlib`)

- **Documentation** : Documentation complète
  - `README.md` : Guide d'utilisation et structure
  - `CHANGELOG.md` : Historique des modifications
  - `IMPORTS.md` : Guide complet des imports
  - `ANNOTATIONS.md` : Guide complet des annotations
  - `pyproject.toml` : Configuration du package Python

### Technique
- Tous les modules sont syntaxiquement valides avec le parser Meshr-Lang
- Structure modulaire organisée en dossiers thématiques
- Exports groupés pour faciliter l'importation
- **Support complet des imports** : simple, groupé et wildcard
- **Support complet des annotations** : méta-annotations et annotations communes
- Conventions de nommage cohérentes
- Support des aspects, traits, entités et relations
- Exemples fonctionnels démontrant l'utilisation des imports et annotations

### Roadmap
- [ ] **Phase 1** : Modules `security` et `governance` ✅
- [ ] **Phase 2** : Modules `business` et `lifecycle` ✅
- [ ] **Phase 3** : Module `analytics` et intégrations
- [ ] **Phase 4** : Outils de validation et génération
- [ ] **Phase 5** : Documentation et exemples avancés
