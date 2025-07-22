from __future__ import annotations

from schemas.fields.integers import Uint8t
from schemas.operation import OperationExtension

DEFAULT_PAIR_ID: Uint8t = 0


class RecurrentTransferPairId(OperationExtension):
    @classmethod
    def get_name(cls) -> str:
        return "recurrent_transfer_pair_id"

    pair_id: Uint8t = DEFAULT_PAIR_ID
