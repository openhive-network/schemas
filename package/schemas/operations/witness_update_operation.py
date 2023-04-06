from __future__ import annotations

from pydantic import BaseModel, Extra

from schemas.predefined import AccountName, PublicKey, LegacyChainProperties


class WitnessUpdateOperation(BaseModel, extra=Extra.forbid):
    owner: AccountName
    url: str
    block_signing_key: PublicKey
    props: LegacyChainProperties
