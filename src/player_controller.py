import pygame

from controller import Controller
from direction import Direction
from world import World


class PlayerController(Controller):
    direction: Direction = None

    def update(self, world: World):
        pass

    def updateKeys(self, keys: list):
        if keys.__contains__(pygame.K_UP):
            self.direction = Direction.UP
        elif keys.__contains__(pygame.K_DOWN):
            self.direction = Direction.DOWN
        elif keys.__contains__(pygame.K_LEFT):
            self.direction = Direction.LEFT
        elif keys.__contains__(pygame.K_RIGHT):
            self.direction = Direction.RIGHT
        else:
            self.direction = None
