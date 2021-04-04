from __future__ import annotations
from typing import TYPE_CHECKING

from direction import Direction
from vector2 import Vector2Int

if TYPE_CHECKING:
    from actor import Actor
    from entity import Entity
    Place = list[Entity]
    Row = list[Place]
    Grid = list[Row]


class World:
    size: Vector2Int
    grid: Grid
    actors: list[Actor]
    time: float
    score: int

    def __init__(self, size: Vector2Int):
        self.size = size
        self.grid = [[[] for i in range(size.y)] for j in range(size.x)]
        self.actors = []
        self.time = 0.0
        self.score = 0

    def update(self, deltaTime: float):
        for actor in self.actors:
            actor.update(self, deltaTime)
        self.time += deltaTime

    def putActor(self, actor: Actor, position: Vector2Int):
        self.actors.append(actor)
        self.putEntity(actor, position)

    def removeActor(self, actor: Actor):
        if self.actors.__contains__(actor):
            self.actors.remove(actor)
        self.removeEntity(actor)

    def putEntity(self, entity: Entity, position: Vector2Int):
        self.grid[position.x][position.y].append(entity)
        entity.setPosition(position)
        entity.worldPosition = position

    def getEntity(self, position: Vector2Int) -> list[Entity]:
        return self.grid[position.x][position.y]

    def removeEntity(self, entity: Entity):
        if entity.worldPosition is not None:
            self.grid[entity.worldPosition.x][entity.worldPosition.y].remove(entity)
            entity.worldPosition = None

    def moveEntity(self, entity: Entity, position: Vector2Int):
        self.removeEntity(entity)
        self.putEntity(entity, position)

    def getPositionInDirection(self, position: Vector2Int, direction: Direction) -> Vector2Int:
        destinationX: int = position.x
        destinationY: int = position.y
        
        if direction is Direction.LEFT:
            destinationX -= 1
        elif direction is Direction.RIGHT:
            destinationX += 1

        if direction is Direction.UP:
            destinationY -= 1
        elif direction is Direction.DOWN:
            destinationY += 1

        if destinationX < 0:
            destinationX = 0
        elif destinationX >= self.size.x:
            destinationX = self.size.x - 1

        if destinationY < 0:
            destinationY = 0
        elif destinationY >= self.size.y:
            destinationY = self.size.y - 1

        return Vector2Int(destinationX, destinationY)
