from typing import List, Tuple


class GameController:
    def __init__(self, field: List[List], pNum: int) -> None:
        self.field = field
        self.pNum = pNum
        self._generate_terrain(field)
        for player in range(pNum):
            self._pick_spawn(field, player)
        
    def _generate_terrain(self) -> None:
        pass

    def _pick_spawn(self, player: int) -> Tuple:
        pass

    def _validate_move (self, src: Tuple, dest: Tuple) -> bool:
        pass

    def move_troop(self, src: Tuple, player: int, dest: Tuple) -> None:
        if self._validate_move(src, dest):
            pass
        else: 
            raise Exception()
        