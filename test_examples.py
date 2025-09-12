#!/usr/bin/env python3
"""
Script de test pour valider les exemples Meshr-Lang
"""

import os
import sys
import subprocess
from pathlib import Path

def test_example_file(file_path):
    """Teste un fichier d'exemple"""
    print(f"Testing {file_path}...")
    
    try:
        # Utiliser le script de test existant avec PYTHONPATH correct
        result = subprocess.run([
            sys.executable, 
            'tests/parse_module.py', 
            str(file_path)
        ], 
        capture_output=True, 
        text=True, 
        env={**os.environ, 'PYTHONPATH': '.'},
        cwd=Path(__file__).parent
        )
        
        if result.returncode == 0:
            print(f"✅ {file_path} - OK")
            return True
        else:
            print(f"❌ {file_path} - FAILED")
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            return False
            
    except Exception as e:
        print(f"❌ {file_path} - ERROR: {e}")
        return False

def main():
    """Teste tous les exemples"""
    examples_dir = Path("examples")
    
    if not examples_dir.exists():
        print("❌ Dossier examples/ non trouvé")
        return 1
    
    # Trouver tous les fichiers .meshr dans examples/
    example_files = list(examples_dir.glob("*.meshr"))
    
    if not example_files:
        print("❌ Aucun fichier .meshr trouvé dans examples/")
        return 1
    
    print(f"🧪 Test de {len(example_files)} exemples...")
    print("=" * 50)
    
    success_count = 0
    total_count = len(example_files)
    
    for file_path in sorted(example_files):
        if test_example_file(file_path):
            success_count += 1
    
    print("=" * 50)
    print(f"📊 Résultats: {success_count}/{total_count} exemples passent")
    
    if success_count == total_count:
        print("🎉 Tous les exemples sont valides !")
        return 0
    else:
        print("⚠️  Certains exemples ont des erreurs")
        return 1

if __name__ == "__main__":
    sys.exit(main())
