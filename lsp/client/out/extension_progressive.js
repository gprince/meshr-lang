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
const node_1 = require("vscode-languageclient/node");
let client;
function activate(context) {
    console.log('Extension Meshr-Lang PROGRESSIVE activée !');
    try {
        // Diagnostic simple pour confirmer l'activation
        const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr-lang');
        context.subscriptions.push(diagnosticCollection);
        // Commande de test
        const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
            vscode.window.showInformationMessage('Commande testée !', 'Source : Meshr-Lang');
        });
        // Commande pour démarrer le serveur LSP
        const startServerCommand = vscode.commands.registerCommand('meshr-lang.startServer', () => {
            if (client) {
                vscode.window.showInformationMessage('Serveur LSP déjà démarré !');
                return;
            }
            startLanguageServer(context);
        });
        // Commande pour arrêter le serveur LSP
        const stopServerCommand = vscode.commands.registerCommand('meshr-lang.stopServer', () => {
            if (client) {
                client.stop().then(() => {
                    client = undefined;
                    vscode.window.showInformationMessage('Serveur LSP arrêté !');
                });
            }
            else {
                vscode.window.showInformationMessage('Serveur LSP non démarré !');
            }
        });
        // Commande pour redémarrer le serveur LSP
        const restartServerCommand = vscode.commands.registerCommand('meshr-lang.restartServer', () => {
            if (client) {
                client.stop().then(() => {
                    client = undefined;
                    startLanguageServer(context);
                });
            }
            else {
                startLanguageServer(context);
            }
        });
        // Commande pour afficher la sortie du serveur
        const showOutputCommand = vscode.commands.registerCommand('meshr-lang.showOutput', () => {
            if (client) {
                client.outputChannel.show();
            }
            else {
                vscode.window.showWarningMessage('Serveur LSP non démarré. Utilisez "Meshr-Lang: Démarrer le serveur LSP"');
            }
        });
        context.subscriptions.push(testCommand, startServerCommand, stopServerCommand, restartServerCommand, showOutputCommand);
        // Diagnostic de base
        const provideDiagnostics = (document) => {
            if (document.languageId === 'meshr') {
                const diagnostics = [];
                const line = document.lineAt(0);
                const diagnostic = new vscode.Diagnostic(new vscode.Range(0, 0, 0, line.text.length), 'Extension PROGRESSIVE fonctionne !', vscode.DiagnosticSeverity.Information);
                diagnostics.push(diagnostic);
                diagnosticCollection.set(document.uri, diagnostics);
            }
        };
        vscode.workspace.onDidOpenTextDocument(provideDiagnostics);
        vscode.workspace.onDidChangeTextDocument(event => provideDiagnostics(event.document));
        vscode.workspace.textDocuments.forEach(provideDiagnostics);
        console.log('Commandes et diagnostics basiques enregistrés avec succès');
        // Démarrer automatiquement le serveur LSP
        setTimeout(() => {
            startLanguageServer(context);
        }, 1000);
    }
    catch (error) {
        console.error('Erreur lors de l\'activation de l\'extension:', error);
        vscode.window.showErrorMessage(`❌ Erreur d'activation: ${error.message}`);
    }
}
exports.activate = activate;
function startLanguageServer(context) {
    try {
        console.log('Tentative de démarrage du serveur LSP...');
        // Configuration du serveur
        const serverExecutable = {
            command: 'python',
            args: ['-m', 'lsp.server.main'],
            options: {
                cwd: '/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang'
            }
        };
        const serverOptions = {
            run: serverExecutable,
            debug: serverExecutable
        };
        // Configuration du client
        const clientOptions = {
            documentSelector: [{ scheme: 'file', language: 'meshr' }],
            diagnosticCollectionName: 'meshr-lang-lsp',
            outputChannel: vscode.window.createOutputChannel('Meshr-Lang LSP')
        };
        // Créer le client LSP
        client = new node_1.LanguageClient('meshr-lang-lsp', 'Meshr-Lang Language Server', serverOptions, clientOptions);
        // Démarrer le client
        client.start().then(() => {
            console.log('Client LSP démarré avec succès');
            vscode.window.showInformationMessage('✅ Serveur LSP Meshr-Lang connecté !');
        }).catch((error) => {
            console.error('Erreur lors du démarrage du client LSP:', error);
            vscode.window.showErrorMessage(`❌ Erreur LSP: ${error.message}`);
            client = undefined;
        });
    }
    catch (error) {
        console.error('Erreur lors de la configuration du serveur LSP:', error);
        vscode.window.showErrorMessage(`❌ Erreur configuration LSP: ${error.message}`);
        client = undefined;
    }
}
function deactivate() {
    if (client) {
        return client.stop();
    }
    return undefined;
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension_progressive.js.map