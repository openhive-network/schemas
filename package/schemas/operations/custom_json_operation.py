from pydantic import Json

from schemas.__private.hive_fields_schemas import AccountName, CustomIdType
from schemas.operations.preconfigure_base_model import PreconfiguredBaseModel


class CustomJsonOperation(PreconfiguredBaseModel):
    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id: CustomIdType
    json: Json
