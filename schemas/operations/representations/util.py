from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from pydantic import create_model

from schemas._case import snake_case_to_pascal_case
from schemas.operation import Operation
from schemas.operations.representations.hf26_representation import HF26Representation
from schemas.operations.representations.legacy_representation import LegacyRepresentation

if TYPE_CHECKING:
    from schemas.operations.representation_types import Hf26OperationRepresentationType
    from schemas.operations.virtual.representation_types import Hf26VirtualOperationRepresentationType
    from schemas.virtual_operation import VirtualOperation

__all__ = [
    "convert_to_representation",
    "get_hf26_operation_representation",
    "get_legacy_operation_representation",
]

__hf26_operation_representations: dict[str, type[HF26Representation[Operation]]] = {}
__legacy_operation_representations: dict[str, type[LegacyRepresentation[Operation]]] = {}


def get_hf26_operation_representation(type_name: str) -> type[HF26Representation[Operation]]:
    return __get_representation_from_type_dict(type_name, __hf26_operation_representations)


def get_legacy_operation_representation(type_name: str) -> type[LegacyRepresentation[Operation]]:
    return __get_representation_from_type_dict(type_name, __legacy_operation_representations)


def convert_to_representation(
    operation: Operation | VirtualOperation | Any,
) -> Hf26OperationRepresentationType | Hf26VirtualOperationRepresentationType:
    supported_types = (Operation, HF26Representation, LegacyRepresentation)
    assertion_message = f"Type {type(operation)} is not supported. Supported types are: {supported_types}"
    assert isinstance(operation, supported_types), assertion_message

    if isinstance(operation, HF26Representation):
        return operation

    if isinstance(operation, LegacyRepresentation):
        operation = operation.value
    return get_hf26_operation_representation(operation.get_name())(
        type=operation.get_name_with_suffix(), value=operation
    )


def _create_hf26_representation(incoming_type: type[Operation]) -> type[HF26Representation[Operation]]:
    operation_name_pascal_case = snake_case_to_pascal_case(incoming_type.get_name())
    new_model_name = f"{operation_name_pascal_case}HF26OperationRepresentation"
    field_definitions = {
        "type": (Literal[incoming_type.get_name_with_suffix()], ...),
        "value": (incoming_type, ...),
    }

    Hf26Operation = create_model(  # type: ignore[call-overload]   # noqa: N806
        new_model_name, __base__=HF26Representation[Operation], **field_definitions
    )
    __hf26_operation_representations[incoming_type.get_name()] = Hf26Operation
    return Hf26Operation  # type: ignore[no-any-return]


def _create_legacy_representation(incoming_cls: type[Operation]) -> type[LegacyRepresentation[Operation]]:
    """
    Representation of operation in legacy format
    Response from api has format [name_of_operation, {parameters}], to provide precise validation in root_validator
    it is converted to format below.
    """

    operation_name_pascal_case = snake_case_to_pascal_case(incoming_cls.get_name())
    new_model_name = f"{operation_name_pascal_case}LegacyOperationRepresentation"
    field_definitions = {
        "type": (Literal[incoming_cls.get_name()], ...),
        "value": (incoming_cls, ...),
    }
    LegacyOperation = create_model(  # type: ignore[call-overload]   # noqa: N806
        new_model_name, __base__=LegacyRepresentation[Operation], **field_definitions
    )
    __legacy_operation_representations[incoming_cls.get_name()] = LegacyOperation
    return LegacyOperation  # type: ignore[no-any-return]


def __get_representation_from_type_dict(type_name: str, collection: dict[str, type]) -> type:
    assert type_name in collection, f"`{type_name}` not found, available are: {list(collection.keys())}"
    return collection[type_name]
