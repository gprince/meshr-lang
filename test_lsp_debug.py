#!/usr/bin/env python3
"""
Test du serveur LSP avec débogage
"""

import json
import subprocess
import sys
import time
import threading
import select
import os

def read_with_timeout(process, timeout=5):
    """Lire avec timeout"""
    try:
        ready, _, _ = select.select([process.stdout], [], [], timeout)
        if ready:
            return process.stdout.readline().decode('utf-8').strip()
        return None
    except:
        return None

def test_lsp_debug():
    """Test du serveur LSP avec débogage"""
    print("🧪 Test du serveur LSP avec débogage...")
    
    # Démarrer le serveur
    print("🚀 Démarrage du serveur LSP debug...")
    process = subprocess.Popen(
        ['python', '-m', 'lsp.server.main_debug'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=0,
        cwd='/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang'
    )
    
    # Thread pour lire les logs stderr
    def read_stderr():
        while True:
            line = process.stderr.readline()
            if not line:
                break
            print(f"📋 SERVEUR: {line.decode('utf-8').strip()}")
    
    stderr_thread = threading.Thread(target=read_stderr, daemon=True)
    stderr_thread.start()
    
    try:
        # Attendre que le serveur démarre
        time.sleep(2)
        
        # Envoyer la requête d'initialisation
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "processId": os.getpid(),
                "rootUri": "file:///Users/gregory_prince/Documents/Workspaces/lang/meshr-lang",
                "capabilities": {}
            }
        }
        
        request_data = json.dumps(init_request)
        request_message = f"Content-Length: {len(request_data)}\r\n\r\n{request_data}"
        
        print("📤 Envoi de la requête d'initialisation...")
        process.stdin.write(request_message.encode('utf-8'))
        process.stdin.flush()
        
        # Lire la réponse
        print("📥 Lecture de la réponse...")
        response = read_with_timeout(process, 10)
        if response:
            print(f"📥 Réponse reçue: {response}")
            
            # Lire le reste de la réponse
            content_length = int(response.split(': ')[1])
            remaining = process.stdout.read(content_length).decode('utf-8')
            print(f"📥 Contenu: {remaining}")
            
            try:
                response_data = json.loads(remaining)
                if 'result' in response_data:
                    print("✅ Initialisation réussie !")
                    print(f"✅ Capacités: {response_data['result'].get('capabilities', {})}")
                else:
                    print(f"❌ Erreur: {response_data.get('error', 'Inconnue')}")
            except json.JSONDecodeError as e:
                print(f"❌ Erreur JSON: {e}")
        else:
            print("❌ Aucune réponse reçue")
        
        # Test d'ouverture de document
        print("\n📖 Test d'ouverture de document...")
        doc_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "textDocument/didOpen",
            "params": {
                "textDocument": {
                    "uri": "file:///Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/stdlib/core/index.meshr",
                    "languageId": "meshr",
                    "version": 1,
                    "text": "module test\n!%£$% invalid syntax"
                }
            }
        }
        
        request_data = json.dumps(doc_request)
        request_message = f"Content-Length: {len(request_data)}\r\n\r\n{request_data}"
        
        print("📤 Envoi de la requête d'ouverture de document...")
        process.stdin.write(request_message.encode('utf-8'))
        process.stdin.flush()
        
        # Attendre les diagnostics
        time.sleep(2)
        
        print("✅ Test terminé")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Arrêter le serveur
        print("🛑 Arrêt du serveur...")
        process.terminate()
        process.wait()
        print("✅ Serveur arrêté")

if __name__ == "__main__":
    test_lsp_debug()
