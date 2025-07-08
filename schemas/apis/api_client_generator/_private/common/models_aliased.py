from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol, TypeAlias, cast

if TYPE_CHECKING:
    import ast
    from struct import Struct

AnyJson: TypeAlias = dict[str, "AnyJson"] | list["AnyJson"] | tuple["AnyJson", ...] | str | int | float | bool | None
SwaggerReadyForExtraction: TypeAlias = dict[str, AnyJson]

EndpointDescriptionBeforeProcessing: TypeAlias = dict[str, str | bool]
"""
A description of an endpoint, params, result, description and response_array boolean parameter.
This is used before processing the endpoint description. At this stage, the params and result are still strings.
"""
ApiDescriptionBeforeProcessing: TypeAlias = dict[str, dict[str, EndpointDescriptionBeforeProcessing]]
EndpointsDescription: TypeAlias = dict[str, dict[str, Any]]
ApiDescription: TypeAlias = dict[str, EndpointsDescription]


class Dataclass(Protocol):
    """A protocol that is used to ensure some object is dataclass."""

    __dataclass_fields__: dict[str, Any]


class Importable(Protocol):
    """A protocol that defines the structure of an importable object."""

    __module__: str
    __name__: str


class EndpointsFactory(Protocol):
    def __call__(  # NOQA: PLR0913
        self,
        name: str,
        params: Struct | None,
        result: Importable | None,
        endpoint_decorator: str,
        description: str | None,
        *,
        response_array: bool,
        asynchronous: bool,
    ) -> ast.AsyncFunctionDef | ast.FunctionDef: ...


class BaseApiClass(Protocol):
    """A protocol that defines the structure of a base class."""

    __module__: str
    __name__: str

    endpoint: EndpointsFactory


def ensure_is_importable(potential_importable: Any) -> Importable:
    """Ensure that the object is importable."""
    assert hasattr(potential_importable, "__module__") and hasattr(
        potential_importable, "__name__"
    ), f"Object {potential_importable} is not importable. It must have __module__ and __name__ attributes."
    return cast(Importable, potential_importable)


class ClientClassFactory(Protocol):
    def __call__(
        self,
        api_name: str,
        endpoints: EndpointsDescription,
        base_class: type[BaseApiClass] | str,
        endpoint_decorator: str,
        *,
        asynchronous: bool,
    ) -> ast.ClassDef: ...
