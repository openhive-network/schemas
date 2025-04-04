from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from schemas.apis.api_client_generator._private.client_class_factory import (
    create_json_rpc_api_client,
)
from schemas.apis.api_client_generator._private.common.defaults import (
    DEFAULT_API_COLLECTION_NAME,
    DEFAULT_ENDPOINT_DECORATOR_NAME,
)
from schemas.apis.api_client_generator._private.common.models_aliased import ApiDefinition, Importable
from schemas.apis.api_client_generator._private.create_collection_module import create_collection_module
from schemas.apis.api_client_generator._private.export_client_module_to_file import export_module_to_file

if TYPE_CHECKING:
    from pathlib import Path


def generate_api_collection(  # NOQA: PLR0913
    api_definitions: ApiDefinition,
    base_class: Importable | str,
    base_class_source: str | None = None,
    path: Path | None = None,
    collection_name: str = DEFAULT_API_COLLECTION_NAME,
    endpoint_decorator: str = DEFAULT_ENDPOINT_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
) -> None:
    """
    Generate an API client collection based on the provided API names, definition, and type and save it to a file.

    Args:
        api_definitions(ApiDefinition): Definitions of the api.
        base_class(Importable | str): The base class for the API client.
        base_class_source(str | None): The source of the base class. If None, a default source will be used.
        path(Path | None): The path where the generated client should be saved. If None, a default path will be used.
        collection_name(str): Name of the collection - will be used as class name.
        endpoint_decorator(str): Name of the decorator to be used for the endpoint.
        additional_items_to_import(Sequence[Importable] | None): Additional items to import in the module.
    """
    api_class_factory_method = create_json_rpc_api_client

    collection_module = create_collection_module(
        api_definitions,
        api_class_factory_method,
        base_class,
        base_class_source,
        collection_name,
        endpoint_decorator,
        additional_items_to_import,
    )

    export_module_to_file(collection_module, path)
