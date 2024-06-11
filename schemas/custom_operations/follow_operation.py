from __future__ import annotations

from schemas.custom_operations.base import CustomOperationBase, LegacyRepresentation
from schemas.fields.basic import AccountName


class FollowOperation(CustomOperationBase):
    __curtom_operation_name__ = "follow"

    follower: AccountName
    following: AccountName
    what: list[str]


FollowOperationLegacyRepresentation = LegacyRepresentation[FollowOperation]
