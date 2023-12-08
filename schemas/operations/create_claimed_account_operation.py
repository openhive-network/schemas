from __future__ import annotations

from pydantic import Field

from schemas.fields.basic import AccountName, PublicKey
from schemas.fields.compound import Authority
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions


class CreateClaimedAccountOperation(Operation):
    __operation_name__ = "create_claimed_account"
    __offset__ = 23

    creator: AccountName
    new_account_name: AccountName
    owner: Authority
    active: Authority
    posting: Authority
    memo_key: PublicKey
    json_metadata: str
    extensions: FutureExtensions = Field(default_factory=FutureExtensions)
