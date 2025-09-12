# Guide d'utilisation de l'extension Meshr-Lang

## 🎉 Installation réussie !

L'extension Meshr-Lang a été installée avec succès dans Cursor. Vous pouvez maintenant utiliser toutes les fonctionnalités du LSP.

## 🚀 Fonctionnalités disponibles

### ✅ Coloration syntaxique
- Mots-clés : `module`, `entity`, `enum`, `trait`, `aspect`, `relation`
- Types : `String`, `Number`, `Boolean`, `List`, `Map`, `Bytes`
- Annotations : `@Documented`, `@Deprecated`, etc.
- Commentaires : `//` et `/* */`

### ✅ Autocomplétion intelligente
- **Mots-clés** : Tapez `mod` → suggestions pour `module`
- **Types** : Tapez `Str` → suggestions pour `String`
- **Annotations** : Tapez `@` → liste des annotations disponibles
- **Imports** : Tapez `import ` → suggestions des modules stdlib
- **Noms d'entités** : Suggestions contextuelles

### ✅ Snippets de code
- `module` → Template de déclaration de module
- `entity` → Template d'entité avec champs
- `enum` → Template d'énumération
- `trait` → Template de trait
- `aspect` → Template d'aspect
- `bytes` → Littéral Bytes
- `json` → Littéral JSON
- `geo` → Littéral Geography

### ✅ Navigation et symboles
- **Outline** : Panneau des symboles (Ctrl+Shift+O)
- **Go to Symbol** : Recherche de symboles (Ctrl+T)
- **Workspace Symbol** : Recherche dans tout le workspace (Ctrl+Shift+O)

### ✅ Diagnostics en temps réel
- Validation syntaxique
- Détection d'erreurs
- Suggestions de correction

## 🧪 Test de l'extension

1. **Ouvrez le fichier** `test-extension.meshr` dans Cursor
2. **Vérifiez la coloration** : Les mots-clés devraient être colorés
3. **Testez l'autocomplétion** :
   - Tapez `@` → vous devriez voir des suggestions d'annotations
   - Tapez `mod` → vous devriez voir `module` suggéré
   - Tapez `import ` → vous devriez voir des modules stdlib
4. **Testez les snippets** :
   - Tapez `entity` puis Tab → template d'entité
   - Tapez `enum` puis Tab → template d'énumération

## 🔧 Commandes disponibles

- **Meshr-Lang: Redémarrer le serveur LSP** - Redémarre le serveur en cas de problème
- **Meshr-Lang: Afficher la sortie du serveur** - Affiche les logs du serveur LSP

## 🐛 Dépannage

### L'extension ne s'active pas
1. Vérifiez que vous ouvrez un fichier `.meshr`
2. Redémarrez Cursor
3. Vérifiez les logs de l'extension

### Pas d'autocomplétion
1. Vérifiez que le serveur LSP est actif (regardez la barre de statut)
2. Utilisez la commande "Redémarrer le serveur LSP"
3. Vérifiez que Python 3.12+ est installé

### Erreurs de parsing
1. Vérifiez que la grammaire ANTLR est générée : `make grammar`
2. Vérifiez les logs du serveur LSP

## 📚 Ressources

- **Documentation complète** : `docs/meshr-lang.md`
- **Exemples** : Dossier `examples/`
- **Tests** : `make lsp-test`

## 🎯 Prochaines étapes

L'extension est maintenant prête à être utilisée ! Vous pouvez :
1. Créer de nouveaux fichiers `.meshr`
2. Utiliser l'autocomplétion et les snippets
3. Naviguer dans vos modules avec les symboles
4. Bénéficier de la validation en temps réel

**Bon développement avec Meshr-Lang !** 🚀
