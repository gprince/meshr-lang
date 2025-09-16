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
let client = null;
function activate(context) {
    console.log('Extension Meshr-Lang DEBUG activée !');
    try {
        // Afficher un message de confirmation
        vscode.window.showInformationMessage('🔍 Extension Meshr-Lang DEBUG activée !');
        // Enregistrer les commandes
        const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
            vscode.window.showInformationMessage('✅ Commande Meshr-Lang testée avec succès !');
        });
        context.subscriptions.push(testCommand);
        const showOutputCommand = vscode.commands.registerCommand('meshr-lang.showOutput', () => {
            if (client) {
                client.outputChannel.show();
            }
            else {
                vscode.window.showInformationMessage('📋 Serveur LSP non disponible');
            }
        });
        context.subscriptions.push(showOutputCommand);
        const restartCommand = vscode.commands.registerCommand('meshr-lang.restartServer', () => {
            if (client) {
                client.stop().then(() => {
                    client = null;
                    vscode.window.showInformationMessage('🔄 Serveur LSP arrêté');
                });
            }
            else {
                vscode.window.showInformationMessage('🔄 Serveur LSP déjà arrêté');
            }
        });
        context.subscriptions.push(restartCommand);
        console.log('Commandes enregistrées avec succès');
        // Essayer de démarrer le serveur LSP avec logs détaillés
        vscode.window.showInformationMessage('🚀 Tentative de démarrage du serveur LSP...');
        const serverOptions = {
            run: {
                command: 'python',
                args: ['-m', 'lsp.server.main'],
                options: {
                    cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd(),
                    env: {
                        ...process.env,
                        PYTHONPATH: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd()
                    }
                },
                transport: node_1.TransportKind.stdio
            },
            debug: {
                command: 'python',
                args: ['-m', 'lsp.server.main'],
                options: {
                    cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd(),
                    env: {
                        ...process.env,
                        PYTHONPATH: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd()
                    }
                },
                transport: node_1.TransportKind.stdio
            }
        };
        const clientOptions = {
            documentSelector: [{ scheme: 'file', language: 'meshr' }],
            synchronize: {
                fileEvents: vscode.workspace.createFileSystemWatcher('**/*.meshr')
            }
        };
        client = new node_1.LanguageClient('meshr-lang-server', 'Meshr-Lang Language Server', serverOptions, clientOptions);
        // Logs détaillés
        client.start().then(() => {
            console.log('✅ Client LSP démarré');
            vscode.window.showInformationMessage('✅ Client LSP démarré !');
            // Attendre que le client soit prêt
            setTimeout(() => {
                if (client && client.isRunning()) {
                    console.log('✅ Client LSP prêt');
                    vscode.window.showInformationMessage('✅ Serveur LSP Meshr-Lang démarré avec succès !');
                }
                else {
                    console.log('❌ Client LSP non prêt');
                    vscode.window.showErrorMessage('❌ Client LSP non prêt');
                }
            }, 2000);
        }).catch((error) => {
            console.error('❌ Erreur démarrage client LSP:', error);
            vscode.window.showErrorMessage(`❌ Erreur démarrage: ${error.message}`);
        });
        console.log('Serveur LSP configuré');
    }
    catch (error) {
        console.error('Erreur lors de l\'activation de l\'extension:', error);
        vscode.window.showErrorMessage(`Erreur d'activation: ${error}`);
    }
}
exports.activate = activate;
function deactivate() {
    console.log('Extension Meshr-Lang désactivée');
    if (client) {
        client.stop();
    }
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension_debug.js.map