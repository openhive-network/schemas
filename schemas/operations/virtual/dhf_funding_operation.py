from __future__ import annotations



from schemas.fields.assets._base import AssetHbd
from schemas.fields.basic import AccountName
from schemas.virtual_operation import VirtualOperation


class _DhfFundingOperation(VirtualOperation, kw_only=True):
    treasury: AccountName
    additional_funds: AssetHbd


    @classmethod
    def get_name(cls):
        return "dhf_funding"
    
    @classmethod
    def offset(cls):
        return 17

class DhfFundingOperation(_DhfFundingOperation):
    pass


class DhfFundingOperationLegacy(_DhfFundingOperation):
    pass
