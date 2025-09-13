#!/usr/bin/env python3
"""
Démonstration complète de l'intégration Meshr -> Dataplex Universal Catalog
"""

import json
import subprocess
import sys
import os
from pathlib import Path

def run_command(command: str, description: str) -> bool:
    """Exécute une commande et affiche le résultat"""
    print(f"\n🔄 {description}")
    print(f"   Commande: {command}")
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"   ✅ Succès")
            if result.stdout:
                print(f"   Sortie: {result.stdout.strip()}")
            return True
        else:
            print(f"   ❌ Erreur (code: {result.returncode})")
            if result.stderr:
                print(f"   Erreur: {result.stderr.strip()}")
            return False
    
    except Exception as e:
        print(f"   ❌ Exception: {e}")
        return False

def main():
    """Démonstration complète"""
    print("🚀 Démonstration de l'intégration Meshr -> Dataplex Universal Catalog")
    print("=" * 70)
    
    # Vérifier que nous sommes dans le bon répertoire
    if not Path("examples/dataplex-data-governance.meshr").exists():
        print("❌ Fichier d'exemple non trouvé. Assurez-vous d'être dans le répertoire racine du projet.")
        return
    
    # Étape 1: Parser le fichier Meshr et générer le JSON
    print("\n📋 ÉTAPE 1: Traduction Meshr -> JSON")
    success = run_command(
        "python tools/meshr_to_dataplex.py",
        "Traduction du fichier Meshr vers JSON"
    )
    
    if not success:
        print("❌ Échec de la traduction. Arrêt de la démonstration.")
        return
    
    # Étape 2: Vérifier le fichier JSON généré
    print("\n📋 ÉTAPE 2: Vérification du fichier JSON généré")
    json_file = "dataplex-data-governance.json"
    
    if Path(json_file).exists():
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        aspect_types = data.get("aspect_types", [])
        api_calls = data.get("api_calls", [])
        
        print(f"   ✅ Fichier JSON généré: {json_file}")
        print(f"   📊 {len(aspect_types)} aspect(s) traduit(s)")
        print(f"   🔧 {len(api_calls)} appel(s) API généré(s)")
        
        # Afficher un résumé des aspects
        for aspect in aspect_types:
            print(f"   - {aspect['display_name']} ({aspect['aspect_type_id']})")
            print(f"     {len(aspect['fields'])} champ(s)")
    else:
        print(f"   ❌ Fichier JSON non trouvé: {json_file}")
        return
    
    # Étape 3: Simulation de l'API Dataplex
    print("\n📋 ÉTAPE 3: Simulation des appels API Dataplex")
    
    if api_calls:
        api_call = api_calls[0]
        print(f"   🔗 URL: {api_call['url']}")
        print(f"   📝 Méthode: {api_call['method']}")
        print(f"   📦 Payload:")
        
        # Afficher un résumé du payload
        body = api_call['body']
        print(f"     - Aspect Type ID: {body['aspectTypeId']}")
        print(f"     - Display Name: {body['displayName']}")
        print(f"     - Description: {body['description'][:50]}...")
        print(f"     - Champs: {len(body['metadataTemplate']['recordFields'])}")
        
        # Afficher quelques champs
        fields = body['metadataTemplate']['recordFields'][:3]
        for field in fields:
            print(f"       * {field['name']} ({field['type']})")
        if len(body['metadataTemplate']['recordFields']) > 3:
            print(f"       ... et {len(body['metadataTemplate']['recordFields']) - 3} autres")
    
    # Étape 4: Instructions pour l'utilisation réelle
    print("\n📋 ÉTAPE 4: Instructions pour l'utilisation réelle")
    print("   Pour pousser les aspects vers Dataplex Universal Catalog:")
    print("   1. Configurez l'authentification Google Cloud:")
    print("      gcloud auth application-default login")
    print("   2. Exécutez le script de push:")
    print("      python tools/push_to_dataplex.py dataplex-data-governance.json \\")
    print("        --project-id YOUR_PROJECT_ID \\")
    print("        --location us-central1")
    print("   3. Ou en mode simulation:")
    print("      python tools/push_to_dataplex.py dataplex-data-governance.json \\")
    print("        --project-id YOUR_PROJECT_ID \\")
    print("        --dry-run")
    
    # Étape 5: Résumé des fichiers créés
    print("\n📋 ÉTAPE 5: Fichiers créés")
    files_created = [
        "examples/dataplex-data-governance.meshr",
        "tools/meshr_to_dataplex.py",
        "tools/push_to_dataplex.py",
        "dataplex-data-governance.json"
    ]
    
    for file_path in files_created:
        if Path(file_path).exists():
            size = Path(file_path).stat().st_size
            print(f"   ✅ {file_path} ({size} bytes)")
        else:
            print(f"   ❌ {file_path} (manquant)")
    
    # Étape 6: Prochaines étapes
    print("\n📋 ÉTAPE 6: Prochaines étapes recommandées")
    print("   1. 🧪 Tester avec un projet Google Cloud réel")
    print("   2. 🔧 Ajouter la gestion des erreurs et la validation")
    print("   3. 📚 Créer des aspects pour d'autres outils (DataHub, OpenMetadata)")
    print("   4. 🎨 Développer une interface utilisateur")
    print("   5. 📖 Documenter l'API et les cas d'usage")
    
    print("\n🎉 Démonstration terminée avec succès!")
    print("   L'intégration Meshr -> Dataplex Universal Catalog est fonctionnelle.")

if __name__ == "__main__":
    main()
