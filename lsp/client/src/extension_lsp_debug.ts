import * as vscode from 'vscode';
import * as path from 'path';
import { LanguageClient, LanguageClientOptions, ServerOptions, TransportKind } from '../lib/vscode-languageclient/node';

let client: LanguageClient | undefined;
let outputChannel: vscode.OutputChannel;

export function activate(context: vscode.ExtensionContext) {
    console.log('🎨 Extension Meshr-Lang LSP Debug activée !');
    vscode.window.showInformationMessage('🎨 Extension Meshr-Lang LSP Debug activée - avec logs de débogage');

    // Créer le canal de sortie pour les logs
    outputChannel = vscode.window.createOutputChannel('Meshr-Lang LSP Debug');
    outputChannel.appendLine('🎨 Extension Meshr-Lang LSP Debug démarrée');
    outputChannel.show();

    // Configuration du serveur LSP
    const serverOptions: ServerOptions = {
        run: {
            command: 'python',
            args: ['-m', 'lsp.server.main'],
            options: {
                cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd()
            }
        },
        debug: {
            command: 'python',
            args: ['-m', 'lsp.server.main'],
            options: {
                cwd: vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || process.cwd()
            }
        }
    };

    // Options du client LSP
    const clientOptions: LanguageClientOptions = {
        documentSelector: [{ scheme: 'file', language: 'meshr' }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/.clientrc')
        },
        outputChannel: outputChannel,
        traceOutputChannel: outputChannel
    };

    // Créer le client LSP
    client = new LanguageClient(
        'meshr-lang',
        'Meshr-Lang Language Server',
        serverOptions,
        clientOptions
    );

    // Démarrer le client LSP
    client.start().then(() => {
        outputChannel.appendLine('✅ Client LSP démarré avec succès');
        console.log('✅ Client LSP démarré avec succès');
    }).catch((error: any) => {
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
            }).catch((error: any) => {
                outputChannel.appendLine(`❌ Erreur initialisation LSP: ${error.message}`);
            });
        } else {
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
            client = new LanguageClient(
                'meshr-lang',
                'Meshr-Lang Language Server',
                serverOptions,
                clientOptions
            );
            
            await client.start();
            outputChannel.appendLine('✅ Serveur LSP redémarré avec succès');
            vscode.window.showInformationMessage('🔄 Serveur LSP redémarré avec succès !');
        } catch (error: any) {
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
                client = new LanguageClient(
                    'meshr-lang',
                    'Meshr-Lang Language Server',
                    serverOptions,
                    clientOptions
                );
            }
            
            await client.start();
            outputChannel.appendLine('✅ Serveur LSP démarré avec succès');
            vscode.window.showInformationMessage('🚀 Serveur LSP démarré avec succès !');
        } catch (error: any) {
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
            } else {
                outputChannel.appendLine('⚠️ Serveur LSP déjà arrêté');
                vscode.window.showWarningMessage('⚠️ Serveur LSP déjà arrêté');
            }
        } catch (error: any) {
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
            } else {
                outputChannel.appendLine('⚠️ Serveur LSP non connecté');
                vscode.window.showWarningMessage('⚠️ Serveur LSP non connecté. Veuillez d\'abord démarrer le serveur.');
            }
        } catch (error: any) {
            outputChannel.appendLine(`❌ Erreur lors de la revalidation: ${error.message}`);
            console.error('❌ Erreur lors de la revalidation:', error);
            vscode.window.showErrorMessage(`Erreur revalidation: ${error.message}`);
        }
    });

    // Ajouter les commandes au contexte
    context.subscriptions.push(
        testCommand,
        restartServerCommand,
        showOutputCommand,
        startServerCommand,
        stopServerCommand,
        revalidateCommand,
        outputChannel
    );
}

export async function deactivate() {
    console.log('🎨 Extension Meshr-Lang LSP Debug désactivée !');
    
    if (client) {
        try {
            await client.stop();
            outputChannel.appendLine('✅ Client LSP arrêté lors de la désactivation');
        } catch (error: any) {
            outputChannel.appendLine(`❌ Erreur lors de l'arrêt du client: ${error.message}`);
            console.error('❌ Erreur lors de l\'arrêt du client:', error);
        }
    }
    
    if (outputChannel) {
        outputChannel.appendLine('🎨 Extension Meshr-Lang LSP Debug désactivée');
        outputChannel.dispose();
    }
}