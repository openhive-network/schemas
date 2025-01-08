from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class RequestAccountRecoveryOperation(Operation):
    recovery_account: AccountName
    account_to_recover: AccountName
    new_owner_authority: Authority
    extensions: FutureExtensions = field(default_factory=FutureExtensions)  # type: ignore[type-arg]

    @classmethod
    def get_name(cls) -> str:
        return "request_account_recovery"

    @classmethod
    def offset(cls) -> int:
        return 24
