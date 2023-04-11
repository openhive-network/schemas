from schemas.package.schemas.predefined import AccountName
from preconfigure_base_model import PreconfiguredBaseModel


class ChangeRecoveryAccountOperation(PreconfiguredBaseModel):
    account_to_recover: AccountName
    new_recovery_account: AccountName
    