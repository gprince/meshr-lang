#!/bin/bash

# Script d'installation de l'extension Meshr-Lang pour VSCode/Cursor

echo "🔌 Installation de l'extension Meshr-Lang"
echo "========================================"

# Vérifier si code (VSCode CLI) est disponible
if command -v code &> /dev/null; then
    echo "📦 Installation dans VSCode..."
    code --install-extension meshr-lang-0.1.0.vsix
    echo "✅ Extension installée dans VSCode"
else
    echo "⚠️  VSCode CLI (code) non trouvé"
fi

# Vérifier si cursor CLI est disponible
if command -v cursor &> /dev/null; then
    echo "📦 Installation dans Cursor..."
    cursor --install-extension meshr-lang-0.1.0.vsix
    echo "✅ Extension installée dans Cursor"
else
    echo "⚠️  Cursor CLI non trouvé"
fi

echo ""
echo "🎉 Installation terminée !"
echo ""
echo "📋 Instructions d'utilisation :"
echo "1. Redémarrez VSCode/Cursor"
echo "2. Ouvrez un fichier .meshr"
echo "3. L'extension devrait s'activer automatiquement"
echo ""
echo "🔧 Si l'extension ne fonctionne pas :"
echo "- Vérifiez que le serveur LSP Python est installé"
echo "- Vérifiez les logs dans la sortie de l'extension"
echo "- Utilisez la commande 'Meshr-Lang: Redémarrer le serveur LSP'"
