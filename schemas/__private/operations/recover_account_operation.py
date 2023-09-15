from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import AccountName, Authority
from schemas.__private.operation import Operation


class RecoverAccountOperation(Operation):
    __operation_name__ = "recover_account"

    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
