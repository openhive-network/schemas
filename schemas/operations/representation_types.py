from __future__ import annotations

from typing import Annotated, Literal, Union, get_args, overload

import msgspec

# from schemas.operations import AnyEveryOperation, AnyLegacyEveryOperation, AnyLegacyOperation, AnyOperation
from schemas.operation import Operation
from schemas.operations.claim_reward_balance_operation import ClaimRewardBalanceOperation
from schemas.operations.representations.util import _create_hf26_representation, _create_legacy_representation
from schemas.operations.vote_operation import VoteOperation

# __all__ = [
#     "Hf26OperationRepresentationType",
#     "LegacyOperationRepresentationType",
#     "Hf26AllOperationRepresentationType",
#     "LegacyAllOperationRepresentationType",
# ]

# # NON-VIRTUAL
# __Hf26OperationRepresentationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
#     tuple(_create_hf26_representation(arg) for arg in get_args(AnyOperation))
# ]

# __LegacyOperationRepresentationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
#     tuple(_create_legacy_representation(arg) for arg in get_args(AnyLegacyOperation))
# ]

# Hf26OperationRepresentationType = Annotated[
#     __Hf26OperationRepresentationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
# ]

# LegacyOperationRepresentationType = Annotated[
#     __LegacyOperationRepresentationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
# ]

# # ALL
# __Hf26AllOperationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
#     tuple(_create_hf26_representation(arg) for arg in get_args(AnyEveryOperation))
# ]

# __LegacyAllOperationUnionType = Union[  # type: ignore[valid-type]  # noqa: UP007
#     tuple(_create_legacy_representation(arg) for arg in get_args(AnyLegacyEveryOperation))
# ]

# Hf26AllOperationRepresentationType = Annotated[
#     __Hf26AllOperationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
# ]

# LegacyAllOperationRepresentationType = Annotated[
#     __LegacyAllOperationUnionType, Field(discriminator="type")  # type: ignore[valid-type]
# ]

class HF26Representation(msgspec.Struct):
    value: Operation
    
    @property
    def type_(self) -> str:
        return self.value.get_name_with_suffix()
    
class LegacyRepresentation(msgspec.Struct):
    value: Operation
    
    @property
    def type_(self) -> str:
        return self.value.get_name()
    
    @overload
    def __getitem__(self, idx: Literal[0]) -> str: ...
    @overload
    def __getitem__(self, idx: Literal[1]) -> Operation: ...

    def __getitem__(self, idx: Literal[0, 1]) -> str | Operation:
        if idx == 0:
            return self.type_
        elif idx == 1:
            return self.value
        raise ValueError("Index out of bound <0; 1>")


class HF26RepresentationVoteOperation(HF26Representation, tag="vote_operation"):
    value: VoteOperation

class HF26RepresentationClaimRewardBalanceOperation(HF26Representation, tag="claim_reward_balance_operation"):
    value: ClaimRewardBalanceOperation


class LegacyRepresentationVoteOperation(LegacyRepresentation, tag="vote", array_like=True):
    value: VoteOperation


class LegacyRepresentationClaimRewardBalanceOperation(LegacyRepresentation, tag="claim_reward_balance", array_like=True):
    value: ClaimRewardBalanceOperation