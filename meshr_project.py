#!/usr/bin/env python3
"""
Meshr-Lang Project Manager
==========================
Gestionnaire de projet pour Meshr-Lang avec résolution de dépendances,
gestion des imports et support LSP.
"""

import os
import json
import toml
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class ModuleInfo:
    """Information sur un module Meshr-Lang"""
    name: str
    path: str
    version: str
    exports: List[str]
    imports: List[str]
    dependencies: List[str]

@dataclass
class ProjectConfig:
    """Configuration d'un projet Meshr-Lang"""
    name: str
    version: str
    description: str
    authors: List[str]
    module_name: str
    module_path: str
    dependencies: Dict[str, Dict]
    build_config: Dict
    lsp_config: Dict
    modules: Dict[str, Dict]  # Modules définis dans [modules]

class MeshrProjectManager:
    """Gestionnaire de projet Meshr-Lang"""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.config_file = self.project_root / "meshr.toml"
        self.config: Optional[ProjectConfig] = None
        self.modules: Dict[str, ModuleInfo] = {}
        self.dependency_graph: Dict[str, Set[str]] = defaultdict(set)
        
    def load_config(self) -> ProjectConfig:
        """Charge la configuration du projet"""
        if not self.config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")
            
        with open(self.config_file, 'r', encoding='utf-8') as f:
            data = toml.load(f)
            
        project_data = data.get('project', {})
        module_data = data.get('project', {}).get('module', {})
        
        self.config = ProjectConfig(
            name=project_data.get('name', ''),
            version=project_data.get('version', '1.0.0'),
            description=project_data.get('description', ''),
            authors=project_data.get('authors', []),
            module_name=module_data.get('name', ''),
            module_path=module_data.get('path', ''),
            dependencies=data.get('dependencies', {}),
            build_config=data.get('build', {}),
            lsp_config=data.get('lsp', {}),
            modules=data.get('modules', {})
        )
        
        return self.config
    
    def resolve_dependencies(self) -> Dict[str, ModuleInfo]:
        """Résout toutes les dépendances du projet"""
        if not self.config:
            self.load_config()
            
        # Charger les modules de dépendances
        for dep_name, dep_config in self.config.dependencies.items():
            if 'path' in dep_config:
                dep_path = self.project_root / dep_config['path']
                self._load_dependency_modules(dep_path, dep_name)
                
        # Charger le module principal
        main_module_path = self.project_root / self.config.module_path
        if main_module_path.exists():
            self._load_module(main_module_path, self.config.module_name)
            
        return self.modules
    
    def _load_dependency_modules(self, dep_path: Path, dep_name: str):
        """Charge les modules d'une dépendance"""
        dep_config_file = dep_path / "meshr.toml"
        if not dep_config_file.exists():
            return
            
        with open(dep_config_file, 'r', encoding='utf-8') as f:
            dep_data = toml.load(f)
            
        modules_config = dep_data.get('modules', {})
        for module_name, module_config in modules_config.items():
            module_path = dep_path / module_config['path']
            if module_path.exists():
                self._load_module(module_path, module_name)
    
    def _load_module(self, module_path: Path, module_name: str):
        """Charge un module Meshr-Lang et extrait ses informations"""
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extraire les exports
        exports = self._extract_exports(content)
        
        # Extraire les imports
        imports = self._extract_imports(content)
        
        # Extraire les dépendances (modules importés)
        dependencies = self._extract_dependencies(content)
        
        self.modules[module_name] = ModuleInfo(
            name=module_name,
            path=str(module_path),
            version="1.0.0",  # TODO: Extraire de la version du module
            exports=exports,
            imports=imports,
            dependencies=dependencies
        )
        
        # Construire le graphe de dépendances
        for dep in dependencies:
            self.dependency_graph[module_name].add(dep)
    
    def _extract_exports(self, content: str) -> List[str]:
        """Extrait les exports d'un module"""
        exports = []
        lines = content.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('export {'):
                # Export groupé multi-lignes: export { Item1, Item2, Item3 }
                export_items = []
                i += 1
                
                # Lire les lignes suivantes jusqu'à trouver '}'
                while i < len(lines):
                    line = lines[i].strip()
                    if line == '}':
                        break
                    # Extraire les items de cette ligne (ignorer les commentaires)
                    if not line.startswith('//') and not line.startswith('#'):
                        if line.endswith(','):
                            line = line[:-1]  # Enlever la virgule finale
                        items = [item.strip() for item in line.split(',') if item.strip()]
                        export_items.extend(items)
                    i += 1
                    
                exports.extend(export_items)
            elif line.startswith('export '):
                # Export inline: export declaration
                # TODO: Extraire le nom de la déclaration
                pass
            i += 1
                
        return exports
    
    def _extract_imports(self, content: str) -> List[str]:
        """Extrait les imports d'un module"""
        imports = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if line.startswith('import '):
                # Import simple: import Item from module
                # Import groupé: import { Item1, Item2 } from module
                if ' from ' in line:
                    module_part = line.split(' from ')[1]
                    if module_part not in imports:
                        imports.append(module_part)
                        
        return imports
    
    def _extract_dependencies(self, content: str) -> List[str]:
        """Extrait les dépendances (modules importés) d'un module"""
        return self._extract_imports(content)
    
    def resolve_import(self, module_name: str, symbol: str) -> Optional[Tuple[str, str]]:
        """Résout un import et retourne (module_source, symbol_path)"""
        if module_name not in self.modules:
            return None
            
        module = self.modules[module_name]
        
        # Vérifier si le symbole est exporté par ce module
        if symbol in module.exports:
            return (module.path, symbol)
            
        # Vérifier dans les dépendances
        for dep in module.dependencies:
            if dep in self.modules:
                dep_module = self.modules[dep]
                if symbol in dep_module.exports:
                    return (dep_module.path, symbol)
                    
        return None
    
    def get_available_symbols(self, module_name: str) -> Dict[str, List[str]]:
        """Retourne les symboles disponibles pour un module"""
        if module_name not in self.modules:
            return {}
            
        available = {}
        module = self.modules[module_name]
        
        # Symboles du module lui-même
        available[module_name] = module.exports
        
        # Symboles des dépendances
        for dep in module.dependencies:
            if dep in self.modules:
                available[dep] = self.modules[dep].exports
                
        return available
    
    def validate_imports(self, module_name: str) -> List[Dict]:
        """Valide les imports d'un module et retourne les erreurs"""
        errors = []
        
        if module_name not in self.modules:
            return [{"error": f"Module {module_name} not found"}]
            
        module = self.modules[module_name]
        
        for import_line in module.imports:
            # TODO: Parser l'import pour extraire les symboles
            # Pour l'instant, on vérifie juste que le module existe
            if import_line not in self.modules:
                errors.append({
                    "error": f"Module '{import_line}' not found",
                    "module": module_name,
                    "import": import_line
                })
                
        return errors

def main():
    """Fonction principale pour tester le gestionnaire de projet"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python meshr_project.py <project_root>")
        sys.exit(1)
        
    project_root = sys.argv[1]
    manager = MeshrProjectManager(project_root)
    
    try:
        config = manager.load_config()
        print(f"Project: {config.name} v{config.version}")
        print(f"Module: {config.module_name}")
        print(f"Dependencies: {list(config.dependencies.keys())}")
        
        modules = manager.resolve_dependencies()
        print(f"\nLoaded modules: {list(modules.keys())}")
        
        for module_name, module_info in modules.items():
            print(f"\nModule: {module_name}")
            print(f"  Exports: {module_info.exports}")
            print(f"  Imports: {module_info.imports}")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
