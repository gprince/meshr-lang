#!/usr/bin/env python3
"""
Point d'entrée pour le serveur LSP Meshr-Lang avec débogage
"""

import sys
import os

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, os.path.dirname(__file__))

# Importer et démarrer le serveur
from language_server_debug import server

if __name__ == "__main__":
    print("🎨 Démarrage du serveur LSP Meshr-Lang Debug", file=sys.stderr)
    server.start_io()
