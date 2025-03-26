from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.operations.custom.custom_base_operation import CustomBaseOperation


class FollowOperation(CustomBaseOperation):
    __operation_name__ = "follow"

    follower: AccountName
    following: AccountName
    what: list[str]

    @classmethod
    def get_name(cls) -> str:
        return "follow"
