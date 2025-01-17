from __future__ import annotations

from typing import Any


from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.operation import Operation
from schemas.operations.extensions.extension import OperationExtension


class HF26Representation(PreconfiguredBaseModel):
    type: str  # noqa: A003
    value: Operation | OperationExtension

    def __getitem__(self, key: str | int) -> Any:
        """This method has been added to reduce changes in tests in cli_wallet, where we change legacy to HF26 protocool"""
        if isinstance(key, int):
            match key:
                case 0:
                    return self.value.get_name()
                case 1:
                    return self.value
                case _:
                    raise ValueError("out of bound")
        return super().__getitem__(key)
