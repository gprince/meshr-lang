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
    console.log('Extension Meshr-Lang HYBRIDE activée !');
    // Diagnostic simple pour confirmer l'activation
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr-lang');
    const diagnostic = new vscode.Diagnostic(new vscode.Range(0, 0, 0, 1), 'Extension HYBRIDE fonctionne!', vscode.DiagnosticSeverity.Information);
    diagnosticCollection.set(vscode.Uri.file('/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/stdlib/core/index.meshr'), [diagnostic]);
    // Commande de test
    const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
        vscode.window.showInformationMessage('Commande testée !', 'Source : Meshr-Lang');
    });
    // Commande pour redémarrer le serveur LSP
    const restartServerCommand = vscode.commands.registerCommand('meshr-lang.restartServer', () => {
        if (client) {
            client.stop().then(() => {
                startLanguageServer(context);
                vscode.window.showInformationMessage('Serveur LSP redémarré !');
            });
        }
        else {
            startLanguageServer(context);
            vscode.window.showInformationMessage('Serveur LSP démarré !');
        }
    });
    // Commande pour afficher la sortie du serveur
    const showOutputCommand = vscode.commands.registerCommand('meshr-lang.showOutput', () => {
        if (client) {
            client.outputChannel.show();
        }
        else {
            vscode.window.showWarningMessage('Serveur LSP non démarré');
        }
    });
    context.subscriptions.push(testCommand, restartServerCommand, showOutputCommand);
    // Démarrer le serveur LSP
    startLanguageServer(context);
}
exports.activate = activate;
function startLanguageServer(context) {
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
        diagnosticCollectionName: 'meshr-lang',
        outputChannel: vscode.window.createOutputChannel('Meshr-Lang LSP')
    };
    // Créer le client LSP
    client = new node_1.LanguageClient('meshr-lang', 'Meshr-Lang Language Server', serverOptions, clientOptions);
    // Démarrer le client
    client.start().then(() => {
        console.log('Client LSP démarré avec succès');
        vscode.window.showInformationMessage('Serveur LSP Meshr-Lang connecté !');
    }).catch((error) => {
        console.error('Erreur lors du démarrage du client LSP:', error);
        vscode.window.showErrorMessage(`Erreur LSP: ${error.message}`);
    });
}
function deactivate() {
    if (client) {
        return client.stop();
    }
    return undefined;
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension_hybrid.js.map