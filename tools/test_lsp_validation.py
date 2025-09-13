#!/usr/bin/env python3
"""
Script de test pour la validation des modules dans le LSP
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire du projet au path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from lsp.server.module_validation import ModuleValidator

def test_module_validation():
    """Test de la validation des modules"""
    print("🧪 Test de la validation des modules Meshr-Lang")
    print("=" * 50)
    
    # Créer un validateur
    workspace_root = str(project_root)
    validator = ModuleValidator(workspace_root)
    
    # Test 1: Analyser le plugin GCP Dataplex
    print("\n📋 Test 1: Analyse du plugin GCP Dataplex")
    
    plugin_files = [
        "stdlib/plugins/gcp/dataplex/annotations.meshr",
        "stdlib/plugins/gcp/dataplex/types.meshr", 
        "stdlib/plugins/gcp/dataplex/aspects.meshr",
        "stdlib/plugins/gcp/dataplex/index.meshr"
    ]
    
    for file_path in plugin_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"  📄 Analyse de {file_path}")
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            module_info = validator.analyze_file(str(full_path), content)
            print(f"    Module: {module_info.name}")
            print(f"    Exports: {len(module_info.exports)} - {list(module_info.exports)}")
            print(f"    Imports: {len(module_info.imports)}")
            
            # Valider les imports/exports
            diagnostics = validator.validate_imports_exports(module_info)
            if diagnostics:
                print(f"    ⚠️  {len(diagnostics)} diagnostic(s) trouvé(s):")
                for diag in diagnostics:
                    print(f"      - {diag.message}")
            else:
                print(f"    ✅ Aucun diagnostic")
        else:
            print(f"  ❌ Fichier non trouvé: {file_path}")
    
    # Test 2: Analyser l'exemple
    print("\n📋 Test 2: Analyse de l'exemple")
    
    example_file = project_root / "examples/dataplex-data-governance.meshr"
    if example_file.exists():
        print(f"  📄 Analyse de {example_file}")
        with open(example_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        module_info = validator.analyze_file(str(example_file), content)
        print(f"    Module: {module_info.name}")
        print(f"    Exports: {len(module_info.exports)} - {list(module_info.exports)}")
        print(f"    Imports: {len(module_info.imports)}")
        
        # Valider les imports/exports
        diagnostics = validator.validate_imports_exports(module_info)
        if diagnostics:
            print(f"    ⚠️  {len(diagnostics)} diagnostic(s) trouvé(s):")
            for diag in diagnostics:
                print(f"      - {diag.message}")
        else:
            print(f"    ✅ Aucun diagnostic")
    else:
        print(f"  ❌ Fichier non trouvé: {example_file}")
    
    # Test 3: Dépendances circulaires
    print("\n📋 Test 3: Validation des dépendances circulaires")
    
    circular_diagnostics = validator.validate_circular_dependencies()
    if circular_diagnostics:
        print(f"  ⚠️  {len(circular_diagnostics)} dépendance(s) circulaire(s) trouvée(s):")
        for diag in circular_diagnostics:
            print(f"    - {diag.message}")
    else:
        print(f"  ✅ Aucune dépendance circulaire")
    
    # Test 4: Résumé des modules
    print("\n📋 Test 4: Résumé des modules analysés")
    
    print(f"  📊 {len(validator.modules)} module(s) analysé(s):")
    for module_name, module_info in validator.modules.items():
        print(f"    - {module_name}")
        print(f"      Fichier: {module_info.file_path}")
        print(f"      Exports: {len(module_info.exports)}")
        print(f"      Imports: {len(module_info.imports)}")
        if module_info.imports:
            for imported_module, items in module_info.imports:
                print(f"        → {imported_module} ({len(items)} items)")
    
    print("\n🎉 Test terminé!")

def test_invalid_imports():
    """Test avec des imports invalides"""
    print("\n🧪 Test avec des imports invalides")
    print("=" * 50)
    
    # Créer un validateur
    workspace_root = str(project_root)
    validator = ModuleValidator(workspace_root)
    
    # Contenu avec import invalide
    invalid_content = """
@Version("1.0.0")
module test.invalid

// Import d'un module inexistant
import { NonExistentType } from stdlib.nonexistent

// Import d'un élément non exporté
import { NonExistentExport } from stdlib.plugins.gcp.dataplex

aspect TestAspect is
    field : String = "test"
end
"""
    
    # Analyser le contenu invalide
    module_info = validator.analyze_file("test_invalid.meshr", invalid_content)
    diagnostics = validator.validate_imports_exports(module_info)
    
    print(f"  📄 Contenu avec imports invalides analysé")
    print(f"  ⚠️  {len(diagnostics)} diagnostic(s) trouvé(s):")
    for diag in diagnostics:
        print(f"    - {diag.message}")

if __name__ == "__main__":
    test_module_validation()
    test_invalid_imports()
