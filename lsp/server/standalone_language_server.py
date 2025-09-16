#!/usr/bin/env python3
"""
Serveur LSP Meshr-Lang standalone - Version complète
====================================================
Version standalone du serveur LSP sans imports relatifs
"""

import sys
import os
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any

# Déterminer le répertoire de base
if getattr(sys, 'frozen', False):
    # Mode PyInstaller (exécutable)
    base_dir = Path(sys._MEIPASS)
else:
    # Mode développement
    base_dir = Path(__file__).parent

# Ajouter les chemins nécessaires
sys.path.insert(0, str(base_dir))
sys.path.insert(0, str(base_dir.parent.parent))  # Pour meshr_project.py

# Imports absolus
try:
    from pygls.server import LanguageServer
    from pygls.workspace import Document
    from pygls.protocol import default_converter
    from lsprotocol.types import (
        InitializeParams, InitializeResult, ServerCapabilities,
        TextDocumentSyncKind, CompletionOptions, Hover, Location,
        DefinitionParams, HoverParams, CompletionItem, Diagnostic,
        TextDocumentItem, Position, Range
    )
except ImportError as e:
    print(f"❌ Erreur import pygls: {e}", file=sys.stderr)
    sys.exit(1)

# Imports locaux
try:
    from meshr_project import MeshrProjectManager
    from project_manager import LSPProjectManager
