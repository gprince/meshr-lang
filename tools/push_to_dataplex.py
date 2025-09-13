#!/usr/bin/env python3
"""
Script pour pousser les aspects Meshr traduits vers l'API Dataplex Universal Catalog
"""

import json
import requests
import argparse
import sys
import yaml
from typing import Dict, Any, List
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.auth import default

class DataplexAPIClient:
    """Client pour l'API Dataplex Universal Catalog"""
    
    def __init__(self, project_id: str, location: str, credentials_path: str = None):
        self.project_id = project_id
        self.location = location
        self.base_url = f"https://dataplex.googleapis.com/v1/projects/{project_id}/locations/{location}"
        
        # Configuration de l'authentification
        if credentials_path:
            self.credentials = service_account.Credentials.from_service_account_file(
                credentials_path,
                scopes=['https://www.googleapis.com/auth/cloud-platform']
            )
        else:
            # Utiliser les credentials par défaut (gcloud auth)
            self.credentials, _ = default(
                scopes=['https://www.googleapis.com/auth/cloud-platform']
            )
        
        # Rafraîchir le token si nécessaire
        if not self.credentials.valid:
            self.credentials.refresh(Request())
    
    def _get_headers(self) -> Dict[str, str]:
        """Retourne les headers d'authentification"""
        return {
            'Authorization': f'Bearer {self.credentials.token}',
            'Content-Type': 'application/json'
        }
    
    def create_aspect_type(self, aspect_data: Dict[str, Any]) -> Dict[str, Any]:
        """Crée un type d'aspect dans Dataplex"""
        url = f"{self.base_url}/aspectTypes"
        
        # Construire le payload selon l'API Dataplex
        payload = {
            "aspectTypeId": aspect_data["aspect_type_id"],
            "displayName": aspect_data["display_name"],
            "description": aspect_data["description"],
            "labels": aspect_data.get("labels", {}),
            "metadataTemplate": {
                "recordFields": []
            }
        }
        
        # Ajouter les champs
        for i, field in enumerate(aspect_data["fields"], 1):
            field_def = {
                "index": i,
                "name": field["name"],
                "type": field["type"],
                "constraints": {
                    "required": field["required"]
                }
            }
            
            # Ajouter les valeurs d'enum si nécessaire
            if field["type"] == "enum" and field.get("enum_values"):
                field_def["enumValues"] = [
                    {"index": j, "name": value}
                    for j, value in enumerate(field["enum_values"], 1)
                ]
            
            payload["metadataTemplate"]["recordFields"].append(field_def)
        
        try:
            response = requests.post(
                url,
                headers=self._get_headers(),
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur lors de la création de l'aspect {aspect_data['aspect_type_id']}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"   Détails: {e.response.text}")
            return None
    
    def list_aspect_types(self) -> List[Dict[str, Any]]:
        """Liste tous les types d'aspects existants"""
        url = f"{self.base_url}/aspectTypes"
        
        try:
            response = requests.get(
                url,
                headers=self._get_headers(),
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data.get("aspectTypes", [])
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur lors de la récupération des aspects: {e}")
            return []
    
    def get_aspect_type(self, aspect_type_id: str) -> Dict[str, Any]:
        """Récupère un type d'aspect spécifique"""
        url = f"{self.base_url}/aspectTypes/{aspect_type_id}"
        
        try:
            response = requests.get(
                url,
                headers=self._get_headers(),
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur lors de la récupération de l'aspect {aspect_type_id}: {e}")
            return None
    
    def update_aspect_type(self, aspect_type_id: str, aspect_data: Dict[str, Any]) -> Dict[str, Any]:
        """Met à jour un type d'aspect existant"""
        url = f"{self.base_url}/aspectTypes/{aspect_type_id}"
        
        # Construire le payload de mise à jour
        payload = {
            "displayName": aspect_data["display_name"],
            "description": aspect_data["description"],
            "labels": aspect_data.get("labels", {}),
            "metadataTemplate": {
                "recordFields": []
            }
        }
        
        # Ajouter les champs
        for i, field in enumerate(aspect_data["fields"], 1):
            field_def = {
                "index": i,
                "name": field["name"],
                "type": field["type"],
                "constraints": {
                    "required": field["required"]
                }
            }
            
            # Ajouter les valeurs d'enum si nécessaire
            if field["type"] == "enum" and field.get("enum_values"):
                field_def["enumValues"] = [
                    {"index": j, "name": value}
                    for j, value in enumerate(field["enum_values"], 1)
                ]
            
            payload["metadataTemplate"]["recordFields"].append(field_def)
        
        try:
            response = requests.patch(
                url,
                headers=self._get_headers(),
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur lors de la mise à jour de l'aspect {aspect_type_id}: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"   Détails: {e.response.text}")
            return None

def load_config(config_file: str = "dataplex_config.yaml") -> Dict[str, Any]:
    """Charge la configuration depuis un fichier YAML"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"⚠️  Fichier de configuration non trouvé: {config_file}")
        return {}
    except yaml.YAMLError as e:
        print(f"❌ Erreur de parsing YAML: {e}")
        return {}

def load_aspects_from_json(json_file: str) -> List[Dict[str, Any]]:
    """Charge les aspects depuis un fichier JSON"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get("aspect_types", [])
    except FileNotFoundError:
        print(f"❌ Fichier non trouvé: {json_file}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de parsing JSON: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Pousser les aspects Meshr vers Dataplex Universal Catalog")
    parser.add_argument("json_file", help="Fichier JSON contenant les aspects traduits")
    parser.add_argument("--config", default="dataplex_config.yaml", help="Fichier de configuration YAML")
    parser.add_argument("--environment", default="staging", help="Environnement à utiliser")
    parser.add_argument("--project-id", help="ID du projet Google Cloud (override la config)")
    parser.add_argument("--location", help="Localisation (override la config)")
    parser.add_argument("--credentials", help="Chemin vers le fichier de credentials JSON")
    parser.add_argument("--dry-run", action="store_true", help="Simulation sans exécution réelle")
    parser.add_argument("--update", action="store_true", help="Mettre à jour les aspects existants")
    parser.add_argument("--list", action="store_true", help="Lister les aspects existants")
    
    args = parser.parse_args()
    
    # Charger la configuration
    config = load_config(args.config)
    
    # Déterminer les paramètres de connexion
    if args.environment in config.get("environments", {}):
        env_config = config["environments"][args.environment]
        project_id = args.project_id or env_config.get("project_id")
        location = args.location or env_config.get("location", "us-central1")
        credentials_path = args.credentials or env_config.get("credentials_path")
    else:
        # Utiliser la configuration par défaut
        default_config = config.get("default", {})
        project_id = args.project_id or default_config.get("project_id")
        location = args.location or default_config.get("location", "us-central1")
        credentials_path = args.credentials or default_config.get("credentials_path")
    
    if not project_id:
        print("❌ ID du projet non spécifié. Utilisez --project-id ou configurez-le dans le fichier de configuration.")
        return
    
    # Initialiser le client Dataplex
    client = DataplexAPIClient(
        project_id=project_id,
        location=location,
        credentials_path=credentials_path
    )
    
    if args.list:
        print(f"🔍 Liste des aspects existants dans {args.project_id}/{args.location}:")
        aspects = client.list_aspect_types()
        
        if not aspects:
            print("   Aucun aspect trouvé.")
        else:
            for aspect in aspects:
                print(f"   - {aspect.get('displayName', 'N/A')} ({aspect.get('name', 'N/A')})")
                print(f"     {aspect.get('description', 'Pas de description')}")
        
        return
    
    # Charger les aspects depuis le fichier JSON
    print(f"📂 Chargement des aspects depuis: {args.json_file}")
    aspects = load_aspects_from_json(args.json_file)
    
    if not aspects:
        print("❌ Aucun aspect trouvé dans le fichier.")
        return
    
    print(f"✅ {len(aspects)} aspect(s) chargé(s)")
    
    # Traiter chaque aspect
    for aspect in aspects:
        aspect_id = aspect["aspect_type_id"]
        display_name = aspect["display_name"]
        
        print(f"\n🔄 Traitement de l'aspect: {display_name} ({aspect_id})")
        
        if args.dry_run:
            print(f"   [DRY RUN] Création/mise à jour de l'aspect {aspect_id}")
            continue
        
        # Vérifier si l'aspect existe déjà
        existing_aspect = client.get_aspect_type(aspect_id)
        
        if existing_aspect:
            if args.update:
                print(f"   📝 Mise à jour de l'aspect existant...")
                result = client.update_aspect_type(aspect_id, aspect)
                if result:
                    print(f"   ✅ Aspect {aspect_id} mis à jour avec succès")
                else:
                    print(f"   ❌ Échec de la mise à jour de l'aspect {aspect_id}")
            else:
                print(f"   ⚠️  Aspect {aspect_id} existe déjà. Utilisez --update pour le mettre à jour.")
        else:
            print(f"   🆕 Création du nouvel aspect...")
            result = client.create_aspect_type(aspect)
            if result:
                print(f"   ✅ Aspect {aspect_id} créé avec succès")
            else:
                print(f"   ❌ Échec de la création de l'aspect {aspect_id}")
    
    print(f"\n🎉 Traitement terminé!")

if __name__ == "__main__":
    main()
