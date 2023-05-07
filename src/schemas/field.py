from pydantic import BaseModel
from typing import Any
from enum import Enum

class Unit(BaseModel): #Надо понять, как относятся юнит из контроллера 
    unit_type: Enum    #и этот юнит

class UnitRetrieve(BaseModel):
    unit_type: Enum


class CellTerrainType(str, Enum):
    empty_field = 'empty_field'
    water = 'water'
    rock = 'rock'
    

class Cell(BaseModel):
    terrain_type: CellTerrainType = CellTerrainType.empty_field
    unit: dict | None = None
    build_type: str | None = None

class CellRetrieve(BaseModel):
    terrain_type: CellTerrainType = CellTerrainType.empty_field
    unit: dict | None = None
    build_type: str | None = None


class FieldRetrieve(BaseModel):
    cells: list[list[Cell]]
