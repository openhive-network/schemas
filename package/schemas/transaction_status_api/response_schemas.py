from schemas.predefined import *

find_transaction = Map({
    "block_num": Int(),
    "status": Str(
        enum=[
            "expired_reversible",
            "expired_reversible",
            "too_old",
            "within_irreversible_block",
            "within_mempool",
            "within_reversible_block",
            "unknown"
        ])

}, required_keys=["status"])
