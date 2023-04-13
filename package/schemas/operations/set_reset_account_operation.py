from schemas.package.schemas.predefined import AccountName
from preconfigure_base_model import PreconfiguredBaseModel


class SetResetAccountOperation(PreconfiguredBaseModel):
    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName
