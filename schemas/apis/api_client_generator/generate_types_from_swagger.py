from __future__ import annotations

from pathlib import Path

from datamodel_code_generator import DataModelType, InputFileType, generate


def generate_types_from_swagger(
    openapi_api_definition: str | Path,
    output: str | Path,
) -> None:
    """
    Generate types defined in Swagger.

    Args:
        openapi_api_definition: The OpenAPI JSON definition file path.
        output: The output file / package path where the generated types will be saved.

    Raises:
        FileNotFoundError: If the OpenAPI definition file does not exist.
    """
    openapi_file = openapi_api_definition if isinstance(openapi_api_definition, Path) else Path(openapi_api_definition)
    output = output if isinstance(output, Path) else Path(output)

    if not openapi_file.exists():
        raise FileNotFoundError(f"File {openapi_file} does not exist.")

    generate(  # generation of types available in the API definition
        openapi_file,
        output=output,
        output_model_type=DataModelType.MsgspecStruct,
        input_file_type=InputFileType.OpenAPI,
        use_field_description=True,
        use_standard_collections=True,
    )
