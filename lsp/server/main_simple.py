#!/usr/bin/env python3
"""
Point d'entrée pour le serveur LSP simple
"""

if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))
    from language_server_simple import server
    server.start_io()

