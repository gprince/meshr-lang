import * as vscode from 'vscode';
import { LanguageClient, LanguageClientOptions, ServerOptions, TransportKind } from 'vscode-languageclient/node';

let client: LanguageClient;

export function activate(context: vscode.ExtensionContext) {
    console.log('Extension Meshr-Lang HYBRIDE activée !');
    
    // Diagnostic simple pour confirmer l'activation
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr-lang');
    const diagnostic = new vscode.Diagnostic(
        new vscode.Range(0, 0, 0, 1),
        'Extension HYBRIDE fonctionne!',
        vscode.DiagnosticSeverity.Information
    );
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
        } else {
            startLanguageServer(context);
            vscode.window.showInformationMessage('Serveur LSP démarré !');
        }
    });

    // Commande pour afficher la sortie du serveur
    const showOutputCommand = vscode.commands.registerCommand('meshr-lang.showOutput', () => {
        if (client) {
            client.outputChannel.show();
        } else {
            vscode.window.showWarningMessage('Serveur LSP non démarré');
        }
    });

    context.subscriptions.push(testCommand, restartServerCommand, showOutputCommand);

    // Démarrer le serveur LSP
    startLanguageServer(context);
}

function startLanguageServer(context: vscode.ExtensionContext) {
    // Configuration du serveur
    const serverExecutable = {
        command: 'python',
        args: ['-m', 'lsp.server.main'],
        options: {
            cwd: '/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang'
        }
    };

    const serverOptions: ServerOptions = {
        run: serverExecutable,
        debug: serverExecutable
    };

    // Configuration du client
    const clientOptions: LanguageClientOptions = {
        documentSelector: [{ scheme: 'file', language: 'meshr' }],
        diagnosticCollectionName: 'meshr-lang',
        outputChannel: vscode.window.createOutputChannel('Meshr-Lang LSP')
    };

    // Créer le client LSP
    client = new LanguageClient(
        'meshr-lang',
        'Meshr-Lang Language Server',
        serverOptions,
        clientOptions
    );

    // Démarrer le client
    client.start().then(() => {
        console.log('Client LSP démarré avec succès');
        vscode.window.showInformationMessage('Serveur LSP Meshr-Lang connecté !');
    }).catch((error: any) => {
        console.error('Erreur lors du démarrage du client LSP:', error);
        vscode.window.showErrorMessage(`Erreur LSP: ${error.message}`);
    });
}

export function deactivate(): Thenable<void> | undefined {
    if (client) {
        return client.stop();
    }
    return undefined;
}