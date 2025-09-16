# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/lsp/server/standalone_language_server.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/lsp/server/*.py', '.'), ('/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/meshr_project.py', '.')],
    hiddenimports=['pygls', 'lsprotocol', 'lsprotocol.types', 'toml', 'antlr4', 'antlr4.InputStream', 'antlr4.CommonTokenStream', 'antlr4.ParseTreeWalker', 'antlr4.error.ErrorListener'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='meshr-lsp-server',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
