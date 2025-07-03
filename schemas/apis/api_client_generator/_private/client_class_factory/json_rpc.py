from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.apis.api_client_generator._private.client_class_factory.common import (
    create_api_client as common_create_api_client,
)
from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import (
    BaseApiClass,
    EndpointsDescription,
)
from schemas.apis.api_client_generator._private.endpoints_factory import create_json_rpc_endpoint

if TYPE_CHECKING:
    import ast


def create_api_client(
    api_name: str,
    endpoints: EndpointsDescription,
    base_class: type[BaseApiClass] | str,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    *,
    asynchronous: bool = True,
) -> ast.ClassDef:
    """
    Creates a client class for the given API name and endpoints.


    Args:
        api_name: The name of the API. Will be used as class name (converted to the CamelCase).
        endpoints: The endpoints description for the API.
        base_class: The base class for the API client.
        endpoint_decorator: The name of the endpoint decorator to be used.
        asynchronous: If True, the endpoints will be created as asynchronous methods.
    """

    return common_create_api_client(
        api_name,
        endpoints,
        create_json_rpc_endpoint,  # type: ignore[arg-type]
        base_class,
        endpoint_decorator,
        asynchronous=asynchronous,
    )
