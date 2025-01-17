from __future__ import annotations



from schemas.fields.assets._base import AssetHbd, AssetHive, AssetVest
from schemas.fields.basic import AccountName
from schemas.operation import Operation


class _ClaimRewardBalanceOperation(Operation):
    account: AccountName
    reward_hive: AssetHive
    reward_hbd: AssetHbd
    reward_vests: AssetVest

    @classmethod
    def get_name(cls):
        return "claim_reward_balance"
    
    @classmethod
    def offset(cls):
        return 39

class ClaimRewardBalanceOperation(_ClaimRewardBalanceOperation):
    ...


class ClaimRewardBalanceOperationLegacy(
    _ClaimRewardBalanceOperation
):
    ...
