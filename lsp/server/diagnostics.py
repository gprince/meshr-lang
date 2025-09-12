"""
Diagnostics et validation pour Meshr-Lang
"""

import logging
from typing import List, Optional, Any
from lsprotocol.types import Diagnostic, Position, Range, DiagnosticSeverity

logger = logging.getLogger(__name__)

class MeshrDiagnostics:
    """Générateur de diagnostics pour Meshr-Lang"""
    
    def __init__(self, parser):
        self.parser = parser
    
    def analyze(self, tree: Optional[Any], uri: str) -> List[Diagnostic]:
        """
        Analyse l'arbre de syntaxe et génère les diagnostics
        
        Args:
            tree: L'arbre de syntaxe abstraite
            uri: URI du document
            
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
        
        # Analyser l'arbre pour détecter les erreurs
        diagnostics.extend(self._analyze_tree(tree))
        
        return diagnostics
    
    def _analyze_tree(self, tree: Any) -> List[Diagnostic]:
        """Analyse récursive de l'arbre de syntaxe"""
        diagnostics = []
        
        # TODO: Implémenter l'analyse spécifique selon le type de nœud
        # Pour l'instant, on retourne une liste vide
        
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
