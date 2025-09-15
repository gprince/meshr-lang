#!/usr/bin/env python3
"""
Serveur LSP Meshr-Lang avec logs de débogage complets
"""

import logging
import sys
import traceback
from typing import Any, Dict, List, Optional

from pygls.server import LanguageServer
from pygls import Diagnostic, TextDocumentSyncKind, ServerCapabilities

# Configuration du logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr),  # Logs vers stderr pour LSP
        logging.FileHandler('/tmp/meshr-lsp-debug.log', mode='w')  # Logs vers fichier
    ]
)
logger = logging.getLogger(__name__)

# Import des modules locaux
try:
    from .parser import MeshrParser
    from .diagnostics import MeshrDiagnostics
    logger.info("✅ Modules locaux importés avec succès")
except ImportError as e:
    logger.error(f"❌ Erreur import modules locaux: {e}")
    # Fallback vers les modules absolus
    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))
    from parser import MeshrParser
    from diagnostics import MeshrDiagnostics
    logger.info("✅ Modules absolus importés avec succès")

class MeshrLanguageServerDebug(LanguageServer):
    """Serveur LSP Meshr-Lang avec débogage complet"""
    
    def __init__(self):
        super().__init__("meshr-lang-debug", "1.0.0")
        logger.info("🎨 Serveur LSP Meshr-Lang Debug initialisé")
        
        # Initialiser les composants
        try:
            self.parser = MeshrParser()
            self.diagnostics = MeshrDiagnostics(self.parser)
            logger.info("✅ Parser et diagnostics initialisés")
        except Exception as e:
            logger.error(f"❌ Erreur initialisation composants: {e}")
            logger.error(traceback.format_exc())
            raise
        
        # Cache des documents
        self.document_cache: Dict[str, str] = {}
        
        # Configuration des capacités
        self.server_capabilities = ServerCapabilities(
            text_document_sync=TextDocumentSyncKind.Full
        )
        
        logger.info("✅ Capacités du serveur configurées")
    
    def _log_request(self, method: str, params: Any = None):
        """Log une requête entrante"""
        logger.debug(f"📥 Requête reçue: {method}")
        if params:
            logger.debug(f"📥 Paramètres: {params}")
    
    def _log_response(self, method: str, result: Any = None, error: Any = None):
        """Log une réponse"""
        if error:
            logger.error(f"📤 Erreur réponse {method}: {error}")
        else:
            logger.debug(f"📤 Réponse {method}: {result}")
    
    def _analyze_document(self, uri: str, content: str) -> List[Diagnostic]:
        """Analyser un document et retourner les diagnostics"""
        logger.debug(f"🔍 Analyse du document: {uri}")
        
        try:
            # Mettre à jour le cache
            self.document_cache[uri] = content
            
            # Analyser avec le parser
            tree = self.parser.parse(content)
            logger.debug(f"✅ Arbre syntaxique généré pour {uri}")
            
            # Générer les diagnostics
            diagnostics = self.diagnostics._analyze_tree(tree, uri)
            logger.debug(f"✅ {len(diagnostics)} diagnostics générés pour {uri}")
            
            return diagnostics
            
        except Exception as e:
            logger.error(f"❌ Erreur analyse document {uri}: {e}")
            logger.error(traceback.format_exc())
            
            # Retourner un diagnostic d'erreur
            return [Diagnostic(
                range=Range(
                    start=Position(line=0, character=0),
                    end=Position(line=0, character=0)
                ),
                message=f"Erreur d'analyse: {str(e)}",
                severity=DiagnosticSeverity.Error,
                source="meshr-lang"
            )]

# Instance globale du serveur
server = MeshrLanguageServerDebug()

