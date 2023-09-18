from __future__ import annotations

from typing import Annotated, Union, get_args

from pydantic import Field

from schemas.operations.representations import _create_hf26_representation, _create_legacy_representation
from schemas.operations.virtual import AnyLegacyVirtualOperation, AnyVirtualOperation

# VIRTUAL
__Hf26VirtualOperationRepresentationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
    tuple(_create_hf26_representation(arg) for arg in get_args(AnyVirtualOperation))
]

__LegacyVirtualOperationRepresentationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
    tuple(_create_legacy_representation(arg) for arg in get_args(AnyLegacyVirtualOperation))
]
Hf26VirtualOperationRepresentationType = Annotated[
    __Hf26VirtualOperationRepresentationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
]

LegacyVirtualOperationRepresentationType = Annotated[
    __LegacyVirtualOperationRepresentationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
]
