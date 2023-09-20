from __future__ import annotations

from typing import Any, Literal

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.operation import Operation
from schemas.operations import AnyLegacyEveryOperation

__all__ = [
    "get_hf26_representation",
    "get_legacy_representation",
    "Hf26OperationRepresentation",
    "LegacyOperationRepresentation",
]


class Hf26OperationRepresentation(PreconfiguredBaseModel):
    type: str  # noqa: A003
    value: Operation


class LegacyOperationRepresentation(PreconfiguredBaseModel):
    type: str  # noqa: A003
    value: Operation

    def __getitem__(self, key: str | int) -> str | AnyLegacyEveryOperation | Any:
        if isinstance(key, int):
            match (key):
                case 0:
                    return self.value.get_name()
                case 1:
                    return self.value
                case _:
                    raise ValueError("out of bound")
        return super().__getitem__(key)


__hf26_operation_representations: dict[str, type[Hf26OperationRepresentation]] = {}
__legacy_operation_representations: dict[str, type[LegacyOperationRepresentation]] = {}


def get_hf26_representation(type_name: str) -> type[Hf26OperationRepresentation]:
    return __get_representation_from_type_dict(type_name, __hf26_operation_representations)


def get_legacy_representation(type_name: str) -> type[LegacyOperationRepresentation]:
    return __get_representation_from_type_dict(type_name, __legacy_operation_representations)


def _create_hf26_representation(incoming_type: type[Operation]) -> type[Hf26OperationRepresentation]:
    class Hf26Operation(Hf26OperationRepresentation):
        type: Literal[incoming_type.get_name_with_suffix()]  # type: ignore[valid-type]  # noqa: A003
        value: incoming_type  # type: ignore[valid-type]

    Hf26Operation.update_forward_refs(**locals())
    __hf26_operation_representations[incoming_type.get_name()] = Hf26Operation
    return Hf26Operation


def _create_legacy_representation(incoming_cls: type[Operation]) -> type[LegacyOperationRepresentation]:
    """
    Representation of operation in legacy format
    Response from api has format [name_of_operation, {parameters}], to provide precise validation in root_validator
    it is converted to format below.
    """

    class LegacyOperation(LegacyOperationRepresentation):
        type: Literal[incoming_cls.get_name()]  # type: ignore[valid-type] # noqa: A003
        value: incoming_cls  # type: ignore[valid-type]

    LegacyOperation.update_forward_refs(**locals())
    __legacy_operation_representations[incoming_cls.get_name()] = LegacyOperation
    return LegacyOperation


def __get_representation_from_type_dict(type_name: str, collection: dict[str, type]) -> type:
    assert type_name in collection, f"`{type_name}` not found, available are: {list(collection.keys())}"
    return collection[type_name]
