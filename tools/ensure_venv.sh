#!/usr/bin/env bash
# Ensure Meshr-Lang virtual environment exists and is activated

set -euo pipefail

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    echo "❌ Ce script doit être sourcé : source tools/ensure_venv.sh"
    exit 1
fi

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${MESHR_VENV_DIR:-$PROJECT_ROOT/.venv}"
if [[ "$VENV_DIR" != /* ]]; then
    VENV_DIR="$PROJECT_ROOT/$VENV_DIR"
fi

if [[ -n "${VIRTUAL_ENV:-}" ]]; then
    if [[ "$VIRTUAL_ENV" == "$VENV_DIR" ]]; then
        echo "✅ Environnement virtuel déjà actif : $VIRTUAL_ENV"
        return 0 2>/dev/null || exit 0
    else
        echo "ℹ️ Un autre environnement virtuel est actif ($VIRTUAL_ENV)."
        echo "   Désactivez-le avant d'activer celui de Meshr-Lang."
        return 1 2>/dev/null || exit 1
    fi
fi

if [[ ! -d "$VENV_DIR" ]]; then
    echo "🛠️ Création de l'environnement virtuel dans $VENV_DIR"
    python3 -m venv "$VENV_DIR"
fi

echo "✅ Activation de l'environnement virtuel Meshr-Lang"
# shellcheck disable=SC1090
source "$VENV_DIR/bin/activate"

python - <<'PY'
import ensurepip
import sys
from pathlib import Path
import zipfile

ensurepip.bootstrap(upgrade=True, default_pip=True)

target = Path(sys.prefix) / 'lib' / f'python{sys.version_info.major}.{sys.version_info.minor}' / 'site-packages'
pip_dir = target / 'pip'
if not pip_dir.exists():
    bundled = Path(ensurepip.__file__).parent / '_bundled'
    for wheel in bundled.glob('pip-*.whl'):
        with zipfile.ZipFile(wheel) as zf:
            zf.extractall(target)
        break
PY

echo "🎉 Environnement Meshr-Lang actif : $VIRTUAL_ENV"
