from schemas.__private.hive_fields_schemas import AccountName, Authority
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class RecoverAccountOperation(PreconfiguredBaseModel):
    account_to_recover: AccountName
    new_owner_authority: Authority
    recent_owner_authority: Authority
