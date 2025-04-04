from __future__ import annotations

import ast

from schemas.apis.api_client_generator._private.common.converters import snake_to_camel
from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import (
    BaseApiClass,
    EndpointsDefinition,
    EndpointsFactory,
    Importable,
)
from schemas.apis.api_client_generator._private.create_init_method import create_init_method


def create_api_client(  # NOQA: PLR0913
    api_name: str,
    endpoints: EndpointsDefinition,
    endpoint_factory: EndpointsFactory,
    base_class: BaseApiClass | str,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    init_args: tuple[tuple[str, Importable]] | None = None,
) -> ast.ClassDef:
    """
    Creates a client class for the given API name and endpoints.

    Args:
        api_name (str): The name of the API. Will be used as class name (converted to the CamelCase).
        endpoints (EndpointsDefinition): The endpoints definition for the API.
        endpoint_factory(EndpointsFactory): The factory function to create endpoints.
        base_class(BaseApiClass | str): The base class for the API client.
        endpoint_decorator(str): The name of the endpoint decorator to be used.
        init_args(tuple[tuple[str, Importable] | None): The arguments for the __init__ method of the API client class.

    Notes:
        - The `base_class` must contain an `endpoint` class method/variable.
        - `__init__` method will be created if `init_args` is provided.
    """
    methods = []

    for endpoint_name, endpoint_parameters in endpoints.items():
        params = endpoint_parameters.get("params", None)
        result = endpoint_parameters.get("result", None)
        description = endpoint_parameters.get("description", None)
        response_array = endpoint_parameters.get("response_array", False)

        methods.append(
            endpoint_factory(
                endpoint_name, params, result, endpoint_decorator, description, response_array=response_array
            )
        )

    base_class_name = base_class if isinstance(base_class, str) else base_class.__name__

    endpoint_decorator_assign = ast.Assign(  # Assign endpoint decorator as class variable
        targets=[ast.Name(id=endpoint_decorator, ctx=ast.Store())],
        value=ast.Attribute(
            value=ast.Name(id=base_class_name, ctx=ast.Load()),
            attr=endpoint_decorator,
            ctx=ast.Load(),
        ),
    )

    body = [endpoint_decorator_assign]

    if init_args:
        body.append(create_init_method(init_args))  # type: ignore[arg-type]

    body.extend(methods)  # type: ignore[arg-type]

    return ast.ClassDef(
        name=snake_to_camel(api_name),
        bases=[ast.Name(id=base_class_name, ctx=ast.Load())],
        keywords=[],
        body=body,  # type: ignore[arg-type]
        decorator_list=[],
        type_params=[],
    )
