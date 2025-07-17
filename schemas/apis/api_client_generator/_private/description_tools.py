from __future__ import annotations

import ast
from typing import Any, TypeAlias

from schemas.apis.api_client_generator._private.common.models_aliased import (
    ApiDescription,
    SwaggerReadyForExtraction,
)

AliasToAssign: TypeAlias = tuple[str, type]


def get_value_from_swagger_part_recursively(
    swagger_part: SwaggerReadyForExtraction,
    keys: tuple[str, ...],
) -> Any:
    """Get a value from the swagger part by a path of keys."""
    assert isinstance(swagger_part, dict), "This swagger part must be a dictionary."

    key = keys[0]
    value = swagger_part[key]

    if len(keys) == 1:  # Last key in the path - return searched value
        return value

    assert isinstance(value, dict), "This swagger part must be a dictionary."

    return get_value_from_swagger_part_recursively(value, keys[1:])


def get_ref_from_schema(response: SwaggerReadyForExtraction) -> str:
    """
    Resolve the reference from the schema.

    Example:
        some_responses = {
            "responses": {
                "200": {
                    "description": "Some operation",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/some_response"
                            }
                        }
                    }
                }
            }
        }

        get_ref_from_schema(some_responses["responses"]["200"])
        >>> "#/components/schemas/some_response"
    """
    ref = get_value_from_swagger_part_recursively(
        response,
        (
            "content",
            "application/json",
            "schema",
            "$ref",
        ),
    )
    assert isinstance(ref, str), "Reference must be a string."

    return ref


def get_last_part_of_ref(ref: str) -> str:
    """Return the last part of the #ref string."""

    return ref.split("/")[-1]


def get_description_for_endpoint(endpoint_properties: SwaggerReadyForExtraction) -> str:
    """
    Resolve the description from the endpoint properties.

    Example:
        example = {
            "some_api.some_endpoint": {
                "post": {
                    "tags": ["some_api"],
                    "summary": "Just example.",
                    "description": "Some description.",
                }
            }
        }

        get_description_for_endpoint(example["some_api.some_endpoint"])
        >>> "Some description."
    """
    post_properties = endpoint_properties["post"]

    assert isinstance(post_properties, dict), "Post properties must be a dictionary."

    description = post_properties.get("description", "")
    assert isinstance(description, str), "Description must of the endpoint be a string."

    return description


def get_result_name_for_endpoint(endpoint_properties: SwaggerReadyForExtraction) -> str:
    """
    Resolve the result from the endpoint properties.

    Example:
        example = {
            "some_api.some_endpoint": {
                "post": {
                    "responses": {
                        "200": {
                            "description": "Successful operation",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/components/schemas/some_endpoint_response"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        get_result_name_for_endpoint(example["some_api.some_endpoint"])
        >>> "some_endpoint_response"
    """
    response = get_value_from_swagger_part_recursively(
        endpoint_properties,
        (
            "post",
            "responses",
            "200",
        ),
    )
    ref = get_ref_from_schema(response)
    return get_last_part_of_ref(ref)


def get_params_name_for_endpoint(endpoint_properties: SwaggerReadyForExtraction) -> str | None:
    """
    Resolve the params from the endpoint properties.

    Example:
        example = {
            "some_api.some_endpoint": {
                "post": {
                   "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/some_ednpoint"
                                }
                            }
                        },
                      "required": true
                    },
                }
            }
        }
        get_params_name_for_endpoint(example["some_api.some_endpoint"])
        >>> "some_ednpoint"
    """
    post_properties = endpoint_properties["post"]

    assert isinstance(post_properties, dict), "Post properties must be a dictionary."

    request_body = post_properties.get("requestBody")
    if request_body is None:
        return None

    assert isinstance(request_body, dict), "Request body must be a dictionary."
    ref = get_ref_from_schema(request_body)

    return get_last_part_of_ref(ref)


def is_result_array(result: str, components: SwaggerReadyForExtraction) -> bool:
    """Check if the response of the endpoint is an array."""

    response_schema = components.get(result)
    assert response_schema is not None, f"Not found response schema for the {result}."

    assert isinstance(response_schema, dict), "Response schema must be a dictionary."
    return response_schema.get("type") == "array"


def create_api_description_module(
    api_description_name: str,
    api_description: ApiDescription,
    additional_aliases: tuple[AliasToAssign] | None = None,
) -> ast.Module:
    assign = ast.Assign(
        targets=[ast.Name(id=api_description_name, ctx=ast.Store())],
        value=ast.Dict(
            keys=[ast.Constant(value=api_name) for api_name in api_description],
            values=[
                ast.Dict(
                    keys=[ast.Constant(value=endpoint) for endpoint in api_description[api_name]],
                    values=[
                        ast.Dict(
                            keys=[ast.Constant(value=param_name) for param_name in params],
                            values=[
                                ast.Name(id=param_value, ctx=ast.Load())
                                if param_name not in ("response_array", "description")
                                else ast.Constant(value=param_value)
                                for param_name, param_value in params.items()
                            ],
                        )
                        for params in api_description[api_name].values()
                    ],
                )
                for api_name in api_description
            ],
        ),
    )

    body: list[ast.stmt] = [assign]

    if additional_aliases:
        for alias in additional_aliases:
            body.insert(
                0,
                ast.Assign(
                    targets=[ast.Name(id=alias[0])],
                    value=ast.Name(id=alias[1].__name__),
                ),
            )

    return ast.Module(body=body, type_ignores=[])


def get_api_name_from_server_property(swagger: SwaggerReadyForExtraction) -> str:
    """
    Get the API name from the server property of the swagger.

    Example:
        swagger = {
            "servers": [
                {
                    "url": "/some-api,
                }
            ]
        }

        get_api_name_from_server_property(swagger)
        >>> "some-api"
    """
    servers = swagger["servers"]
    assert isinstance(servers, list), "Servers must be a list."

    assert len(servers) == 1, "Swagger must have exactly one server."

    server = servers[0]
    assert isinstance(server, dict), "Server must be a dictionary."
    server_url = server["url"]

    assert isinstance(server_url, str), "Server URL must be a string."

    split_server_url = server_url.split("/")
    split_server_url.remove("")  # Remove empty strings from the list

    if len(split_server_url) > 1:
        return "_".join(split_server_url)  # If the URL contains slashes, join them with underscores

    return split_server_url[0]


def get_types_name_from_components(swagger: SwaggerReadyForExtraction) -> str:
    """
    Get the names of the types from the components of the swagger.

    Example:
        swagger = "components": {
            "schemas": {
                "some_types.some_type": {
                    "type": "string",
                    "enum": [
                        "post",
                        "comment",
                        "all"
                    ]
                },
            }
        }

        get_types_name_from_components(components)
        >>> "some_types"
    """
    schemas_in_swagger = get_value_from_swagger_part_recursively(swagger, ("components", "schemas"))

    first_type = next(iter(schemas_in_swagger))
    assert isinstance(first_type, str), "First type in the schemas must be a string."
    return first_type.split(".")[0]
