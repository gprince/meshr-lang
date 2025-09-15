#!/usr/bin/env python3
"""
Test de connexion LSP pour diagnostiquer le problème
"""

import subprocess
import sys
import json
import time
from pathlib import Path

def test_lsp_server():
    """Test du serveur LSP en mode stdio"""
    
    print("=== Test de connexion LSP ===\n")
    
    # Chemin vers le serveur
    server_path = Path(__file__).parent / "lsp" / "server" / "main.py"
    
    if not server_path.exists():
        print(f"❌ Serveur non trouvé: {server_path}")
        return False
    
    print(f"📁 Serveur trouvé: {server_path}")
    
    # Message d'initialisation LSP
    init_message = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "processId": None,
            "rootUri": f"file://{Path(__file__).parent}",
            "capabilities": {
                "textDocument": {
                    "diagnostic": {}
                }
            }
        }
    }
    
    try:
        # Lancer le serveur
        print("🚀 Lancement du serveur LSP...")
        process = subprocess.Popen(
            [sys.executable, str(server_path)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=str(Path(__file__).parent)
        )
        
        # Envoyer le message d'initialisation
        message = json.dumps(init_message) + "\n"
        print(f"📤 Envoi: {message.strip()}")
        
        process.stdin.write(message)
        process.stdin.flush()
        
        # Attendre la réponse
        time.sleep(2)
        
        # Lire la réponse
        if process.stdout.readable():
            response = process.stdout.readline()
            print(f"📥 Réponse: {response.strip()}")
            
            if response.strip():
                try:
                    response_data = json.loads(response)
                    if "result" in response_data:
                        print("✅ Serveur LSP répond correctement")
                        return True
                except json.JSONDecodeError:
                    print("❌ Réponse JSON invalide")
            else:
                print("❌ Aucune réponse du serveur")
        
        # Vérifier les erreurs
        if process.stderr.readable():
            error = process.stderr.read()
            if error:
                print(f"❌ Erreur du serveur: {error}")
        
        process.terminate()
        return False
        
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

def test_extension_activation():
    """Test de l'activation de l'extension"""
    
    print("\n=== Test d'activation de l'extension ===\n")
    
    # Vérifier que l'extension est installée
    try:
        result = subprocess.run(
            ["cursor", "--list-extensions"],
            capture_output=True,
            text=True
        )
        
        if "meshr-lang" in result.stdout:
            print("✅ Extension Meshr-Lang installée")
        else:
            print("❌ Extension Meshr-Lang non trouvée")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors de la vérification de l'extension: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("🔍 Diagnostic du problème LSP Meshr-Lang\n")
    
    # Test 1: Extension
    extension_ok = test_extension_activation()
    
    # Test 2: Serveur LSP
    server_ok = test_lsp_server()
    
    print("\n" + "="*50)
    print("📊 Résultats du diagnostic:")
    print(f"   Extension: {'✅ OK' if extension_ok else '❌ Problème'}")
    print(f"   Serveur LSP: {'✅ OK' if server_ok else '❌ Problème'}")
    
    if extension_ok and server_ok:
        print("\n🎉 Tout fonctionne ! Le problème pourrait être dans la configuration de Cursor.")
    else:
        print("\n🔧 Des corrections sont nécessaires.")
