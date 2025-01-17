from __future__ import annotations


from msgspec import field

from schemas.fields.assets._base import AssetHive
from schemas.fields.basic import AccountName
from schemas.operation import Operation
from schemas.operations.extensions.future_extension import FutureExtensions

"""
If a user wants to pay a fee in RC fee should be equal 0.
"""


class _ClaimAccountOperation(Operation):
    creator: AccountName
    fee: AssetHive# | Literal[0]
    extensions: FutureExtensions = field(default_factory=FutureExtensions)

    @classmethod
    def get_name(cls):
        return "claim_account"
    
    @classmethod
    def offset(cls):
        return 22


class ClaimAccountOperation(_ClaimAccountOperation):
    ...


class ClaimAccountOperationLegacy(_ClaimAccountOperation):
    ...
