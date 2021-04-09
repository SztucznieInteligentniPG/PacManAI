from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from controller import Controller
from direction import Direction
from entity import Entity
from vector2 import Vector2Int, Vector2Float

if TYPE_CHECKING:
    from world import World


class Actor(Entity, ABC):
    controller: Controller
    position: Vector2Float = None

    def __init__(self, controller: Controller):
        super().__init__()
        self.controller = controller

    def destroy(self, world: World):
        world.removeActor(self)

    def setPosition(self, worldPosition: Vector2Int):
        self.worldPosition = worldPosition
        self.position = Vector2Float(worldPosition.x, worldPosition.y)

    def getDistanceTo(self, worldPosition: Vector2Int) -> float:
        return abs(self.position.x - worldPosition.x) + abs(self.position.y - worldPosition.y)

    def moveInDirection(self, direction: Direction, distance: float):
        if direction is Direction.UP:
            self.position.y -= distance
        elif direction is Direction.DOWN:
            self.position.y += distance
        elif direction is Direction.RIGHT:
            self.position.x += distance
        elif direction is Direction.LEFT:
            self.position.x -= distance

    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass
