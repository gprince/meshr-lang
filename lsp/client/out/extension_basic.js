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
    try {
        // Afficher un message de confirmation
        vscode.window.showInformationMessage('🎉 Extension Meshr-Lang activée !');
        // Enregistrer une commande de test
        const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
            vscode.window.showInformationMessage('✅ Commande Meshr-Lang testée avec succès !');
        });
        context.subscriptions.push(testCommand);
        // Enregistrer une commande pour afficher la sortie
        const showOutputCommand = vscode.commands.registerCommand('meshr-lang.showOutput', () => {
            vscode.window.showInformationMessage('📋 Sortie du serveur (mode basique)');
        });
        context.subscriptions.push(showOutputCommand);
        // Enregistrer une commande pour redémarrer le serveur
        const restartCommand = vscode.commands.registerCommand('meshr-lang.restartServer', () => {
            vscode.window.showInformationMessage('🔄 Serveur redémarré (mode basique)');
        });
        context.subscriptions.push(restartCommand);
        console.log('Commandes enregistrées avec succès');
    }
    catch (error) {
        console.error('Erreur lors de l\'activation de l\'extension:', error);
        vscode.window.showErrorMessage(`Erreur d'activation: ${error}`);
    }
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
                // Détecter les erreurs de syntaxe
                if (line.includes('!%£$%')) {
                    const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Caractères invalides détectés !', vscode.DiagnosticSeverity.Error);
                    diagnostics.push(diagnostic);
                }
                if (line.includes('%*"$"*%')) {
                    const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Caractères invalides détectés !', vscode.DiagnosticSeverity.Error);
                    diagnostics.push(diagnostic);
                }
                // Détecter les déclarations const invalides
                if (line.includes('const = %*"$"*% }')) {
                    const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Erreur de syntaxe: déclaration const invalide', vscode.DiagnosticSeverity.Error);
                    diagnostics.push(diagnostic);
                }
                if (line.includes('exported {')) {
                    const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Erreur: "exported" au lieu de "export"', vscode.DiagnosticSeverity.Error);
                    diagnostics.push(diagnostic);
                }
                if (line.includes('$lô^$o')) {
                    const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Caractères invalides détectés !', vscode.DiagnosticSeverity.Error);
                    diagnostics.push(diagnostic);
                }
                if (line.includes('Deprecated,dd')) {
                    const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Erreur de syntaxe: "Deprecated,dd" invalide', vscode.DiagnosticSeverity.Error);
                    diagnostics.push(diagnostic);
                }
                // Détecter les imports avant les modules
                if (line.trim().startsWith('import') && i < 10) {
                    // Vérifier s'il y a un module après
                    const hasModuleAfter = text.split('\n').slice(i + 1, i + 5).some(l => l.trim().startsWith('module'));
                    if (hasModuleAfter) {
                        const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Erreur: import doit être placé après la déclaration de module', vscode.DiagnosticSeverity.Error);
                        diagnostics.push(diagnostic);
                    }
                }
                // Détecter les déclarations de module multiples
                if (line.trim().startsWith('module')) {
                    const moduleCount = text.split('\n').filter(l => l.trim().startsWith('module')).length;
                    if (moduleCount > 1) {
                        const diagnostic = new vscode.Diagnostic(new vscode.Range(i, 0, i, line.length), 'Erreur: déclaration de module multiple détectée', vscode.DiagnosticSeverity.Error);
                        diagnostics.push(diagnostic);
                    }
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
//# sourceMappingURL=extension_basic.js.map