from __future__ import annotations

import contextlib
import operator
import re
from abc import ABC, ABCMeta, abstractmethod
from decimal import Decimal
from typing import TYPE_CHECKING, Any

import msgspec
from typing_extensions import Self

from schemas.fields.assets._symbol import HbdSymbolType, HiveSymbolType, VestsSymbolType
from schemas.fields.assets._validators import validate_nai, validate_precision
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt, HiveIntFactory
from schemas.fields.serializable import OverrideTypeNameMeta, Serializable

if TYPE_CHECKING:  # nofmt
    from collections.abc import Callable

    AssetNaiAmount = int
else:
    AssetNaiAmount = HiveIntFactory.factory("AssetNaiAmount", msgspec.Meta(ge=0))


class MetaAsset(OverrideTypeNameMeta, ABCMeta):
    """
    This implementation is because of HiddenAssetType which can be used in isinstance context.
    """

    def __instancecheck__(cls: type[Any], instance: Any) -> bool:
        if issubclass(cls, AssetBase):
            instance_t = type(instance)
            if issubclass(instance_t, AssetBase):
                return cls._compare_asset_types(instance_t)
            return False
        return False

    def _compare_asset_types(cls, other: type[AssetBase]) -> bool:
        assert issubclass(cls, AssetBase) and issubclass(other, AssetBase), "Both classes must be AssetBase subclasses"
        if issubclass(cls, HiddenAssetBase) and (not issubclass(other, HiddenAssetBase)):
            other_nai = other.get_asset_information().nai
            return any(other_nai == allowed.get_asset_information().nai for allowed in cls.allowed_types())
        if issubclass(other, HiddenAssetBase) and (not issubclass(cls, HiddenAssetBase)):
            cls_nai = cls.get_asset_information().nai
            return any(cls_nai == allowed.get_asset_information().nai for allowed in other.allowed_types())
        if (not issubclass(other, HiddenAssetBase)) and (not issubclass(cls, HiddenAssetBase)):
            return cls.get_asset_information().nai == other.get_asset_information().nai
        return True


class AssetBase(Serializable, ABC, metaclass=MetaAsset):
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

    @int_amount.setter
    def int_amount(self, value: int) -> None:
        self.__amount = AssetNaiAmount(value)

    def copy(self, *, amount: int | AssetBase | None = None) -> Self:
        if amount is None:
            return self.__class__(amount=self.amount, precision=self.precision(), nai=self.nai())
        if isinstance(amount, (int, AssetBase)):
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
    def from_legacy(cls, other: str) -> Self:
        amount, precision, symbol = cls.parse_raw(other)
        info = cls.get_asset_information()
        if symbol not in info.symbol:
            raise ValueError(f"Invalid symbol! Parsing for: {info.symbol}")
        return cls(amount=amount, precision=precision, nai=info.nai)

    @classmethod
    def from_nai(cls, other: dict[str, Any]) -> Self:
        return cls(**other)

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

    def serialize(self) -> dict[str, str | HiveInt]:
        return self.as_serialized_nai()

    def serialize_as_legacy(self) -> str:
        return self.as_legacy()

    def serialize_as_legacy_testnet(self) -> str:
        return self.as_legacy(testnet=True)

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

        if precision is not None:
            (validate_precision(int(precision), info),)

        if nai is not None:
            validate_nai(nai, info)

    @classmethod
    def __legacy_regex_validator(cls, value: str) -> None:
        if "-" in value:
            raise ValueError("Asset could not be negative value!")
        regex = cls._get_legacy_regex()
        if regex.match(value) is None:
            raise ValueError("Given legacy asset does not match regex")

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


class HiddenAssetBase(AssetBase):
    @classmethod
    @abstractmethod
    def allowed_types(cls) -> list[type[AssetBase]]:
        """
        Returns a list of allowed asset types for this AssetUnion.
        This method should be implemented by subclasses to specify which asset types are allowed.
        """
        raise NotImplementedError("This method should be implemented by subclasses to specify allowed asset types.")


class AssetHive(AssetBase):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return HiveSymbolType.get_asset_information(testnet=False)


class AssetHbd(AssetBase):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return HbdSymbolType.get_asset_information(testnet=False)


class AssetVests(AssetBase):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return VestsSymbolType.get_asset_information(testnet=False)


class AssetTests(AssetHive):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return HiveSymbolType.get_asset_information(testnet=True)


class AssetTbd(AssetHbd):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return HbdSymbolType.get_asset_information(testnet=True)
