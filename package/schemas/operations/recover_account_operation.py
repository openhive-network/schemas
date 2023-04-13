from schemas.package.schemas.predefined import AccountName, Authority
from preconfigure_base_model import PreconfiguredBaseModel


class RecoverAccountOperation(PreconfiguredBaseModel):
    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
