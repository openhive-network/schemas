from __future__ import annotations

from schemas.apis.block_api.fundaments_of_responses import EmptyModel


class EnableFastConfirm(EmptyModel):
    pass


class DisableFastConfirm(EmptyModel):
    pass


IsFastConfirmEnabled = bool
