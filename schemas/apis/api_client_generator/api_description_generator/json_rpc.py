"""
Simple way to generate a JSON-RPC params-result structure to be used in the client generator.

This script reads the OpenAPI JSON file, generates the API definition, and creates a dictionary like that:

api_definition = {
    "name_of_api":
        {
            "name_of_endpoint": {
                "params": ParamsClass,
                "result": NameOfEndpointResponse,
                "description": "Description of the endpoint if given",
            },
        },
        {
        "name_of_second_endpoint:
            {
                "name_of_endpoint": {
                    "params": ParamsClass,
                    "result": NameOfEndpointResponseItem,
                    "response_array": True,
                    "description": "Description of the endpoint if given",
            },
        },
    }
"""


from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any, TypeAlias

import black
from black.mode import Mode
from datamodel_code_generator import DataModelType, InputFileType, generate

from schemas.apis.api_client_generator._private.common.converters import snake_to_camel

__all__ = ["generate_api_description"]


AliasToAssign: TypeAlias = tuple[str, type]
ApiDescription: TypeAlias = dict[str, Any]


def generate_api_description(
    openapi_api_definition: str | Path,
    output_file: str | Path,
    additional_aliases: tuple[AliasToAssign] | None = None,
) -> None:
    """
    Generate an API description based on the provided OpenAPI definition.

    Args:
        openapi_api_definition(str | Path): The OpenAPI definition file path.
        output_file(Path): The file where the generated API description will be saved.
        additional_aliases(tuple[AliasToAssign] | None): Additional aliases to be used in the API description.

    Raises:
        FileNotFoundError: If the OpenAPI definition file does not exist.
        AssertionError: If the response schema for the endpoint is not found.
    """
    openapi_file = openapi_api_definition if isinstance(openapi_api_definition, Path) else Path(openapi_api_definition)
    output_file = output_file if isinstance(output_file, Path) else Path(output_file)
    api_description: ApiDescription = {}

    if not openapi_file.exists():
        raise FileNotFoundError(f"File {openapi_file} does not exist.")

    generate(  # generation of types available in the API definition
        openapi_file,
        output=output_file,
        output_model_type=DataModelType.DataclassesDataclass,
        input_file_type=InputFileType.OpenAPI,
        use_field_description=True,
    )

    with openapi_file.open() as f:
        as_dict = dict(json.load(f))

        endpoints = list(as_dict["paths"].keys())
        components = as_dict["components"]["schemas"]

    for endpoint in endpoints:
        api_name, endpoint_name = endpoint.split(".")

        if api_name not in api_description:
            api_description[api_name] = {}

        class_name = snake_to_camel(endpoint_name)
        endpoint_description = {
            "params": class_name,
            "result": class_name + "Response",
            "description": as_dict["paths"][endpoint]["post"].get("description", ""),
        }

        if _is_response_array(endpoint_name, components):
            endpoint_description["response_array"] = True
            endpoint_description["result"] += "Item"  # It will be typed as list[ClasNameResponseItem]

        api_description[api_name][endpoint_name] = endpoint_description

    formatted_description = _format_api_description(_create_api_description_as_str(api_description, additional_aliases))

    with output_file.open(mode="a") as f:
        f.write("\n\n")
        f.write(formatted_description)
        f.write("\n")


def _is_response_array(endpoint: str, components: dict[str, Any]) -> bool:
    response_schema = components.get(f"{endpoint}_response")
    assert response_schema is not None, f"Not found response schema for the {endpoint} endpoint."

    return response_schema.get("type") == "array"  # type: ignore[no-any-return]


def _create_api_description_as_str(
    api_description: ApiDescription,
    additional_aliases: tuple[AliasToAssign] | None = None,
) -> str:
    api_name = next(iter(api_description.keys()))
    assign = ast.Assign(  # Assign the API description to a variable
        targets=[ast.Name(id=f"{api_name}_description", ctx=ast.Store())],
        value=ast.Dict(
            keys=[ast.Constant(value=api_name)],
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
            ],
        ),
    )
    body = [assign]

    if additional_aliases:
        for alias in additional_aliases:
            body.insert(
                0,
                ast.Assign(
                    targets=[ast.Name(id=alias[0], ctx=ast.Store())],
                    value=ast.Name(id=alias[1].__name__, ctx=ast.Load()),
                ),
            )

    module = ast.Module(body=body, type_ignores=[])  # type: ignore[arg-type]
    ast.fix_missing_locations(module)

    return ast.unparse(module)


def _format_api_description(api_description: str) -> str:
    return black.format_str(api_description, mode=Mode())
