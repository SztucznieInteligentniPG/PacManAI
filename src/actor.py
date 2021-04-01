from abc import ABC, abstractmethod
from entity import Entity
from controller import Controller


class Actor(Entity, ABC):
    controller: Controller

    def __init__(self, controller, position, state):
        super().__init__(position, state)
        self.controller = controller

    @abstractmethod
    def update(self, world, deltaTime: float):
        from world import World
        pass
