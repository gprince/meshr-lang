"""Minimal TOML wrapper using the standard library `tomllib`.

This replaces the external `toml` dependency so the language server can
operate without requiring network access to install third-party packages.
Only the APIs used by Meshr-Lang (`load` and `loads`) are implemented.
"""

from __future__ import annotations

import io
import os
from pathlib import Path
import tomllib
from typing import Any, BinaryIO, TextIO


def _read_to_str(stream: BinaryIO | TextIO) -> str:
    data = stream.read()
    if isinstance(data, bytes):
        return data.decode("utf-8")
    return data


def load(fp: str | os.PathLike[str] | BinaryIO | TextIO, *, parse_float=None) -> Any:
    """Parse TOML content from a file path or file-like object."""

    if isinstance(fp, (str, os.PathLike, Path)):
        with Path(fp).expanduser().open("rb") as handle:
            return tomllib.load(handle, parse_float=parse_float or float)

    # File-like object: normalise to text before parsing.
    text = _read_to_str(fp)
    return tomllib.loads(text, parse_float=parse_float or float)


def loads(s: str | bytes, *, parse_float=None) -> Any:
    """Parse TOML content from a string."""

    if isinstance(s, bytes):
        s = s.decode("utf-8")
    return tomllib.loads(s, parse_float=parse_float or float)

