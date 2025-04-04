from __future__ import annotations

import ast
from pathlib import Path

from schemas.apis.api_client_generator._private.format_using_black import format_using_black


def export_module_to_file(module: ast.Module, file_path: Path | None = None) -> None:
    """
    Export an AST module to a Python file. Also formats the code using Black.

    Args:
        module: The AST module to export.
        file_path: The path to the file where the module will be saved.
        If None, defaults to "cwd/generated_api_client.py".
    """

    ast.fix_missing_locations(module)
    module_code = ast.unparse(module)

    formatted_module = format_using_black(module_code)

    if file_path is None:
        file_path = Path.cwd() / "generated_api_client.py"

    with file_path.open("w", encoding="utf-8") as f:
        f.write(formatted_module)
