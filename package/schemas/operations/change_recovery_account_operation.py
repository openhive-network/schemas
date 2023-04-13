from schemas.__private.hive_fields_schemas import AccountName
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class ChangeRecoveryAccountOperation(PreconfiguredBaseModel):
    account_to_recover: AccountName
    new_recovery_account: AccountName
