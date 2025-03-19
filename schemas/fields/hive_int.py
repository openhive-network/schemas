from __future__ import annotations

from decimal import Decimal
from typing import Any

from typing_extensions import Self

__all__ = [
    "HiveInt",
]


class HiveInt:
    def __init__(self, value: int | str | Self):
        self._value = self._validate(value)

    @property
    def value(self) -> int:
        return self._value

    @property
    def safe_int_value(self) -> int | str:
        max_safe_int = (2**53) - 1
        min_safe_int = -(2**53) + 1
        if self.value >= min_safe_int and self.value <= max_safe_int:
            return self._value
        return str(self._value)

    def __int__(self) -> int:
        return self._value

    def __str__(self) -> str:
        return str(self._value)

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

    def _convert_value(self, value: Any) -> int:
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            return self._validate(value)
        if isinstance(value, HiveInt):
            return value.value
        raise NotImplementedError(f"Cannot compare with {type(value)}")

    def __eq__(self, value: object) -> bool:
        return self.value == self._convert_value(value)

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    def __lt__(self, value: object) -> bool:
        return self.value < self._convert_value(value)

    def __le__(self, value: object) -> bool:
        return self.value <= self._convert_value(value)

    def __gt__(self, value: object) -> bool:
        return self.value > self._convert_value(value)

    def __ge__(self, value: object) -> bool:
        return self.value >= self._convert_value(value)

    def __mul__(self, value: object) -> object:
        return HiveInt(self._value * self._convert_value(value))

    def __truediv__(self, value: object) -> object:
        if isinstance(value, int):
            if value == 0:
                raise ZeroDivisionError("division by zero")
            return HiveInt(int(self._value / value))
        if isinstance(value, HiveInt):
            if value.value == 0:
                raise ZeroDivisionError("division by zero")
            return HiveInt(int(self._value / value.value))
        return NotImplemented

    def __rtruediv__(self, value: object) -> object:
        if isinstance(value, int):
            if self._value == 0:
                raise ZeroDivisionError("division by zero")
            return HiveInt(int(value / self._value))
        return NotImplemented

    def __add__(self, value: object) -> object:
        return HiveInt(self._value + self._convert_value(value))

    def __sub__(self, value: object) -> object:
        return HiveInt(self._value - self._convert_value(value))

    def __pow__(self, value: Any, modulo: Any | None = None) -> HiveInt | Decimal:
        if isinstance(value, int):
            result = pow(self._value, value, modulo) if modulo else pow(self._value, value)
            return HiveInt(result)
        if isinstance(value, HiveInt):
            result = pow(self._value, value.value, modulo) if modulo else pow(self._value, value.value)
            return HiveInt(result)
        if isinstance(value, Decimal):
            return Decimal(self._value) ** value
        raise TypeError(f"Unsupported type: {type(value)}")

    def __radd__(self, value: object) -> object:
        return self.__add__(value)

    def __rsub__(self, value: object) -> object:
        if isinstance(value, int):
            return HiveInt(value - self._value)
        return NotImplemented

    def __rmul__(self, value: object) -> object:
        return self.__mul__(value)
