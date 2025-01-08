from __future__ import annotations

from msgspec import field

from schemas.fields.basic import AccountName, PublicKey
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class CreateClaimedAccountOperation(Operation):
    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str
    extensions: FutureExtensions = field(default_factory=FutureExtensions)  # type: ignore[type-arg]

    @classmethod
    def get_name(cls) -> str:
        return "create_claimed_account"

    @classmethod
    def offset(cls) -> int:
        return 23
