from __future__ import annotations

from typing import TYPE_CHECKING

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import Dataclass, Importable
from schemas.apis.api_client_generator._private.endpoints_factory.common import (
    create_async_endpoint as create_endpoint_common,
)
from schemas.apis.api_client_generator._private.endpoints_factory.json_rpc.common import get_endpoint_args

if TYPE_CHECKING:
    import ast


def create_endpoint(  # NOQA: PLR0913
    name: str,
    params: Dataclass | None = None,
    result: Importable | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    description: str | None = None,
    *,
    response_array: bool = False,
) -> ast.AsyncFunctionDef:
    """
    Create asynchronous JSON-RPC endpoint method.

    Args:
        name(str): The name of the endpoint.
        params(Dataclass | None): A dataclass of parameters.
        result( Importable | None): The type of the result.
        endpoint_decorator(str): The decorator for the endpoint.
        description(str | None): The description of the endpoint.
        response_array(bool): If True, the result type will be a list of the result type.

    Notice:
        Please note that the `params` argument is expected to be dataclasses (or any object
        that is compatible with `fields` method from `dataclasses` module).

    Returns:
        ast.AsyncFunctionDef: The AST representation of the endpoint method.

    Raises:
        ValueError: If the params is not a dataclass.
    """

    return create_endpoint_common(
        name, get_endpoint_args(params), endpoint_decorator, result, description, response_array=response_array
    )
