from abc import abstractmethod
import typing
from typing import Dict

from schemas.__private.fundamental_schemas import AnyOf, Array, ArrayStrict, Date, Int, Map, Schema, Str


class CustomSchema(Schema):
    @abstractmethod
    def _define_schema(self) -> Schema:
        pass

    def _create_core_of_schema(self) -> Dict[str, typing.Any]:
        return self._define_schema()._create_schema()


class AccountName(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[a-z0-9-\.]{3,16}$')


class AssetAny(CustomSchema):
    def _define_schema(self) -> Schema:
        return AnyOf(
            AssetHbd(),
            AssetHive(),
            AssetVests(),
        )


class AssetHbd(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'amount': Int(),
            'precision': Int(enum=[3]),
            'nai': Str(pattern='@@000000013'),
        })


class AssetHive(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'amount': Int(),
            'precision': Int(enum=[3]),
            'nai': Str(pattern='@@000000021'),
        })


class AssetVests(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'amount': Int(),
            'precision': Int(enum=[6]),
            'nai': Str(pattern='@@000000037'),
        })


class Authority(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'weight_threshold': Int(),
            'account_auths': Array(
                ArrayStrict(
                    Str(),
                    Int(),
                )
            ),
            'key_auths': Array(
                ArrayStrict(
                    PublicKey(),
                    Int(),
                )
            ),
        })


class HardforkVersion(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^\d+\.\d+\.\d+$')


class Hex(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'[0-9a-fA-F]')


class LegacyAssetAny(CustomSchema):
    def _define_schema(self) -> Schema:
        return AnyOf(
            LegacyAssetHbd(),
            LegacyAssetHive(),
            LegacyAssetVests(),
        )


class LegacyAssetHbd(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9]*.[0-9]{3} HBD$')


class LegacyAssetHive(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9]*.[0-9]{3} HIVE$')


class LegacyAssetVests(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9]*.[0-9]{6} VESTS$')


class Manabar(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            "current_mana": Int(),
            "last_update_time": Int(),
        })


class Price(CustomSchema):
    def __init__(self, base, quote):
        super().__init__()
        self.base = base
        self.quote = quote

    def _define_schema(self) -> Schema:
        return Map({
            'base': self.base,
            'quote': self.quote,
        })


class Proposal(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'id': Int(),
            'proposal_id': Int(),
            'creator': Str(),
            'receiver': Str(),
            'start_date': Date(),
            'end_date': Date(),
            'daily_pay': AssetHbd(),
            'subject': Str(),
            'permlink': Str(),
            'total_votes': Int(),
            'status': Str(),
        })


class PublicKey(CustomSchema):
    def _define_schema(self) -> Schema:
        # See `wif_to_key` implementation in `fc` library for more information about this regex:
        wif_private_key_regex = r'^[ ]*^(?:STM|TST)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}[ ]*$'
        return Str(pattern=wif_private_key_regex)


class Signature(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9a-fA-F]{130}$')


class TransactionId(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9a-fA-F]{40}$')
