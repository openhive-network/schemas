from __future__ import annotations


import msgspec

from schemas.operations.virtual.author_reward_operation import AuthorRewardOperation, AuthorRewardOperationLegacy
# from schemas.operations.virtual import AnyLegacyVirtualOperation, AnyVirtualOperation

# VIRTUAL
# __Hf26VirtualOperationRepresentationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
#     tuple(_create_hf26_representation(arg) for arg in get_args(AnyVirtualOperation))
# ]

# __LegacyVirtualOperationRepresentationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
#     tuple(_create_legacy_representation(arg) for arg in get_args(AnyLegacyVirtualOperation))
# ]
# Hf26VirtualOperationRepresentationType = Annotated[
#     __Hf26VirtualOperationRepresentationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
# ]

# LegacyVirtualOperationRepresentationType = Annotated[
#     __LegacyVirtualOperationRepresentationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
# ]


class HF26RepresentationAuthorRewardOperation(msgspec.Struct, tag="author_reward_operation"):
    value: AuthorRewardOperation


class LegacyRepresentationAuthorRewardOperationLegacy(msgspec.Struct, tag="author_reward", array_like=True):
    value: AuthorRewardOperationLegacy
