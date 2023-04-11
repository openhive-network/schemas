from schemas.package.schemas.predefined import AccountName, Authority
from preconfigure_base_model import PreconfiguredBaseModel


class ResetAccountOperation(PreconfiguredBaseModel):
    reset_account: AccountName
    account_to_reset: AccountName
    new_owner_authority: Authority
