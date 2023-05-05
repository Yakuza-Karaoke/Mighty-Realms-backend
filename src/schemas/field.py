from pydantic import BaseModel
from typing import Any
from enum import Enum

class Unit(BaseModel): #Надо понять, как относятся юнит из контроллера и этот юнит
    unit_type: str

class UnitRetrieve(BaseModel):
    unit: Unit

class Cell(BaseModel):
    terrain_type: str
    unit: dict | None
    build_type: str | None

class CellRetrieve(BaseModel): #Доделать ретривы, с учётом фронта
    cell: Cell

class CellTerrainType(str, Enum): #Не уверен насчёт правильности
    empty_field = 'empty_field'
    water = 'water'
    rock = 'rock'

class FieldRetrieve(BaseModel):
    cells: list[list[Any]]
