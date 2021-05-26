from random import Random

from controller import Controller
from direction import Direction
from world import World


class RandomController(Controller):
    direction: Direction = None
    tickRate: int
    timer = 0
    random: Random

    def __init__(self, tickRate: int, seed: int):
        self.tickRate = tickRate
        self.random = Random() if seed is None else Random(seed)

    def update(self, world: World):
        self.timer += 1

        if self.timer >= self.tickRate:
            self.direction = Direction(self.random.randint(0, 3))
            self.timer = 0