except ImportError as e:
    print(f"❌ Erreur import modules locaux: {e}", file=sys.stderr)
    sys.exit(1)

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StandaloneMeshrLanguageServer(LanguageServer):
    """Serveur LSP Meshr-Lang standalone"""
    
    def __init__(self):
        super().__init__('meshr-lang', '1.0.0')
        self.project_manager = None
        # Compteur de requêtes actives pour éviter la surcharge
        self._active_requests = 0
        self._max_concurrent_requests = 2  # Réduire drastiquement les requêtes simultanées
        # Limites mémoire pour éviter les fuites et la pression mémoire
        self._max_cache_size = 50  # Réduire drastiquement le cache
        self._symbol_cache = {}
        self._cache_hits = 0
        
        # Monitoring de la mémoire
        self._memory_checks = 0
        self._max_memory_checks = 25  # Nettoyer le cache tous les 25 appels
        self._memory_warnings = 0  # Compteur d'alertes mémoire
        self._setup_handlers()
    
    def _cleanup_memory(self):
        """Nettoie la mémoire pour éviter la pression"""
        try:
            # Surveillance de l'utilisation mémoire
            import psutil
            import os
            
            process = psutil.Process(os.getpid())
            memory_mb = process.memory_info().rss / 1024 / 1024
            
            if memory_mb > 100:  # Plus de 100MB
                self._memory_warnings += 1
                logger.warning(f"⚠️ Mémoire LSP élevée: {memory_mb:.1f}MB (alerte #{self._memory_warnings})")
                
                # Nettoyage agressif si trop de mémoire
                if memory_mb > 200:  # Plus de 200MB
                    logger.error(f"🚨 MÉMOIRE CRITIQUE: {memory_mb:.1f}MB - Nettoyage d'urgence")
                    self._symbol_cache.clear()
                    
            # Nettoyer le cache si trop gros
            if len(self._symbol_cache) > self._max_cache_size:
                logger.info(f"🧹 Nettoyage du cache: {len(self._symbol_cache)} -> {self._max_cache_size//2}")
                # Garder seulement la moitié des entrées les plus récentes
                items = list(self._symbol_cache.items())
                self._symbol_cache = dict(items[-self._max_cache_size//2:])
            
            # Forcer le garbage collection
            import gc
            collected = gc.collect()
            if collected > 0:
                logger.info(f"🧹 Garbage collection: {collected} objets libérés")
                
        except ImportError:
            # psutil pas disponible, nettoyage basique
            import gc
            collected = gc.collect()
            if collected > 0:
                logger.info(f"🧹 Garbage collection: {collected} objets libérés")
        except Exception as e:
            logger.warning(f"⚠️ Erreur lors du nettoyage mémoire: {e}")
    
    def _setup_handlers(self):
        """Configure les handlers LSP"""
        
        # Configuration de logs détaillés pour le debug
        import sys
        import traceback
        
        # Handler global pour capturer les exceptions non gérées
        def exception_handler(exc_type, exc_value, exc_traceback):
            logger.error(f"🚨 EXCEPTION NON GÉRÉE: {exc_type.__name__}: {exc_value}")
            logger.error("🚨 TRACEBACK COMPLET:")
            traceback.print_exception(exc_type, exc_value, exc_traceback)
            # Ne pas arrêter le serveur sur les exceptions
            logger.info("🔄 Serveur LSP continue malgré l'exception...")
        
        sys.excepthook = exception_handler
        
        # Handler pour les signaux de fermeture propre
        import signal
        
        def signal_handler(signum, frame):
            logger.info(f"🛑 Signal reçu: {signum}")
            logger.info("🔄 Arrêt propre du serveur LSP...")
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        @self.feature('initialize')
        def initialize(ls, params: InitializeParams) -> InitializeResult:
            """Initialisation du serveur"""
            logger.info("🚀 Initialisation du serveur LSP Meshr-Lang")
            
            try:
                # Initialiser le gestionnaire de projet LSP
                if params.root_uri:
                    workspace_root = params.root_uri.replace('file://', '')
                    self.project_manager = LSPProjectManager()
                    
                    # Si on est dans un sous-projet (comme hr-employees-project), l'utiliser directement
                    if 'hr-employees-project' in workspace_root:
                        logger.info(f"🔧 Chargement du projet spécifique: {workspace_root}")
                        self.project_manager.add_workspace_root(workspace_root)
                    else:
                        # Sinon, chercher des projets Meshr-Lang dans le workspace
                        logger.info(f"🔧 Recherche de projets Meshr-Lang dans: {workspace_root}")
                        self.project_manager.add_workspace_root(workspace_root)
                    
                    logger.info(f"✅ Gestionnaire de projet initialisé pour: {workspace_root}")
                
                result = InitializeResult(
                    capabilities=ServerCapabilities(
                        text_document_sync=TextDocumentSyncKind.Full,
                        completion_provider=CompletionOptions(
                            resolve_provider=True,
                            trigger_characters=['.', '@', ' ', '\n']
                        ),
                        hover_provider=True,
                        definition_provider=True,
                        references_provider=True
                    )
                )
                
                logger.info("✅ Serveur LSP initialisé avec succès")
                return result
                
            except Exception as e:
                logger.error(f"❌ Erreur initialisation: {e}")
                raise
        
        # Logs pour surveiller les communications
        @self.feature('textDocument/didOpen')
        def did_open(ls, params):
            """Document ouvert"""
            doc = self.workspace.get_text_document(params.text_document.uri)
            logger.info(f"📄 Document ouvert: {doc.uri}")
        
        @self.feature('textDocument/didChange')
        def did_change(ls, params):
            """Document modifié"""
            doc = self.workspace.get_text_document(params.text_document.uri)
            logger.info(f"📝 Document modifié: {doc.uri}")
        
        @self.feature('textDocument/definition')
        def definition(ls, params: DefinitionParams) -> Optional[List[Location]]:
            """Go to Definition"""
            try:
                # Protection contre les requêtes concurrentes
                if not hasattr(self, '_definition_lock'):
                    import threading
                    self._definition_lock = threading.Lock()
                
                with self._definition_lock:
                    # Vérifier la charge du serveur
                    if self._active_requests >= self._max_concurrent_requests:
                        logger.warning(f"⚠️ Trop de requêtes concurrentes ({self._active_requests}), requête ignorée")
                        return None
                    
                    self._active_requests += 1
                    
                    # Nettoyage périodique de la mémoire
                    self._memory_checks += 1
                    if self._memory_checks >= self._max_memory_checks:
                        self._memory_checks = 0
                        self._cleanup_memory()
                    
                    try:
                        uri = params.text_document.uri
                        position = params.position
                        
                        # Obtenir le symbole à la position
                        doc = self.workspace.get_text_document(uri)
                        if position.line >= len(doc.lines):
                            logger.warning(f"⚠️ Ligne {position.line} hors limites (document a {len(doc.lines)} lignes)")
                            return None
                        line = doc.lines[position.line]
                        
                        # Extraire le symbole (simplifié)
                        word = self._get_word_at_position(line, position.character)
                        if not word:
                            logger.info(f"🔍 Aucun symbole trouvé à la position {position.line}:{position.character}")
                            return None
                        
                        logger.info(f"🔍 Recherche de définition pour: '{word}' dans {uri}")
                        
                        # Résoudre le symbole via le gestionnaire de projet
                        if self.project_manager:
                            symbol_info = self.project_manager.resolve_symbol(uri, word)
                            logger.info(f"🔍 Symbol info: {symbol_info}")
                            
                            if symbol_info:
                                location = self.project_manager.get_definition(uri, word)
                                logger.info(f"🔍 Location: {location}")
                                
                                if location:
                                    try:
                                        # Retourner directement le dictionnaire de localisation
                                        # pygls se chargera de la sérialisation
                                       result = [{
                                           "uri": location['uri'],
                                           "range": {
                                               "start": {
                                                   "line": location['range']['start']['line'],
                                                   "character": location['range']['start']['character']
                                               },
                                               "end": {
                                                   "line": location['range']['end']['line'],
                                                   "character": location['range']['end']['character']
                                               }
                                           }
                                       }]
                                       logger.info(f"✅ Définition trouvée pour '{word}': {result}")
                                       logger.info("🔄 Envoi de la réponse definition...")
                                       
                                       # Log avant retour pour tracer le plantage
                                       logger.info("🔄 Préparation du retour de définition...")
                                       
                                       # PROTECTION ANTI-CRASH : Copie défensive
                                       try:
                                           safe_result = []
                                           for item in result:
                                               safe_result.append(dict(item))
                                           logger.info("✅ Résultat sécurisé prêt")
                                           return safe_result
                                       except Exception as safety_error:
                                           logger.error(f"🚨 ERREUR PROTECTION: {safety_error}")
                                           # Retour du résultat original en cas d'échec de la copie
                                           return result
                                    except Exception as e:
                                        logger.error(f"❌ Erreur lors de la création de l'objet Location: {e}")
                                        logger.error(f"❌ Location data: {location}")
                                        return None
                            else:
                                logger.info(f"🔍 Symbole '{word}' non trouvé dans l'index")
                        
                        return None
                    finally:
                        self._active_requests -= 1
                
            except Exception as e:
                logger.error(f"❌ Erreur lors de la résolution de définition: {e}")
                import traceback
                traceback.print_exc()
                return None
        
        @self.feature('textDocument/hover')
        def hover(ls, params: HoverParams) -> Optional[Hover]:
            """Hover (informations au survol)"""
            try:
                # Protection contre les requêtes concurrentes
                if not hasattr(self, '_hover_lock'):
                    import threading
                    self._hover_lock = threading.Lock()
                
                with self._hover_lock:
                    uri = params.text_document.uri
                    position = params.position
                    
                    # Obtenir le symbole à la position
                    doc = self.workspace.get_text_document(uri)
                    line = doc.lines[position.line]
                    
                    # Extraire le symbole (simplifié)
                    word = self._get_word_at_position(line, position.character)
                    if not word:
                        return None
                    
                    # Obtenir les informations de hover
                    if self.project_manager:
                        hover_info = self.project_manager.get_hover_info(uri, word)
                        if hover_info:
                            logger.info(f"✅ Hover info trouvé pour '{word}': {hover_info}")
                            logger.info("🔄 Création de l'objet Hover...")
                            
                            try:
                                hover_result = Hover(**hover_info)
                                logger.info(f"✅ Hover créé pour '{word}': {hover_result}")
                                logger.info("🔄 Envoi de la réponse hover...")
                                
                                # Log avant retour pour tracer le plantage
                                logger.info("🔄 Préparation du retour de hover...")
                                
                                # PROTECTION ANTI-CRASH : Forcer la finalisation
                                try:
                                    # Copie défensive du résultat
                                    safe_hover = Hover(
                                        contents=hover_result.contents,
                                        range=hover_result.range
                                    )
                                    logger.info("✅ Hover sécurisé prêt")
                                    return safe_hover
                                except Exception as safety_error:
                                    logger.error(f"🚨 ERREUR PROTECTION HOVER: {safety_error}")
                                    return None
                            except Exception as hover_error:
                                logger.error(f"🚨 ERREUR LORS DE LA CRÉATION HOVER: {hover_error}")
                                traceback.print_exc()
                                return None
                    
                    return None
                
            except Exception as e:
                logger.error(f"❌ Erreur lors du hover: {e}")
                return None
    
    def _get_word_at_position(self, line: str, character: int) -> Optional[str]:
        """Extrait le mot à la position donnée"""
        if character >= len(line):
            return None
            
        # Trouver le début du mot
        start = character
        while start > 0 and (line[start - 1].isalnum() or line[start - 1] in '._'):
            start -= 1
            
        # Trouver la fin du mot
        end = character
        while end < len(line) and (line[end].isalnum() or line[end] in '._'):
            end += 1
            
        if start < end:
            return line[start:end]
        return None

def main():
    """Point d'entrée principal"""
    try:
        logger.info("🚀 Démarrage du serveur LSP Meshr-Lang standalone")
        
        # Créer et configurer le serveur avec logs détaillés
        logger.info("🔄 Création du serveur...")
        server = StandaloneMeshrLanguageServer()
        logger.info("✅ Serveur LSP créé")
        
        logger.info("✅ Serveur LSP initialisé, démarrage IO...")
        
        # Démarrer le serveur avec logging détaillé
        logger.info("🔄 Appel de server.start_io()...")
        
        # Intercepter les erreurs de communication
        original_send_data = server.send_data if hasattr(server, 'send_data') else None
        
        def logged_send_data(data):
            try:
                logger.info(f"📤 ENVOI LSP: {str(data)[:200]}...")
                if original_send_data:
                    result = original_send_data(data)
                    logger.info("✅ Envoi LSP réussi")
                    return result
            except Exception as send_error:
                logger.error(f"🚨 ERREUR ENVOI LSP: {send_error}")
                import traceback
                traceback.print_exc()
                raise
        
        if hasattr(server, 'send_data'):
            server.send_data = logged_send_data
        
        try:
            server.start_io()
            logger.info("✅ server.start_io() terminé normalement")
        except Exception as io_error:
            logger.error(f"🚨 ERREUR DANS start_io(): {io_error}")
            import traceback
            traceback.print_exc()
            raise
        
    except KeyboardInterrupt:
        logger.info("🛑 Arrêt du serveur LSP (Ctrl+C)")
    except Exception as e:
        logger.error(f"❌ Erreur serveur LSP: {e}")
        import traceback
        traceback.print_exc()
        # Ne pas faire sys.exit(1) pour éviter de planter le serveur
        # Le serveur LSP doit rester stable
        logger.error("❌ Serveur LSP arrêté à cause d'une erreur")

if __name__ == "__main__":
    main()
