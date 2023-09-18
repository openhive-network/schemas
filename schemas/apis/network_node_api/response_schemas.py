from __future__ import annotations

from typing import Literal

from schemas.__private.hive_fields_basic_schemas import HiveInt
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.network_node_api.fundaments_of_responses import (
    ApiPeerStatus,
    PublicKeyData,
)


class AddNode(PreconfiguredBaseModel):
    endpoint: str


class GetConnectedPeers(PreconfiguredBaseModel):
    connected_peers: list[ApiPeerStatus]


class GetInfo(PreconfiguredBaseModel):
    listening_on: str
    node_public_key: PublicKeyData
    node_id: PublicKeyData
    firewalled: Literal["unknown", "firewalled", "not_firewalled"]
    connection_count: HiveInt


class SetAllowedPeers(PreconfiguredBaseModel):
    """Empty model"""
