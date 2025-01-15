from __future__ import annotations

from msgspec import field
from pydantic import Field

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
    extensions: FutureExtensions = field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls):
        return "create_claimed_account"
    
    @classmethod
    def offset(cls):
        return 23
