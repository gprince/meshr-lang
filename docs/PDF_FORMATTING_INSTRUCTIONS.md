# Instructions de mise en page PDF - Meshr-Lang Documentation

> **Fichier de référence pour la génération automatique du PDF professionnel**  
> **Créé :** 2025-09-18  
> **Version :** 1.0.0

## 🎯 Objectifs de mise en page

### ✅ Exigences de structure
1. **Page de garde séparée** : Logo, titre, version, métadonnées
2. **Table des matières dédiée** : Page séparée après la page de garde
3. **Chapitres bien structurés** : Numérotation claire et hiérarchie logique
4. **Sauts de page appropriés** : Entre chapitres majeurs

### ✅ Style visuel requis
- **Logo** : Utiliser `assets/meshr-lang-color.png` (400px de largeur)
- **Taille de police page de garde** : Grande et lisible
- **Style de titre chapitre** : 
  - Numéro de chapitre en grand sur une ligne
  - Titre du chapitre juste en dessous
- **Police système** : Arial/Helvetica pour compatibilité maximale

## 🏗️ Structure des chapitres

### Restructuration requise (v0.2.0)
```
Ancien format → Nouveau format
=====================================
## 🎯 Introduction → # 1. Introduction
### 🧭 Contexte...  → ## Contexte et motivation
### 🎨 Philosophie → ## Philosophie du langage

## 📑 Table des matières → SUPPRIMÉ (généré automatiquement)

## 🧭 Objectif du langage → # 2. Objectif du langage
### 🎯 Vision...    → ## Vision et philosophie
### 🧠 Rationnel   → ## Rationnel du langage

## 🔤 Syntaxe de base → # 3. Syntaxe de base
### 📄 Structure    → ## Structure des fichiers
### 🎨 Style        → ## Style déclaratif

Et ainsi de suite pour tous les ## → #
```

### Règles de conversion
- **Niveau 2 (##)** → **Niveau 1 (#)** = Chapitres
- **Niveau 3 (###)** → **Niveau 2 (##)** = Sections
- **Niveau 4 (####)** → **Niveau 3 (###)** = Sous-sections

## 📄 Template de page de garde

```markdown
---
title: "Meshr-Lang"
subtitle: "Documentation du langage"
author: "G. Prince - Architecte Principal"
date: "Version 0.2.0 - Septembre 2025"
---

![Logo Meshr-Lang](assets/meshr-lang-color.png){ width=400px }

# Meshr-Lang
## Documentation du langage

**Version 0.2.0 - Septembre 2025**

*Avec support complet des métriques et pattern matching*

---

**G. Prince - Architecte Principal**  
2025-09-18

\newpage
```

## 🛠️ Commande Pandoc optimisée

```bash
pandoc docs/cover-page.md docs/meshr-lang-pdf.md \
  -o docs/meshr-lang.pdf \
  --pdf-engine=xelatex \
  --variable=mainfont="Arial" \
  --variable=sansfont="Arial" \
  --variable=monofont="Courier New" \
  --variable=geometry:"margin=2.5cm" \
  --variable=fontsize:"11pt" \
  --variable=linestretch:"1.2" \
  --toc \
  --toc-depth=3 \
  --number-sections \
  --highlight-style=github \
  --template=eisvogel \
  --listings
```

## 🎨 Styles de titre personnalisés

### Chapitre (Niveau 1)
```latex
% Style souhaité :
% 1
% Introduction
%
% Avec numéro en grand et titre en dessous
```

### Section (Niveau 2)
```latex
% Style standard avec numérotation automatique
% 1.1 Contexte et motivation
```

## 🔧 Processus de génération

### Étapes automatisées
1. **Préparation** : Créer `cover-page.md` et `meshr-lang-pdf.md`
2. **Nettoyage** : Supprimer emojis et table des matières manuelle
3. **Restructuration** : Convertir ## → # selon les règles
4. **Sauts de page** : Ajouter `\newpage` avant chaque chapitre
5. **Génération** : Exécuter commande Pandoc
6. **Nettoyage** : Supprimer fichiers temporaires

### Fichiers temporaires
- `docs/cover-page.md` : Page de garde avec logo
- `docs/meshr-lang-pdf.md` : Contenu optimisé PDF
- `docs/meshr-lang.pdf` : Résultat final

## ✅ Checklist de validation

### Page de garde
- [ ] Logo Meshr-Lang visible et centré
- [ ] Titre principal en grande taille
- [ ] Version et date correctes
- [ ] Métadonnées auteur présentes
- [ ] Pas de table des matières sur cette page

### Table des matières
- [ ] Page dédiée après la page de garde
- [ ] Numérotation automatique
- [ ] Profondeur limitée à 3 niveaux
- [ ] Liens cliquables (si PDF interactif)

### Structure des chapitres
- [ ] Chapitres commencent par numéro en grand
- [ ] Titre de chapitre en dessous
- [ ] Saut de page avant chaque chapitre
- [ ] Hiérarchie cohérente (1, 1.1, 1.1.1)

### Contenu
- [ ] Emojis supprimés du PDF
- [ ] Code syntax highlighting
- [ ] Images et diagrammes correctement intégrés
- [ ] Liens et références fonctionnels

## 🔄 Maintenance

### Mise à jour de version
1. Modifier `version` dans les métadonnées
2. Mettre à jour `date` de génération
3. Vérifier que tous les nouveaux chapitres suivent les règles
4. Régénérer le PDF avec ces instructions

### Ajout de contenu
- Respecter la hiérarchie ## → # pour nouveaux chapitres
- Ajouter `\newpage` avant les chapitres majeurs
- Tester la génération PDF après modifications importantes

---

> **Note** : Ce fichier doit être consulté à chaque génération de PDF pour assurer la cohérence et la qualité professionnelle du document.
