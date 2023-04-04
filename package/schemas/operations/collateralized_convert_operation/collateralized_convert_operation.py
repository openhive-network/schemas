from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, Uint32t, LegacyAssetHive


class CollateralizedConvertOperation(BaseModel, extra=Extra.forbid):
    owner: AccountName
    request_id: Uint32t = 0
    amount: LegacyAssetHive
    