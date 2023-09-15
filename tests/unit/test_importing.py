from __future__ import annotations

from typing import Any, Final

TRANSFER_OPERATION_VALID_DATA: Final[dict[str, Any]] = {
    "from": "alice",
    "to": "bob",
    "amount": {"amount": "0", "precision": 3, "nai": "@@000000021"},
    "memo": "",
}


def test_from_schemas_import() -> None:
    # ACT & ASSERT
    from schemas.operations import TransferOperationHF26

    TransferOperationHF26(**TRANSFER_OPERATION_VALID_DATA)


def test_import_schemas() -> None:
    # ACT & ASSERT
    import schemas

    schemas.operations.TransferOperationHF26(**TRANSFER_OPERATION_VALID_DATA)
