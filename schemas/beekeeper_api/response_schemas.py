from __future__ import annotations

from schemas.__private.hive_fields_basic_schemas import HiveDateTime, PublicKey
from schemas.__private.hive_fields_custom_schemas import Signature
from schemas.__private.preconfigured_base_model import PreconfiguredBaseModel
from schemas.beekeeper_api.fundaments_of_responses import WalletDetails


class EmptyResponse(PreconfiguredBaseModel):
    pass


class CreateSession(PreconfiguredBaseModel):
    token: str


class Create(PreconfiguredBaseModel):
    password: str


class ImportKey(PreconfiguredBaseModel):
    public_key: PublicKey


class ListKeys(PreconfiguredBaseModel):
    keys: dict[str, str]


class ListWallets(PreconfiguredBaseModel):
    wallets: list[WalletDetails]


class GetPublicKeys(PreconfiguredBaseModel):
    keys: list[PublicKey]


class SignDigest(PreconfiguredBaseModel):
    signature: Signature


class SignTransaction(SignDigest):
    pass


class GetInfo(PreconfiguredBaseModel):
    now: HiveDateTime
    timeout_time: HiveDateTime
