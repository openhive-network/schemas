from __future__ import annotations

from typing import Any, Final

TRANSFER_OPERATION_VALID_DATA: Final[dict[str, Any]] = {
    "from": "alice",
    "to": "bob",
    "amount": "1.000 HIVE",
    "memo": "",
}


def test_from_schemas_import() -> None:
    # ACT & ASSERT
    from schemas.operations import TransferOperation

    TransferOperation(**TRANSFER_OPERATION_VALID_DATA)


def test_import_schemas() -> None:
    # ACT & ASSERT
    import schemas

    schemas.operations.TransferOperation(**TRANSFER_OPERATION_VALID_DATA)
