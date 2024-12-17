from __future__ import annotations

from decimal import Decimal
from typing import Any

from typing_extensions import Self

__all__ = [
    "HiveInt",
]


class HiveInt:
    def __init__(self, value: int | str | Self):
        self.value = self._validate(value)

    def __int__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)

    def _validate(self, value: Any) -> int:
        error_template = ValueError("The value could only be int or string that can be converted to int!")
        if isinstance(value, HiveInt):
            return value.value
        if isinstance(value, bool):
            raise error_template
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            try:
                return int(value)
            except ValueError:
                raise error_template
        raise error_template

    def __eq__(self, value: object) -> bool:
        if isinstance(value, int):
            return self.value == value
        if isinstance(value, str):
            return self.value == self._validate(value)
        if isinstance(value, HiveInt):
            return self.value == value.value
        return False

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    def __lt__(self, value: object) -> bool:
        if isinstance(value, int):
            return self.value < value
        if isinstance(value, str):
            return self.value < self._validate(value)
        if isinstance(value, HiveInt):
            return self.value < value.value
        return NotImplemented

    def __le__(self, value: object) -> bool:
        if isinstance(value, int):
            return self.value <= value
        if isinstance(value, str):
            return self.value <= self._validate(value)
        if isinstance(value, HiveInt):
            return self.value <= value.value
        return NotImplemented

    def __gt__(self, value: object) -> bool:
        if isinstance(value, int):
            return self.value > value
        if isinstance(value, str):
            return self.value > self._validate(value)
        if isinstance(value, HiveInt):
            return self.value > value.value
        return NotImplemented

    def __ge__(self, value: object) -> bool:
        if isinstance(value, int):
            return self.value >= value
        if isinstance(value, str):
            return self.value >= self._validate(value)
        if isinstance(value, HiveInt):
            return self.value >= value.value
        return NotImplemented

    def __mul__(self, value: object) -> object:
        if isinstance(value, int):
            return HiveInt(self.value * value)
        if isinstance(value, str):
            return self.value * self._validate(value)
        if isinstance(value, HiveInt):
            return HiveInt(self.value * value.value)
        return NotImplemented

    def __truediv__(self, value: object) -> object:
        if isinstance(value, int):
            if value == 0:
                raise ZeroDivisionError("division by zero")
            return HiveInt(int(self.value / value))
        if isinstance(value, HiveInt):
            if value.value == 0:
                raise ZeroDivisionError("division by zero")
            return HiveInt(int(self.value / value.value))
        return NotImplemented

    def __rmul__(self, value: object) -> object:
        return self.__mul__(value)

    def __pow__(self, value: Any, modulo: Any | None = None) -> HiveInt | Decimal:
        if isinstance(value, int):
            result = pow(self.value, value, modulo) if modulo else pow(self.value, value)
            return HiveInt(result)
        if isinstance(value, HiveInt):
            result = pow(self.value, value.value, modulo) if modulo else pow(self.value, value.value)
            return HiveInt(result)
        if isinstance(value, Decimal):
            return Decimal(self.value) ** value
        raise TypeError(f"Unsupported type: {type(value)}")
