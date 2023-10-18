from __future__ import annotations

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class RecoverAccountOperation(Operation):
    __operation_name__ = "recover_account"
    __offset__ = 25

    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
    extensions: FutureExtensions
