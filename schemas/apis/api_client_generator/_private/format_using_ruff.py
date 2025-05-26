from __future__ import annotations

import subprocess

from ruff.__main__ import find_ruff_bin  # type: ignore[import-untyped]

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_LINE_LENGTH_FOR_RUFF


def format_using_ruff(code: str, line_length: int = DEFAULT_LINE_LENGTH_FOR_RUFF) -> str:
    """Format the given code using Ruff."""

    try:
        ruff_bin = find_ruff_bin()
    except FileNotFoundError:
        ruff_bin = "ruff"

    try:
        completed_process = subprocess.run(
            [
                ruff_bin,
                "format",
                "--config",
                f"line-length={line_length}",
                "--stdin-filename",
                "file.py",
                "-",
            ],
            check=True,
            capture_output=True,
            text=True,
            input=code,
        )
    except subprocess.CalledProcessError:
        return code
    else:
        return completed_process.stdout
