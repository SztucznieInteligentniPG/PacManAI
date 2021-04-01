import array
import types
import time as time
from entity import Entity
from actor import Actor
from position import Position

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

    def putEntity(self, entity: Entity, pos: Position):
        self.grid[pos.x][pos.y] = entity




