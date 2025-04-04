from __future__ import annotations

import ast

from schemas.apis.api_client_generator._private.common.models_aliased import Importable


def create_init_method(*init_args: tuple[str, Importable]) -> ast.FunctionDef:
    """
    Create the __init__ method for a class.

    Args:
        init_args (tuple[str, Importable]): Each tuple contains the argument name and its type.

    Returns:
        ast.FunctionDef: The AST representation of the __init__ method.

    Notes:
        - The method initializes the instance attributes with the provided arguments.
        - The method does not include any default values for the arguments.
    """
    return ast.FunctionDef(  # type: ignore[no-any-return, call-overload]
        name="__init__",
        args=ast.arguments(
            posonlyargs=[],
            args=[ast.arg(arg="self")]
            + [ast.arg(arg=arg[0], annotation=ast.Name(id=arg[1].__name__)) for arg in init_args],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[],
        ),
        body=[
            ast.Assign(
                targets=[ast.Attribute(value=ast.Name(id="self", ctx=ast.Load()), attr=arg[0], ctx=ast.Store())],
                value=ast.Name(id=arg[0], ctx=ast.Load()),
            )
            for arg in init_args
        ],
        decorator_list=[],
    )
