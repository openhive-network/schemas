from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName, PublicKey
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class AccountUpdate2Operation(Operation):
    account: AccountName
    owner: Authority | None = None
    active: Authority | None = None
    posting: Authority | None = None
    memo_key: PublicKey | None = None
    json_metadata: str | None = None
    posting_json_metadata: str | None = None
    extensions: FutureExtensions = field(default_factory=FutureExtensions)  # type: ignore[type-arg]

    @classmethod
    def get_name(cls) -> str:
        return "account_update2"

    @classmethod
    def offset(cls) -> int:
        return 43
