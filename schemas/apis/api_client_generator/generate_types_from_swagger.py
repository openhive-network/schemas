from __future__ import annotations

import re
from pathlib import Path
from typing import TYPE_CHECKING

from datamodel_code_generator import DataModelType, InputFileType, generate

from schemas.apis.api_client_generator._private.resolve_needed_imports import (
    compute_full_module_name,
    find_package_root,
)

if TYPE_CHECKING:
    from collections.abc import Callable


def generate_types_from_swagger(
    openapi_api_definition: str | Path,
    output: str | Path,
    base_class: str = "",
    custom_class_name_generator: Callable[[str], str] | None = None,
) -> None:
    """
    Generate types defined in Swagger.

    Args:
        openapi_api_definition: The OpenAPI JSON definition file path.
        output: The output file / package path where the generated types will be saved.

    Notes:
        The generated types will be saved in the specified output directory, and relative imports will be fixed
        to use absolute imports based on the package structure.

    Raises:
        FileNotFoundError: If the OpenAPI definition file does not exist.
    """
    openapi_file = Path(openapi_api_definition)
    output = Path(output)

    if not openapi_file.exists():
        raise FileNotFoundError(f"File {openapi_file} does not exist.")

    generate(  # generation of types available in the API definition
        openapi_file,
        output=output,
        output_model_type=DataModelType.MsgspecStruct,
        input_file_type=InputFileType.OpenAPI,
        use_field_description=True,
        use_standard_collections=True,
        apply_default_values_for_required_fields=True,
        use_union_operator=True,
        strict_nullable=True,
        base_class=base_class,
        custom_class_name_generator=custom_class_name_generator,
    )

    package_root = find_package_root(output)
    path_to_add_to_imports = compute_full_module_name(output, package_root)

    if path_to_add_to_imports.startswith(
        "."
    ):  # There is just one dot which means that output is in the same directory as package root
        path_to_add_to_imports = path_to_add_to_imports.replace(".", "", 1)

    fix_relative_imports(output, path_to_add_to_imports)


def fix_relative_imports(output_dir: Path, path_to_add: str) -> None:
    """
    Replace relative imports (from .xyz import ...) with absolute imports using the path_to_add.

    Args:
        output_dir: Directory with generated Python files.
        path_to_add: Path to use in absolute imports.
    """
    for py_file in output_dir.rglob("*.py"):
        content = py_file.read_text(encoding="utf-8")

        fixed_content = re.sub(
            r"^from \.(\w+) import (.+)$", rf"from {path_to_add}.\1 import \2", content, flags=re.MULTILINE
        )

        py_file.write_text(fixed_content, encoding="utf-8")
