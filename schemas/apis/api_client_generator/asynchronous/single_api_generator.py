from __future__ import annotations

from pathlib import Path
from typing import Sequence

from schemas.apis.api_client_generator._private.client_class_factory import create_json_rpc_async_api_client
from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.models_aliased import ApiDefinition, Importable
from schemas.apis.api_client_generator._private.create_single_client_module import create_single_client_module
from schemas.apis.api_client_generator._private.export_client_module_to_file import export_module_to_file


def generate_api_client(  # NOQA: PLR0913
    api_definition: ApiDefinition,
    base_class: Importable | str,
    base_class_source: str | None = None,
    path: Path | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
) -> None:
    """
    Generate an API client class based on the provided API name, definition, and type and save it to a file.

    Args:
        api_definition(ApiDefinition): The definition of the API.
        base_class(Importable | str): The base class for the API client.
        base_class_source(str | None): The source of the base class. If None, a default source will be used.
        path(Path | None): The path where the generated client should be saved. If None, a default path will be used.
        endpoint_decorator(str): Name of the decorator to be used for the endpoint.
        additional_items_to_import(Sequence[Importable] | None): Additional items to import in the module.

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
                "type": "json_rpc",
                "params": MyApiParameters,
                "result": MyApiResult,
            }
        }

        generate_api_client(my_api_definition, AbstractAsyncApi)
    """

    api_class_factory_method = create_json_rpc_async_api_client

    client_module = create_single_client_module(
        api_definition,
        api_class_factory_method,
        base_class,
        base_class_source,
        endpoint_decorator,
        additional_items_to_import,
    )

    file_path = Path(f"{next(iter(api_definition.keys())).lower()}_client.py") if path is None else path
    export_module_to_file(client_module, file_path)
