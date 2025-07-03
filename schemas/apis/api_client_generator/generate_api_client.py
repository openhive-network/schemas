from __future__ import annotations

from pathlib import Path
from typing import Sequence

from schemas.apis.api_client_generator._private.api_name_tools import get_api_name_from_definition
from schemas.apis.api_client_generator._private.check_whether_was_ran_as_script import check_whether_was_ran_as_script
from schemas.apis.api_client_generator._private.client_class_factory import create_json_rpc_api_client
from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import ApiDefinition, BaseApiClass, Importable
from schemas.apis.api_client_generator._private.create_single_client_module import create_single_client_module
from schemas.apis.api_client_generator._private.export_client_module_to_file import export_module_to_file
from schemas.apis.api_client_generator.exceptions import InvalidApiDefinitionsAmountError


def generate_api_client(  # NOQA: PLR0913
    api_definition: ApiDefinition,
    base_class: type[BaseApiClass] | str,
    base_class_source: str | None = None,
    path: Path | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
    *,
    asynchronous: bool = True,
) -> None:
    """
    Generate an API client class based on the provided API name, definition, and type and save it to a file.

    Args:
        api_definition: The definition of the API.
        base_class: The base class for the API client.
        base_class_source: The source of the base class. If None, a default source will be used.
        path: The path where the generated client should be saved. If None, a default path will be used.
        endpoint_decorator: Name of the decorator to be used for the endpoint.
        additional_items_to_import: Additional items to import in the module.
        asynchronous: If True, the endpoints will be created as asynchronous methods.

    Notes:
        Your script must be run with the `-m` flag to ensure that the module is executed as a script.

    Raises:
        MoreThanOneApiPassedToSingleGeneratorError: If more than one or none API definition is provided. If you want to generate a client for multiple APIs,
        use `generate_api_collection` instead or pass your api definitions one by one.
        InvalidApiNameError: If the API name is invalid.
        RunningScriptWithoutAppropriateFlagError: If the script is run without the appropriate (-m) flag.


    Example:
        from beekeepy import AbstractAsyncApi


        @dataclass
        class MyApiParameters:
            account: str


        @dataclass
        class MyApiResult:
            data: str


        my_api_definition = {
            "my_api": {
                "params": MyApiParameters,
                "result": MyApiResult,
            }
        }

        generate_dapi_client(my_api_definition, AbstractAsyncApi)
    """
    check_whether_was_ran_as_script()

    if len(api_definition.keys()) != 1:
        raise InvalidApiDefinitionsAmountError

    client_module = create_single_client_module(
        api_definition,
        create_json_rpc_api_client,
        base_class,
        base_class_source,
        endpoint_decorator,
        additional_items_to_import,
        asynchronous=asynchronous,
    )

    api_name = get_api_name_from_definition(api_definition)  # Already validated in the `create_single_client_module`

    file_path = Path(f"{api_name}_client.py") if path is None else path
    export_module_to_file(client_module, file_path=file_path)
