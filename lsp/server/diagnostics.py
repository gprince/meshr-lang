"""
Diagnostics et validation pour Meshr-Lang
"""

import logging
from typing import List, Optional, Any
from lsprotocol.types import Diagnostic, Position, Range, DiagnosticSeverity
from .semantic_validator import SemanticValidator

logger = logging.getLogger(__name__)

class MeshrDiagnostics:
    """Générateur de diagnostics pour Meshr-Lang"""
    
    def __init__(self, parser):
        self.parser = parser
        self.semantic_validator = SemanticValidator()
    
    def analyze(self, tree: Optional[Any], uri: str, text: str = "") -> List[Diagnostic]:
        """
        Analyse l'arbre de syntaxe et génère les diagnostics
        
        Args:
            tree: L'arbre de syntaxe abstraite
            uri: URI du document
            text: Le contenu du document (pour la validation sémantique)
            
        Returns:
            Liste des diagnostics
        """
        diagnostics = []
        
        if tree is None:
            # Erreur de parsing générale
            diagnostics.append(Diagnostic(
                range=Range(
                    start=Position(line=0, character=0),
                    end=Position(line=0, character=0)
                ),
                message="Erreur de parsing du fichier",
                severity=DiagnosticSeverity.Error,
                source="meshr-lang"
            ))
            return diagnostics
        
        # Analyser l'arbre pour détecter les erreurs de syntaxe
        diagnostics.extend(self._analyze_tree(tree))
        
        # Ajouter la validation sémantique si le texte est fourni
        if text:
            semantic_diagnostics = self.semantic_validator.validate(text)
            diagnostics.extend(semantic_diagnostics)
        
        return diagnostics
    
    def _analyze_tree(self, tree: Any) -> List[Diagnostic]:
        """Analyse récursive de l'arbre de syntaxe"""
        diagnostics = []
        
        # Récupérer les erreurs de syntaxe du parser
        syntax_errors = self.parser.get_syntax_errors()
        if syntax_errors:
            diagnostics.extend(self._extract_syntax_errors(syntax_errors))
        
        return diagnostics
    
    def _extract_syntax_errors(self, syntax_errors: List[dict]) -> List[Diagnostic]:
        """Extrait les erreurs de syntaxe de l'arbre ANTLR"""
        diagnostics = []
        
        for error in syntax_errors:
            # Convertir les numéros de ligne (ANTLR commence à 1, LSP à 0)
            line = error['line'] - 1 if error['line'] > 0 else 0
            column = error['column']
            
            diagnostics.append(Diagnostic(
                range=Range(
                    start=Position(line=line, character=column),
                    end=Position(line=line, character=column + 1)
                ),
                message=error['message'],
                severity=DiagnosticSeverity.Error,
                source="meshr-lang"
            ))
        
        return diagnostics
    
    def validate_syntax(self, text: str) -> List[Diagnostic]:
        """
        Valide la syntaxe d'un texte Meshr-Lang
        
        Args:
            text: Le texte à valider
            
        Returns:
            Liste des diagnostics de validation
        """
        diagnostics = []
        
        # Vérifications basiques
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line_num = i + 1
            
            # Vérifier les erreurs communes
            if line.strip().startswith('module') and not line.strip().endswith(';'):
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=line_num-1, character=0),
                        end=Position(line=line_num-1, character=len(line))
                    ),
                    message="Déclaration de module doit se terminer par ';'",
                    severity=DiagnosticSeverity.Error,
                    source="meshr-lang"
                ))
            
            # Vérifier les imports
            if line.strip().startswith('import') and not line.strip().endswith(';'):
                diagnostics.append(Diagnostic(
                    range=Range(
                        start=Position(line=line_num-1, character=0),
                        end=Position(line=line_num-1, character=len(line))
                    ),
                    message="Import doit se terminer par ';'",
                    severity=DiagnosticSeverity.Error,
                    source="meshr-lang"
                ))
            
            # Vérifier les annotations
            if '@' in line and not line.strip().startswith('@'):
                # Vérifier si c'est une annotation mal placée
                if line.strip().startswith('entity') or line.strip().startswith('enum'):
                    diagnostics.append(Diagnostic(
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        message="Les annotations doivent être placées avant la déclaration",
                        severity=DiagnosticSeverity.Warning,
                        source="meshr-lang"
                    ))
        
        return diagnostics
