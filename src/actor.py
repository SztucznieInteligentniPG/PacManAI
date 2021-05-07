from __future__ import annotations
from abc import ABC, abstractmethod
import math
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
    spawn: Vector2Int = None

    def __init__(self, controller: Controller):
        super().__init__()
        self.controller = controller

    def destroy(self, world: World):
        world.removeActor(self)

    def setPosition(self, worldPosition: Vector2Int):
        self.worldPosition = worldPosition
        self.position = Vector2Float(worldPosition.x, worldPosition.y)

    def checkCollision(self, other: Entity):
        selfLeft = self.position.x - self.collisionBox.x / 2
        selfRight = self.position.x + self.collisionBox.x / 2
        selfUp = self.position.y - self.collisionBox.y / 2
        selfDown = self.position.y + self.collisionBox.y / 2
        if isinstance(other, Actor):
            otherLeft = other.position.x - other.collisionBox.x / 2
            otherRight = other.position.x + other.collisionBox.x / 2
            otherUp = other.position.y - other.collisionBox.y / 2
            otherDown = other.position.y + other.collisionBox.y / 2
        else:
            otherLeft = other.worldPosition.x - other.collisionBox.x / 2
            otherRight = other.worldPosition.x + other.collisionBox.x / 2
            otherUp = other.worldPosition.y - other.collisionBox.y / 2
            otherDown = other.worldPosition.y + other.collisionBox.y / 2

        if (((selfLeft <= otherLeft <= selfRight) or (selfRight >= otherRight >= selfLeft)) and
                ((selfUp <= otherUp <= selfDown) or (selfDown >= otherDown >= selfUp))):
            return True
        return False

    def checkCollidingEntities(self, world: World) -> list[Entity]:
        mask = [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]
        x = self.worldPosition.x - 2
        y = self.worldPosition.y - 2
        entityList = []
        for i in range(5):
            if (x + i) >= world.size.x:
                break
            for j in range(5):
                if (y + j) >= world.size.y:
                    break
                if mask[j][i] == 1 and x + i >= 0 and y + j >= 0:
                    entities = world.getEntities(Vector2Int(x + i, y + j))

                    for entity in entities:
                        if self.checkCollision(entity):
                            entityList.append(entity)
        return entityList

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


    def isWalkable(self, world: World, position: Vector2Int) -> bool:
        return True

    def maximumSafeUpdateTime(self) -> float:
        return math.inf

    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass

    def wakeUp(self):
        pass

    def respawn(self, world: World):
        pass
