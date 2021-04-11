from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from controller import Controller
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

    def checkCollision(self, other: Entity):
        size = 16
        selfLeft = self.position.x*size*2 - self.collisionBox.x * size
        selfRight = self.position.x*size*2 + self.collisionBox.x * size
        selfUp = self.position.y*size*2 - self.collisionBox.y * size
        selfDown = self.position.y*size*2 + self.collisionBox.y * size
        if isinstance(other, Actor):
            otherLeft = other.position.x*size*2 - other.collisionBox.x * size
            otherRight = other.position.x*size*2 + other.collisionBox.x * size
            otherUp = other.position.y*size*2 - other.collisionBox.y * size
            otherDown = other.position.y*size*2 + other.collisionBox.y * size
        else:
            otherLeft = other.worldPosition.x*size*2 - other.collisionBox.x * size
            otherRight = other.worldPosition.x*size*2 + other.collisionBox.x * size
            otherUp = other.worldPosition.y*size*2 - other.collisionBox.y * size
            otherDown = other.worldPosition.y*size*2 + other.collisionBox.y * size

        if (selfLeft < otherLeft < selfRight) or (selfRight > otherRight > selfLeft):
            if (selfUp < otherUp < selfDown) or (selfDown > otherDown > selfUp):
                return True
        return False

    def checkCollidingEntities(self, world: World) -> list[Entity]:
        mask = [[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0]]
        x = self.worldPosition.x - 2
        y = self.worldPosition.y - 2
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        entityList = []
        for i in range(5):
            if (x + i) >= world.size.x:
                break
            for j in range(5):
                if (y + j) >= world.size.y:
                    break
                if mask[j][i] == 1:
                    entities = world.getEntities(Vector2Int(x+i, y+j))
                    for entity in entities:
                        if self.checkCollision(entity):
                            entityList.append(entity)
        return entityList



    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass
