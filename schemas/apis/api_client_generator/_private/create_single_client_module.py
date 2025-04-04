from __future__ import annotations

import ast
from typing import Sequence

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import (
    ApiDefinition,
    ClientClassFactory,
    Importable,
    ensure_is_importable,
)
from schemas.apis.api_client_generator._private.resolve_needed_imports import (
    import_class,
    import_classes,
    import_params_types,
)


def create_single_client_module(  # NOQA: PLR0913
    api_definition: ApiDefinition,
    client_class_factory: ClientClassFactory,
    base_class: Importable | str,
    base_class_source: str | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
) -> ast.Module:
    """
    Generate an API client class based on the provided API name, definition, and type.

    Args:
        api_definition(ApiDefinition): The definition of the API.
        client_class_factory(ClientClassFactory): The factory function to create api client class.
        base_class(Importable | str): The base class for the API client. Should include the necessary `endpoint` decorator.
        base_class_source(str | None): The source of the base class. If None, a default source will be used.
        endpoint_decorator(str): The name of the endpoint decorator to be used.
        additional_items_to_import(Sequence[Importable] | None): Additional things to import in the created module.

    Raises:
        AssertionError: If the API definition does not contain endpoints.
    """
    api_definition.pop("type", None)  # Remove the "type" key from the definition

    api_name = next(iter(api_definition.keys()))
    endpoints = api_definition.get(api_name)
    assert endpoints is not None, "API definition must contain endpoints"

    generated_client = client_class_factory(api_name, endpoints, base_class, endpoint_decorator)

    needed_results = [ensure_is_importable(params["result"]) for params in endpoints.values() if params.get("result")]

    needed_params_import = []
    already_imported: list[str] = []  # List of already imported classes to avoid duplicates

    for params in endpoints.values():
        if params.get("params") is not None:
            needed_params_import.extend(import_params_types(params["params"], already_imported))

    additional_imports = import_classes(additional_items_to_import or [], already_imported)

    all_imports = additional_imports + import_classes(needed_results, already_imported) + needed_params_import

    base_class_import = import_class(base_class, base_class_source)

    if base_class_import:
        all_imports.insert(0, base_class_import)

    return ast.Module(
        body=[*all_imports, generated_client],
        type_ignores=[],
    )
