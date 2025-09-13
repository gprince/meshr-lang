"""
Validation des modules, imports et exports pour Meshr-Lang
"""

import logging
import re
from typing import List, Dict, Set, Optional, Any, Tuple
from pathlib import Path
from lsprotocol.types import Diagnostic, Position, Range, DiagnosticSeverity

logger = logging.getLogger(__name__)

class ModuleInfo:
    """Informations sur un module"""
    
    def __init__(self, name: str, file_path: str):
        self.name = name
        self.file_path = file_path
        self.exports: Set[str] = set()
        self.imports: List[Tuple[str, List[str]]] = []  # (module, [items])
        self.declarations: Dict[str, str] = {}  # {name: type}
        self.exported_declarations: Set[str] = set()
    
    def add_export(self, name: str, declaration_type: str):
        """Ajoute une déclaration exportée"""
        self.exports.add(name)
        self.declarations[name] = declaration_type
        self.exported_declarations.add(name)
    
    def add_import(self, module: str, items: List[str]):
        """Ajoute un import"""
        self.imports.append((module, items))
    
    def add_declaration(self, name: str, declaration_type: str):
        """Ajoute une déclaration locale"""
        self.declarations[name] = declaration_type

class ModuleValidator:
    """Validateur de modules pour Meshr-Lang"""
    
    def __init__(self, workspace_root: str):
        self.workspace_root = Path(workspace_root)
        self.modules: Dict[str, ModuleInfo] = {}
        self.module_files: Dict[str, str] = {}  # {module_name: file_path}
    
    def analyze_file(self, file_path: str, content: str) -> ModuleInfo:
        """Analyse un fichier et retourne les informations du module"""
        module_info = self._parse_module_content(content, file_path)
        self.modules[module_info.name] = module_info
        self.module_files[module_info.name] = file_path
        return module_info
    
    def validate_imports_exports(self, module_info: ModuleInfo) -> List[Diagnostic]:
        """Valide les imports et exports d'un module"""
        diagnostics = []
        
        # Valider les imports
        for module_name, imported_items in module_info.imports:
            diagnostics.extend(self._validate_import(module_info, module_name, imported_items))
        
        # Valider les exports
        diagnostics.extend(self._validate_exports(module_info))
        
        return diagnostics
    
    def _parse_module_content(self, content: str, file_path: str) -> ModuleInfo:
        """Parse le contenu d'un fichier pour extraire les informations du module"""
        lines = content.split('\n')
        module_info = None
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Détecter la déclaration du module
            module_match = re.match(r'module\s+(\S+)', line)
            if module_match and module_info is None:
                module_name = module_match.group(1)
                module_info = ModuleInfo(module_name, file_path)
                continue
            
            if module_info is None:
                continue
            
            # Détecter les imports
            import_match = re.match(r'import\s*\{\s*([^}]+)\s*\}\s*from\s+(\S+)', line)
            if import_match:
                items_str = import_match.group(1)
                module_name = import_match.group(2)
                items = [item.strip() for item in items_str.split(',')]
                module_info.add_import(module_name, items)
                continue
            
            # Détecter les exports
            export_match = re.match(r'export\s+(annotation|enum|aspect|entity|trait|record|collection|composite)\s+(\w+)', line)
            if export_match:
                declaration_type = export_match.group(1)
                name = export_match.group(2)
                module_info.add_export(name, declaration_type)
                continue
            
            # Détecter les déclarations non exportées
            decl_match = re.match(r'(annotation|enum|aspect|entity|trait|record|collection|composite)\s+(\w+)', line)
            if decl_match:
                declaration_type = decl_match.group(1)
                name = decl_match.group(2)
                module_info.add_declaration(name, declaration_type)
                continue
        
        if module_info is None:
            # Créer un module par défaut si aucune déclaration n'est trouvée
            module_info = ModuleInfo("unknown", file_path)
        
        return module_info
    
    def _validate_import(self, module_info: ModuleInfo, module_name: str, imported_items: List[str]) -> List[Diagnostic]:
        """Valide un import spécifique"""
        diagnostics = []
        
        # Vérifier si le module existe
        if module_name not in self.modules:
            # Essayer de résoudre le module depuis le système de fichiers
            resolved_module = self._resolve_module_path(module_name)
            if resolved_module is None:
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=0, character=0),
                        end=Position(line=0, character=0)
                    ),
                    message=f"Module '{module_name}' non trouvé",
                    severity=DiagnosticSeverity.Error,
                    source="meshr-lang"
                ))
                return diagnostics
            else:
                # Charger le module résolu
                self._load_module_from_path(resolved_module)
        
        # Vérifier si le module a été chargé
        if module_name not in self.modules:
            diagnostics.append(Diagnostic(
                range=Range(
                    start=Position(line=0, character=0),
                    end=Position(line=0, character=0)
                ),
                message=f"Impossible de charger le module '{module_name}'",
                severity=DiagnosticSeverity.Error,
                source="meshr-lang"
            ))
            return diagnostics
        
        target_module = self.modules[module_name]
        
        # Vérifier chaque élément importé
        for item in imported_items:
            if item not in target_module.exports:
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=0, character=0),
                        end=Position(line=0, character=0)
                    ),
                    message=f"'{item}' n'est pas exporté par le module '{module_name}'",
                    severity=DiagnosticSeverity.Error,
                    source="meshr-lang"
                ))
        
        return diagnostics
    
    def _validate_exports(self, module_info: ModuleInfo) -> List[Diagnostic]:
        """Valide les exports d'un module"""
        diagnostics = []
        
        # Vérifier que tous les exports existent
        for export_name in module_info.exports:
            if export_name not in module_info.declarations:
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=0, character=0),
                        end=Position(line=0, character=0)
                    ),
                    message=f"Export '{export_name}' non déclaré dans le module",
                    severity=DiagnosticSeverity.Error,
                    source="meshr-lang"
                ))
        
        return diagnostics
    
    def _resolve_module_path(self, module_name: str) -> Optional[str]:
        """Résout le chemin d'un module depuis son nom"""
        # Convertir le nom du module en chemin de fichier
        module_path = module_name.replace('.', '/')
        
        # Essayer différentes extensions
        for ext in ['.meshr', '/index.meshr']:
            full_path = self.workspace_root / f"{module_path}{ext}"
            if full_path.exists():
                return str(full_path)
        
        return None
    
    def _load_module_from_path(self, file_path: str):
        """Charge un module depuis un chemin de fichier"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            module_info = self._parse_module_content(content, file_path)
            self.modules[module_info.name] = module_info
            self.module_files[module_info.name] = file_path
            
        except Exception as e:
            logger.error(f"Erreur lors du chargement du module {file_path}: {e}")
    
    def get_module_dependencies(self, module_name: str) -> Set[str]:
        """Retourne les dépendances d'un module"""
        if module_name not in self.modules:
            return set()
        
        dependencies = set()
        module_info = self.modules[module_name]
        
        for imported_module, _ in module_info.imports:
            dependencies.add(imported_module)
            # Récursion pour les dépendances transitives
            dependencies.update(self.get_module_dependencies(imported_module))
        
        return dependencies
    
    def validate_circular_dependencies(self) -> List[Diagnostic]:
        """Valide qu'il n'y a pas de dépendances circulaires"""
        diagnostics = []
        
        for module_name in self.modules:
            if self._has_circular_dependency(module_name, set(), set()):
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=0, character=0),
                        end=Position(line=0, character=0)
                    ),
                    message=f"Dépendance circulaire détectée pour le module '{module_name}'",
                    severity=DiagnosticSeverity.Error,
                    source="meshr-lang"
                ))
        
        return diagnostics
    
    def _has_circular_dependency(self, module_name: str, visited: Set[str], rec_stack: Set[str]) -> bool:
        """Vérifie s'il y a une dépendance circulaire"""
        if module_name not in self.modules:
            return False
        
        visited.add(module_name)
        rec_stack.add(module_name)
        
        module_info = self.modules[module_name]
        for imported_module, _ in module_info.imports:
            if imported_module not in visited:
                if self._has_circular_dependency(imported_module, visited, rec_stack):
                    return True
            elif imported_module in rec_stack:
                return True
        
        rec_stack.remove(module_name)
        return False
