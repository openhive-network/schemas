from __future__ import annotations

from typing import Any, Final

import msgspec

from schemas.decoders import dec_hook_hf26

TRANSFER_OPERATION_VALID_DATA: Final[dict[str, Any]] = {
    "from": "alice",
    "to": "bob",
    "amount": {"amount": "0", "precision": 3, "nai": "@@000000021"},
    "memo": "",
}


def test_from_schemas_import() -> None:
    # ACT & ASSERT
    from schemas.operations import TransferOperation

    msgspec.convert(obj=TRANSFER_OPERATION_VALID_DATA, type=TransferOperation, dec_hook=dec_hook_hf26)


def test_import_schemas() -> None:
    # ACT & ASSERT
    import schemas

    msgspec.convert(
        obj=TRANSFER_OPERATION_VALID_DATA, type=schemas.operations.TransferOperation, dec_hook=dec_hook_hf26
    )
