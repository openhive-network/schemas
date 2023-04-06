from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Uint16t


class CustomOperation(BaseModel, extra=Extra.forbid):
    required_auths: list[AccountName]
    id: Uint16t = 0
    data: list[str]
    