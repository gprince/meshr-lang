"""
Intégration du parser ANTLR avec le serveur LSP
"""

import logging
from typing import Optional, Any, List
from pathlib import Path
import sys

# Ajouter le chemin vers la grammaire générée
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "grammar" / "generated"))

try:
    from MeshrModuleLexer import MeshrModuleLexer
    from MeshrModuleParser import MeshrModuleParser
    from MeshrModuleListener import MeshrModuleListener
    from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, RecognitionException, Token
    from antlr4.error.ErrorListener import ErrorListener
except ImportError as e:
    logging.warning(f"Impossible d'importer la grammaire ANTLR: {e}")
    MeshrModuleLexer = None
    MeshrModuleParser = None
    MeshrModuleListener = None
    ErrorListener = None
    RecognitionException = None
    Token = None

logger = logging.getLogger(__name__)

class MeshrErrorListener:
    """Listener personnalisé pour capturer les erreurs ANTLR"""
    
    def __init__(self):
        self.errors = []
        self.lexer_errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """Capture les erreurs de syntaxe"""
        error_info = {
            'line': line,
            'column': column,
            'message': msg,
            'offending_symbol': offendingSymbol,
            'type': 'syntax'
        }
        self.errors.append(error_info)
        logger.debug(f"Erreur de syntaxe ligne {line}:{column} - {msg}")
    
    def reportLexicalError(self, recognizer, offendingSymbol, line, column, msg, e):
        """Capture les erreurs lexicales (token recognition errors)"""
        error_info = {
            'line': line,
            'column': column,
            'message': f"Caractère invalide: '{offendingSymbol}'",
            'offending_symbol': offendingSymbol,
            'type': 'lexical'
        }
        self.lexer_errors.append(error_info)
        logger.debug(f"Erreur lexicale ligne {line}:{column} - {msg}")
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        """Rapporte les ambiguïtés"""
        pass
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        """Rapporte les tentatives de contexte complet"""
        pass
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        """Rapporte la sensibilité au contexte"""
        pass

class MeshrParser:
    """Parser Meshr-Lang utilisant ANTLR"""
    
    def __init__(self):
        self.lexer = None
        self.parser = None
        self.error_listener = None
        self.antlr_available = MeshrModuleLexer is not None
        self._check_grammar_availability()
    
    def _check_grammar_availability(self):
        """Vérifie si la grammaire ANTLR est disponible"""
        if MeshrModuleLexer is None:
            logger.warning("Grammaire ANTLR non disponible. Parser en mode dégradé.")
            return
        
        try:
            # Test rapide de la grammaire
            input_stream = InputStream("module test;")
            self.lexer = MeshrModuleLexer(input_stream)
            self.parser = MeshrModuleParser(CommonTokenStream(self.lexer))
            logger.info("Grammaire ANTLR chargée avec succès")
        except Exception as e:
            logger.error(f"Erreur lors du chargement de la grammaire: {e}")
            self.lexer = None
            self.parser = None
    
    def parse(self, text: str) -> Optional[Any]:
        """
        Parse le texte Meshr-Lang
        
        Args:
            text: Le contenu du fichier à parser
            
        Returns:
            L'arbre de syntaxe abstraite ou None en cas d'erreur
        """
        if not self.antlr_available:
            logger.warning("ANTLR non disponible - parser en mode dégradé")
            return None
            
        if not self.lexer or not self.parser:
            logger.warning("Parser non disponible")
            return None
        
        try:
            # Créer le flux d'entrée
            input_stream = InputStream(text)
            
            # Créer le lexer
            self.lexer = MeshrModuleLexer(input_stream)
            
            # Ajouter notre listener d'erreurs personnalisé au lexer
            self.error_listener = MeshrErrorListener()
            self.lexer.removeErrorListeners()  # Supprimer les listeners par défaut
            self.lexer.addErrorListener(self.error_listener)
            
            token_stream = CommonTokenStream(self.lexer)
            
            # Créer le parser
            self.parser = MeshrModuleParser(token_stream)
            
            # Ajouter notre listener d'erreurs personnalisé au parser
            self.parser.removeErrorListeners()  # Supprimer les listeners par défaut
            self.parser.addErrorListener(self.error_listener)
            
            # Parser le module
            tree = self.parser.compilationUnit()
            
            # Vérifier s'il y a des erreurs de syntaxe
            syntax_errors = self.parser.getNumberOfSyntaxErrors()
            if syntax_errors > 0:
                logger.warning(f"Erreurs de syntaxe détectées: {syntax_errors}")
                # On retourne quand même l'arbre pour permettre l'analyse des erreurs
            
            logger.debug("Parsing terminé")
            return tree
            
        except Exception as e:
            logger.error(f"Erreur de parsing: {e}")
            return None
    
    def is_grammar_available(self) -> bool:
        """Vérifie si la grammaire ANTLR est disponible"""
        return self.lexer is not None and self.parser is not None
    
    def get_syntax_errors(self) -> List[dict]:
        """Récupère les erreurs de syntaxe et lexicales capturées"""
        if self.error_listener:
            # Combiner les erreurs de syntaxe et lexicales
            all_errors = self.error_listener.errors + self.error_listener.lexer_errors
            # Trier par ligne et colonne
            all_errors.sort(key=lambda x: (x['line'], x['column']))
            return all_errors
        return []
    
    def get_tokens(self, text: str) -> list:
        """
        Tokenise le texte sans parsing complet
        
        Args:
            text: Le texte à tokeniser
            
        Returns:
            Liste des tokens
        """
        if not self.lexer:
            return []
        
        try:
            input_stream = InputStream(text)
            self.lexer = MeshrModuleLexer(input_stream)
            tokens = []
            
            token = self.lexer.nextToken()
            while token.type != token.EOF:
                tokens.append({
                    'type': token.type,
                    'text': token.text,
                    'line': token.line,
                    'column': token.column
                })
                token = self.lexer.nextToken()
            
            return tokens
            
        except Exception as e:
            logger.error(f"Erreur de tokenisation: {e}")
            return []
