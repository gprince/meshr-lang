grammar MeshrModule;

moduleDecl: 'module' qualifiedName ;

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

exportDecl: 'export' topLevelDecl ;

topLevelDecl: productDecl ; // À étendre avec d'autres artefacts (domain, contract, etc.)

productDecl: 'product' IDENTIFIER '{' .*? '}' ;

qualifiedName: IDENTIFIER ('.' IDENTIFIER)* ;

STRING_LITERAL: '"' (~["\\] | '\\' .)* '"' ;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
