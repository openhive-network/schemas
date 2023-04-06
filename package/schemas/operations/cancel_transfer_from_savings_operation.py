from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Uint32t


class CancelTransferFromSavingsOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    request_id: Uint32t = 0
