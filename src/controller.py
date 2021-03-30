from abc import ABC, abstractmethod
from world import World


class Controller(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, world: World):
        pass
