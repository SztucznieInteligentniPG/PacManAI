from __future__ import annotations
from typing import TYPE_CHECKING

from direction import Direction
from world_position import WorldPosition

if TYPE_CHECKING:
    from actor import Actor
    from entity import Entity
    Row = list[Entity]
    Grid = list[Row]


class World:
    size: WorldPosition
    grid: Grid
    actors: list[Actor]
    time: float
    score: int

    def __init__(self, size: WorldPosition):
        self.size = size
        self.grid = [[None for i in range(size.y)] for j in range(size.x)]
        pass

    def update(self, deltaTime: float):
        for actor in self.actors:
            actor.update(self, deltaTime)
        self.time += deltaTime

    def addActor(self, actor: Actor):
        self.actors.append(actor)

    def putEntity(self, entity: Entity, position: WorldPosition):
        self.grid[position.x][position.y] = entity
        entity.setPosition(position)
        entity.worldPosition = position

    def getEntity(self, position: WorldPosition) -> Entity:
        return self.grid[position.x][position.y]

    def removeEntity(self, entity: Entity):
        del self.grid[entity.worldPosition.x][entity.worldPosition.y]
        entity.worldPosition = None

    def moveEntity(self, entity: Entity, position: WorldPosition):
        self.removeEntity(entity)
        self.putEntity(entity, position)

    def getPositionInDirection(self, position: WorldPosition, direction: Direction) -> WorldPosition:
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

        return WorldPosition(destinationX, destinationY)
