# 🧷 Sauvegarde d’état — Meshr-Lang

## 📅 Date
2025-09-09

## ✅ Avancement

- [x] Définition des instructions du projet ChatGPT
- [x] Génération de la structure initiale de documentation Markdown
- [x] Spécification des artefacts `domain` et `product` (version MVP)
- [ ] Grammaire ANTLR (`MeshrLangParser.g4`)
- [ ] CLI `meshr` (parse, lint)
- [ ] Language Server (diagnostics, coloration)
- [ ] Export vers DCDL, AML, Rego

## 💡 Décisions prises

| Date       | Sujet                     | Décision                                                                 |
|------------|---------------------------|--------------------------------------------------------------------------|
| 2025-09-09 | Style syntaxique          | Syntaxe à blocs `{}` type HCL/Kotlin DSL                                 |
| 2025-09-09 | Documentation intégrée    | Format Markdown, avec contexte + décision + justification                |
| 2025-09-09 | Sauvegarde dans ChatGPT   | Ajout d'un template markdown dédié à utiliser régulièrement              |

## 🧠 Prochaines étapes

- Définir la grammaire ANTLR pour `domain` et `product`
- Générer des exemples `.ms`
- Initier le CLI `meshr` en mode `parse` + `ast`
