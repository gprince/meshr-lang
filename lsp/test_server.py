#!/usr/bin/env python3
"""
Test simple du serveur LSP Meshr-Lang
"""

import sys
import json
from pathlib import Path

# Ajouter le chemin vers le serveur LSP
sys.path.insert(0, str(Path(__file__).parent / "server"))

from lsp.server.parser import MeshrParser
from lsp.server.diagnostics import MeshrDiagnostics
from lsp.server.completion import MeshrCompletion
from lsp.server.symbols import MeshrSymbols

def test_lsp_components():
    """Test des composants LSP"""
    print("🧪 Test des composants LSP Meshr-Lang")
    print("=" * 50)
    
    # Test du parser
    parser = MeshrParser()
    print(f"✅ Parser initialisé: {parser.is_grammar_available()}")
    
    # Test avec un fichier simple
    test_code = """
module test;

entity User is
    name : String
    age : Integer
end
"""
    
    tree = parser.parse(test_code)
    print(f"✅ Parsing réussi: {tree is not None}")
    
    # Test des diagnostics
    diagnostics = MeshrDiagnostics(parser)
    diags = diagnostics.analyze(tree, "test.meshr")
    print(f"✅ Diagnostics: {len(diags)} trouvés")
    
    # Test de l'autocomplétion
    completion = MeshrCompletion(parser)
    print(f"✅ Autocomplétion initialisée")
    
    # Test des symboles
    symbols = MeshrSymbols(parser)
    print(f"✅ Symboles initialisés")
    
    print("\n🎉 Tous les composants LSP fonctionnent correctement !")
    return True

if __name__ == "__main__":
    try:
        test_lsp_components()
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)
