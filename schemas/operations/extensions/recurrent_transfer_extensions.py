from __future__ import annotations

from schemas.fields.integers import Uint8t
from schemas.operations.extensions.extension import OperationExtension

DEFAULT_PAIR_ID: Uint8t = Uint8t(0)


class RecurrentTransferPairId(OperationExtension):
    __extension_name__ = "recurrent_transfer_pair_id"

    pair_id: Uint8t = DEFAULT_PAIR_ID
