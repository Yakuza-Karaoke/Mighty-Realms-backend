from pydantic import BaseModel
from typing import Any

class CellRetrieve(BaseModel):
    pass


class FieldRetrieve(BaseModel):
    cells: list[list[Any]]
