from __future__ import annotations

from typing import Literal, overload

import msgspec

from schemas.operation import Operation
from schemas.operations.claim_reward_balance_operation import ClaimRewardBalanceOperation
from schemas.operations.vote_operation import VoteOperation


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


class LegacyRepresentationVoteOperation(LegacyRepresentation, tag="vote", array_like=True):
    value: VoteOperation


class HF26RepresentationClaimRewardBalanceOperation(HF26Representation, tag="claim_reward_balance_operation"):
    value: ClaimRewardBalanceOperation


class LegacyRepresentationClaimRewardBalanceOperation(LegacyRepresentation, tag="claim_reward_balance", array_like=True):
    value: ClaimRewardBalanceOperation
