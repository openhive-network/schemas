from __future__ import annotations

from typing import Annotated, Any

import msgspec

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hive_int import HiveInt

PublicKeyData = Annotated[str, msgspec.Meta(min_length=66, max_length=66)]


class ApiPeerStatus(PreconfiguredBaseModel):
    version: HiveInt
    host: str
    info: Any
