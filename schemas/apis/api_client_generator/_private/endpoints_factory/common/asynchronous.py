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
) -> ast.AsyncFunctionDef:
    """
    Create asynchronous endpoint method.

    Args:
        name(str): The name of the endpoint.
        endpoint_arguments(ast.arguments): The arguments for the endpoint.
        endpoint_decorator(str): The name of the endpoint decorator to be used.
        result_type(Importable | None): The type of the result.
        description(str | None): The description of the endpoint.
        response_array(bool): If True, the result type will be a list of the result type.

    Notes:
        - The method body contains an ellipsis (`...`), decorator do all the work.
        - If `result_type` is provided, it will be used as the return type hint.
        - The first argument is always `self` (function always add it automatically).

    Returns:
        ast.AsyncFunctionDef: The AST representation of the endpoint method.
    """
    endpoint_arguments.args.insert(0, ast.arg(arg="self"))
    body = [
        ast.Expr(value=ast.Constant(value=Ellipsis))
        if not description
        else ast.Expr(value=ast.Constant(value=description))
    ]

    returns = (
        ast.Name(id=result_type.__name__ if not response_array else f"list[{result_type.__name__}]", ctx=ast.Load())
        if result_type is not None
        else None
    )

    return ast.AsyncFunctionDef(  # type: ignore[no-any-return, call-overload]
        name=name,
        args=endpoint_arguments,
        body=body,
        decorator_list=[ast.Name(id=endpoint_decorator, ctx=ast.Load())],
        returns=returns,
    )
