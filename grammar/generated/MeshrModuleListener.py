# Generated from MeshrModule.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MeshrModuleParser import MeshrModuleParser
else:
    from MeshrModuleParser import MeshrModuleParser

# This class defines a complete listener for a parse tree produced by MeshrModuleParser.
class MeshrModuleListener(ParseTreeListener):

    # Enter a parse tree produced by MeshrModuleParser#compilationUnit.
    def enterCompilationUnit(self, ctx:MeshrModuleParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#compilationUnit.
    def exitCompilationUnit(self, ctx:MeshrModuleParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotatedModuleDecl.
    def enterAnnotatedModuleDecl(self, ctx:MeshrModuleParser.AnnotatedModuleDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotatedModuleDecl.
    def exitAnnotatedModuleDecl(self, ctx:MeshrModuleParser.AnnotatedModuleDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#importDecl.
    def enterImportDecl(self, ctx:MeshrModuleParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#importDecl.
    def exitImportDecl(self, ctx:MeshrModuleParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#SingleImport.
    def enterSingleImport(self, ctx:MeshrModuleParser.SingleImportContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#SingleImport.
    def exitSingleImport(self, ctx:MeshrModuleParser.SingleImportContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#WildcardImport.
    def enterWildcardImport(self, ctx:MeshrModuleParser.WildcardImportContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#WildcardImport.
    def exitWildcardImport(self, ctx:MeshrModuleParser.WildcardImportContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#GroupImport.
    def enterGroupImport(self, ctx:MeshrModuleParser.GroupImportContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#GroupImport.
    def exitGroupImport(self, ctx:MeshrModuleParser.GroupImportContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#importItems.
    def enterImportItems(self, ctx:MeshrModuleParser.ImportItemsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#importItems.
    def exitImportItems(self, ctx:MeshrModuleParser.ImportItemsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#InlineExport.
    def enterInlineExport(self, ctx:MeshrModuleParser.InlineExportContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#InlineExport.
    def exitInlineExport(self, ctx:MeshrModuleParser.InlineExportContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#GroupedExport.
    def enterGroupedExport(self, ctx:MeshrModuleParser.GroupedExportContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#GroupedExport.
    def exitGroupedExport(self, ctx:MeshrModuleParser.GroupedExportContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#exportItems.
    def enterExportItems(self, ctx:MeshrModuleParser.ExportItemsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#exportItems.
    def exitExportItems(self, ctx:MeshrModuleParser.ExportItemsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#topLevelDecl.
    def enterTopLevelDecl(self, ctx:MeshrModuleParser.TopLevelDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#topLevelDecl.
    def exitTopLevelDecl(self, ctx:MeshrModuleParser.TopLevelDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#exportableDecl.
    def enterExportableDecl(self, ctx:MeshrModuleParser.ExportableDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#exportableDecl.
    def exitExportableDecl(self, ctx:MeshrModuleParser.ExportableDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotatedEnumDecl.
    def enterAnnotatedEnumDecl(self, ctx:MeshrModuleParser.AnnotatedEnumDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotatedEnumDecl.
    def exitAnnotatedEnumDecl(self, ctx:MeshrModuleParser.AnnotatedEnumDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sealedEnumDecl.
    def enterSealedEnumDecl(self, ctx:MeshrModuleParser.SealedEnumDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sealedEnumDecl.
    def exitSealedEnumDecl(self, ctx:MeshrModuleParser.SealedEnumDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotatedEntityDecl.
    def enterAnnotatedEntityDecl(self, ctx:MeshrModuleParser.AnnotatedEntityDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotatedEntityDecl.
    def exitAnnotatedEntityDecl(self, ctx:MeshrModuleParser.AnnotatedEntityDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sealedEntityDecl.
    def enterSealedEntityDecl(self, ctx:MeshrModuleParser.SealedEntityDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sealedEntityDecl.
    def exitSealedEntityDecl(self, ctx:MeshrModuleParser.SealedEntityDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumDecl.
    def enterEnumDecl(self, ctx:MeshrModuleParser.EnumDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumDecl.
    def exitEnumDecl(self, ctx:MeshrModuleParser.EnumDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumSignature.
    def enterEnumSignature(self, ctx:MeshrModuleParser.EnumSignatureContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumSignature.
    def exitEnumSignature(self, ctx:MeshrModuleParser.EnumSignatureContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumAttributeList.
    def enterEnumAttributeList(self, ctx:MeshrModuleParser.EnumAttributeListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumAttributeList.
    def exitEnumAttributeList(self, ctx:MeshrModuleParser.EnumAttributeListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumAttribute.
    def enterEnumAttribute(self, ctx:MeshrModuleParser.EnumAttributeContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumAttribute.
    def exitEnumAttribute(self, ctx:MeshrModuleParser.EnumAttributeContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumValueList.
    def enterEnumValueList(self, ctx:MeshrModuleParser.EnumValueListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumValueList.
    def exitEnumValueList(self, ctx:MeshrModuleParser.EnumValueListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumValue.
    def enterEnumValue(self, ctx:MeshrModuleParser.EnumValueContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumValue.
    def exitEnumValue(self, ctx:MeshrModuleParser.EnumValueContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumValueArgList.
    def enterEnumValueArgList(self, ctx:MeshrModuleParser.EnumValueArgListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumValueArgList.
    def exitEnumValueArgList(self, ctx:MeshrModuleParser.EnumValueArgListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumValueArg.
    def enterEnumValueArg(self, ctx:MeshrModuleParser.EnumValueArgContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumValueArg.
    def exitEnumValueArg(self, ctx:MeshrModuleParser.EnumValueArgContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#entityDecl.
    def enterEntityDecl(self, ctx:MeshrModuleParser.EntityDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#entityDecl.
    def exitEntityDecl(self, ctx:MeshrModuleParser.EntityDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#entityFieldList.
    def enterEntityFieldList(self, ctx:MeshrModuleParser.EntityFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#entityFieldList.
    def exitEntityFieldList(self, ctx:MeshrModuleParser.EntityFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#entityField.
    def enterEntityField(self, ctx:MeshrModuleParser.EntityFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#entityField.
    def exitEntityField(self, ctx:MeshrModuleParser.EntityFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#entityAspects.
    def enterEntityAspects(self, ctx:MeshrModuleParser.EntityAspectsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#entityAspects.
    def exitEntityAspects(self, ctx:MeshrModuleParser.EntityAspectsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aspectInstanceList.
    def enterAspectInstanceList(self, ctx:MeshrModuleParser.AspectInstanceListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aspectInstanceList.
    def exitAspectInstanceList(self, ctx:MeshrModuleParser.AspectInstanceListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aspectInstance.
    def enterAspectInstance(self, ctx:MeshrModuleParser.AspectInstanceContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aspectInstance.
    def exitAspectInstance(self, ctx:MeshrModuleParser.AspectInstanceContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aspectInstanceFieldList.
    def enterAspectInstanceFieldList(self, ctx:MeshrModuleParser.AspectInstanceFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aspectInstanceFieldList.
    def exitAspectInstanceFieldList(self, ctx:MeshrModuleParser.AspectInstanceFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aspectInstanceField.
    def enterAspectInstanceField(self, ctx:MeshrModuleParser.AspectInstanceFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aspectInstanceField.
    def exitAspectInstanceField(self, ctx:MeshrModuleParser.AspectInstanceFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotatedTypeRelationDecl.
    def enterAnnotatedTypeRelationDecl(self, ctx:MeshrModuleParser.AnnotatedTypeRelationDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotatedTypeRelationDecl.
    def exitAnnotatedTypeRelationDecl(self, ctx:MeshrModuleParser.AnnotatedTypeRelationDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sealedTypeRelationDecl.
    def enterSealedTypeRelationDecl(self, ctx:MeshrModuleParser.SealedTypeRelationDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sealedTypeRelationDecl.
    def exitSealedTypeRelationDecl(self, ctx:MeshrModuleParser.SealedTypeRelationDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#typeRelationDecl.
    def enterTypeRelationDecl(self, ctx:MeshrModuleParser.TypeRelationDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#typeRelationDecl.
    def exitTypeRelationDecl(self, ctx:MeshrModuleParser.TypeRelationDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#typeRelationFieldList.
    def enterTypeRelationFieldList(self, ctx:MeshrModuleParser.TypeRelationFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#typeRelationFieldList.
    def exitTypeRelationFieldList(self, ctx:MeshrModuleParser.TypeRelationFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#typeRelationField.
    def enterTypeRelationField(self, ctx:MeshrModuleParser.TypeRelationFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#typeRelationField.
    def exitTypeRelationField(self, ctx:MeshrModuleParser.TypeRelationFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#typeRelationAspects.
    def enterTypeRelationAspects(self, ctx:MeshrModuleParser.TypeRelationAspectsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#typeRelationAspects.
    def exitTypeRelationAspects(self, ctx:MeshrModuleParser.TypeRelationAspectsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotatedRelationDecl.
    def enterAnnotatedRelationDecl(self, ctx:MeshrModuleParser.AnnotatedRelationDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotatedRelationDecl.
    def exitAnnotatedRelationDecl(self, ctx:MeshrModuleParser.AnnotatedRelationDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sealedRelationDecl.
    def enterSealedRelationDecl(self, ctx:MeshrModuleParser.SealedRelationDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sealedRelationDecl.
    def exitSealedRelationDecl(self, ctx:MeshrModuleParser.SealedRelationDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#relationDecl.
    def enterRelationDecl(self, ctx:MeshrModuleParser.RelationDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#relationDecl.
    def exitRelationDecl(self, ctx:MeshrModuleParser.RelationDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#relationType.
    def enterRelationType(self, ctx:MeshrModuleParser.RelationTypeContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#relationType.
    def exitRelationType(self, ctx:MeshrModuleParser.RelationTypeContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#relationEndpoints.
    def enterRelationEndpoints(self, ctx:MeshrModuleParser.RelationEndpointsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#relationEndpoints.
    def exitRelationEndpoints(self, ctx:MeshrModuleParser.RelationEndpointsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#relationEndpoint.
    def enterRelationEndpoint(self, ctx:MeshrModuleParser.RelationEndpointContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#relationEndpoint.
    def exitRelationEndpoint(self, ctx:MeshrModuleParser.RelationEndpointContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#relationFieldList.
    def enterRelationFieldList(self, ctx:MeshrModuleParser.RelationFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#relationFieldList.
    def exitRelationFieldList(self, ctx:MeshrModuleParser.RelationFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#relationField.
    def enterRelationField(self, ctx:MeshrModuleParser.RelationFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#relationField.
    def exitRelationField(self, ctx:MeshrModuleParser.RelationFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#relationAspects.
    def enterRelationAspects(self, ctx:MeshrModuleParser.RelationAspectsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#relationAspects.
    def exitRelationAspects(self, ctx:MeshrModuleParser.RelationAspectsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotatedAnnotationDecl.
    def enterAnnotatedAnnotationDecl(self, ctx:MeshrModuleParser.AnnotatedAnnotationDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotatedAnnotationDecl.
    def exitAnnotatedAnnotationDecl(self, ctx:MeshrModuleParser.AnnotatedAnnotationDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotationDecl.
    def enterAnnotationDecl(self, ctx:MeshrModuleParser.AnnotationDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotationDecl.
    def exitAnnotationDecl(self, ctx:MeshrModuleParser.AnnotationDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotationFieldList.
    def enterAnnotationFieldList(self, ctx:MeshrModuleParser.AnnotationFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotationFieldList.
    def exitAnnotationFieldList(self, ctx:MeshrModuleParser.AnnotationFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotationField.
    def enterAnnotationField(self, ctx:MeshrModuleParser.AnnotationFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotationField.
    def exitAnnotationField(self, ctx:MeshrModuleParser.AnnotationFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotation.
    def enterAnnotation(self, ctx:MeshrModuleParser.AnnotationContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotation.
    def exitAnnotation(self, ctx:MeshrModuleParser.AnnotationContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotationArgs.
    def enterAnnotationArgs(self, ctx:MeshrModuleParser.AnnotationArgsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotationArgs.
    def exitAnnotationArgs(self, ctx:MeshrModuleParser.AnnotationArgsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotationArg.
    def enterAnnotationArg(self, ctx:MeshrModuleParser.AnnotationArgContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotationArg.
    def exitAnnotationArg(self, ctx:MeshrModuleParser.AnnotationArgContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotationArgPair.
    def enterAnnotationArgPair(self, ctx:MeshrModuleParser.AnnotationArgPairContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotationArgPair.
    def exitAnnotationArgPair(self, ctx:MeshrModuleParser.AnnotationArgPairContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#baseType.
    def enterBaseType(self, ctx:MeshrModuleParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#baseType.
    def exitBaseType(self, ctx:MeshrModuleParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#stringType.
    def enterStringType(self, ctx:MeshrModuleParser.StringTypeContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#stringType.
    def exitStringType(self, ctx:MeshrModuleParser.StringTypeContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#stringConstraints.
    def enterStringConstraints(self, ctx:MeshrModuleParser.StringConstraintsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#stringConstraints.
    def exitStringConstraints(self, ctx:MeshrModuleParser.StringConstraintsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#stringConstraint.
    def enterStringConstraint(self, ctx:MeshrModuleParser.StringConstraintContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#stringConstraint.
    def exitStringConstraint(self, ctx:MeshrModuleParser.StringConstraintContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#qualifiedName.
    def enterQualifiedName(self, ctx:MeshrModuleParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#qualifiedName.
    def exitQualifiedName(self, ctx:MeshrModuleParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#typeRef.
    def enterTypeRef(self, ctx:MeshrModuleParser.TypeRefContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#typeRef.
    def exitTypeRef(self, ctx:MeshrModuleParser.TypeRefContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#listType.
    def enterListType(self, ctx:MeshrModuleParser.ListTypeContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#listType.
    def exitListType(self, ctx:MeshrModuleParser.ListTypeContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#mapType.
    def enterMapType(self, ctx:MeshrModuleParser.MapTypeContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#mapType.
    def exitMapType(self, ctx:MeshrModuleParser.MapTypeContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#rangeType.
    def enterRangeType(self, ctx:MeshrModuleParser.RangeTypeContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#rangeType.
    def exitRangeType(self, ctx:MeshrModuleParser.RangeTypeContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotationValue.
    def enterAnnotationValue(self, ctx:MeshrModuleParser.AnnotationValueContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotationValue.
    def exitAnnotationValue(self, ctx:MeshrModuleParser.AnnotationValueContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:MeshrModuleParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:MeshrModuleParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#intervalSinglePart.
    def enterIntervalSinglePart(self, ctx:MeshrModuleParser.IntervalSinglePartContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#intervalSinglePart.
    def exitIntervalSinglePart(self, ctx:MeshrModuleParser.IntervalSinglePartContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#intervalUnit.
    def enterIntervalUnit(self, ctx:MeshrModuleParser.IntervalUnitContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#intervalUnit.
    def exitIntervalUnit(self, ctx:MeshrModuleParser.IntervalUnitContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#recordDecl.
    def enterRecordDecl(self, ctx:MeshrModuleParser.RecordDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#recordDecl.
    def exitRecordDecl(self, ctx:MeshrModuleParser.RecordDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sealedRecordDecl.
    def enterSealedRecordDecl(self, ctx:MeshrModuleParser.SealedRecordDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sealedRecordDecl.
    def exitSealedRecordDecl(self, ctx:MeshrModuleParser.SealedRecordDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#recordFieldList.
    def enterRecordFieldList(self, ctx:MeshrModuleParser.RecordFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#recordFieldList.
    def exitRecordFieldList(self, ctx:MeshrModuleParser.RecordFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#recordField.
    def enterRecordField(self, ctx:MeshrModuleParser.RecordFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#recordField.
    def exitRecordField(self, ctx:MeshrModuleParser.RecordFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#traitDecl.
    def enterTraitDecl(self, ctx:MeshrModuleParser.TraitDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#traitDecl.
    def exitTraitDecl(self, ctx:MeshrModuleParser.TraitDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sealedTraitDecl.
    def enterSealedTraitDecl(self, ctx:MeshrModuleParser.SealedTraitDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sealedTraitDecl.
    def exitSealedTraitDecl(self, ctx:MeshrModuleParser.SealedTraitDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#traitFieldList.
    def enterTraitFieldList(self, ctx:MeshrModuleParser.TraitFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#traitFieldList.
    def exitTraitFieldList(self, ctx:MeshrModuleParser.TraitFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#traitField.
    def enterTraitField(self, ctx:MeshrModuleParser.TraitFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#traitField.
    def exitTraitField(self, ctx:MeshrModuleParser.TraitFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#traitAspects.
    def enterTraitAspects(self, ctx:MeshrModuleParser.TraitAspectsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#traitAspects.
    def exitTraitAspects(self, ctx:MeshrModuleParser.TraitAspectsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#withClause.
    def enterWithClause(self, ctx:MeshrModuleParser.WithClauseContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#withClause.
    def exitWithClause(self, ctx:MeshrModuleParser.WithClauseContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotatedAspectDecl.
    def enterAnnotatedAspectDecl(self, ctx:MeshrModuleParser.AnnotatedAspectDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotatedAspectDecl.
    def exitAnnotatedAspectDecl(self, ctx:MeshrModuleParser.AnnotatedAspectDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aspectDecl.
    def enterAspectDecl(self, ctx:MeshrModuleParser.AspectDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aspectDecl.
    def exitAspectDecl(self, ctx:MeshrModuleParser.AspectDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sealedAspectDecl.
    def enterSealedAspectDecl(self, ctx:MeshrModuleParser.SealedAspectDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sealedAspectDecl.
    def exitSealedAspectDecl(self, ctx:MeshrModuleParser.SealedAspectDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aspectInheritance.
    def enterAspectInheritance(self, ctx:MeshrModuleParser.AspectInheritanceContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aspectInheritance.
    def exitAspectInheritance(self, ctx:MeshrModuleParser.AspectInheritanceContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#extendsClause.
    def enterExtendsClause(self, ctx:MeshrModuleParser.ExtendsClauseContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#extendsClause.
    def exitExtendsClause(self, ctx:MeshrModuleParser.ExtendsClauseContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aspectFieldList.
    def enterAspectFieldList(self, ctx:MeshrModuleParser.AspectFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aspectFieldList.
    def exitAspectFieldList(self, ctx:MeshrModuleParser.AspectFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aspectField.
    def enterAspectField(self, ctx:MeshrModuleParser.AspectFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aspectField.
    def exitAspectField(self, ctx:MeshrModuleParser.AspectFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#listLiteral.
    def enterListLiteral(self, ctx:MeshrModuleParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#listLiteral.
    def exitListLiteral(self, ctx:MeshrModuleParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#mapLiteral.
    def enterMapLiteral(self, ctx:MeshrModuleParser.MapLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#mapLiteral.
    def exitMapLiteral(self, ctx:MeshrModuleParser.MapLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#mapEntry.
    def enterMapEntry(self, ctx:MeshrModuleParser.MapEntryContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#mapEntry.
    def exitMapEntry(self, ctx:MeshrModuleParser.MapEntryContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#recordLiteral.
    def enterRecordLiteral(self, ctx:MeshrModuleParser.RecordLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#recordLiteral.
    def exitRecordLiteral(self, ctx:MeshrModuleParser.RecordLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#recordLitField.
    def enterRecordLitField(self, ctx:MeshrModuleParser.RecordLitFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#recordLitField.
    def exitRecordLitField(self, ctx:MeshrModuleParser.RecordLitFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#rangeLiteral.
    def enterRangeLiteral(self, ctx:MeshrModuleParser.RangeLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#rangeLiteral.
    def exitRangeLiteral(self, ctx:MeshrModuleParser.RangeLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#jsonLiteral.
    def enterJsonLiteral(self, ctx:MeshrModuleParser.JsonLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#jsonLiteral.
    def exitJsonLiteral(self, ctx:MeshrModuleParser.JsonLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#jsonObjectContent.
    def enterJsonObjectContent(self, ctx:MeshrModuleParser.JsonObjectContentContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#jsonObjectContent.
    def exitJsonObjectContent(self, ctx:MeshrModuleParser.JsonObjectContentContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#jsonArrayContent.
    def enterJsonArrayContent(self, ctx:MeshrModuleParser.JsonArrayContentContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#jsonArrayContent.
    def exitJsonArrayContent(self, ctx:MeshrModuleParser.JsonArrayContentContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#jsonPair.
    def enterJsonPair(self, ctx:MeshrModuleParser.JsonPairContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#jsonPair.
    def exitJsonPair(self, ctx:MeshrModuleParser.JsonPairContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#jsonValue.
    def enterJsonValue(self, ctx:MeshrModuleParser.JsonValueContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#jsonValue.
    def exitJsonValue(self, ctx:MeshrModuleParser.JsonValueContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#signedNumber.
    def enterSignedNumber(self, ctx:MeshrModuleParser.SignedNumberContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#signedNumber.
    def exitSignedNumber(self, ctx:MeshrModuleParser.SignedNumberContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#geographyLiteral.
    def enterGeographyLiteral(self, ctx:MeshrModuleParser.GeographyLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#geographyLiteral.
    def exitGeographyLiteral(self, ctx:MeshrModuleParser.GeographyLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#bytesLiteral.
    def enterBytesLiteral(self, ctx:MeshrModuleParser.BytesLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#bytesLiteral.
    def exitBytesLiteral(self, ctx:MeshrModuleParser.BytesLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#bytesArrayContent.
    def enterBytesArrayContent(self, ctx:MeshrModuleParser.BytesArrayContentContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#bytesArrayContent.
    def exitBytesArrayContent(self, ctx:MeshrModuleParser.BytesArrayContentContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#bytesValue.
    def enterBytesValue(self, ctx:MeshrModuleParser.BytesValueContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#bytesValue.
    def exitBytesValue(self, ctx:MeshrModuleParser.BytesValueContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#datetimeLiteral.
    def enterDatetimeLiteral(self, ctx:MeshrModuleParser.DatetimeLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#datetimeLiteral.
    def exitDatetimeLiteral(self, ctx:MeshrModuleParser.DatetimeLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#dateLiteral.
    def enterDateLiteral(self, ctx:MeshrModuleParser.DateLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#dateLiteral.
    def exitDateLiteral(self, ctx:MeshrModuleParser.DateLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#timeLiteral.
    def enterTimeLiteral(self, ctx:MeshrModuleParser.TimeLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#timeLiteral.
    def exitTimeLiteral(self, ctx:MeshrModuleParser.TimeLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#timestampLiteral.
    def enterTimestampLiteral(self, ctx:MeshrModuleParser.TimestampLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#timestampLiteral.
    def exitTimestampLiteral(self, ctx:MeshrModuleParser.TimestampLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sqlLiteral.
    def enterSqlLiteral(self, ctx:MeshrModuleParser.SqlLiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sqlLiteral.
    def exitSqlLiteral(self, ctx:MeshrModuleParser.SqlLiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#MultiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:MeshrModuleParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#MultiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:MeshrModuleParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:MeshrModuleParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:MeshrModuleParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#FieldReferenceExpr.
    def enterFieldReferenceExpr(self, ctx:MeshrModuleParser.FieldReferenceExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#FieldReferenceExpr.
    def exitFieldReferenceExpr(self, ctx:MeshrModuleParser.FieldReferenceExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#AdditiveExpr.
    def enterAdditiveExpr(self, ctx:MeshrModuleParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#AdditiveExpr.
    def exitAdditiveExpr(self, ctx:MeshrModuleParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#ComparisonExpr.
    def enterComparisonExpr(self, ctx:MeshrModuleParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#ComparisonExpr.
    def exitComparisonExpr(self, ctx:MeshrModuleParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#WhereExpr.
    def enterWhereExpr(self, ctx:MeshrModuleParser.WhereExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#WhereExpr.
    def exitWhereExpr(self, ctx:MeshrModuleParser.WhereExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:MeshrModuleParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:MeshrModuleParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#ParenthesizedExpr.
    def enterParenthesizedExpr(self, ctx:MeshrModuleParser.ParenthesizedExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#ParenthesizedExpr.
    def exitParenthesizedExpr(self, ctx:MeshrModuleParser.ParenthesizedExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#InExpr.
    def enterInExpr(self, ctx:MeshrModuleParser.InExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#InExpr.
    def exitInExpr(self, ctx:MeshrModuleParser.InExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#LogicalExpr.
    def enterLogicalExpr(self, ctx:MeshrModuleParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#LogicalExpr.
    def exitLogicalExpr(self, ctx:MeshrModuleParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#EnumReferenceExpr.
    def enterEnumReferenceExpr(self, ctx:MeshrModuleParser.EnumReferenceExprContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#EnumReferenceExpr.
    def exitEnumReferenceExpr(self, ctx:MeshrModuleParser.EnumReferenceExprContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#functionCall.
    def enterFunctionCall(self, ctx:MeshrModuleParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#functionCall.
    def exitFunctionCall(self, ctx:MeshrModuleParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#fieldReference.
    def enterFieldReference(self, ctx:MeshrModuleParser.FieldReferenceContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#fieldReference.
    def exitFieldReference(self, ctx:MeshrModuleParser.FieldReferenceContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumReference.
    def enterEnumReference(self, ctx:MeshrModuleParser.EnumReferenceContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumReference.
    def exitEnumReference(self, ctx:MeshrModuleParser.EnumReferenceContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#literal.
    def enterLiteral(self, ctx:MeshrModuleParser.LiteralContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#literal.
    def exitLiteral(self, ctx:MeshrModuleParser.LiteralContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#annotatedMetricDecl.
    def enterAnnotatedMetricDecl(self, ctx:MeshrModuleParser.AnnotatedMetricDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#annotatedMetricDecl.
    def exitAnnotatedMetricDecl(self, ctx:MeshrModuleParser.AnnotatedMetricDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#sealedMetricDecl.
    def enterSealedMetricDecl(self, ctx:MeshrModuleParser.SealedMetricDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#sealedMetricDecl.
    def exitSealedMetricDecl(self, ctx:MeshrModuleParser.SealedMetricDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricDecl.
    def enterMetricDecl(self, ctx:MeshrModuleParser.MetricDeclContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricDecl.
    def exitMetricDecl(self, ctx:MeshrModuleParser.MetricDeclContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricSource.
    def enterMetricSource(self, ctx:MeshrModuleParser.MetricSourceContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricSource.
    def exitMetricSource(self, ctx:MeshrModuleParser.MetricSourceContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricCalculation.
    def enterMetricCalculation(self, ctx:MeshrModuleParser.MetricCalculationContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricCalculation.
    def exitMetricCalculation(self, ctx:MeshrModuleParser.MetricCalculationContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricAggregation.
    def enterMetricAggregation(self, ctx:MeshrModuleParser.MetricAggregationContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricAggregation.
    def exitMetricAggregation(self, ctx:MeshrModuleParser.MetricAggregationContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aggregationFieldList.
    def enterAggregationFieldList(self, ctx:MeshrModuleParser.AggregationFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aggregationFieldList.
    def exitAggregationFieldList(self, ctx:MeshrModuleParser.AggregationFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#aggregationField.
    def enterAggregationField(self, ctx:MeshrModuleParser.AggregationFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#aggregationField.
    def exitAggregationField(self, ctx:MeshrModuleParser.AggregationFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricUnit.
    def enterMetricUnit(self, ctx:MeshrModuleParser.MetricUnitContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricUnit.
    def exitMetricUnit(self, ctx:MeshrModuleParser.MetricUnitContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricOutputs.
    def enterMetricOutputs(self, ctx:MeshrModuleParser.MetricOutputsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricOutputs.
    def exitMetricOutputs(self, ctx:MeshrModuleParser.MetricOutputsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#outputFieldList.
    def enterOutputFieldList(self, ctx:MeshrModuleParser.OutputFieldListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#outputFieldList.
    def exitOutputFieldList(self, ctx:MeshrModuleParser.OutputFieldListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#outputField.
    def enterOutputField(self, ctx:MeshrModuleParser.OutputFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#outputField.
    def exitOutputField(self, ctx:MeshrModuleParser.OutputFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricDimensions.
    def enterMetricDimensions(self, ctx:MeshrModuleParser.MetricDimensionsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricDimensions.
    def exitMetricDimensions(self, ctx:MeshrModuleParser.MetricDimensionsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#dimensionList.
    def enterDimensionList(self, ctx:MeshrModuleParser.DimensionListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#dimensionList.
    def exitDimensionList(self, ctx:MeshrModuleParser.DimensionListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#dimension.
    def enterDimension(self, ctx:MeshrModuleParser.DimensionContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#dimension.
    def exitDimension(self, ctx:MeshrModuleParser.DimensionContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#matchExpression.
    def enterMatchExpression(self, ctx:MeshrModuleParser.MatchExpressionContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#matchExpression.
    def exitMatchExpression(self, ctx:MeshrModuleParser.MatchExpressionContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#matchArms.
    def enterMatchArms(self, ctx:MeshrModuleParser.MatchArmsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#matchArms.
    def exitMatchArms(self, ctx:MeshrModuleParser.MatchArmsContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#matchArm.
    def enterMatchArm(self, ctx:MeshrModuleParser.MatchArmContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#matchArm.
    def exitMatchArm(self, ctx:MeshrModuleParser.MatchArmContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#pattern.
    def enterPattern(self, ctx:MeshrModuleParser.PatternContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#pattern.
    def exitPattern(self, ctx:MeshrModuleParser.PatternContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#orPattern.
    def enterOrPattern(self, ctx:MeshrModuleParser.OrPatternContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#orPattern.
    def exitOrPattern(self, ctx:MeshrModuleParser.OrPatternContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#basicPattern.
    def enterBasicPattern(self, ctx:MeshrModuleParser.BasicPatternContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#basicPattern.
    def exitBasicPattern(self, ctx:MeshrModuleParser.BasicPatternContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#literalPattern.
    def enterLiteralPattern(self, ctx:MeshrModuleParser.LiteralPatternContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#literalPattern.
    def exitLiteralPattern(self, ctx:MeshrModuleParser.LiteralPatternContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#rangePattern.
    def enterRangePattern(self, ctx:MeshrModuleParser.RangePatternContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#rangePattern.
    def exitRangePattern(self, ctx:MeshrModuleParser.RangePatternContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#enumPattern.
    def enterEnumPattern(self, ctx:MeshrModuleParser.EnumPatternContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#enumPattern.
    def exitEnumPattern(self, ctx:MeshrModuleParser.EnumPatternContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#wildcardPattern.
    def enterWildcardPattern(self, ctx:MeshrModuleParser.WildcardPatternContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#wildcardPattern.
    def exitWildcardPattern(self, ctx:MeshrModuleParser.WildcardPatternContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#matchResult.
    def enterMatchResult(self, ctx:MeshrModuleParser.MatchResultContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#matchResult.
    def exitMatchResult(self, ctx:MeshrModuleParser.MatchResultContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricFilters.
    def enterMetricFilters(self, ctx:MeshrModuleParser.MetricFiltersContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricFilters.
    def exitMetricFilters(self, ctx:MeshrModuleParser.MetricFiltersContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#filterList.
    def enterFilterList(self, ctx:MeshrModuleParser.FilterListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#filterList.
    def exitFilterList(self, ctx:MeshrModuleParser.FilterListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#filterExpression.
    def enterFilterExpression(self, ctx:MeshrModuleParser.FilterExpressionContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#filterExpression.
    def exitFilterExpression(self, ctx:MeshrModuleParser.FilterExpressionContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricTemporal.
    def enterMetricTemporal(self, ctx:MeshrModuleParser.MetricTemporalContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricTemporal.
    def exitMetricTemporal(self, ctx:MeshrModuleParser.MetricTemporalContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#temporalConfigList.
    def enterTemporalConfigList(self, ctx:MeshrModuleParser.TemporalConfigListContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#temporalConfigList.
    def exitTemporalConfigList(self, ctx:MeshrModuleParser.TemporalConfigListContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#temporalConfig.
    def enterTemporalConfig(self, ctx:MeshrModuleParser.TemporalConfigContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#temporalConfig.
    def exitTemporalConfig(self, ctx:MeshrModuleParser.TemporalConfigContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#temporalField.
    def enterTemporalField(self, ctx:MeshrModuleParser.TemporalFieldContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#temporalField.
    def exitTemporalField(self, ctx:MeshrModuleParser.TemporalFieldContext):
        pass


    # Enter a parse tree produced by MeshrModuleParser#metricAspects.
    def enterMetricAspects(self, ctx:MeshrModuleParser.MetricAspectsContext):
        pass

    # Exit a parse tree produced by MeshrModuleParser#metricAspects.
    def exitMetricAspects(self, ctx:MeshrModuleParser.MetricAspectsContext):
        pass



del MeshrModuleParser