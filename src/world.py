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
    size: (int, int)
    grid: Grid
    actors: list[Actor]
    time: float
    score: int

    def __init__(self, size):
        (x, y) = size
        self.grid = [[None]*x]*y
        pass

    def update(self, deltaTime: float):
        for actor in self.actors:
            actor.update(self, deltaTime)
        self.time += deltaTime

    def addActor(self, actor: Actor):
        self.actors.append(actor)

    def putEntity(self, entity: Entity, position: WorldPosition):
        self.grid[position.x][position.y] = entity

    def getEntity(self, position: WorldPosition):
        return self.grid[position.x][position.y]

    def removeEntity(self, position: WorldPosition):
        del self.grid[position.x][position.y]

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
        elif destinationX >= self.size[0]:
            destinationX = self.size[0] - 1

        if destinationY < 0:
            destinationY = 0
        elif destinationY >= self.size[1]:
            destinationY = self.size[1] - 1

        return WorldPosition(destinationX, destinationY)