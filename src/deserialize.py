from __future__ import annotations
from typing import TYPE_CHECKING

from blockade import Blockade
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
    enemyControllers: list[Controller]
    cooldowns: list[float] = [3.0, 6.0, 9.0, 12.0]

    def __init__(self, playerController: Controller, ghost1: Controller, ghost2: Controller, ghost3: Controller, ghost4: Controller):
        self.playerController = playerController
        self.enemyControllers = [ghost1, ghost2, ghost3, ghost4]

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
            return Enemy(self.enemyControllers.pop(0), Direction.UP, self.cooldowns.pop(0))
        if entityCode == EntityDictionary.ENEMY_LEFT:
            return Enemy(self.enemyControllers.pop(0), Direction.LEFT, self.cooldowns.pop(0))
        if entityCode == EntityDictionary.ENEMY_DOWN:
            return Enemy(self.enemyControllers.pop(0), Direction.DOWN, self.cooldowns.pop(0))
        if entityCode == EntityDictionary.ENEMY_RIGHT:
            return Enemy(self.enemyControllers.pop(0), Direction.RIGHT, self.cooldowns.pop(0))
        if entityCode == EntityDictionary.BLOCKADE:
            return Blockade()
