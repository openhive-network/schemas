from __future__ import annotations

import ast
import inspect
from dataclasses import is_dataclass
from typing import Sequence, get_type_hints

from schemas.apis.api_client_generator._private.common.defaults import DEFAULT_IMPORT_LEVEL
from schemas.apis.api_client_generator._private.common.models_aliased import Dataclass, Importable


def import_class(
    class_: Importable | str,
    class_source: str | None = None,
) -> ast.ImportFrom | None:
    """
    Import a class from its module.

    Args:
        class_(Importable | str): The class to import.
        class_source(str | None): The source of the class. If None, uses the __module__.

    Raises:
        AttributeError: If the module cannot be resolved.

    Returns:
        ast.ImportFrom | None: The AST representation of the import statement.
                               Returns None if the class is from the builtins or __main__ module.
    """
    if not isinstance(class_, str) and class_.__module__ == "builtins":
        return None

    class_source = class_source or class_.__module__

    if class_source == "__main__":
        class_source = inspect.getmodule(class_)  # type: ignore[assignment]
        if class_source is None:
            raise AttributeError("Cannot resolve module for class")
        class_source = class_source.__spec__.name  # type: ignore[attr-defined]

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
        classes(Sequence[Importable] | None): A sequence of classes to import.
        already_imported(list[str]): A list of already imported classes.
        sources(Sequence[str] | None): A sequence of sources for the classes. If None, uses the __module__.

    Raises:
        AssertionError: If the length of classes and sources do not match.

    Notes:
        - If classes is None or empty, an empty list is returned.
        - If sources is provided, it must match the length of classes.
    """

    if not classes:
        return []

    classes_imports = []

    if sources is not None:
        assert len(classes) == len(sources), "Length of classes and sources must match"
        for class_, class_source in zip(classes, sources):
            if class_.__name__ not in already_imported and class_.__module__ != "builtins":
                already_imported.append(class_.__name__)
                classes_imports.append(import_class(class_, class_source))
        return classes_imports  # type: ignore[return-value] # import class returns None if type_ is builtins

    for class_ in classes:
        if class_ is not None and class_.__module__ != "builtins" and class_.__name__ not in already_imported:
            already_imported.append(class_.__name__)
            classes_imports.append(import_class(class_))

    return classes_imports  # type: ignore[return-value] # import class returns None if type_ is builtins


def import_params_types(params: Dataclass | None, already_imported: list[str]) -> list[ast.ImportFrom]:
    """
    Import parameters types from the given dataclass of parameters.

    Args:
        params(Dataclass | None): A dataclass with parameters to import.
        already_imported(list[str]): A list of already imported types.

    Notes:
        - If params is None or empty, an empty list is returned.
        - If a parameter is from the builtins or __main__ module, it is skipped.

    Raises:
        ValueError: If params is not a dataclass.
    """

    if not params:
        return []

    if not is_dataclass(params):
        raise ValueError("Params must be a dataclass")

    needed_imports = []

    for type_ in get_type_hints(params).values():
        if type_.__module__ != "builtins" and type_.__name__ not in already_imported:
            already_imported.append(type_.__name__)
            needed_imports.append(import_class(type_))

    return needed_imports  # type: ignore[return-value] # import class returns None if type_ is builtins
