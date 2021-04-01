import array
import types
from entity import Entity
from actor import Actor
from position import Position
from world_position import WorldPosition

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

    def putEntity(self, entity: Entity, pos: WorldPosition):
        self.grid[pos.x][pos.y] = entity

    def getEntity(self, pos: WorldPosition):
        return self.grid[pos.x][pos.y]

    def removeEntity(self, pos: WorldPosition):
        del self.grid[pos.x][pos.y]




