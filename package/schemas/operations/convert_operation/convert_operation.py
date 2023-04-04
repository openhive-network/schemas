from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, Uint32t, LegacyAssetHbd


class ConvertOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    request_id: Uint32t = 0
    amount: LegacyAssetHbd
