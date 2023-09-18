from __future__ import annotations

from typing import Annotated, Union, get_args

from pydantic import Field

from schemas.__private.operations import AnyEveryOperation, AnyLegacyEveryOperation, AnyLegacyOperation, AnyOperation
from schemas.__private.operations.representations import _create_hf26_representation, _create_legacy_representation

__all__ = [
    "Hf26OperationRepresentationType",
    "LegacyOperationRepresentationType",
    "Hf26AllOperationRepresentationType",
    "LegacyAllOperationRepresentationType",
]

# NON-VIRTUAL
__Hf26OperationRepresentationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
    tuple(_create_hf26_representation(arg) for arg in get_args(AnyOperation))
]

__LegacyOperationRepresentationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
    tuple(_create_legacy_representation(arg) for arg in get_args(AnyLegacyOperation))
]

Hf26OperationRepresentationType = Annotated[
    __Hf26OperationRepresentationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
]

LegacyOperationRepresentationType = Annotated[
    __LegacyOperationRepresentationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
]

# ALL
__Hf26AllOperationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
    tuple(_create_hf26_representation(arg) for arg in get_args(AnyEveryOperation))
]

__LegacyAllOperationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
    tuple(_create_legacy_representation(arg) for arg in get_args(AnyLegacyEveryOperation))
]

Hf26AllOperationRepresentationType = Annotated[
    __Hf26AllOperationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
]

LegacyAllOperationRepresentationType = Annotated[
    __LegacyAllOperationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
]
