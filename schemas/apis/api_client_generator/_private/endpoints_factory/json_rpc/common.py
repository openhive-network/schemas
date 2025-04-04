from __future__ import annotations

import ast
from dataclasses import MISSING, fields, is_dataclass

from schemas.apis.api_client_generator._private.common.models_aliased import Dataclass


def get_endpoint_args(params: Dataclass | None) -> ast.arguments:
    """
    Generate arguments for the json-rpc api endpoint method.

    Args:
        params(Dataclass | None): The dataclass representing the parameters for the API endpoint.

    Returns:
        ast.arguments: The arguments for the API endpoint method.

    Raises:
        ValueError: If the params is not a dataclass.
    """

    if params is not None and not is_dataclass(params):
        raise ValueError("If params is not None, it must be a dataclass")

    defaults: list[ast.Constant | None] = []

    if params is not None:
        for param in fields(params):
            if param.default is not MISSING:
                defaults.append(ast.Constant(value=param.default))
            else:
                defaults.append(None)

    return ast.arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[
            ast.arg(
                arg=param.name,
                annotation=ast.Name(id=param.type, ctx=ast.Load()),  # type: ignore[arg-type]
            )
            for param in fields(params)
        ]
        if params
        else [],
        kw_defaults=defaults,  # type: ignore[arg-type]
        kwarg=None,
        defaults=[],
    )
