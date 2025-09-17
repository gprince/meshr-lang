grammar MeshrModule;

// ==============================
// Entrée principale
// ==============================
compilationUnit
    : annotatedModuleDecl importDecl* (exportDecl | topLevelDecl)* EOF
    ;

// ==============================
// Déclarations de module
// ==============================
annotatedModuleDecl
    : annotation* 'module' qualifiedName
    ;

// ==============================
// Import / Export
// ==============================
importDecl
    : 'import' importItemsWithOptionalBraces 'from' qualifiedName
    ;

importItemsWithOptionalBraces
    : IDENTIFIER                          # SingleImport
    | '*'                                 # WildcardImport
    | '{' importItems '}'                # GroupImport
    ;

importItems
    : IDENTIFIER (',' IDENTIFIER)*
    ;

exportDecl
    : annotation* 'export' exportableDecl            # InlineExport
    | 'export' '{' exportItems '}'                   # GroupedExport
    ;

exportItems
    : IDENTIFIER (',' IDENTIFIER)*
    ;

// ==============================
// Déclarations de haut niveau
// ==============================
topLevelDecl
    : annotatedEnumDecl
    | sealedEnumDecl
    | annotatedAnnotationDecl
    | sealedRecordDecl
    | recordDecl
    | sealedTraitDecl
    | traitDecl
    | annotatedAspectDecl
    | sealedAspectDecl
    | annotatedEntityDecl
    | sealedEntityDecl
    | annotatedTypeRelationDecl
    | sealedTypeRelationDecl
    | annotatedRelationDecl
    | sealedRelationDecl
    | annotatedMetricDecl
    | sealedMetricDecl
    ;

// ========== ENUM =============
exportableDecl
    : annotatedAnnotationDecl
    | annotatedEnumDecl
    | sealedEnumDecl
    | annotatedEntityDecl
    | sealedEntityDecl
    | annotatedTypeRelationDecl
    | sealedTypeRelationDecl
    | annotatedRelationDecl
    | sealedRelationDecl
    | recordDecl
    | sealedRecordDecl
    | traitDecl
    | sealedTraitDecl
    | annotatedAspectDecl
    | sealedAspectDecl
    | annotatedMetricDecl
    | sealedMetricDecl
    ;

annotatedEnumDecl
    : annotation* enumDecl
    ;

sealedEnumDecl
    : SEALED enumDecl
    ;

// ========== ENTITY =============
annotatedEntityDecl
    : annotation* entityDecl
    ;

sealedEntityDecl
    : SEALED entityDecl
    ;

enumDecl
    : 'enum' IDENTIFIER enumSignature? 'is' '(' enumValueList ')'
    ;

enumSignature
    : '(' enumAttributeList ')'
    ;

enumAttributeList
    : enumAttribute (',' enumAttribute)*
    ;

enumAttribute
    : IDENTIFIER ':' typeRef ('=' annotationValue)?
    ;

enumValueList
    : enumValue (',' enumValue)*
    ;

enumValue
    : (IDENTIFIER | STRING_LITERAL) ('(' enumValueArgList? ')')?
    ;

enumValueArgList
    : enumValueArg (',' enumValueArg)*
    ;

enumValueArg
    : IDENTIFIER '=' annotationValue
    ;

// ========== ENTITY DECLARATION ============
entityDecl
    : ENTITY IDENTIFIER withClause? 'is' entityFieldList entityAspects? 'end'
    ;

entityFieldList
    : entityField+
    ;

entityField
    : IDENTIFIER ':' typeRef ('=' annotationValue)?
    ;

entityAspects
    : ASPECTS '{' aspectInstanceList '}'
    ;

aspectInstanceList
    : aspectInstance (',' aspectInstance)*
    ;

aspectInstance
    : IDENTIFIER '{' aspectInstanceFieldList? '}'
    ;

aspectInstanceFieldList
    : aspectInstanceField (',' aspectInstanceField)*
    ;

aspectInstanceField
    : IDENTIFIER ':' annotationValue
    ;

// ========== TYPE RELATION DECLARATION ============
annotatedTypeRelationDecl
    : annotation* typeRelationDecl
    ;

sealedTypeRelationDecl
    : SEALED typeRelationDecl
    ;

typeRelationDecl
    : TYPE RELATION IDENTIFIER withClause? 'is' typeRelationFieldList typeRelationAspects? 'end'
    ;

typeRelationFieldList
    : typeRelationField+
    ;

typeRelationField
    : IDENTIFIER ':' typeRef ('=' annotationValue)?
    ;

typeRelationAspects
    : ASPECTS '{' aspectInstanceList '}'
    ;

