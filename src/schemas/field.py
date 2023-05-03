from pydantic import BaseModel


class CellRetrieve(BaseModel):
    pass


class FieldRetrieve(BaseModel):
    cells: list[list[CellRetrieve]]
