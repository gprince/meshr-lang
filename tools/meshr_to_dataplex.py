#!/usr/bin/env python3
"""
Outil de traduction des aspects Meshr vers Dataplex Universal Catalog
Traduit les déclarations d'aspects Meshr en appels API Dataplex
"""

import json
import re
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

@dataclass
class DataplexField:
    """Représente un champ dans un aspect Dataplex"""
    name: str
    type: str
    description: str
    required: bool = False
    enum_values: Optional[List[str]] = None
    default_value: Optional[Any] = None

@dataclass
class DataplexAspectType:
    """Représente un type d'aspect Dataplex"""
    aspect_type_id: str
    display_name: str
    description: str
    project_id: str
    location: str
    labels: Dict[str, str]
    fields: List[DataplexField]
    created_on: str
    last_modified: str

class MeshrToDataplexTranslator:
    """Traducteur des aspects Meshr vers Dataplex Universal Catalog"""
    
    # Mapping des types Meshr vers les types Dataplex
    TYPE_MAPPING = {
        'String': 'string',
        'Integer': 'int',
        'Float': 'double',
        'Boolean': 'bool',
        'Datetime': 'datetime',
        'Date': 'datetime',
        'Time': 'datetime',
        'Timestamp': 'datetime',
        'Json': 'string',  # JSON sera sérialisé en string
        'Bytes': 'string',  # Bytes sera encodé en base64
        'Geography': 'string',  # Géographie sera en format WKT/GeoJSON
        'Sql': 'string',  # SQL sera en string
        'Interval': 'string'  # Interval sera en string
    }
    
    def __init__(self):
        self.aspect_types: List[DataplexAspectType] = []
        self.enums: Dict[str, List[str]] = {}
    
    def parse_meshr_file(self, file_path: str) -> List[DataplexAspectType]:
        """Parse un fichier Meshr et extrait les aspects"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraire les imports
        imports = self._extract_imports(content)
        
        # Charger les plugins si nécessaire
        self._load_plugins(imports)
        
        # Extraire les aspects
        aspects = self._extract_aspects(content)
        
        # Extraire les enums
        self._extract_enums(content)
        
        # Convertir chaque aspect
        for aspect in aspects:
            dataplex_aspect = self._convert_aspect_to_dataplex(aspect)
            if dataplex_aspect:
                self.aspect_types.append(dataplex_aspect)
        
        return self.aspect_types
    
    def _extract_imports(self, content: str) -> List[Dict[str, Any]]:
        """Extrait les déclarations d'import du contenu Meshr"""
        imports = []
        
        # Pattern pour capturer les imports
        import_pattern = r'import\s*\{\s*([^}]+)\s*\}\s*from\s+([^\s]+)'
        
        matches = re.finditer(import_pattern, content, re.MULTILINE)
        
        for match in matches:
            imported_items = match.group(1)
            module_path = match.group(2)
            
            # Parser les éléments importés
            items = [item.strip() for item in imported_items.split(',')]
            
            imports.append({
                'items': items,
                'module': module_path
            })
        
        return imports
    
    def _load_plugins(self, imports: List[Dict[str, Any]]):
        """Charge les plugins nécessaires"""
        for import_info in imports:
            module_path = import_info['module']
            
            # Charger le plugin GCP Dataplex si nécessaire
            if 'stdlib.plugins.gcp.dataplex' in module_path:
                self._load_dataplex_plugin()
    
    def _load_dataplex_plugin(self):
        """Charge le plugin GCP Dataplex"""
        plugin_path = "stdlib/plugins/gcp/dataplex"
        
        # Charger les types
        types_file = f"{plugin_path}/types.meshr"
        if Path(types_file).exists():
            with open(types_file, 'r', encoding='utf-8') as f:
                content = f.read()
            self._extract_enums(content)
        
        # Charger les aspects
        aspects_file = f"{plugin_path}/aspects.meshr"
        if Path(aspects_file).exists():
            with open(aspects_file, 'r', encoding='utf-8') as f:
                content = f.read()
            self._extract_enums(content)
    
    def _extract_aspects(self, content: str) -> List[Dict[str, Any]]:
        """Extrait les déclarations d'aspects du contenu Meshr"""
        aspects = []
        
        # Pattern pour capturer un aspect complet
        aspect_pattern = r'@DataplexAspect\([^)]*\)\s*aspect\s+(\w+)\s+is\s*((?:[^}]+|{[^}]*})*?)\s*end'
        
        matches = re.finditer(aspect_pattern, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            aspect_name = match.group(1)
            aspect_body = match.group(2)
            
            # Extraire les annotations
            annotations = self._extract_annotations(match.group(0))
            
            # Extraire les champs
            fields = self._extract_fields(aspect_body)
            
            aspects.append({
                'name': aspect_name,
                'annotations': annotations,
                'fields': fields
            })
        
        return aspects
    
    def _extract_annotations(self, aspect_text: str) -> Dict[str, Any]:
        """Extrait les annotations d'un aspect"""
        annotations = {}
        
        # Pattern pour les annotations DataplexAspect
        annotation_pattern = r'@DataplexAspect\(\s*([^)]+)\s*\)'
        match = re.search(annotation_pattern, aspect_text, re.DOTALL)
        
        if match:
            annotation_content = match.group(1)
            
            # Extraire les paires clé=valeur
            pairs = re.findall(r'(\w+)\s*=\s*([^,}]+)', annotation_content)
            
            for key, value in pairs:
                # Nettoyer la valeur
                value = value.strip().strip('"\'')
                
                # Convertir les types spéciaux
                if value.startswith('Map{'):
                    # Parser les maps
                    annotations[key] = self._parse_map(value)
                elif value.upper() in ['TRUE', 'FALSE']:
                    annotations[key] = value.upper() == 'TRUE'
                elif value.isdigit():
                    annotations[key] = int(value)
                else:
                    annotations[key] = value
        
        return annotations
    
    def _extract_fields(self, aspect_body: str) -> List[Dict[str, Any]]:
        """Extrait les champs d'un aspect"""
        fields = []
        
        # Pattern pour capturer les champs
        field_pattern = r'(\w+)\s*:\s*(\w+(?:\s+of\s+\w+)?)\s*(?:=\s*([^;]+))?'
        
        lines = aspect_body.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            
            match = re.search(field_pattern, line)
            if match:
                field_name = match.group(1)
                field_type = match.group(2)
                default_value = match.group(3).strip() if match.group(3) else None
                
                # Extraire la description si elle existe
                description = self._extract_field_description(line)
                
                fields.append({
                    'name': field_name,
                    'type': field_type,
                    'description': description,
                    'default_value': default_value
                })
        
        return fields
    
    def _extract_field_description(self, line: str) -> str:
        """Extrait la description d'un champ depuis sa valeur par défaut"""
        # Si la valeur par défaut est une chaîne, l'utiliser comme description
        if '=' in line:
            default_part = line.split('=')[1].strip()
            if default_part.startswith('"') and default_part.endswith('"'):
                return default_part[1:-1]
        return ""
    
    def _extract_enums(self, content: str):
        """Extrait les déclarations d'enums"""
        enum_pattern = r'@DataplexEnum\([^)]*\)\s*enum\s+(\w+)\s+is\s*\(\s*([^)]+)\s*\)'
        
        matches = re.finditer(enum_pattern, content, re.MULTILINE | re.DOTALL)
        
        for match in matches:
            enum_name = match.group(1)
            enum_values_text = match.group(2)
            
            # Extraire les valeurs de l'enum
            values = []
            for value in enum_values_text.split(','):
                value = value.strip()
                if value:
                    values.append(value)
            
            self.enums[enum_name] = values
    
    def _parse_map(self, map_str: str) -> Dict[str, str]:
        """Parse une chaîne Map{...} en dictionnaire Python"""
        # Pattern simple pour Map{"key": "value"}
        pairs = re.findall(r'"([^"]+)"\s*:\s*"([^"]+)"', map_str)
        return dict(pairs)
    
    def _convert_aspect_to_dataplex(self, aspect: Dict[str, Any]) -> Optional[DataplexAspectType]:
        """Convertit un aspect Meshr en aspect Dataplex"""
        annotations = aspect.get('annotations', {})
        fields = aspect.get('fields', [])
        
        # Vérifier que c'est un aspect Dataplex
        if 'aspect_type_id' not in annotations:
            return None
        
        # Convertir les champs
        dataplex_fields = []
        for field in fields:
            field_name = field['name']
            field_type = field['type']
            description = field['description']
            
            # Mapper le type
            dataplex_type = self.TYPE_MAPPING.get(field_type, 'string')
            
            # Vérifier si c'est un enum
            enum_values = None
            if field_type in self.enums:
                enum_values = self.enums[field_type]
                dataplex_type = 'enum'
            
            # Déterminer si le champ est requis
            required = field.get('default_value') is None
            
            dataplex_field = DataplexField(
                name=field_name,
                type=dataplex_type,
                description=description,
                required=required,
                enum_values=enum_values
            )
            dataplex_fields.append(dataplex_field)
        
        # Créer l'aspect Dataplex
        return DataplexAspectType(
            aspect_type_id=annotations.get('aspect_type_id', ''),
            display_name=annotations.get('display_name', aspect['name']),
            description=annotations.get('description', ''),
            project_id=annotations.get('project_id', 'default-project'),
            location=annotations.get('location', 'us-central1'),
            labels=annotations.get('labels', {}),
            fields=dataplex_fields,
            created_on=datetime.now().isoformat(),
            last_modified=datetime.now().isoformat()
        )
    
    def generate_dataplex_api_calls(self) -> List[Dict[str, Any]]:
        """Génère les appels API Dataplex pour créer les aspects"""
        api_calls = []
        
        for aspect_type in self.aspect_types:
            # Construire le payload pour l'API Dataplex
            payload = {
                "aspectTypeId": aspect_type.aspect_type_id,
                "displayName": aspect_type.display_name,
                "description": aspect_type.description,
                "labels": aspect_type.labels,
                "metadataTemplate": {
                    "recordFields": []
                }
            }
            
            # Ajouter les champs
            for i, field in enumerate(aspect_type.fields, 1):
                field_def = {
                    "index": i,
                    "name": field.name,
                    "type": field.type,
                    "constraints": {
                        "required": field.required
                    }
                }
                
                # Ajouter les valeurs d'enum si nécessaire
                if field.type == 'enum' and field.enum_values:
                    field_def["enumValues"] = [
                        {"index": j, "name": value}
                        for j, value in enumerate(field.enum_values, 1)
                    ]
                
                payload["metadataTemplate"]["recordFields"].append(field_def)
            
            api_call = {
                "method": "POST",
                "url": f"https://dataplex.googleapis.com/v1/projects/{aspect_type.project_id}/locations/{aspect_type.location}/aspectTypes",
                "headers": {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
                },
                "body": payload
            }
            
            api_calls.append(api_call)
        
        return api_calls
    
    def save_to_json(self, output_file: str):
        """Sauvegarde les aspects traduits en JSON"""
        data = {
            "aspect_types": [
                {
                    "aspect_type_id": at.aspect_type_id,
                    "display_name": at.display_name,
                    "description": at.description,
                    "project_id": at.project_id,
                    "location": at.location,
                    "labels": at.labels,
                    "fields": [
                        {
                            "name": f.name,
                            "type": f.type,
                            "description": f.description,
                            "required": f.required,
                            "enum_values": f.enum_values
                        }
                        for f in at.fields
                    ]
                }
                for at in self.aspect_types
            ],
            "api_calls": self.generate_dataplex_api_calls()
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    """Fonction principale"""
    translator = MeshrToDataplexTranslator()
    
    # Parser le fichier Meshr
    input_file = "examples/dataplex-data-governance.meshr"
    output_file = "dataplex-data-governance.json"
    
    print(f"🔍 Parsing du fichier Meshr : {input_file}")
    aspect_types = translator.parse_meshr_file(input_file)
    
    print(f"✅ {len(aspect_types)} aspect(s) trouvé(s)")
    
    for aspect in aspect_types:
        print(f"  - {aspect.display_name} ({aspect.aspect_type_id})")
        print(f"    {len(aspect.fields)} champ(s)")
    
    # Générer les appels API
    print(f"\n🔧 Génération des appels API Dataplex...")
    api_calls = translator.generate_dataplex_api_calls()
    
    # Sauvegarder en JSON
    translator.save_to_json(output_file)
    print(f"💾 Résultats sauvegardés dans : {output_file}")
    
    # Afficher un exemple d'appel API
    if api_calls:
        print(f"\n📋 Exemple d'appel API :")
        print(json.dumps(api_calls[0], indent=2))

if __name__ == "__main__":
    main()
