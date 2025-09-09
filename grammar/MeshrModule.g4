grammar MeshrModule;

compilationUnit
    : moduleDecl importDecl* exportDecl* enumDecl* EOF
    ;

moduleDecl: annotation* 'module' qualifiedName ;

annotation
    : '@' IDENTIFIER ('(' annotationArgs? ')')?
    ;

annotationArgs
    : annotationArg (',' annotationArg)*
    ;

annotationArg
    : annotationArgPair
    | annotationValue
    ;

annotationArgPair
    : IDENTIFIER '=' annotationValue
    ;

annotationValue
    : STRING_LITERAL
    | NUMBER_LITERAL
    | qualifiedName
    ;

importDecl
    : 'import' importItemsWithOptionalBraces 'from' qualifiedName
    ;

importItemsWithOptionalBraces
    : IDENTIFIER                          # SingleImport
    | '*'                                 # WildcardImport
    | '{' importItems '}'                # GroupImport
    ;

importItems
    : IDENTIFIER (',' IDENTIFIER)+
    ;

exportDecl
    : 'export' exportableDecl            # InlineExport
    | 'export' '{' exportItems '}'       # GroupedExport
    ;

exportItems
    : IDENTIFIER (',' IDENTIFIER)*
    ;

topLevelDecl
    : enumDecl
    ;

exportableDecl
    : enumDecl
    ;

enumDecl
    : 'enum' IDENTIFIER enumSignature? 'is' '(' enumValueList ')'
    ;

enumValueList
    : enumValue (',' enumValue)*
    ;

enumSignature
    : '(' enumAttributeList ')'
    ;

enumAttributeList
    : enumAttribute (',' enumAttribute)*
    ;

enumAttribute
    : IDENTIFIER ':' qualifiedName ('=' annotationValue)?
    ;

enumValue
    : IDENTIFIER ('(' enumValueArgList? ')')?
    ;

enumValueArgList
    : enumValueArg (',' enumValueArg)*
    ;

enumValueArg
    : IDENTIFIER '=' annotationValue
    ;


qualifiedName: IDENTIFIER ('.' IDENTIFIER)* ;


fragment ESC: '\\' ["\\/bfnrt] ;

AT: '@';
STRING_LITERAL: '"' (ESC | ~["\\\r\n])* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip ;
NUMBER_LITERAL: [0-9]+ ('.' [0-9]+)? | '0' [xX] [0-9a-fA-F]+;