from schemas.package.schemas.predefined import AccountName, Authority
from preconfigure_base_model import PreconfiguredBaseModel


class RequestAccountRecoveryOperation(PreconfiguredBaseModel):
    recovery_account: AccountName
    account_to_recover: AccountName
    new_owner_authority: Authority

