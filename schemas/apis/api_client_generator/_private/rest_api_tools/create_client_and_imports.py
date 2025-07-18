from __future__ import annotations

import ast
from pathlib import Path
from typing import Sequence

from schemas.apis.api_client_generator._private.common.converters import snake_to_camel
from schemas.apis.api_client_generator._private.common.defaults import (
    DEFAULT_ENDPOINT_REST_DECORATOR_NAME,
    DEFAULT_IMPORT_LEVEL,
)
from schemas.apis.api_client_generator._private.common.generated_class import GeneratedClass
from schemas.apis.api_client_generator._private.common.models_aliased import (
    BaseApiClass,
    Importable,
)
from schemas.apis.api_client_generator._private.resolve_needed_imports import (
    compute_full_module_name,
    find_package_root,
    import_class,
    import_classes,
)
from schemas.apis.api_client_generator._private.rest_api_tools.models_aliased import CreatedEndpoints


def create_client_and_imports(  # NOQA: PLR0913
    api_name: str,
    server_url: str,
    endpoints: CreatedEndpoints,
    types_module_path: str | Path,
    base_class: type[BaseApiClass] | str,
    base_class_source: str | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_REST_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
    already_imported: list[str] | None = None,
) -> GeneratedClass:
    """
    Create a client class and resolve the needed imports.

    Args:
        api_name: The name of the API.
        server_url: The server URL for the API.
        types_module_path: The path to the module containing types.
        endpoints: The endpoints description for the API.
        base_class: The base class for the API client.
        base_class_source: The source of the base class.
        endpoint_decorator: The name of the endpoint decorator to be used.
        additional_items_to_import: Additional items to import.
        already_imported: A list of already imported items.
    """

    already_imported = already_imported or []

    needed_imports: list[ast.ImportFrom] = []

    base_class_import = import_class(base_class, base_class_source)

    if base_class_import is not None:
        needed_imports.append(base_class_import)

    base_class_name = base_class if isinstance(base_class, str) else base_class.__name__
    already_imported.append(base_class_name)

    types_module_path = Path(types_module_path)
    root = find_package_root(types_module_path)
    full_module_name = compute_full_module_name(types_module_path, root)

    needed_imports.append(
        ast.ImportFrom(
            module=full_module_name,
            names=[ast.alias(name="*")],
            level=DEFAULT_IMPORT_LEVEL,
        )
    )

    additional_imports = import_classes(additional_items_to_import or [], already_imported)
    needed_imports.extend(additional_imports)

    class_name = snake_to_camel(api_name)

    endpoint_decorator_assign = ast.Assign(  # Assign endpoint decorator as class variable
        targets=[ast.Name(id=endpoint_decorator)],
        value=ast.Attribute(
            value=ast.Name(id=base_class_name),
            attr=f"{endpoint_decorator}()",  # rest decorator is a class method of the base class
        ),
    )
    base_url_method = ast.FunctionDef(  # type: ignore[call-overload]
        name="base_path",
        args=ast.arg(arg="self"),
        returns=ast.Name(id="str"),
        body=[ast.Return(value=ast.Constant(value="/" + server_url))],
        decorator_list=[],
    )

    body: list[ast.stmt] = [endpoint_decorator_assign, base_url_method, *endpoints]

    class_def = ast.ClassDef(
        name=class_name,
        bases=[ast.Name(id=base_class_name)],
        keywords=[],
        body=body,
        decorator_list=[],
        type_params=[],
    )

    return GeneratedClass(
        class_def,
        needed_imports,
    )
