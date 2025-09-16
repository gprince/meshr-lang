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
    // Afficher un message de confirmation
    vscode.window.showInformationMessage('Extension Meshr-Lang activée !');
    // Enregistrer une commande simple pour tester
    const disposable = vscode.commands.registerCommand('meshr-lang.test', () => {
        vscode.window.showInformationMessage('Commande Meshr-Lang testée !');
    });
    context.subscriptions.push(disposable);
    // Créer un diagnostic simple pour tester
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr');
    context.subscriptions.push(diagnosticCollection);
    // Écouter les changements de documents
    vscode.workspace.onDidChangeTextDocument(event => {
        if (event.document.languageId === 'meshr') {
            // Créer un diagnostic simple
            const diagnostic = new vscode.Diagnostic(new vscode.Range(0, 0, 0, 1), 'Test diagnostic - Extension Meshr-Lang fonctionne !', vscode.DiagnosticSeverity.Information);
            diagnosticCollection.set(event.document.uri, [diagnostic]);
        }
    });
}
exports.activate = activate;
function deactivate() {
    console.log('Extension Meshr-Lang désactivée');
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension_working.js.map