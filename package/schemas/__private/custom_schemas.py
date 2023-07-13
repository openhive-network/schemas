from abc import abstractmethod
import typing
from typing import Any, Dict, Optional

from schemas.__private.fundamental_schemas import Any_, AnyOf, Array, ArrayStrict, Bool, Date, Int, Map, Schema, Str


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
    def __init__(self, **options: Any):
        super().__init__(**options)
        self.__data = Map({
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
                ArrayStrict(Str(), Map({}, allow_additional_properties=True))
            )
        })

    def __setitem__(self, key, schema):
        self.__data[key] = schema

    def __delitem__(self, key):
        del self.__data[key]

    def _define_schema(self) -> Schema:
        return self.__data


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


class EmptyArray(CustomSchema):
    def _define_schema(self) -> Schema:
        return Array(Any_(), maxItems=0)


class EmptyString(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern='')


class FloatAsString(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^(?:(?:[1-9][0-9]*)|0)\.[0-9]+$')


class HardforkVersion(CustomSchema):
    def _define_schema(self) -> Schema:
        return Str(pattern=r'^\d+\.\d+\.\d+$')


class HiveVersion(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'blockchain_version': HardforkVersion(),
            'hive_revision': Hex(minLength=40, maxLength=40),
            'fc_revision': Hex(minLength=40, maxLength=40),
            'chain_id': Sha256(),
            'node_type': Str(pattern=r'^(mainnet|testnet|mirrornet)$')
        })


class HbdExchangeRate(CustomSchema):
    def __init__(self, legacy_format=False):
        """
        A field similar to the `Price` type, with the difference that it is allowed to return a value by this field:
          {
            base: Hbd or Hive
            quote: Hive
          }
        Explanation. When creating a new witness, the `update_witnesses_operation` completes the field
        `hbd_exchange_rate` with default value (base: HIVE, quote: HIVE). Which is inconsistent with the `Price` field.
        This is because the pointer in hive must be set to an existing value. Cannot be a null pointer.
        :param legacy_format: Set to `True` to validate `HbdExchangeRate` in legacy format.
        """
        super().__init__()
        self.__legacy_format = legacy_format

    @property
    def legacy_format(self):
        return self.__legacy_format

    @legacy_format.setter
    def legacy_format(self, value: bool):
        self.__legacy_format = value

    def _define_schema(self) -> Schema:
        return Map({
            'base': AnyOf(AssetHbd(), AssetHive()) if self.__legacy_format is False else AnyOf(LegacyAssetHbd(),
                                                                                               LegacyAssetHive()),
            'quote': AssetHive() if self.__legacy_format is self.__legacy_format is False else LegacyAssetHive(),
        })


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
    def __init__(self, legacy_format=False):
        """
        Valid values for the `Price` structures are:
         - `base: Hbd` and `quote: Hive`,
         - `base: Hive` and `quote: Hbd`.
        :param legacy_format: Set to `True` to validate `Price` in legacy format.
        """
        super().__init__()
        self.__legacy_format = legacy_format

    @property
    def legacy_format(self):
        return self.__legacy_format

    @legacy_format.setter
    def legacy_format(self, value: bool):
        self.__legacy_format = value

    def _define_schema(self) -> Schema:
        return AnyOf(
            Map({
                'base': AssetHbd() if self.__legacy_format is False else LegacyAssetHbd(),
                'quote': AssetHive() if self.__legacy_format is self.__legacy_format is False else LegacyAssetHive(),
            }),
            Map({
                'base': AssetHive() if self.__legacy_format is False else LegacyAssetHive(),
                'quote': AssetHbd() if self.__legacy_format is self.__legacy_format is False else LegacyAssetHbd(),
            }),
        )


class Proposal(CustomSchema):
    def __init__(self, *, legacy_format: [Optional] = False, **options: Any):
        super().__init__(**options)
        self.__legacy_format = legacy_format
        self.__data = Map({
            'id': Int(),
            'proposal_id': Int(),
            'creator': Str(),
            'receiver': Str(),
            'start_date': Date(),
            'end_date': Date(),
            'daily_pay': LegacyAssetHbd() if self.__legacy_format else AssetHbd(),
            'subject': Str(),
            'permlink': Str(),
            'total_votes': Int(),
            'status': Str(),
        })

    def __setitem__(self, key: str, schema: Schema):
        self.__data[key] = schema

    def __delitem__(self, key):
        del self.__data[key]

    @property
    def legacy_format(self):
        return self.__legacy_format

    @legacy_format.setter
    def legacy_format(self, value: bool):
        self.__legacy_format = value
        self.__data['daily_pay'] = LegacyAssetHbd() if self.__legacy_format else AssetHbd()

    def _define_schema(self) -> Schema:
        return self.__data


class PublicKey(CustomSchema):
    def _define_schema(self) -> Schema:
        # See `wif_to_key` implementation in `fc` library for more information about this regex:
        wif_private_key_regex = r'^(?:STM|TST)[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{7,51}$'
        return Str(pattern=wif_private_key_regex)


class RcAccountObject(CustomSchema):
    def __init__(self, *, legacy_format: [Optional] = False, **options: Any):
        super().__init__(**options)
        self.__legacy_format = legacy_format
        self.__data = Map({
            'account': AccountName(),
            'rc_manabar': Manabar(),
            'max_rc_creation_adjustment': LegacyAssetVests() if self.__legacy_format else AssetVests(),
            'max_rc': Int(),
            'delegated_rc': Int(),
            'received_delegated_rc': Int(),
        })

    def __getitem__(self, key):
        return self.__data[key]

    def __setitem__(self, key: str, schema: Schema):
        self.__data[key] = schema

    def __delitem__(self, key):
        del self.__data[key]

    @property
    def legacy_format(self):
        return self.__legacy_format

    @legacy_format.setter
    def legacy_format(self, value: bool):
        self.__legacy_format = value
        self.__data['max_rc_creation_adjustment'] = LegacyAssetVests() if self.__legacy_format else AssetVests()

    def _define_schema(self) -> Schema:
        return self.__data

    def keys(self) -> list:
        return list(self.__data.keys())


class RdDynamicParams(CustomSchema):
    def _define_schema(self) -> Schema:
        return Map({
            'resource_unit': Int(),
            'budget_per_time_unit': Int(),
            'pool_eq': Int(),
            'max_pool_size': Int(),
            'decay_params': Map({
                'decay_per_time_unit': Int(),
                'decay_per_time_unit_denom_shift': Int()
            }),
            'min_decay': Int(),
        })


class Sha256(CustomSchema):
    def _define_schema(self) -> Schema:
        return Hex(minLength=64, maxLength=64)


class Signature(CustomSchema):
    def _define_schema(self) -> Schema:
        return Hex(minLength=130, maxLength=130)


class TransactionId(CustomSchema):
    def _define_schema(self) -> Schema:
        return Hex(minLength=40, maxLength=40)
