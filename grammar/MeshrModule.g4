grammar MeshrModule;

compilationUnit
    : moduleDecl importDecl* exportDecl* EOF
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
    : 'export' topLevelDecl            # InlineExport
    | 'export' '{' exportItems '}'     # GroupedExport
    ;

exportItems
    : IDENTIFIER (',' IDENTIFIER)*
    ;

topLevelDecl: productDecl ; // À étendre avec d'autres artefacts (domain, contract, etc.)

productDecl: 'product' IDENTIFIER '{' .*? '}' ;

qualifiedName: IDENTIFIER ('.' IDENTIFIER)* ;


fragment ESC: '\\' ["\\/bfnrt] ;

AT: '@';
STRING_LITERAL: '"' (ESC | ~["\\\r\n])* '"';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip ;
NUMBER_LITERAL: [0-9]+ ('.' [0-9]+)?;