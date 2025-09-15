#!/usr/bin/env python3
"""
Test de l'extension LSP avec débogage
"""

import json
import os
import subprocess
import sys
import time
import threading

def test_extension_lsp_debug():
    """Test de l'extension LSP avec débogage"""
    print("🧪 Test de l'extension LSP avec débogage...")
    
    # Vérifier que l'extension est compilée
    extension_js = "/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/lsp/client/out/extension_lsp_debug.js"
    if not os.path.exists(extension_js):
        print("❌ Extension LSP debug non compilée")
        return False
    
    # Vérifier le contenu
    with open(extension_js, 'r') as f:
        content = f.read()
    
    # Vérifier que les commandes sont présentes
    required_commands = [
        'meshr-lang.test',
        'meshr-lang.restartServer',
        'meshr-lang.showOutput',
        'meshr-lang.startServer',
        'meshr-lang.stopServer'
    ]
    
    for cmd in required_commands:
        if f"'{cmd}'" in content or f'"{cmd}"' in content:
            print(f"✅ Commande {cmd} trouvée")
        else:
            print(f"❌ Commande {cmd} manquante")
            return False
    
    # Vérifier que le client LSP est configuré
    if 'LanguageClient' in content and 'lsp.server.main' in content:
        print("✅ Client LSP configuré")
    else:
        print("❌ Client LSP non configuré")
        return False
    
    # Vérifier que les logs de débogage sont présents
    if 'outputChannel' in content and 'appendLine' in content:
        print("✅ Logs de débogage configurés")
    else:
        print("❌ Logs de débogage manquants")
        return False
    
    # Vérifier le package.json
    package_json_path = "/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/lsp/client/package.json"
    with open(package_json_path, 'r') as f:
        package_data = json.load(f)
    
    main_file = package_data.get('main', '')
    if main_file == './out/extension_lsp_debug.js':
        print("✅ Main pointe vers extension_lsp_debug.js")
    else:
        print(f"❌ Main pointe vers {main_file}")
        return False
    
    # Vérifier les activation events
    activation_events = package_data.get('activationEvents', [])
    if 'onLanguage:meshr' in activation_events:
        print("✅ Activation sur onLanguage:meshr")
    else:
        print(f"❌ Activation events: {activation_events}")
        return False
    
    print("✅ Extension LSP avec débogage prête !")
    return True

if __name__ == "__main__":
    success = test_extension_lsp_debug()
    sys.exit(0 if success else 1)
