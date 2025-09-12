"""
Intégration du parser ANTLR avec le serveur LSP
"""

import logging
from typing import Optional, Any
from pathlib import Path
import sys

# Ajouter le chemin vers la grammaire générée
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "grammar" / "generated"))

try:
    from MeshrModuleLexer import MeshrModuleLexer
    from MeshrModuleParser import MeshrModuleParser
    from MeshrModuleListener import MeshrModuleListener
    from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
except ImportError as e:
    logging.warning(f"Impossible d'importer la grammaire ANTLR: {e}")
    MeshrModuleLexer = None
    MeshrModuleParser = None
    MeshrModuleListener = None

logger = logging.getLogger(__name__)

class MeshrParser:
    """Parser Meshr-Lang utilisant ANTLR"""
    
    def __init__(self):
        self.lexer = None
        self.parser = None
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
        if not self.lexer or not self.parser:
            logger.warning("Parser non disponible")
            return None
        
        try:
            # Créer le flux d'entrée
            input_stream = InputStream(text)
            
            # Créer le lexer
            self.lexer = MeshrModuleLexer(input_stream)
            token_stream = CommonTokenStream(self.lexer)
            
            # Créer le parser
            self.parser = MeshrModuleParser(token_stream)
            
            # Parser le module
            tree = self.parser.compilationUnit()
            
            logger.debug("Parsing réussi")
            return tree
            
        except Exception as e:
            logger.error(f"Erreur de parsing: {e}")
            return None
    
    def is_grammar_available(self) -> bool:
        """Vérifie si la grammaire ANTLR est disponible"""
        return self.lexer is not None and self.parser is not None
    
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
