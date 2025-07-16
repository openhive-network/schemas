from __future__ import annotations


def create_method_name(url_path: str) -> str:
    """
    Create a method name for a REST API client based on the URL path.

    Args:
        url_path: The URL path of the endpoint, e.g., "/name_of_endpoint/{some_param}".

    Returns:
        url_path: The constructed method name.

    Example:
        my_url_path = "/name_of_endpoint/{some_param}/path_part"
        create_method_name(my_url_path)
        >>> "name_of_endpoint_path_part"
    """
    split_path = url_path.split("/")
    split_path = [part for part in split_path if part and not part.startswith("{") and not part.endswith("}")]

    return "_".join(split_path).replace("-", "_")
