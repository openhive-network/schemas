from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, Uint32t


class WitnessBlockApproveOperation(BaseModel, extra=Extra.forbid):
    witness: AccountName
    block_id: Uint32t

