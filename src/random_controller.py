import random

from controller import Controller
from direction import Direction
from world import World


class RandomController(Controller):
    direction: Direction = None
    timerMax: int = 60
    timer: int = 0

    def update(self, world: World):
        self.timer += 1

        if self.timer == self.timerMax:
            self.direction = Direction(random.randint(0, 3))
            self.timer = 0
