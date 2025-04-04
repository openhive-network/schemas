from __future__ import annotations

import ast
from typing import Sequence

from schemas.apis.api_client_generator._private.common.defaults import (
    DEFAULT_API_COLLECTION_NAME,
    DEFAULT_ENDPOINT_DECORATOR_NAME,
)
from schemas.apis.api_client_generator._private.common.models_aliased import (
    ApiDefinition,
    ClientClassFactory,
    Importable,
    ensure_is_importable,
)
from schemas.apis.api_client_generator._private.create_collection_class import create_api_collection
from schemas.apis.api_client_generator._private.resolve_needed_imports import (
    import_class,
    import_classes,
    import_params_types,
)


def create_collection_module(  # NOQA: PLR0913
    api_definitions: ApiDefinition,
    client_class_factory: ClientClassFactory,
    base_class: Importable | str,
    base_class_source: str | None = None,
    collection_name: str = DEFAULT_API_COLLECTION_NAME,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
) -> ast.Module:
    """
    Generate an API client class based on the provided API definitions.

    Args:
        api_definitions(ApiDefinition): The definition of the APIs.
        client_class_factory(ClientClassFactory): The factory function to create api client class.
        base_class(Importable | str): The base class for the API client. Should include the necessary `endpoint` decorator.
        base_class_source(str | None): The source of the base class. If None, a `__module__` will be used.
        collection_name(str): The name of the collection class.
        endpoint_decorator(str): The name of the endpoint decorator to be used.
        additional_items_to_import(Sequence[Importable] | None): Additional things to import in the created module.
    """

    generated_clients = []
    already_imported: list[str] = []  # List of already imported classes to avoid duplicates
    imports = import_classes(additional_items_to_import or [], already_imported)

    for api_name, endpoints in api_definitions.items():
        endpoints.pop("type", None)  # Remove the "type" key from the definition

        generated_clients.append(client_class_factory(api_name, endpoints, base_class, endpoint_decorator))

        needed_results = [
            ensure_is_importable(parameters["result"])
            for parameters in endpoints.values()
            if parameters.get("result") is not None
        ]

        needed_params_import = []
        for params in endpoints.values():
            if params.get("params") is not None:
                needed_params_import.extend(import_params_types(params["params"], already_imported))

        imports.extend(import_classes(needed_results, already_imported) + needed_params_import)

    base_class_import = import_class(base_class, base_class_source)
    if base_class_import is not None:
        imports.insert(0, base_class_import)

    collection = create_api_collection(collection_name, generated_clients)

    return ast.Module(
        body=[*imports, collection, *generated_clients],
        type_ignores=[],
    )
