from __future__ import annotations
from typing import TYPE_CHECKING

from direction import Direction
from vector2 import Vector2Int
from gameState import GameState

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
    timeLimit: float
    timeToChangeMode: float
    pointsRemaining: int
    lives: int
    gameState: GameState

    def __init__(self, size: Vector2Int):
        self.size = size

        self.grid = [[[] for _ in range(size.y)] for _ in range(size.x)]
        self.actors = []
        self.time = 0.0
        self.score = 0
        self.timeLimit = 50.0
        self.timeToChangeMode = 15.0
        self.pointsRemaining = 0
        self.gameState = GameState.RUNNING

    def update(self, deltaTime: float):
        if not self.gameState == GameState.LOST or self.gameState == GameState.WON:
            for actor in self.actors:
                actor.update(self, deltaTime)
            self.time += deltaTime
            if self.time >= self.timeLimit:
                self.gameState = GameState.LOST
            self.timeToChangeMode -= deltaTime
            if self.timeToChangeMode <= 0:
                if self.gameState == GameState.RUNNING:
                    self.gameState = GameState.RUNNING_CHAOS
                else:
                    self.gameState = GameState.RUNNING
                print(self.gameState)
                self.timeToChangeMode = 15.0

    def putActor(self, actor: Actor, position: Vector2Int):
        self.actors.append(actor)
        self.putEntity(actor, position)

    def removeActor(self, actor: Actor):
        if self.actors.__contains__(actor):
            self.actors.remove(actor)
        self.removeEntity(actor)

    def putEntity(self, entity: Entity, position: Vector2Int):
        from point import Point
        self.grid[position.x][position.y].append(entity)
        entity.setPosition(position)
        entity.worldPosition = position
        if isinstance(entity, Point):
            self.pointsRemaining += 1

    def getEntities(self, position: Vector2Int) -> list[Entity]:
        return self.grid[position.x][position.y]

    def addScore(self, score: int):
        self.score += score
        print('Wynik:', self.score)

    def getKilled(self):
        self.lives -= 1
        if self.lives == 0:
            self.gameState = GameState.LOST

    def hasEntityOfType(self, position: Vector2Int, entityType: type) -> bool:
        result = False
        for entity in self.getEntities(position):
            if isinstance(entity, entityType):
                result = True
        return result

    def removeEntity(self, entity: Entity):
        from point import Point
        if entity.worldPosition is not None:
            self.grid[entity.worldPosition.x][entity.worldPosition.y].remove(entity)
        entity.worldPosition = None
        if isinstance(entity, Point):
            self.pointsRemaining -= 1
            if self.pointsRemaining == 0:
                self.gameState = GameState.WON


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
