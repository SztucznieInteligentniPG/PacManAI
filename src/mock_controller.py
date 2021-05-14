from controller import Controller
from direction import Direction
from world import World


class MockController(Controller):
    direction: Direction = None

    def __init__(self, direction: Direction):
        self.direction = direction

    def update(self, world: World, deltaTime: float):
        pass
