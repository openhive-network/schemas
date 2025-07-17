from __future__ import annotations

import ast
from typing import Literal, TypeGuard, get_args

PathParam = ast.arg
QueryParam = ast.arg

CreatedEndpoints = list[ast.FunctionDef | ast.AsyncFunctionDef]

RestApiParameterType = Literal[
    "query",
    "path",
]
RestApiMethodType = Literal[
    "get",
    "post",
    "put",
    "patch",
    "delete",
]
RestApiMethods: tuple[RestApiMethodType, ...] = get_args(RestApiMethodType)


def is_valid_rest_api_method_type(value: str) -> TypeGuard[RestApiMethodType]:
    """
    Check if the given value is a valid REST API method type.

    Args:
        value: The value to check.

    Returns:
        True if the value is a valid REST API method type, False otherwise.
    """
    return value in RestApiMethods
