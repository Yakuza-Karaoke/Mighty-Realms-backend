from pydantic import BaseModel
from typing import Any
from enum import Enum

from src.controllers.controller import Unit

class Unit(BaseModel):
    unit_type: str

class UnitRetrieve(BaseModel):
    pass

class Cell(BaseModel):
    terrain_type: str
    unit: dict | None
    build_type: str | None

class CellRetrieve(BaseModel):
    pass

class CellTerrainType(str, Enum):
    empty_field = 'empty_field'
    woods = 'woods'
    

class FieldRetrieve(BaseModel):
    cells: list[list[Any]]
