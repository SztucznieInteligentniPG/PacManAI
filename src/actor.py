from abc import ABC, abstractmethod
import time as time
from world import World
from entity import Entity
from controller import Controller


class Actor(Entity, ABC):
    controller: Controller

    def __init__(self, controller, position, state):
        super().__init__(position, state)
        self.controller = controller

    @abstractmethod
    def update(self, world: World, deltaTime: time.struct_time):
        pass
