#!/usr/bin/env python3
"""
Script de build pour créer un serveur LSP standalone
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path

def build_server():
    """Build le serveur LSP avec PyInstaller"""
    
    server_dir = Path(__file__).parent
    output_dir = server_dir / "dist"
    client_dir = server_dir.parent / "client"
    
    # Nettoyer les builds précédents
    if output_dir.exists():
        shutil.rmtree(output_dir)
    
    # Créer le répertoire de sortie
    output_dir.mkdir(exist_ok=True)
    
    # Commande PyInstaller
    cmd = [
        "pyinstaller",
        "--onefile",
        "--name", "meshr-lsp-server",
        "--distpath", str(output_dir),
        "--add-data", f"{server_dir}/*.py:.",
        "--add-data", f"{server_dir.parent.parent}/meshr_project.py:.",
        "--hidden-import", "toml",
        "--hidden-import", "antlr4",
        "--hidden-import", "antlr4.InputStream",
        "--hidden-import", "antlr4.CommonTokenStream",
        "--hidden-import", "antlr4.ParseTreeWalker",
        "--hidden-import", "antlr4.error.ErrorListener",
        "--collect-submodules", "pygls",
        "--collect-submodules", "lsprotocol",
        "--collect-data", "lsprotocol",
        "--collect-data", "pygls",
        "--collect-all", "pygls",
        "--collect-all", "lsprotocol",
        str(server_dir / "standalone_language_server.py")
    ]
    
    print("🔨 Building LSP server...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        env = os.environ.copy()
        cache_dir = server_dir / "pyinstaller_cache"
        config_dir = server_dir / "pyinstaller_config"
        cache_dir.mkdir(exist_ok=True)
        config_dir.mkdir(exist_ok=True)

        env["PYINSTALLER_CACHE_DIR"] = str(cache_dir)
        env["PYINSTALLER_CONFIG_DIR"] = str(config_dir)

        result = subprocess.run(cmd, check=True, capture_output=True, text=True, env=env)
        print("✅ Server built successfully!")
        
        # Copier vers le répertoire client
        server_binary = output_dir / "meshr-lsp-server"
        client_server_dir = client_dir / "server"
        client_server_dir.mkdir(exist_ok=True)
        
        shutil.copy2(server_binary, client_server_dir / "meshr-lsp-server")
        print(f"✅ Server copied to: {client_server_dir / 'meshr-lsp-server'}")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        print(f"Error output: {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller not found. Install with: pip install pyinstaller")
        return False

if __name__ == "__main__":
    build_server()
