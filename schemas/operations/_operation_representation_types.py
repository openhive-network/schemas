from __future__ import annotations

from typing import Annotated, Any, Literal, Union, get_args

from pydantic import Field

from schemas.operations._operation_types import (
    AllOperationType,
    Hf26AllOperationType,
    Hf26OperationType,
    Hf26VirtualOperationType,
    LegacyAllOperationType,
    LegacyOperationType,
    LegacyVirtualOperationType,
)
from schemas.operations.virtual import (
    LegacyEffectiveCommentVoteOperation,
    NaiEffectiveCommentVoteOperation,
)
from schemas.preconfigured_base_model import PreconfiguredBaseModel


class Hf26OperationRepresentation(PreconfiguredBaseModel):
    type: str  # noqa: A003
    value: Hf26AllOperationType


class LegacyOperationRepresentation(PreconfiguredBaseModel):
    type: str  # noqa: A003
    value: LegacyAllOperationType

    def __getitem__(self, key: str | int) -> str | LegacyAllOperationType | Any:
        if isinstance(key, int):
            match (key):
                case 0:
                    return self.value.get_name().replace("_operation", "")
                case 1:
                    return self.value
                case _:
                    raise ValueError("out of bound")
        return super().__getitem__(key)


__hf26_operation_representations: dict[str, type[Hf26OperationRepresentation]] = {}
__legacy_operation_representations: dict[str, type[LegacyOperationRepresentation]] = {}


def __get_representation_from_type_dict(type_name: str, collection: dict[str, type]) -> type:
    assert type_name in collection, f"`{type_name}` not found, available are: {list(collection.keys())}"
    return collection[type_name]


def get_hf26_representation(type_name: str) -> type[Hf26OperationRepresentation]:
    return __get_representation_from_type_dict(type_name, __hf26_operation_representations)


def get_legacy_representation(type_name: str) -> type[LegacyOperationRepresentation]:
    return __get_representation_from_type_dict(type_name, __legacy_operation_representations)


def __create_hf26_representation(incoming_type: type[Hf26OperationType]) -> type[Hf26OperationRepresentation]:
    class Hf26Operation(Hf26OperationRepresentation):
        type: Literal[f"{incoming_type.get_name()}"]  # type: ignore[valid-type]  # noqa: A003
        value: incoming_type  # type: ignore[valid-type]

    Hf26Operation.update_forward_refs(**locals())
    __hf26_operation_representations[incoming_type.get_name()] = Hf26Operation
    return Hf26Operation


def __create_legacy_representation(incoming_cls: type[LegacyOperationType]) -> type[LegacyOperationRepresentation]:
    """
    Representation of operation in legacy format
    Response from api has format [name_of_operation, {parameters}], to provide precise validation in root_validator
    it is converted to format below.
    """

    cls_name_snake: str = incoming_cls.get_name().replace("_operation", "")

    class LegacyOperation(LegacyOperationRepresentation):
        type: Literal[f"{cls_name_snake}"]  # type: ignore[valid-type] # noqa: A003
        value: incoming_cls  # type: ignore[valid-type]

    LegacyOperation.update_forward_refs(**locals())
    __legacy_operation_representations[cls_name_snake] = LegacyOperation
    return LegacyOperation


# NON-VIRTUAL
__Hf26OperationRepresentationUnionType = Union[tuple(__create_hf26_representation(arg) for arg in get_args(Hf26OperationType))]  # type: ignore
__LegacyOperationRepresentationUnionType = Union[tuple(__create_legacy_representation(arg) for arg in get_args(LegacyOperationType))]  # type: ignore
Hf26OperationRepresentationType = Annotated[__Hf26OperationRepresentationUnionType, Field(discriminator="type")]  # type: ignore
LegacyOperationRepresentationType = Annotated[__LegacyOperationRepresentationUnionType, Field(discriminator="type")]  # type: ignore

# VIRTUAL
__Hf26VirtualOperationRepresentationUnionType = Union[tuple(__create_hf26_representation(arg) for arg in (*get_args(Hf26VirtualOperationType), NaiEffectiveCommentVoteOperation))]  # type: ignore
__LegacyVirtualOperationRepresentationUnionType = Union[tuple(__create_legacy_representation(arg) for arg in (*get_args(LegacyVirtualOperationType), LegacyEffectiveCommentVoteOperation))]  # type: ignore
Hf26VirtualOperationRepresentationType = Annotated[__Hf26VirtualOperationRepresentationUnionType, Field(discriminator="type")]  # type: ignore
LegacyVirtualOperationRepresentationType = Annotated[__LegacyVirtualOperationRepresentationUnionType, Field(discriminator="type")]  # type: ignore

# ALL
__Hf26AllOperationUnionType = Union[tuple(__create_hf26_representation(arg) for arg in (*get_args(AllOperationType), NaiEffectiveCommentVoteOperation))]  # type: ignore
__LegacyAllOperationUnionType = Union[tuple(__create_legacy_representation(arg) for arg in (*get_args(AllOperationType), LegacyEffectiveCommentVoteOperation))]  # type: ignore
Hf26AllOperationRepresentationType = Annotated[__Hf26AllOperationUnionType, Field(discriminator="type")]  # type: ignore
LegacyAllOperationRepresentationType = Annotated[__LegacyAllOperationUnionType, Field(discriminator="type")]  # type: ignore

__all__ = [
    "get_hf26_representation",
    "get_legacy_representation",
    "Hf26OperationRepresentation",
    "LegacyOperationRepresentation",
    "Hf26OperationRepresentationType",
    "LegacyOperationRepresentationType",
    "Hf26VirtualOperationRepresentationType",
    "LegacyVirtualOperationRepresentationType",
    "Hf26AllOperationRepresentationType",
    "LegacyAllOperationRepresentationType",
]
