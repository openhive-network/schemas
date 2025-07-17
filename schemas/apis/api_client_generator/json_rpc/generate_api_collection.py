from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from schemas.apis.api_client_generator._private.check_whether_was_ran_as_script import check_whether_was_ran_as_script
from schemas.apis.api_client_generator._private.client_class_factory import create_json_rpc_api_client
from schemas.apis.api_client_generator._private.common.defaults import (
    DEFAULT_API_COLLECTION_NAME,
    DEFAULT_ENDPOINT_DECORATOR_NAME,
)
from schemas.apis.api_client_generator._private.common.models_aliased import ApiDescription, BaseApiClass, Importable
from schemas.apis.api_client_generator._private.export_client_module_to_file import export_module_to_file
from schemas.apis.api_client_generator._private.json_rpc_tools.create_collection_module import create_collection_module

if TYPE_CHECKING:
    from pathlib import Path


def generate_api_collection(  # NOQA: PLR0913
    api_descriptions: ApiDescription,
    base_class: type[BaseApiClass] | str,
    base_class_source: str | None = None,
    path: Path | None = None,
    collection_name: str = DEFAULT_API_COLLECTION_NAME,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
    *,
    asynchronous: bool = True,
) -> None:
    """
    Generate an API client collection based on the provided API names, definition, and type and save it to a file.

    Args:
        api_descriptions: Description of the APIs.
        base_class: The base class for the API client.
        base_class_source: The source of the base class. If None, a default source will be used.
        path: The path where the generated client should be saved. If None, a default path will be used.
        collection_name: Name of the collection. Will be used as the class name for the collection.
        endpoint_decorator: Name of the decorator to be used for the endpoint.
        additional_items_to_import: Additional items to import in the module.
        asynchronous: If True, the endpoints will be created as asynchronous methods.

    Notes:
        Your script must be run with the `-m` flag to ensure that the module is executed as a script.

    Raises:
        InvalidApiNameError: If the API name is invalid.
        RunningScriptWithoutAppropriateFlagError: If the script is run without the appropriate (-m) flag.
    """
    check_whether_was_ran_as_script()

    collection_module = create_collection_module(
        api_descriptions,
        create_json_rpc_api_client,
        base_class,
        base_class_source,
        collection_name,
        endpoint_decorator,
        additional_items_to_import,
        asynchronous=asynchronous,
    )

    export_module_to_file(collection_module, file_path=path)
