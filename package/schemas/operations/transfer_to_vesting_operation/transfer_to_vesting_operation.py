from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, LegacyAssetHive


class TransferToVestingOperation(BaseModel, extra=Extra.forbid):
    From: AccountName
    to: AccountName | None
    amount: LegacyAssetHive
