from pydantic import BaseModel

from src.controllers.controller import GameController


class MoveRequest(BaseModel):
    start: tuple[int, int]
    end: tuple[int, int]


class MoveResultRetrieve(BaseModel):
    valid: bool = GameController.validate_move
    start: tuple[int, int] | None = None
    end: tuple[int, int] | None = None
