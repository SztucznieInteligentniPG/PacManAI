from abc import ABC, abstractmethod


class Controller(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, world):
        from world import World
        pass
