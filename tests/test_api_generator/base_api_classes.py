from __future__ import annotations

from functools import wraps
from typing import Any, Awaitable, Callable, Final, Self

VALID_RETURN_VALUE: Final[str] = "valid_return_value"


class MockAsyncJsonRpcApiBase:
    """Base class for test generating async api."""

    @classmethod
    def endpoint_jsonrpc(cls, wrapped_function: Callable[..., Awaitable[str]]) -> Callable[..., Awaitable[str]]:
        @wraps(wrapped_function)
        async def impl(*args: Any, **kwargs: Any) -> str:  # NOQA: ARG001
            return VALID_RETURN_VALUE

        return impl


class MockSyncJsonRpcApiBase:
    """Base class for test generating async api."""

    @classmethod
    def endpoint_jsonrpc(cls, wrapped_function: Callable[..., str]) -> Callable[..., str]:
        @wraps(wrapped_function)
        def impl(*args: Any, **kwargs: Any) -> str:  # NOQA: ARG001
            return VALID_RETURN_VALUE

        return impl


class MockAsyncRestApiBase:
    """Base class for test generating async rest api."""

    @classmethod
    def endpoint_rest(cls) -> Self:
        return cls()

    @classmethod
    def get(cls, path: str) -> Callable[[Callable[..., Awaitable[str]]], Callable[..., Awaitable[str]]]:  # NOQA: ARG003
        def decorator(func: Callable[..., Awaitable[str]]) -> Callable[..., Awaitable[str]]:
            @wraps(func)
            async def impl(*args: Any, **kwargs: Any) -> str:  # NOQA: ARG001
                return VALID_RETURN_VALUE

            return impl

        return decorator


class MockSyncRestApiBase:
    """Base class for test generating sync rest api."""

    @classmethod
    def endpoint_rest(cls) -> Self:
        return cls()

    @classmethod
    def get(cls, path: str) -> Callable[[Callable[..., str]], Callable[..., str]]:  # NOQA: ARG003
        def decorator(func: Callable[..., str]) -> Callable[..., str]:
            @wraps(func)
            def impl(*args: Any, **kwargs: Any) -> str:  # NOQA: ARG001
                return VALID_RETURN_VALUE

            return impl

        return decorator
