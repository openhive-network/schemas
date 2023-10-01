from __future__ import annotations

import contextlib
import operator
import re
from abc import ABC, abstractmethod
from copy import deepcopy
from typing import TYPE_CHECKING, Any

from pydantic import ConstrainedStr, StrRegexError, validator
from typing_extensions import Self

from schemas._preconfigured_base_model import PreconfiguredBaseModel
from schemas.fields.assets._validators import validate_nai, validate_precision
from schemas.fields.assets.asset_info import AssetInfo
from schemas.fields.hive_int import HiveInt

if TYPE_CHECKING:
    from collections.abc import Callable

    from pydantic.typing import CallableGenerator


class AssetBase(ABC):
    @staticmethod
    @abstractmethod
    def get_asset_information() -> AssetInfo:
        """This method returns asset details, which we use to perform checks"""

    @abstractmethod
    def _get_amount(self) -> int:
        """Returns raw amount as it is stored on hived side."""

    @abstractmethod
    def clone(self, *, amount: Any | int | str | AssetBase | None = None) -> Self:
        """Returns new instance of self, alternatively with other amount."""

    @abstractmethod
    def _set_amount(self, amount: int) -> None:
        """Sets amount of self to given amount."""

    @classmethod
    @abstractmethod
    def from_legacy(cls, other: str) -> Self:
        """Returns self converted from legacy format."""

    @classmethod
    @abstractmethod
    def from_nai(cls, other: dict[str, str | int]) -> Self:
        """Returns self converted from nai format."""

    def as_nai(self) -> dict[str, str | int]:
        info = self.get_asset_information()
        return {"amount": self._get_amount(), "nai": info.nai, "precision": info.precision}

    def as_legacy(self) -> str:
        return f"{self.pretty_amount()} {self.get_asset_information().symbol[0]}"

    def pretty_amount(self) -> str:
        info = self.get_asset_information()
        return f"{int(self._get_amount()) / 10**info.precision :.{info.precision}f}"

    def __lt__(self, other: Any) -> bool:
        return self._get_amount() < self.__convert_to_asset(other)._get_amount()

    def __le__(self, other: Any) -> bool:
        return self._get_amount() <= self.__convert_to_asset(other)._get_amount()

    def __gt__(self, other: Any) -> bool:
        return self._get_amount() > self.__convert_to_asset(other)._get_amount()

    def __ge__(self, other: Any) -> bool:
        return self._get_amount() >= self.__convert_to_asset(other)._get_amount()

    def __add__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.add)

    def __sub__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.sub)

    def __iadd__(self, other: Any) -> Self:
        new_asset = self.__combine_with(other, operator.add)
        self._set_amount(new_asset._get_amount())
        return self

    def __isub__(self, other: Any) -> Self:
        new_asset = self.__combine_with(other, operator.sub)
        self._set_amount(new_asset._get_amount())
        return self

    def __mul__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.mul)

    def __rmul__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.mul)

    def __imul__(self, other: Any) -> Self:
        new_asset = self.__combine_with(other, operator.mul)
        self._set_amount(new_asset._get_amount())
        return self

    def __truediv__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.truediv)

    def __rtruediv__(self, other: Any) -> Self:
        return self.__combine_with(other, operator.truediv)

    def __itruediv__(self, other: Any) -> Self:
        new_asset = self.__combine_with(other, operator.itruediv)
        self._set_amount(new_asset._get_amount())
        return self

    def __radd__(self, other: Any) -> Self:
        if other == 0:
            return self
        return self.__add__(other)

    def __convert_to_asset(self, other: Any) -> Self:
        with contextlib.suppress(ValueError):
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
        return converted.clone(amount=operator_(self._get_amount(), converted._get_amount()))


