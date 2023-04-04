from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, Uint32t


class CancelTransferFromSavingsOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    request_id: Uint32t = 0
