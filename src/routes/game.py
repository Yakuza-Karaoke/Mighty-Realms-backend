from fastapi import APIRouter, Body

from src.schemas.field import FieldRetrieve
from src.schemas.move import MoveRequest, MoveResultRetrieve
from src.controllers.controller import GameController



router = APIRouter(prefix='/game')


@router.get(
    '/field',
    response_model=FieldRetrieve,
    description='Показать текущее игровое поле',
)
async def get_field():
    return FieldRetrieve(cells=GameController.get_field())


@router.post(
    '/move',
    response_model=MoveResultRetrieve,
    description='Сделать ход',
)
async def perform_move(
    player_id: int,
    move: MoveRequest = Body(..., embed=True),
):
    return MoveResultRetrieve()
