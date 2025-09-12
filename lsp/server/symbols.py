"""
Navigation et symboles pour Meshr-Lang
"""

import logging
from typing import List, Optional, Dict, Any
from lsprotocol.types import (
    DocumentSymbol, SymbolKind, Location, WorkspaceSymbol,
    Position, Range
)
from pygls.workspace import Document, Workspace

logger = logging.getLogger(__name__)

class MeshrSymbols:
    """Gestionnaire de symboles pour Meshr-Lang"""
    
    def __init__(self, parser):
        self.parser = parser
    
    def get_document_symbols(self, doc: Document) -> List[DocumentSymbol]:
        """
        Extrait les symboles d'un document
        
        Args:
            doc: Le document à analyser
            
        Returns:
            Liste des symboles du document
        """
        symbols = []
        
        try:
            lines = doc.lines
            
            for i, line in enumerate(lines):
                line_num = i + 1
                line_stripped = line.strip()
                
                # Module
                if line_stripped.startswith('module '):
                    module_name = line_stripped[7:].rstrip(';').strip()
                    symbols.append(DocumentSymbol(
                        name=module_name,
                        kind=SymbolKind.Module,
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        selection_range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        detail="Module Meshr-Lang"
                    ))
                
                # Import
                elif line_stripped.startswith('import '):
                    import_name = line_stripped[7:].rstrip(';').strip()
                    symbols.append(DocumentSymbol(
                        name=f"import {import_name}",
                        kind=SymbolKind.Namespace,
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        selection_range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        detail="Import"
                    ))
                
                # Entity
                elif line_stripped.startswith('entity '):
                    entity_name = line_stripped[7:].split()[0].rstrip('{').strip()
                    symbols.append(DocumentSymbol(
                        name=entity_name,
                        kind=SymbolKind.Class,
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        selection_range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        detail="Entité"
                    ))
                
                # Enum
                elif line_stripped.startswith('enum '):
                    enum_name = line_stripped[5:].split()[0].rstrip('{').strip()
                    symbols.append(DocumentSymbol(
                        name=enum_name,
                        kind=SymbolKind.Enum,
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        selection_range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        detail="Énumération"
                    ))
                
                # Trait
                elif line_stripped.startswith('trait '):
                    trait_name = line_stripped[6:].split()[0].rstrip('{').strip()
                    symbols.append(DocumentSymbol(
                        name=trait_name,
                        kind=SymbolKind.Interface,
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        selection_range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        detail="Trait"
                    ))
                
                # Aspect
                elif line_stripped.startswith('aspect '):
                    aspect_name = line_stripped[7:].split()[0].rstrip('{').strip()
                    symbols.append(DocumentSymbol(
                        name=aspect_name,
                        kind=SymbolKind.Class,
                        range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        selection_range=Range(
                            start=Position(line=line_num-1, character=0),
                            end=Position(line=line_num-1, character=len(line))
                        ),
                        detail="Aspect"
                    ))
        
        except Exception as e:
            logger.error(f"Erreur lors de l'extraction des symboles: {e}")
        
        return symbols
    
    def get_workspace_symbols(self, workspace: Workspace, query: str) -> List[WorkspaceSymbol]:
        """
        Recherche des symboles dans l'espace de travail
        
        Args:
            workspace: L'espace de travail
            query: Requête de recherche
            
        Returns:
            Liste des symboles trouvés
        """
        symbols = []
        
        try:
            # Parcourir tous les documents .meshr
            for doc_uri, doc in workspace._docs.items():
                if doc_uri.endswith('.meshr'):
                    doc_symbols = self.get_document_symbols(doc)
                    
                    # Filtrer selon la requête
                    for symbol in doc_symbols:
                        if query.lower() in symbol.name.lower():
                            symbols.append(WorkspaceSymbol(
                                name=symbol.name,
                                kind=symbol.kind,
                                location=Location(
                                    uri=doc_uri,
                                    range=symbol.range
                                )
                            ))
        
        except Exception as e:
            logger.error(f"Erreur lors de la recherche de symboles: {e}")
        
        return symbols
