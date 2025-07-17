from __future__ import annotations

import ast
from typing import Sequence

from schemas.apis.api_client_generator._private.common.defaults import (
    DEFAULT_API_COLLECTION_NAME,
    DEFAULT_ENDPOINT_DECORATOR_NAME,
)
from schemas.apis.api_client_generator._private.common.models_aliased import (
    ApiDescription,
    BaseApiClass,
    ClientClassFactory,
    Importable,
)
from schemas.apis.api_client_generator._private.create_collection_class import create_collection_class
from schemas.apis.api_client_generator._private.json_rpc_tools.api_name_tools import validate_api_name
from schemas.apis.api_client_generator._private.json_rpc_tools.create_client_and_imports import (
    create_client_and_imports,
)


def create_collection_module(  # NOQA: PLR0913
    api_descriptions: ApiDescription,
    client_class_factory: ClientClassFactory,
    base_class: type[BaseApiClass] | str,
    base_class_source: str | None = None,
    collection_name: str = DEFAULT_API_COLLECTION_NAME,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
    *,
    asynchronous: bool = True,
) -> ast.Module:
    """
    Generate an API client class based on the provided API descriptions.

    Args:
        api_descriptions: The description of the APIs.
        client_class_factory: The factory function to create api client class.
        base_class: The base class for the API client.
        base_class_source: The source of the base class. If None, a `__module__` will be used.
        collection_name: The name of the collection class.
        endpoint_decorator: The name of the endpoint decorator to be used.
        additional_items_to_import: Additional things to import in the created module.
        asynchronous: If True, the endpoints will be created as asynchronous methods.

    Raises:
        InvalidApiNameError: If the API name is invalid.
    """

    generated_clients = []
    already_imported: list[str] = []  # List of already imported classes to avoid duplicates
    imports: list[ast.ImportFrom] = []

    for api_name, endpoints in api_descriptions.items():
        validate_api_name(api_name)

        created_client = create_client_and_imports(
            api_name,
            client_class_factory,
            endpoints,
            base_class,
            base_class_source,
            endpoint_decorator,
            additional_items_to_import,
            already_imported,
            asynchronous=asynchronous,
        )
        generated_clients.append(created_client.class_def)
        imports.extend(created_client.imports)

    collection = create_collection_class(collection_name, generated_clients)

    return ast.Module(
        body=[*imports, collection, *generated_clients],
        type_ignores=[],
    )
