# 📚 Exemples pratiques Meshr-Lang

Ce dossier contient des exemples concrets d'utilisation du langage Meshr-Lang dans différents contextes métier et techniques.

## 🎯 Objectif

Ces exemples démontrent les capacités du langage Meshr-Lang pour :
- **Modéliser des domaines métier** complexes
- **Implémenter la gouvernance** des données
- **Assurer la conformité** réglementaire
- **Gérer les relations** entre entités
- **Utiliser les traits et aspects** efficacement

## 📁 Exemples disponibles

### 🛒 E-commerce
- **`ecommerce-products.meshr`** : Gestion du catalogue produits
  - Entités : `Product`, `ProductCategory`
  - Traits : `WithPricing`, `WithInventory`
  - Relations : Hiérarchie des catégories

- **`ecommerce-orders.meshr`** : Gestion des commandes
  - Entités : `Customer`, `Order`, `OrderItem`
  - Conformité : GDPR, aspects de sécurité
  - Relations : Commandes clients, références produits

### 🏢 Ressources Humaines
- **`hr-employees.meshr`** : Gestion des employés
  - Entités : `Employee`, `Department`, `Position`
  - Traits : `WithPersonalInfo`, `WithEmploymentInfo`

- **`hr-recrutement-project/`** : Projet complet de gestion de recrutement ⭐
  - **Architecture modulaire** : `src/referentiels/`, `src/recrutement/`, `src/metrics/`
  - **Entités** : `Candidate`, `JobPosting`, `Application`, `Interview`
  - **Métriques avancées** : `TimeToHire`, `CostPerHire`, `SourceEffectiveness`
  - **Pattern matching** : Dimensions conditionnelles avec `match...is...end`
  - **Enums optimisés** : Syntaxe mixte identifiants/chaînes
  - **Documentation professionnelle** : Mapping BigQuery/Dataplex automatisé

### 🏦 Secteur financier
- **`banking-accounts.meshr`** : Gestion des comptes bancaires
  - Entités : `Customer`, `Account`, `Transaction`
  - Conformité : KYC, AML, aspects de sécurité
  - Relations : Propriété des comptes, transactions

### 🔧 Intégration technique
- **`apis-management.meshr`** : Gestion des APIs et microservices
  - Entités : `API`, `Endpoint`, `Service`
  - Traits : `WithTechnicalInfo`, `WithMonitoring`
  - Relations : Services exposant des APIs

## 🚀 Utilisation

### Tester les exemples

```bash
# Tester tous les exemples
make test

# Tester un exemple spécifique
python tests/parse_module.py examples/ecommerce-products.meshr
```

### Importer dans vos modules

```meshr
// Import d'un module d'exemple
import { Product, ProductCategory } from ecommerce.products
import { Customer, Order } from ecommerce.orders

// Utilisation dans votre module
entity MyProduct with WithPricing is
  product_id : String
  name : String
  // ... autres champs
end
```

## 📋 Caractéristiques des exemples

### ✅ Bonnes pratiques démontrées
- **Annotations complètes** : `@Version`, `@Author`, `@Documented`
- **Imports structurés** : Utilisation de la stdlib
- **Traits réutilisables** : Factorisation de comportements
- **Aspects de gouvernance** : `DataClassification`, `DataStewardship`
- **Relations complexes** : Modélisation des dépendances
- **Conformité** : GDPR, sécurité, audit

### 🎯 Domaines couverts
- **E-commerce** : Catalogue, commandes, clients
- **RH** : Employés, départements, positions
- **Finance** : Comptes, transactions, conformité
- **Technique** : APIs, services, monitoring

### 🔧 Fonctionnalités avancées
- **Énumérations métier** : Statuts, types, niveaux
- **Contraintes de validation** : Patterns, longueurs
- **Aspects multiples** : Sécurité, gouvernance, lifecycle
- **Relations bidirectionnelles** : Hiérarchies, références

## 📖 Documentation

Pour plus de détails sur la syntaxe et les concepts :
- Consultez la [documentation complète](../docs/meshr-lang.md)
- Explorez la [bibliothèque standard](../stdlib/)
- Testez avec les [fichiers de test](../tests/)

## 🤝 Contribution

Pour ajouter de nouveaux exemples :
1. Créez un fichier `.meshr` dans ce dossier
2. Suivez les conventions de nommage
3. Ajoutez les annotations requises
4. Testez avec `make test`
5. Mettez à jour ce README

---

*Ces exemples sont fournis à des fins éducatives et de démonstration. Adaptez-les selon vos besoins spécifiques.*
