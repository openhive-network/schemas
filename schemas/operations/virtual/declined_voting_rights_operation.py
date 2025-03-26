from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class DeclinedVotingRightsOperation(VirtualOperation):
    account: AccountName

    @classmethod
    def get_name(cls) -> str:
        return "declined_voting_rights"

    @classmethod
    def vop_offset(cls) -> int:
        return 42
