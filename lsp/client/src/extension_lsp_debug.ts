import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';
import { LanguageClient, LanguageClientOptions, ServerOptions, ErrorAction, CloseAction, State } from '../lib/vscode-languageclient/node';

const MAX_RESTART_ATTEMPTS = 5;

let client: LanguageClient | undefined;
let outputChannel: vscode.OutputChannel | undefined;
let serverOptions: ServerOptions | undefined;
let clientOptions: LanguageClientOptions | undefined;
let clientState: State = State.Stopped;
let restartAttempts = 0;
let allowAutoRestart = true;
let hadStartFailure = false;

function resolveRepoRoot(context: vscode.ExtensionContext): string {
    const workspaceFolder = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
    if (workspaceFolder) {
        return workspaceFolder;
    }
    return path.resolve(context.extensionPath, '..', '..');
}

function resolvePythonExecutable(repoRoot: string): string {
    const isWindows = process.platform === 'win32';
    const venvCandidates = ['.venv', 'venv', '.virtualenv'];

    for (const venvName of venvCandidates) {
        const venvPath = path.join(repoRoot, venvName);
        if (!fs.existsSync(venvPath)) {
            continue;
        }

        const executables = isWindows
            ? [path.join(venvPath, 'Scripts', 'python.exe'), path.join(venvPath, 'Scripts', 'python3.exe')]
            : [path.join(venvPath, 'bin', 'python3'), path.join(venvPath, 'bin', 'python')];

        for (const candidate of executables) {
            if (fs.existsSync(candidate)) {
                return candidate;
            }
        }
    }

    return isWindows ? 'python' : 'python3';
}

function buildPythonEnv(repoRoot: string): NodeJS.ProcessEnv {
    const serverPath = path.join(repoRoot, 'lsp', 'server');
    const paths: string[] = [];

    if (process.env.PYTHONPATH) {
        paths.push(process.env.PYTHONPATH);
    }

    paths.unshift(serverPath, repoRoot);

    return {
        ...process.env,
        PYTHONPATH: paths.filter(Boolean).join(path.delimiter)
    };
}

type StopResult = 'stopped' | 'notRunning' | 'error';
type StartResult = 'started' | 'alreadyRunning' | 'alreadyStarting';

function createLanguageClient(): LanguageClient {
    if (!serverOptions || !clientOptions) {
        throw new Error('Options du client LSP non initialisées');
    }

    const languageClient = new LanguageClient(
        'meshr-lang',
        'Meshr-Lang Language Server',
        serverOptions,
        clientOptions
    );

    languageClient.onDidChangeState(({ newState }) => {
        clientState = newState;
        switch (newState) {
            case State.Running:
                restartAttempts = 0;
                hadStartFailure = false;
                outputChannel?.appendLine('✅ Client LSP en état RUNNING');
                break;
            case State.Starting:
                outputChannel?.appendLine('⏳ Client LSP en cours de démarrage');
                break;
            case State.Stopped:
                outputChannel?.appendLine('🛑 Client LSP en état STOPPED');
                break;
            default:
                outputChannel?.appendLine(`ℹ️ Changement d\'état du client LSP: ${newState}`);
                break;
        }
    });

    return languageClient;
}

async function stopClient(): Promise<StopResult> {
    if (!client) {
        outputChannel?.appendLine('⚠️ Serveur LSP non initialisé, arrêt ignoré');
        allowAutoRestart = false;
        clientState = State.Stopped;
        restartAttempts = 0;
        return 'notRunning';
    }

    if (clientState !== State.Running) {
        const stateLabel = clientState === State.Starting ? 'STARTING' : 'STOPPED';
        const failureNote = hadStartFailure ? ' (échec de démarrage détecté)' : '';
        outputChannel?.appendLine(`⚠️ Serveur LSP non actif (état: ${stateLabel})${failureNote}. Aucun arrêt nécessaire`);
        allowAutoRestart = false;
        client = undefined;
        restartAttempts = 0;
        hadStartFailure = false;
        return 'notRunning';
    }

    allowAutoRestart = false;

    try {
        await client.stop();
        outputChannel?.appendLine('✅ Serveur LSP arrêté');
        return 'stopped';
    } catch (error: any) {
        const message = error?.message ?? String(error);
        outputChannel?.appendLine(`❌ Erreur lors de l'arrêt: ${message}`);
        console.error('❌ Erreur lors de l\'arrêt:', error);
        return 'error';
    } finally {
        clientState = State.Stopped;
        restartAttempts = 0;
        client = undefined;
        hadStartFailure = false;
    }
}

