from schemas.__private.hive_fields_schemas import AccountName
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class SetResetAccountOperation(PreconfiguredBaseModel):
    account: AccountName
    current_reset_account: AccountName
    reset_account: AccountName
