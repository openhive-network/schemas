from pydantic import BaseModel, Extra

from schemas.__private.fields_schemas import AccountName


class RequestAccountRecovery(BaseModel, extra=Extra.forbid):
    