"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
const vscode = require("vscode");
function activate(context) {
    console.log('Extension Meshr-Lang ULTRA SIMPLE activée !');
    // Message immédiat
    vscode.window.showInformationMessage('🎉 Extension Meshr-Lang ULTRA SIMPLE activée !');
    // Commande simple
    const disposable = vscode.commands.registerCommand('meshr-lang.test', () => {
        vscode.window.showInformationMessage('✅ Commande testée !');
    });
    context.subscriptions.push(disposable);
    // Diagnostic simple
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr');
    context.subscriptions.push(diagnosticCollection);
    // Analyser les documents
    const analyzeDocument = (document) => {
        if (document.languageId === 'meshr') {
            const diagnostic = new vscode.Diagnostic(new vscode.Range(0, 0, 0, 1), 'Extension ULTRA SIMPLE fonctionne !', vscode.DiagnosticSeverity.Information);
            diagnosticCollection.set(document.uri, [diagnostic]);
        }
    };
    // Écouter les documents
    vscode.workspace.textDocuments.forEach(analyzeDocument);
    vscode.workspace.onDidOpenTextDocument(analyzeDocument);
    vscode.workspace.onDidChangeTextDocument(event => {
        analyzeDocument(event.document);
    });
}
exports.activate = activate;
function deactivate() {
    console.log('Extension Meshr-Lang ULTRA SIMPLE désactivée');
}
exports.deactivate = deactivate;
