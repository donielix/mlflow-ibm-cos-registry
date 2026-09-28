from pathlib import Path
from typing import Dict, Union

from pydantic import AfterValidator, Field
from typing_extensions import Annotated


def validate_model_path(v: Union[str, Path]) -> str:
    path_obj = Path(v) if isinstance(v, str) else v
    if not path_obj.exists():
        raise ValueError(f"Path {v} does not exist.")
    return str(path_obj.resolve())


NonEmptyStr = Annotated[str, Field(min_length=1)]
ModelPath = Annotated[Union[str, Path], AfterValidator(validate_model_path)]
NonEmptyDict = Annotated[Dict[NonEmptyStr, NonEmptyStr], Field(min_length=1)]
