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

    // Configuration du serveur LSP
    const serverOptions: ServerOptions = {
        run: {
            command: getServerCommand(),
            args: getServerArgs(),
            options: {
                cwd: getServerCwd()
            },
            transport: TransportKind.stdio
        },
        debug: {
            command: getServerCommand(),
            args: getServerArgs(),
            options: {
                cwd: getServerCwd()
            },
            transport: TransportKind.stdio
        }
    };

    // Configuration du client LSP
    const clientOptions: LanguageClientOptions = {
        documentSelector: [{ scheme: 'file', language: 'meshr' }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/.meshr')
        }
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
        vscode.commands.registerCommand('meshr-lang.restartServer', () => {
            restartServer();
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

function getServerCommand(): string {
    const config = vscode.workspace.getConfiguration('meshr-lang.server');
    return config.get<string>('path', 'python');
}

function getServerArgs(): string[] {
    const config = vscode.workspace.getConfiguration('meshr-lang.server');
    return config.get<string[]>('args', ['-m', 'lsp.server.main']);
}

function getServerCwd(): string {
    const config = vscode.workspace.getConfiguration('meshr-lang.server');
    const cwd = config.get<string>('cwd', '${workspaceFolder}');
    
    // Remplacer les variables d'environnement
    if (cwd.includes('${workspaceFolder}')) {
        const workspaceFolder = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
        if (workspaceFolder) {
            return cwd.replace('${workspaceFolder}', workspaceFolder);
        }
    }
    
    return cwd;
}

async function restartServer(): Promise<void> {
    if (client) {
        await client.stop();
        client.start();
        vscode.window.showInformationMessage('Serveur LSP Meshr-Lang redémarré');
    }
}
