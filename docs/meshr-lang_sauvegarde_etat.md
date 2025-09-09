# 🧷 Sauvegarde d’état — Meshr-Lang

## 📅 Date
2025-09-09

## ✅ Avancement

- [x] Définition des instructions du projet ChatGPT
- [x] Génération de la structure initiale de documentation Markdown
- [x] Spécification des artefacts `domain` et `product` (version MVP)
- [x] Grammaire ANTLR (`MeshrModule.g4`) — avec support de `module`, `import`, `annotation`, `enum`
- [x] Makefile de tests (lancement des tests via `make test`)
- [x] Tests de parsing pour `module`, `import`, `enum`, `annotation` (✅ tous passent)
- [ ] Bloc `trait` (syntaxe définie, à implémenter dans la grammaire)
- [ ] Language Server (diagnostics, coloration, navigation)
- [ ] Export vers DCDL, AML, Rego

## 💡 Décisions prises

| Date       | Sujet                     | Décision                                                                 |
|------------|---------------------------|--------------------------------------------------------------------------|
| 2025-09-09 | Style syntaxique          | Syntaxe à blocs `{}` type HCL/Kotlin DSL                                 |
| 2025-09-09 | Documentation intégrée    | Format Markdown, avec contexte + décision + justification                |
| 2025-09-09 | Sauvegarde dans ChatGPT   | Ajout d'un template markdown dédié à utiliser régulièrement              |
| 2025-09-09 | Enum avec attributs       | Syntaxe Kotlin-like avec signature explicite obligatoire (pas d'inférence) |
| 2025-09-09 | Enum hexadecimaux         | Support des entiers hexadécimaux dans les valeurs d’enum                 |
| 2025-09-09 | Enum valeur avec attributs | Signature explicite obligatoire, pas d’inférence                        |

## 🧠 Prochaines étapes

- Finaliser la grammaire pour le bloc `trait`
- Ajouter les tests de parsing pour `trait` avec accès aux attributs d’enum
- Débuter le resolving des références (ex : `Severity.high.color`)
- Documenter l’ordre de résolution et la sémantique
- Initier le Language Server avec diagnostics de base
