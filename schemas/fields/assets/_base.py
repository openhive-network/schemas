"""
Assets in a fixed JSON form - the type decides the form (msgspec decodes by the declared type and encodes by the type of
the value, see `schemas.decoders` and `schemas.encoders`):

- `AssetHive`, `AssetHbd`, `AssetVests` (and the unions `AssetHiveOrHbd`, `AssetHiveOrVests`, `AnyAsset`) - NAI form
  (`{"amount": "1000", "precision": 3, "nai": "@@000000021"}`),
- `LegacyAssetHive`, `LegacyAssetHbd`, `LegacyAssetVests` (and the unions `LegacyAssetHiveOrHbd`,
  `LegacyAssetHiveOrVests`, `LegacyAnyAsset`) - legacy form (`"1.000 HIVE"`).

msgspec allows only one custom type in a union and requires a decoded value to be an instance of the declared type, so
unions of assets are base classes of their members.
"""

from __future__ import annotations

import contextlib
import inspect
import operator
import re
from abc import ABC, ABCMeta, abstractmethod
from dataclasses import replace
from decimal import Decimal
from typing import TYPE_CHECKING, Any, ClassVar, Final, Self

import msgspec

from schemas.errors import FieldValidationError
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt, HiveIntFactory
from schemas.fields.serializable import OverrideTypeNameMeta, Serializable

if TYPE_CHECKING:  # nofmt
    from collections.abc import Callable

    AssetNaiAmount = int
else:
    AssetNaiAmount = HiveIntFactory.factory("AssetNaiAmount", msgspec.Meta(ge=0))

_HIVE_INFO: Final[AssetInfo] = AssetInfo(
    precision=HiveInt(3), nai="@@000000021", symbol=("HIVE", "TESTS"), testnet=False
)
_HBD_INFO: Final[AssetInfo] = AssetInfo(precision=HiveInt(3), nai="@@000000013", symbol=("HBD", "TBD"), testnet=False)
_VESTS_INFO: Final[AssetInfo] = AssetInfo(
    precision=HiveInt(6), nai="@@000000037", symbol=("VESTS", "VESTS"), testnet=False
)
_LEGACY_ASSET_REGEX: Final[re.Pattern[str]] = re.compile(r"^\d+\.\d+ ([A-Z]+)$")


class _AssetMeta(OverrideTypeNameMeta, ABCMeta):
    def __instancecheck__(cls, instance: object) -> bool:
        # testnet assets (`AssetTests`, `AssetTbd`) are the same assets as the mainnet ones - only their legacy symbol
        # differs
        mainnet_asset = cls.__dict__.get("_testnet_of")
        return super().__instancecheck__(instance) or (
            mainnet_asset is not None and isinstance(instance, mainnet_asset)
        )


