import * as vscode from 'vscode';
import {
    LanguageClient,
    LanguageClientOptions,
    ServerOptions,
    TransportKind
} from 'vscode-languageclient/node';

let client: LanguageClient | null = null;

export function activate(context: vscode.ExtensionContext) {
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
            } else {
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
            } else {
                vscode.window.showInformationMessage('🔄 Serveur LSP déjà arrêté');
            }
        });
        context.subscriptions.push(restartCommand);
        
        console.log('Commandes enregistrées avec succès');
        
        // Essayer de démarrer le serveur LSP avec logs détaillés
        vscode.window.showInformationMessage('🚀 Tentative de démarrage du serveur LSP...');
        
        const serverOptions: ServerOptions = {
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
                transport: TransportKind.stdio
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
                transport: TransportKind.stdio
            }
        };

        const clientOptions: LanguageClientOptions = {
            documentSelector: [{ scheme: 'file', language: 'meshr' }],
            synchronize: {
                fileEvents: vscode.workspace.createFileSystemWatcher('**/*.meshr')
            }
        };

        client = new LanguageClient(
            'meshr-lang-server',
            'Meshr-Lang Language Server',
            serverOptions,
            clientOptions
        );

        // Logs détaillés
        client.start().then(() => {
            console.log('✅ Client LSP démarré');
            vscode.window.showInformationMessage('✅ Client LSP démarré !');
            
            // Attendre que le client soit prêt
            setTimeout(() => {
                if (client && client.isRunning()) {
                    console.log('✅ Client LSP prêt');
                    vscode.window.showInformationMessage('✅ Serveur LSP Meshr-Lang démarré avec succès !');
                } else {
                    console.log('❌ Client LSP non prêt');
                    vscode.window.showErrorMessage('❌ Client LSP non prêt');
                }
            }, 2000);
            
        }).catch((error: any) => {
            console.error('❌ Erreur démarrage client LSP:', error);
            vscode.window.showErrorMessage(`❌ Erreur démarrage: ${error.message}`);
        });

        console.log('Serveur LSP configuré');
        
    } catch (error) {
        console.error('Erreur lors de l\'activation de l\'extension:', error);
        vscode.window.showErrorMessage(`Erreur d'activation: ${error}`);
    }
}

export function deactivate() {
    console.log('Extension Meshr-Lang désactivée');
    if (client) {
        client.stop();
    }
}
