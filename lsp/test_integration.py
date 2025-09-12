#!/usr/bin/env python3
"""
Test d'intégration du serveur LSP avec les vrais fichiers Meshr-Lang
"""

import sys
from pathlib import Path

# Ajouter le chemin vers le serveur LSP
sys.path.insert(0, str(Path(__file__).parent / "server"))

from lsp.server.parser import MeshrParser
from lsp.server.diagnostics import MeshrDiagnostics
from lsp.server.completion import MeshrCompletion
from lsp.server.symbols import MeshrSymbols

def test_real_files():
    """Test avec les vrais fichiers d'exemple"""
    print("🧪 Test d'intégration du serveur LSP")
    print("=" * 50)
    
    # Initialiser les composants
    parser = MeshrParser()
    diagnostics = MeshrDiagnostics(parser)
    completion = MeshrCompletion(parser)
    symbols = MeshrSymbols(parser)
    
    # Tester avec les fichiers d'exemple
    example_files = [
        "examples/ecommerce-products.meshr",
        "examples/ecommerce-orders.meshr", 
        "examples/hr-employees.meshr",
        "examples/banking-accounts.meshr",
        "examples/apis-management.meshr"
    ]
    
    success_count = 0
    total_count = len(example_files)
    
    for file_path in example_files:
        print(f"\n📄 Test de {file_path}...")
        
        try:
            # Lire le fichier
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Test du parser
            tree = parser.parse(content)
            if tree is not None:
                print("  ✅ Parser: OK")
            else:
                print("  ❌ Parser: ÉCHEC")
                continue
            
            # Test des diagnostics
            diags = diagnostics.analyze(tree, file_path)
            print(f"  ✅ Diagnostics: {len(diags)} trouvés")
            
            # Test des symboles
            class MockDocument:
                def __init__(self, text):
                    self.lines = text.split('\n')
            
            doc = MockDocument(content)
            syms = symbols.get_document_symbols(doc)
            print(f"  ✅ Symboles: {len(syms)} extraits")
            
            # Test de l'autocomplétion (simulation)
            from lsprotocol.types import Position
            position = Position(line=0, character=0)
            completions = completion.get_completions(doc, position)
            print(f"  ✅ Autocomplétion: {len(completions)} suggestions")
            
            success_count += 1
            print(f"  🎉 {file_path}: TOUS LES TESTS PASSENT")
            
        except Exception as e:
            print(f"  ❌ Erreur: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Résultats: {success_count}/{total_count} fichiers testés avec succès")
    
    if success_count == total_count:
        print("🎉 TOUS LES TESTS D'INTÉGRATION PASSENT !")
        return True
    else:
        print("⚠️  Certains tests ont échoué")
        return False

if __name__ == "__main__":
    success = test_real_files()
    sys.exit(0 if success else 1)
