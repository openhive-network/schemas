from __future__ import annotations

from typing import Final

from schemas.fields.integers import Uint32t
from schemas.virtual_operation import VirtualOperation

DEFAULT_HARDFORK_ID: Final[Uint32t] = Uint32t(0)


class HardforkOperation(VirtualOperation):
    hardfork_id: Uint32t = DEFAULT_HARDFORK_ID

    @classmethod
    def get_name(cls):
        return "hardfork"
    
    @classmethod
    def offset(cls):
        return 10
