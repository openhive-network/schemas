from __future__ import annotations

import ast
from typing import Any, TypeAlias

AliasToAssign: TypeAlias = tuple[str, type]
ApiDescription: TypeAlias = dict[str, Any]


def get_ref_from_schema(response: dict[str, Any]) -> str:
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
    """

    return str(response["content"]["application/json"]["schema"]["$ref"])


def get_last_part_of_ref(ref: str) -> str:
    """Return the last part of the #ref string."""

    return ref.split("/")[-1]


def get_description_from_endpoint_properties(endpoint_properties: dict[str, Any]) -> str:
    """
    Resolve the description from the endpoint properties.

    Example:
        example = "some_api.some_endpoint": {
                    "post": {
                    "tags": [
                        "some_api"
                        ],
                    "summary": "Just example.",
                    "description": "Some description.",
                    }
                    }

        get_description_from_endpoint_parameters(example["some_api.some_endpoint"]["post"])
    """

    return endpoint_properties.get("description", "")  # type: ignore[no-any-return]


def get_result_from_endpoint_properties(endpoint_properties: dict[str, Any]) -> str:
    """
    Resolve the result from the endpoint properties.

    Endpoint parameters are the properties of the endpoint, you should pass everything after "post" key.
    """

    response = endpoint_properties["responses"].get("200")

    ref = get_ref_from_schema(response)
    return get_last_part_of_ref(ref)


def get_params_from_endpoint_properties(endpoint_properties: dict[str, Any]) -> str | None:
    """
    Resolve the params from the endpoint properties.

    Endpoint parameters are the properties of the endpoint, you should pass everything after "post" key.
    """
    request_body = endpoint_properties.get("requestBody")

    if not request_body:
        return None

    ref = get_ref_from_schema(request_body)
    return get_last_part_of_ref(ref)


def is_result_array(result: str, components: dict[str, Any]) -> bool:
    """Check if the response of the endpoint is an array."""

    response_schema = components.get(result)
    assert response_schema is not None, f"Not found response schema for the {result}."

    return response_schema.get("type") == "array"  # type: ignore[no-any-return]


def convert_description_to_str(
    api_description_name: str,
    api_description: ApiDescription,
    additional_aliases: tuple[AliasToAssign] | None = None,
) -> str:
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

    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module)

    return ast.unparse(module)
