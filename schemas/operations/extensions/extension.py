from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel


class OperationExtension(PreconfiguredBaseModel):
    __extension_name__: str

    @classmethod
    def get_name(cls) -> str:
        return cls.__extension_name__
