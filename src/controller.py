from abc import ABC, abstractmethod

from direction import Direction
from world import World


class Controller(ABC):
    direction: Direction = None

    @abstractmethod
    def update(self, world: World, deltaTime: float):
        pass