class AssetLegacy(ConstrainedStr, AssetBase, ABC):  # type: ignore[misc]
    """Base class for all legacy assets"""

    def _get_amount(self) -> int:
        return self.parse_raw(self)[0]

    @classmethod
    def parse_raw(cls, str_to_parse: str) -> tuple[int, int, str]:
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
        return parsed_amount, precision, symbol

    @classmethod
    def __legacy_regex_validator(cls, value: str) -> str:
        if "-" in value:
            raise ValueError("Asset could not be negative value!")
        regex = cls._get_legacy_regex()
        if regex.match(value) is None:
            raise StrRegexError(pattern=cls._get_pattern(regex))
        return value

    @classmethod
    def __assure_assetlegacy_type(cls, value: str) -> Self:
        """Without this method pydantic will replace AssetLegacy type with str without all helpful methods."""
        return cls(value)  # type: ignore[abstract]

    @classmethod
    def _get_legacy_regex(cls) -> re.Pattern[str]:
        """Returns compiled regex, that simplifies extraction of certain asset properties.

        Groups:
            0 - whole asset
            1 - numeric part of asset (ex.: `1.000`, `12.050`, `0.000001`)
            2 - decimal part of asset (ex.: `000`, `050`, `000001`)
            3 - symbol part of asst (ex. `HIVE`, `TBD`, `VESTS`)

        Returns:
            compiled regex
        """
        info = cls.get_asset_information()
        return re.compile(r"(^\d+\.(\d{" + str(info.precision) + r"})) (" + "|".join(info.symbol) + r")$")

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield from super().__get_validators__()
        yield cls.__legacy_regex_validator
        yield cls.__assure_assetlegacy_type

    def clone(self, *, amount: Any | int | str | AssetBase | None = None) -> Self:
        with contextlib.suppress(ValueError):
            amount = int(amount)  # type: ignore  # in case of AssetNaiAmount

        if amount is None:
            return deepcopy(self)
        if isinstance(amount, str):
            return self.__class__(amount)  # type: ignore[abstract]
        if isinstance(amount, int):
            info = self.get_asset_information()
            return self.from_nai({"amount": int(amount), "nai": info.nai, "precision": info.precision})
        if isinstance(self, AssetBase):
            return self.clone(amount=self._get_amount())
        raise TypeError(f"`{amount}` cannot be used as amount.")

    @classmethod
    def from_legacy(cls, other: str) -> Self:
        return cls(other)  # type: ignore[abstract]

    @classmethod
    def from_nai(cls, other: dict[str, str | int]) -> Self:
        if "nai" not in other or "amount" not in other or "precision" not in other:
            raise ValueError("invalid dict", other)
        info = cls.get_asset_information()
        precision = int(other["precision"])
        nai = other["nai"]
        if nai != info.nai or precision != info.precision:
            raise TypeError(
                f"[{precision=}, {nai=}] is not supported symbol type. Supported are: [{info.precision=}, {info.nai=}]"
            )
        amount = int(other["amount"])
        return cls.from_legacy(f"{int(amount) / 10**info.precision :.{info.precision}f} {info.symbol[0]}")

    def _set_amount(self, amount: int) -> None:  # noqa: ARG002
        assert (
            False  # noqa: B011
        ), "strings are immutable in Python; Use: `some_object.field = some_object.field.clone(amount=new_amount)` instead"


class AssetNaiAmount(HiveInt):
    """
    Amount in HF26 have to be serialized as str, to be properly recognized by c++
    """

    ge = 0

    @classmethod
    def __get_validators__(cls) -> CallableGenerator:
        yield from super().__get_validators__()
        yield cls.__stringify

    @classmethod
    def __stringify(cls, value: int | str) -> str:
        return str(value)


class AssetHF26(PreconfiguredBaseModel, AssetBase, ABC):
    """Base class for all nai asset fields"""

    amount: AssetNaiAmount
    precision: HiveInt
    nai: str

    class Config:
        allow_reuse = True

    @validator("nai", allow_reuse=True)
    @classmethod
    def check_nai(cls, value: Any) -> Any:
        return validate_nai(value=value, asset_info=cls.get_asset_information())

    @validator("precision", allow_reuse=True)
    @classmethod
    def check_precision(cls, value: int) -> int:
        return validate_precision(value=value, asset_info=cls.get_asset_information())

    def _get_amount(self) -> int:
        return int(self.amount)

    def clone(self, *, amount: Any | int | AssetBase | None = None) -> Self:
        if amount is None:
            return self.__class__(**self.as_nai())
        if isinstance(amount, int | AssetBase):
            amount_to_use = amount if isinstance(amount, int) else amount._get_amount()
            return self.__class__(amount=amount_to_use, precision=self.precision, nai=self.nai)
        raise TypeError(f"`{amount}` cannot be used as amount.")

    def as_nai(self) -> dict[str, str | int]:
        """Faster implementation."""
        return super().dict(by_alias=True)

    @classmethod
    def from_nai(cls, other: dict[str, str | int]) -> Self:
        return cls(**other)

    @classmethod
    def from_legacy(cls, other: str) -> Self:
        info = cls.get_asset_information()
        amount, precision, symbol = AssetLegacy.parse_raw(other)
        if precision != info.precision or symbol not in info.symbol:
            raise TypeError(
                f"[{precision=}, {symbol=}] is not supported symbol type. Supported are: [{info.precision=}, {info.symbol=}]"
            )
        return cls(amount=amount, precision=precision, nai=info.nai)

    def _set_amount(self, amount: int) -> None:
        self.amount = AssetNaiAmount(amount)
