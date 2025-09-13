"""
Serveur Language Server Protocol pour Meshr-Lang
"""

import logging
from typing import List, Optional, Dict, Any
from pathlib import Path

from pygls.server import LanguageServer
from lsprotocol.types import (
    InitializeParams, InitializeResult, ServerCapabilities,
    TextDocumentSyncKind, CompletionOptions, CompletionItem,
    Diagnostic, Position, Range, TextDocumentItem,
    Hover, MarkupContent, MarkupKind,
    DocumentSymbol, SymbolKind, Location, WorkspaceSymbol
)
from pygls.workspace import Document

from .parser import MeshrParser
from .diagnostics import MeshrDiagnostics
from .completion import MeshrCompletion
from .symbols import MeshrSymbols
from .module_validation import ModuleValidator

logger = logging.getLogger(__name__)

class MeshrLanguageServer(LanguageServer):
    """Serveur LSP pour Meshr-Lang"""
    
    def __init__(self):
        super().__init__("meshr-lang-server", "0.1.0")
        
        # Composants du serveur
        self.parser = MeshrParser()
        self.diagnostics = MeshrDiagnostics(self.parser)
        self.completion = MeshrCompletion(self.parser)
        self.symbols = MeshrSymbols(self.parser)
        self.module_validator = None  # Initialisé dans initialize
        
        # Cache des documents analysés
        self.document_cache: Dict[str, Any] = {}
        
        # Configuration des handlers
        self._setup_handlers()
    
    def _setup_handlers(self):
        """Configure les handlers LSP"""
        
        @self.feature('initialize')
        def initialize(params: InitializeParams) -> InitializeResult:
            """Initialisation du serveur"""
            logger.info("Initialisation du serveur LSP Meshr-Lang")
            
            # Initialiser le validateur de modules
            if params.root_uri:
                workspace_root = params.root_uri.replace('file://', '')
                self.module_validator = ModuleValidator(workspace_root)
            
            return InitializeResult(
                capabilities=ServerCapabilities(
                    text_document_sync=TextDocumentSyncKind.FULL,
                    completion_provider=CompletionOptions(
                        resolve_provider=True,
                        trigger_characters=['.', '@', ' ', '\n']
                    ),
                    hover_provider=True,
                    document_symbol_provider=True,
                    workspace_symbol_provider=True,
                    diagnostic_provider=True
                )
            )
        
        @self.feature('textDocument/didOpen')
        def did_open(ls, params):
            """Document ouvert"""
            doc = params.text_document
            logger.info(f"Document ouvert: {doc.uri}")
            self._analyze_document(doc)
        
        @self.feature('textDocument/didChange')
        def did_change(ls, params):
            """Document modifié"""
            doc = params.text_document
            logger.info(f"Document modifié: {doc.uri}")
            self._analyze_document(doc)
        
        @self.feature('textDocument/didClose')
        def did_close(ls, params):
            """Document fermé"""
            doc = params.text_document
            logger.info(f"Document fermé: {doc.uri}")
            if doc.uri in self.document_cache:
                del self.document_cache[doc.uri]
        
        @self.feature('textDocument/completion')
        def completion(ls, params) -> List[CompletionItem]:
            """Autocomplétion"""
            doc = self.workspace.get_document(params.text_document.uri)
            return self.completion.get_completions(
                doc, params.position
            )
        
        @self.feature('textDocument/hover')
        def hover(ls, params) -> Optional[Hover]:
            """Information au survol"""
            doc = self.workspace.get_document(params.text_document.uri)
            return self.completion.get_hover(doc, params.position)
        
        @self.feature('textDocument/documentSymbol')
        def document_symbols(ls, params) -> List[DocumentSymbol]:
            """Symboles du document"""
            doc = self.workspace.get_document(params.text_document.uri)
            return self.symbols.get_document_symbols(doc)
        
        @self.feature('workspace/symbol')
        def workspace_symbols(ls, params) -> List[WorkspaceSymbol]:
            """Symboles de l'espace de travail"""
            return self.symbols.get_workspace_symbols(
                self.workspace, params.query
            )
    
    def _analyze_document(self, doc: TextDocumentItem):
        """Analyse un document et publie les diagnostics"""
        try:
            # Parser le document
            tree = self.parser.parse(doc.text)
            
            # Générer les diagnostics de base
            diagnostics = self.diagnostics.analyze(tree, doc.uri)
            
            # Ajouter la validation des modules si disponible
            if self.module_validator:
                try:
                    # Analyser le module
                    module_info = self.module_validator.analyze_file(doc.uri, doc.text)
                    
                    # Valider les imports/exports
                    module_diagnostics = self.module_validator.validate_imports_exports(module_info)
                    diagnostics.extend(module_diagnostics)
                    
                    # Valider les dépendances circulaires
                    circular_diagnostics = self.module_validator.validate_circular_dependencies()
                    diagnostics.extend(circular_diagnostics)
                    
                except Exception as e:
                    logger.error(f"Erreur lors de la validation du module {doc.uri}: {e}")
            
            # Publier les diagnostics
            self.publish_diagnostics(doc.uri, diagnostics)
            
            # Mettre en cache
            self.document_cache[doc.uri] = {
                'tree': tree,
                'diagnostics': diagnostics
            }
            
        except Exception as e:
            logger.error(f"Erreur lors de l'analyse de {doc.uri}: {e}")
            # Publier une erreur générique
            error_diagnostic = Diagnostic(
                range=Range(
                    start=Position(line=0, character=0),
                    end=Position(line=0, character=0)
                ),
                message=f"Erreur d'analyse: {str(e)}",
                severity=1  # Error
            )
            self.publish_diagnostics(doc.uri, [error_diagnostic])
