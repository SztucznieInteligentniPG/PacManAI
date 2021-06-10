from __future__ import annotations
import random
from typing import TYPE_CHECKING

from controller import Controller
from direction import Direction
if TYPE_CHECKING:
    from enemy import Enemy
    from player import Player
    from vector2 import Vector2Int, Vector2Float
    from world import World

class BlinkieController(Controller):
    direction: Direction = None
    position: Vector2Int
    tickRate: int
    timer = 0
    pacman: Player
    ghost: Enemy
    def __init__(self, tickRate: int):
        self.tickRate = tickRate

    def setGhost(self,ghost:Enemy, world: World):
        self.ghost = ghost

    def update(self, world: World):
        from blockade import Blockade
        from game_state import GameState
        from vector2 import Vector2Int
        from wall import Wall

        self.timer += 1

        if self.timer >= self.tickRate:
            self.timer = 0
            self.pacman = world.getPacman()
            grandPosition = world.getPositionInDirection(self.ghost.worldPosition, self.ghost.direction)
            obstacles = world.getEntities(grandPosition)
            point = 0
            for obstacle in obstacles:
                if isinstance(obstacle, Wall):
                    grandPosition = self.ghost.position
            right = world.getPositionInDirection(grandPosition, Direction.RIGHT)
            up = world.getPositionInDirection(grandPosition, Direction.UP)
            left = world.getPositionInDirection(grandPosition, Direction.LEFT)
            down = world.getPositionInDirection(grandPosition, Direction.DOWN)
            target = self.pacman.worldPosition
            obstacles = world.getEntities(self.ghost.worldPosition)
            for obstacle in obstacles:
                if isinstance(obstacle, Blockade):
                    target =  Vector2Int(8,5)
            positions = [right, up, left, down]
            points = []
            if world.gameState == GameState.RUNNING:
                for position in positions:
                    obstacles = world.getEntities(position)
                    point = 0
                    for obstacle in obstacles:
                        if isinstance(obstacle,Wall):
                            point = 10000
                    point += world.countDistance(target,position)
                    points.append(point)
                direction_index = points.index(min(points))
                self.direction = Direction(direction_index)

            if world.gameState == GameState.RUNNING_CHAOS:
                for position in positions:
                    obstacles = world.getEntities(position)
                    point = 0
                    for obstacle in obstacles:
                        if isinstance(obstacle,Wall):
                            point = 10000
                    point += world.countDistance(Vector2Int(20,0),position)
                    points.append(point)
                direction_index = points.index(min(points))
                self.direction = Direction(direction_index)

            if world.gameState == GameState.PSYCHODELIC:
                self.direction = Direction(random.randint(0, 3))

