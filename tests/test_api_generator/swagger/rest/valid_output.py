from __future__ import annotations


def get_valid_params_for_sync_balances_endpoint() -> dict[str, type]:
    from .generated_sync.test_api import SortDirection  # type: ignore[import-untyped]

    return {
        "test_name": str,
        "test_name_2": SortDirection | None,
        "return": str,
    }


def get_valid_params_for_async_balances_endpoint() -> dict[str, type]:
    from .generated_async.test_api import SortDirection  # type: ignore[import-untyped]

    return {
        "test_name": str,
        "test_name_2": SortDirection | None,
        "return": str,
    }


def get_valid_params_for_test_2_sync_endpoint() -> dict[str, type]:
    from .generated_sync.test_api import Balance

    return {
        "test_name_3": Balance | None,
        "return": str,
    }


def get_valid_params_for_test_2_async_endpoint() -> dict[str, type]:
    from .generated_async.test_api import Balance

    return {
        "test_name_3": Balance | None,
        "return": str,
    }
