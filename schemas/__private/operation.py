from __future__ import annotations

import re

from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel


class Operation(PreconfiguredBaseModel):
    """Base class for all operations to provide valid json serialization"""

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__.split("[")[0]

    @classmethod
    def get_name(cls) -> str:
        """
        Get the name of the operation.

        e.g. `transfer` for `TransferOperation`
        """
        return cls.get_name_with_suffix().replace("_operation", "")

    @classmethod
    def get_name_with_suffix(cls) -> str:
        """
        Get the name of the operation with the `_operation` suffix.

        e.g. `transfer_operation` for `TransferOperation`
        """
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.get_class_name()).lower()  # convert class name to snake case
