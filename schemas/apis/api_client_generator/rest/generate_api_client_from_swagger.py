from __future__ import annotations

import ast
import json
from pathlib import Path

from schemas.apis.api_client_generator._private.check_whether_was_ran_as_script import check_whether_was_ran_as_script
from schemas.apis.api_client_generator._private.common.converters import hyphen_to_snake
from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_REST_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import BaseApiClass
from schemas.apis.api_client_generator._private.description_tools import (
    get_api_name_from_server_property,
    get_types_name_from_components,
)
from schemas.apis.api_client_generator._private.export_client_module_to_file import export_module_to_file
from schemas.apis.api_client_generator._private.rest_api_tools.create_client_and_imports import (
    create_client_and_imports,
)
from schemas.apis.api_client_generator._private.rest_api_tools.create_endpoints_for_all_url_paths import (
    create_endpoints_for_all_url_paths,
)
from schemas.apis.api_client_generator.generate_types_from_swagger import generate_types_from_swagger


def generate_api_client_from_swagger(  # NOQA: PLR0913
    openapi_api_definition: str | Path,
    output_package: str | Path,
    base_class: type[BaseApiClass] | str,
    base_class_source: str | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_REST_DECORATOR_NAME,
    *,
    asynchronous: bool = True,
) -> None:
    """
    Generates a REST API client from an OpenAPI definition file.

    Args:
        openapi_api_definition: The OpenAPI JSON definition file path.
        output_package: The output package where the generated client will be saved. It should be a directory path.
        base_class: The base class for the API client.
        base_class_source: Optional source file for the base class, if it is not in the same module as the generated client.
        endpoint_decorator: The name of the decorator to be used for the endpoints.
        asynchronous: Whether to create asynchronous endpoints.

    Raises:
        FileNotFoundError: If the OpenAPI definition file does not exist.
        RunningScriptWithoutAppropriateFlagError: If the script is run without the appropriate (-m) flag.
    """
    check_whether_was_ran_as_script()

    openapi_file = openapi_api_definition if isinstance(openapi_api_definition, Path) else Path(openapi_api_definition)
    output_package = output_package if isinstance(output_package, Path) else Path(output_package)

    generate_types_from_swagger(openapi_api_definition, output_package)

    openapi = json.loads(openapi_file.read_text())

    server_url = get_api_name_from_server_property(openapi)
    api_name = hyphen_to_snake(server_url)

    types_module_name = get_types_name_from_components(openapi)
    module_path = output_package / f"{types_module_name}.py"

    endpoints = create_endpoints_for_all_url_paths(openapi, asynchronous=asynchronous)

    class_and_imports = create_client_and_imports(
        api_name,
        server_url,
        endpoints,
        module_path,
        base_class,
        base_class_source,
        endpoint_decorator,
    )

    client_module = ast.Module(body=[*class_and_imports.imports, class_and_imports.class_def], type_ignores=[])

    output_client_file = output_package / f"{api_name}_client.py"

    export_module_to_file(client_module, mode="w", file_path=output_client_file)
