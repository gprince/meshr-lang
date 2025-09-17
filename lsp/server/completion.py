"""
Autocomplétion pour Meshr-Lang
"""

import logging
from typing import List, Optional, Dict, Any
from lsprotocol.types import (
    CompletionItem, CompletionItemKind, Position, Range,
    Hover, MarkupContent, MarkupKind
)
from pygls.workspace import Document

logger = logging.getLogger(__name__)

class MeshrCompletion:
    """Générateur d'autocomplétion pour Meshr-Lang"""
    
    def __init__(self, parser):
        self.parser = parser
        
        # Mots-clés Meshr-Lang
        self.keywords = {
            'module', 'import', 'entity', 'enum', 'trait', 'aspect',
            'relation', 'sealed', 'export', 'of', 'extends', 'implements',
            'metric', 'source', 'calculation', 'aggregation', 'unit', 
            'outputs', 'dimensions', 'filters', 'temporal', 'window',
            'refresh_frequency', 'historical_depth', 'match', 'or',
            'String', 'Number', 'Boolean', 'Bytes', 'List', 'Map',
            'true', 'false', 'null'
        }
        
        # Types primitifs
        self.primitive_types = {
            'String', 'Number', 'Boolean', 'Bytes', 'List', 'Map'
        }
        
        # Annotations communes
        self.annotations = {
            '@Documented', '@Deprecated', '@Override', '@SuppressWarnings',
            '@Validated', '@Required', '@Optional', '@Default'
        }
    
    def get_completions(self, doc: Document, position: Position) -> List[CompletionItem]:
        """
        Génère les suggestions d'autocomplétion
        
        Args:
            doc: Le document courant
            position: Position du curseur
            
        Returns:
            Liste des éléments d'autocomplétion
        """
        completions = []
        
        # Obtenir le contexte autour de la position
        line = doc.lines[position.line] if position.line < len(doc.lines) else ""
        before_cursor = line[:position.character]
        
        # Déterminer le type de complétion
        if before_cursor.strip().endswith('@'):
            # Complétion d'annotations
            completions.extend(self._get_annotation_completions())
        
        elif before_cursor.strip().endswith('import '):
            # Complétion d'imports
            completions.extend(self._get_import_completions())
        
        elif before_cursor.strip().endswith('module '):
            # Complétion de noms de modules
            completions.extend(self._get_module_completions())
        
        elif before_cursor.strip().endswith('entity ') or before_cursor.strip().endswith('enum '):
            # Complétion de noms d'entités/énumérations
            completions.extend(self._get_entity_completions())
        
        elif before_cursor.strip().endswith('extends ') or before_cursor.strip().endswith('implements '):
            # Complétion de types
            completions.extend(self._get_type_completions())
        
        else:
            # Complétion générale
            completions.extend(self._get_general_completions())
        
        return completions
    
    def _get_annotation_completions(self) -> List[CompletionItem]:
        """Complétion pour les annotations"""
        completions = []
        
        for annotation in self.annotations:
            completions.append(CompletionItem(
                label=annotation,
                kind=CompletionItemKind.Class,
                detail="Annotation",
                documentation=f"Annotation {annotation} pour Meshr-Lang"
            ))
        
        return completions
    
    def _get_import_completions(self) -> List[CompletionItem]:
        """Complétion pour les imports"""
        completions = []
        
        # Imports de la stdlib
        stdlib_modules = [
            'core.types', 'core.annotations', 'core.governance',
            'core.lifecycle', 'core.security'
        ]
        
        for module in stdlib_modules:
            completions.append(CompletionItem(
                label=module,
                kind=CompletionItemKind.Module,
                detail="Module stdlib",
                documentation=f"Import du module {module} de la bibliothèque standard"
            ))
        
        return completions
    
    def _get_module_completions(self) -> List[CompletionItem]:
        """Complétion pour les noms de modules"""
        completions = []
        
        # Suggestions de noms de modules
        suggestions = [
            'com.example', 'org.company', 'net.domain',
            'business', 'analytics', 'governance'
        ]
        
        for suggestion in suggestions:
            completions.append(CompletionItem(
                label=suggestion,
                kind=CompletionItemKind.Module,
                detail="Nom de module",
                documentation=f"Nom de module suggéré: {suggestion}"
            ))
        
        return completions
    
    def _get_entity_completions(self) -> List[CompletionItem]:
        """Complétion pour les noms d'entités"""
        completions = []
        
        # Suggestions de noms d'entités
        suggestions = [
            'User', 'Product', 'Order', 'Customer', 'Account',
            'Employee', 'Department', 'Project', 'Task'
        ]
        
        for suggestion in suggestions:
            completions.append(CompletionItem(
                label=suggestion,
                kind=CompletionItemKind.Class,
                detail="Entité",
                documentation=f"Nom d'entité suggéré: {suggestion}"
            ))
        
        return completions
    
    def _get_type_completions(self) -> List[CompletionItem]:
        """Complétion pour les types"""
        completions = []
        
        # Types primitifs
        for type_name in self.primitive_types:
            completions.append(CompletionItem(
                label=type_name,
                kind=CompletionItemKind.Class,
                detail="Type primitif",
                documentation=f"Type primitif: {type_name}"
            ))
        
        return completions
    
    def _get_general_completions(self) -> List[CompletionItem]:
        """Complétion générale"""
        completions = []
        
        # Mots-clés
        for keyword in self.keywords:
            completions.append(CompletionItem(
                label=keyword,
                kind=CompletionItemKind.Keyword,
                detail="Mot-clé",
                documentation=f"Mot-clé Meshr-Lang: {keyword}"
            ))
        
        return completions
    
    def get_hover(self, doc: Document, position: Position) -> Optional[Hover]:
        """
        Génère l'information au survol
        
        Args:
            doc: Le document courant
            position: Position du curseur
            
        Returns:
            Information de survol ou None
        """
        line = doc.lines[position.line] if position.line < len(doc.lines) else ""
        
        # Trouver le mot sous le curseur
        word_start = position.character
        word_end = position.character
        
        # Étendre vers la gauche
        while word_start > 0 and line[word_start - 1].isalnum():
            word_start -= 1
        
        # Étendre vers la droite
        while word_end < len(line) and line[word_end].isalnum():
            word_end += 1
        
        word = line[word_start:word_end]
        
        if not word:
            return None
        
        # Générer l'information de survol
        hover_info = self._get_hover_info(word)
        
        if hover_info:
            return Hover(
                contents=MarkupContent(
                    kind=MarkupKind.Markdown,
                    value=hover_info
                ),
                range=Range(
                    start=Position(line=position.line, character=word_start),
                    end=Position(line=position.line, character=word_end)
                )
            )
        
        return None
    
    def _get_hover_info(self, word: str) -> Optional[str]:
        """Génère l'information de survol pour un mot"""
        
        if word in self.keywords:
            return f"**{word}**\n\nMot-clé Meshr-Lang"
        
        elif word in self.primitive_types:
            return f"**{word}**\n\nType primitif Meshr-Lang"
        
        elif word.startswith('@'):
            return f"**{word}**\n\nAnnotation Meshr-Lang"
        
        return None
