import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('Extension Meshr-Lang activée !');
    
    // Afficher un message de confirmation
    vscode.window.showInformationMessage('Extension Meshr-Lang activée !');
    
    // Enregistrer une commande simple pour tester
    const disposable = vscode.commands.registerCommand('meshr-lang.test', () => {
        vscode.window.showInformationMessage('Commande Meshr-Lang testée !');
    });
    
    context.subscriptions.push(disposable);
    
    // Créer un diagnostic simple pour tester
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr');
    context.subscriptions.push(diagnosticCollection);
    
    // Écouter les changements de documents
    vscode.workspace.onDidChangeTextDocument(event => {
        if (event.document.languageId === 'meshr') {
            // Créer un diagnostic simple
            const diagnostic = new vscode.Diagnostic(
                new vscode.Range(0, 0, 0, 1),
                'Test diagnostic - Extension Meshr-Lang fonctionne !',
                vscode.DiagnosticSeverity.Information
            );
            
            diagnosticCollection.set(event.document.uri, [diagnostic]);
        }
    });
}

export function deactivate() {
    console.log('Extension Meshr-Lang désactivée');
}
