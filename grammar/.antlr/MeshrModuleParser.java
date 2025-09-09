// Generated from /Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/grammar/MeshrModule.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class MeshrModuleParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, STRING_LITERAL=11, IDENTIFIER=12, WS=13, COMMENT=14;
	public static final int
		RULE_moduleDecl = 0, RULE_importDecl = 1, RULE_importItemsWithOptionalBraces = 2, 
		RULE_importItems = 3, RULE_exportDecl = 4, RULE_topLevelDecl = 5, RULE_productDecl = 6, 
		RULE_qualifiedName = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"moduleDecl", "importDecl", "importItemsWithOptionalBraces", "importItems", 
			"exportDecl", "topLevelDecl", "productDecl", "qualifiedName"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'module'", "'import'", "'from'", "'*'", "'{'", "'}'", "','", "'export'", 
			"'product'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "STRING_LITERAL", 
			"IDENTIFIER", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "MeshrModule.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MeshrModuleParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModuleDeclContext extends ParserRuleContext {
		public QualifiedNameContext qualifiedName() {
			return getRuleContext(QualifiedNameContext.class,0);
		}
		public ModuleDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_moduleDecl; }
	}

	public final ModuleDeclContext moduleDecl() throws RecognitionException {
		ModuleDeclContext _localctx = new ModuleDeclContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_moduleDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			match(T__0);
			setState(17);
			qualifiedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImportDeclContext extends ParserRuleContext {
		public ImportItemsWithOptionalBracesContext importItemsWithOptionalBraces() {
			return getRuleContext(ImportItemsWithOptionalBracesContext.class,0);
		}
		public QualifiedNameContext qualifiedName() {
			return getRuleContext(QualifiedNameContext.class,0);
		}
		public ImportDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importDecl; }
	}

	public final ImportDeclContext importDecl() throws RecognitionException {
		ImportDeclContext _localctx = new ImportDeclContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_importDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(T__1);
			setState(20);
			importItemsWithOptionalBraces();
			setState(21);
			match(T__2);
			setState(22);
			qualifiedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImportItemsWithOptionalBracesContext extends ParserRuleContext {
		public ImportItemsWithOptionalBracesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importItemsWithOptionalBraces; }
	 
		public ImportItemsWithOptionalBracesContext() { }
		public void copyFrom(ImportItemsWithOptionalBracesContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class GroupImportContext extends ImportItemsWithOptionalBracesContext {
		public ImportItemsContext importItems() {
			return getRuleContext(ImportItemsContext.class,0);
		}
		public GroupImportContext(ImportItemsWithOptionalBracesContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SingleImportContext extends ImportItemsWithOptionalBracesContext {
		public TerminalNode IDENTIFIER() { return getToken(MeshrModuleParser.IDENTIFIER, 0); }
		public SingleImportContext(ImportItemsWithOptionalBracesContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class WildcardImportContext extends ImportItemsWithOptionalBracesContext {
		public WildcardImportContext(ImportItemsWithOptionalBracesContext ctx) { copyFrom(ctx); }
	}

	public final ImportItemsWithOptionalBracesContext importItemsWithOptionalBraces() throws RecognitionException {
		ImportItemsWithOptionalBracesContext _localctx = new ImportItemsWithOptionalBracesContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_importItemsWithOptionalBraces);
		try {
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				_localctx = new SingleImportContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				match(IDENTIFIER);
				}
				break;
			case T__3:
				_localctx = new WildcardImportContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(25);
				match(T__3);
				}
				break;
			case T__4:
				_localctx = new GroupImportContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(26);
				match(T__4);
				setState(27);
				importItems();
				setState(28);
				match(T__5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImportItemsContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(MeshrModuleParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(MeshrModuleParser.IDENTIFIER, i);
		}
		public ImportItemsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_importItems; }
	}

	public final ImportItemsContext importItems() throws RecognitionException {
		ImportItemsContext _localctx = new ImportItemsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_importItems);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(IDENTIFIER);
			setState(35); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(33);
				match(T__6);
				setState(34);
				match(IDENTIFIER);
				}
				}
				setState(37); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__6 );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExportDeclContext extends ParserRuleContext {
		public TopLevelDeclContext topLevelDecl() {
			return getRuleContext(TopLevelDeclContext.class,0);
		}
		public ExportDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exportDecl; }
	}

	public final ExportDeclContext exportDecl() throws RecognitionException {
		ExportDeclContext _localctx = new ExportDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_exportDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(T__7);
			setState(40);
			topLevelDecl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopLevelDeclContext extends ParserRuleContext {
		public ProductDeclContext productDecl() {
			return getRuleContext(ProductDeclContext.class,0);
		}
		public TopLevelDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topLevelDecl; }
	}

	public final TopLevelDeclContext topLevelDecl() throws RecognitionException {
		TopLevelDeclContext _localctx = new TopLevelDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_topLevelDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			productDecl();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProductDeclContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(MeshrModuleParser.IDENTIFIER, 0); }
		public ProductDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_productDecl; }
	}

	public final ProductDeclContext productDecl() throws RecognitionException {
		ProductDeclContext _localctx = new ProductDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_productDecl);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(T__8);
			setState(45);
			match(IDENTIFIER);
			setState(46);
			match(T__4);
			setState(50);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(47);
					matchWildcard();
					}
					} 
				}
				setState(52);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			setState(53);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QualifiedNameContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(MeshrModuleParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(MeshrModuleParser.IDENTIFIER, i);
		}
		public QualifiedNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifiedName; }
	}

	public final QualifiedNameContext qualifiedName() throws RecognitionException {
		QualifiedNameContext _localctx = new QualifiedNameContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_qualifiedName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(IDENTIFIER);
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(56);
				match(T__9);
				setState(57);
				match(IDENTIFIER);
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000e@\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002\u001f\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0004\u0003$\b\u0003\u000b\u0003\f\u0003%\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0005\u00061\b\u0006\n\u0006\f\u00064\t\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007;\b\u0007"+
		"\n\u0007\f\u0007>\t\u0007\u0001\u0007\u00012\u0000\b\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0000\u0000<\u0000\u0010\u0001\u0000\u0000\u0000\u0002"+
		"\u0013\u0001\u0000\u0000\u0000\u0004\u001e\u0001\u0000\u0000\u0000\u0006"+
		" \u0001\u0000\u0000\u0000\b\'\u0001\u0000\u0000\u0000\n*\u0001\u0000\u0000"+
		"\u0000\f,\u0001\u0000\u0000\u0000\u000e7\u0001\u0000\u0000\u0000\u0010"+
		"\u0011\u0005\u0001\u0000\u0000\u0011\u0012\u0003\u000e\u0007\u0000\u0012"+
		"\u0001\u0001\u0000\u0000\u0000\u0013\u0014\u0005\u0002\u0000\u0000\u0014"+
		"\u0015\u0003\u0004\u0002\u0000\u0015\u0016\u0005\u0003\u0000\u0000\u0016"+
		"\u0017\u0003\u000e\u0007\u0000\u0017\u0003\u0001\u0000\u0000\u0000\u0018"+
		"\u001f\u0005\f\u0000\u0000\u0019\u001f\u0005\u0004\u0000\u0000\u001a\u001b"+
		"\u0005\u0005\u0000\u0000\u001b\u001c\u0003\u0006\u0003\u0000\u001c\u001d"+
		"\u0005\u0006\u0000\u0000\u001d\u001f\u0001\u0000\u0000\u0000\u001e\u0018"+
		"\u0001\u0000\u0000\u0000\u001e\u0019\u0001\u0000\u0000\u0000\u001e\u001a"+
		"\u0001\u0000\u0000\u0000\u001f\u0005\u0001\u0000\u0000\u0000 #\u0005\f"+
		"\u0000\u0000!\"\u0005\u0007\u0000\u0000\"$\u0005\f\u0000\u0000#!\u0001"+
		"\u0000\u0000\u0000$%\u0001\u0000\u0000\u0000%#\u0001\u0000\u0000\u0000"+
		"%&\u0001\u0000\u0000\u0000&\u0007\u0001\u0000\u0000\u0000\'(\u0005\b\u0000"+
		"\u0000()\u0003\n\u0005\u0000)\t\u0001\u0000\u0000\u0000*+\u0003\f\u0006"+
		"\u0000+\u000b\u0001\u0000\u0000\u0000,-\u0005\t\u0000\u0000-.\u0005\f"+
		"\u0000\u0000.2\u0005\u0005\u0000\u0000/1\t\u0000\u0000\u00000/\u0001\u0000"+
		"\u0000\u000014\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u000020\u0001"+
		"\u0000\u0000\u000035\u0001\u0000\u0000\u000042\u0001\u0000\u0000\u0000"+
		"56\u0005\u0006\u0000\u00006\r\u0001\u0000\u0000\u00007<\u0005\f\u0000"+
		"\u000089\u0005\n\u0000\u00009;\u0005\f\u0000\u0000:8\u0001\u0000\u0000"+
		"\u0000;>\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000<=\u0001\u0000"+
		"\u0000\u0000=\u000f\u0001\u0000\u0000\u0000><\u0001\u0000\u0000\u0000"+
		"\u0004\u001e%2<";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}