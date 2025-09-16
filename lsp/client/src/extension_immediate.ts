import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('Extension Meshr-Lang activée !');
    
    // Afficher un message de confirmation immédiatement
    vscode.window.showInformationMessage('🎉 Extension Meshr-Lang activée !');
    
    // Enregistrer une commande de test
    const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
        vscode.window.showInformationMessage('✅ Commande Meshr-Lang testée avec succès !');
    });
    
    context.subscriptions.push(testCommand);
    
    // Créer un diagnostic simple pour tous les fichiers .meshr
    const diagnosticCollection = vscode.languages.createDiagnosticCollection('meshr');
    context.subscriptions.push(diagnosticCollection);
    
    // Fonction pour analyser un document
    const analyzeDocument = (document: vscode.TextDocument) => {
        if (document.languageId === 'meshr') {
            const diagnostics: vscode.Diagnostic[] = [];
            
            // Créer un diagnostic simple
            const diagnostic = new vscode.Diagnostic(
                new vscode.Range(0, 0, 0, 1),
                'Extension Meshr-Lang fonctionne ! Diagnostic de test.',
                vscode.DiagnosticSeverity.Information
            );
            
            diagnostics.push(diagnostic);
            
            // Ajouter des diagnostics pour les erreurs évidentes
            const text = document.getText();
            const lines = text.split('\n');
            
            for (let i = 0; i < lines.length; i++) {
                const line = lines[i];
                if (line.includes('!%£$%')) {
                    const diagnostic = new vscode.Diagnostic(
                        new vscode.Range(i, 0, i, line.length),
                        'Caractères invalides détectés !',
                        vscode.DiagnosticSeverity.Error
                    );
                    diagnostics.push(diagnostic);
                }
            }
            
            diagnosticCollection.set(document.uri, diagnostics);
        }
    };
    
    // Analyser les documents ouverts
    vscode.workspace.textDocuments.forEach(analyzeDocument);
    
    // Écouter l'ouverture de nouveaux documents
    vscode.workspace.onDidOpenTextDocument(analyzeDocument);
    
    // Écouter les changements de documents
    vscode.workspace.onDidChangeTextDocument(event => {
        analyzeDocument(event.document);
    });
}

export function deactivate() {
    console.log('Extension Meshr-Lang désactivée');
}

