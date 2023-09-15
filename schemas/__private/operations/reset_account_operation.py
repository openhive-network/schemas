from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority
from schemas.__private.operation import Operation


class ResetAccountOperation(Operation):
    __operation_name__ = "reset_account"

    reset_account: AccountName
    account_to_reset: AccountName
    new_owner_authority: Authority
