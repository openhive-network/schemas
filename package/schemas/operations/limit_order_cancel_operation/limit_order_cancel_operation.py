from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName, Uint32t


class LimitOrderCancelOperation(BaseModel, extra=Extra.forbid):
    owner: AccountName
    order_id: Uint32t = 0
