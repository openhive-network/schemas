from __future__ import annotations

import ast
from typing import Sequence, get_type_hints

from msgspec import Struct

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_IMPORT_LEVEL
from schemas.apis.api_client_generator._private.common.models_aliased import Importable
from schemas.apis.api_client_generator.exceptions import (
    ClassPassedByStrWithoutSourceError,
    EndpointParamsIsNotMsgspecStructError,
)


def is_struct(obj: object) -> bool:
    """
    Check if the object is a msgspec struct.

    Args:
        obj: The object to check.

    Returns:
        bool: True if the object is a msgspec struct, False otherwise.
    """
    return type(obj) is type(Struct)


def import_class(
    class_: Importable | str,
    class_source: str | None = None,
) -> ast.ImportFrom | None:
    """
    Import a class from its module.

    Args:
        class_: The class to import.
        class_source: The source of the class. If None, uses the __module__.

    Raises:
        AttributeError: If the module cannot be resolved.

    Returns:
        ast.ImportFrom | None: The AST representation of the import statement.
                               Returns None if the class is from the builtins module.

    Notes:
        Please note that the `class_` argument can be a string, but in this case class_source should be passed also.
    """
    if not isinstance(class_, str) and class_.__module__ == "builtins":
        return None

    if not isinstance(class_, str):
        class_source = class_.__module__

    if class_source is None:
        raise ClassPassedByStrWithoutSourceError

    return ast.ImportFrom(
        class_source,
        [ast.alias(name=class_.__name__ if not isinstance(class_, str) else class_)],
        DEFAULT_IMPORT_LEVEL,
    )


def import_classes(
    classes: Sequence[Importable] | None, already_imported: list[str], sources: Sequence[str] | None = None
) -> list[ast.ImportFrom]:
    """
    Import class from the given sequence of classes.

    Args:
        classes: A sequence of classes to import.
        already_imported: A list of already imported classes.
        sources: A sequence of sources for the classes. If None, uses the __module__.

    Raises:
        AssertionError: If the length of classes and sources do not match.

    Notes:
        - If classes is None or empty, an empty list is returned.
        - If sources is provided, it must match the length of classes.
    """

    classes_imports: list[ast.ImportFrom] = []

    if not classes:
        return classes_imports

    def add_import(class_: Importable, source: str | None = None) -> None:
        if _should_be_imported(class_, already_imported):
            already_imported.append(class_.__name__)
            import_stmt = import_class(class_, source)
            if import_stmt:
                classes_imports.append(import_stmt)

    if sources is None:
        for class_ in classes:
            add_import(class_)
    else:
        assert len(classes) == len(sources), "Length of classes and sources must match"
        for class_, source in zip(classes, sources):
            add_import(class_, source)

    return classes_imports


def import_params_types(params: Struct | None, already_imported: list[str]) -> list[ast.ImportFrom]:
    """
    Import parameters types from the given dataclass of parameters.

    Args:
        params: A msgspec struct with parameters to import.
        already_imported: A list of already imported types.

    Notes:
        - If params is None or empty, an empty list is returned.
        - If a parameter is from the builtins or __main__ module, it is skipped.

    Raises:
        EndpointParamsIsNotMsgspecStructError: If params is not a msgspec struct.
    """
    if params is not None and not is_struct(params):
        raise EndpointParamsIsNotMsgspecStructError

    needed_imports: list[ast.ImportFrom] = []

    def add_import(class_: Importable) -> None:
        if _should_be_imported(class_, already_imported):
            already_imported.append(class_.__name__)
            import_stmt = import_class(class_)
            if import_stmt:
                needed_imports.append(import_stmt)

    if not params:
        return []

    for type_ in get_type_hints(params).values():
        add_import(type_)

    return needed_imports


def _should_be_imported(class_: Importable, already_imported: list[str]) -> bool:
    """
    Check if a class should be imported.

    Args:
        class_: The class to check.
        already_imported: A list of already imported classes.

    Returns:
        bool: True if the class should be imported, False otherwise.
    """
    return class_.__module__ != "builtins" and class_.__name__ not in already_imported
