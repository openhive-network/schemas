from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName
from schemas.virtual_operation import VirtualOperation


class DeclinedVotingRightsOperation(VirtualOperation):
    __operation_name__ = "declined_voting_rights"

    account: AccountName
