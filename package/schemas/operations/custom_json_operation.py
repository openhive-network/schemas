from pydantic import BaseModel, Extra, Json

from schemas.predefined import AccountName, CustomIdType


class CustomJsonOperation(BaseModel, extra=Extra.forbid):
    required_auths: list[AccountName]
    required_posting_auths: list[AccountName]
    id: CustomIdType
    json: Json
