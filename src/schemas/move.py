from pydantic import BaseModel


class MoveRequest(BaseModel):
    start: tuple[int, int]
    end: tuple[int, int]


class MoveResultRetrieve(BaseModel):
    valid: bool = True
    start: tuple[int, int] | None = None
    end: tuple[int, int] | None = None
