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
const node_1 = require("vscode-languageclient/node");
let client;
function activate(context) {
    console.log('Extension Meshr-Lang activée');
    // Configuration du serveur LSP
    const serverOptions = {
        run: {
            command: getServerCommand(),
            args: getServerArgs(),
            options: {
                cwd: getServerCwd()
            },
            transport: node_1.TransportKind.stdio
        },
        debug: {
            command: getServerCommand(),
            args: getServerArgs(),
            options: {
                cwd: getServerCwd()
            },
            transport: node_1.TransportKind.stdio
        }
    };
    // Configuration du client LSP
    const clientOptions = {
        documentSelector: [{ scheme: 'file', language: 'meshr' }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/.meshr')
        }
    };
    // Créer le client LSP
    client = new node_1.LanguageClient('meshr-lang-server', 'Meshr-Lang Language Server', serverOptions, clientOptions);
    // Démarrer le client
    client.start();
    // Enregistrer les commandes
    context.subscriptions.push(vscode.commands.registerCommand('meshr-lang.restartServer', () => {
        restartServer();
    }));
    context.subscriptions.push(vscode.commands.registerCommand('meshr-lang.showOutput', () => {
        client.outputChannel.show();
    }));
    // Nettoyer à la désactivation
    context.subscriptions.push({
        dispose: () => {
            if (client) {
                client.stop();
            }
        }
    });
}
exports.activate = activate;
function deactivate() {
    if (!client) {
        return undefined;
    }
    return client.stop();
}
exports.deactivate = deactivate;
function getServerCommand() {
    const config = vscode.workspace.getConfiguration('meshr-lang.server');
    return config.get('path', 'python');
}
function getServerArgs() {
    const config = vscode.workspace.getConfiguration('meshr-lang.server');
    return config.get('args', ['-m', 'lsp.server.main']);
}
function getServerCwd() {
    const config = vscode.workspace.getConfiguration('meshr-lang.server');
    const cwd = config.get('cwd', '${workspaceFolder}');
    // Remplacer les variables d'environnement
    if (cwd.includes('${workspaceFolder}')) {
        const workspaceFolder = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
        if (workspaceFolder) {
            return cwd.replace('${workspaceFolder}', workspaceFolder);
        }
    }
    return cwd;
}
async function restartServer() {
    if (client) {
        await client.stop();
        client.start();
        vscode.window.showInformationMessage('Serveur LSP Meshr-Lang redémarré');
    }
}
//# sourceMappingURL=extension.js.map