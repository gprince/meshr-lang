#!/usr/bin/env python3
"""
Script de test pour la bibliothèque standard Meshr-Lang
Valide que tous les modules de la stdlib sont syntaxiquement corrects
"""

import os
import sys
import subprocess
from pathlib import Path

def test_meshr_file(file_path):
    """Teste un fichier .meshr avec le parser"""
    try:
        result = subprocess.run([
            sys.executable, 
            "tests/parse_module.py", 
            str(file_path)
        ], capture_output=True, text=True, cwd=Path(__file__).parent.parent)
        
        if result.returncode == 0:
            print(f"✅ {file_path}")
            return True
        else:
            print(f"❌ {file_path}")
            print(f"   Erreur: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {file_path}")
        print(f"   Exception: {e}")
        return False

def main():
    """Teste tous les fichiers .meshr de la stdlib"""
    stdlib_dir = Path(__file__).parent
    project_root = stdlib_dir.parent
    
    print("🧪 Test de la bibliothèque standard Meshr-Lang")
    print("=" * 50)
    
    # Trouve tous les fichiers .meshr dans la stdlib
    meshr_files = list(stdlib_dir.rglob("*.meshr"))
    
    if not meshr_files:
        print("❌ Aucun fichier .meshr trouvé dans la stdlib")
        return 1
    
    print(f"📁 Fichiers trouvés: {len(meshr_files)}")
    print()
    
    success_count = 0
    total_count = len(meshr_files)
    
    for file_path in meshr_files:
        relative_path = file_path.relative_to(stdlib_dir)
        if test_meshr_file(file_path):
            success_count += 1
    
    print()
    print("=" * 50)
    print(f"📊 Résultats: {success_count}/{total_count} fichiers valides")
    
    if success_count == total_count:
        print("🎉 Tous les modules de la stdlib sont syntaxiquement corrects !")
        return 0
    else:
        print("⚠️  Certains modules ont des erreurs de syntaxe")
        return 1

if __name__ == "__main__":
    sys.exit(main())
