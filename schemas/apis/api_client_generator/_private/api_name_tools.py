from __future__ import annotations

import re

from schemas.apis.api_client_generator._private.common.models_aliased import ApiDescription
from schemas.apis.api_client_generator.exceptions import InvalidApiNameError


def get_api_name_from_description(api_description: ApiDescription) -> str:
    """
    Extract the API name from the provided API description.

    Args:
        api_description: The API description.

    Returns:
        The name of the API.
    """

    return next(iter(api_description.keys()))


def validate_api_name(api_name: str) -> None:
    """
    Validate the API name.

    Args:
        api_name: The API name to validate.

    Raises:
        ApiNameInvalidError: If the API name is not valid.
    """
    is_valid = bool(re.match(r"^[a-z]+(_[a-z]+)*$", api_name))
    if not is_valid:
        raise InvalidApiNameError(api_name)
