from __future__ import annotations

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.apis.beekeeper_api.fundaments_of_responses import PublicKeyItem, WalletDetails
from schemas.fields.basic import PublicKey
from schemas.fields.hex import Signature
from schemas.fields.hive_datetime import HiveDateTime


class Create(PreconfiguredBaseModel):
    password: str


class CreateSession(PreconfiguredBaseModel):
    token: str


class EmptyResponse(PreconfiguredBaseModel):
    pass


class GetInfo(PreconfiguredBaseModel):
    now: HiveDateTime
    timeout_time: HiveDateTime


class GetPublicKeys(PreconfiguredBaseModel):
    keys: list[PublicKeyItem]


class ImportKey(PublicKeyItem):
    pass


class ImportKeys(PreconfiguredBaseModel):
    public_keys: list[PublicKey]


class ListKeys(PreconfiguredBaseModel):
    keys: dict[str, str]


class ListWallets(PreconfiguredBaseModel):
    wallets: list[WalletDetails]


class SignDigest(PreconfiguredBaseModel):
    signature: Signature


class SignTransaction(SignDigest):
    pass


class HasMatchingPrivateKey(PreconfiguredBaseModel):
    exists: bool


class EncryptData(PreconfiguredBaseModel):
    encrypted_content: str


class DecryptData(PreconfiguredBaseModel):
    decrypted_content: str