@server.feature("initialize")
def initialize(params):
    """Initialiser le serveur LSP"""
    server._log_request("initialize", params)
    
    try:
        logger.info("🚀 Initialisation du serveur LSP Meshr-Lang Debug")
        
        # Log des informations du client
        logger.info(f"📋 Client: {getattr(params, 'client_info', 'N/A')}")
        logger.info(f"📋 Workspace: {getattr(params, 'root_uri', 'N/A')}")
        logger.info(f"📋 Capabilities: {getattr(params, 'capabilities', 'N/A')}")
        
        result = {
            "capabilities": server.server_capabilities,
            "serverInfo": {
                "name": "meshr-lang-debug",
                "version": "1.0.0"
            }
        }
        
        server._log_response("initialize", result)
        return result
        
    except Exception as e:
        logger.error(f"❌ Erreur initialisation: {e}")
        logger.error(traceback.format_exc())
        server._log_response("initialize", error=e)
        raise

@server.feature("textDocument/didOpen")
def did_open(params):
    """Document ouvert"""
    server._log_request("textDocument/didOpen", params)
    
    try:
        uri = params.text_document.uri
        content = params.text_document.text
        version = params.text_document.version
        
        logger.info(f"📖 Document ouvert: {uri} (version {version})")
        
        # Analyser le document
        diagnostics = server._analyze_document(uri, content)
        
        # Publier les diagnostics
        server.publish_diagnostics(uri, diagnostics)
        logger.info(f"📤 {len(diagnostics)} diagnostics publiés pour {uri}")
        
    except Exception as e:
        logger.error(f"❌ Erreur didOpen: {e}")
        logger.error(traceback.format_exc())

@server.feature("textDocument/didChange")
def did_change(params):
    """Document modifié"""
    server._log_request("textDocument/didChange", params)
    
    try:
        uri = params.text_document.uri
        version = params.text_document.version
        
        logger.debug(f"📝 Document modifié: {uri} (version {version})")
        
        # Récupérer le contenu actuel
        content = params.content_changes[0].text if params.content_changes else ""
        
        # Analyser le document
        diagnostics = server._analyze_document(uri, content)
        
        # Publier les diagnostics
        server.publish_diagnostics(uri, diagnostics)
        logger.debug(f"📤 {len(diagnostics)} diagnostics publiés pour {uri}")
        
    except Exception as e:
        logger.error(f"❌ Erreur didChange: {e}")
        logger.error(traceback.format_exc())

@server.feature("textDocument/didSave")
def did_save(params):
    """Document sauvegardé"""
    server._log_request("textDocument/didSave", params)
    
    try:
        uri = params.text_document.uri
        logger.info(f"💾 Document sauvegardé: {uri}")
        
        # Le document est déjà analysé par didChange
        # Ici on pourrait faire des analyses supplémentaires
        
    except Exception as e:
        logger.error(f"❌ Erreur didSave: {e}")
        logger.error(traceback.format_exc())

@server.feature("textDocument/didClose")
def did_close(params):
    """Document fermé"""
    server._log_request("textDocument/didClose", params)
    
    try:
        uri = params.text_document.uri
        logger.info(f"📕 Document fermé: {uri}")
        
        # Nettoyer le cache
        if uri in server.document_cache:
            del server.document_cache[uri]
            logger.debug(f"🧹 Cache nettoyé pour {uri}")
        
    except Exception as e:
        logger.error(f"❌ Erreur didClose: {e}")
        logger.error(traceback.format_exc())

# Fonctions de complétion et hover supprimées pour simplifier
# Elles seront ajoutées plus tard quand les types seront disponibles

@server.feature("shutdown")
def shutdown():
    """Arrêt du serveur"""
    logger.info("🛑 Arrêt du serveur LSP Meshr-Lang Debug")
    server._log_response("shutdown")

@server.feature("exit")
def exit():
    """Sortie du serveur"""
    logger.info("👋 Sortie du serveur LSP Meshr-Lang Debug")
    server._log_response("exit")

if __name__ == "__main__":
    logger.info("🎨 Démarrage du serveur LSP Meshr-Lang Debug")
    server.start_io()
