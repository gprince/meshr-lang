#!/usr/bin/env python3
"""
Script de test pour valider les diagnostics du serveur LSP Meshr-Lang
"""

import sys
import os
from pathlib import Path

# Ajouter les chemins nécessaires
sys.path.insert(0, str(Path(__file__).parent / "lsp" / "server"))
sys.path.insert(0, str(Path(__file__).parent / "grammar" / "generated"))

from lsp.server.language_server import MeshrLanguageServer
from lsprotocol.types import TextDocumentItem, Position, Range
from lsprotocol.types import InitializeParams, ClientCapabilities, TextDocumentClientCapabilities

def test_diagnostics():
    """Test des diagnostics avec le fichier index.meshr"""
    
    print("=== Test des diagnostics LSP Meshr-Lang ===\n")
    
    # Créer le serveur LSP
    server = MeshrLanguageServer()
    
    # Lire le fichier index.meshr
    index_file = Path(__file__).parent / "stdlib" / "core" / "index.meshr"
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"📄 Fichier analysé: {index_file}")
    print(f"📏 Taille du fichier: {len(content)} caractères")
    
    # Créer un document LSP
    doc = TextDocumentItem(
        uri=f"file://{index_file}",
        language_id="meshr",
        version=1,
        text=content
    )
    
    # Analyser directement le document
    print("\n🔍 Analyse du document...")
    server._analyze_document(doc)
    
    # Vérifier les diagnostics dans le cache
    if doc.uri in server.document_cache:
        cached_data = server.document_cache[doc.uri]
        diagnostics = cached_data.get('diagnostics', [])
        
        print(f"\n📊 Résultats de l'analyse:")
        print(f"   Nombre de diagnostics: {len(diagnostics)}")
        
        if diagnostics:
            print("\n🚨 Diagnostics trouvés:")
            for i, diag in enumerate(diagnostics, 1):
                print(f"   {i}. Ligne {diag.range.start.line + 1}, colonne {diag.range.start.character}")
                print(f"      Message: {diag.message}")
                print(f"      Sévérité: {diag.severity}")
                print(f"      Source: {diag.source}")
                print()
        else:
            print("   ✅ Aucun diagnostic trouvé")
    else:
        print("❌ Document non trouvé dans le cache")
    
    # Test avec un fichier contenant des erreurs évidentes
    print("\n" + "="*50)
    print("🧪 Test avec des erreurs de syntaxe évidentes")
    
    test_content = """
module test;

// Erreur de syntaxe évidente
export { !@#$%^&*() }

// Autre erreur
entity TestEntity {
    invalid syntax here
}
"""
    
    test_doc = TextDocumentItem(
        uri="file:///test_errors.meshr",
        language_id="meshr",
        version=1,
        text=test_content
    )
    
    print("🔍 Analyse du document de test...")
    server._analyze_document(test_doc)
    
    if test_doc.uri in server.document_cache:
        cached_data = server.document_cache[test_doc.uri]
        diagnostics = cached_data.get('diagnostics', [])
        
        print(f"\n📊 Résultats de l'analyse du test:")
        print(f"   Nombre de diagnostics: {len(diagnostics)}")
        
        if diagnostics:
            print("\n🚨 Diagnostics trouvés:")
            for i, diag in enumerate(diagnostics, 1):
                print(f"   {i}. Ligne {diag.range.start.line + 1}, colonne {diag.range.start.character}")
                print(f"      Message: {diag.message}")
                print(f"      Sévérité: {diag.severity}")
                print()
        else:
            print("   ⚠️  Aucun diagnostic trouvé (problème possible)")
    else:
        print("❌ Document de test non trouvé dans le cache")

if __name__ == "__main__":
    test_diagnostics()