// ========== RELATION DECLARATION ============
annotatedRelationDecl
    : annotation* relationDecl
    ;

sealedRelationDecl
    : SEALED relationDecl
    ;

relationDecl
    : BIDIRECTIONAL? RELATION IDENTIFIER relationType? withClause? 'is' relationEndpoints relationFieldList? relationAspects? 'end'
    ;

relationType
    : 'of' TYPE IDENTIFIER
    ;

relationEndpoints
    : FROM relationEndpoint TO relationEndpoint
    ;

relationEndpoint
    : IDENTIFIER '(' IDENTIFIER (',' IDENTIFIER)* ')'
    ;

relationFieldList
    : relationField+
    ;

relationField
    : IDENTIFIER ':' typeRef ('=' annotationValue)?
    ;

relationAspects
    : ASPECTS '{' aspectInstanceList '}'
    ;

// ========== ANNOTATION DECLARATION ============
annotatedAnnotationDecl
    : annotation* annotationDecl
    ;

annotationDecl
    : 'annotation' IDENTIFIER 'is' annotationFieldList 'end'
    ;

annotationFieldList
    : annotationField+
    ;

annotationField
    : ('required' | 'optional') IDENTIFIER ':' typeRef ('=' annotationValue)? NEWLINE?
    ;

// ========== ANNOTATION USAGE ============
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

// ========== TYPES DE BASE ============
  
// Types de base reconnus
baseType
    : 'Boolean'
    | stringType
    | 'Integer'
    | 'Float'
    | 'Double'
    | 'Date'
    | 'Datetime'
    | 'Time'
    | 'Geography'
    | 'Timestamp'
    | 'Bytes'
    | 'Json'
    | 'Sql'
    | 'Interval'
    | 'Range'
    ;

// Type String avec contraintes optionnelles
stringType
    : 'String' stringConstraints?
    ;

stringConstraints
    : stringConstraint (stringConstraint)*
    ;

stringConstraint
    : 'pattern' STRING_LITERAL
    | 'length' signedNumber '..' signedNumber
    ;

// ========== SHARED ============
qualifiedName
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

// ========== TYPE REFERENCES ============
typeRef
    : qualifiedName
    | baseType
    | listType
    | mapType
    | rangeType
    ;

listType
    : 'List' 'of' typeRef
    ;

mapType
    : 'Map' 'of' typeRef 'to' typeRef
    ;

rangeType
    : 'Range' 'of' typeRef
    ;

// ========== ANNOTATION USAGE ============
annotationValue
    : STRING_LITERAL
    | NUMBER_LITERAL
    | BOOLEAN_LITERAL
    | qualifiedName
    | intervalLiteral
    | listLiteral
    | mapLiteral
    | recordLiteral
    | rangeLiteral
    | jsonLiteral
    | geographyLiteral
    | bytesLiteral
    | datetimeLiteral
    | dateLiteral
    | timeLiteral
    | timestampLiteral
    | sqlLiteral
    ;

// ========== INTERVAL LITERALS ============
intervalLiteral
    : 'Interval' intervalSinglePart
    | 'Interval' STRING_LITERAL 'year' 'to' 'month'
    | 'Interval' STRING_LITERAL 'year' 'to' 'day'
    | 'Interval' STRING_LITERAL 'year' 'to' 'hour'
    | 'Interval' STRING_LITERAL 'year' 'to' 'minute'
    | 'Interval' STRING_LITERAL 'year' 'to' 'second'
    | 'Interval' STRING_LITERAL 'month' 'to' 'day'
    | 'Interval' STRING_LITERAL 'month' 'to' 'hour'
    | 'Interval' STRING_LITERAL 'month' 'to' 'minute'
    | 'Interval' STRING_LITERAL 'month' 'to' 'second'
    | 'Interval' STRING_LITERAL 'day' 'to' 'hour'
    | 'Interval' STRING_LITERAL 'day' 'to' 'minute'
    | 'Interval' STRING_LITERAL 'day' 'to' 'second'
    | 'Interval' STRING_LITERAL 'hour' 'to' 'minute'
    | 'Interval' STRING_LITERAL 'hour' 'to' 'second'
    | 'Interval' STRING_LITERAL 'minute' 'to' 'second'
    ;

intervalSinglePart
    : '-'? NUMBER_LITERAL intervalUnit
    ;

intervalUnit
    : 'year' | 'quarter' | 'month' | 'week' | 'day'
    | 'hour' | 'minute' | 'second' | 'millisecond' | 'microsecond'
    ;

// ========== RECORD DECLARATION ==========
recordDecl
    : 'record' IDENTIFIER withClause? 'is' recordFieldList 'end'
    ;

sealedRecordDecl
    : SEALED recordDecl
    ;

