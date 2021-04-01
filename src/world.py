import array
import types
import time as time
from entity import Entity
from actor import Actor
from world_position import WorldPosition
from direction import Direction

Row = list[Entity]
Grid = list[Row]


class World:
    size: (int, int)
    grid: Grid
    actors: list[Actor]

    def __init__(self, size):
        (x, y) = size
        self.grid = [[None]*x]*y
        pass

    def update(self, deltaTime: float):
        pass

    def addActor(self, actor: Actor):
        self.actors.append(actor)

    def putEntity(self, entity: Entity, pos: WorldPosition):
        self.grid[pos.x][pos.y] = entity

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