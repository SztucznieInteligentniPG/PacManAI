from __future__ import annotations
from typing import TYPE_CHECKING

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