recordFieldList
    : recordField+
    ;

recordField
    : IDENTIFIER ':' typeRef ('=' annotationValue)? NEWLINE?
    ;

// ========== TRAIT DECLARATION ==========
traitDecl
    : 'trait' IDENTIFIER withClause? 'is' traitFieldList traitAspects? 'end'
    ;

sealedTraitDecl
    : SEALED traitDecl
    ;

traitFieldList
    : traitField+
    ;

traitField
    : IDENTIFIER ':' typeRef ('=' annotationValue)? NEWLINE?
    ;

traitAspects
    : ASPECTS '{' aspectInstanceList '}'
    ;

withClause
    : 'with' qualifiedName (',' qualifiedName)*
    ;

// ========== ASPECT DECLARATION ==========
annotatedAspectDecl
    : annotation* aspectDecl
    ;

aspectDecl
    : 'abstract'? 'aspect' IDENTIFIER aspectInheritance? 'is' aspectFieldList 'end'
    ;

sealedAspectDecl
    : SEALED aspectDecl
    ;

aspectInheritance
    : extendsClause withClause?
    | withClause extendsClause?
    ;

extendsClause
    : 'extends' qualifiedName
    ;

aspectFieldList
    : aspectField+
    ;

aspectField
    : IDENTIFIER ':' typeRef ('=' annotationValue)? NEWLINE?
    ;

// ========== COLLECTION AND COMPOSITE LITERALS ==========
listLiteral
    : 'List' '[' (annotationValue (',' annotationValue)*)? ']'
    ;

mapLiteral
    : 'Map' '{' (mapEntry (',' mapEntry)*)? '}'
    ;

mapEntry
    : annotationValue ':' annotationValue
    ;

recordLiteral
    : 'Record' '{' (recordLitField (',' recordLitField)*)? '}'
    ;

recordLitField
    : IDENTIFIER ':' annotationValue
    ;

rangeLiteral
    : 'Range' signedNumber '..' signedNumber
    ;

// ========== JSON LITERALS ==========
jsonLiteral
    : 'Json' '{' jsonObjectContent '}'
    | 'Json' '[' jsonArrayContent ']'
    | 'Json' STRING_LITERAL
    ;

jsonObjectContent
    : jsonPair (',' jsonPair)*
    | // empty
    ;

jsonArrayContent
    : jsonValue (',' jsonValue)*
    | // empty
    ;

jsonPair
    : STRING_LITERAL ':' jsonValue
    ;

jsonValue
    : STRING_LITERAL
    | NUMBER_LITERAL
    | BOOLEAN_LITERAL
    | 'null'
    | '{' jsonObjectContent '}'
    | '[' jsonArrayContent ']'
    ;

signedNumber
    : '-'? NUMBER_LITERAL
    ;

// ========== GEOGRAPHY LITERALS ==========
geographyLiteral
    : 'Geography' STRING_LITERAL
    | 'Geography' '{' jsonObjectContent '}'
    ;

// ========== BYTES LITERALS ==========
bytesLiteral
    : 'Bytes' STRING_LITERAL
    | 'Bytes' '[' bytesArrayContent ']'
    | 'Bytes' '{' jsonObjectContent '}'
    ;

bytesArrayContent
    : bytesValue (',' bytesValue)*
    | // empty
    ;

bytesValue
    : signedNumber
    ;

// ========== TEMPORAL LITERALS ==========
datetimeLiteral
    : 'Datetime' STRING_LITERAL
    ;

dateLiteral
    : 'Date' STRING_LITERAL
    ;

timeLiteral
    : 'Time' STRING_LITERAL
    ;

timestampLiteral
    : 'Timestamp' STRING_LITERAL
    ;

// ========== SQL LITERALS ==========
sqlLiteral
    : 'Sql' STRING_LITERAL
    ;

