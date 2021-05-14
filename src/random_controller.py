from random import Random

from controller import Controller
from direction import Direction
from world import World


class RandomController(Controller):
    direction: Direction = None
    timerMax = 1 / 3
    timer = 0
    random: Random

    def __init__(self, seed: int):
        self.random = Random() if seed is None else Random(seed)

    def update(self, world: World, deltaTime: float):
        self.timer += deltaTime

        if self.timer >= self.timerMax:
            self.direction = Direction(self.random.randint(0, 3))
            self.timer = 0
