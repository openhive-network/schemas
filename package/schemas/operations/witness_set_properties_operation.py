from pydantic import BaseModel, Extra
from typing import Dict

from schemas.predefined import AccountName, LegacyChainProperties


class WitnessSetPropertiesOperation(BaseModel, extra=Extra.forbid):
    witness: AccountName
    props: LegacyChainProperties
