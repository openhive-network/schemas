"""
Simple way to generate a JSON-RPC params-result structure to be used in the client generator.

This script reads the OpenAPI JSON file, generates the API description, and creates a dictionary like that:

api_description = {
    "name_of_api":
        {
        "name_of_endpoint": {

                "params": ParamsClass,
                "result": NameOfEndpointResponse,
                "description": "Description of the endpoint if given",
            },
        },
        "name_of_second_endpoint":
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

import json
from pathlib import Path
from typing import Container

from schemas.apis.api_client_generator._private.common.converters import snake_to_camel
from schemas.apis.api_client_generator._private.common.models_aliased import (
    ApiDescriptionBeforeProcessing,
    EndpointDescriptionBeforeProcessing,
)
from schemas.apis.api_client_generator._private.description_tools import (
    AliasToAssign,
    create_api_description_module,
    get_description_for_endpoint,
    get_params_name_for_endpoint,
    get_result_name_for_endpoint,
    is_result_array,
)
from schemas.apis.api_client_generator._private.export_client_module_to_file import export_module_to_file
from schemas.apis.api_client_generator.generate_types_from_swagger import generate_types_from_swagger


def generate_api_description(
    api_description_name: str,
    openapi_api_definition: str | Path,
    output_file: str | Path,
    additional_aliases: tuple[AliasToAssign] | None = None,
    apis_to_skip: Container[str] | None = None,
) -> None:
    """
    Generate an API description based on the provided OpenAPI definition.

    Args:
        api_description_name: The name of the API description to be generated.
        openapi_api_definition: The OpenAPI JSON definition file path.
        output_file: The file where the generated API description will be saved.
        additional_aliases: Additional aliases to be used in the API description.
        apis_to_skip: APIs to skip during the generation process.

    Raises:
        FileNotFoundError: If the OpenAPI definition file does not exist.
    """
    openapi_api_definition = (
        openapi_api_definition if isinstance(openapi_api_definition, Path) else Path(openapi_api_definition)
    )
    output_file = output_file if isinstance(output_file, Path) else Path(output_file)
    generate_types_from_swagger(openapi_api_definition, output_file)

    api_description: ApiDescriptionBeforeProcessing = {}

    openapi = json.loads(openapi_api_definition.read_text())

    paths = list(openapi["paths"].keys())  # path is construct like name_of_api.name_of_endpoint
    components = openapi["components"]["schemas"]

    for path in paths:
        api_name, endpoint_name = path.split(".")

        if apis_to_skip and api_name in apis_to_skip:
            continue

        if api_name not in api_description:
            api_description[api_name] = {}

        endpoint_properties = openapi["paths"][path]

        params_name = get_params_name_for_endpoint(endpoint_properties)
        result_name = get_result_name_for_endpoint(
            endpoint_properties
        )  # that's the name of the response class, in the snake case

        endpoint_description: EndpointDescriptionBeforeProcessing = {
            "params": snake_to_camel(params_name) if params_name else "None",
            "result": snake_to_camel(result_name),
            "description": get_description_for_endpoint(endpoint_properties),
        }

        if is_result_array(result_name, components):
            endpoint_description["response_array"] = True

            assert isinstance(endpoint_description["result"], str), "Result must be a string at this point."
            endpoint_description["result"] += "Item"  # It will be typed as list[ClasNameResponseItem]

        api_description[api_name][endpoint_name] = endpoint_description

    description_module = create_api_description_module(api_description_name, api_description, additional_aliases)

    export_module_to_file(
        description_module,
        mode="a",
        file_path=output_file,
    )
