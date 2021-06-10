from __future__ import annotations

import copy
import json
import math
import numpy as np
from typing import TYPE_CHECKING

from blockade import Blockade
from direction import Direction
from game_state import GameState
from reward import Reward
from vector2 import Vector2Int
from statistic import Statistic

if TYPE_CHECKING:
    from actor import Actor
    from blinkie_controller import BlinkieController
    from deserialize import Deserialize
    from enemy import Enemy
    from entity import Entity
    from player import Player
    from point import Point
    from power_up import PowerUp

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
    deserialize: Deserialize
    respawning: Player
    log: bool
    train: bool
    statistic: Statistic
    generationNumber: int
    individualNumber: int

    def __init__(self, size: Vector2Int, deserialize: Deserialize, log=False, train=False):
        self.size = size

        self.grid = [[[] for _ in range(size.y)] for _ in range(size.x)]
        self.actors = []
        self.time = 0.0
        self.score = 0
        self.timeLimit = 90.0
        self.timeToChangeMode = 15.0
        self.pointsRemaining = 0
        self.gameState = GameState.RUNNING
        self.lives = 3
        self.deserialize = deserialize
        self.log = log
        self.train = train
        self.statistic = Statistic()

    def update(self, tickRate: int):
        if self.gameState is not GameState.LOST and self.gameState is not GameState.WON:
            self.time += 1 / tickRate
            if self.time >= self.timeLimit:
                self.gameState = GameState.LOST
            self.timeToChangeMode -= 1 / tickRate

            if self.timeToChangeMode <= 0:
                if self.gameState == GameState.RUNNING:
                    self.gameState = GameState.RUNNING_CHAOS
                else:
                    if self.gameState == GameState.RESPAWNING:
                        for actor in self.actors:
                            actor.wakeUp()
                    self.gameState = GameState.RUNNING

                if self.log:
                    print(self.gameState)
                self.timeToChangeMode = 15.0

            for actor in self.actors:
                actor.update(self, tickRate)

    def putActor(self, actor: Actor, position: Vector2Int):
        self.actors.append(actor)
        self.putEntity(actor, position)

    def getPacman(self):
        from player import Player
        for entity in self.actors:
            if isinstance(entity, Player):
                return entity
    def getBlinkiePosition(self):
        from blinkie_controller import BlinkieController
        from enemy import Enemy
        for entity in self.actors:
            if isinstance(entity, Enemy):
                if isinstance(entity.controller, BlinkieController):
                    return entity.worldPosition

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

    def countDistance(self, positionA: Vector2Int, positionB: Vector2Int):
        a = copy.copy(positionA)
        b = copy.copy(positionB)
        sum = (b.x-a.x)**2+(b.y-a.y)**2
        return sum

    def getEntities(self, position: Vector2Int) -> list[Entity]:
        return self.grid[position.x][position.y]

    def addScore(self, score: Reward, multiplier=1.0):
        value = score.value*multiplier
        self.score += value
        if self.train:
            self.statistic.addPoint(value, score)
        if self.log:
            print('Wynik:', self.score)

    def getKilled(self, player: Player):
        self.lives -= 1
        self.addScore(Reward.DEATH)
        if self.lives <= 0:
            self.gameState = GameState.LOST
            self.statistic.setTime(self.time)
        else:
            self.respawning = player
            self.removeActor(player)
            for enemy in self.actors:
                enemy.respawn(self)
            self.respawning.respawn(self)
            self.gameState = GameState.RESPAWNING
            self.timeToChangeMode = 3.0

    def hasEntityOfType(self, position: Vector2Int, entityType: type) -> bool:
        result = False
        for entity in self.getEntities(position):
            if isinstance(entity, entityType):
                result = True
        return result

    def removeEntity(self, entity: Entity):
        from point import Point
        from power_up import PowerUp
        if entity.worldPosition is not None:
            self.grid[entity.worldPosition.x][entity.worldPosition.y].remove(entity)
        entity.worldPosition = None
        if isinstance(entity, Point):
            self.pointsRemaining -= 1
            if self.pointsRemaining == 0:
                self.gameState = GameState.WON
                self.addScore(Reward.TIME_REMAINING, (self.timeLimit - self.time))
                self.statistic.setTime(self.time)
        if isinstance(entity, PowerUp):
            self.gameState = GameState.PSYCHODELIC
            if self.log:
                print(self.gameState)
            self.timeToChangeMode = 10.0

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

    def loadGrid(self):
        from actor import Actor
        from blinkie_controller import BlinkieController
        from enemy import Enemy
        f = open("map.txt", "r")
        data = json.load(f)
        grid = data["grid"]

        for i in range(self.size.y):
            for j in range(self.size.x):
                place = grid[i][j]
                for entityCode in place:
                    entity = self.deserialize.deserialize(entityCode)
                    if isinstance(entity, Enemy):
                        entity.controller.setGhost(entity,self)
                    if isinstance(entity, Actor):
                        self.putActor(entity, Vector2Int(j, i))
                    elif isinstance(entity, Blockade):
                        self.putEntity(entity, Vector2Int(j, i))
                    elif entity is not None:
                        self.putEntity(entity, Vector2Int(j, i))

    def tickRate(self) -> int:
        tickRate: int = 1

        for actor in self.actors:
            tickRate = int(tickRate * actor.tickRate() / math.gcd(tickRate, actor.tickRate()))

        return tickRate

    def generateTensor(self):
        from enemy import Enemy
        from player import Player
        from point import Point
        from power_up import PowerUp
        from wall import Wall
        tensor = np.zeros((1, 19, 19, 10))
        for x, column in enumerate(self.grid):
            for y, place in enumerate(column):
                for entity in place:
                    if isinstance(entity, Wall):
                        tensor[0][x][y][0] = 1
                    if isinstance(entity, Blockade):
                        tensor[0][x][y][1] = 1
                    if isinstance(entity, Point):
                        tensor[0][x][y][2] = 1
                    if isinstance(entity, PowerUp):
                        tensor[0][x][y][3] = 1
                    if isinstance(entity, Player):
                        tensor[0][x][y][4] = 1
                    if isinstance(entity, Enemy):
                        if entity.isFearful:
                            tensor[0][x][y][9] = 1
                        else:
                            tensor[0][x][y][5 + entity.id] = 1

        return tensor
