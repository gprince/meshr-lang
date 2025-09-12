#!/usr/bin/env python3
"""
Point d'entrée du serveur LSP Meshr-Lang
"""

import sys
import logging
from pathlib import Path

# Ajouter le répertoire parent pour importer la grammaire
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lsp.server.language_server import MeshrLanguageServer

def main():
    """Point d'entrée principal du serveur LSP"""
    # Configuration du logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    logger = logging.getLogger(__name__)
    logger.info("Démarrage du serveur LSP Meshr-Lang")
    
    # Créer et démarrer le serveur
    server = MeshrLanguageServer()
    
    try:
        server.start_io()
    except KeyboardInterrupt:
        logger.info("Arrêt du serveur LSP")
    except Exception as e:
        logger.error(f"Erreur du serveur LSP: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