async function startClient(options: { showNotification?: boolean } = {}): Promise<StartResult> {
    const { showNotification = false } = options;

    if (!serverOptions || !clientOptions) {
        throw new Error('Options du serveur LSP non initialisées');
    }

    if (!client) {
        client = createLanguageClient();
    }

    if (clientState === State.Running) {
        outputChannel?.appendLine('⚠️ Serveur LSP déjà démarré');
        if (showNotification) {
            vscode.window.showInformationMessage('⚠️ Serveur LSP déjà démarré');
        }
        return 'alreadyRunning';
    }

    if (clientState === State.Starting) {
        outputChannel?.appendLine('⏳ Serveur LSP en cours de démarrage');
        return 'alreadyStarting';
    }

    try {
        allowAutoRestart = true;
        clientState = State.Starting;
        await client.start();
        outputChannel?.appendLine('✅ Serveur LSP démarré avec succès');
        if (showNotification) {
            vscode.window.showInformationMessage('🚀 Serveur LSP démarré avec succès !');
        }
        return 'started';
    } catch (error: any) {
        const message = error?.message ?? String(error);
        outputChannel?.appendLine(`❌ Erreur lors du démarrage: ${message}`);
        console.error('❌ Erreur lors du démarrage:', error);
        if (showNotification) {
            vscode.window.showErrorMessage(`Erreur démarrage: ${message}`);
        }
        clientState = State.Stopped;
        allowAutoRestart = false;
        hadStartFailure = true;
        client = undefined;
        throw error;
    }
}

