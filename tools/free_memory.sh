#!/bin/bash

echo "🧹 Libération de la mémoire système macOS"
echo "========================================"

echo "💾 État mémoire AVANT :"
vm_stat | head -5

echo ""
echo "🧹 Nettoyage en cours..."

# Purger les caches système
echo "   - Purge des caches système..."
sudo purge

# Forcer le nettoyage mémoire
echo "   - Pression mémoire critique..."
sudo memory_pressure -S -l critical

# Attendre un peu
sleep 2

echo ""
echo "💾 État mémoire APRÈS :"
vm_stat | head -5

echo ""
echo "🎯 Processus Cursor :"
ps aux | grep -i "Cursor" | grep -v "grep" | awk '{print "PID: " $2 " | RAM: " $6/1024 " MB | " $11}'

echo ""
echo "✅ Nettoyage terminé ! Vous pouvez maintenant tester le serveur LSP."
