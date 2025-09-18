# Generated from MeshrModule.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MeshrModuleParser import MeshrModuleParser
else:
    from MeshrModuleParser import MeshrModuleParser

# This class defines a complete generic visitor for a parse tree produced by MeshrModuleParser.

class MeshrModuleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MeshrModuleParser#compilationUnit.
    def visitCompilationUnit(self, ctx:MeshrModuleParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedModuleDecl.
    def visitAnnotatedModuleDecl(self, ctx:MeshrModuleParser.AnnotatedModuleDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#importDecl.
    def visitImportDecl(self, ctx:MeshrModuleParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#SingleImport.
    def visitSingleImport(self, ctx:MeshrModuleParser.SingleImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#WildcardImport.
    def visitWildcardImport(self, ctx:MeshrModuleParser.WildcardImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#GroupImport.
    def visitGroupImport(self, ctx:MeshrModuleParser.GroupImportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#importItems.
    def visitImportItems(self, ctx:MeshrModuleParser.ImportItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#InlineExport.
    def visitInlineExport(self, ctx:MeshrModuleParser.InlineExportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#GroupedExport.
    def visitGroupedExport(self, ctx:MeshrModuleParser.GroupedExportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#exportItems.
    def visitExportItems(self, ctx:MeshrModuleParser.ExportItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#topLevelDecl.
    def visitTopLevelDecl(self, ctx:MeshrModuleParser.TopLevelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#exportableDecl.
    def visitExportableDecl(self, ctx:MeshrModuleParser.ExportableDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedEnumDecl.
    def visitAnnotatedEnumDecl(self, ctx:MeshrModuleParser.AnnotatedEnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedEnumDecl.
    def visitSealedEnumDecl(self, ctx:MeshrModuleParser.SealedEnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedEntityDecl.
    def visitAnnotatedEntityDecl(self, ctx:MeshrModuleParser.AnnotatedEntityDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedEntityDecl.
    def visitSealedEntityDecl(self, ctx:MeshrModuleParser.SealedEntityDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumDecl.
    def visitEnumDecl(self, ctx:MeshrModuleParser.EnumDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumSignature.
    def visitEnumSignature(self, ctx:MeshrModuleParser.EnumSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumAttributeList.
    def visitEnumAttributeList(self, ctx:MeshrModuleParser.EnumAttributeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumAttribute.
    def visitEnumAttribute(self, ctx:MeshrModuleParser.EnumAttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumValueList.
    def visitEnumValueList(self, ctx:MeshrModuleParser.EnumValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumValue.
    def visitEnumValue(self, ctx:MeshrModuleParser.EnumValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumValueArgList.
    def visitEnumValueArgList(self, ctx:MeshrModuleParser.EnumValueArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumValueArg.
    def visitEnumValueArg(self, ctx:MeshrModuleParser.EnumValueArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#entityDecl.
    def visitEntityDecl(self, ctx:MeshrModuleParser.EntityDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#entityFieldList.
    def visitEntityFieldList(self, ctx:MeshrModuleParser.EntityFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#entityField.
    def visitEntityField(self, ctx:MeshrModuleParser.EntityFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#entityAspects.
    def visitEntityAspects(self, ctx:MeshrModuleParser.EntityAspectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aspectInstanceList.
    def visitAspectInstanceList(self, ctx:MeshrModuleParser.AspectInstanceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aspectInstance.
    def visitAspectInstance(self, ctx:MeshrModuleParser.AspectInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aspectInstanceFieldList.
    def visitAspectInstanceFieldList(self, ctx:MeshrModuleParser.AspectInstanceFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aspectInstanceField.
    def visitAspectInstanceField(self, ctx:MeshrModuleParser.AspectInstanceFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedTypeDecl.
    def visitAnnotatedTypeDecl(self, ctx:MeshrModuleParser.AnnotatedTypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedTypeDecl.
    def visitSealedTypeDecl(self, ctx:MeshrModuleParser.SealedTypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#typeDecl.
    def visitTypeDecl(self, ctx:MeshrModuleParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#baseTypeWithConstraints.
    def visitBaseTypeWithConstraints(self, ctx:MeshrModuleParser.BaseTypeWithConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#stringTypeWithConstraints.
    def visitStringTypeWithConstraints(self, ctx:MeshrModuleParser.StringTypeWithConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#numericTypeWithConstraints.
    def visitNumericTypeWithConstraints(self, ctx:MeshrModuleParser.NumericTypeWithConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#integerTypeWithConstraints.
    def visitIntegerTypeWithConstraints(self, ctx:MeshrModuleParser.IntegerTypeWithConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#floatTypeWithConstraints.
    def visitFloatTypeWithConstraints(self, ctx:MeshrModuleParser.FloatTypeWithConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#numericConstraint.
    def visitNumericConstraint(self, ctx:MeshrModuleParser.NumericConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#temporalTypeWithConstraints.
    def visitTemporalTypeWithConstraints(self, ctx:MeshrModuleParser.TemporalTypeWithConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#temporalType.
    def visitTemporalType(self, ctx:MeshrModuleParser.TemporalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#temporalConstraint.
    def visitTemporalConstraint(self, ctx:MeshrModuleParser.TemporalConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#temporalLiteral.
    def visitTemporalLiteral(self, ctx:MeshrModuleParser.TemporalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#otherTypeWithConstraints.
    def visitOtherTypeWithConstraints(self, ctx:MeshrModuleParser.OtherTypeWithConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#otherType.
    def visitOtherType(self, ctx:MeshrModuleParser.OtherTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#otherConstraint.
    def visitOtherConstraint(self, ctx:MeshrModuleParser.OtherConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedTypeRelationDecl.
    def visitAnnotatedTypeRelationDecl(self, ctx:MeshrModuleParser.AnnotatedTypeRelationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedTypeRelationDecl.
    def visitSealedTypeRelationDecl(self, ctx:MeshrModuleParser.SealedTypeRelationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#typeRelationDecl.
    def visitTypeRelationDecl(self, ctx:MeshrModuleParser.TypeRelationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#typeRelationFieldList.
    def visitTypeRelationFieldList(self, ctx:MeshrModuleParser.TypeRelationFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#typeRelationField.
    def visitTypeRelationField(self, ctx:MeshrModuleParser.TypeRelationFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#typeRelationAspects.
    def visitTypeRelationAspects(self, ctx:MeshrModuleParser.TypeRelationAspectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedRelationDecl.
    def visitAnnotatedRelationDecl(self, ctx:MeshrModuleParser.AnnotatedRelationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedRelationDecl.
    def visitSealedRelationDecl(self, ctx:MeshrModuleParser.SealedRelationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#relationDecl.
    def visitRelationDecl(self, ctx:MeshrModuleParser.RelationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#relationType.
    def visitRelationType(self, ctx:MeshrModuleParser.RelationTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#relationEndpoints.
    def visitRelationEndpoints(self, ctx:MeshrModuleParser.RelationEndpointsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#relationEndpoint.
    def visitRelationEndpoint(self, ctx:MeshrModuleParser.RelationEndpointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#relationFieldList.
    def visitRelationFieldList(self, ctx:MeshrModuleParser.RelationFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#relationField.
    def visitRelationField(self, ctx:MeshrModuleParser.RelationFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#relationAspects.
    def visitRelationAspects(self, ctx:MeshrModuleParser.RelationAspectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedAnnotationDecl.
    def visitAnnotatedAnnotationDecl(self, ctx:MeshrModuleParser.AnnotatedAnnotationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotationDecl.
    def visitAnnotationDecl(self, ctx:MeshrModuleParser.AnnotationDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotationFieldList.
    def visitAnnotationFieldList(self, ctx:MeshrModuleParser.AnnotationFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotationField.
    def visitAnnotationField(self, ctx:MeshrModuleParser.AnnotationFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotation.
    def visitAnnotation(self, ctx:MeshrModuleParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotationArgs.
    def visitAnnotationArgs(self, ctx:MeshrModuleParser.AnnotationArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotationArg.
    def visitAnnotationArg(self, ctx:MeshrModuleParser.AnnotationArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotationArgPair.
    def visitAnnotationArgPair(self, ctx:MeshrModuleParser.AnnotationArgPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#baseType.
    def visitBaseType(self, ctx:MeshrModuleParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#stringType.
    def visitStringType(self, ctx:MeshrModuleParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#stringConstraints.
    def visitStringConstraints(self, ctx:MeshrModuleParser.StringConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#stringConstraint.
    def visitStringConstraint(self, ctx:MeshrModuleParser.StringConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#qualifiedName.
    def visitQualifiedName(self, ctx:MeshrModuleParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#typeRef.
    def visitTypeRef(self, ctx:MeshrModuleParser.TypeRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#listType.
    def visitListType(self, ctx:MeshrModuleParser.ListTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#mapType.
    def visitMapType(self, ctx:MeshrModuleParser.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#rangeType.
    def visitRangeType(self, ctx:MeshrModuleParser.RangeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotationValue.
    def visitAnnotationValue(self, ctx:MeshrModuleParser.AnnotationValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#intervalLiteral.
    def visitIntervalLiteral(self, ctx:MeshrModuleParser.IntervalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#intervalSinglePart.
    def visitIntervalSinglePart(self, ctx:MeshrModuleParser.IntervalSinglePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#intervalUnit.
    def visitIntervalUnit(self, ctx:MeshrModuleParser.IntervalUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#recordDecl.
    def visitRecordDecl(self, ctx:MeshrModuleParser.RecordDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedRecordDecl.
    def visitSealedRecordDecl(self, ctx:MeshrModuleParser.SealedRecordDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#recordFieldList.
    def visitRecordFieldList(self, ctx:MeshrModuleParser.RecordFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#recordField.
    def visitRecordField(self, ctx:MeshrModuleParser.RecordFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#traitDecl.
    def visitTraitDecl(self, ctx:MeshrModuleParser.TraitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedTraitDecl.
    def visitSealedTraitDecl(self, ctx:MeshrModuleParser.SealedTraitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#traitFieldList.
    def visitTraitFieldList(self, ctx:MeshrModuleParser.TraitFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#traitField.
    def visitTraitField(self, ctx:MeshrModuleParser.TraitFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#traitAspects.
    def visitTraitAspects(self, ctx:MeshrModuleParser.TraitAspectsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#withClause.
    def visitWithClause(self, ctx:MeshrModuleParser.WithClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedAspectDecl.
    def visitAnnotatedAspectDecl(self, ctx:MeshrModuleParser.AnnotatedAspectDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aspectDecl.
    def visitAspectDecl(self, ctx:MeshrModuleParser.AspectDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedAspectDecl.
    def visitSealedAspectDecl(self, ctx:MeshrModuleParser.SealedAspectDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aspectInheritance.
    def visitAspectInheritance(self, ctx:MeshrModuleParser.AspectInheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#extendsClause.
    def visitExtendsClause(self, ctx:MeshrModuleParser.ExtendsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aspectFieldList.
    def visitAspectFieldList(self, ctx:MeshrModuleParser.AspectFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aspectField.
    def visitAspectField(self, ctx:MeshrModuleParser.AspectFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#listLiteral.
    def visitListLiteral(self, ctx:MeshrModuleParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#mapLiteral.
    def visitMapLiteral(self, ctx:MeshrModuleParser.MapLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#mapEntry.
    def visitMapEntry(self, ctx:MeshrModuleParser.MapEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#recordLiteral.
    def visitRecordLiteral(self, ctx:MeshrModuleParser.RecordLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#recordLitField.
    def visitRecordLitField(self, ctx:MeshrModuleParser.RecordLitFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#rangeLiteral.
    def visitRangeLiteral(self, ctx:MeshrModuleParser.RangeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#jsonLiteral.
    def visitJsonLiteral(self, ctx:MeshrModuleParser.JsonLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#jsonObjectContent.
    def visitJsonObjectContent(self, ctx:MeshrModuleParser.JsonObjectContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#jsonArrayContent.
    def visitJsonArrayContent(self, ctx:MeshrModuleParser.JsonArrayContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#jsonPair.
    def visitJsonPair(self, ctx:MeshrModuleParser.JsonPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#jsonValue.
    def visitJsonValue(self, ctx:MeshrModuleParser.JsonValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#signedNumber.
    def visitSignedNumber(self, ctx:MeshrModuleParser.SignedNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#geographyLiteral.
    def visitGeographyLiteral(self, ctx:MeshrModuleParser.GeographyLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#bytesLiteral.
    def visitBytesLiteral(self, ctx:MeshrModuleParser.BytesLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#bytesArrayContent.
    def visitBytesArrayContent(self, ctx:MeshrModuleParser.BytesArrayContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#bytesValue.
    def visitBytesValue(self, ctx:MeshrModuleParser.BytesValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#datetimeLiteral.
    def visitDatetimeLiteral(self, ctx:MeshrModuleParser.DatetimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#dateLiteral.
    def visitDateLiteral(self, ctx:MeshrModuleParser.DateLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#timeLiteral.
    def visitTimeLiteral(self, ctx:MeshrModuleParser.TimeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#timestampLiteral.
    def visitTimestampLiteral(self, ctx:MeshrModuleParser.TimestampLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sqlLiteral.
    def visitSqlLiteral(self, ctx:MeshrModuleParser.SqlLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#MultiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:MeshrModuleParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:MeshrModuleParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#FieldReferenceExpr.
    def visitFieldReferenceExpr(self, ctx:MeshrModuleParser.FieldReferenceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#AdditiveExpr.
    def visitAdditiveExpr(self, ctx:MeshrModuleParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#ComparisonExpr.
    def visitComparisonExpr(self, ctx:MeshrModuleParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#WhereExpr.
    def visitWhereExpr(self, ctx:MeshrModuleParser.WhereExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#LiteralExpr.
    def visitLiteralExpr(self, ctx:MeshrModuleParser.LiteralExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#ParenthesizedExpr.
    def visitParenthesizedExpr(self, ctx:MeshrModuleParser.ParenthesizedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#InExpr.
    def visitInExpr(self, ctx:MeshrModuleParser.InExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#LogicalExpr.
    def visitLogicalExpr(self, ctx:MeshrModuleParser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#EnumReferenceExpr.
    def visitEnumReferenceExpr(self, ctx:MeshrModuleParser.EnumReferenceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#functionCall.
    def visitFunctionCall(self, ctx:MeshrModuleParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#fieldReference.
    def visitFieldReference(self, ctx:MeshrModuleParser.FieldReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumReference.
    def visitEnumReference(self, ctx:MeshrModuleParser.EnumReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#literal.
    def visitLiteral(self, ctx:MeshrModuleParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#annotatedMetricDecl.
    def visitAnnotatedMetricDecl(self, ctx:MeshrModuleParser.AnnotatedMetricDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#sealedMetricDecl.
    def visitSealedMetricDecl(self, ctx:MeshrModuleParser.SealedMetricDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricDecl.
    def visitMetricDecl(self, ctx:MeshrModuleParser.MetricDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricSource.
    def visitMetricSource(self, ctx:MeshrModuleParser.MetricSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricCalculation.
    def visitMetricCalculation(self, ctx:MeshrModuleParser.MetricCalculationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricAggregation.
    def visitMetricAggregation(self, ctx:MeshrModuleParser.MetricAggregationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aggregationFieldList.
    def visitAggregationFieldList(self, ctx:MeshrModuleParser.AggregationFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#aggregationField.
    def visitAggregationField(self, ctx:MeshrModuleParser.AggregationFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricUnit.
    def visitMetricUnit(self, ctx:MeshrModuleParser.MetricUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricOutputs.
    def visitMetricOutputs(self, ctx:MeshrModuleParser.MetricOutputsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#outputFieldList.
    def visitOutputFieldList(self, ctx:MeshrModuleParser.OutputFieldListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#outputField.
    def visitOutputField(self, ctx:MeshrModuleParser.OutputFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricDimensions.
    def visitMetricDimensions(self, ctx:MeshrModuleParser.MetricDimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#dimensionList.
    def visitDimensionList(self, ctx:MeshrModuleParser.DimensionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#dimension.
    def visitDimension(self, ctx:MeshrModuleParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#matchExpression.
    def visitMatchExpression(self, ctx:MeshrModuleParser.MatchExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#matchArms.
    def visitMatchArms(self, ctx:MeshrModuleParser.MatchArmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#matchArm.
    def visitMatchArm(self, ctx:MeshrModuleParser.MatchArmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#pattern.
    def visitPattern(self, ctx:MeshrModuleParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#orPattern.
    def visitOrPattern(self, ctx:MeshrModuleParser.OrPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#basicPattern.
    def visitBasicPattern(self, ctx:MeshrModuleParser.BasicPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#literalPattern.
    def visitLiteralPattern(self, ctx:MeshrModuleParser.LiteralPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#rangePattern.
    def visitRangePattern(self, ctx:MeshrModuleParser.RangePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#enumPattern.
    def visitEnumPattern(self, ctx:MeshrModuleParser.EnumPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#wildcardPattern.
    def visitWildcardPattern(self, ctx:MeshrModuleParser.WildcardPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#matchResult.
    def visitMatchResult(self, ctx:MeshrModuleParser.MatchResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricFilters.
    def visitMetricFilters(self, ctx:MeshrModuleParser.MetricFiltersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#filterList.
    def visitFilterList(self, ctx:MeshrModuleParser.FilterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#filterExpression.
    def visitFilterExpression(self, ctx:MeshrModuleParser.FilterExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricTemporal.
    def visitMetricTemporal(self, ctx:MeshrModuleParser.MetricTemporalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#temporalConfigList.
    def visitTemporalConfigList(self, ctx:MeshrModuleParser.TemporalConfigListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#temporalConfig.
    def visitTemporalConfig(self, ctx:MeshrModuleParser.TemporalConfigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#temporalField.
    def visitTemporalField(self, ctx:MeshrModuleParser.TemporalFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MeshrModuleParser#metricAspects.
    def visitMetricAspects(self, ctx:MeshrModuleParser.MetricAspectsContext):
        return self.visitChildren(ctx)



del MeshrModuleParser