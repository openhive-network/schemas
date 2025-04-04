from __future__ import annotations

from schemas.apis.api_client_generator.exceptions import RunningScriptWithoutAppropriateFlagError


def check_whether_was_ran_as_script() -> None:
    """Check if the script is run as a script. If so, raise an error."""

    if __name__ == "__main__":
        if __package__ is None:
            raise RunningScriptWithoutAppropriateFlagError