class AssetBase(Serializable, ABC, metaclass=_AssetMeta):
    def __init__(self, amount: int, precision: HiveInt | None = None, nai: str | None = None):
        self.__amount = AssetNaiAmount(amount)
        self.validate(precision, nai)

    def __eq__(self, other: Any) -> bool:
        try:
            asset = self.__convert_to_asset(other)
        except (ValueError, TypeError):
            return False
        return asset.get_asset_information() == self.get_asset_information() and self.int_amount == asset.int_amount

    def __lt__(self, other: Any) -> bool:
        return self.int_amount < self.__convert_to_asset(other).int_amount

    def __le__(self, other: Any) -> bool:
        return self.int_amount <= self.__convert_to_asset(other).int_amount

    def __gt__(self, other: Any) -> bool:
        return self.int_amount > self.__convert_to_asset(other).int_amount

    def __ge__(self, other: Any) -> bool:
        return self.int_amount >= self.__convert_to_asset(other).int_amount

    def __add__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.add)

    def __sub__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.sub)

    def __iadd__(self, other: Any) -> Self:
        new_asset = self.__combine_with(other, operator.add)
        self.amount = new_asset.amount
        return self

    def __isub__(self, other: Any) -> Self:
        new_asset = self.__combine_with(other, operator.sub)
        self.amount = new_asset.amount
        return self

    def __mul__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.mul)

    def __rmul__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.mul)

    def __imul__(self, other: Any) -> Self:
        new_asset = self.__combine_with(other, operator.mul)
        self.amount = new_asset.amount
        return self

    def __truediv__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.truediv)

    def __rtruediv__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.truediv)

    def __itruediv__(self, other: Any) -> Self:
        new_asset = self.__combine_with(other, operator.itruediv)
        self.amount = new_asset.amount
        return self

    def __radd__(self, other: Any) -> Self:
        if other == 0:
            return self
        return self.__add__(other)

    @staticmethod
    @abstractmethod
    def get_asset_information() -> AssetInfo:
        """This method returns asset details, which we use to perform checks"""

    @classmethod
    def symbol(cls) -> tuple[str, str]:
        return cls.get_asset_information().symbol

    @classmethod
    def precision(cls) -> HiveInt:
        return cls.get_asset_information().precision

    @classmethod
    def nai(cls) -> str:
        return cls.get_asset_information().nai

    @property
    def amount(self) -> AssetNaiAmount:
        return self.__amount

    @amount.setter
    def amount(self, value: AssetNaiAmount) -> None:
        self.__amount = value

    @property
    def int_amount(self) -> int:
        return int(self.amount)

    def copy(self, *, amount: int | AssetBase | None = None) -> Self:
        if amount is None:
            return self.__class__(amount=self.amount, precision=self.precision(), nai=self.nai())
        if isinstance(amount, int | AssetBase):
            amount_to_use = amount if isinstance(amount, int) else amount.amount
            return self.__class__(amount=AssetNaiAmount(amount_to_use), precision=self.precision(), nai=self.nai())
        raise TypeError(f"`{amount}` cannot be used as amount.")

    @classmethod
    def _get_legacy_regex(cls) -> re.Pattern[str]:
        """Returns compiled regex, that simplifies extraction of certain asset properties.

        Groups:
            0 - whole asset
            1 - numeric part of asset (ex.: `1.000`, `12.050`, `0.000001`)
            2 - decimal part of asset (ex.: `000`, `050`, `000001`)
            3 - symbol part of asset (ex. `HIVE`, `TBD`, `VESTS`)

        Returns:
            compiled regex
        """
        return re.compile(r"(^\d+\.(\d{" + str(cls.precision()) + r"})) (" + "|".join(cls.symbol()) + r")$")

    @classmethod
    def parse_raw(cls, str_to_parse: str) -> tuple[AssetNaiAmount, HiveInt, str]:
        """Parses given str as if it is legacy asset.

        Arguments:
            str_to_parse -- string to be parsed

        Returns:
            Tuple with 3 values in following order: amount, precision, symbol
        """
        cls.__legacy_regex_validator(str_to_parse)
        matched = cls._get_legacy_regex().match(str_to_parse)
        assert matched is not None, "Regex should match the given string, but it did not."
        parsed_amount = int(matched.group(1).replace(".", ""))
        precision = len(matched.group(2))
        symbol = matched.group(3)
        return AssetNaiAmount(parsed_amount), HiveInt(precision), symbol

    @classmethod
    def deserialize(cls, value: object) -> Self:
        """Create the asset from its JSON form - NAI form (legacy assets override it)."""
        return cls.from_nai(value)

    @classmethod
    def from_legacy(cls, other: str) -> Self:
        amount, precision, symbol = cls.parse_raw(other)
        info = cls.get_asset_information()
        if symbol not in info.symbol:
            raise FieldValidationError(f"Invalid symbol! Parsing for: {info.symbol}")
        return cls(amount=amount, precision=precision, nai=info.nai)

    @classmethod
    def from_nai(cls, other: object) -> Self:
        if not isinstance(other, dict):
            raise FieldValidationError(f"Expected asset in NAI form (object), got: `{other}`")
        if not inspect.isabstract(cls):
            return cls(**other)
        for asset in _NAI_ASSETS:
            if issubclass(asset, cls) and asset.nai() == other.get("nai"):
                return asset(**other)
        members = [asset.__name__ for asset in _NAI_ASSETS if issubclass(asset, cls)]
        raise FieldValidationError(f"Expected one of {members}, got: `{other}`")

    def as_legacy_asset(self) -> LegacyAnyAsset:
        """Return the asset in the legacy form (e.g. to put it into a legacy operation)."""
        if isinstance(self, LegacyAnyAsset):
            return self
        info = self.get_asset_information()
        for asset in _LEGACY_ASSETS:
            asset_info = asset.get_asset_information()
            if asset_info.nai == info.nai and asset_info.testnet == info.testnet:
                return asset(amount=self.amount)
        raise AssertionError(f"No legacy asset for {type(self)}")

    def as_nai(self) -> dict[str, AssetNaiAmount | str | HiveInt]:
        info = self.get_asset_information()
        return {
            "amount": self.amount,
            "nai": info.nai,
            "precision": info.precision,
        }

    def as_serialized_nai(self) -> dict[str, str | HiveInt]:
        info = self.get_asset_information()
        return {
            "amount": str(self.amount),
            "nai": info.nai,
            "precision": info.precision,
        }

    def serialize(self) -> dict[str, str | HiveInt] | str:
        """Return the JSON form of the asset - NAI form (legacy assets override it with the legacy form)."""
        return self.as_serialized_nai()

    def as_float(self) -> float:
        info = self.get_asset_information()
        return float(self.amount / (10**info.precision))

    def token(self, testnet: bool | None = None) -> str:
        return self.get_asset_information().get_symbol(testnet=testnet)

    def as_legacy(self, *, testnet: bool | None = None) -> str:
        return f"{self.pretty_amount()} {self.token(testnet=testnet)}"

    def as_decimal(self) -> Decimal:
        info = self.get_asset_information()
        return Decimal(self.int_amount) / (Decimal(10) ** int(info.precision))

    def pretty_amount(self) -> str:
        info = self.get_asset_information()
        return f"{self.as_decimal() :.{info.precision}f}"

    @classmethod
    def validate(cls, precision: HiveInt | None, nai: str | None) -> None:
        info = cls.get_asset_information()
        if precision is not None and int(precision) != info.precision:
            raise FieldValidationError("Invalid decimals")
        if nai is not None and nai != info.nai:
            raise FieldValidationError("Invalid nai !")

    @classmethod
    def __legacy_regex_validator(cls, value: str) -> None:
        if not isinstance(value, str):
            raise FieldValidationError(f"Legacy asset must be a string, got: `{type(value)}`")
        if "-" in value:
            raise FieldValidationError("Asset could not be negative value!")
        regex = cls._get_legacy_regex()
        if regex.match(value) is None:
            raise FieldValidationError("Given legacy asset does not match regex")

    def __convert_to_asset(self, other: Any) -> Self:
        with contextlib.suppress(ValueError, TypeError):
            other = int(other)

        if isinstance(other, int):
            return self.copy(amount=other)
        if isinstance(other, dict):
            return self.from_nai(other)
        if isinstance(other, str):
            return self.from_legacy(other)
        if isinstance(other, AssetBase):
            return other.copy()  # type: ignore[return-value]
        raise TypeError(f"`{other}` cannot be used as asset.")

    def __combine_with(self, other: AssetBase | int, operator_: Callable[[int, int], int]) -> Self:
        converted = self.__convert_to_asset(other)
        return converted.copy(amount=int(float(operator_(self.int_amount, converted.int_amount))))

    def __hash__(self) -> int:
        return hash(self.as_serialized_nai())


