from pydantic import BaseModel, Extra
from typing import Dict

from schemas.predefined import AccountName


class WitnessSetPropertiesOperation(BaseModel, extra=Extra.forbid):
    witness: AccountName
    props: Dict[str, str]  # to check
