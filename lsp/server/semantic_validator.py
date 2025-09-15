"""
Validateur sémantique pour Meshr-Lang
Implémente les règles fondamentales du langage qui ne sont pas déductibles du parser
"""

import logging
import re
from typing import List, Dict, Set, Optional
from lsprotocol.types import Diagnostic, Position, Range, DiagnosticSeverity

logger = logging.getLogger(__name__)

class SemanticValidator:
    """Validateur sémantique pour Meshr-Lang"""
    
    def __init__(self):
        self.imports = {}  # {module: [imported_items]}
        self.exports = {}  # {module: [exported_items]}
        self.declared_items = {}  # {module: [declared_items]}
        self.module_name = None
    
    def validate(self, text: str) -> List[Diagnostic]:
        """
        Valide les règles sémantiques du langage
        
        Args:
            text: Le contenu du fichier à valider
            
        Returns:
            Liste des diagnostics sémantiques
        """
        diagnostics = []
        lines = text.split('\n')
        
        # Phase 1: Analyser la structure du fichier
        self._analyze_structure(lines)
        
        # Phase 2: Valider les règles sémantiques
        diagnostics.extend(self._validate_imports(lines))
        diagnostics.extend(self._validate_exports(lines))
        diagnostics.extend(self._validate_module_structure(lines))
        diagnostics.extend(self._validate_naming_conventions(lines))
        
        return diagnostics
    
    def _analyze_structure(self, lines: List[str]):
        """Analyse la structure du fichier pour extraire les informations"""
        self.imports = {}
        self.exports = {}
        self.declared_items = {}
        self.module_name = None
        
        current_module = None
        
        for i, line in enumerate(lines):
            line_num = i + 1
            stripped = line.strip()
            
            # Détecter la déclaration du module
            if stripped.startswith('module '):
                match = re.match(r'module\s+([a-zA-Z_][a-zA-Z0-9_.]*)', stripped)
                if match:
                    self.module_name = match.group(1)
                    current_module = self.module_name
                    self.declared_items[current_module] = []
            
            # Détecter les imports
            elif stripped.startswith('import '):
                self._parse_import(line, line_num)
            
            # Détecter les exports
            elif stripped.startswith('export '):
                self._parse_export(line, line_num)
    
    def _parse_import(self, line: str, line_num: int):
        """Parse une ligne d'import"""
        # Format: import { item1, item2 } from module.name
        match = re.match(r'import\s*\{\s*([^}]+)\s*\}\s*from\s+([a-zA-Z_][a-zA-Z0-9_.]*)', line)
        if match:
            items_str = match.group(1)
            module = match.group(2)
            items = [item.strip() for item in items_str.split(',')]
            self.imports[module] = items
    
    def _parse_export(self, line: str, line_num: int):
        """Parse une ligne d'export"""
        # Format: export { item1, item2 } from module.name
        match = re.match(r'export\s*\{\s*([^}]+)\s*\}\s*from\s+([a-zA-Z_][a-zA-Z0-9_.]*)', line)
        if match:
            items_str = match.group(1)
            module = match.group(2)
            items = [item.strip() for item in items_str.split(',')]
            self.exports[module] = items
    
    def _validate_imports(self, lines: List[str]) -> List[Diagnostic]:
        """Valide les règles des imports"""
        diagnostics = []
        
        for i, line in enumerate(lines):
            line_num = i + 1
            stripped = line.strip()
            
            # Règle: Les imports doivent être après la déclaration du module
            if stripped.startswith('import ') and self.module_name:
                # Vérifier si l'import est avant la déclaration du module
                module_line = None
                for j, check_line in enumerate(lines):
                    if check_line.strip().startswith('module '):
                        module_line = j + 1
                        break
                
                if module_line and line_num < module_line:
                    diagnostics.append(Diagnostic(
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        message="Les imports doivent être placés après la déclaration du module",
                        severity=DiagnosticSeverity.Error,
                        source="meshr-lang-semantic"
                    ))
            
            # Règle: Vérifier la syntaxe des imports
            if stripped.startswith('import '):
                if not re.match(r'import\s*\{\s*[^}]+\s*\}\s*from\s+[a-zA-Z_][a-zA-Z0-9_.]*', stripped):
                    diagnostics.append(Diagnostic(
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        message="Syntaxe d'import invalide. Format attendu: import { item1, item2 } from module.name",
                        severity=DiagnosticSeverity.Error,
                        source="meshr-lang-semantic"
                    ))
        
        return diagnostics
    
    def _validate_exports(self, lines: List[str]) -> List[Diagnostic]:
        """Valide les règles des exports"""
        diagnostics = []
        
        for i, line in enumerate(lines):
            line_num = i + 1
            stripped = line.strip()
            
            # Règle: Vérifier la syntaxe des exports
            if stripped.startswith('export '):
                # Vérifier les formats d'export supportés par la grammaire :
                # 1. Export groupé: export { item1, item2 } (peut être multi-ligne)
                # 2. Export inline: export declaration
                if not (re.match(r'export\s*\{', stripped) or  # Export groupé (début)
                        re.match(r'export\s+[a-zA-Z_][a-zA-Z0-9_.]*', stripped)):  # Export inline
                    diagnostics.append(Diagnostic(
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        message="Syntaxe d'export invalide. Formats supportés: export { item1, item2 } ou export declaration",
                        severity=DiagnosticSeverity.Error,
                        source="meshr-lang-semantic"
                    ))
            
            # Règle: Détecter "exported" au lieu de "export"
            if stripped.startswith('exported '):
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=line_num-1, character=0),
                        end=Position(line=line_num-1, character=9)
                    ),
                    message="Mot-clé incorrect: 'exported' au lieu de 'export'",
                    severity=DiagnosticSeverity.Error,
                    source="meshr-lang-semantic"
                ))
        
        return diagnostics
    
    def _validate_module_structure(self, lines: List[str]) -> List[Diagnostic]:
        """Valide la structure du module"""
        diagnostics = []
        
        # Règle: Un fichier doit contenir exactement une déclaration de module
        module_declarations = []
        for i, line in enumerate(lines):
            if line.strip().startswith('module '):
                module_declarations.append(i + 1)
        
        if len(module_declarations) == 0:
            diagnostics.append(Diagnostic(
                range=Range(
                    start=Position(line=0, character=0),
                    end=Position(line=0, character=0)
                ),
                message="Fichier Meshr-Lang doit contenir une déclaration de module",
                severity=DiagnosticSeverity.Error,
                source="meshr-lang-semantic"
            ))
        elif len(module_declarations) > 1:
            for line_num in module_declarations[1:]:  # Toutes sauf la première
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=line_num-1, character=0),
                        end=Position(line=line_num-1, character=len(lines[line_num-1]))
                    ),
                    message="Déclaration de module en double. Un fichier ne peut contenir qu'un seul module",
                    severity=DiagnosticSeverity.Error,
                    source="meshr-lang-semantic"
                ))
        
        return diagnostics
    
    def _validate_naming_conventions(self, lines: List[str]) -> List[Diagnostic]:
        """Valide les conventions de nommage"""
        diagnostics = []
        
        for i, line in enumerate(lines):
            line_num = i + 1
            stripped = line.strip()
            
            # Règle: Les noms de modules doivent être des identifiants valides
            if stripped.startswith('module '):
                match = re.match(r'module\s+([a-zA-Z_][a-zA-Z0-9_.]*)', stripped)
                if not match:
                    diagnostics.append(Diagnostic(
                        range=Range(
                            start=Position(line=line_num-1, character=7),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        message="Nom de module invalide. Doit être un identifiant valide",
                        severity=DiagnosticSeverity.Error,
                        source="meshr-lang-semantic"
                    ))
            
            # Règle: Détecter les caractères invalides dans les identifiants
            if re.search(r'[^a-zA-Z0-9_.\s{}@(),;:"\'\-]', stripped):
                # Vérifier si c'est dans un contexte d'identifiant
                if any(keyword in stripped for keyword in ['module', 'import', 'export', 'entity', 'enum', 'annotation']):
                    invalid_chars = re.findall(r'[^a-zA-Z0-9_.\s{}@(),;:"\'\-]', stripped)
                    for char in invalid_chars:
                        if char not in ['$', '!', '%', '£', '^', '`', 'ô', '¨']:  # Caractères déjà détectés par le lexer
                            continue
                        char_pos = stripped.find(char)
                        diagnostics.append(Diagnostic(
                            range=Range(
                                start=Position(line=line_num-1, character=char_pos),
                                end=Position(line=line_num-1, character=char_pos+1)
                            ),
                            message=f"Caractère invalide dans l'identifiant: '{char}'",
                            severity=DiagnosticSeverity.Error,
                            source="meshr-lang-semantic"
                        ))
        
        return diagnostics
