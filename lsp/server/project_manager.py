"""
Project Manager pour le LSP Meshr-Lang
======================================
Gestion des projets, résolution de dépendances et support des imports
pour le Language Server Protocol.
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from meshr_project import MeshrProjectManager, ModuleInfo, ProjectConfig

@dataclass
class LSPProjectInfo:
    """Information de projet pour le LSP"""
    project_root: str
    config: ProjectConfig
    modules: Dict[str, ModuleInfo]
    symbol_index: Dict[str, Dict[str, Any]]  # symbol -> {module, type, location}

class LSPProjectManager:
    """Gestionnaire de projet pour le LSP"""
    
    def __init__(self):
        self.projects: Dict[str, LSPProjectInfo] = {}
        self.workspace_roots: Set[str] = set()
        self.global_symbol_index: Dict[str, Dict[str, Any]] = {}
        
    def add_workspace_root(self, root_path: str):
        """Ajoute une racine de workspace et charge les projets"""
        self.workspace_roots.add(root_path)
        self._discover_projects(root_path)
        
    def _discover_projects(self, root_path: str):
        """Découvre les projets Meshr-Lang dans un répertoire"""
        root = Path(root_path)
        
        # Chercher meshr.toml dans le répertoire racine
        config_file = root / "meshr.toml"
        if config_file.exists():
            self._load_project(str(root))
            
        # Chercher dans les sous-répertoires
        for item in root.iterdir():
            if item.is_dir():
                sub_config = item / "meshr.toml"
                if sub_config.exists():
                    self._load_project(str(item))
                    
    def _load_project(self, project_root: str):
        """Charge un projet Meshr-Lang"""
        import logging
        logger = logging.getLogger(__name__)
        
        try:
            logger.info(f"🔧 Chargement du projet: {project_root}")
            manager = MeshrProjectManager(project_root)
            config = manager.load_config()
            logger.info(f"🔧 Config chargée: {config.name}")
            
            # Essayer de résoudre les dépendances, mais ignorer les erreurs de module principal
            try:
                modules = manager.resolve_dependencies()
                logger.info(f"🔧 Modules résolus: {list(modules.keys())}")
            except Exception as dep_error:
                logger.warning(f"⚠️ Erreur lors de la résolution des dépendances: {dep_error}")
                # Essayer de charger seulement les modules définis dans la config
                modules = self._load_modules_from_config(manager, config)
                logger.info(f"🔧 Modules chargés depuis la config: {list(modules.keys())}")
                
                # Essayer de charger les dépendances manuellement
                try:
                    self._load_dependencies_manually(manager, config, modules)
                    logger.info(f"🔧 Dépendances chargées manuellement: {list(modules.keys())}")
                except Exception as dep_manual_error:
                    logger.warning(f"⚠️ Erreur lors du chargement manuel des dépendances: {dep_manual_error}")
            
            # S'assurer que le module principal est chargé même en cas d'erreur
            if config.module_name and config.module_path and config.module_name not in modules:
                try:
                    module_path = manager.project_root / config.module_path
                    if module_path.exists() and module_path.is_file():
                        manager._load_module(module_path, config.module_name)
                        modules[config.module_name] = manager.modules[config.module_name]
                        logger.info(f"🔧 Module principal chargé (fallback): {config.module_name} depuis {module_path}")
                except Exception as e:
                    logger.warning(f"⚠️ Erreur lors du chargement du module principal (fallback): {e}")
            
            # Construire l'index des symboles
            symbol_index = self._build_symbol_index(modules)
            logger.info(f"🔧 Index construit avec {len(symbol_index)} symboles: {list(symbol_index.keys())}")
            
            project_info = LSPProjectInfo(
                project_root=project_root,
                config=config,
                modules=modules,
                symbol_index=symbol_index
            )
            
            # Ajouter les symboles à l'index global
            self.global_symbol_index.update(symbol_index)
            
            self.projects[project_root] = project_info
            logger.info(f"✅ Projet chargé: {config.name} à {project_root}")
            
        except Exception as e:
            logger.error(f"❌ Erreur lors du chargement du projet {project_root}: {e}")
            import traceback
            traceback.print_exc()
            
    def _load_modules_from_config(self, manager, config) -> Dict[str, Any]:
        """Charge les modules directement depuis la configuration"""
        import logging
        logger = logging.getLogger(__name__)
        modules = {}
        
        # Charger le module principal défini dans [project.module]
        if config.module_name and config.module_path:
            try:
                module_name = config.module_name
                module_path = manager.project_root / config.module_path
                if module_path.exists() and module_path.is_file():
                    manager._load_module(module_path, module_name)
                    modules[module_name] = manager.modules[module_name]
                    logger.info(f"🔧 Module principal chargé: {module_name} depuis {module_path}")
                else:
                    logger.warning(f"⚠️ Module principal non trouvé: {module_path}")
            except Exception as e:
                logger.warning(f"⚠️ Erreur lors du chargement du module principal: {e}")
        
        # Charger les modules définis dans la section [modules]
        if config.modules:
            for module_name, module_config in config.modules.items():
                try:
                    module_path = manager.project_root / module_config['path']
                    if module_path.exists() and module_path.is_file():
                        manager._load_module(module_path, module_name)
                        modules[module_name] = manager.modules[module_name]
                        logger.info(f"🔧 Module chargé: {module_name} depuis {module_path}")
                except Exception as e:
                    logger.warning(f"⚠️ Erreur lors du chargement du module {module_name}: {e}")
        
        return modules
    
    def _load_dependencies_manually(self, manager: MeshrProjectManager, config, modules: Dict[str, ModuleInfo]):
        """Charge les dépendances manuellement en cas d'échec de la résolution automatique"""
        import logging
        logger = logging.getLogger(__name__)
        
        # Charger les dépendances définies dans [dependencies]
        if config.dependencies:
            for dep_name, dep_config in config.dependencies.items():
                if 'path' in dep_config:
                    try:
                        dep_path = manager.project_root / dep_config['path']
                        logger.info(f"🔧 Chargement de la dépendance: {dep_name} depuis {dep_path}")
                        
                        # Charger la configuration de la dépendance
                        dep_config_file = dep_path / "meshr.toml"
                        if dep_config_file.exists():
                            import toml
                            with open(dep_config_file, 'r', encoding='utf-8') as f:
                                dep_data = toml.load(f)
                            
                            # Charger les modules de la dépendance
                            dep_modules = dep_data.get('modules', {})
                            for module_name, module_config in dep_modules.items():
                                try:
                                    module_path = dep_path / module_config['path']
                                    if module_path.exists() and module_path.is_file():
                                        manager._load_module(module_path, module_name)
                                        modules[module_name] = manager.modules[module_name]
                                        logger.info(f"🔧 Module de dépendance chargé: {module_name} depuis {module_path}")
                                except Exception as e:
                                    logger.warning(f"⚠️ Erreur lors du chargement du module de dépendance {module_name}: {e}")
                        else:
                            logger.warning(f"⚠️ Fichier de configuration de dépendance non trouvé: {dep_config_file}")
                    except Exception as e:
                        logger.warning(f"⚠️ Erreur lors du chargement de la dépendance {dep_name}: {e}")
            
    def _build_symbol_index(self, modules: Dict[str, ModuleInfo]) -> Dict[str, Dict[str, Any]]:
        """Construit un index des symboles pour la recherche rapide"""
        index = {}
        
        import logging
        logger = logging.getLogger(__name__)
        
        for module_name, module_info in modules.items():
            logger.info(f"🔧 Indexation du module: {module_name}")
            logger.info(f"🔧 Exports: {module_info.exports}")
            logger.info(f"🔧 Chemin: {module_info.path}")
            
            # Extraire les symboles avec leur localisation exacte
            symbol_locations = self._extract_symbol_locations(module_info.path)
            logger.info(f"🔧 Localisations trouvées: {symbol_locations}")
            
            for symbol in module_info.exports:
                if symbol in symbol_locations:
                    index[symbol] = {
                        "module": module_name,
                        "type": symbol_locations[symbol].get("type", "export"),
                        "location": module_info.path,
                        "line": symbol_locations[symbol]["line"],
                        "character": symbol_locations[symbol].get("character", 0)
                    }
                    logger.info(f"🔧 Symbole indexé: {symbol} -> ligne {symbol_locations[symbol]['line']}")
                else:
                    # Fallback si on ne trouve pas la localisation exacte
                    index[symbol] = {
                        "module": module_name,
                        "type": "export",
                        "location": module_info.path,
                        "line": 0,
                        "character": 0
                    }
                    logger.info(f"🔧 Symbole indexé (fallback): {symbol}")
                
        return index
        
    def _extract_symbol_locations(self, file_path: str) -> Dict[str, Dict[str, Any]]:
        """Extrait les localisations exactes des symboles dans un fichier"""
        locations = {}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            for line_num, line in enumerate(lines):
                line = line.strip()
                
                # Détecter les déclarations d'entités
                if line.startswith('entity '):
                    parts = line.split()
                    if len(parts) >= 2:
                        entity_name = parts[1]
                        locations[entity_name] = {
                            "type": "entity",
                            "line": line_num,
                            "character": line.find(entity_name)
                        }
                
                # Détecter les déclarations de traits
                elif line.startswith('trait '):
                    parts = line.split()
                    if len(parts) >= 2:
                        trait_name = parts[1]
                        locations[trait_name] = {
                            "type": "trait", 
                            "line": line_num,
                            "character": line.find(trait_name)
                        }
                
                # Détecter les déclarations d'aspects
                elif line.startswith('aspect '):
                    parts = line.split()
                    if len(parts) >= 2:
                        aspect_name = parts[1]
                        locations[aspect_name] = {
                            "type": "aspect",
                            "line": line_num,
                            "character": line.find(aspect_name)
                        }
                
                # Détecter les déclarations d'énumérations
                elif line.startswith('enum '):
                    parts = line.split()
                    if len(parts) >= 2:
                        enum_name = parts[1]
                        locations[enum_name] = {
                            "type": "enum",
                            "line": line_num,
                            "character": line.find(enum_name)
                        }
                
                # Détecter les déclarations d'annotations
                elif line.startswith('annotation '):
                    parts = line.split()
                    if len(parts) >= 2:
                        annotation_name = parts[1]
                        locations[annotation_name] = {
                            "type": "annotation",
                            "line": line_num,
                            "character": line.find(annotation_name)
                        }
                
        except Exception as e:
            print(f"Erreur lors de l'extraction des symboles de {file_path}: {e}")
            
        return locations
        
    def find_project_for_file(self, file_path: str) -> Optional[LSPProjectInfo]:
        """Trouve le projet qui contient un fichier"""
        file_path = Path(file_path).resolve()
        
        for project_root, project_info in self.projects.items():
            project_root_path = Path(project_root).resolve()
            try:
                file_path.relative_to(project_root_path)
                return project_info
            except ValueError:
                continue
                
        return None
        
    def resolve_symbol(self, file_path: str, symbol: str) -> Optional[Dict[str, Any]]:
        """Résout un symbole et retourne ses informations"""
        print(f"🔍 resolve_symbol: {symbol} dans {file_path}")
        
        project = self.find_project_for_file(file_path)
        if not project:
            print(f"🔍 Aucun projet trouvé pour {file_path}")
            return None
            
        print(f"🔍 Projet trouvé: {project.project_root}")
        print(f"🔍 Index global contient {len(self.global_symbol_index)} symboles: {list(self.global_symbol_index.keys())}")
            
        # Chercher dans l'index global des symboles
        if symbol in self.global_symbol_index:
            result = self.global_symbol_index[symbol]
            print(f"🔍 Symbole trouvé dans l'index global: {result}")
            return result
            
        print(f"🔍 Symbole '{symbol}' non trouvé dans l'index global")
            
        # Si pas trouvé, essayer de résoudre via les dépendances
        # Trouver le module du fichier courant
        file_path_obj = Path(file_path)
        for module_name, module_info in project.modules.items():
            if Path(module_info.path).resolve() == file_path_obj.resolve():
                print(f"🔍 Module trouvé: {module_name}")
                # Utiliser le MeshrProjectManager pour résoudre
                meshr_manager = MeshrProjectManager(project.project_root)
                meshr_manager.load_config()
                meshr_manager.resolve_dependencies()
                result = meshr_manager.resolve_import(module_name, symbol)
                if result:
                    print(f"🔍 Résolution via dépendances: {result}")
                    return {
                        "module": module_name,
                        "type": "import",
                        "location": result[0],
                        "line": 0
                    }
                break
                
        return None
        
    def get_completion_items(self, file_path: str, module_name: str) -> List[Dict[str, Any]]:
        """Retourne les éléments de complétion pour un module"""
        project = self.find_project_for_file(file_path)
        if not project:
            return []
            
        completions = []
        
        # Symboles du module lui-même
        if module_name in project.modules:
            module_info = project.modules[module_name]
            for symbol in module_info.exports:
                completions.append({
                    "label": symbol,
                    "kind": "Variable",  # TODO: Détecter le type exact
                    "detail": f"From {module_name}",
                    "documentation": f"Exported from {module_name}"
                })
                
        # Symboles des dépendances
        if module_name in project.modules:
            module_info = project.modules[module_name]
            for dep in module_info.dependencies:
                if dep in project.modules:
                    dep_module = project.modules[dep]
                    for symbol in dep_module.exports:
                        completions.append({
                            "label": symbol,
                            "kind": "Variable",
                            "detail": f"From {dep}",
                            "documentation": f"Imported from {dep}"
                        })
                        
        return completions
        
    def validate_imports(self, file_path: str) -> List[Dict[str, Any]]:
        """Valide les imports d'un fichier"""
        project = self.find_project_for_file(file_path)
        if not project:
            return []
            
        # Trouver le module correspondant au fichier
        file_path_obj = Path(file_path)
        module_name = None
        
        for name, module_info in project.modules.items():
            if Path(module_info.path) == file_path_obj:
                module_name = name
                break
                
        if not module_name:
            return []
            
        # Valider les imports
        manager = MeshrProjectManager(project.project_root)
        manager.modules = project.modules
        return manager.validate_imports(module_name)
        
    def get_hover_info(self, file_path: str, symbol: str) -> Optional[Dict[str, Any]]:
        """Retourne les informations de hover pour un symbole"""
        symbol_info = self.resolve_symbol(file_path, symbol)
        if not symbol_info:
            return None
            
        return {
            "contents": {
                "kind": "markdown",
                "value": f"**{symbol}**\n\nExported from `{symbol_info['module']}`\n\nLocation: `{symbol_info['location']}`"
            }
        }
        
    def get_definition(self, file_path: str, symbol: str) -> Optional[Dict[str, Any]]:
        """Retourne la définition d'un symbole"""
        symbol_info = self.resolve_symbol(file_path, symbol)
        if not symbol_info:
            return None
            
        # Utiliser les informations de localisation exacte
        line = symbol_info.get('line', 0)
        character = symbol_info.get('character', 0)
        location = symbol_info.get('location', '')
        
        # S'assurer que l'URI est correctement formaté
        if location.startswith('file://'):
            uri = location
        else:
            # Convertir le chemin en URI file://
            uri = f"file://{location}"
        
        return {
            "uri": uri,
            "range": {
                "start": {"line": line, "character": character},
                "end": {"line": line, "character": character + len(symbol)}
            }
        }
        
    def get_references(self, file_path: str, symbol: str) -> List[Dict[str, Any]]:
        """Retourne les références d'un symbole"""
        # TODO: Implémenter la recherche de références
        return []
        
    def reload_project(self, project_root: str):
        """Recharge un projet"""
        if project_root in self.projects:
            del self.projects[project_root]
        self._load_project(project_root)
        
    def get_project_info(self, project_root: str) -> Optional[LSPProjectInfo]:
        """Retourne les informations d'un projet"""
        return self.projects.get(project_root)
