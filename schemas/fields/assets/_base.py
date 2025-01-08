from __future__ import annotations

from abc import ABC, abstractmethod
import contextlib
import operator
import re
# from abc import ABC, abstractmethod
from copy import deepcopy
from typing import TYPE_CHECKING, Annotated, Any

import msgspec
from pydantic import ConstrainedStr, StrRegexError, validator
from typing_extensions import Self

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._validators import validate_nai, validate_precision
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt

if TYPE_CHECKING:
    from collections.abc import Callable

    from pydantic.typing import CallableGenerator

class AssetNaiAmount(HiveInt):
    def _validate(self):
        assert int(self) >= 0

class AssetBase(ABC):
    def __init__(self, amount: AssetNaiAmount, precision: HiveInt | None = None, nai: str | None = None):
        self.__amount = amount
        self.validate(precision, nai)

    @staticmethod
    @abstractmethod
    def get_asset_information() -> AssetInfo:
        """This method returns asset details, which we use to perform checks"""

    @property
    def symbol(self) -> tuple[str, str]:
        return self.get_asset_information().symbol

    @property
    def precision(self) -> HiveInt:
        return self.get_asset_information().precision

    @property
    def nai(self) -> str:
        return self.get_asset_information().nai

    @property
    def amount(self) -> AssetNaiAmount:
        return self.__amount

    @amount.setter
    def amount(self, value: AssetNaiAmount) -> None:
        self.__amount = value

    @property
    def iamount(self) -> int:
        return int(self.amount)

    @iamount.setter
    def iamount(self, value: int) -> None:
        self.__amount = AssetNaiAmount(value)

    def clone(self, *, amount: Any | int | AssetBase | None = None) -> Self:
        if amount is None:
            return self.__class__(amount=self.amount, precision=self.precision, nai=self.nai)
        if isinstance(amount, int | AssetBase):
            amount_to_use = amount if isinstance(amount, int) else amount.amount
            return self.__class__(amount=AssetNaiAmount(amount_to_use), precision=self.precision, nai=self.nai)
        raise TypeError(f"`{amount}` cannot be used as amount.")

    @classmethod
    def _get_legacy_regex(cls) -> re.Pattern[str]: # use_asset_info: AssetInfo | None = None) -> re.Pattern[str]:
        """Returns compiled regex, that simplifies extraction of certain asset properties.

        Groups:
            0 - whole asset
            1 - numeric part of asset (ex.: `1.000`, `12.050`, `0.000001`)
            2 - decimal part of asset (ex.: `000`, `050`, `000001`)
            3 - symbol part of asst (ex. `HIVE`, `TBD`, `VESTS`)

        Returns:
            compiled regex
        """
        return re.compile(r"(^\d+\.(\d{" + str(cls.precision) + r"})) (" + "|".join(cls.symbol) + r")$")

    @classmethod
    def __legacy_regex_validator(cls, value: str) -> str: # *, use_asset_info: AssetInfo | None = None) -> str:
        if "-" in value:
            raise ValueError("Asset could not be negative value!")
        regex = cls._get_legacy_regex()
        if regex.match(value) is None:
            raise Exception("Given legacy asset does not match regex")
        return value

    @classmethod
    def parse_raw(cls, str_to_parse: str) -> tuple[AssetNaiAmount, HiveInt, str]: # *, use_asset_info: AssetInfo | None = None) -> tuple[int, int, str]:
        """Parses given str as if it is legacy asset.

        Arguments:
            str_to_parse -- string to be parsed

        Returns:
            Tuple with 3 values in following order: amount, precision, symbol
        """
        cls.__legacy_regex_validator(str_to_parse)
        matched = cls._get_legacy_regex().match(str_to_parse)
        assert matched is not None
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

    def as_nai(self) -> dict[str, Any]:
        info = self.get_asset_information()
        return {
            "amount": self.iamount,
            "nai": info.nai,
            "precision": info.precision,
        }

    def token(self) -> str:
        return self.get_asset_information().get_symbol()

    def as_legacy(self, *, testnet: bool = False) -> str:
        return f"{self.pretty_amount()} {self.get_asset_information().get_symbol(testnet=testnet)}"

    def as_float(self) -> float:
        info = self.get_asset_information()
        return float(self.iamount / (10 ** int(info.precision)))

    def pretty_amount(self) -> str:
        info = self.get_asset_information()
        return f"{self.as_float() :.{info.precision}f}"

    @classmethod
    def validate(cls, precision: HiveInt | None, nai: str | None) -> None:
        info = cls.get_asset_information()

        if precision is not None:
            validate_precision(int(precision), info),

        if nai is not None:
            validate_nai(nai, info)

    def __eq__(self, other: Any) -> bool:
        asset = self.__convert_to_asset(other)
        return (
            asset.get_asset_information() == self.get_asset_information() and self.iamount == asset.iamount
        )

    def __lt__(self, other: Any) -> bool:
        return self.iamount < self.__convert_to_asset(other).iamount

    def __le__(self, other: Any) -> bool:
        return self.iamount <= self.__convert_to_asset(other).iamount

    def __gt__(self, other: Any) -> bool:
        return self.iamount > self.__convert_to_asset(other).iamount

    def __ge__(self, other: Any) -> bool:
        return self.iamount >= self.__convert_to_asset(other).iamount

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

    def __convert_to_asset(self, other: Any) -> Self:
        with contextlib.suppress(ValueError, TypeError):
            other = int(other)

        if isinstance(other, int):
            return self.clone(amount=other)
        if isinstance(other, dict):
            return self.from_nai(other)
        if isinstance(other, str):
            return self.from_legacy(other)
        if isinstance(other, AssetBase):
            return other.clone()  # type: ignore[return-value]
        raise TypeError(f"`{other}` cannot be used as asset.")

    def __combine_with(self, other: AssetBase | int, operator_: Callable[[int, int], int]) -> Self:
        converted = self.__convert_to_asset(other)
        return converted.clone(amount=int(float(operator_(self.iamount, converted.iamount))))

class AssetHive(AssetBase):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return AssetInfo(precision=HiveInt(3), nai="@@000000021", symbol=("HIVE", "TESTS"))

class AssetHbd(AssetBase):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return AssetInfo(precision=HiveInt(3), nai="@@000000013", symbol=("HBD", "TBD"))


class AssetVest(AssetBase):
    @staticmethod
    def get_asset_information() -> AssetInfo:
        return AssetInfo(precision=HiveInt(6), nai="@@000000037", symbol=("VESTS", "VESTS"))
