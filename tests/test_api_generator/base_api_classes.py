from __future__ import annotations

from functools import wraps
from typing import Any, Awaitable, Callable, Final

VALID_RETURN_VALUE: Final[str] = "valid_return_value"


class MockAsyncApiBase:
    """Base class for test generating async api."""

    @classmethod
    def endpoint(cls, wrapped_function: Callable[..., Awaitable[str]]) -> Callable[..., Awaitable[str]]:
        @wraps(wrapped_function)
        async def impl(*args: Any, **kwargs: Any) -> str:  # NOQA: ARG001
            return VALID_RETURN_VALUE

        return impl


class MockSyncApiBase:
    """Base class for test generating async api."""

    @classmethod
    def endpoint(cls, wrapped_function: Callable[..., str]) -> Callable[..., str]:
        @wraps(wrapped_function)
        def impl(*args: Any, **kwargs: Any) -> str:  # NOQA: ARG001
            return VALID_RETURN_VALUE

        return impl
