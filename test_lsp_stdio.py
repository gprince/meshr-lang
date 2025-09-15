#!/usr/bin/env python3
"""
Test du serveur LSP en mode stdio pour diagnostiquer le problème
"""

import subprocess
import sys
import json
import time
from pathlib import Path

def test_lsp_stdio():
    """Test du serveur LSP en mode stdio"""
    
    print("=== Test du serveur LSP en mode stdio ===\n")
    
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
        
        # Envoyer le message d'initialisation avec Content-Length header
        message = json.dumps(init_message)
        content_length = len(message.encode('utf-8'))
        header = f"Content-Length: {content_length}\r\n\r\n"
        
        print(f"📤 Envoi header: {header.strip()}")
        print(f"📤 Envoi message: {message}")
        
        process.stdin.write(header + message)
        process.stdin.flush()
        
        # Attendre la réponse
        time.sleep(2)
        
        # Lire la réponse
        if process.stdout.readable():
            # Lire les headers
            headers = {}
            while True:
                line = process.stdout.readline()
                if line.strip() == "":
                    break
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    headers[key.strip()] = value.strip()
                print(f"📥 Header: {line.strip()}")
            
            # Lire le message JSON
            content_length = int(headers.get("Content-Length", "0"))
            if content_length > 0:
                response = process.stdout.read(content_length)
                print(f"📥 Réponse JSON: {response}")
                
                try:
                    response_data = json.loads(response)
                    if "result" in response_data:
                        print("✅ Serveur LSP répond correctement")
                        print(f"📊 Résultat: {response_data['result']}")
                        return True
                    elif "error" in response_data:
                        print(f"❌ Erreur du serveur: {response_data['error']}")
                        return False
                except json.JSONDecodeError as e:
                    print(f"❌ Réponse JSON invalide: {e}")
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

if __name__ == "__main__":
    test_lsp_stdio()
