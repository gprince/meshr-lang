// Generated from /Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/grammar/MeshrModule.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MeshrModuleLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, STRING_LITERAL=11, IDENTIFIER=12, WS=13, COMMENT=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "STRING_LITERAL", "IDENTIFIER", "WS", "COMMENT"
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


	public MeshrModuleLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MeshrModule.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000em\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0005\nN\b"+
		"\n\n\n\f\nQ\t\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0005\u000bW\b"+
		"\u000b\n\u000b\f\u000bZ\t\u000b\u0001\f\u0004\f]\b\f\u000b\f\f\f^\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0005\rg\b\r\n\r\f\rj\t\r\u0001"+
		"\r\u0001\r\u0000\u0000\u000e\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0019\r\u001b\u000e\u0001\u0000\u0005\u0002\u0000\"\"\\\\\u0003"+
		"\u0000AZ__az\u0004\u000009AZ__az\u0003\u0000\t\n\r\r  \u0002\u0000\n\n"+
		"\r\rq\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0001"+
		"\u001d\u0001\u0000\u0000\u0000\u0003$\u0001\u0000\u0000\u0000\u0005+\u0001"+
		"\u0000\u0000\u0000\u00070\u0001\u0000\u0000\u0000\t2\u0001\u0000\u0000"+
		"\u0000\u000b4\u0001\u0000\u0000\u0000\r6\u0001\u0000\u0000\u0000\u000f"+
		"8\u0001\u0000\u0000\u0000\u0011?\u0001\u0000\u0000\u0000\u0013G\u0001"+
		"\u0000\u0000\u0000\u0015I\u0001\u0000\u0000\u0000\u0017T\u0001\u0000\u0000"+
		"\u0000\u0019\\\u0001\u0000\u0000\u0000\u001bb\u0001\u0000\u0000\u0000"+
		"\u001d\u001e\u0005m\u0000\u0000\u001e\u001f\u0005o\u0000\u0000\u001f "+
		"\u0005d\u0000\u0000 !\u0005u\u0000\u0000!\"\u0005l\u0000\u0000\"#\u0005"+
		"e\u0000\u0000#\u0002\u0001\u0000\u0000\u0000$%\u0005i\u0000\u0000%&\u0005"+
		"m\u0000\u0000&\'\u0005p\u0000\u0000\'(\u0005o\u0000\u0000()\u0005r\u0000"+
		"\u0000)*\u0005t\u0000\u0000*\u0004\u0001\u0000\u0000\u0000+,\u0005f\u0000"+
		"\u0000,-\u0005r\u0000\u0000-.\u0005o\u0000\u0000./\u0005m\u0000\u0000"+
		"/\u0006\u0001\u0000\u0000\u000001\u0005*\u0000\u00001\b\u0001\u0000\u0000"+
		"\u000023\u0005{\u0000\u00003\n\u0001\u0000\u0000\u000045\u0005}\u0000"+
		"\u00005\f\u0001\u0000\u0000\u000067\u0005,\u0000\u00007\u000e\u0001\u0000"+
		"\u0000\u000089\u0005e\u0000\u00009:\u0005x\u0000\u0000:;\u0005p\u0000"+
		"\u0000;<\u0005o\u0000\u0000<=\u0005r\u0000\u0000=>\u0005t\u0000\u0000"+
		">\u0010\u0001\u0000\u0000\u0000?@\u0005p\u0000\u0000@A\u0005r\u0000\u0000"+
		"AB\u0005o\u0000\u0000BC\u0005d\u0000\u0000CD\u0005u\u0000\u0000DE\u0005"+
		"c\u0000\u0000EF\u0005t\u0000\u0000F\u0012\u0001\u0000\u0000\u0000GH\u0005"+
		".\u0000\u0000H\u0014\u0001\u0000\u0000\u0000IO\u0005\"\u0000\u0000JN\b"+
		"\u0000\u0000\u0000KL\u0005\\\u0000\u0000LN\t\u0000\u0000\u0000MJ\u0001"+
		"\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000NQ\u0001\u0000\u0000\u0000"+
		"OM\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000PR\u0001\u0000\u0000"+
		"\u0000QO\u0001\u0000\u0000\u0000RS\u0005\"\u0000\u0000S\u0016\u0001\u0000"+
		"\u0000\u0000TX\u0007\u0001\u0000\u0000UW\u0007\u0002\u0000\u0000VU\u0001"+
		"\u0000\u0000\u0000WZ\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000"+
		"XY\u0001\u0000\u0000\u0000Y\u0018\u0001\u0000\u0000\u0000ZX\u0001\u0000"+
		"\u0000\u0000[]\u0007\u0003\u0000\u0000\\[\u0001\u0000\u0000\u0000]^\u0001"+
		"\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000"+
		"_`\u0001\u0000\u0000\u0000`a\u0006\f\u0000\u0000a\u001a\u0001\u0000\u0000"+
		"\u0000bc\u0005/\u0000\u0000cd\u0005/\u0000\u0000dh\u0001\u0000\u0000\u0000"+
		"eg\b\u0004\u0000\u0000fe\u0001\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000"+
		"hf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ik\u0001\u0000\u0000"+
		"\u0000jh\u0001\u0000\u0000\u0000kl\u0006\r\u0000\u0000l\u001c\u0001\u0000"+
		"\u0000\u0000\u0006\u0000MOX^h\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}