from antlr4 import InputStream, CommonTokenStream
from grammar.generated.MeshrModuleLexer import MeshrModuleLexer
from grammar.generated.MeshrModuleParser import MeshrModuleParser

def main():
    with open("tests/module-decl.meshr", encoding="utf-8") as f:
        input_stream = InputStream(f.read())

    lexer = MeshrModuleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MeshrModuleParser(stream)

    tree = parser.moduleDecl()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()