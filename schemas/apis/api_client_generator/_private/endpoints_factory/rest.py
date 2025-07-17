from __future__ import annotations

import ast
from typing import TYPE_CHECKING

from schemas.apis.api_client_generator._private.common.converters import hyphen_to_snake
from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.get_type_from_ref import get_type_from_ref_in_camel
from schemas.apis.api_client_generator._private.common.models_aliased import Importable
from schemas.apis.api_client_generator._private.common.openapi_to_python_type import convert_openapi_type_to_python_type
from schemas.apis.api_client_generator._private.description_tools import get_value_from_swagger_part_recursively
from schemas.apis.api_client_generator._private.endpoints_factory.common import (
    create_endpoint as create_endpoint_common,
)
from schemas.apis.api_client_generator._private.rest_api_tools.models_aliased import (
    PathParam,
    QueryParam,
    RestApiMethodType,
)

if TYPE_CHECKING:
    from schemas.apis.api_client_generator._private.rest_api_tools.rest_method_model import RestApiMethod


def create_endpoint(  # NOQA: PLR0913
    name: str,
    url_path: str,
    method: RestApiMethod | None = None,
    result: Importable | str | None = None,
    method_type: RestApiMethodType = "get",
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    description: str | None = None,
    *,
    response_array: bool = False,
    asynchronous: bool = True,
) -> ast.AsyncFunctionDef | ast.FunctionDef:
    """
    Create an endpoint function definition.

    Args:
        name: The name of the endpoint function.
        url_path: The URL path of the endpoint.
        method: The REST API method.
        result: The expected result type of the endpoint. If str, will be used as a type hint exactly as it was passed.
        method_type: The type of the REST API method (e.g., "get", "post").
        endpoint_decorator: The decorator to use for the endpoint. Note that method_type will be appended to it.
        description: A description of the endpoint.
        response_array: Whether the response is an array.
        asynchronous: Whether the endpoint function should be asynchronous.

    Returns:
        An AST representing the endpoint function definition.
    """

    endpoint_decorator += f""".{method_type}("{url_path}")"""
    return create_endpoint_common(
        name,
        get_endpoint_args(method),
        endpoint_decorator,
        result,
        description,
        response_array=response_array,
        asynchronous=asynchronous,
    )


def get_endpoint_args(params: RestApiMethod | None) -> ast.arguments:
    arguments = ast.arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[],
    )

    if params is None or params.parameters is None:
        return arguments

    args: list[PathParam] = []
    kwonlyargs: list[QueryParam] = []
    defaults: list[ast.expr | None] = []

    for param in params.parameters:
        assert isinstance(param, dict), "Parameter of the REST API endpoint must be a dictionary."

        schema = param["schema"]
        assert isinstance(schema, dict), "Parameter schema must be a dictionary."
        default = schema.get("default", None)

        if (
            default is not None or param["in"] == "query"
        ):  # query param must have a default value to properly generate as the kwonly argument
            defaults.append(ast.Constant(value=default))

        annotation = ast.Name(
            id=convert_openapi_type_to_python_type(
                get_value_from_swagger_part_recursively(
                    param,
                    (
                        "schema",
                        "type",
                    ),
                )
            ).__name__
            if param["schema"].get("type")  # type: ignore[union-attr]
            else get_type_from_ref_in_camel(
                get_value_from_swagger_part_recursively(
                    param,
                    (
                        "schema",
                        "$ref",
                    ),
                )
            )
        )

        if not param.get("required"):
            annotation.id += " | None"

        argument_name = param.get("name")
        assert isinstance(argument_name, str), "Parameter name must be a string."
        argument = ast.arg(arg=hyphen_to_snake(argument_name), annotation=annotation)

        if param["in"] == "path":
            args.append(argument)
        else:
            kwonlyargs.append(argument)

        arguments.kwonlyargs = kwonlyargs
        arguments.args = args
        arguments.kw_defaults = defaults
    return arguments
