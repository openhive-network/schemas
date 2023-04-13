from schemas.__private.hive_fields_schemas import AccountName, Uint16t
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class CustomOperation(PreconfiguredBaseModel):
    required_auths: list[AccountName]
    id: Uint16t = 0
    data: list[str]
