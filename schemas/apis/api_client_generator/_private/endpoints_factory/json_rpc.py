from __future__ import annotations

import ast

from msgspec import NODEFAULT, Struct
from msgspec.structs import fields

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_JSON_RPC_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import Importable
from schemas.apis.api_client_generator._private.endpoints_factory.common import (
    create_endpoint as create_endpoint_common,
)
from schemas.apis.api_client_generator._private.resolve_needed_imports import is_struct
from schemas.apis.api_client_generator.exceptions import EndpointParamsIsNotMsgspecStructError


def create_endpoint(  # NOQA: PLR0913
    name: str,
    params: Struct | None = None,
    result: Importable | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_JSON_RPC_DECORATOR_NAME,
    description: str | None = None,
    *,
    response_array: bool = False,
    asynchronous: bool = True,
) -> ast.AsyncFunctionDef | ast.FunctionDef:
    """
    Create JSON-RPC endpoint method.

    Args:
        name: The name of the endpoint.
        params: A msgspec struct of parameters.
        result: The type of the result.
        endpoint_decorator: The decorator for the endpoint.
        description: The description of the endpoint.
        response_array: If True, the result type will be a list of the result type.
        asynchronous: If True, the endpoint will be created as an asynchronous method.

    Notice:
        Please note that the `params` argument is expected to be a msgspec struct.

    Returns:
        ast.AsyncFunctionDef | ast.FunctionDef: The AST representation of the endpoint method.

    Raises:
        EndpointParamsIsNotMsgspecStructError: If the params is not a msgspec struct.
    """

    return create_endpoint_common(
        name,
        get_endpoint_args(params),
        endpoint_decorator,
        result,
        description,
        response_array=response_array,
        asynchronous=asynchronous,
    )


def get_endpoint_args(params: Struct | None) -> ast.arguments:
    """
    Generate arguments for the json-rpc api endpoint method.

    Args:
        params: The msgspec struct representing the parameters for the API endpoint.

    Returns:
        ast.arguments: The arguments for the API endpoint method.

    Raises:
        EndpointParamsIsNotMsgspecStructError: If the params is not a msgspec struct.
    """

    arguments = ast.arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[],
    )

    if params is None:
        return arguments

    kwonlyargs: list[ast.arg] = []
    defaults: list[ast.expr | None] = []

    if not is_struct(params):
        raise EndpointParamsIsNotMsgspecStructError

    for param in fields(params):
        if param.default is not NODEFAULT:
            defaults.append(ast.Constant(value=param.default))
        else:
            defaults.append(None)

        kwonlyargs.append(
            ast.arg(
                arg=param.name,
                annotation=ast.Name(id=param.type.__name__),
            )
        )

    arguments.kwonlyargs = kwonlyargs
    arguments.kw_defaults = defaults
    return arguments
