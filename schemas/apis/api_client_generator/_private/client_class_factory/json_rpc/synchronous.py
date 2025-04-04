from __future__ import annotations

import ast
from typing import TYPE_CHECKING

from schemas.apis.api_client_generator._private.client_class_factory.common import (
    create_api_client as common_create_api_client,
)
from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import (
    BaseApiClass,
    EndpointsDefinition,
    Importable,
)
from schemas.apis.api_client_generator._private.endpoints_factory import create_json_rpc_endpoint

if TYPE_CHECKING:
    import ast


def create_api_client(
    api_name: str,
    endpoints: EndpointsDefinition,
    base_class: BaseApiClass | str,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    init_args: tuple[tuple[str, Importable]] | None = None,
) -> ast.ClassDef:
    """
    Creates a client class for the given API name and endpoints.

    Args:
        api_name (str): The name of the API. Will be used as class name (converted to the CamelCase).
        endpoints (EndpointsDefinition): The endpoints definition for the API.
        base_class(BaseApiClass | str): The base class for the API client.
        endpoint_decorator(str): The name of the endpoint decorator to be used.
        init_args(tuple[tuple[str, Importable]] | None): The arguments for the __init__ method of the API client class.

    Notes:
        - The `base_class` must contain an `endpoint` class method/variable.
        - `__init__` method will be created if `init_args` is provided.
    """

    return common_create_api_client(
        api_name,
        endpoints,
        create_json_rpc_endpoint,
        base_class,
        endpoint_decorator,
        init_args,
    )