class AnyAsset(AssetBase):
    """HIVE, HBD or VESTS."""


class AssetHiveOrHbd(AnyAsset):
    """HIVE or HBD."""


class AssetHiveOrVests(AnyAsset):
    """HIVE or VESTS."""


class AssetHive(AssetHiveOrHbd, AssetHiveOrVests):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return _HIVE_INFO


class AssetHbd(AssetHiveOrHbd):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return _HBD_INFO


class AssetVests(AssetHiveOrVests):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return _VESTS_INFO


class AssetTests(AssetHive):
    _testnet_of: ClassVar[type[AssetBase]] = AssetHive

    @staticmethod
    def get_asset_information() -> AssetInfo:
        return replace(_HIVE_INFO, testnet=True)


class AssetTbd(AssetHbd):
    _testnet_of: ClassVar[type[AssetBase]] = AssetHbd

    @staticmethod
    def get_asset_information() -> AssetInfo:
        return replace(_HBD_INFO, testnet=True)


class LegacyAnyAsset(AnyAsset):
    """HIVE, HBD or VESTS in the legacy form."""

    @classmethod
    def deserialize(cls, value: object) -> Self:
        return cls.from_legacy(value)

    @classmethod
    def from_legacy(cls, other: object) -> Self:
        # the symbol decides the asset - also the testnet one, so the asset is serialized back with the same symbol
        if not isinstance(other, str) or (matched := _LEGACY_ASSET_REGEX.match(other)) is None:
            raise FieldValidationError(f"Expected asset in legacy form (e.g. `1.000 HIVE`), got: `{other}`")
        symbols = {_legacy_symbol(asset): asset for asset in _LEGACY_ASSETS if issubclass(asset, cls)}
        if matched.group(1) not in symbols:
            raise FieldValidationError(f"Expected asset with one of symbols {list(symbols)}, got: `{other}`")
        return super(LegacyAnyAsset, symbols[matched.group(1)]).from_legacy(other)

    def serialize(self) -> str:
        return self.as_legacy()


class LegacyAssetHiveOrHbd(LegacyAnyAsset, AssetHiveOrHbd):
    """HIVE or HBD in the legacy form."""


class LegacyAssetHiveOrVests(LegacyAnyAsset, AssetHiveOrVests):
    """HIVE or VESTS in the legacy form."""


class LegacyAssetHive(LegacyAssetHiveOrHbd, LegacyAssetHiveOrVests, AssetHive):
    pass


class LegacyAssetHbd(LegacyAssetHiveOrHbd, AssetHbd):
    pass


class LegacyAssetVests(LegacyAssetHiveOrVests, AssetVests):
    pass


class LegacyAssetTests(LegacyAssetHive):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return replace(_HIVE_INFO, testnet=True)


class LegacyAssetTbd(LegacyAssetHbd):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return replace(_HBD_INFO, testnet=True)


def _legacy_symbol(asset: type[AssetBase]) -> str:
    info = asset.get_asset_information()
    return info.symbol[int(info.testnet)]


_NAI_ASSETS: Final[tuple[type[AssetBase], ...]] = (AssetHive, AssetHbd, AssetVests)
_LEGACY_ASSETS: Final[tuple[type[LegacyAnyAsset], ...]] = (
    LegacyAssetHive,
    LegacyAssetTests,
    LegacyAssetHbd,
    LegacyAssetTbd,
    LegacyAssetVests,
)
