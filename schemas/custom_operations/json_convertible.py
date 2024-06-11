from __future__ import annotations

import json

from schemas._preconfigured_base_model import PreconfiguredBaseModel


class JsonConvertible(PreconfiguredBaseModel):
    @classmethod
    def validate(cls, value: str | JsonConvertible) -> JsonConvertible:
        if isinstance(value, JsonConvertible):
            return value
        parsed = json.loads(value)
        return cls(**parsed)
