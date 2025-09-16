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
const node_1 = require("../lib/vscode-languageclient/node");
let client;
let outputChannel;
function activate(context) {
    console.log('🎨 Extension Meshr-Lang LSP Debug activée !');
    vscode.window.showInformationMessage('🎨 Extension Meshr-Lang LSP Debug activée - avec logs de débogage');
    // Créer le canal de sortie pour les logs
    outputChannel = vscode.window.createOutputChannel('Meshr-Lang LSP Debug');
    outputChannel.appendLine('🎨 Extension Meshr-Lang LSP Debug démarrée');
    outputChannel.show();
    // Configuration du serveur LSP
    // Chemin vers le serveur LSP embarqué
    const serverPath = require('path').join(__dirname, '..', 'server', 'meshr-lsp-server');
    const serverOptions = {
        run: {
            command: serverPath,
            args: [],
            options: {}
        },
        debug: {
            command: 'python',
            args: ['-m', 'lsp.server.main'],
            options: {
                cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath ?
                    require('path').resolve(vscode.workspace.workspaceFolders[0].uri.fsPath, '../../..') :
                    process.cwd()
            }
        }
    };
    // Options du client LSP avec robustesse améliorée
    const clientOptions = {
        documentSelector: [{ scheme: 'file', language: 'meshr' }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/.clientrc')
        },
        outputChannel: outputChannel,
        traceOutputChannel: outputChannel,
        // Options de robustesse pour éviter les timeouts
        initializationOptions: {},
        initializationFailedHandler: (error) => {
            outputChannel.appendLine(`🚨 Échec d'initialisation LSP: ${error.message}`);
            return false; // Ne pas redémarrer automatiquement
        },
        errorHandler: {
            error: (error, message, count) => {
                outputChannel.appendLine(`🚨 Erreur LSP (${count}): ${error.message}`);
                outputChannel.appendLine(`🚨 Message: ${message}`);
                // Limiter les redémarrages pour éviter la surcharge mémoire
                return count < 3 ? { action: 'restart' } : { action: 'shutdown' };
            },
            closed: () => {
                outputChannel.appendLine('🚨 Connexion LSP fermée');
                return { action: 'restart' };
            }
        },
        // Limiter les redémarrages pour éviter la surcharge mémoire
        connectionOptions: {
            maxRestartCount: 2 // Réduire les redémarrages
        }
    };
    // Créer le client LSP
    client = new node_1.LanguageClient('meshr-lang', 'Meshr-Lang Language Server', serverOptions, clientOptions);
    // Démarrer le client LSP
    client.start().then(() => {
        outputChannel.appendLine('✅ Client LSP démarré avec succès');
        console.log('✅ Client LSP démarré avec succès');
    }).catch((error) => {
        outputChannel.appendLine(`❌ Erreur lors du démarrage du client LSP: ${error.message}`);
        console.error('❌ Erreur lors du démarrage du client LSP:', error);
        vscode.window.showErrorMessage(`Erreur LSP: ${error.message}`);
    });
    // Enregistrer les commandes
    const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
        outputChannel.appendLine('🧪 Commande test exécutée');
        console.log('🧪 Commande test exécutée');
        vscode.window.showInformationMessage('🧪 Commande Meshr-Lang: Test exécutée !');
        // Tester la connexion LSP
        if (client) {
            outputChannel.appendLine('✅ Client LSP disponible');
            client.sendRequest('initialize', {
                processId: process.pid,
                rootUri: vscode.workspace.workspaceFolders?.[0]?.uri.toString(),
                capabilities: {}
            }).then((result) => {
                outputChannel.appendLine(`✅ Initialisation LSP réussie: ${JSON.stringify(result)}`);
            }).catch((error) => {
                outputChannel.appendLine(`❌ Erreur initialisation LSP: ${error.message}`);
            });
        }
        else {
            outputChannel.appendLine('❌ Client LSP non disponible');
        }
    });
    const restartServerCommand = vscode.commands.registerCommand('meshr-lang.restartServer', async () => {
        outputChannel.appendLine('🔄 Redémarrage du serveur LSP...');
        console.log('🔄 Redémarrage du serveur LSP...');
        try {
            if (client) {
                await client.stop();
                outputChannel.appendLine('✅ Serveur LSP arrêté');
            }
            // Redémarrer le client
            client = new node_1.LanguageClient('meshr-lang', 'Meshr-Lang Language Server', serverOptions, clientOptions);
            await client.start();
            outputChannel.appendLine('✅ Serveur LSP redémarré avec succès');
            vscode.window.showInformationMessage('🔄 Serveur LSP redémarré avec succès !');
        }
        catch (error) {
            outputChannel.appendLine(`❌ Erreur lors du redémarrage: ${error.message}`);
            console.error('❌ Erreur lors du redémarrage:', error);
            vscode.window.showErrorMessage(`Erreur redémarrage: ${error.message}`);
        }
    });
    const showOutputCommand = vscode.commands.registerCommand('meshr-lang.showOutput', () => {
        outputChannel.show();
        outputChannel.appendLine('📋 Affichage de la sortie demandé');
        console.log('📋 Affichage de la sortie demandé');
        vscode.window.showInformationMessage('📋 Sortie du serveur LSP affichée !');
    });
    const startServerCommand = vscode.commands.registerCommand('meshr-lang.startServer', async () => {
        outputChannel.appendLine('🚀 Démarrage du serveur LSP...');
        console.log('🚀 Démarrage du serveur LSP...');
        try {
            if (!client) {
                client = new node_1.LanguageClient('meshr-lang', 'Meshr-Lang Language Server', serverOptions, clientOptions);
            }
            await client.start();
            outputChannel.appendLine('✅ Serveur LSP démarré avec succès');
            vscode.window.showInformationMessage('🚀 Serveur LSP démarré avec succès !');
        }
        catch (error) {
            outputChannel.appendLine(`❌ Erreur lors du démarrage: ${error.message}`);
            console.error('❌ Erreur lors du démarrage:', error);
            vscode.window.showErrorMessage(`Erreur démarrage: ${error.message}`);
        }
    });
    const stopServerCommand = vscode.commands.registerCommand('meshr-lang.stopServer', async () => {
        outputChannel.appendLine('🛑 Arrêt du serveur LSP...');
        console.log('🛑 Arrêt du serveur LSP...');
        try {
            if (client) {
                await client.stop();
                client = undefined;
                outputChannel.appendLine('✅ Serveur LSP arrêté avec succès');
                vscode.window.showInformationMessage('🛑 Serveur LSP arrêté avec succès !');
            }
            else {
                outputChannel.appendLine('⚠️ Serveur LSP déjà arrêté');
                vscode.window.showWarningMessage('⚠️ Serveur LSP déjà arrêté');
            }
        }
        catch (error) {
            outputChannel.appendLine(`❌ Erreur lors de l\'arrêt: ${error.message}`);
            console.error('❌ Erreur lors de l\'arrêt:', error);
            vscode.window.showErrorMessage(`Erreur arrêt: ${error.message}`);
        }
    });
    // Commande pour revalider les diagnostics
    const revalidateCommand = vscode.commands.registerCommand('meshr-lang.revalidate', async () => {
        try {
            outputChannel.appendLine('🔄 Revalidation des diagnostics demandée...');
            if (client) {
                // Envoyer la commande de revalidation au serveur LSP
                const result = await client.sendRequest('meshr-lang.revalidate', {});
                outputChannel.appendLine(`✅ Revalidation terminée: ${JSON.stringify(result)}`);
                vscode.window.showInformationMessage('🔄 Diagnostics revalidés avec succès !');
            }
            else {
                outputChannel.appendLine('⚠️ Serveur LSP non connecté');
                vscode.window.showWarningMessage('⚠️ Serveur LSP non connecté. Veuillez d\'abord démarrer le serveur.');
            }
        }
        catch (error) {
            outputChannel.appendLine(`❌ Erreur lors de la revalidation: ${error.message}`);
            console.error('❌ Erreur lors de la revalidation:', error);
            vscode.window.showErrorMessage(`Erreur revalidation: ${error.message}`);
        }
    });
    // Ajouter les commandes au contexte
    context.subscriptions.push(testCommand, restartServerCommand, showOutputCommand, startServerCommand, stopServerCommand, revalidateCommand, outputChannel);
}
exports.activate = activate;
async function deactivate() {
    console.log('🎨 Extension Meshr-Lang LSP Debug désactivée !');
    if (client) {
        try {
            await client.stop();
            outputChannel.appendLine('✅ Client LSP arrêté lors de la désactivation');
        }
        catch (error) {
            outputChannel.appendLine(`❌ Erreur lors de l'arrêt du client: ${error.message}`);
            console.error('❌ Erreur lors de l\'arrêt du client:', error);
        }
    }
    if (outputChannel) {
        outputChannel.appendLine('🎨 Extension Meshr-Lang LSP Debug désactivée');
        outputChannel.dispose();
    }
}
exports.deactivate = deactivate;
//# sourceMappingURL=extension_lsp_debug.js.map