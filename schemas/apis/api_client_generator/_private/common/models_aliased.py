from __future__ import annotations

import ast
from typing import Any, Callable, Protocol, TypeAlias, cast

EndpointsDefinition: TypeAlias = dict[str, dict[str, type]]
ApiDefinition: TypeAlias = dict[str, EndpointsDefinition]
ClientClassFactory: TypeAlias = Callable[..., ast.ClassDef]
EndpointsFactory: TypeAlias = Callable[..., ast.FunctionDef | ast.AsyncFunctionDef]
Dataclass = object


class Importable(Protocol):
    """A protocol that defines the structure of an importable object."""

    __module__: str
    __name__: str


class BaseApiClass(Importable):
    """A protocol that defines the structure of a base class."""

    endpoint: EndpointsFactory


def ensure_is_importable(potential_importable: Any) -> Importable:
    """Ensure that the object is importable."""
    assert hasattr(potential_importable, "__module__") and hasattr(
        potential_importable, "__name__"
    ), f"Object {potential_importable} is not importable. It must have __module__ and __name__ attributes."
    return cast(Importable, potential_importable)
