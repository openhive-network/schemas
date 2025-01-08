from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class RecoverAccountOperation(Operation):
    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
    extensions: FutureExtensions = field(default_factory=FutureExtensions)  # type: ignore[type-arg]

    @classmethod
    def get_name(cls) -> str:
        return "recover_account"

    @classmethod
    def offset(cls) -> int:
        return 25
