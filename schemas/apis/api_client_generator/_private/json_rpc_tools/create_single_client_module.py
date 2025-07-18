from __future__ import annotations

import ast
from typing import Sequence

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_JSON_RPC_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import (
    ApiDescription,
    BaseApiClass,
    ClientClassFactory,
    Importable,
)
from schemas.apis.api_client_generator._private.json_rpc_tools.api_name_tools import (
    get_api_name_from_description,
    validate_api_name,
)
from schemas.apis.api_client_generator._private.json_rpc_tools.create_client_and_imports import (
    create_client_and_imports,
)


def create_single_client_module(  # NOQA: PLR0913
    api_description: ApiDescription,
    client_class_factory: ClientClassFactory,
    base_class: type[BaseApiClass] | str,
    base_class_source: str | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_JSON_RPC_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
    *,
    asynchronous: bool = True,
) -> ast.Module:
    """
    Generate an API client class based on the provided API name, description, and type.

    Args:
        api_description: The description of the API.
        client_class_factory: The factory function to create api client class.
        base_class: The base class for the API client.
        base_class_source: The source of the base class. If None, a default source will be used.
        endpoint_decorator: The name of the endpoint decorator to be used.
        additional_items_to_import(: Additional things to import in the created module.
        asynchronous: If True, the endpoints will be created as asynchronous methods.

    Raises:
        AssertionError: If the API description does not contain endpoints.
        InvalidApiNameError: If the API name is invalid.
    """

    api_name = get_api_name_from_description(api_description)
    validate_api_name(api_name)
    endpoints = api_description.get(api_name)
    assert endpoints is not None, "API description must contain endpoints"
    generated_client = create_client_and_imports(
        api_name,
        client_class_factory,
        endpoints,
        base_class,
        base_class_source,
        endpoint_decorator,
        additional_items_to_import,
        asynchronous=asynchronous,
    )

    return ast.Module(
        body=[*generated_client.imports, generated_client.class_def],
        type_ignores=[],
    )
