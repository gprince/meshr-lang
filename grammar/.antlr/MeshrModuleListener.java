// Generated from /Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/grammar/MeshrModule.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MeshrModuleParser}.
 */
public interface MeshrModuleListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MeshrModuleParser#moduleDecl}.
	 * @param ctx the parse tree
	 */
	void enterModuleDecl(MeshrModuleParser.ModuleDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MeshrModuleParser#moduleDecl}.
	 * @param ctx the parse tree
	 */
	void exitModuleDecl(MeshrModuleParser.ModuleDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MeshrModuleParser#importDecl}.
	 * @param ctx the parse tree
	 */
	void enterImportDecl(MeshrModuleParser.ImportDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MeshrModuleParser#importDecl}.
	 * @param ctx the parse tree
	 */
	void exitImportDecl(MeshrModuleParser.ImportDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MeshrModuleParser#annotation}.
	 * @param ctx the parse tree
	 */
	void enterAnnotation(MeshrModuleParser.AnnotationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MeshrModuleParser#annotation}.
	 * @param ctx the parse tree
	 */
	void exitAnnotation(MeshrModuleParser.AnnotationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MeshrModuleParser#qualifiedName}.
	 * @param ctx the parse tree
	 */
	void enterQualifiedName(MeshrModuleParser.QualifiedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link MeshrModuleParser#qualifiedName}.
	 * @param ctx the parse tree
	 */
	void exitQualifiedName(MeshrModuleParser.QualifiedNameContext ctx);
}