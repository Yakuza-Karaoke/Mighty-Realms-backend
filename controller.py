from typing import List, Tuple


class GameController:
    def __init__(self, field: int, pNum: int = 2) -> None:
        self.field = self._generate_terrain(field)
        self.pNum = pNum
        for player in range(pNum):
            self.capital = self._pick_spawn(field, player)
        
    def _generate_terrain(self, field: int) -> List[List]:
        return [[0 for _ in range(field)] for _ in range(field)]

    def _pick_spawn(self, player: int) -> Tuple:
        pass

    def _validate_move (self, troop: Unit,  src: Tuple, dest: Tuple) -> bool:
        pass

    def move_troop(self, src: Tuple, player: int, dest: Tuple) -> None:
        if self._validate_move(src, dest):
            pass
        else: 
            raise Exception()
        
    def _attack(self, src:Tuple, dst: Tuple):
        pass
        

class Unit:
    def __init__(self, hp: int, attack: int, atck_range: int, defence: int, movespeed: int) -> None:
        self,hp = hp
        self.attack = attack
        self.atck_range = atck_range
        self.defence = defence
        self.movespeed = movespeed

    