import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('🚀 Extension Meshr-Lang TEST activée !');
    
    // Message immédiat
    vscode.window.showInformationMessage('✅ Extension Meshr-Lang TEST activée !');
    
    // Commande de test
    const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
        vscode.window.showInformationMessage('🎯 Commande testée avec succès !');
    });

    context.subscriptions.push(testCommand);

    // Diagnostic simple
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr-lang-test');
    context.subscriptions.push(diagnosticCollection);

    const provideDiagnostics = (document: vscode.TextDocument) => {
        if (document.languageId === 'meshr') {
            const diagnostics: vscode.Diagnostic[] = [];
            const line = document.lineAt(0);
            const diagnostic = new vscode.Diagnostic(
                new vscode.Range(0, 0, 0, line.text.length),
                '✅ Extension TEST fonctionne !',
                vscode.DiagnosticSeverity.Information
            );
            diagnostics.push(diagnostic);
            diagnosticCollection.set(document.uri, diagnostics);
        }
    };

    vscode.workspace.onDidOpenTextDocument(provideDiagnostics);
    vscode.workspace.onDidChangeTextDocument(event => provideDiagnostics(event.document));
    vscode.workspace.textDocuments.forEach(provideDiagnostics);

    console.log('✅ Extension TEST complètement initialisée');
}

export function deactivate() {
    console.log('🛑 Extension Meshr-Lang TEST désactivée');
}

