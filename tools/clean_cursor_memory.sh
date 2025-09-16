#!/bin/bash

echo "🧹 Nettoyage complet de la mémoire Cursor"
echo "========================================"

echo "1. 🗑️ Suppression des caches Cursor..."
rm -rf "$HOME/Library/Application Support/Cursor/User/workspaceStorage/images/"
rm -rf "$HOME/Library/Application Support/Cursor/logs/"
rm -rf "$HOME/Library/Application Support/Cursor/CachedData/"

echo "2. 🧹 Nettoyage des caches TypeScript..."
rm -rf "$HOME/.cursor/extensions/*/node_modules/.cache/"
rm -rf "$HOME/Library/Caches/com.todesktop.230313mzl4w4u92/"

echo "3. 💾 État mémoire système AVANT nettoyage:"
vm_stat | head -5

echo "4. 🔄 Purge des caches système..."
if command -v purge >/dev/null 2>&1; then
    sudo purge 2>/dev/null || echo "   (purge nécessite sudo, ignoré)"
fi

echo "5. 🧹 Garbage collection forcé..."
python3 -c "import gc; gc.collect(); print('✅ Python GC terminé')" 2>/dev/null || echo "   (Python non disponible)"

echo "6. 💾 État mémoire système APRÈS nettoyage:"
vm_stat | head -5

echo ""
echo "7. 🎯 Processus Cursor restants :"
ps aux | grep -i "Cursor" | grep -v "grep" | wc -l | xargs echo "   Processus Cursor actifs:"

echo ""
echo "✅ Nettoyage terminé ! Redémarrez Cursor pour appliquer les changements."
