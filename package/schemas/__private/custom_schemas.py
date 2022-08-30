from abc import abstractmethod
import typing
from typing import Dict

from schemas.__private.fundamental_schemas import AnyOf, Array, ArrayStrict, Bool, Date, Int, Map, Schema, Str


class CustomSchema(Schema):
    @abstractmethod
    def _define_schema(self) -> Schema:
        pass

    def _create_core_of_schema(self) -> Dict[str, typing.Any]:
        return self._define_schema()._create_schema()


class AccountName(CustomSchema):
    def _define_schema(self) -> Schema:
        name_segment = r'[a-z][a-z0-9\-]+[a-z0-9]'
        return Str(
            pattern=fr'^{name_segment}(?:\.{name_segment})*$',
            minLength=3,
            maxLength=16
        )


class ApiOperationObject(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'trx_id': TransactionId(),
            'block': Int(),
            'trx_in_block': Int(),
            'op_in_trx': Int(),
            'virtual_op': Bool(),
            'operation_id': Int(),
            'timestamp': Date(),
            'op': AnyOf(
                Map({
                    'type': Str(),
                    'value': Map({}, allow_additional_properties=True),
                }),
                ArrayStrict(Str(), Map({}))
            )
        })


class AssetAny(CustomSchema):
    def _define_schema(self) -> Schema:
        return AnyOf(
            AssetHbd(),
            AssetHive(),
            AssetVests(),
        )


class AssetHbd(CustomSchema):
    @staticmethod
    def Amount():
        return Int()

    @staticmethod
    def Precision():
        return Int(enum=[3])

    @staticmethod
    def Nai():
        return Str(pattern='@@000000013')

    def _define_schema(self) -> Schema:
        return Map({
            'amount': self.Amount(),
            'precision': self.Precision(),
            'nai': self.Nai(),
        })


class AssetHive(CustomSchema):
    @staticmethod
    def Amount():
        return Int()

    @staticmethod
    def Precision():
        return Int(enum=[3])

    @staticmethod
    def Nai():
        return Str(pattern='@@000000021')

    def _define_schema(self) -> Schema:
        return Map({
            'amount': self.Amount(),
            'precision': self.Precision(),
            'nai': self.Nai(),
        })


class AssetVests(CustomSchema):
    @staticmethod
    def Amount():
        return Int()

    @staticmethod
    def Precision():
        return Int(enum=[6])

    @staticmethod
    def Nai():
        return Str(pattern='@@000000037')

    def _define_schema(self) -> Schema:
        return Map({
            'amount': self.Amount(),
            'precision': self.Precision(),
            'nai': self.Nai(),
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


class EmptyString(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern='')


class HardforkVersion(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^\d+\.\d+\.\d+$')


class Hex(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9a-fA-F]*$')


class LegacyAssetAny(CustomSchema):
    def _define_schema(self) -> Schema:
        return AnyOf(
            LegacyAssetHbd(),
            LegacyAssetHive(),
            LegacyAssetVests(),
        )


class LegacyAssetHbd(CustomSchema):
    @staticmethod
    def Symbol():
        return Str(enum=['HBD', 'TBD'])

    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9]+\.[0-9]{3} (?:HBD|TBD)$')


class LegacyAssetHive(CustomSchema):
    @staticmethod
    def Symbol():
        return Str(enum=['HIVE', 'TESTS'])

    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9]+\.[0-9]{3} (?:HIVE|TESTS)$')


class LegacyAssetVests(CustomSchema):
    @staticmethod
    def Symbol():
        return Str(enum=['VESTS'])

    def _define_schema(self) -> Schema:
        return Str(pattern=r'^[0-9]+\.[0-9]{6} VESTS$')


class Manabar(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            "current_mana": Int(),
            "last_update_time": Int(),
        })


class Permlink(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(maxLength=256)


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
        wif_private_key_regex = r'^(?:STM|TST)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$'
        return Str(pattern=wif_private_key_regex)


class Signature(CustomSchema):
    def _define_schema(self) -> Schema:
        return Hex(minLength=130, maxLength=130)


class TransactionId(CustomSchema):
    def _define_schema(self) -> Schema:
        return Hex(minLength=40, maxLength=40)
