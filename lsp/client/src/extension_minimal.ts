import * as vscode from 'vscode';
import {
    LanguageClient,
    LanguageClientOptions,
    ServerOptions,
    TransportKind
} from 'vscode-languageclient/node';

let client: LanguageClient;

export function activate(context: vscode.ExtensionContext) {
    console.log('Extension Meshr-Lang activée');

    // Configuration minimale du serveur LSP
    const serverOptions: ServerOptions = {
        run: {
            command: 'python',
            args: ['-m', 'lsp.server.main'],
            transport: TransportKind.stdio
        },
        debug: {
            command: 'python',
            args: ['-m', 'lsp.server.main'],
            transport: TransportKind.stdio
        }
    };

    // Configuration du client LSP
    const clientOptions: LanguageClientOptions = {
        documentSelector: [{ scheme: 'file', language: 'meshr' }]
    };

    // Créer le client LSP
    client = new LanguageClient(
        'meshr-lang-server',
        'Meshr-Lang Language Server',
        serverOptions,
        clientOptions
    );

    // Démarrer le client
    client.start();

    // Enregistrer les commandes
    context.subscriptions.push(
        vscode.commands.registerCommand('meshr-lang.restartServer', async () => {
            if (client) {
                await client.stop();
                client.start();
                vscode.window.showInformationMessage('Serveur LSP Meshr-Lang redémarré');
            }
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('meshr-lang.showOutput', () => {
            client.outputChannel.show();
        })
    );

    // Nettoyer à la désactivation
    context.subscriptions.push({
        dispose: () => {
            if (client) {
                client.stop();
            }
        }
    });
}

export function deactivate(): Thenable<void> | undefined {
    if (!client) {
        return undefined;
    }
    return client.stop();
}
