from __future__ import annotations

from typing import Any


class GameController:
    def __init__(self, field: int, p_num: int = 2) -> None:
        self.field: list[list[Any]] = self._generate_terrain(field)
        self.p_num = p_num
        for player in range(p_num):
            self.capital = self._pick_spawn(p_num)
        
    def _generate_terrain(self, field_size: int) -> list[list[Any]]:
        return [[0 for _ in range(field_size)] for _ in range(field_size)]

    def _pick_spawn(self, player: int) -> tuple[int, int]:
        pass

    def _validate_move(self, troop: Unit, src: tuple[int, int], dest: tuple[int, int]) -> bool:
        pass

    def move_troop(self, player: int, src: tuple[int, int], dest: tuple[int, int]) -> None:
        if self._validate_move(..., src, dest):
            pass
        else: 
            raise Exception()
        
    def _attack(self, src: tuple[int, int], dst: tuple[int, int]):
        pass
        

class Unit:
    def __init__(self, hp: int, attack: int, attack_range: int, defence: int, movespeed: int) -> None:
        self.hp = hp
        self.attack = attack
        self.atck_range = attack_range
        self.defence = defence
        self.movespeed = movespeed