// ========== TERMINALS ============
fragment ESC
    : '\\' ["\\/bfnrt]
    ;

AT: '@';
STRING_LITERAL: '"' (ESC | ~["\\\r\n])* '"';

// Keywords
SEALED: 'sealed';
ENTITY: 'entity';
TYPE: 'type';
RELATION: 'relation';
BIDIRECTIONAL: 'bidirectional';
FROM: 'from';
TO: 'to';
ASPECTS: 'aspects';
METRIC: 'metric';
SOURCE: 'source';
CALCULATION: 'calculation';
AGGREGATION: 'aggregation';
UNIT: 'unit';
OUTPUTS: 'outputs';
DIMENSIONS: 'dimensions';
FILTERS: 'filters';
TEMPORAL: 'temporal';
MATCH: 'match';
WINDOW: 'window';
REFRESH_FREQUENCY: 'refresh_frequency';
HISTORICAL_DEPTH: 'historical_depth';

NUMBER_LITERAL
    : [0-9]+ ('.' [0-9]+)?
    | '0' [xX] [0-9a-fA-F]+
    ;

BOOLEAN_LITERAL
    : 'true' | 'false'
    ;

// ========== EXPRESSIONS ==========
expression
    : expression ('*' | '/' | '%') expression                      # MultiplicativeExpr
    | expression ('+' | '-') expression                            # AdditiveExpr
    | expression ('==' | '!=' | '<' | '<=' | '>' | '>=') expression # ComparisonExpr
    | expression ('and' | 'or') expression                         # LogicalExpr
    | expression 'in' expression                                   # InExpr
    | expression 'where' expression                                # WhereExpr
    | functionCall                                                  # FunctionCallExpr
    | fieldReference                                                # FieldReferenceExpr
    | enumReference                                                 # EnumReferenceExpr
    | literal                                                       # LiteralExpr
    | '(' expression ')'                                            # ParenthesizedExpr
    ;

functionCall
    : IDENTIFIER '(' (expression (',' expression)*)? ')'
    ;

fieldReference
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

enumReference
    : qualifiedName '.' (IDENTIFIER | STRING_LITERAL)
    ;

literal
    : STRING_LITERAL
    | NUMBER_LITERAL
    | BOOLEAN_LITERAL
    | dateLiteral
    | timeLiteral
    | timestampLiteral
    | datetimeLiteral
    | intervalLiteral
    | listLiteral
    | mapLiteral
    | recordLiteral
    | rangeLiteral
    | jsonLiteral
    | geographyLiteral
    | bytesLiteral
    | sqlLiteral
    ;

// ========== METRIC DECLARATION ==========
annotatedMetricDecl
    : annotation* metricDecl
    ;

sealedMetricDecl
    : SEALED metricDecl
    ;

metricDecl
    : METRIC IDENTIFIER withClause? 'is'
      metricSource
      (metricCalculation | metricAggregation)
      metricUnit?
      metricOutputs?
      metricDimensions?
      metricFilters?
      metricTemporal?
      metricAspects?
      'end'
    ;

metricSource
    : SOURCE qualifiedName
    ;

metricCalculation
    : CALCULATION expression
    ;

metricAggregation
    : AGGREGATION '{' aggregationFieldList '}'
    ;

aggregationFieldList
    : aggregationField (',' aggregationField)*
    ;

aggregationField
    : IDENTIFIER 'as' expression
    ;

metricUnit
    : UNIT STRING_LITERAL
    ;

metricOutputs
    : OUTPUTS '{' outputFieldList '}'
    ;

outputFieldList
    : outputField (',' outputField)*
    ;

outputField
    : IDENTIFIER ':' typeRef
    ;

metricDimensions
    : DIMENSIONS '{' dimensionList '}'
    ;

dimensionList
    : dimension (',' dimension)*
    ;

dimension
    : IDENTIFIER expression
    | IDENTIFIER matchExpression
    ;

matchExpression
    : MATCH expression 'is' matchArms 'end'
    ;

matchArms
    : matchArm (',' matchArm)*
    ;

matchArm
    : pattern '->' matchResult
    ;

pattern
    : orPattern
    ;

orPattern
    : basicPattern ('or' basicPattern)*
    ;

basicPattern
    : literalPattern
    | rangePattern
    | enumPattern
    | wildcardPattern
    ;

literalPattern
    : STRING_LITERAL
    | NUMBER_LITERAL
    | BOOLEAN_LITERAL
    ;

rangePattern
    : NUMBER_LITERAL '..' NUMBER_LITERAL?
    | dateLiteral '..' dateLiteral?
    ;

enumPattern
    : qualifiedName
    ;

wildcardPattern
    : '_'
    ;

matchResult
    : STRING_LITERAL
    | NUMBER_LITERAL
    | BOOLEAN_LITERAL
    | qualifiedName
    ;

metricFilters
    : FILTERS '{' filterList '}'
    ;

filterList
    : filterExpression (',' filterExpression)*
    ;

filterExpression
    : expression
    ;

metricTemporal
    : TEMPORAL '{' temporalConfigList '}'
    ;

temporalConfigList
    : temporalConfig (',' temporalConfig)*
    ;

temporalConfig
    : temporalField intervalLiteral
    ;

temporalField
    : WINDOW
    | REFRESH_FREQUENCY
    | HISTORICAL_DEPTH
    ;

metricAspects
    : 'aspects' '{' aspectInstanceList '}'
    ;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;
NEWLINE: ('\r'? '\n')+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
MULTILINE_COMMENT: '/*' .*? '*/' -> skip ;