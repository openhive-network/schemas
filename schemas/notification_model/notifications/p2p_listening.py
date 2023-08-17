from __future__ import annotations

from typing import Literal

from pydantic import Field

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class P2PListening(PreconfiguredBaseModel):
    type_: Literal["p2p"] = Field(alias="type")
    address: str
    port: int
