from __future__ import annotations

import ast

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import Importable


def create_endpoint(  # NOQA: PLR0913
    name: str,
    endpoint_arguments: ast.arguments,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    result_type: Importable | None = None,
    description: str | None = None,
    *,
    response_array: bool = False,
    asynchronous: bool = True,
) -> ast.AsyncFunctionDef | ast.FunctionDef:
    """
    Create endpoint method.

    Args:
        name: The name of the endpoint.
        endpoint_arguments: The arguments for the endpoint.
        endpoint_decorator: The name of the endpoint decorator to be used.
        result_type: The type of the result.
        description: The description of the endpoint.
        response_array: If True, the result type will be a list of the result type.
        asynchronous: If True, the endpoint will be created as an asynchronous method.

    Notes:
        - The method body contains an ellipsis (`...`), decorator do all the work.
        - If `result_type` is provided, it will be used as the return type hint.
        - The first argument is always `self` (function always add it automatically).

    Returns:
        ast.AsyncFunctionDef | ast.FunctionDef: The AST representation of the endpoint method.
    """
    endpoint_arguments.args.insert(0, ast.arg(arg="self"))
    body: list[ast.stmt] = [
        ast.Expr(value=ast.Constant(value=Ellipsis))
        if not description
        else ast.Expr(value=ast.Constant(value=description))
    ]

    returns = (
        ast.Name(id=result_type.__name__ if not response_array else f"list[{result_type.__name__}]")
        if result_type is not None
        else None
    )

    function_def: type[ast.FunctionDef] | type[ast.AsyncFunctionDef] = (
        ast.AsyncFunctionDef if asynchronous else ast.FunctionDef
    )

    return function_def(
        name=name,
        args=endpoint_arguments,
        body=body,
        decorator_list=[ast.Name(id=endpoint_decorator)],
        returns=returns,
        type_params=[],
    )
