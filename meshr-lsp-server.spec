# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all

datas = [('/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/lsp/server/*.py', '.'), ('/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/meshr_project.py', '.')]
binaries = []
hiddenimports = ['toml', 'antlr4', 'antlr4.InputStream', 'antlr4.CommonTokenStream', 'antlr4.ParseTreeWalker', 'antlr4.error.ErrorListener']
datas += collect_data_files('lsprotocol')
datas += collect_data_files('pygls')
hiddenimports += collect_submodules('pygls')
hiddenimports += collect_submodules('lsprotocol')
tmp_ret = collect_all('pygls')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('lsprotocol')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['/Users/gregory_prince/Documents/Workspaces/lang/meshr-lang/lsp/server/standalone_language_server.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
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
