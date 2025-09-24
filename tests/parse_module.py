import sys
from antlr4 import InputStream, CommonTokenStream
try:
    from grammar.generated.MeshrModuleLexer import MeshrModuleLexer
    from grammar.generated.MeshrModuleParser import MeshrModuleParser
except ModuleNotFoundError:
    from grammar.generated.grammar.MeshrModuleLexer import MeshrModuleLexer
    from grammar.generated.grammar.MeshrModuleParser import MeshrModuleParser
from antlr4.atn.PredictionMode import PredictionMode

def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_module.py <path-to-file.meshr>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, encoding="utf-8") as f:
        input_stream = InputStream(f.read())

    lexer = MeshrModuleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MeshrModuleParser(stream)
    parser._interp.predictionMode = PredictionMode.LL

    from antlr4.error.ErrorListener import ErrorListener

    class ThrowingErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            raise Exception(f"Syntax error at line {line}:{column} - {msg}")

    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    try:
        tree = parser.compilationUnit()
        print(tree.toStringTree(recog=parser))
        print("--------------------------------")
        print("test: " + input_file + " ✅ OK")
        print("--------------------------------")
        print("")
    except Exception as e:
        print(f"[ERROR] Failed to parse {input_file}:\n{e}", file=sys.stderr)
        print("--------------------------------")
        print("test: " + input_file + " ❌ KO", file=sys.stderr)
        print("--------------------------------")
        print("")
        sys.exit(1)

if __name__ == "__main__":
    main()
