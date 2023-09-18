from __future__ import annotations

from typing import Final

from schemas.__private.hive_fields_basic_schemas import Uint32t
from schemas.__private.virtual_operation import VirtualOperation

DEFAULT_HARDFORK_ID: Final[Uint32t] = Uint32t(0)


class HardforkOperation(VirtualOperation):
    __operation_name__ = "hardfork"

    hardfork_id: Uint32t = DEFAULT_HARDFORK_ID
