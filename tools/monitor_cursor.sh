#!/bin/bash

# Script de monitoring mémoire pour Cursor sous macOS
# Usage: ./monitor_cursor.sh

echo "🖥️  Monitoring mémoire Cursor - macOS"
echo "======================================"

# Fonction pour formater les tailles
format_size() {
    local size=$1
    if [ $size -gt 1073741824 ]; then
        echo "$(echo "scale=2; $size/1073741824" | bc) GB"
    elif [ $size -gt 1048576 ]; then
        echo "$(echo "scale=2; $size/1048576" | bc) MB"
    else
        echo "$(echo "scale=2; $size/1024" | bc) KB"
    fi
}

# Mémoire système globale
echo "💾 Mémoire système :"
vm_stat | head -n 5

echo ""
echo "🎯 Processus Cursor :"

# Trouver tous les processus Cursor
cursor_pids=$(pgrep -f -i cursor)

if [ -z "$cursor_pids" ]; then
    echo "❌ Aucun processus Cursor trouvé"
    exit 1
fi

total_memory=0

for pid in $cursor_pids; do
    if ps -p $pid > /dev/null 2>&1; then
        process_info=$(ps -p $pid -o pid,ppid,rss,vsz,pcpu,command | tail -n 1)
        rss=$(echo $process_info | awk '{print $3}')
        rss_bytes=$((rss * 1024))
        total_memory=$((total_memory + rss_bytes))
        
        echo "PID: $pid | RAM: $(format_size $rss_bytes) | $(echo $process_info | awk '{print $6}')"
    fi
done

echo ""
echo "📊 Total mémoire Cursor: $(format_size $total_memory)"

# Vérifier les extensions LSP
echo ""
echo "🔌 Processus LSP actifs :"
pgrep -f -l "lsp\|language.*server" | grep -v grep

# Recommandations
echo ""
echo "💡 Recommandations :"

# Si plus de 2GB utilisés
if [ $total_memory -gt 2147483648 ]; then
    echo "⚠️  Utilisation mémoire élevée (>2GB)"
    echo "   • Redémarrer Cursor : Cmd+Shift+P → 'Developer: Reload Window'"
    echo "   • Fermer les onglets inutiles"
    echo "   • Désactiver les extensions non essentielles"
fi

# Vérifier le swap
swap_used=$(sysctl vm.swapusage | grep -o "used = [0-9.]*[MG]" | cut -d' ' -f3)
if [[ $swap_used =~ G ]]; then
    echo "⚠️  Swap utilisé: $swap_used - Considérez redémarrer"
fi

echo ""
echo "🔄 Pour libérer la mémoire :"
echo "   sudo purge                    # Vider les caches"
echo "   sudo memory_pressure -S -l critical  # Forcer le nettoyage"
