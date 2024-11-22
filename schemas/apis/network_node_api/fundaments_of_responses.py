from __future__ import annotations

from typing import Any

from pydantic import StringConstraints

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.hive_int import HiveInt


class PublicKeyData(StringConstraints):
    strict = True
    min_length = 66
    max_length = 66


class ApiPeerStatus(PreconfiguredBaseModel):
    version: HiveInt
    host: str
    info: Any
