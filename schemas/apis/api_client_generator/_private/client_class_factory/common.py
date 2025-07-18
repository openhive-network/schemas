from __future__ import annotations

import ast

from schemas.apis.api_client_generator._private.common.converters import snake_to_camel
from schemas.apis.api_client_generator._private.common.models_aliased import (
    BaseApiClass,
    EndpointsDescription,
    EndpointsFactory,
)
from schemas.apis.api_client_generator._private.resolve_needed_imports import is_struct
from schemas.apis.api_client_generator.exceptions import EndpointParamsIsNotMsgspecStructError


def create_api_client(  # NOQA: PLR0913
    api_name: str,
    endpoints: EndpointsDescription,
    endpoint_factory: EndpointsFactory,
    base_class: type[BaseApiClass] | str,
    endpoint_decorator: str,
    *,
    asynchronous: bool = True,
) -> ast.ClassDef:
    """
    Creates a client class for the given API name and endpoints.

    Args:
        api_name: The name of the API. Will be used as class name (converted to the CamelCase).
        endpoints: The endpoints description for the API.
        endpoint_factory: The factory function to create endpoints.
        base_class: The base class for the API client.
        endpoint_decorator: The name of the endpoint decorator to be used.
        asynchronous: If True, the endpoints will be created as asynchronous methods.

    Raises:
        EndpointParamsIsNotDataclassError: If the endpoint parameters are not a dataclass.
    """
    methods = []

    for endpoint_name, endpoint_parameters in endpoints.items():
        params = endpoint_parameters.get("params", None)

        if params is not None and not is_struct(params):
            raise EndpointParamsIsNotMsgspecStructError(endpoint_name)

        result = endpoint_parameters.get("result", None)
        description = endpoint_parameters.get("description", None)
        response_array = endpoint_parameters.get("response_array", False)

        methods.append(
            endpoint_factory(
                endpoint_name,
                params,
                result,
                endpoint_decorator,
                str(description) if description else None,
                response_array=response_array,
                asynchronous=asynchronous,
            )
        )

    base_class_name = base_class if isinstance(base_class, str) else base_class.__name__

    endpoint_decorator_assign = ast.Assign(  # Assign endpoint decorator as class variable
        targets=[ast.Name(id=endpoint_decorator)],
        value=ast.Attribute(
            value=ast.Name(id=base_class_name),
            attr=endpoint_decorator,
        ),
    )

    body: list[ast.stmt] = [endpoint_decorator_assign, *methods]

    return ast.ClassDef(
        name=snake_to_camel(api_name),
        bases=[ast.Name(id=base_class_name)],
        keywords=[],
        body=body,
        decorator_list=[],
        type_params=[],
    )
