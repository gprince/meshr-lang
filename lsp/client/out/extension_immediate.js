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
    console.log('Extension Meshr-Lang activée !');
    // Afficher un message de confirmation immédiatement
    vscode.window.showInformationMessage('🎉 Extension Meshr-Lang activée !');
    // Enregistrer une commande de test
    const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
        vscode.window.showInformationMessage('✅ Commande Meshr-Lang testée avec succès !');
    });
    context.subscriptions.push(testCommand);
    // Créer un diagnostic simple pour tous les fichiers .meshr
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr');
    context.subscriptions.push(diagnosticCollection);
    // Fonction pour analyser un document
    const analyzeDocument = (document) => {
        if (document.languageId === 'meshr') {
            const diagnostics = [];
            // Créer un diagnostic simple
            const diagnostic = new vscode.Diagnostic(new vscode.Range(0, 0, 0, 1), 'Extension Meshr-Lang fonctionne ! Diagnostic de test.', vscode.DiagnosticSeverity.Information);
            diagnostics.push(diagnostic);
            // Ajouter des diagnostics pour les erreurs évidentes
            const text = document.getText();
            const lines = text.split('\n');
            for (let i = 0; i < lines.length; i++) {
                const line = lines[i];
                if (line.includes('!%£$%')) {
                    const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Caractères invalides détectés !', vscode.DiagnosticSeverity.Error);
                    diagnostics.push(diagnostic);
                }
            }
            diagnosticCollection.set(document.uri, diagnostics);
        }
    };
    // Analyser les documents ouverts
    vscode.workspace.textDocuments.forEach(analyzeDocument);
    // Écouter l'ouverture de nouveaux documents
    vscode.workspace.onDidOpenTextDocument(analyzeDocument);
    // Écouter les changements de documents
    vscode.workspace.onDidChangeTextDocument(event => {
        analyzeDocument(event.document);
    });
}
exports.activate = activate;
function deactivate() {
    console.log('Extension Meshr-Lang désactivée');
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension_immediate.js.map