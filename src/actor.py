from abc import ABC, abstractmethod
from world import World
from entity import Entity
from controller import Controller
from position import Position


class Actor(Entity, ABC):
    controller: Controller
    position: Position

    def __init__(self, worldPosition, position: Position, controller: Controller):
        super().__init__(worldPosition)
        self.controller = controller
        self.position = position

    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass
