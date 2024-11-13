from __future__ import annotations

import difflib

from schemas.jsonrpc_models.generate_jsonrpc_models import FILE_PATH, generate_json_rpc_models_content


def test_jsonrpc_models_file_is_valid() -> None:
    with FILE_PATH.open() as file:
        file_content = file.read()

    generated_content = generate_json_rpc_models_content()

    if file_content != generated_content:
        diffs = difflib.unified_diff(
            file_content.splitlines(),
            generated_content.splitlines(),
        )
        diffs_summary = "\n".join(diffs)

        raise AssertionError(f"Existing jsonrpc_models are incorrect. Differences: {diffs_summary}")
