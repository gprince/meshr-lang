"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = __importStar(require("vscode"));
function activate(context) {
    console.log('🚀 Extension Meshr-Lang TEST activée !');
    // Message immédiat
    vscode.window.showInformationMessage('✅ Extension Meshr-Lang TEST activée !');
    // Commande de test
    const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
        vscode.window.showInformationMessage('🎯 Commande testée avec succès !');
    });
    context.subscriptions.push(testCommand);
    // Diagnostic simple
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr-lang-test');
    context.subscriptions.push(diagnosticCollection);
    const provideDiagnostics = (document) => {
        if (document.languageId === 'meshr') {
            const diagnostics = [];
            const line = document.lineAt(0);
            const diagnostic = new vscode.Diagnostic(new vscode.Range(0, 0, 0, line.text.length), '✅ Extension TEST fonctionne !', vscode.DiagnosticSeverity.Information);
            diagnostics.push(diagnostic);
            diagnosticCollection.set(document.uri, diagnostics);
        }
    };
    vscode.workspace.onDidOpenTextDocument(provideDiagnostics);
    vscode.workspace.onDidChangeTextDocument(event => provideDiagnostics(event.document));
    vscode.workspace.textDocuments.forEach(provideDiagnostics);
    console.log('✅ Extension TEST complètement initialisée');
}
exports.activate = activate;
function deactivate() {
    console.log('🛑 Extension Meshr-Lang TEST désactivée');
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension_test.js.map