export function activate(context: vscode.ExtensionContext) {
    console.log('🎨 Extension Meshr-Lang LSP Debug activée !');
    vscode.window.showInformationMessage('🎨 Extension Meshr-Lang LSP Debug activée - avec logs de débogage');

    // Créer le canal de sortie pour les logs
    outputChannel = vscode.window.createOutputChannel('Meshr-Lang LSP Debug');
    const channel = outputChannel;
    channel.appendLine('🎨 Extension Meshr-Lang LSP Debug démarrée');
    channel.show();

    // Réinitialiser l'état client
    client = undefined;
    clientState = State.Stopped;
    restartAttempts = 0;
    allowAutoRestart = true;

    const repoRoot = resolveRepoRoot(context);
    const pythonCommand = resolvePythonExecutable(repoRoot);
    const pythonArgs = ['-m', 'lsp.server.standalone_language_server'];
    const pythonOptions = {
        cwd: repoRoot,
        env: buildPythonEnv(repoRoot)
    };

    channel.appendLine(`📁 Répertoire workspace: ${repoRoot}`);
    channel.appendLine(`🐍 Utilisation de l'interpréteur Python: ${pythonCommand}`);

    const bundledServerPath = path.join(__dirname, '..', 'server', 'meshr-lsp-server');
    const hasBundledServer = fs.existsSync(bundledServerPath);

    if (hasBundledServer) {
        channel.appendLine(`📦 Serveur LSP embarqué détecté: ${bundledServerPath}`);
    } else {
        channel.appendLine('⚠️ Serveur LSP embarqué absent — utilisation du serveur Python via venv');
    }

    // Configuration du serveur LSP
    serverOptions = {
        run: {
            command: hasBundledServer ? bundledServerPath : pythonCommand,
            args: hasBundledServer ? [] : pythonArgs,
            options: hasBundledServer ? {} : pythonOptions
        },
        debug: {
            command: pythonCommand,
            args: pythonArgs,
            options: pythonOptions
        }
    };

    // Options du client LSP avec robustesse améliorée
    clientOptions = {
        documentSelector: [{ scheme: 'file', language: 'meshr' }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/.clientrc')
        },
        outputChannel: channel,
        traceOutputChannel: channel,
        // Options de robustesse pour éviter les timeouts
        initializationOptions: {},
        initializationFailedHandler: (error) => {
            channel.appendLine(`🚨 Échec d'initialisation LSP: ${error.message}`);
            return false; // Ne pas redémarrer automatiquement
        },
        errorHandler: {
            error: (error, message, count) => {
                restartAttempts = Math.max(restartAttempts, count);
                channel.appendLine(`🚨 Erreur LSP (${count}): ${error.message}`);
                channel.appendLine(`🚨 Message: ${message}`);
                if (count >= MAX_RESTART_ATTEMPTS) {
                    channel.appendLine('🛑 Limite de tentatives atteinte après erreurs consécutives. Arrêt du client.');
                    return { action: ErrorAction.Shutdown };
                }
                return { action: ErrorAction.Continue };
            },
            closed: () => {
                clientState = State.Stopped;
                if (!allowAutoRestart) {
                    channel.appendLine('ℹ️ Connexion LSP fermée suite à un arrêt manuel. Aucun redémarrage automatique.');
                    return { action: CloseAction.DoNotRestart };
                }

                if (restartAttempts >= MAX_RESTART_ATTEMPTS) {
                    channel.appendLine('🛑 Limite de redémarrages atteinte. Aucun redémarrage supplémentaire.');
                    return { action: CloseAction.DoNotRestart };
                }

                restartAttempts += 1;
                channel.appendLine(`♻️ Connexion LSP fermée. Redémarrage automatique ${restartAttempts}/${MAX_RESTART_ATTEMPTS}`);
                return { action: CloseAction.Restart };
            }
        },
        // Limiter les redémarrages pour éviter la surcharge mémoire
        connectionOptions: {
            maxRestartCount: MAX_RESTART_ATTEMPTS
        }
    };

    // Démarrer le client LSP
    startClient({ showNotification: false }).then(() => {
        channel.appendLine('✅ Client LSP démarré avec succès');
        console.log('✅ Client LSP démarré avec succès');
    }).catch((error: any) => {
        const message = error?.message ?? String(error);
        channel.appendLine(`❌ Erreur lors du démarrage du client LSP: ${message}`);
        console.error('❌ Erreur lors du démarrage du client LSP:', error);
        vscode.window.showErrorMessage(`Erreur LSP: ${message}`);
    });

    // Enregistrer les commandes
    const testCommand = vscode.commands.registerCommand('meshr-lang.test', () => {
        channel.appendLine('🧪 Commande test exécutée');
        console.log('🧪 Commande test exécutée');
        vscode.window.showInformationMessage('🧪 Commande Meshr-Lang: Test exécutée !');

        if (client && clientState === State.Running) {
            channel.appendLine('✅ Client LSP disponible, envoi de la requête de test');
            client.sendRequest('initialize', {
                processId: process.pid,
                rootUri: vscode.workspace.workspaceFolders?.[0]?.uri.toString(),
                capabilities: {}
            }).then((result) => {
                channel.appendLine(`✅ Initialisation LSP réussie: ${JSON.stringify(result)}`);
            }).catch((error: any) => {
                channel.appendLine(`❌ Erreur initialisation LSP: ${error.message}`);
            });
        } else {
            channel.appendLine('❌ Client LSP non disponible');
            vscode.window.showWarningMessage('⚠️ Serveur LSP non disponible. Démarrez-le avant de tester.');
        }
    });

    const restartServerCommand = vscode.commands.registerCommand('meshr-lang.restartServer', async () => {
        channel.appendLine('🔄 Redémarrage du serveur LSP...');
        console.log('🔄 Redémarrage du serveur LSP...');

        try {
            const stopResult = await stopClient();
            if (stopResult === 'error') {
                vscode.window.showErrorMessage('Erreur redémarrage: impossible d\'arrêter le serveur LSP');
                return;
            }

            await startClient({ showNotification: false });
            channel.appendLine('✅ Serveur LSP redémarré avec succès');
            vscode.window.showInformationMessage('🔄 Serveur LSP redémarré avec succès !');
        } catch (error: any) {
            const message = error?.message ?? String(error);
            channel.appendLine(`❌ Erreur lors du redémarrage: ${message}`);
            console.error('❌ Erreur lors du redémarrage:', error);
            vscode.window.showErrorMessage(`Erreur redémarrage: ${message}`);
        }
    });

    const showOutputCommand = vscode.commands.registerCommand('meshr-lang.showOutput', () => {
        channel.show();
        channel.appendLine('📋 Affichage de la sortie demandé');
        console.log('📋 Affichage de la sortie demandé');
        vscode.window.showInformationMessage('📋 Sortie du serveur LSP affichée !');
    });

    const startServerCommand = vscode.commands.registerCommand('meshr-lang.startServer', async () => {
        channel.appendLine('🚀 Démarrage du serveur LSP...');
        console.log('🚀 Démarrage du serveur LSP...');

        try {
            const result = await startClient({ showNotification: false });
            if (result === 'started') {
                vscode.window.showInformationMessage('🚀 Serveur LSP démarré avec succès !');
            } else if (result === 'alreadyRunning') {
                vscode.window.showInformationMessage('⚠️ Serveur LSP déjà démarré');
            } else {
                vscode.window.showInformationMessage('⏳ Serveur LSP déjà en cours de démarrage');
            }
        } catch (error: any) {
            const message = error?.message ?? String(error);
            channel.appendLine(`❌ Erreur lors du démarrage: ${message}`);
            console.error('❌ Erreur lors du démarrage:', error);
            vscode.window.showErrorMessage(`Erreur démarrage: ${message}`);
        }
    });

    const stopServerCommand = vscode.commands.registerCommand('meshr-lang.stopServer', async () => {
        channel.appendLine('🛑 Arrêt du serveur LSP...');
        console.log('🛑 Arrêt du serveur LSP...');

        const result = await stopClient();
        if (result === 'stopped') {
            vscode.window.showInformationMessage('🛑 Serveur LSP arrêté avec succès !');
        } else if (result === 'notRunning') {
            vscode.window.showWarningMessage('⚠️ Serveur LSP déjà arrêté');
        } else {
            vscode.window.showErrorMessage('Erreur arrêt: consultez la sortie Meshr-Lang LSP Debug');
        }
    });

    // Commande pour revalider les diagnostics
    const revalidateCommand = vscode.commands.registerCommand('meshr-lang.revalidate', async () => {
        try {
            channel.appendLine('🔄 Revalidation des diagnostics demandée...');

            if (client && clientState === State.Running) {
                const result = await client.sendRequest('meshr-lang.revalidate', {});
                channel.appendLine(`✅ Revalidation terminée: ${JSON.stringify(result)}`);
                vscode.window.showInformationMessage('🔄 Diagnostics revalidés avec succès !');
            } else {
                channel.appendLine('⚠️ Serveur LSP non connecté');
                vscode.window.showWarningMessage('⚠️ Serveur LSP non connecté. Veuillez d\'abord démarrer le serveur.');
            }
        } catch (error: any) {
            const message = error?.message ?? String(error);
            channel.appendLine(`❌ Erreur lors de la revalidation: ${message}`);
            console.error('❌ Erreur lors de la revalidation:', error);
            vscode.window.showErrorMessage(`Erreur revalidation: ${message}`);
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
        channel,
        { dispose: () => { void stopClient(); } }
    );
}

export async function deactivate() {
    console.log('🎨 Extension Meshr-Lang LSP Debug désactivée !');
    
    const result = await stopClient();
    if (result === 'stopped') {
        outputChannel?.appendLine('✅ Client LSP arrêté lors de la désactivation');
    }

    outputChannel?.appendLine('🎨 Extension Meshr-Lang LSP Debug désactivée');
    outputChannel?.dispose();
}
