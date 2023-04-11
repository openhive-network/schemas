from pydantic import Json

from schemas.package.schemas.predefined import AccountName, CustomIdType
from preconfigure_base_model import PreconfiguredBaseModel


class CustomJsonOperation(PreconfiguredBaseModel):
    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id: CustomIdType
    json: Json
