# 🏢 Projet HR-Recrutement

## 🎯 Vue d'ensemble

Exemple complet d'implémentation Meshr-Lang pour le **domaine RH - Sous-domaine Recrutement**. 

Ce projet démontre l'utilisation exhaustive de toutes les fonctionnalités de Meshr-Lang :
- **🏷️ Annotations** : Versioning, documentation, criticité métier
- **🎯 Aspects** : Gouvernance, sécurité, qualité des données
- **🎭 Traits** : Réutilisabilité et composition
- **🏛️ Entités** : Modélisation des concepts métier
- **🔗 Relations** : Relations typées et bidirectionnelles
- **📊 Métriques** : KPIs et tableaux de bord (syntaxe étendue)

## 🏗️ Architecture

### 📦 Modules

```
hr-recrutement/
├── referentiels/          # Référentiels d'entreprise
│   ├── organisation.meshr # BU, départements, équipes
│   ├── locaux.meshr       # Sites, bureaux, espaces
│   └── profils.meshr      # Compétences, certifications
├── recrutement/           # Domaine recrutement
│   ├── candidats.meshr    # Candidats et profils
│   ├── postes.meshr       # Postes et exigences
│   └── processus.meshr    # Processus et évaluations
└── metrics/               # Métriques et KPIs
    └── recrutement-metrics.meshr
```

### 🎯 Concepts modélisés

#### 🏢 **Référentiels (Foundation)**
- **Organisation** : BusinessUnit, Department, Team, CostCenter
- **Locaux** : Site, Building, Office, WorkSpace
- **Profils** : Skill, SkillCategory, Certification

#### 👥 **Recrutement (Core Domain)**
- **Candidats** : Candidate, CandidateProfile, CandidateSkill
- **Postes** : JobPosting, JobRequirement, JobLocation
- **Processus** : Application, Interview, Evaluation, Offer

#### 📊 **Métriques (Analytics)**
- **Performance** : TimeToHire, CostPerHire, SourceEffectiveness
- **Qualité** : InterviewConversionRate, OfferAcceptanceRate
- **Expérience** : CandidateExperience, RecruiterProductivity

## 🎨 Fonctionnalités démontrées

### 🏷️ **Annotations avancées**
```meshr
@Version("1.0.0")
@Author(name="HR Analytics Team", email="hr.analytics@company.com")
@BusinessCritical(impact="high", stakeholders=["hr_director", "ceo"])
@Experimental(reason="Nouvelle métrique d'expérience candidat en test")
```

### 🎯 **Aspects multiples**
```meshr
aspects {
  DataClassification { level: "confidential", encryption_required: true },
  DataStewardship { steward: "recruitment@company.com", business_domain: "recruitment" },
  MetricGovernance { business_criticality: "high", refresh_frequency: Interval 1 day }
}
```

### 🎭 **Traits composables**
```meshr
trait WithCandidateInfo is
  first_name : String length 1..50
  email : String pattern "^[^@]+@[^@]+$"
  notice_period : Interval
end

entity Candidate with WithSecurity, WithGDPR, WithCandidateInfo, WithEducationInfo is
  // Hérite de tous les champs des traits
end
```

### 🎨 **Enums optimisés** (syntaxe mixte)
```meshr
// Flexibilité identifiants + chaînes pour lisibilité métier
enum ApplicationStatus is (
  submitted,                    // Identifiant simple
  "under review",              // Chaîne avec espace
  "screening passed",          // Espace au lieu d'underscore
  interviewing,                // Identifiant simple
  hired,                       // Identifiant simple
  "offer extended"             // Chaîne avec espace
)

// Référence uniforme avec notation pointée
filters {
  application_status == ApplicationStatus.hired,           // Identifiant
  interview_status == InterviewStatus."in progress"       // Chaîne
}
```

### 🔗 **Relations complexes**
```meshr
// Relation typée
relation RecruitmentPipeline of type RECRUITMENT_PROCESS is
  from Application(application_id) to Application(application_id)
  
// Relation bidirectionnelle  
bidirectional relation OrganizationalHierarchy is
  from Department(parent_id) to Department(department_id)
```

### 📊 **Métriques avec nouvelle syntaxe**
```meshr
metric TimeToHire is
  source Application                    // ← Mot-clé source
  calculation avg(offer_date - application_date)  // ← Mot-clé calculation
  unit "days"                          // ← Mot-clé unit
  
  outputs {                            // ← Bloc outputs
    average_days : Float,
    sample_size : Integer
  }
  
  dimensions {                         // ← Bloc dimensions
    department from related(JobPosting, job_id).department_id
  }
  
  aspects {                           // ← Gouvernance via aspects
    MetricGovernance { business_criticality: "high" }
  }
end
```

## 🎯 Points clés démontrés

### ✅ **Séparation claire Traits vs Aspects**
- **Traits** : Propriétés métier du CSM (`WithCandidateInfo`, `WithJobInfo`)
- **Aspects** : Métadonnées de gouvernance (`DataClassification`, `MetricGovernance`)

### ✅ **Métriques sans ambiguïté syntaxique**
- **Mots-clés dédiés** : `source`, `calculation`, `unit`
- **Blocs structurés** : `dimensions`, `filters`, `temporal`, `aspects`
- **Outputs typés** : Résultats calculés comme champs

### ✅ **Réutilisabilité maximale**
- **Référentiels partagés** : Organisation, locaux, profils
- **Traits composables** : Combinaison flexible
- **Relations typées** : Réutilisation des patterns

### ✅ **Optimisations appliquées**
- **25+ enums optimisés** dans 6 fichiers
- **Underscores → espaces** : `"technical_skills"` → `"technical skills"`
- **Chaînes → identifiants** : `"draft"` → `draft` (quand approprié)
- **Lisibilité métier maximale** : Valeurs naturelles vs techniques

## 🚀 Utilisation

```bash
# Tester le parsing
PYTHONPATH=. python3 tests/parse_module.py examples/hr-recrutement-project/src/referentiels/organisation.meshr

# Valider la cohérence
meshr validate examples/hr-recrutement-project/

# Générer la documentation
meshr docs examples/hr-recrutement-project/
```

---

**Ce projet illustre parfaitement la puissance de Meshr-Lang** pour modéliser des domaines métier complexes avec gouvernance complète ! 🌟
