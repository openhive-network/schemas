from __future__ import annotations

from typing import TYPE_CHECKING, Sequence

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_ENDPOINT_JSON_RPC_DECORATOR_NAME
from schemas.apis.api_client_generator._private.common.generated_class import GeneratedClass
from schemas.apis.api_client_generator._private.common.models_aliased import (
    BaseApiClass,
    ClientClassFactory,
    EndpointsDescription,
    Importable,
    ensure_is_importable,
)
from schemas.apis.api_client_generator._private.resolve_needed_imports import (
    import_class,
    import_classes,
    import_params_types,
    is_struct,
)
from schemas.apis.api_client_generator.exceptions import EndpointParamsIsNotMsgspecStructError

if TYPE_CHECKING:
    import ast


def create_client_and_imports(  # NOQA: PLR0913
    api_name: str,
    client_class_factory: ClientClassFactory,
    endpoints: EndpointsDescription,
    base_class: type[BaseApiClass] | str,
    base_class_source: str | None = None,
    endpoint_decorator: str = DEFAULT_ENDPOINT_JSON_RPC_DECORATOR_NAME,
    additional_items_to_import: Sequence[Importable] | None = None,
    already_imported: list[str] | None = None,
    *,
    asynchronous: bool = True,
) -> GeneratedClass:
    """
    Create a client class and resolve the needed imports.

    Args:
        api_name: The name of the API.
        client_class_factory: The factory function to create the client class.
        endpoints: The endpoints description for the API.
        base_class: The base class for the API client.
        base_class_source: The source of the base class.
        endpoint_decorator: The name of the endpoint decorator to be used.
        additional_items_to_import: Additional items to import.
        already_imported: A list of already imported items.
        asynchronous: If True, the endpoints will be created as asynchronous methods.

    Raises:
        EndpointParamsIsNotDataclassError: If the endpoint parameters are not a dataclass.
    """

    needed_imports: list[ast.ImportFrom] = []
    if already_imported is None:
        already_imported = []

    needed_results = [ensure_is_importable(params["result"]) for params in endpoints.values() if params.get("result")]
    needed_results_import = import_classes(needed_results, already_imported)

    needed_params_import = []

    for params in endpoints.values():
        if params.get("params") is not None:
            extracted_params = params.get("params")

            if extracted_params is not None and not is_struct(extracted_params):
                raise EndpointParamsIsNotMsgspecStructError

            needed_params_import.extend(import_params_types(extracted_params, already_imported))

    additional_imports = import_classes(additional_items_to_import or [], already_imported)

    needed_imports.extend(additional_imports + needed_results_import + needed_params_import)

    base_class_import = import_class(base_class, base_class_source)

    base_class_name = base_class if isinstance(base_class, str) else base_class.__name__

    if base_class_import and base_class_name not in already_imported:
        already_imported.append(base_class_name)
        needed_imports.append(base_class_import)

    return GeneratedClass(
        client_class_factory(api_name, endpoints, base_class, endpoint_decorator, asynchronous=asynchronous),
        needed_imports,
    )
