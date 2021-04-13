from __future__ import annotations
from typing import TYPE_CHECKING

from direction import Direction
from enemy import Enemy
from entity_dictionary import EntityDictionary
from wall import Wall

if TYPE_CHECKING:
    from controller import Controller
    from player import Player
    from point import Point
    from power_up import PowerUp


class Deserialize:
    playerController: Controller
    ghost1: Controller
    ghost2: Controller
    ghost3: Controller
    ghost4: Controller

    def __init__(self, playerController: Controller, ghost1: Controller, ghost2: Controller, ghost3: Controller, ghost4: Controller):
        self.playerController = playerController
        self.ghost1 = ghost1
        self.ghost2 = ghost2
        self.ghost3 = ghost3
        self.ghost4 = ghost4

    def deserialize(self, code: EntityDictionary):
        from player import Player
        from point import Point
        from power_up import PowerUp

        entityCode = EntityDictionary(code)


        if entityCode == EntityDictionary.WALL:
            return Wall()
        if entityCode == EntityDictionary.POINT:
            return Point()
        if entityCode == EntityDictionary.POWER_UP:
            return PowerUp()
        if entityCode == EntityDictionary.PLAYER_UP:
            return Player(self.playerController, Direction.UP)
        if entityCode == EntityDictionary.PLAYER_LEFT:
            return Player(self.playerController, Direction.LEFT)
        if entityCode == EntityDictionary.PLAYER_DOWN:
            return Player(self.playerController, Direction.DOWN)
        if entityCode == EntityDictionary.PLAYER_RIGHT:
            return Player(self.playerController, Direction.RIGHT)
        if entityCode == EntityDictionary.ENEMY_UP:
            return Enemy(self.ghost1, Direction.UP)
        if entityCode == EntityDictionary.ENEMY_LEFT:
            return Enemy(self.ghost1, Direction.LEFT)
        if entityCode == EntityDictionary.ENEMY_DOWN:
            return Enemy(self.ghost1, Direction.DOWN)
        if entityCode == EntityDictionary.ENEMY_RIGHT:
            return Enemy(self.ghost1, Direction.RIGHT)
