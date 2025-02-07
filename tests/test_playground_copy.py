# ruff: noqa
# type: ignore

from __future__ import annotations

import pytest

from schemas.decoders import get_hf26_decoder
from schemas.fields.assets._base import AssetHbd, AssetVests
from schemas.fields.hive_datetime import HiveDateTime
from schemas.operations.representation_types import HF26RepresentationTransferOperation
from schemas.operations.transfer_operation import TransferOperation
from schemas.transaction import Transaction
from schemas.jsonrpc import get_response_model
import json
from schemas.apis import database_api, wallet_bridge_api

TRX = Transaction(
    operations=[
        HF26RepresentationTransferOperation(
            value=TransferOperation(from_="alice", to="bob", amount=AssetHbd(1), memo="test")
        )
    ],
    ref_block_num=1,
    ref_block_prefix=2,
    expiration="2021-01-01T00:00:00",
    extensions=[],
    signatures=[],
)


GET_ACTIVE_WITNESSES = {
    "jsonrpc": "2.0",
    "result": {
        "witnesses": [
            "emrebeyler",
            "roelandp",
            "steempeak",
            "ausbitbank",
            "abit",
            "themarkymark",
            "cervantes",
            "gtg",
            "321",
            "good-karma",
            "threespeak",
            "smooth.witness",
            "blocktrades",
            "deathwing",
            "yabapmatt",
            "quochuy",
            "guiltyparties",
            "therealwolf",
            "ocd-witness",
            "steempress",
            "arcange",
        ]
    },
    "id": 1,
}


LIST_PROPOSALS = {
    "jsonrpc": "2.0",
    "result": {
        "proposals": [
            {
                "id": 250,
                "proposal_id": 250,
                "creator": "actifit",
                "receiver": "actifit.funds",
                "start_date": "2023-01-02T00:00:00",
                "end_date": "2024-01-02T00:00:00",
                "daily_pay": {"amount": "230000", "precision": 3, "nai": "@@000000013"},
                "subject": "Proposal for the Support of Actifit - Hive's Flagship Move2Earn Dapp",
                "permlink": "proposal-for-the-support-of-actifit-hives-flagship-move2earn-dapp",
                "total_votes": "68790473297987607",
                "status": "active",
            }
        ]
    },
    "id": 1,
}


# @pytest.mark.skip(reason="no way of currently testing this")
def test_responses_from_api_correct_values() -> None:
    amount = 296909911037211111

    dupa = AssetVests(amount)

    xd = dupa.as_legacy()

    pass
