#!/usr/bin/env python3
"""
Serveur LSP Meshr-Lang standalone
=================================
Serveur LSP embarqué dans l'extension VS Code
"""

import sys
import os
from pathlib import Path

# Déterminer le répertoire de base
if getattr(sys, 'frozen', False):
    # Mode PyInstaller (exécutable)
    base_dir = Path(sys._MEIPASS)
else:
    # Mode développement
    base_dir = Path(__file__).parent

# Ajouter les chemins nécessaires
sys.path.insert(0, str(base_dir))
sys.path.insert(0, str(base_dir.parent.parent))  # Pour meshr_project.py

# Importer et lancer le serveur
if __name__ == "__main__":
    try:
        # Import direct des modules nécessaires
        from language_server import MeshrLanguageServer
        from pygls.server import LanguageServer
        
        # Créer et lancer le serveur
        server = MeshrLanguageServer()
        server.start_io()
    except Exception as e:
        print(f"❌ Erreur serveur LSP: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
