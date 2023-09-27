from __future__ import annotations

from schemas.operations import RecurrentTransferOperation, RecurrentTransferOperationLegacy


def test_recurrent_transfer_extension_hf_26_representation() -> None:
    # ARRANGE
    data = {
        "amount": {"amount": "1000", "precision": 3, "nai": "@@000000013"},
        "executions": 2,
        "extensions": [
            {
                "type": "recurrent_transfer_pair_id",
                "value": {"pair_id": 1},
            }
        ],
        "from": "sender",
        "memo": "{}",
        "recurrence": 48,
        "to": "receiver",
    }

    # ACT & ASSERT
    RecurrentTransferOperation(**data)


def test_recurrent_transfer_extension_legacy_representation() -> None:
    # ARRANGE
    data = {
        "amount": "1.000 HIVE",
        "executions": 2,
        "extensions": [
            [
                "recurrent_transfer_pair_id",
                {"pair_id": 1},
            ]
        ],
        "from": "sender",
        "memo": "{}",
        "recurrence": 48,
        "to": "receiver",
    }

    # ACT & ASSERT
    RecurrentTransferOperationLegacy(**data)
