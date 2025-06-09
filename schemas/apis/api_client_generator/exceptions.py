from __future__ import annotations


class ApiClientGeneratorError(Exception):
    """Base class for all exceptions raised by the ApiClientGenerator."""


class InvalidApiNameError(ApiClientGeneratorError):
    """Exception raised when the API name is invalid."""

    def __init__(self, api_name: str) -> None:
        self.message = f"Invalid API name: {api_name} provided."
        self.api_name = api_name
        super().__init__(self.message)


class InvalidApiDefinitionsAmountError(ApiClientGeneratorError):
    """Exception raised when more than one or none API definition is passed to a single generator."""

    def __init__(self) -> None:
        self.message = "More than one or none API definition passed to the single api client generator."
        super().__init__(self.message)


class RunningScriptWithoutAppropriateFlagError(ApiClientGeneratorError):
    def __init__(self) -> None:
        self.message = (
            "Seems like you are trying to run the script without the -m flag. Please run your generation script like this:\n"
            "python -m your_script_name.py"
        )
        super().__init__(self.message)


class EndpointParamsIsNotMsgspecStructError(ApiClientGeneratorError):
    """Exception raised when the endpoint parameters are not a msgspec struct."""

    def __init__(self, endpoint_name: str = "any") -> None:
        self.message = f"Params for {endpoint_name} endpoint must be a msgspec struct."
        self.endpoint_name = endpoint_name
        super().__init__(self.message)


class ClassPassedByStrWithoutSourceError(ApiClientGeneratorError):
    """Exception raised when a class is passed by string without its source."""

    def __init__(self) -> None:
        self.message = "You've probably passed a class by string and not provided class source."
        super().__init__(self.message)
